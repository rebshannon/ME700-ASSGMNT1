
# ME700 Assignment 1

ME 700 Assignment 1
Rebecca Shannon
1/29/2025

## About the Solver

Uses the bisection method to find the root $(x = C)$ of a provided function $f(x)$ based on the user's initial guesses $(x = A,~B)$. The tolerance and maximum number of iterations are also defined by the user.

## Files included

*bisectionMethod.py* - user should define $A$, $B$, $nIterMax$, and $tol$
*assgnmen_functions.py* - includes python functions necessary for the bisection method

## Using the code

In the *bisectionMethod.py* script, four user inputs are required: two initial guesses $(A$ and $B)$, the maximum number of iterations $(nIterMax)$, and the desired tolerance level $(tol)$. Three conditions must be met for the user inputs:

1. $A < B$
2. $sign[f(A)] \neq sign[f(B)]$
3. $nIterMax$ must be a positive whole number

The function $f(x)$ which is being solved with the bisection method should be defined in a separate Python script and imported as *exSoln*. The solutions to these examples are currently held in *exampleSolutions.py*. In this script,  uncomment the function associated with the example problem that you are atttempting. When moving on to another example, make sure to comment out the old example function.



## Example 1

Use the bisection method to find the root of the following equation:
$$y = x^3 - 1$$

## Example 2
