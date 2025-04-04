import os
from datetime import datetime
from .utils import generate_summary_table, load_test_results, render_template

REPORTS_DIR = "reports/compliance/output/"
TEMPLATE_PATH = "reports/compliance/templates/owasp_top10_template.md"

def generate_report(test_results_path="tests/test_samples/sample_inputs.json"):
    print("[*] Loading test results...")
    test_data = load_test_results(test_results_path)

    print("[*] Generating summary table...")
    summary = generate_summary_table(test_data)

    print("[*] Rendering markdown report...")
    rendered = render_template(TEMPLATE_PATH, summary)

    os.makedirs(REPORTS_DIR, exist_ok=True)
    output_path = os.path.join(REPORTS_DIR, f"aisecguard_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")

    with open(output_path, "w") as f:
        f.write(rendered)

    print(f"[+] Report generated at: {output_path}")

if __name__ == "__main__":
    generate_report()
