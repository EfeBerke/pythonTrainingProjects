import gurobipy as gp
from gurobipy import GRB

m = gp.Model()

# For site 1' s calculation
x1 = m.addVar(lb=0.0, ub=1.0)
y1 = m.addVar(lb=0.0, ub=1.0)
z1 = m.addVar(lb=0.0, ub=1.0)
t1 = m.addVar(lb=0.8, ub=1.0)
v1 = m.addVar(lb=0.0, ub=1.0)

m.setObjective(1000*x1 + 2100*y1 + 2350*z1 + 1850*t1 + 2950*v1 + 30000 , GRB.MINIMIZE)

m.addConstr(20*x1 + 50*y1 + 50*z1 + 30*t1 + 60*v1 == 180)


m.optimize()




n = gp.Model()

# For site 2' s calculation
x2 = n.addVar(lb=0.0, ub=1.0)
y2 = n.addVar(lb=0.0, ub=1.0)
z2 = n.addVar(lb=0.6, ub=1.0)
t2 = n.addVar(lb=0.0, ub=1.0)


n.setObjective(2800*x2 + 1900*y2 + 2800*z2 + 2500*t2 + 32000, GRB.MINIMIZE)
n.addConstr(80*x2 + 60*y2 + 50*z2 + 70*t2 == 180)

n.optimize()

print("------------------------------------------------")

# print only objective value
if m.status == GRB.OPTIMAL:
    print(m.ObjVal) # -> 38683.33 

# print only objective value
if n.status == GRB.OPTIMAL:
    print(n.ObjVal) # -> 38737.14

