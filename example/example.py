def sum_to_N(N):
    num_1 = 1
    num_2 = 1

    if N < 1:
        return 0
    else:
        for i in range(N):
            res = num_1 + num_2
            num_1 = num_2
            num_2 = res
        return res


if __name__ == "__main__":
    print(sum_to_N(10))
