import sys
import json
from client import HMMCpgDetector

def main():
    hmm = HMMCpgDetector()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "detect":
            states = hmm.viterbi(params.get("sequence", ""))
            res = {"states": states}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
