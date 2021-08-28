------------------------------ MODULE FourBitIncrementer ------------------------------------
VARIABLES inc, i1, i2, i3, i4

And_Inst0 == INSTANCE And WITH in1 <- inc, in2 <- i1
Xor_Inst0 == INSTANCE Xor WITH in1 <- inc, in2 <- i1

Out0 == Xor_Inst0!Xor_Out

And_Inst1 == INSTANCE And WITH in1 <- And_Inst0!And_Out, in2 <- i2
Xor_Inst1 == INSTANCE Xor WITH in1 <- And_Inst0!And_Out, in2 <- i2

Out1 == Xor_Inst1!Xor_Out

And_Inst2 == INSTANCE And WITH in1 <- And_Inst1!And_Out, in2 <- i3
Xor_Inst2 == INSTANCE Xor WITH in1 <- And_Inst1!And_Out, in2 <- i3

Out2 == Xor_Inst2!Xor_Out

And_Inst3 == INSTANCE And WITH in1 <- And_Inst2!And_Out, in2 <- i4
Xor_Inst3 == INSTANCE Xor WITH in1 <- And_Inst2!And_Out, in2 <- i4

Out3 == Xor_Inst3!Xor_Out

Carry_Out == And_Inst3!And_Out
=============================================================================================