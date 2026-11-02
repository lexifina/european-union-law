# European Union: law history in git

The law of the European Union as a git history: one file per article, one commit per amending act on the day its change took effect, and the act that made each change as the commit's author. `git blame` names the act behind every paragraph; `git log` lists every change to an article; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `eu/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `teu/` | Treaty on European Union (consolidated version) | 4 | From the entry into force of the Treaty of Lisbon (1 December 2009) to the 2016 consolidation, through the accession of Croatia (1 July 2013) |
| `tfeu/` | Treaty on the Functioning of the European Union (consolidated version) | 7 | From 1 December 2009 to the 2016 consolidation, through European Council Decisions 2010/718/EU (Saint-Barthélemy), 2011/199/EU (Article 136(3), the stability mechanism), 2012/419/EU (Mayotte) and the accession of Croatia |
| `charter/` | Charter of Fundamental Rights of the European Union | 1 | As proclaimed on 12 December 2007, binding from 1 December 2009; unchanged since |

Every text comes from the Publications Office of the European Union (EUR-Lex and its Cellar repository). The Treaties are the consolidated versions published in the Official Journal C series (2008, 2012 and 2016). The per-act `README.md` in each folder lists every article, how often it changed and when.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did Article 136 TFEU say on 30 April 2013? | `python tools/on.py 2013-04-30 tfeu 136` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2013-04-30T23:59:59Z" main -- tfeu/art-136.md):tfeu/art-136.md` |
| Which act wrote each paragraph of Article 355 TFEU? | `git blame tfeu/art-355.md` |
| Every change to Article 52 TEU, word by word | `git log -p --word-diff teu/art-052.md` |
| Every act in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one act changed | `git show law/decision-2011-199-eu` (tags `law/<key>` mark each commit) |
| The whole Treaty on a date | `python tools/on.py 2012-06-01 tfeu` |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Europe/Brussels, on the day the change took effect**. The act's own date and its publication date are trailers, and the in-force day is in `In-force:`, which the tools read.
- **The Treaties** start on 1 December 2009, the day the Treaty of Lisbon entered into force, with the consolidated versions the Official Journal published on 9 May 2008 (OJ C 115). Each later amendment is dated by the day it entered into force: European Council Decision 2010/718/EU on 1 January 2012, Decision 2011/199/EU on 1 May 2013, the Treaty of Accession of Croatia on 1 July 2013 and Decision 2012/419/EU on 1 January 2014.
- **Republications.** The Official Journal republished the consolidated Treaties on 26 October 2012 (OJ C 326) and 7 June 2016 (OJ C 202). Where a republication differs from the one before in words no amending act in this record explains (corrections of wording, punctuation, subheadings the 2016 text does not print), the difference is a commit on the day of the republication, credited to the publisher and marked unexplained.
- **The Charter** was proclaimed on 12 December 2007 and has the same legal value as the Treaties from 1 December 2009 (Article 6(1) TEU); its history starts on that day.

## How it is checked

- Every version of every act is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- Where an amendment is applied to an earlier consolidation by hand (Saint-Barthélemy and Mayotte in Articles 349 and 355 TFEU), the result must equal the wording of the later consolidation, or the build stops.
- Health checks: no merge commits on `main`, commit dates never go backwards, nothing dated in the future, and every commit's trailers parse with `git interpret-trailers --parse`.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the act that made the change, with an e-mail address that cannot exist (`decision-2011-199-eu@publications.europa.eu.invalid`), so `git blame` and `git log --author` name it. The committer is always Lexifina.

- **The first commit of each Treaty** is "oldest version available", credited to the publisher: it is the text as amended by the Treaty of Lisbon, not the Treaties as first signed.
- Blame credits whole lines (one paragraph or point per line). Use `git log -p --word-diff` to see exactly which words each act changed.

## What it does not show

- **The Treaties before 1 December 2009** (the EEC Treaty of 1957, the Treaties of Maastricht, Amsterdam and Nice): not yet in this record.
- **Protocols, annexes and declarations** annexed to the Treaties, and the headings of parts, titles, chapters and sections: not yet in this record; only the preamble and the articles are.
- **Editorial matter.** The consolidated Treaties print a reference under many articles ("(ex Article 2 TEU)") and footnotes; neither is law text, and neither is in the files.
- **Court rulings.** The Court of Justice can annul acts of the institutions, but no ruling strikes words from the Treaties.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

The source is the Publications Office's Cellar repository: its SPARQL service lists the acts and their consolidated versions, and each document is read as English XHTML. Lexifina's code reads the documents into `corpus.json`, and the shared builder `tools/build.py` writes the history with `git fast-import`.

## Sources

| Source | Kind | Past versions | Names the amending act | Bulk | Notes |
| --- | --- | --- | --- | --- | --- |
| [Cellar](https://op.europa.eu/en/web/cellar), Publications Office of the European Union | Official repository behind EUR-Lex | every consolidated version, and the consolidated Treaties of 2008, 2012 and 2016 | yes, in each consolidated version's list of amending acts | SPARQL and per-document XHTML | Used: the text of every version |
| [EUR-Lex](https://eur-lex.europa.eu) | Official publisher's site | yes | yes | no | Linked for each act; not read |

## Licence

The texts are © European Union, https://eur-lex.europa.eu, 1998-2026, reused under Commission Decision 2011/833/EU on the reuse of Commission documents. Only the Official Journal of the European Union is authentic; consolidated texts are a documentation tool with no legal effect. The arrangement, tables, commit messages and tools are by Lexifina, under the terms in `LICENSE`.

This repository is not legal advice and not an official publication.
