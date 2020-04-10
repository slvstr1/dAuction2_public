#!/usr/bin/env python
# -*- coding: utf-8 -*-
# first, download CONEMU https://conemu.github.io/

#how to install pyomo for the class
# install anaconda https://www.continuum.io/downloads
    # (or miniconda http://conda.pydata.org/miniconda.html)
    # for python 35, 64bit, windows
    # get conda cheatsheat (http://conda.pydata.org/docs/using/cheatsheet.html)
# conda install anaconda-client
# instal anaconda-client (https://docs.continuum.io/anaconda-cloud/using)
# conda install -c conda-forge pyomo=4.3.11377
    # search pyomo on https://anaconda.org/
    # https://anaconda.org/search?q=pyomo
    # https://anaconda.org/conda-forge/pyomo
    # can also install pyomo.extras in same way
# conda install -c cachemeorg glpk=4.57
    # this is hte solver. Search glpk on anaconda.org
    # DO NOT INSTALL gplk 4.60 (or any > 4.57: THERE IS AN ERROR IN IT!!!)

# possible problems: things not in the path, having to use the pip.exe and using the one from Python instead of the one of Anaconda (in C:\Miniconda3\Scripts)


import pyomo.core
import pyomo.environ
from pyomo.opt import SolverFactory

# Import
from pyomo.environ import *

# Creation of a Concrete Model
model = ConcreteModel()
# instance=model.create()
## Define sets ##
#  Sets
#       n   canning plants   / seattle, san-diego /
#       j   markets          / new-york, chncago, topeka / ;
# model.n = Set(initialize=['N1', 'N2', 'N3'], doc='Nodes')
# model.l = Set(initialize=['L1', 'L2', 'L3'], doc='Lines')

N=[1,2,3]
slack=3
# Ndeslacked=[1,2]
# print(N)
Ndeslacked=N.copy()
Ndeslacked.remove(3)
# print("N",N)
# print("Ndeslacked",Ndeslacked)
L=[1,2,3]
PTDF = {
    (1,1): 1,
    (2,1): 1,
    (3,1): 2,
    (1,2): -1,
    (2,2): 2,
    (3,2): 1,}

model.mc = Param(N, initialize={1:70, 2:30, 3:200},  doc='Marginal cost of plant n')
model.lc = Param(L, initialize={1:20, 2:999, 3:999}, doc='Line capacity at line l')

print("model.lc",model.lc)

model.x = Var(N, within=NonNegativeReals)
print("ok5")
model.obj = Objective(expr=sum(model.mc[i]*model.x[i] for i in N))

# model.conl1 = Constraint(expr=sum(model.x[n]*PTDF[n,1] for n in Ndeslacked) <= model.lc[1])
# model.conl2 = Constraint(expr=sum(model.x[n]*PTDF[n,2] for n in Ndeslacked) <= model.lc[2])
# model.conl3 = Constraint(expr=sum(model.x[n]*PTDF[n,3] for n in Ndeslacked) <= model.lc[3])
# def con_flow_rule(model, l):
#     return sum(model.x[n]*PTDF[l,n]/3 for n in Ndeslacked) <= model.lc[l]
def con_flow_rule(model, l):
    return (- model.lc[1],sum(model.x[n]*PTDF[l,n]/3 for n in Ndeslacked),  model.lc[l])
model.con_flow = Constraint(L, rule=con_flow_rule)

# def con_demand_rule(model, l):
#     return  sum(model.x[n]*PTDF[n,l]/3 for n in Ndeslacked) <= model.lc[l]
model.con_demand = Constraint(expr= sum(model.x[n] for n in Ndeslacked) >= 120)


def pyomo_postprocess(options=None, instance=None, results=None):
    model.x.display()

# solve abstract1.py abstract1.dat --solver=glpk

model.dual = Suffix(direction=Suffix.IMPORT_EXPORT)
opt = SolverFactory("glpk")
# results = opt.solve(model)
results = opt.solve(model,suffixes=["dual"],keepfiles=False)
# sends results to stdout
results.write()
print("\nDisplaying Solution\n" + '-p-' * 60)
print(model.x.display())
print(model.dual.display())
# print(Suffix(direction=Suffix.IMPORT))
# model.pprint()
# instance=None
# pyomo_postprocess(None, instance, results)
