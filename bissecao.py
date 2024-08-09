def f(x):
    return x**2 - 2

def bissecao(f, a, b, error = 0.001):
    if a + error < b:
        x = (a + b) / 2
        if f(x) < 0:
            return bissecao(f, x, b)
        else:
            return bissecao(f, a, x)
    return (a + b) / 2

def main():
    print(bissecao(f, 1, 2))

main()