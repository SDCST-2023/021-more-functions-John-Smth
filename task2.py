#!python3
"""
Create a function that calculates the amount of compound interest 
earned.
t = time in years
P = amount invested
n = # of compounding periods per year (how often interest is calculated)
Output should be rounded to 2 decimal places
r = rate of interest as a percentage
"""

def compoundInterest(P,r,t,n):


    R = r/100

    AM1 = R/n
    AM2 = 1 + AM1
    AM3 = n*t
    AM4 = AM2**AM3
    AM5 = P* AM4
    AM6 = round(AM5,2)
    print(AM6)

    return AM6

assert compoundInterest(1000,4,2,4) == 1082.86
assert compoundInterest(2500,4.2,20,12) == 5782.43
assert compoundInterest(83,7,5,365) == 117.78
assert compoundInterest(10000,3,10,2) == 13468.55