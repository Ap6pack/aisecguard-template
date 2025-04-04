import json
import requests

class APIFuzzer:
    def __init__(self, api_endpoint, payloads_file):
        self.endpoint = api_endpoint
        with open(payloads_file, 'r') as f:
            self.payloads = json.load(f)

    def run_tests(self):
        results = []
        for p in self.payloads:
            response = requests.post(self.endpoint, json=p)
            results.append({
                "input": p,
                "status_code": response.status_code,
                "response": response.text
            })
        return results
