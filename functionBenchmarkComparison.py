import timeit

def compareFunctions(runs, *functions):
    for function in functions:
        print(timeit.timeit(function, number=runs))