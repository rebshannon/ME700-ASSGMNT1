# Functions needed for bisectionMethod.py
# ME 700 Assignment 1
# Rebecca Shannon 1/25/25

import numpy as np

def A_lessThan_B(A: float, B: float):
    """Given A and B, check if A < B"""
    if A > B or A == B: 
        print("FAIL: A should be less than B, exiting") 
        exit()
    else: print("PASS: A is less than B")

# def nIterMaxCheck(nIterMax: float, nIter: float):
#     """Check if nIterMax is a postivie whole number, exits is false"""
#     if nIterMax <= 0 or 

def A_B_signCheck(fA: float, fB: float):
    """Checks if f(A) and f(B) have opposite signs"""
    if np.sign(fA) == np.sign(fB):
        print("FAIL: f(A) and f(B) should have opposite signs:")
        print("f(A) = ",fA)
        print("f(B) = ",fB)
        print("Change inputs A and B")
        print("Exiting")
        exit()
    else: print("PASS: f(A) and f(B) have opposite signs")


def midpoint_A_B(A: float, B: float) -> float:
    """Given two float values. Find the midpoint between them."""
    val = (A + B)/2
    return val

def checkTol(fC: float, tol: float, C: float, nIter: float):
    """Check is f(C) is within the given tolerance"""
    if np.abs(fC) < tol:
        print("Root found in ", nIter, " iterations")
        print("C =", C)
        print("f(C) = ", fC)
        exit()  

def reassignC(fA: float, fB: float, fC: float, A: float, B: float,C: float) -> float:
    """Reassign C to A or B based on the sign of f(C)"""
    if np.sign(fC) == np.sign(fA): 
        valA = C
        valB = B
    else: 
        valA = A
        valB = C
    return valA, valB

def maxIterReached(nIterMax: float, nIter: float, C: float):
    """Check if the naximum number of iterations has been reached and exit"""
    if nIter == nIterMax:
        print("Max number of iteractions exceeded.")
        print("Last value found: C = ",C)
        print("Increase nIterMax or decrease tol")
        print("Exiting")


def testFn(x: float) -> float:
    """Test function to find f(A), f(B), f(C)"""
    val = bisectionMethon.xsqrd(x)
    return val