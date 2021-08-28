------------------ MODULE HalfAdder ---------------------
VARIABLES i1, i2

InstAnd == INSTANCE And WITH in1 <- i1, in2 <- i2
InstXor == INSTANCE Xor WITH in1 <- i1, in2 <- i2

HalfAdder_Carry == InstAnd!And_Out
HalfAdder_Sum == InstXor!Xor_Out
===========================================================