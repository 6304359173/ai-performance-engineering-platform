def get_deployment_decision(score):

    if score >= 90:
        return (
            "🟢 PRODUCTION READY",
            "Application meets all performance targets."
        )

    elif score >= 80:
        return (
            "🟡 DEPLOY TO UAT",
            "Performance is acceptable. Monitor closely."
        )

    elif score >= 70:
        return (
            "🟠 NEEDS OPTIMIZATION",
            "Performance issues should be addressed before production."
        )

    else:
        return (
            "🔴 DO NOT DEPLOY",
            "Critical performance issues detected."
        )