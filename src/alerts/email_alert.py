import os
import json
import smtplib
from pathlib import Path
from email.mime.text import MIMEText
from dotenv import load_dotenv

#BASE_DIR = Path("/Users/sugashinikaliappan/nyc-taxi-data-quality-platform")
BASE_DIR = Path(__file__).resolve().parents[2]
REPORT_FILE = BASE_DIR / "data/reports/quality_report_2024_01.json"

load_dotenv(BASE_DIR / ".env")


def send_email_alert(subject: str, body: str):
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    recipient = os.getenv("ALERT_RECIPIENT")

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = recipient

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)


def evaluate_quality_and_alert():
    report = json.loads(REPORT_FILE.read_text(encoding="utf-8"))

    quality_score = report["quality_score_percent"]
    threshold = float(os.getenv("QUALITY_SCORE_THRESHOLD", "99.0"))

    failed_rules = [
        rule for rule in report["rule_results"]
        if rule["status"] == "FAIL"
    ]

    if quality_score < threshold or failed_rules:
        subject = f"Data Quality Alert: {report['dataset']}"

        body = f"""
Data Quality Alert Triggered

Dataset: {report['dataset']}
Total Records: {report['total_records']:,}
Quality Score: {quality_score}%
Threshold: {threshold}%
Rules Failed: {report['rules_failed']}

Failed Rules:
"""

        for rule in failed_rules:
            body += f"""
- Rule: {rule['rule_name']}
  Severity: {rule['severity']}
  Owner: {rule['owner']}
  Pass Rate: {rule['pass_rate_percent']}%
  Failed Records: {rule['failed_records']:,}
"""

        send_email_alert(subject, body)
        print("Email alert sent.")
    else:
        print("Quality score is within threshold. No alert sent.")


if __name__ == "__main__":
    evaluate_quality_and_alert()
