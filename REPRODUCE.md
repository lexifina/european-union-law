# How this repository was made (European Union)

This file is written by the build on 2026-11-02, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Publications Office of the European Union: Cellar (EUR-Lex documents) | <https://op.europa.eu/en/web/cellar> | 2026-11-02 | Commission Decision 2011/833/EU on the reuse of Commission documents; © European Union, 1998-2026 |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `teu` | Treaty on European Union (consolidated version) | 4 | 2009-12-01 to 2016-06-07 |
| `tfeu` | Treaty on the Functioning of the European Union (consolidated version) | 7 | 2009-12-01 to 2016-06-07 |
| `charter` | Charter of Fundamental Rights of the European Union | 1 | 2009-12-01 to 2009-12-01 |

The build made 11 commits:

| Commits | Kind |
| ---: | --- |
| 3 | first version of an act |
| 4 | one law on its in-force day |
| 4 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-02.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 10 laws in the record.
- 17 tags.

## Dates

Each commit is dated at noon (Europe/Brussels) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Article 297 TFEU: legislative acts, and regulations and directives addressed to all Member States, enter into force on the date specified in them or, in the absence thereof, on the twentieth day following that of their publication in the Official Journal https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12016E297

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `94be4e81ec55d721f7201b3bc28b7e924f043217eed4350d269e344539695531` (524188 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- The Treaty on European Union and the Treaty on the Functioning of the European Union start on 1 December 2009, the day the Treaty of Lisbon entered into force, with the consolidated versions published in OJ C 115 of 9 May 2008; earlier versions are not yet in this record, so the first version is credited to the publisher as the oldest version available.
- The Charter of Fundamental Rights starts on 1 December 2009 with the text proclaimed on 12 December 2007 (OJ C 303 of 14 December 2007), which Article 6(1) TEU gives the same legal value as the Treaties from that day. Its republications of 2012 and 2016 print the same articles.
- Only the preamble and the articles of each Treaty are recorded; the protocols, annexes and declarations annexed to the Treaties, and the headings of parts, titles, chapters and sections, are not yet in this record.
- The consolidated Treaties print an editorial reference under many articles ('(ex Article 2 TEU)') and footnote calls; both are left out of the text.
- The 2010 republication of the consolidated Treaties (OJ C 83 of 30 March 2010) is not available as text from the publisher and is not used.
- Saint-Barthélemy: European Council Decision 2010/718/EU changed its status from 1 January 2012; Articles 349 and 355(1) TFEU lose its name on that day, although the 2012 consolidation still prints it.
- Article 136(3) TFEU is added on 1 May 2013, the day European Council Decision 2011/199/EU entered into force, with the wording of the 2016 consolidation.
- The Treaty of Accession of Croatia entered into force on 1 July 2013; Articles 52 and 55 TEU and Article 64 TFEU take the wording of the 2016 consolidation on that day.
- Mayotte: European Council Decision 2012/419/EU changed its status from 1 January 2014; Articles 349 and 355(1) TFEU take the wording of the 2016 consolidation on that day.
- Differences between successive republications of the consolidated Treaties (2008, 2012, 2016) that no amending act in this record explains are dated by the day of the republication and credited to the publisher.
- Typesetting is normalised once: non-breaking spaces become spaces, double and typographic quotation marks become ', dashes become -, and a paragraph number or point letter printed on its own line is joined to its text.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none: no model output is used as legal text; a model (Claude) wrote the scripts.
