def prettyprint(iterable):
    for row in iterable:
        print(row)

def format_output(**kwargs):
    """
    format and build output file
    """
    def write_line(out_str, line):
        return out_str + str(line) + '\n'
    out_str = ""
    for param in kwargs:
        out_str = write_line(out_str, param)
        val = kwargs[param]
        if isinstance(val, list) or isinstance(val, set):
            for item in val:
                out_str = write_line(out_str, item)
        else:
            out_str = write_line(out_str, val)
    return out_str
    
def plot(P, E, M, func):
    import matplotlib.pyplot as plt; plt.rcdefaults()
    import matplotlib.pyplot as plt
    trials = 20000
    y_pos = list(range(1,N+1))
    py_performance = [0] * N
    for i in range(trials):
        result = func(N)
        py_performance[int(result)] += 1
    plt.bar(y_pos, py_performance, align="center", alpha=0.5)
    plt.title('Triangular')
    plt.show()