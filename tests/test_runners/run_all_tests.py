from test_prompt_injection import run_prompt_injection_tests
from test_jailbreaks import run_jailbreak_tests
from test_api_fuzzing import run_api_fuzz_tests
from test_privacy_attacks import run_privacy_tests

def main():
    print(\"[+] Running Prompt Injection Tests...\")
    run_prompt_injection_tests()

    print(\"[+] Running Jailbreak Tests...\")
    run_jailbreak_tests()

    print(\"[+] Running API Fuzzing Tests...\")
    run_api_fuzz_tests()

    print(\"[+] Running Privacy Attacks...\")
    run_privacy_tests()

if __name__ == \"__main__\":
    main()
