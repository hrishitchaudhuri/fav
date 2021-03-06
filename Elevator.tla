----------------------------- MODULE Elevator -----------------------------
EXTENDS Integers

VARIABLES on_floor, switch_up, on_ground, lift_up, on_first, lift_down

Init == /\  on_floor = 1
        /\  switch_up \in {0, 1}
        /\  on_ground = 1
        /\  lift_up = 0 
        /\  on_first = 0
        /\  lift_down = 0
        
Input_SU == \/  /\  switch_up = 1
                /\  IF on_ground = 1 
                        THEN /\ on_ground' = 0
                             /\ lift_up' = 1
                             /\ lift_down' = lift_down
                             /\ on_first' = on_first
                             
                        ELSE /\ on_first = 1
                             /\ on_first' = on_first
                             /\ on_ground' = on_ground
                             /\ lift_up' = lift_up
                             /\ lift_down' = lift_down
                             
            \/  /\  switch_up = 0
                /\  IF on_first = 1
                        THEN /\ on_first' = 0
                             /\ lift_down' = 1
                             /\ lift_up' = lift_up
                             /\ on_ground' = on_ground
                             
                        ELSE /\ on_ground = 1
                             /\ on_ground' = on_ground
                             /\ on_first' = on_first
                             /\ lift_down' = lift_down
                             /\ lift_up' = lift_up
                    
Input_OF == \/  /\  on_floor = 1
                /\  IF lift_up = 1
                        THEN /\ lift_up' = 0
                             /\ on_first' = 1
                             /\ lift_down' = lift_down
                             /\ on_ground' = on_ground
                        
                        ELSE /\ lift_down = 1
                             /\ lift_down' = 0
                             /\ on_ground' = 1
                             /\ on_first' = on_first
                             /\ lift_up' = lift_up
                             
            \/  /\  on_floor = 0
                /\  lift_up = 1 \/ lift_down = 1
                /\  lift_down' = lift_down
                /\  on_ground' = on_ground
                /\  on_first' = on_first
                /\  lift_up' = lift_up
                    
                             
Next_IP == /\   switch_up' = CHOOSE x \in {0, 1} : TRUE
           /\   on_floor' = CHOOSE x \in {0, 1} : TRUE

Next == Next_IP /\ (Input_SU \/ Input_OF)

Spec == Init /\ [][Next]_<<switch_up, on_first, on_ground, lift_up, on_floor, lift_down>>

-----------------------------------------------------------------------------

THEOREM Spec => \/ (on_ground = 1 /\ lift_up = 1 /\ on_first = 0 /\ lift_down = 0)
                \/ (on_ground = 0 /\ lift_up = 1 /\ on_first = 1 /\ lift_down = 0)
                \/ (on_ground = 0 /\ lift_up = 0 /\ on_first = 1 /\ lift_down = 1)
                \/ (on_ground = 1 /\ lift_up = 0 /\ on_first = 0 /\ lift_down = 1)


=============================================================================