import state
import relations
import labels
import kripke
import formula

if __name__=='__main__':
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

    L.addLabel(s1, p)
    L.addLabel(s1, q)
    L.addLabel(s2, q)
    L.addLabel(s3, p)

    K = kripke.KripkeStructure(S, 1, R, L)

    print(K)

    """
    K.labelNot(p)
    K.labelNot(q)
    """

    K.labelEU(p, q)
    print(K)

    K.labelAnd(p, q)

    print(K)