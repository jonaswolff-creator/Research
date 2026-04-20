#!/usr/bin/env python3
"""
Science Report Builder – invariant build logic.
Usage: python science_report_builder.py <content.json> [output.pdf]
If output path is omitted, it is derived from the date in the JSON:
  reports/YYYY-MM-DD_science_update.pdf
"""

import json
import os
import sys
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

GERMAN_MONTHS = {
    1: "Januar", 2: "Februar", 3: "März", 4: "April",
    5: "Mai", 6: "Juni", 7: "Juli", 8: "August",
    9: "September", 10: "Oktober", 11: "November", 12: "Dezember",
}


def format_date_german(iso_date: str) -> str:
    d = datetime.strptime(iso_date, "%Y-%m-%d")
    return f"{d.day}. {GERMAN_MONTHS[d.month]} {d.year}"


def build_pdf(output_path: str, content: dict) -> None:
    date_iso = content["date"]
    date_display = format_date_german(date_iso)
    generated_display = format_date_german(
        content.get("generated_date", datetime.today().strftime("%Y-%m-%d"))
    )
    footer_sources = content.get("footer_sources", "")

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    styles = getSampleStyleSheet()

    style_title = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontSize=18,
        leading=22,
        textColor=colors.HexColor("#1a1a2e"),
        spaceAfter=6,
        alignment=TA_CENTER,
    )
    style_subtitle = ParagraphStyle(
        "Subtitle",
        parent=styles["Normal"],
        fontSize=9,
        textColor=colors.HexColor("#555555"),
        spaceAfter=4,
        alignment=TA_CENTER,
    )
    style_section = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#16213e"),
        spaceBefore=12,
        spaceAfter=4,
        borderPad=2,
    )
    style_item_title = ParagraphStyle(
        "ItemTitle",
        parent=styles["Normal"],
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#0f3460"),
        spaceBefore=6,
        spaceAfter=2,
        fontName="Helvetica-Bold",
    )
    style_body = ParagraphStyle(
        "ItemBody",
        parent=styles["Normal"],
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#333333"),
        spaceAfter=2,
        alignment=TA_JUSTIFY,
    )
    style_relevance = ParagraphStyle(
        "ItemRelevance",
        parent=styles["Normal"],
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#1a6b1a"),
        spaceAfter=1,
        fontName="Helvetica-Oblique",
    )
    style_source = ParagraphStyle(
        "ItemSource",
        parent=styles["Normal"],
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#888888"),
        spaceAfter=4,
    )
    style_footer = ParagraphStyle(
        "Footer",
        parent=styles["Normal"],
        fontSize=7,
        textColor=colors.HexColor("#aaaaaa"),
        alignment=TA_CENTER,
    )

    story = []

    story.append(Paragraph(f"Wissenschafts-Update - {date_iso}", style_title))
    story.append(Paragraph(
        f"Tägliche Übersicht wissenschaftlicher &amp; technologischer Entwicklungen"
        f" | Zeitraum: {date_display}, 00:00–23:59 UTC",
        style_subtitle,
    ))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1a1a2e"), spaceAfter=8))

    for section in content["sections"]:
        story.append(Paragraph(section["heading"], style_section))
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#aaaaaa"), spaceAfter=4))

        for item in section["items"]:
            story.append(Paragraph(f"• {item['title']}", style_item_title))
            story.append(Paragraph(item["body"], style_body))
            story.append(Paragraph(item["relevance"], style_relevance))
            story.append(Paragraph(item["source"], style_source))

    story.append(Spacer(1, 0.5 * cm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc"), spaceAfter=4))
    story.append(Paragraph(
        f"Generiert am {generated_display} | Quellen: {footer_sources}",
        style_footer,
    ))

    doc.build(story)
    print(f"PDF created: {output_path}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python science_report_builder.py <content.json> [output.pdf]")
        sys.exit(1)

    json_path = sys.argv[1]
    with open(json_path, encoding="utf-8") as f:
        content = json.load(f)

    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        repo_root = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(repo_root, "reports", f"{content['date']}_science_update.pdf")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    build_pdf(output_path, content)


if __name__ == "__main__":
    main()
