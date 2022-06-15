def multiplicate(A: list) -> list:
    len_array = len(A)
    before = [1] * len_array
    after = [1] * len_array
    for i in range(1, len_array):
        before[i] = before[i - 1] * A[i - 1]
        after[-i - 1] = after[-i] * A[-i]
    res = []
    for i in range(len_array):
        res.append(before[i] * after[i])
    return res


if __name__ == "__main__":
    print(multiplicate([1, 2, 3, 4]))
