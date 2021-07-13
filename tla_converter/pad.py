class Node:
    def __init__(self, id, init, pred):
        """
        id : number uniquely identifying current node.
        init : Boolean value indicating whether current node is an initial node in PAD
        pred : TLA predicate labelling node.
        """

        self.id = id
        self.isInit = init
        self.predicate = pred

class Edge:
    def __init__(self, src_id, dest_id, edge_id, label):
        """
        src_id : ID of source node of current edge.
        dest_id : ID of destination node of current edge.
        label : TLA action labelling edge.
        """

        self.source = src_id
        self.dest = dest_id
        self.id = edge_id
        self.action = label

class PredicateActionDiagram:
    def __init__(self, N, E, V):
        self._nodes = N
        self._edges = E
        self._variables = V

    def getInitialSet(self):
        initset = []
        for node in self._nodes:
            if node.isInit:
                initset.append(node.id)

    def getTLAvariables(self):
        var_str = ""
        for node in self._nodes:
            var_str += "E(" + str(node.id) + ") == <<"
            for edge in self._edges:
                if edge.source == node.id:
                    var_str += str(edge.id) + ", "
            var_str += ">>\n\n"
            
            var_str += "P(" + str(node.id) + ") == " + node.predicate +"\n\n"
        
        return var_str

    def convert2TLAbody(self, moduleName):
        init = "Init == \E n \in I : P(n)\n\n"
        for node in self._nodes:
            init += "A(" + str(node.id) + ") == \E e \in E(n) : Eps(e) /\ P(d(e))\n\n"

        init += moduleName + " == Init /\ \A n \in N : [][P(n) => A(n)]<<"
        for v in range(len(self._variables)):
            if v == len(self._variables) - 1:
                init += self._variables[v]
            else:
                init += self._variables[v] + ", "

        init += ">>\n"

        return init
