from moore import Moore
from mstate import mState
from mrelation import mRelation
from prop import Prop

f0 = mState(True, "f0")
f01 =  mState(False, "f01")
f1 =  mState(False, "f1") 
f10 = mState(False, "f10")

S = [f0, f01, f1, f10]

I = ["switch_up", "on_floor"]

O = ["on_ground", "lift_up", "on_first", "lift_down"]

R = mRelation()
R.addRelation(f0, f0, Prop([[0, 1], [0, 0]]))
R.addRelation(f0, f01, Prop([[1, 0], [1, 1]]))
R.addRelation(f01, f01, Prop([[0, 0], [1, 0]]))
R.addRelation(f01, f1, Prop([[0, 1], [1, 1]]))
R.addRelation(f1, f1, Prop([[1, 0], [1, 1]]))
R.addRelation(f1, f10, Prop([[0, 0], [0, 1]]))
R.addRelation(f10, f10, Prop([[0, 0], [0, 1]]))
R.addRelation(f10, f0, Prop([[0, 1], [1, 1]]))

P = {
    f0 : "on_ground", 
    f01 : "lift_up",
    f1 : "on_first",
    f10 : "lift_down"
}

M = Moore(S, I, O, R, P)
print(M.generateKripke())