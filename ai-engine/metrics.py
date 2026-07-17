def calculate_metrics(df):

    total = len(df)

    success = len(df[df["success"] == True])

    failed = len(df[df["success"] == False])

    average = df["elapsed"].mean()

    minimum = df["elapsed"].min()

    maximum = df["elapsed"].max()

    p95 = df["elapsed"].quantile(0.95)

    p99 = df["elapsed"].quantile(0.99)

    return {

        "total": total,

        "success": success,

        "failed": failed,

        "average": average,

        "minimum": minimum,

        "maximum": maximum,

        "p95": p95,

        "p99": p99

    }