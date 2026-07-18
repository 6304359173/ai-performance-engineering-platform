def quality_gate(score):

    print("\n" + "=" * 65)
    print("JENKINS QUALITY GATE")
    print("=" * 65)

    if score >= 90:
        print("Result : PASS")
        print("Deployment : Production Approved")
        return 0

    elif score >= 80:
        print("Result : PASS")
        print("Deployment : UAT Approved")
        return 0

    elif score >= 70:
        print("Result : MANUAL APPROVAL REQUIRED")
        print("Deployment : Needs Optimization Before Production")
        return 0   # Continue pipeline but require manual approval

    else:
        print("Result : FAIL")
        print("Deployment : Build Rejected")
        return 1