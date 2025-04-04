import json
import random
import requests

class PromptInjector:
    def __init__(self, model_endpoint, headers=None):
        self.endpoint = model_endpoint
        self.headers = headers or {}

        with open('modules/prompt_injection/payloads.json') as f:
            self.payloads = json.load(f)

    def run_tests(self, base_prompt):
        results = []

        for attack in self.payloads:
            crafted = base_prompt + attack["payload"]
            response = self._send_prompt(crafted)
            results.append({
                "payload": attack["payload"],
                "response": response,
                "type": attack["type"]
            })

        return results

    def _send_prompt(self, prompt):
        data = {"prompt": prompt}
        res = requests.post(self.endpoint, json=data, headers=self.headers)
        return res.text if res.ok else f"Error: {res.status_code}"
