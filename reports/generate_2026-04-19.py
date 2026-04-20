#!/usr/bin/env python3
"""Generate daily science update PDF report."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
import os

DATE = "2026-04-19"
OUTPUT_PATH = "/home/user/Research/reports/2026-04-19_science_update.pdf"

CONTENT = {
    "title": f"Wissenschafts-Update - {DATE}",
    "sections": [
        {
            "heading": "Künstliche Intelligenz",
            "items": [
                {
                    "title": "Meta Llama 4: Mixture-of-Experts mit 10-Millionen-Token-Kontextfenster",
                    "body": "Meta veröffentlichte Llama 4, das erste Llama-Modell mit Mixture-of-Experts (MoE)-Architektur und nativer multimodaler Vortrainierung. Die Scout-Variante (17B aktive / 109B Gesamtparameter, 16 Experten) unterstützt ein Kontextfenster von 10 Millionen Token – das größte aller Open-Weight-Modelle und größer als jedes kommerziell verfügbare proprietäre Modell. Die MoE-Architektur aktiviert pro Token nur einen Bruchteil der Parameter, was Inferenz erheblich effizienter macht.",
                    "relevance": "Relevanz: Native Multimodalität ab dem Pretraining (kein nachträgliches Adapter-Retrofitting) und das massive Kontextfenster setzen neue Maßstäbe für Open-Source-LLMs und erhöhen den Druck auf proprietäre Anbieter.",
                    "source": "Quelle: Mean CEO Blog / Medium – April 2026 AI Model Review (April 2026)"
                },
                {
                    "title": "Google TurboQuant: 5x KV-Cache-Kompression mit minimalem Genauigkeitsverlust",
                    "body": "Google präsentierte TurboQuant, eine neue Quantisierungsmethode für Large Language Models. Der zweistufige Ansatz kombiniert PolarQuant-Vektorrotation mit der Quantized Johnson-Lindenstrauss-Methode und erreicht eine 5,02-fache Kompression des Key-Value-Cache bei minimalem Genauigkeitsverlust. Parallel stellte MIT CompreSSM vor – eine komplementäre Kompressionstechnik für State-Space-Modelle.",
                    "relevance": "Relevanz: KV-Cache-Kompression ist einer der kritischsten Bottlenecks bei langen Kontextfenstern; TurboQuant könnte Inferenzkosten und Speicheranforderungen für Produktionssysteme drastisch senken.",
                    "source": "Quelle: devFlokers – New AI Research Papers April 2026 (April 2026)"
                },
                {
                    "title": "Gemini 3.1 Ultra: Nativ-multimodale Architektur mit 2-Millionen-Token-Fenster",
                    "body": "Google DeepMinds Gemini 3.1 Ultra eliminiert Transkriptions-Zwischenschritte und verarbeitet Text, Audio, Bild und Video in einem einzigen, gemeinsamen Trainings-Objective – ohne separate Encoder-Module. Das Modell unterstützt ein Kontextfenster von 2 Millionen Token und setzt damit neue Maßstäbe für native Multimodalität bei proprietären Modellen.",
                    "relevance": "Relevanz: Die architektonische Entscheidung gegen separate Modalitäten-Encoder verspricht kohärenteres Cross-Modal-Reasoning; besonders relevant für Video-Analyse und Echtzeit-Audioverarbeitung.",
                    "source": "Quelle: devFlokers / Medium – April 2026 AI Model Reviews (April 2026)"
                },
            ]
        },
        {
            "heading": "Luft- und Raumfahrt",
            "items": [
                {
                    "title": "Blue Origin New Glenn NG-3: Erste erfolgreiche Booster-Wiederverwendung – Nutzlast im falschen Orbit",
                    "body": "Blue Origins New-Glenn-Rakete startete am 19. April 2026 um 07:25 Uhr EDT (11:25 UTC) zum dritten Mal – erstmals mit einem bereits geflogenen Booster. Der Erststufentriebwerk trennte sich nach ca. 3,5 Minuten und landete rund 6 Minuten nach dem Start auf dem Drohnenschiff 'Jacklyn' im Atlantik. Der AST-SpaceMobile-BlueBird-7-Satellit wurde dabei jedoch in eine falsche Umlaufbahn gebracht.",
                    "relevance": "Relevanz: Der erste erfolgreiche Wiederflug eines New-Glenn-Boosters ist ein Meilenstein für Blue Origins Wettbewerbsfähigkeit, auch wenn die Nutzlastzustellung scheiterte – dies zeigt, dass Wiederverwendbarkeit und Zuverlässigkeit noch getrennte Herausforderungen sind.",
                    "source": "Quelle: Space.com – Blue Origin reuses New Glenn rocket, April 19 2026"
                },
                {
                    "title": "SpaceX Starlink 17-22: 25 weitere Satelliten im Orbit",
                    "body": "SpaceX startete am 19. April 2026 um 07:33 Uhr PDT (14:33 UTC) von Vandenberg Space Force Base eine Falcon-9-Rakete mit 25 Starlink-Breitbandsatelliten der Generation 2. Der Booster führte eine routinierte Erstlandung durch. Die Konstellation wächst damit auf über 7.000 aktive Satelliten.",
                    "relevance": "Relevanz: Unterstreicht SpaceX' kontinuierlichen Vorteil bei Startrate und Konstellationsdichte gegenüber Konkurrenten wie Blue Origin und OneWeb.",
                    "source": "Quelle: Spaceflight Now – Launch Schedule (April 2026)"
                },
                {
                    "title": "Space Symposium 2026: Fünf strategische Schlüsselthemen",
                    "body": "Das jährliche Space Symposium in Colorado Springs endete am 19. April mit fünf prägenden Themen: kommerzielle Mondmissionen vor Artemis-Zeitplan, zunehmende militärische Nutzung des Erdorbits, Debatte um Weltraumtrümmer-Regulierung, Indiens aufstrebende Position als dritte Raumfahrtgroßmacht sowie KI-gestützte autonome Satellitensteuerung.",
                    "relevance": "Relevanz: Das Symposium gibt die strategische Agenda der globalen Raumfahrtindustrie vor und spiegelt geopolitische Verschiebungen in der Weltraumnutzung wider.",
                    "source": "Quelle: Gazette.com – Five big things from Space Symposium, April 19 2026"
                },
            ]
        },
        {
            "heading": "Robotik",
            "items": [
                {
                    "title": "Humanoid-Halbmarathon Peking: Autonomer Roboter unterbietet Welt-Bestzeit des Menschen",
                    "body": "Beim ersten Humanoid-Roboter-Halbmarathon Pekings (21 km) absolvierte ein autonomes Modell von Honor den Kurs in 50 Minuten und 26 Sekunden – schneller als der menschliche Weltrekord von Jacob Kiplimo (ca. 57 Minuten). Über 300 Roboter von mehr als 100 Teams nahmen teil. Ein ferngesteuertes Honor-Modell überquerte die Ziellinie in 48:19 min als Erstes, erhielt aber unter den Regelwerk-Gewichtungen den zweiten Platz hinter dem autonomen Sieger.",
                    "relevance": "Relevanz: Markiert einen Paradigmenwechsel in der Humanoiden-Robotik: Ausdauer, autonome Navigation und Stabilitätskontrolle auf einem Niveau, das menschliche Spitzensportler überbietet – enormer Benchmark-Sprung gegenüber 2:40h im Vorjahr.",
                    "source": "Quelle: PBS News / ABC News / Global Times – Humanoid Robot Half-Marathon, April 19 2026"
                },
                {
                    "title": "Unitree H1 erreicht 10 m/s Sprint – nahe Usain-Bolt-Niveau",
                    "body": "Unitree Robotics gab bekannt, dass sein H1-Humanoid-Roboter einen neuen Weltrekord im Sprint aufgestellt hat: 10 m/s – nahezu identisch mit Usain Bolts gemessener Spitzengeschwindigkeit von 10,44 m/s. Die Leistung wurde durch ein neues Aktuatorsystem und verbesserte Gangplanungsalgorithmen erreicht.",
                    "relevance": "Relevanz: Kombiniert mit dem Halbmarathon-Ergebnis signalisiert dies, dass Humanoide sowohl in Ausdauer als auch in Spitzenleistung an menschliche Grenzen stoßen – mit weitreichenden Implikationen für industrielle und militärische Anwendungen.",
                    "source": "Quelle: Global Times – Humanoid robot half-marathon / Unitree Robotics (April 2026)"
                },
            ]
        },
        {
            "heading": "Astronomie",
            "items": [
                {
                    "title": "HETDEX entdeckt 33.000+ Lyman-Alpha-Nebel: Wasserstoffreservoire der frühen Galaxien",
                    "body": "Eine neue Studie im Astrophysical Journal, basierend auf Daten des Hobby-Eberly Telescope Dark Energy Experiment (HETDEX), erhöhte die Anzahl bekannter Lyman-Alpha-Nebel – riesiger Wasserstoffgas-Halos um Galaxien – von ca. 3.000 auf über 33.000. Die Halos existierten vor 10–12 Milliarden Jahren (Cosmic Noon) und reichen teils über Hunderttausende von Lichtjahren. Einige haben unregelmäßige, amöbenähnliche Formen mit langen Ausläufern.",
                    "relevance": "Relevanz: Diese Wasserstoffreservoire sind der Treibstoff des kosmischen Galaxienwachstums; die 10-fache Erhöhung der Stichprobengröße liefert erstmals statistisch belastbare Daten über die Gasversorgung früher Galaxien.",
                    "source": "Quelle: Phys.org / Penn State University / The Astrophysical Journal (April 2026)"
                },
                {
                    "title": "Event Horizon Telescope: 3.000 Lichtjahre langer Jet aus M87 kartiert",
                    "body": "Das Event Horizon Telescope (EHT) veröffentlichte neue Beobachtungen des 3.000 Lichtjahre langen relativistischen Jets aus dem supermassiven schwarzen Loch M87* – dem ersten je direkt abgebildeten schwarzen Loch. Neue VLBI-Daten zeigen die Jetstruktur vom Ursprung bis in große Entfernung mit bislang unerreichter Auflösung und erlauben Rückschlüsse auf den Energieextraktionsmechanismus (Blandford-Znajek-Prozess).",
                    "relevance": "Relevanz: Klärt grundlegende Fragen der Relativitätsastrophysik und bietet experimentellen Zugang zur Magnetfeldstruktur in der Nähe des Ereignishorizonts.",
                    "source": "Quelle: Scientific American / EarthSky – EHT M87 Jet Study (April 2026)"
                },
            ]
        },
        {
            "heading": "Quantencomputing",
            "items": [
                {
                    "title": "Caltech & ETH Zürich: Praktischer Quantencomputer mit nur 10.000–20.000 Qubits realisierbar",
                    "body": "Forscher der Caltech und ETH Zürich zeigten, dass ein fehlertoleranter universeller Quantencomputer mit nur 10.000–20.000 physischen Qubits realisierbar ist – statt der bislang angenommenen Millionen. Der Schlüssel liegt in neutralen Atom-Qubits ('Laser-Pinzetten'), bei denen ein logisches Qubit aus nur 5 physischen Qubits konstruiert werden kann (statt ~1.000 bei Supraleiter-Architekturen). ETH Zürich demonstrierte zusätzlich bemerkenswerte Fehlerresistenz dieser Plattform.",
                    "relevance": "Relevanz: Reduziert die Hürde zur Quantenfehlerkorrektur um Größenordnungen und macht kommerzielle Quantencomputer in diesem Jahrzehnt deutlich realistischer – mit direkten Auswirkungen auf Kryptographie, Materialwissenschaft und Pharma.",
                    "source": "Quelle: BGR / ScienceDaily – Quantum Computing Breakthrough (April 2026)"
                },
                {
                    "title": "NVIDIA Ising: Erste offene KI-Modelle zur Beschleunigung von Quantenalgorithmen",
                    "body": "NVIDIA lancierte 'Ising' – die weltweit ersten open-source KI-Modelle, die speziell zur Beschleunigung des Wegs zu praktisch nützlichen Quantencomputern entwickelt wurden. Ising optimiert Quantenschaltkreise, approximiert Quantenlösungen auf klassischer Hardware und verbessert Fehlermitigationsstrategien – integriert in NVIDIAs CUDA-Quantum-Ökosystem.",
                    "relevance": "Relevanz: KI als Wegbereiter für Quantencomputing schafft eine Hybridstrategie, die bereits heute Quantenvorteile approximiert und gleichzeitig die Entwicklung echter Quantensysteme beschleunigt.",
                    "source": "Quelle: NVIDIA Newsroom – NVIDIA launches Ising (April 2026)"
                },
            ]
        },
        {
            "heading": "Medizin & Biologie",
            "items": [
                {
                    "title": "Ozempic/Wegovy wirken bei 10 % der Patienten nicht – genetische Variante identifiziert",
                    "body": "Eine neue Studie zeigt, dass die GLP-1-Rezeptoragonisten Semaglutid (Ozempic/Wegovy) bei etwa 10 % der Anwender signifikant schlechter wirken – ursächlich sind spezifische genetische Varianten im GLP1R-Gen, die die Rezeptorbindung schwächen. Die Identifikation der Varianten ermöglicht künftig pharmakogenomische Tests vor der Verschreibung.",
                    "relevance": "Relevanz: Öffnet den Weg zu personalisierter Adipositas-Therapie und erklärt eine bislang klinisch rätselhafte Patientengruppe – direkte Auswirkungen auf Millionen von Anwendern weltweit.",
                    "source": "Quelle: ScienceDaily / Biomedical Research Journals (April 2026)"
                },
                {
                    "title": "Synthetisches DNA-basiertes Wirkstoffsystem targetiert Krebszellen mit neuer Präzision",
                    "body": "Forscher entwickelten ein programmierbares Wirkstoff-Delivery-System aus synthetischer DNA (DNA-Origami-Nanostruktur), das Krebszellen anhand ihrer Oberflächenproteine mit bislang unerreichter Spezifität erkennt und Chemotherapeutika gezielt freisetzt. In ersten In-vitro- und Mausmodellen wurden gesunde Zellen weitgehend verschont.",
                    "relevance": "Relevanz: Adressiert das zentrale Problem der Krebstherapie – Kollateralschäden an gesunden Geweben – mit einem molekular programmierbaren Ansatz, der unabhängig vom Krebstyp anpassbar ist.",
                    "source": "Quelle: ScienceDaily / Biotech Research News (April 2026)"
                },
            ]
        },
        {
            "heading": "Chips & Halbleiter",
            "items": [
                {
                    "title": "SambaNova RDU + Intel Xeon: Neue Architektur für agentische KI-Inferenz",
                    "body": "SambaNova Systems gab die Integration seiner Reconfigurable Dataflow Units (RDUs) mit Intel Xeon CPUs bekannt, um schnelle agentische KI-Inferenz zu ermöglichen. RDUs sind speziell für dynamische, datenflussgesteuerte Berechnungen optimiert – im Gegensatz zu GPUs, die auf statische Parallelverarbeitung ausgerichtet sind. Die Hybrid-Architektur soll Latenz für sequenzielle Reasoning-Chains senken.",
                    "relevance": "Relevanz: Agentische KI mit komplexen Tool-Use-Ketten erfordert andere Rechenprofile als Standard-Matrixmultiplikation; spezialisierte Dataflow-Architekturen könnten GPUs für diese Workloads ablösen.",
                    "source": "Quelle: SambaNova Systems / EE Times (April 2026)"
                },
                {
                    "title": "Globaler Halbleitermarkt 2026: 975 Mrd. USD erwartet – AI-Boom als Haupttreiber",
                    "body": "Laut Deloitte Semiconductor Outlook 2026 wird der globale Halbleitermarkt in diesem Jahr voraussichtlich 975 Milliarden USD erreichen – ein historisches Hoch mit 26 % Wachstum gegenüber 2025. Die Februarumsätze lagen bei 88,8 Mrd. USD (+61,8 % gegenüber Feb. 2025). Kritischer Engpass bleiben HBM (High Bandwidth Memory) und Advanced Packaging.",
                    "relevance": "Relevanz: Das KI-Infrastrukturwachstum treibt eine branchenweite Kapazitätsexpansion; der HBM-Engpass bestimmt, wie schnell AI-GPU-Shipments skalieren können.",
                    "source": "Quelle: Deloitte Semiconductor Outlook 2026 / SIA (April 2026)"
                },
            ]
        },
        {
            "heading": "Automobilindustrie & E-Mobilität",
            "items": [
                {
                    "title": "BYD expandiert nach Argentinien: Erste EV-Lieferung nach Zollabschaffung",
                    "body": "BYD lieferte die erste Ladung Elektro- und Hybridfahrzeuge nach Argentinien, nachdem Präsident Javier Milei die Importzölle im April 2025 abgeschafft hatte. Die Marktöffnung gilt als Testfall für BYDs Strategie, Lateinamerika als neuen Kernmarkt zu erschließen, nachdem Europa zunehmend Strafzölle auf chinesische EVs erhebt.",
                    "relevance": "Relevanz: BYDs geopolitische Diversifikationsstrategie zeigt die direkte Auswirkung handelspolitischer Entscheidungen auf EV-Marktdynamiken; Lateinamerika wird zum neuen Schlachtfeld für chinesische und westliche Hersteller.",
                    "source": "Quelle: Cox Automotive / Automotive News (April 2026)"
                },
                {
                    "title": "US-EV-Markt Q1 2026: Verkäufe fallen 27 % – Marktanteil stabilisiert sich bei 6 %",
                    "body": "Laut Cox Automotive/Kelley Blue Book brachen die BEV-Verkäufe in den USA im ersten Quartal 2026 um 27 % gegenüber Q1 2025 ein. Der Marktanteil (BEV + PHEV) stabilisierte sich bei etwa 6 % – weit unter früheren Prognosen von 24,7 %. Hauptgründe: gestiegene Zinsen, Verunsicherung durch US-Zollpolitik und Ladeinfrastruktur-Bedenken.",
                    "relevance": "Relevanz: Signalisiert eine Verlangsamung der EV-Adoption in den USA trotz globalen Wachstums; stellt Hersteller wie Ford und GM vor strategische Dilemmas beim Investitionsvolumen.",
                    "source": "Quelle: Cox Automotive – Q1 2026 EV Sales Report (April 2026)"
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
        "Tägliche Übersicht wissenschaftlicher &amp; technologischer Entwicklungen | Zeitraum: 19. April 2026, 00:00–23:59 UTC",
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
        "Generiert am 20. April 2026 | Quellen: Space.com, Spaceflight Now, PBS News, ABC News, Global Times, "
        "Phys.org, Penn State University, NVIDIA Newsroom, BGR, ScienceDaily, Deloitte, Cox Automotive, "
        "devFlokers, Mean CEO Blog, Scientific American u.a.",
        ParagraphStyle("Footer", parent=styles["Normal"], fontSize=7, textColor=colors.HexColor("#aaaaaa"), alignment=TA_CENTER)
    ))

    doc.build(story)
    print(f"PDF created: {output_path}")


if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    build_pdf(OUTPUT_PATH, CONTENT)
