import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from generator.rag_engine import generate_answer



TEST_CASES = [
    {"query": "Who is the author?", "expected": "John Smith"},
    {"query": "Summarize the article.", "expected": "summary"}
]

def evaluate_all():
    results = []
    for test in TEST_CASES:
        start = time.time()
        answer = generate_answer(test["query"])
        latency = round(time.time() - start, 2)
        correctness = test["expected"].lower() in answer.lower()
        results.append({
            "query": test["query"],
            "expected": test["expected"],
            "answer": answer,
            "correct": correctness,
            "latency": latency
        })
    return results

if __name__ == '__main__':
    from pprint import pprint
    pprint(evaluate_all())