---- MODULE MC ----
EXTENDS Elevator, TLC

\* INIT definition @modelBehaviorNoSpec:0
init_16234653598713000 ==
FALSE/\on_ground = 0
----
\* NEXT definition @modelBehaviorNoSpec:0
next_16234653598714000 ==
FALSE/\on_ground' = on_ground
----
=============================================================================
\* Modification History
\* Created Sat Jun 12 08:05:59 IST 2021 by hp
