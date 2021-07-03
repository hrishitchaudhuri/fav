---------------------------- MODULE Counter ----------------------------
EXTENDS Integers

VARIABLES P

And(i1, i2) == i1 /\ i2
Xor(i1, i2) == (i1 /\ ~i2) \/ (~i1 /\ i2)

HalfAdder(i1, i2) == [sum |-> Xor(i1, i2), cout |-> And(i1, i2)]

boolToInt(m) == IF m = TRUE THEN 1 ELSE 0 

FourBitIncrementer(A, inc) == <<HalfAdder(A[1], inc).sum,
                                HalfAdder(A[2], HalfAdder(A[1], inc).cout).sum,
                                HalfAdder(A[3], HalfAdder(A[2], HalfAdder(A[1], inc).cout).cout).sum,
                                HalfAdder(A[4], HalfAdder(A[3], HalfAdder(A[2], HalfAdder(A[1], inc).cout).cout).cout).sum>> 

Init == P = <<FALSE, FALSE, FALSE, FALSE>>

Next == P' = FourBitIncrementer(P, TRUE)

Spec == Init /\ [][Next]_<<P>>
===========================================================================