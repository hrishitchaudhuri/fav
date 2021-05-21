import state
import relations
import labels
import kripke
import formula


s1 = state.State(1)
s2 = state.State(2)
s3 = state.State(3)

S = []
S.append(s1)
S.append(s2)
S.append(s3)

R = relations.Relation()
R.addRelation(s1, s2)
R.addRelation(s2, s1)
R.addRelation(s2, s3)
R.addRelation(s3, s3)

L = labels.Labelling()

p = formula.Proposition('p', True)
q = formula.Proposition('q', True)
P = [p, q]

L.addLabel(s1, p)
L.addLabel(s1, q)
L.addLabel(s2, q)
L.addLabel(s3, p)

TestStructureK = kripke.KripkeStructure(S, s1, R, L, P)