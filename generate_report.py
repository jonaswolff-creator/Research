#!/usr/bin/env python3
"""Generate daily science update PDF report."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
import os

DATE = "2026-04-18"
OUTPUT_PATH = "/home/user/Research/reports/2026-04-18_science_update.pdf"

CONTENT = {
    "title": f"Wissenschafts-Update - {DATE}",
    "sections": [
        {
            "heading": "Künstliche Intelligenz",
            "items": [
                {
                    "title": "NASA-Rover auf dem Mars durch KI gesteuert",
                    "body": "NASAs Perseverance-Rover absolvierte erstmals vollständig KI-geplante Fahrten auf dem Mars. Anthropics Claude-Vision-Sprachmodelle analysierten Orbitaldaten und Geländeinformationen, um autonome Wegpunkte zu generieren. Dies markiert einen Meilenstein in der autonomen Raumfahrtexploration.",
                    "relevance": "Relevanz: Belegt den praktischen Einsatz von KI in der Planetenexploration und eröffnet neue Möglichkeiten für autonome Missionen.",
                    "source": "Quelle: ScienceDaily / NASA (April 2026)"
                },
                {
                    "title": "KI-System interpretiert Gehirn-MRTs in Sekunden",
                    "body": "Forscher der University of Michigan entwickelten ein KI-System, das MRT-Scans des Gehirns in Sekunden auswertet, eine breite Palette neurologischer Erkrankungen erkennt und dringende Fälle priorisiert. Das System erreicht diagnostische Genauigkeit auf Facharzt-Niveau.",
                    "relevance": "Relevanz: Könnte neurologische Diagnostik in unterversorgten Regionen ohne Spezialisten ermöglichen und Wartezeiten drastisch senken.",
                    "source": "Quelle: ScienceDaily (April 2026)"
                },
                {
                    "title": "KI-Energieverbrauch: 100x-Reduktion durch neuen Ansatz",
                    "body": "Forscher präsentierten eine neue Methode, die den Energieverbrauch von KI-Modellen um den Faktor 100 reduziert und dabei die Genauigkeit steigert. Der Ansatz kombiniert Quantencomputing-Prinzipien mit neuartiger Modellarchitektur.",
                    "relevance": "Relevanz: Adressiert einen der größten Kritikpunkte am KI-Boom - den massiven Energiebedarf - mit direkten Auswirkungen auf Nachhaltigkeit und Betriebskosten.",
                    "source": "Quelle: ScienceDaily, 5. April 2026"
                },
            ]
        },
        {
            "heading": "Luft- und Raumfahrt",
            "items": [
                {
                    "title": "Blue Origin: New Glenn mit wiederverwendeter Stufe",
                    "body": "Blue Origins New-Glenn-Rakete bereitete sich auf ihren dritten Flug vor - erstmals mit einer bereits geflogenen Booster-Stufe. Ein Statischer Feuertest des wiederverwendeten Boosters fand am 16. April statt. Der Start ist für den 19. April geplant.",
                    "relevance": "Relevanz: Demonstration der Wiederverwendbarkeit von New Glenn ist entscheidend für Blue Origins langfristige Wettbewerbsfähigkeit gegenüber SpaceX.",
                    "source": "Quelle: Space.com / SpaceFlight Now (April 2026)"
                },
                {
                    "title": "SpaceX: 600. Falcon-9-Booster-Landung",
                    "body": "SpaceX erzielte mit einer Starlink-Mission von Cape Canaveral die 600. Booster-Landung einer Falcon-9-Rakete. Die Mission beförderte gleichzeitig den 600. Starlink-Satelliten des Jahres 2026 in die Umlaufbahn.",
                    "relevance": "Relevanz: Unterstreicht die industrielle Reife der Wiederverwendbarkeitstechnologie von SpaceX und den rasanten Ausbau des Starlink-Netzwerks.",
                    "source": "Quelle: SpaceflightNow (April 2026)"
                },
                {
                    "title": "eVTOL-Fliegender-Krankenwagen: SkyClinic",
                    "body": "Das Unternehmen SkyClinic stellte ein eVTOL-Konzept (electric Vertical Take-Off and Landing) vor, das als fliegendes Krankenhaus für Katastrophengebiete dienen soll und chirurgische Eingriffe direkt am Einsatzort ermöglicht.",
                    "relevance": "Relevanz: Verbindet Luftfahrtinnovation mit humanitärem Einsatz und könnte die Notfallmedizin in unzugänglichen Regionen transformieren.",
                    "source": "Quelle: Aerospace Global News / Royal Aeronautical Society (April 2026)"
                },
            ]
        },
        {
            "heading": "Medizin & Biologie",
            "items": [
                {
                    "title": "Breakthrough Prize: Gentherapie für Sichelzellanämie",
                    "body": "Stuart H. Orkin und Swee Lay Thein wurden mit dem Breakthrough Prize in Life Sciences ausgezeichnet für ihre Forschung, die Sichelzellanämie und Beta-Thalassämie durch Genbearbeitung (BCL11A-Gen) von unheilbar zu behandelbar machte. Die Therapien sind bereits im klinischen Einsatz.",
                    "relevance": "Relevanz: Direkte Patientenauswirkung: Millionen Betroffene weltweit profitieren von diesen Gentherapien; Auszeichnung unterstreicht strategische Bedeutung.",
                    "source": "Quelle: PR Newswire / Breakthrough Prize Foundation (April 2026)"
                },
                {
                    "title": "KI reshapes Wirkstoffforschung für Biologika",
                    "body": "Laut The Medicine Maker transformiert KI die Entdeckung biologischer Wirkstoffe grundlegend: Modelle können Protein-Interaktionen schneller und präziser vorhersagen als bisherige Methoden und beschleunigen den Weg vom Target zur klinischen Studie deutlich.",
                    "relevance": "Relevanz: Könnte Entwicklungszeiten für Medikamente von ~12 Jahren auf unter 5 Jahre reduzieren und die Kosten der Medikamentenentwicklung drastisch senken.",
                    "source": "Quelle: The Medicine Maker, April 2026"
                },
            ]
        },
        {
            "heading": "Astronomie",
            "items": [
                {
                    "title": "TOI-201: Dreikörper-Planetensystem in Echtzeit beobachtbar",
                    "body": "Astronomen der Universität Birmingham, ESA und Observatoire de la Côte d'Azur entdeckten das Planetensystem TOI-201 - drei Himmelskörper in einer seltenen gravitativen Wechselwirkung, deren Orbits sich schnell genug verändern, um in Echtzeit messbar zu sein. Entdeckt mit ASTEP (Antarktis), TESS und LCOGT.",
                    "relevance": "Relevanz: Ermöglicht einzigartigen Einblick in Dreikörper-Dynamik und bietet ein natürliches Labor für Himmelsmechanik und Planetenentstehung.",
                    "source": "Quelle: University of Birmingham (15. April 2026)"
                },
                {
                    "title": "Webb-Teleskop: Exoplanet mit unerklärlicher Helium-Kohlenstoff-Atmosphäre",
                    "body": "Das James Webb Space Telescope beobachtete PSR J2322-2650b - einen Jupiter-schweren Exoplaneten mit einer Atmosphäre aus Helium und Kohlenstoff, der rußartige Wolken und eine zitronenförmige Gestalt aufweist. Die Zusammensetzung widerspricht aktuellen Planetenentstehungsmodellen.",
                    "relevance": "Relevanz: Fordert bestehende Theorien der Planetenbildung heraus und erweitert das Spektrum bekannter Exoplanetentypen erheblich.",
                    "source": "Quelle: NASA Science / ScienceDaily (Dezember 2025, bestätigt April 2026)"
                },
            ]
        },
        {
            "heading": "Automobilindustrie & E-Mobilität",
            "items": [
                {
                    "title": "Feststoffbatterie: Greater Bay Technology kündigt Massenproduktion an",
                    "body": "Greater Bay Technology gab bekannt, nach einem Durchbruch die weltweit erste massenproduktionsfähige Feststoffbatterie (All-Solid-State Battery) noch 2026 auf den Markt bringen zu wollen. Diese Technologie verspricht höhere Energiedichte, schnelleres Laden und verbesserte Sicherheit.",
                    "relevance": "Relevanz: Feststoffbatterien gelten als Schlüsseltechnologie für die nächste EV-Generation; Massenproduktion würde die Reichweiten- und Sicherheitsdebatte neu definieren.",
                    "source": "Quelle: InsideEVs / EV Magazine (April 2026)"
                },
                {
                    "title": "V2G-Technologie: EVs verdienen bis zu 3.359 $/Jahr",
                    "body": "Forscher der University of Delaware und Exelon/Delmarva Power veröffentlichten eine Studie, die zeigt, dass Vehicle-to-Grid (V2G)-fähige Elektrofahrzeuge Besitzern bis zu 3.359 US-Dollar jährlich einbringen können, indem sie Energie ins Netz zurückspeisen.",
                    "relevance": "Relevanz: Macht Elektrofahrzeuge zu wirtschaftlichen Netzspeichern und könnte die Amortisationszeit deutlich verkürzen.",
                    "source": "Quelle: UDaily / University of Delaware (April 2026)"
                },
            ]
        },
        {
            "heading": "Chips & Halbleiter",
            "items": [
                {
                    "title": "Arm launcht ersten eigenen Chip: Arm AGI CPU auf TSMC 3nm",
                    "body": "Arm Holdings stellte am 24. März 2026 den Arm AGI CPU vor - den ersten vollständigen Produktionschip des Unternehmens, gefertigt auf TSMCs 3nm-Prozess. Der Schritt markiert Arms Wandel vom Lizenzgeber zum Chiphersteller mit vollständigem Hardware-Software-Stack.",
                    "relevance": "Relevanz: Verändert die Halbleiter-Wertschöpfungskette fundamental; Kunden erhalten schnellere, risikoärmere Deployment-Pfade für ARM-basierte Systeme.",
                    "source": "Quelle: Omdia / Arm Holdings (März-April 2026)"
                },
                {
                    "title": "Halbleitermarkt 2026: Auf dem Weg zur Billion-Dollar-Branche",
                    "body": "Globale Halbleiterumsätze erreichten im Februar 2026 88,8 Milliarden US-Dollar - ein Anstieg von 61,8 % gegenüber Februar 2025. Der AI-getriebene Aufschwung treibt die Branche auf einen prognostizierten Jahresumsatz von ~1 Billion USD.",
                    "relevance": "Relevanz: Zeigt das historische Ausmaß des KI-getriebenen Chip-Booms und dessen Bedeutung als strategische Infrastruktur.",
                    "source": "Quelle: SIA / Deloitte Semiconductor Outlook 2026"
                },
            ]
        },
        {
            "heading": "Robotik",
            "items": [
                {
                    "title": "Beijing Halbmarathon für Humanoide Roboter - Vortag",
                    "body": "Am 18. April fand der Vorbereitungs-Challenge 'Robot Baturu' mit 17 Hindernisevents für Humanoide Roboter statt - Auftakt zum großen Halbmarathon am 19. April mit über 300 Robotern. Teilnehmende Einheiten trugen BeiDou-GPS-Abzeichen mit Zentimeter-Präzision.",
                    "relevance": "Relevanz: Erster Wettbewerb dieser Skala für autonome Humanoide; setzt neue Benchmarks für Stabilität, Ausdauer und Navigationspräzision in Echtumgebungen.",
                    "source": "Quelle: Global Times / Digitimes (April 2026)"
                },
                {
                    "title": "Gig-Economy für Robotik-Training",
                    "body": "Laut MIT Technology Review entsteht eine neue Gig-Worker-Kategorie: Menschen, die Humanoide Roboter von zu Hause aus per Teleoperations-Interface trainieren. Diese Daten gelten als eigentlicher Wert der Robotik-Unternehmen - wertvoller als die Hardware selbst.",
                    "relevance": "Relevanz: Zeigt die Abhängigkeit der Robotik-KI von menschlichen Trainingsdaten und eröffnet gleichzeitig neue Beschäftigungsformen.",
                    "source": "Quelle: MIT Technology Review, 1. April 2026"
                },
            ]
        },
        {
            "heading": "Quantencomputing",
            "items": [
                {
                    "title": "Globale Quanteninvestitionen überschreiten 55 Mrd. USD",
                    "body": "Weltweite Investitionen in Quantentechnologien übertrafen 2025 die Marke von 55 Milliarden US-Dollar. Für 2026 wird ein Marktumsatz von ~9 Milliarden USD erwartet (von 2,5 Mrd. in 2025). M&A-Aktivität und staatliche Programme beschleunigen sich weltweit.",
                    "relevance": "Relevanz: Quantencomputing nähert sich dem kommerziellen Einsatz; Energiesektor, Logistik und Pharma gehören zu den ersten Zielindustrien.",
                    "source": "Quelle: The Quantum Insider / WEF (April 2026)"
                },
            ]
        },
    ]
}


def build_pdf(output_path: str, content: dict) -> None:
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm,
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

    story = []

    story.append(Paragraph(content["title"], style_title))
    story.append(Paragraph(
        "Tägliche Übersicht wissenschaftlicher &amp; technologischer Entwicklungen | Zeitraum: 18. April 2026, 00:00-23:59 UTC",
        style_subtitle
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

    story.append(Spacer(1, 0.5*cm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#cccccc"), spaceAfter=4))
    story.append(Paragraph(
        "Generiert am 19. April 2026 | Quellen: ScienceDaily, NASA, Space.com, MIT Technology Review, The Quantum Insider, "
        "University of Birmingham, Global Times, InsideEVs, Breakthrough Prize Foundation, Arm Holdings, SIA u.a.",
        ParagraphStyle("Footer", parent=styles["Normal"], fontSize=7, textColor=colors.HexColor("#aaaaaa"), alignment=TA_CENTER)
    ))

    doc.build(story)
    print(f"PDF created: {output_path}")


if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    build_pdf(OUTPUT_PATH, CONTENT)
