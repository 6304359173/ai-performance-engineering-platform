import json
import os

def export_json(metrics, score, assessment):

    os.makedirs("reports", exist_ok=True)

    data = {
        "PerformanceScore": score,
        "Assessment": assessment,
        "TotalRequests": metrics["total"],
        "SuccessfulRequests": metrics["success"],
        "FailedRequests": metrics["failed"],
        "AverageResponseTime": round(metrics["average"],2),
        "P95": round(metrics["p95"],2),
        "P99": round(metrics["p99"],2)
    }

    with open("reports/performance_summary.json","w") as f:
        json.dump(data,f,indent=4)

    print("JSON Summary Generated.")