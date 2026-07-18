def get_assessment(score):

    if score >= 90:
        return "✅ Production Ready"

    elif score >= 80:
        return "🟡 UAT Ready"

    elif score >= 70:
        return " Needs Optimization"

    else:
        return "❌ Not Ready"