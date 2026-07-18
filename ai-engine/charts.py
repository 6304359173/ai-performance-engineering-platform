import matplotlib.pyplot as plt
import os


def generate_transaction_chart(summary):

    os.makedirs("reports", exist_ok=True)

    plt.figure(figsize=(10,6))

    plt.bar(summary["label"], summary["Average"])

    plt.title("Average Response Time by Transaction")

    plt.xlabel("Transaction")

    plt.ylabel("Average Response Time (ms)")

    plt.xticks(rotation=20)

    plt.tight_layout()

    plt.savefig("reports/response_time_by_transaction.png")

    plt.close()