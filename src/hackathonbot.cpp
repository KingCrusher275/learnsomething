//
// Created by Ethan on 9/13/2023.
//

#include "hackathonbot.h"

HackathonBot::HackathonBot()
{
    prices.push_back(100);
    balance = 0;
    holding = true;
    daysUp = 0;
    daysDown = 0;
    daysNoFlux = 0;
    dropsInPrice = 0;
}

void HackathonBot::takeAction(float price)
{
    prices.push_back(price);
    int n = prices.size();

    if (holding)
    {
        if (prices[n - 1] > prices[n - 2])
            daysUp++;
        if (prices[n - 1] < prices[n - 2])
            daysDown++;
        if (prices[n - 1] <= 1.05 * prices[0] && prices[n - 1] >= 0.95 * prices[0])
            daysNoFlux++;
        if (daysUp == 52 || daysDown == 47 || price < 0.38 * prices[0] || price > 1.89 * prices[0] || daysNoFlux == 10 || threeSeries())
        {
            balance += price;
            holding = false;
            prices.clear();
            prices.push_back(price);
            daysUp = daysDown = daysNoFlux = 0;
        }
    }
    else
    {
        if (n > 0 && prices[n - 1] < prices[n - 2])
            dropsInPrice++;
        if ((price < 52 && balance >= price) || dropsInPrice >= 5)
        {
            balance -= price;
            holding = true;
            dropsInPrice = 0;
            prices.clear();
            prices.push_back(price);
        }
    }
}
double HackathonBot::getBalance()
{
    return balance;
}
bool HackathonBot::isHolding()
{
    return holding;
}

bool HackathonBot::threeSeries()
{
    if (prices.size() < 4)
        return false;
    int n = prices.size();
    if (1.2 * prices[n - 4] <= prices[n - 3] && prices[n - 2] <= 0.85 * prices[n - 3] && 1.5 * prices[n - 2] <= prices[n - 1] && prices[n - 4] <= 1.5 * prices[n - 1])
        return true;

    if (0.85 * prices[n - 4] >= prices[n - 3] && prices[n - 2] >= 1.15 * prices[n - 3] && 0.75 * prices[n - 2] <= prices[n - 1] && prices[0] * 0.55 >= prices[n - 1])
        return true;

    return false;
}