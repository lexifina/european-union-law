"""Read Cellar XHTML into a flat list of blocks: (class, text, ids), in document order."""
from __future__ import annotations

import html
import re
from html.parser import HTMLParser

BLOCK = {'p', 'div', 'td', 'th', 'tr', 'table', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'br', 'hr', 'dt', 'dd'}
SKIP = {'head', 'script', 'style'}


class Block:
    __slots__ = ('cls', 'text', 'ids', 'tag', 'depth')

    def __init__(self, cls, text, ids, tag, depth):
        self.cls, self.text, self.ids, self.tag, self.depth = cls, text, ids, tag, depth

    def __repr__(self):
        return f'<{self.tag}.{self.cls} {self.ids} {self.text[:60]!r}>'


class _P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out: list[Block] = []
        self.buf: list[str] = []
        self.stack: list[tuple[str, str, str]] = []   # tag, class, id
        self.skip = 0
        self.pending_ids: list[str] = []
        self.note = 0   # inside a footnote reference <span class="super"> / <a class="footnote">

    def _flush(self):
        t = ''.join(self.buf)
        self.buf = []
        t = norm(t)
        if t:
            cls = ''
            tag = ''
            for tg, c, _ in reversed(self.stack):
                if tg in BLOCK and tg not in ('table', 'tr'):
                    cls, tag = c, tg
                    break
            self.out.append(Block(cls, t, self.pending_ids, tag, len(self.stack)))
            self.pending_ids = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in SKIP:
            self.skip += 1
        if tag in BLOCK:
            self._flush()
        if a.get('id'):
            self.pending_ids = self.pending_ids + [a['id']]
        if tag == 'br':
            return
        if tag in ('img', 'col', 'meta', 'link', 'hr', 'input'):
            if tag == 'img' and a.get('alt') and not self.skip:
                self.buf.append(a['alt'])
            return
        if tag == 'a' and ((a.get('id') or '').startswith('ntc') or (a.get('href') or '').startswith('#ntr')):
            self.skip += 1
            self.stack.append(('a-note', '', ''))
            return
        self.stack.append((tag, a.get('class', '') or '', a.get('id', '') or ''))
        if tag == 'td':
            self.buf.append('')

    def handle_endtag(self, tag):
        if tag in SKIP:
            self.skip = max(0, self.skip - 1)
        if tag in BLOCK:
            self._flush()
        if tag == 'a' and self.stack and self.stack[-1][0] == 'a-note':
            self.stack.pop()
            self.skip = max(0, self.skip - 1)
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break
        if tag == 'td':
            self.buf.append(' ')

    def handle_data(self, data):
        if not self.skip:
            self.buf.append(data)


QUOTES = {'‘': "'", '’': "'", '‚': "'", '‛': "'", '′': "'",
          '“': "'", '”': "'", '„': "'", '«': "'", '»': "'", '"': "'",
          '–': '-', '—': '-', '‑': '-', '‐': '-', '−': '-',
          ' ': ' ', ' ': ' ', ' ': ' ', ' ': ' ', ' ': ' ', '​': '', '﻿': '',
          '­': ''}
_QT = str.maketrans(QUOTES)


def norm(t: str) -> str:
    t = html.unescape(t).translate(_QT)
    return re.sub(r'\s+', ' ', t).strip()


def blocks(raw: bytes) -> list[Block]:
    p = _P()
    p.feed(raw.decode('utf-8', errors='replace'))
    p._flush()
    return p.out
