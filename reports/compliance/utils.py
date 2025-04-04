import json

def load_test_results(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

def generate_summary_table(data):
    # Example format based on sample input structure
    table = "| Test | Result | Notes |\n|------|--------|-------|\n"
    for module in data.get("results", []):
        table += f"| {module['name']} | {module['status']} | {module['note']} |\n"
    return table

def render_template(template_path, summary_table):
    with open(template_path, "r") as f:
        template = f.read()

    # Replace marker with dynamic table
    return template.replace("{{SUMMARY_TABLE}}", summary_table)
