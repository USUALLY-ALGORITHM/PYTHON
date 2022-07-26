def solution(s):
    s_len = len(s)
    answer = [''] * (s_len // 2)
    for i in range(s_len // 2):
        base = s[:i + 1]
        count = 1
        for j in range(i + 1, len(s), i + 1):
            new = s[j:i + j + 1]
            if base == new:
                count += 1
            else:
                if count != 1:
                    answer[i] += str(count)
                answer[i] += base
                count = 1
                base = new
        if count != 1:
            answer[i] += str(count)
        answer[i] += base

        s_len = min(len(answer[i]), s_len)

    return s_len