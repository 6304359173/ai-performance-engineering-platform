import pandas as pd

def transaction_summary(df):

    summary = (
        df.groupby("label")
          .agg(
              Requests=("label", "count"),
              Average=("elapsed", "mean"),
              Minimum=("elapsed", "min"),
              Maximum=("elapsed", "max"),
              P95=("elapsed", lambda x: x.quantile(0.95)),
              Failed=("success", lambda x: (~x).sum())
          )
          .reset_index()
    )

    summary = summary.sort_values(by="Average", ascending=False)

    return summary