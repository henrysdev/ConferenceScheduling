def prettyprint(iterable):
    for row in iterable:
        print(row)
    
def plot(P, E, M):
    import matplotlib.pyplot as plt; plt.rcdefaults()
    import matplotlib.pyplot as plt
    trials = 20000
    y_pos = list(range(1,N+1))
    py_performance = [0] * N
    for i in range(trials):
        result = triangular(N)
        py_performance[int(result)] += 1
    plt.bar(y_pos, py_performance, align="center", alpha=0.5)
    plt.title('Triangular')
    plt.show()