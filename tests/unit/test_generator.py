import os
from reports.compliance.generator import generate_report

def test_generate_report_creates_file(tmp_path):
    test_file = tmp_path / "sample_results.json"
    test_file.write_text('{ "results": [ { "name": "Test", "status": "Pass", "note": "Example" } ] }')
    
    os.makedirs("reports/compliance/output", exist_ok=True)
    generate_report(str(test_file))
    generated = list(os.listdir("reports/compliance/output"))
    assert any(f.endswith(".md") for f in generated)
