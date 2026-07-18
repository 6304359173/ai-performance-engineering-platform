import pandas as pd
import matplotlib.pyplot as plt
import os

HISTORY_FILE = "history/performance_history.csv"

def generate_trend_chart():

    if not os.path.exists(HISTORY_FILE):
        print("History file not found.")
        return

    df = pd.read_csv(HISTORY_FILE)

    if len(df) < 2:
        print("Need at least two executions for trend chart.")
        return

    plt.figure(figsize=(8,4))

    plt.plot(
        range(1, len(df)+1),
        df["PerformanceScore"],
        marker="o",
        linewidth=2
    )

    plt.title("Performance Score Trend")

    plt.xlabel("Execution")

    plt.ylabel("Performance Score")

    plt.grid(True)

    os.makedirs("reports", exist_ok=True)

    plt.savefig("reports/performance_trend.png")

    plt.close()

    print("Trend Chart Generated Successfully.")