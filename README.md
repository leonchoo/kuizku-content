# KuizKu Content

**Public source repository for KuizKu original question banks, blueprints, QA scripts, and Apps Script.**

This repo contains the *source* content that drives the KuizKu Android app. Published encrypted runtime banks are emitted from this content via a separate publishing pipeline (not in this repo).

---

## Repository layout

```
kuizku-content/
├── banks/                          # Production canonical question banks
│   ├── primary/
│   │   ├── sk/
│   │   │   ├── bm/                 # SK Primary Bahasa Melayu
│   │   │   └── english/            # SK Primary English
│   │   ├── sjkc/                   # SJKC Primary (empty placeholder)
│   │   └── international/          # International Primary (empty placeholder)
│   └── secondary/
│       ├── sk/bm/t1/               # SK Secondary Bahasa Melayu T1
│       ├── sjkc/                   # SJKC Secondary (empty placeholder)
│       └── international/          # International Secondary (empty placeholder)
├── blueprints/                     # Per-combination planning documents
├── coverage/                       # Coverage matrix + selection reports
├── docs/                           # Phase 10 implementation docs
├── forensic/                       # LOCKED audit sources (do not modify)
├── legacy/                         # Pre-multi-track pilot content
├── tools/                          # Generator + QA + utility scripts
│   ├── generators/
│   ├── qa/
│   ├── utils/
│   └── tests/
└── apps-script/                    # Google Apps Script backend
    ├── backend_v6.gs               # Current production
    └── .clasp.json                 # clasp configuration
```

---

## Source policy

All committed banks and question items MUST have:
- `contentOrigin: "ORIGINAL"` — self-authored content
- `licenseStatus: "self_authored"` — owned by KuizKu authors
- `commercialReuseAllowed: true` — permitted for distribution
- `examYear: null` — not from any specific exam

Each item is tagged with a `source_tag` of one of:
- `CURRICULUM_DERIVED` — derived from Malaysian KSSR/KSSR_SJKC curriculum
- `INFERRED` — inferred from typical Year/Tingkatan-level content
- `REFERENCE_DB_ANCHOR` — used a Reference DB file as style anchor only (no content lifted)

The actual Reference DB is **NEVER** included in this repo. Only provenance metadata (topic-only descriptions) is recorded.

---

## Apps Script

The Apps Script backend (`apps-script/backend_v6.gs`) is the runtime backend that receives question reports from the Android app. It writes to a Google Sheets database.

`apps-script/.clasp.json` contains only the public Apps Script project ID and a `rootDir` setting for clasp. No tokens, secrets, or credentials.

To deploy:
```bash
cd apps-script
clasp push
```

---

## Tooling

- `tools/generators/` — Python scripts that generate bank JSONs
- `tools/qa/` — Python scripts that run QA checks on bank JSONs
- `tools/utils/` — utility scripts (apply audit fixes, etc.)
- `tools/tests/` — internal test scripts

All tools are designed to be run on a local Python 3.11+ environment. No secrets or local paths are required.

---

## Privacy guarantees

This repo contains:
- ✅ No encryption keys (decryption secrets for runtime banks)
- ✅ No API keys, OAuth tokens, or service account credentials
- ✅ No personal email addresses
- ✅ No local filesystem paths
- ✅ No Reference DB content (only generic provenance metadata)
- ✅ No published runtime artifacts (encrypted banks live in a separate artifact store)

What lives elsewhere:
- Reference DB (private, local) — NOT in this repo
- Encryption keys (private, local) — used for publishing only
- Published encrypted banks — distributed via a separate artifact store (not this repo)

---

## Versioning

This repo follows semantic versioning principles:
- Bank JSONs are versioned by their `versionId` and `updatedAtMillis` fields
- Bank files may have a `.revN.json` suffix indicating generation revision
- Source-level changes are documented in `CHANGELOG.md`

---

## License

See `LICENSE` (CC BY 4.0 — free to use with attribution).

## Contact

This repo is maintained by the KuizKu team. For issues or contributions, please open a GitHub Issue.
