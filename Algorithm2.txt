# Algorithm 2 Introduction

This file describes the steps of Algorithm 2. Algorithm 2 starts with 1 user request and x Light Bulbs, where x is a number greater than 1. All light bulbs can give a maximum of 500 lumens.
As an example, the document will demonstrate 1 user request and 3 light bulbs, but the principle can be applied to any number of light bulbs greater than 1.

## Calculating Distance

Distances between the User Request Coordinate and the Light Bulb Coordinates are calculated using the distance formula. Algorithm 2 depends on distance from user request to light bulb. In 
essence, further the light bulb, the less lumen it is requested. 

## Determining a 'Common' Value

To show this mathematically,
Assume there are three light bulbs, Light Bulb 1(LB1), Light Bulb 2(LB2) and Light Bulb 3(LB3). 
LB1, LB2 and LB3 are 200 pixels, 360 pixels and 500 pixels away(calculated from the distance formula in the previous section) from the user request. The user wants 140 lumens.
140 lumens = (1/200)*x + (1/360)*x + (1/500)*x 
where x is the 'common' variable that determines the amount of lumens that each light bulb will contribute to the lumen request. 
After solving this, x comes out to be 14324.

## Finding Expected Lumen Distribution

Now, based on the value of x, what each light bulb should be giving to the user will be calculated:
LB1: 14324 * 1/200 = 72 lumens
LB2: 14324 * 1/360 = 40 lumens
LB3: 14324 * 1/500 = 28 lumens
72 + 40 + 28 lumen is equal to 140 lumens. 72, 40 and 28 lumens are expected from LB1, LB2 and LB3 respectively. 
Then it is checked whether the lightbulbs can fulfill their requirements.

## Finding Given Lumen Distribution

Now, the maximum lumens that a light bulb can give is 500. Based on distance, this value will be different when it arrives at where the user request is. Using a slight modification of the 
distance formula, the maximum lumens that the light bulbs can give to the user request are:
LB1: 125 lumens
LB2: 38 lumens
LB3: 20 lumens

## Configuring a new lumen distribution based on the expected and given lumens

The code loops through the expected and the max lumens list and if expected lumens is greater than given lumens for a light bulb, the expected lumens for a light bulb is saved so that it 
is not modified later. The difference between expected and given lumens is calculated and added to a 'difference' variable.

[LB1, LB2, LB3] in that order
Expected: [72, 40, 28]
Given: [125, 38, 20]
LB1 will not enter if statement because given lumens is greater than expected lumens.
LB2 will enter if statement because expected lumens is greater than given lumens. This is a difference of 2 lumens and 2 is added to the difference variable. LB2's expected lumens is set
to 38.
LB3 will enter if statement because expected lumens is greater than given lumens. This is a difference of 8 lumens and 8 is added to the difference variable. LB3's expected lumens is set
to 20.

In the end, LB2 and LB3 are set to give those values, the total difference comes out to 10(2+8) and those 10 lumens, in the 'difference' variable, will be spread to light bulbs whose 
maximum is greater than expected.

The code goes into a while loop that loops until the 'difference' becomes 0(or in some cases, never becomes 0 and the code breaks out of the while loop). That is achieved by using light 
bulbs whose expected values are not set yet. From the example so far, LB1 has not been set yet. User wants 72 lumens from LB1 but since LB2 and LB3 could not meet that requirement, those 
10 lumens are given to LB1 to fulfill. In the end, the expected lumens come out to be: [82, 38, 20].

## Setting Lumens for the Light Bulbs

Using a slightly modified distance formula, the light bulbs are set to a lumen value based on the final expected lumens list.
LB1: 328 lumens
LB2: 494 lumens
LB3: 500 lumens

## Conclusion

Based on the example of 3 light bulbs(each 500 lumens) and 1 user request(140 lumens), the algorithm can be applied to any number of light bulbs(greater than 1) and 1 user request.
The algorithm has a running time of O(number of light bulbs), or simply, O(n), where n is number of light bulbs. 

