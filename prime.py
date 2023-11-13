import timeit
import math

def disasterCode():
    uniquePrimes = []
    for i in range (2,2500):
        flag = False
        for k in range (len(uniquePrimes)):
            if (i%uniquePrimes[k]==0):
                flag = True
                break
        if(not flag):
            uniquePrimes.append(i)

    for i in range (2,2500):
        currentPrime = i
        for j in range (len(uniquePrimes)):
            checkPrime = uniquePrimes[j]
            while (currentPrime%checkPrime==0):
                currentPrime/=checkPrime
                
            if(currentPrime == 1):
                break

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
