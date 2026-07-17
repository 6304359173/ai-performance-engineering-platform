import sys

from parser import load_jtl
from metrics import calculate_metrics
from recommendations import get_recommendation
from report import print_report

if len(sys.argv) < 2:
    print("Usage:")
    print("python analyzer.py results.jtl")
    sys.exit()

file = sys.argv[1]

df = load_jtl(file)

metrics = calculate_metrics(df)

recommendations = get_recommendation(metrics)

print_report(metrics, recommendations)