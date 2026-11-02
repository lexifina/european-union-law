"""Rewrite the act table in repo/README.md and the build line in repo/jurisdiction.json from the corpus parts."""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    acts = []
    for p in sorted((HERE / 'corpus.d').glob('*.json')):
        acts += json.loads(p.read_text(encoding='utf-8'))['acts']
    rows = []
    for a in acts:
        vs = a['versions']
        t = re.sub(r'^[0-9]{4}/[0-9]+/[A-Za-z]+: ', '', a['title'])
        start = ('as enacted, in force ' if a['first_law'] else 'oldest consolidated version available, ') + vs[0]['from']
        rows.append(f"| `{a['slug']}/` | {t} | {len(vs)} | {start}" + (f"; latest consolidated version {vs[-1]['from']}" if len(vs) > 1 else '') + ' |')
    p = HERE / 'repo' / 'README.md'
    s = p.read_text(encoding='utf-8')
    start = s.index('| `charter/` |')
    end = s.index('\n', start)
    nxt = s.index('\n\n', end)
    s = s[:end + 1] + '\n'.join(rows) + s[nxt:]
    p.write_text(s, encoding='utf-8', newline='\n')
    j = HERE / 'repo' / 'jurisdiction.json'
    d = json.loads(j.read_text(encoding='utf-8'))
    d['build'] = (f'built: TEU (2009-2016), TFEU (2009-2016), Charter of Fundamental Rights (2009), and {len(acts)} '
                  'regulations and directives with every EUR-Lex consolidated version (GDPR, DSA, DMA, AI Act, eIDAS, '
                  'Brussels I bis, Rome I and II, MiFID II, CRR, CRD, EMIR, VAT Directive, REACH and others)')
    j.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    print(len(rows), 'acts in README')


if __name__ == '__main__':
    main()
