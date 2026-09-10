import math

class HMMCpgDetector:
    """
    Hidden Markov Model (HMM) for CpG Island Detection.
    Decodes hidden states (CpG vs non-CpG) via dynamic programming Viterbi paths.
    """
    def __init__(self):
        self.trans = [[0.9, 0.1], [0.2, 0.8]]
        self.emit = [
            {"A": 0.3, "C": 0.2, "G": 0.2, "T": 0.3},
            {"A": 0.15, "C": 0.35, "G": 0.35, "T": 0.15}
        ]

    def viterbi(self, obs):
        v = [{0: math.log(0.5) + math.log(self.emit[0][obs[0]]),
              1: math.log(0.5) + math.log(self.emit[1][obs[0]])}]
        path = {0: [0], 1: [1]}

        for t in range(1, len(obs)):
            new_v = {}
            new_path = {}
            for curr_st in (0, 1):
                best_prob, best_prev = max(
                    (v[t - 1][prev_st] + math.log(self.trans[prev_st][curr_st]) + math.log(self.emit[curr_st][obs[t]]), prev_st)
                    for prev_st in (0, 1)
                )
                new_v[curr_st] = best_prob
                new_path[curr_st] = path[best_prev] + [curr_st]
            v.append(new_v)
            path = new_path

        best_final = max(v[-1], key=v[-1].get)
        return path[best_final]
