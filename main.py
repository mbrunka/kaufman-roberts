def calc_all(a, t, v, m, round_lvl=2):
    """
    calc_all calculates all needed components and then returns them as
    list of lists in order [[x0, x1, ...][P0, P1, ...][b1, b2, ...]]

    Names of functions contained in calc_all are self explenatory

    Args:
        a (list of floats): as in formula
        t (list of floats): _description_
        v (int): _description_
        m (int): _description_
        round_lvl (int, optional):
            how many numbers after "," for all calculated componets.
            Defaults to 2.
    """

    def calc_x(v, m, a, t, round_lvl):
        x = [1] * (v + 1)
        for n in range(1, v + 1):
            sum = 0
            for i in range(0, m):
                if n >= t[i]:
                    sum += a[i] * t[i] * x[n - t[i]]
            x[n] = round(sum / n, round_lvl)
        return x

    def calc_p0(x, round_lvl):
        sum = 0
        for xi in x:
            sum += xi
        return round(1 / sum, round_lvl)

    def calc_pn(x, v, m, a, t, round_lvl):
        p = [1] * (v + 1)
        p[0] = calc_p0(x, round_lvl)
        for n in range(1, v + 1):
            sum = 0
            for i in range(0, m):
                if n >= t[i]:
                    sum += a[i] * t[i] * p[n - t[i]]
            p[n] = round(sum / n, round_lvl)
        return p

    def calc_bn(p, v, t, i=1):
        sum = 0
        for n in range(v - t[i - 1] + 1, v + 1):
            sum += p[n]
        return sum

    x = calc_x(v, m, a, t, round_lvl)
    p = calc_pn(x, v, m, a, t, round_lvl)
    b = [1] * m
    for i in range(1, m + 1):
        b[i - 1] = calc_bn(p, v, t, i)
    return [x, p, b]


def print_all(results):
    """
    print each variable of result with label in new line

    Args:
        results (list of lists): as returned from calc_all function
    """
    for set, result in enumerate(results):
        print("---------------------")
        print(f"-- Set number: {set+1} --")
        print("---------------------")
        for i, x in enumerate(result[0]):
            print(f"x{i} = {x}")
        for i, p in enumerate(result[1]):
            print(f"P{i} = {x}")
        for i, b in enumerate(result[2]):
            print(f"x{i+1} = {b}")


def print_all_table(results):
    """
    Prints the results of calc_all function.
    Required texttable or use print_all as alternative.

    Args:
        results (list of lists): as returned from calc_all function
    """

    from texttable import Texttable

    header = []

    for i, x in enumerate(results[0][0]):
        header.append(f"x{i}")
    for i, p in enumerate(results[0][1]):
        header.append(f"P{i}")
    for i, b in enumerate(results[0][2]):
        header.append(f"b{i+1}")

    joined_list = []
    for result in results:
        joined_list.append(result[0] + result[1] + result[2])

    print(len(results))

    t = Texttable()
    t.add_rows([header] + joined_list)
    print(t.draw())


def main():
    """
    Main exist only ass test for class asigment
    """
    results = []
    round_lvl = 2
    sets = 5
    a = [[0.4, 1.0], [0.8, 0.8], [1.2, 0.6], [1.6, 0.4], [2.0, 0.2]]
    t = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]
    v = 3
    m = 2

    for s in range(sets):
        results.append(calc_all(a[s], t[s], v, m, round_lvl))

    # print_all(results)

    print_all_table(results)


if __name__ == "__main__":
    main()
