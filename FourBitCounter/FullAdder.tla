------------------ MODULE FullAdder ---------------------
VARIABLES i1, i2, cin

InstXor_0 == INSTANCE Xor WITH in1 <- i1, in2 <- i2
InstXor_1 == INSTANCE Xor WITH in1 <- InstXor_0!Xor_Out, in2 <- cin

FullAdder_Sum == InstXor_1!Xor_Out

InstAnd_0 == INSTANCE And WITH in1 <- i1, in2 <- i2
InstAnd_1 == INSTANCE And WITH in1 <- i1, in2 <- cin
InstAnd_2 == INSTANCE And WITH in1 <- i2, in2 <- cin

InstOr_0 == INSTANCE Or WITH in1 <- InstAnd_0!And_Out, in2 <- InstAnd_1!And_Out
InstOr_1 == INSTANCE Or WITH in1 <- InstOr_0!Or_Out, in2 <- InstAnd_2!And_Out

FullAdder_Carry == InstOr_1!Or_Out
===========================================================