---------------------------- MODULE Counter ----------------------------
EXTENDS Integers

VARIABLES P

And(i1, i2) == [out |-> i1 /\ i2]
Xor(i1, i2) == [out |-> (i1 /\ ~i2) \/ (~i1 /\ i2)]

HalfAdder(i1, i2) == [sum |-> Xor(i1, i2).out, cout |-> And(i1, i2).out]

FourBitIncrementer(A, inc) == [out1 |-> HalfAdder(A[1], inc).sum,
                               out2 |-> HalfAdder(A[2], HalfAdder(A[1], inc).cout).sum,
                               out3 |-> HalfAdder(A[3], HalfAdder(A[2], HalfAdder(A[1], inc).cout).cout).sum,
                               out4 |-> HalfAdder(A[4], HalfAdder(A[3], HalfAdder(A[2], HalfAdder(A[1], inc).cout).cout).cout).sum,
                               cout |-> HalfAdder(A[4], HalfAdder(A[3], HalfAdder(A[2], HalfAdder(A[1], inc).cout).cout).cout).cout]

Init == P = <<FALSE, FALSE, FALSE, FALSE>>

Next == P' = <<FourBitIncrementer(P, TRUE).out1, FourBitIncrementer(P, TRUE).out2, FourBitIncrementer(P, TRUE).out3, FourBitIncrementer(P, TRUE).out4>>

Spec == Init /\ [][Next]_<<P>>
===========================================================================