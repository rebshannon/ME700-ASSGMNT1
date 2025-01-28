import fnAssignment1 as testFns

def test_midpoint_A_B():
    assert testFns.midpoint_A_B(2,4) == 3


def test_reassignC():
    assert testFns.reassignC(10, -10, 5, 0, 5, 3) == (3, 5)
    #                       (fA,  fB, fC, A, B, C)   (A, B)