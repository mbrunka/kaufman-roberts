ROUND_LVL = 3


def calc_x(v, m, a, t):
    x = [1] * (v + 1)
    for n in range(1, v + 1):
        sum = 0
        for i in range(0, m):
            if n >= t[i]:
                sum += a[i] * t[i] * x[n - t[i]]
        x[n] = round(sum / n, ROUND_LVL)
    return x


def calc_p0(x):
    sum = 0
    for xi in x:
        sum += xi
    return round(1 / sum, ROUND_LVL)


def calc_pn(x, v, m, a, t):
    p = [1] * (v + 1)
    p[0] = calc_p0(x)
    for n in range(1, v + 1):
        sum = 0
        for i in range(0, m):
            if n >= t[i]:
                sum += a[i] * t[i] * p[n - t[i]]
        p[n] = round(sum / n, ROUND_LVL)
    return p


def calc_bn(p, v, t, i=1):
    sum = 0
    for n in range(v - t[i - 1] + 1, v + 1):
        sum += p[n]
    return sum


def calc_all(a, t, v, m):
    x = calc_x(v, m, a, t)
    p = calc_pn(x, v, m, a, t)
    b = [1] * m
    for i in range(1, m + 1):
        b[i - 1] = calc_bn(p, v, t, i)
    return (x, p, b)


def main():
    # test input
    sets = 5
    a = [[0.4, 1.0], [0.8, 0.8], [1.2, 0.6], [1.6, 0.4], [2.0, 0.2]]
    t = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]
    v = 3
    m = 2
    results = []
    for s in range(sets):
        results.append(calc_all(a[s], t[s], v, m))
    for result in results:
        print(result)

    # Future functionality
    # TODO: user input


if __name__ == "__main__":
    main()
