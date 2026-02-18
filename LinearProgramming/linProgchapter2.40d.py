import gurobipy as gp
from gurobipy import GRB

m = gp.Model()

a = m.addVar(lb=0.0, ub=1.0)
b = m.addVar(lb=0.0, ub=1.0)
c = m.addVar(lb=0.0, ub=1.0)
d = m.addVar(lb=0.0, ub=1.0)
e = m.addVar(lb=0.0, ub=1.0)
f = m.addVar(lb=0.0, ub=1.0)

m.setObjective(324*a + 358*b + 177.5*c + 148*d + 182*e + 123.5*f , GRB.MAXIMIZE)

m.addConstr(29.5*a + 33.5*b + 34.2*c + 30.2*d + 37*e + 29*f <= 185)



m.optimize()