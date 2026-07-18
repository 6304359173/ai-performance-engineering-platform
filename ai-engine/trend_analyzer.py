import pandas as pd
import os

HISTORY_FILE = "history/performance_history.csv"

def analyze_trend():

    if not os.path.exists(HISTORY_FILE):
        print("No execution history available.")
        return None

    df = pd.read_csv(HISTORY_FILE)

    if len(df) < 2:
        print("Only one execution available. Trend analysis requires at least two runs.")
        return None

    latest = df.iloc[-1]
    previous = df.iloc[-2]

    score_change = latest["PerformanceScore"] - previous["PerformanceScore"]
    avg_change = latest["AverageRT"] - previous["AverageRT"]
    p95_change = latest["P95"] - previous["P95"]

    print("\n================ PERFORMANCE TREND ================\n")

    print(f"Previous Score : {previous['PerformanceScore']}")
    print(f"Current Score  : {latest['PerformanceScore']}")
    print(f"Score Change   : {score_change:+}")

    print()

    print(f"Previous Avg RT : {previous['AverageRT']} ms")
    print(f"Current Avg RT  : {latest['AverageRT']} ms")

    print()

    if score_change > 0:
        print("AI Insight : Performance Improved ✅")
    elif score_change < 0:
        print("AI Insight : Performance Regressed ❌")
    else:
        print("AI Insight : Performance Stable ⚖")

    return df