def lcs(S, T):
    m = len(S)
    n = len(T)
    counter = [[0] * (n + 1) for x in range(m + 1)]
    longest = 0
    lcs_set = list()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i + 1][j + 1] = c
                if c > longest:
                    lcs_set = list()
                    longest = c
                    lcs_set.append(S[i - c + 1:i + 1])
                elif c == longest:
                    lcs_set.append(S[i - c + 1:i + 1])

    return lcs_set


seq_list = []
with open("test_strings") as f:
    for line in f:
        if line.startswith(">"):
            pass
        else:
            seq_list.append(line.strip())


common = []
for item in range(len(seq_list) - 1):
    common.append(lcs(seq_list[item], seq_list[item + 1]))

all_common_substrings = []
for kmer_list in range(len(common) -1):
    all_common_substrings.append(lcs(common[kmer_list], common[kmer_list + 1]))

print(all_common_substrings)
