from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import os


def generate_pdf(metrics, recommendations):

    os.makedirs("reports", exist_ok=True)

    pdf = SimpleDocTemplate("reports/executive_report.pdf")

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>AI PERFORMANCE ENGINEERING REPORT</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(Paragraph(f"Total Requests : {metrics['total']}", styles["Normal"]))
    story.append(Paragraph(f"Successful Requests : {metrics['success']}", styles["Normal"]))
    story.append(Paragraph(f"Failed Requests : {metrics['failed']}", styles["Normal"]))
    story.append(Paragraph(f"Average RT : {metrics['average']:.2f} ms", styles["Normal"]))
    story.append(Paragraph(f"P95 : {metrics['p95']:.2f} ms", styles["Normal"]))
    story.append(Paragraph(f"P99 : {metrics['p99']:.2f} ms", styles["Normal"]))

    story.append(Spacer(1, 20))

    story.append(Paragraph("<b>AI Recommendations</b>", styles["Heading2"]))

    for item in recommendations:
        story.append(Paragraph("• " + item, styles["Normal"]))

    pdf.build(story)

    print("\nExecutive PDF Generated Successfully!")