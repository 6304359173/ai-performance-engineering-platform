def calculate_score(metrics):

    score = 100

    # Failures carry the highest penalty
    if metrics["failed"] > 0:
        score -= metrics["failed"] * 10

    # Average Response Time
    if metrics["average"] > 1000:
        score -= 10

    if metrics["average"] > 2000:
        score -= 10

    # P95 Response Time
    if metrics["p95"] > 2000:
        score -= 15

    if metrics["p95"] > 3000:
        score -= 10

    if score < 0:
        score = 0

    return score