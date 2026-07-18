import sys

from parser import load_jtl
from metrics import calculate_metrics
from recommendations import get_recommendation
from report import print_report, print_transaction_summary
from transaction_metrics import transaction_summary
from charts import generate_transaction_chart
from pdf_generator import generate_pdf
from score import calculate_score
from assessment import get_assessment
from json_export import export_json
from dashboard import generate_dashboard
from history_tracker import save_execution
from trend_analyzer import analyze_trend
from trend_chart import generate_trend_chart


if len(sys.argv) < 2:
    print("Usage:")
    print("python analyzer.py results.jtl")
    sys.exit()

file = sys.argv[1]

# Load JTL
df = load_jtl(file)

# Calculate Metrics
metrics = calculate_metrics(df)

# Calculate Score
score = calculate_score(metrics)

# Assessment
assessment = get_assessment(score)

# AI Recommendations
recommendations = get_recommendation(metrics)

# Print Executive Summary
print_report(metrics, recommendations, score, assessment)

# Transaction Analytics
summary = transaction_summary(df)

print_transaction_summary(summary)

# Generate Chart
generate_transaction_chart(summary)

# Generate PDF
print("Generating Executive PDF...")
generate_pdf(metrics, recommendations)

# Generate JSON
export_json(metrics, score, assessment)

# Generate HTML Dashboard
generate_dashboard(metrics, score, assessment)

# Save Execution History
save_execution(metrics, score)
analyze_trend()
generate_trend_chart()
print("Program Completed Successfully.")
