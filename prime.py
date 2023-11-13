import timeit

def disasterCode():
    spf = [i for i in range(2500)]
    for i in range (2,2500):
        if(spf[i] == i):
            for cntr in range(i*i, 2500, i):
                spf[cntr] = i
        
        curNum = i
        while(curNum > 1):
            curNum = curNum // spf[curNum]
        

# Benchmark the code
if __name__ == "__main__":
    benchmark_code = "disasterCode()"
    setup_code = "from __main__ import disasterCode"

    # Measure the execution time of disasterCode function
    times = []
    for i in range(0,5):
        times.append(timeit.timeit(benchmark_code, setup=setup_code, number=1))

    res = sum(times)/5

    print(f"Average execution time after 5 runs: {res:.6f} seconds")
