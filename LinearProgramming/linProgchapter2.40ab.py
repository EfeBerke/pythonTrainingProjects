import gurobipy as gp
from gurobipy import GRB

m = gp.Model()

# project fractions
x = m.addVars(6, lb=0.0, ub=1.0, vtype=GRB.CONTINUOUS, name="x")

# carryover variables
s1 = m.addVar(lb=0.0, name="s1")
s2 = m.addVar(lb=0.0, name="s2")
s3 = m.addVar(lb=0.0, name="s3")

out1 = [10.5, 8.3, 10.2, 7.2, 12.3, 9.2]
out2 = [14.4, 12.6, 14.2, 10.5, 10.1, 7.8]
out3 = [ 2.2, 9.5, 5.6, 7.5, 8.3, 6.9]
out4 = [ 2.4, 3.1, 4.2, 5.0, 6.3, 5.1]

m.addConstr(gp.quicksum(out1[j]*x[j] for j in range(6)) + s1 == 60.0)
m.addConstr(gp.quicksum(out2[j]*x[j] for j in range(6)) + s2 == 70.0 + s1)
m.addConstr(gp.quicksum(out3[j]*x[j] for j in range(6)) + s3 == 35.0 + s2)
m.addConstr(gp.quicksum(out4[j]*x[j] for j in range(6)) <= 20.0 + s3)

# objective
ret = [324.0, 358.0, 177.5, 148.0, 182.0, 123.5]
m.setObjective(gp.quicksum(ret[j]*x[j] for j in range(6)), GRB.MAXIMIZE)

m.optimize()

