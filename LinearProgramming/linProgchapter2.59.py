import gurobipy as gp
from gurobipy import GRB

m = gp.Model()

# For site 1' s calculation
a8 = m.addVar(lb=0.0)
a9= m.addVar(lb=0.0)
a10 = m.addVar(lb=0.0)
a11 = m.addVar(lb=0.0)
a1 = m.addVar(lb=0.0)
a2 = m.addVar(lb=0.0)
a3 = m.addVar(lb=0.0)
a4 = m.addVar(lb=0.0)

m.setObjective(a8 + a9 + a10 + a11 + a1 + a2 + a3 + a4  , GRB.MINIMIZE)

m.addConstr(a8 >= 2) # Demand for 8 - 9
m.addConstr(a8 + a9 >= 2) # Demand for 9 - 10
m.addConstr(a8 + a9 + a10 >= 4) # Demand for 10 - 11
m.addConstr(a9 + a10 + a11 >= 3) # Demand for 11 - 12
m.addConstr(a10 + a11 >= 3) # Demand for 12 - 1
m.addConstr(a11 + a1 >= 2) # Demand for 1 - 2
m.addConstr(a1 + a2 >= 2) # Demand for 2 - 3
m.addConstr(a1 + a2 + a3 >= 2) # Demand for 3 - 4
m.addConstr(a2 + a3 + a4 >= 2) # Demand for 4 - 5


m.optimize()

for v in m.getVars():
    print(v.VarName, "Value:", v.X)