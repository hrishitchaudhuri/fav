------------------ MODULE Xor ---------------------
VARIABLES in1, in2

Xor_Out == (in1 /\ ~in2) \/ (~in1 /\ in2)
====================================================