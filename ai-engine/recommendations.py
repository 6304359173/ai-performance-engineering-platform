def get_recommendation(metrics):

    recommendation = []

    if metrics["failed"] > 0:
        recommendation.append("Investigate failed requests.")

    if metrics["p95"] > 2000:
        recommendation.append("P95 exceeds 2 seconds. Review slow APIs.")

    if metrics["average"] > 1000:
        recommendation.append("Average response time is above 1 second.")

    if len(recommendation) == 0:
        recommendation.append("Application performance is healthy.")

    return recommendation