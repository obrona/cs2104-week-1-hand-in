from collections.abc import Callable

def sigma0(f: Callable[[int], int], n: int) -> int:
    return sum(f(i) for i in range(n + 1))

def test_constant_func():
    assert(sigma0(lambda x: 1, 10) == 11)

def test_identity_func():
    assert(sigma0(lambda x: x, 10) == 10 * 11 / 2)

test_constant_func()
test_identity_func()

def sigma1(f: Callable[[int], int], n: int) -> int:
    return 0 if n < 1 else sum(f(i) for i in range(1, n + 1))

print('ex6a', [sigma0(lambda x: x // 2, 2 * i) for i in range(10)])
print('ex6b', [sigma0(lambda x: x // 3, 3 * i) for i in range(10)])
print('ex6c', [sigma0(lambda x: x // 4, 4 * i) for i in range(10)])

def ex7f(N: int, x: int) -> int:
    if N == 0:
        return 1
    else:
        return sum(ex7f(N - 1, i) for i in range(x + 1))

print('ex7f', [ex7f(5, i) for i in range(10)])

def ex8(N: int) -> int:
    if N == 0:
        return 1

    def helper(x: int, lvl: int) -> int:
        if lvl == 0:
            return 1
        return sum(helper(i, lvl - 1) for i in range(x + 2))

    return helper(0, N - 1)

print('ex8', [ex8(i) for i in range(10)])

def ex9(N: int) -> int:
    if N == 0:
        return 1

    def helper(x: int, lvl: int) -> int:
        if lvl == 0:
            return 1
        return sum(helper(i, lvl - 1) for i in range(1 - x + 1) if i >= 0)

    return helper(0, N - 1)

print('ex9', [ex9(i) for i in range(10)])

def ex10(N: int) -> int:
    if N == 0:
        return 1
    else:
        return (N + 1) * ex10(N - 1)

print('ex10', [ex10(i) for i in range(10)])

def ex11(N: int) -> int:
    def helper(i: int) -> int:
        if i == N + 1:
            return 1
        else:
            return (i + 1) * helper(i + 1)
    return helper(0)

print('ex11', [ex11(i) for i in range(10)])
