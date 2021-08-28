------------------ MODULE FlipFlop ----------------------
VARIABLES State

Input(sign) == State = sign

Output == State

Next(sign) == State' = sign
=========================================================