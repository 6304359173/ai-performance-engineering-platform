def print_report(metrics, recommendations):

    print("=" * 60)

    print("AI PERFORMANCE SUMMARY")

    print("=" * 60)

    print(f"Total Requests      : {metrics['total']}")

    print(f"Successful Requests : {metrics['success']}")

    print(f"Failed Requests     : {metrics['failed']}")

    print(f"Average RT          : {metrics['average']:.2f} ms")

    print(f"Minimum RT          : {metrics['minimum']} ms")

    print(f"Maximum RT          : {metrics['maximum']} ms")

    print(f"P95 Response Time   : {metrics['p95']:.2f} ms")

    print(f"P99 Response Time   : {metrics['p99']:.2f} ms")

    print("\nAI Recommendations")

    print("-" * 60)

    for item in recommendations:
        print(f"• {item}")