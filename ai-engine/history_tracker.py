import csv
import os
from datetime import datetime

HISTORY_FILE = "history/performance_history.csv"

def save_execution(metrics, score):

    os.makedirs("history", exist_ok=True)

    file_exists = os.path.exists(HISTORY_FILE)

    with open(HISTORY_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "ExecutionTime",
                "PerformanceScore",
                "AverageRT",
                "P95",
                "Failures"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            score,
            round(metrics["average"], 2),
            round(metrics["p95"], 2),
            metrics["failed"]
        ])

    print("Execution History Updated.")