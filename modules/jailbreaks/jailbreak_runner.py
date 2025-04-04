import requests

class JailbreakTester:
    def __init__(self, model_endpoint, jailbreak_list_path):
        self.endpoint = model_endpoint
        with open(jailbreak_list_path, 'r') as f:
            self.payloads = [line.strip() for line in f.readlines()]

    def run(self):
        results = []
        for payload in self.payloads:
            response = requests.post(self.endpoint, json={"prompt": payload})
            results.append({
                "payload": payload,
                "status": "success" if response.ok else "error",
                "output": response.text
            })
        return results
