# Research Repository – Claude Instructions

## Daily Science Update

- Commit and push daily science update PDFs directly to the `main` branch.
- Do **not** use feature branches for these reports.
- Commit message format: `daily science update: YYYY-MM-DD`
- Output path: `reports/YYYY-MM-DD_science_update.pdf`

## PDF Generation Workflow

Do **not** write a full Python script each time. Instead:

1. **Produce a JSON file** at `reports/YYYY-MM-DD_content.json` following the schema in `content_schema.json`.
2. **Run the builder** to generate the PDF:
   ```
   python science_report_builder.py reports/YYYY-MM-DD_content.json
   ```
3. **Commit both files** (JSON + PDF) and push to `main`.

The builder (`science_report_builder.py`) owns the design – never modify it as part of a daily update.

### JSON fields

| Field | Description |
|---|---|
| `date` | ISO date of the report day (yesterday), e.g. `"2026-04-19"` |
| `generated_date` | ISO date of today (when report is generated) |
| `footer_sources` | Comma-separated source list for the footer |
| `sections` | Array of topic sections (see `content_schema.json`) |

Each item in a section has: `title`, `body` (2–4 sentences), `relevance`, `source`.
