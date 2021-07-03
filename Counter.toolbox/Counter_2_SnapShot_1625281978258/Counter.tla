---------------------------- MODULE Counter ----------------------------
EXTENDS Integers

VARIABLES P

And(i1, i2) == i1 /\ i2
Xor(i1, i2) == (i1 /\ ~i2) \/ (~i1 /\ i2)

HalfAdder(i1, i2) == [sum |-> And(i1, i2), cout |-> Xor(i1, i2)]

FourBitIncrementer(A, inc) == <<HalfAdder(A[1], inc).sum,
                                HalfAdder(A[2], HalfAdder(A[1], inc).cout).sum,
                                HalfAdder(A[3], HalfAdder(A[2], HalfAdder(A[1], inc).cout).cout).sum,
                                HalfAdder(A[4], HalfAdder(A[3], HalfAdder(A[2], HalfAdder(A[1], inc).cout).cout).cout).sum>> 

Init == P = <<FALSE, FALSE, FALSE, FALSE>>

Next == P' = FourBitIncrementer(P, CHOOSE i \in {TRUE, FALSE} : TRUE)

Spec == Init /\ [][Next]_<<P>>
===========================================================================