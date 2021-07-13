---------------------------- MODULE Counter ----------------------------
EXTENDS Integers

VARIABLES P

And(i1, i2) == [out |-> i1 /\ i2]
Xor(i1, i2) == [out |-> (i1 /\ ~i2) \/ (~i1 /\ i2)]

HalfAdder(i1, i2) == [sum |-> Xor(i1, i2).out, cout |-> And(i1, i2).out]

(* 
FourBitIncrementer(A, inc) == [out1 |-> HalfAdder(A[1], inc).sum,
                               out2 |-> HalfAdder(A[2], HalfAdder(A[1], inc).cout).sum,
                               out3 |-> HalfAdder(A[3], HalfAdder(A[2], HalfAdder(A[1], inc).cout).cout).sum,
                               out4 |-> HalfAdder(A[4], HalfAdder(A[3], HalfAdder(A[2], HalfAdder(A[1], inc).cout).cout).cout).sum,
                               cout |-> HalfAdder(A[4], HalfAdder(A[3], HalfAdder(A[2], HalfAdder(A[1], inc).cout).cout).cout).cout]
*)

TwoBitIncrementer(A, inc) ==   [out1 |-> HalfAdder(A[1], inc).sum,
                                out2 |-> HalfAdder(A[2], HalfAdder(A[1], inc).cout).sum,
                                cout |-> HalfAdder(A[2], HalfAdder(A[1], inc).cout).cout]
                                
ThreeBitIncrementer(A, inc) == [out1 |-> TwoBitIncrementer(A, inc).out1,
                                out2 |-> TwoBitIncrementer(A, inc).out2,
                                out3 |-> HalfAdder(A[3], TwoBitIncrementer(A, inc).cout).sum,
                                cout |-> HalfAdder(A[3], TwoBitIncrementer(A, inc).cout).cout]
                                
FourBitIncrementer(A, inc) == [ out1 |-> ThreeBitIncrementer(A, inc).out1,
                                out2 |-> ThreeBitIncrementer(A, inc).out2,
                                out3 |-> ThreeBitIncrementer(A, inc).out3,
                                out4 |-> HalfAdder(A[4], ThreeBitIncrementer(A, inc).cout).sum,
                                cout |-> HalfAdder(A[4], ThreeBitIncrementer(A, inc).cout).cout]
                                

Init == P = <<FALSE, FALSE, FALSE, FALSE>>

Next == P' = <<FourBitIncrementer(P, TRUE).out1, FourBitIncrementer(P, TRUE).out2, FourBitIncrementer(P, TRUE).out3, FourBitIncrementer(P, TRUE).out4>>

Spec == Init /\ [][Next]_<<P>>
===========================================================================