import math
from collections.abc import Callable


def sigma(fn: Callable[[int], int], begin: int, n: int) -> int:
    ls = []
    for i in range(n + 1):
        ls.append(fn(i))

    return sum(ls)


# 5.b
def sigma_0(fn: Callable[[int], int], n: int) -> int:
    return sigma(fn=fn, begin=0, n=n)


# 5.a, 5.c
def test_sigma_0():
    # passthrough
    n = 10
    actual = sigma_0(lambda x: x, n)
    expected = int((n * (n + 1)) / 2)
    assert (
        actual == expected
    ), "An identity function should return the sum of all numbers in [0, n]"

    # doubler
    n = 3
    actual = sigma_0(lambda x: 2 * x, n)
    expected = 1 * 2 + 2 * 2 + 3 * 2
    assert (
        actual == expected
    ), "A doubler function should return the sum of the double of each number in [0, n]"

    # negative
    n = -3
    actual = sigma_0(lambda x: x, n)
    expected = 0
    assert actual == expected, "A negative n should always be 0"


test_sigma_0()


# 5.d
def sigma_1(fn: Callable[[int], int], n: int) -> int:
    return sigma(fn=fn, begin=1, n=n)


# 6.a - 6.d
def ex_6():
    range_max = 10

    def create_floored_divide(n: int):
        return lambda x: math.floor(x / n)

    m = 2
    print("6.a.", [sigma_0(create_floored_divide(m), n * m) for n in range(range_max)])

    m = 3
    print("6.b.", [sigma_0(create_floored_divide(m), n * m) for n in range(range_max)])

    m = 4
    print("6.c.", [sigma_0(create_floored_divide(m), n * m) for n in range(range_max)])

    m = 1
    print("6.d.", [sigma_0(create_floored_divide(m), n * m) for n in range(range_max)])


ex_6()


def ex_7_b_to_e():
    def create_nested(N: int) -> Callable[[int], int]:
        if N == 0:
            return lambda x: 1
        return lambda x: sum([create_nested(N - 1)(i) for i in range(x + 1)])

    range_max = 10

    print("7.b.", [create_nested(1)(i) for i in range(range_max)])

    print("7.c.", [create_nested(2)(i) for i in range(range_max)])

    print("7.d.", [create_nested(3)(i) for i in range(range_max)])

    print("7.e.", [create_nested(4)(i) for i in range(range_max)])


ex_7_b_to_e()


def ex_7_f():
    def create_nested(N: int) -> Callable[[int], int]:
        if N == 0:
            return lambda x: 1
        return lambda x: sum([create_nested(N - 1)(i) for i in range(x + 1)])

    def fn(N: int, x: int) -> int:
        return create_nested(N)(x)

    range_max = 10

    print("7.f.")
    for N in range(1, range_max):
        print(f"    N = {N}", [fn(N, i) for i in range(range_max)])


ex_7_f()


def ex_8():
    def fn(N: int, max_value: int = 0) -> int:
        if N == 0:
            return 1
        return sum([fn(N=N - 1, max_value=iN + 1) for iN in range(max_value + 1)])

    print("8.", [fn(N) for N in range(10)])


ex_8()


def ex_9():
    def fn(N: int, max_value: int = 0) -> int:
        if N == 0:
            return 1
        return sum([fn(N=N - 1, max_value=1 - iN) for iN in range(max_value + 1)])

    print("9.", [fn(N) for N in range(10)])


ex_9()


def ex_10():
    def fn(N: int) -> int:
        if N == 0:
            return 1
        return sum([fn(N - 1) for i in range(N + 1)])

    print("10.", [fn(N) for N in range(10)])


ex_10()


def ex_11():
    def fn_(N: int, curr: int = 0) -> int:
        if N == 0:
            return 1
        if curr == N - 1:
            return sum([i for i in range(N + 1)])
        return sum([fn_(N, curr + 1) for i in range(curr + 1)])

    def fn(N: int) -> int:
        return fn_(N)

    print("11.", [fn(N) for N in range(10)])


ex_11()
