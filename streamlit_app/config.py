import yaml

def load_config(path="config/test_settings.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)
