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

m.addConstr(10.5*a + 8.3*b + 10.2*c + 7.2*d + 12.3*e + 9.2*f <= 60)
m.addConstr(14.4*a + 12.6*b + 14.2*c + 10.5*d + 10.1*e + 7.8*f <= 70)
m.addConstr(2.2*a + 9.5*b + 5.6*c + 7.5*d + 8.3*e + 6.9*f <= 35)
m.addConstr(2.4*a + 3.1*b + 4.2*c + 5*d + 6.3*e + 5.1*f <= 20)

# m.addConstr(b <= f) -> For solution b.

m.optimize()