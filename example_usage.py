from client import HMMCpgDetector

def main():
    print("=== Testing HMM CpG Island Detector ===")
    hmm = HMMCpgDetector()
    path = hmm.viterbi("CGCGCGCG")
    print("Predicted state sequence (1 = CpG island):", path)

    assert all(st == 1 for st in path)
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
