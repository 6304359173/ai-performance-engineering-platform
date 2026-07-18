import os

def generate_dashboard(metrics, score, assessment):

    os.makedirs("reports", exist_ok=True)

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>AI Performance Dashboard</title>
<style>

body {{
    font-family: Arial;
    background:#f5f5f5;
    padding:30px;
}}

.card {{
    background:white;
    padding:20px;
    border-radius:10px;
    width:350px;
    box-shadow:0px 2px 8px gray;
}}

h1 {{
    color:#0055aa;
}}

.metric {{
    font-size:22px;
    margin:12px 0;
}}

</style>
</head>

<body>

<div class="card">

<h1>AI Performance Dashboard</h1>

<div class="metric"><b>Performance Score:</b> {score}/100</div>

<div class="metric"><b>Status:</b> {assessment}</div>

<div class="metric"><b>Total Requests:</b> {metrics['total']}</div>

<div class="metric"><b>Success:</b> {metrics['success']}</div>

<div class="metric"><b>Failures:</b> {metrics['failed']}</div>

<div class="metric"><b>Average RT:</b> {metrics['average']:.2f} ms</div>

<div class="metric"><b>P95:</b> {metrics['p95']:.2f} ms</div>

</div>

</body>

</html>
"""

    with open("reports/performance_dashboard.html","w") as f:
        f.write(html)

    print("HTML Dashboard Generated Successfully.")