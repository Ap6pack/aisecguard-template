import pytest
from reports.compliance.utils import generate_summary_table

def test_generate_summary_table():
    sample = {
        "results": [
            {"name": "Prompt Injection", "status": "Fail", "note": "Payload bypassed filters"},
            {"name": "API Fuzzing", "status": "Pass", "note": "No issues detected"}
        ]
    }
    result = generate_summary_table(sample)
    assert "| Prompt Injection | Fail" in result
    assert "| API Fuzzing | Pass" in result
