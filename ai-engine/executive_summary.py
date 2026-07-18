def generate_executive_summary(metrics, score, assessment, deployment_status):

    summary = f"""
The performance test completed with {metrics['success']} successful requests out of {metrics['total']} total requests.

Overall Performance Score: {score}/100.

Assessment:
{assessment}

Average Response Time:
{metrics['average']:.2f} ms

P95 Response Time:
{metrics['p95']:.2f} ms

Deployment Recommendation:
{deployment_status}

Overall, the application is stable but requires optimization before production deployment.
"""

    return summary