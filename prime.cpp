#include <iostream>
#include <chrono>
#include <numeric>
using namespace std::chrono;

void improvedAlgo()
{
    int spf[2500];
    std::iota(spf, spf + 2500, 0);
    for (int i = 2; i < 2500; i++)
    {
        if (spf[i] == i)
        {
            for (int j = i * i; j < 2500; j += i)
            {
                spf[j] = i;
            }
        }

        int curNum = i;
        while (curNum > 1)
            curNum = curNum / spf[curNum];
    }
}
int main()
{
    double tot = 0;
    for (int i = 0; i < 5; i++)
    {
        auto start = high_resolution_clock::now();
        improvedAlgo();
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(stop - start);
        tot += std::chrono::duration<double>(duration).count();
    }
    tot /= 5;
    std::cout << tot << "\n";
}