//
// Created by Ethan on 9/13/2023.
//

#include <vector>
#include "action.h"

#ifndef LEARNSOMETHING_HACKATHONBOT_H
#define LEARNSOMETHING_HACKATHONBOT_H

class HackathonBot
{
public:
    HackathonBot();
    void takeAction(float price);
    double getBalance();
    bool isHolding();
    bool threeSeries();

private:
    double balance;
    bool holding;
    std::vector<float> prices;
    int daysUp;
    int daysDown;
    int daysNoFlux;
    int dropsInPrice = 0;
};

#endif // LEARNSOMETHING_HACKATHONBOT_H
