#include <gtest/gtest.h>
#include "pricingutil.h"

TEST(sampleTest, sample)
{
    EXPECT_EQ(4, 4);
}

TEST(pricingUtil, edgeCases)
{
    PricingUtil p;
    p.calcVal(5, 0, 1);
    EXPECT_NEAR(p.getVal(), 4.5, 1e-4);
    p.calcVal(-5, 0.2, 1.5);
    EXPECT_NEAR(p.getVal(), -8.25, 1e-4);
    p.calcVal(-10, -0.1, 1);
    EXPECT_NEAR(p.getVal(), -8, 1e-4);
}