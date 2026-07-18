def print_report(metrics, recommendations, score, assessment):

    print("=" * 65)
    print("AI PERFORMANCE EXECUTIVE SUMMARY")
    print("=" * 65)

    print(f"Total Requests      : {metrics['total']}")
    print(f"Successful Requests : {metrics['success']}")
    print(f"Failed Requests     : {metrics['failed']}")

    print()

    print(f"Average RT          : {metrics['average']:.2f} ms")
    print(f"Minimum RT          : {metrics['minimum']} ms")
    print(f"Maximum RT          : {metrics['maximum']} ms")
    print(f"P95 Response Time   : {metrics['p95']:.2f} ms")
    print(f"P99 Response Time   : {metrics['p99']:.2f} ms")

    print()

    print(f"Performance Score   : {score}/100")
    print(f"Assessment          : {assessment}")

    print()

    print("AI Recommendations")
    print("-" * 65)

    for item in recommendations:
        print(f"• {item}")


def print_transaction_summary(summary):

    print()
    print("=" * 65)
    print("TOP SLOWEST TRANSACTIONS")
    print("=" * 65)

    for _, row in summary.iterrows():

        print(f"\nTransaction : {row['label']}")
        print(f"Requests    : {row['Requests']}")
        print(f"Average RT  : {row['Average']:.2f} ms")
        print(f"Maximum RT  : {row['Maximum']} ms")
        print(f"P95 RT      : {row['P95']:.2f} ms")
        print(f"Failures    : {row['Failed']}")