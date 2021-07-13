import pad

nodes = [pad.Node(1, True, "in[i] = out"), pad.Node(2, False, "in[i] /= out")]
edges = [pad.Edge(1, 1, 1, "\E j /= i : Input(j)"), pad.Edge(1, 2, 2, "Input(i)"), pad.Edge(2, 2, 3, "\E j /= i : Input(j)"), pad.Edge(2, 1, 4, "Output")]
vars = ["in", "out"]

spec = pad.PredicateActionDiagram(nodes, edges, vars)

specstr = spec.getTLAvariables() + spec.convert2TLAbody("celem")
print(specstr)
