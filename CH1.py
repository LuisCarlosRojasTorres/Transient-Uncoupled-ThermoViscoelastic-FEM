# -*- coding: utf-8 -*-
"""
TRANSIENT STATE
Resolve através do Metodo dos Elementos Finitos o problema
termo-vicoelastico de geracao de temperatura numa laje submetida a 
carregamento cizalhante.
author: Luis Carlos A. Rojas Torres
email: luiscarlos.bsf@oceanica.ufrj.br
"""
import numpy as np
import FEM1D as f1
from LinearViscoelastic import LinearViscoelastic

f=0.25
dtime=60
TotalTime=60 #en horas
TotalTime*=3600

tau0=150000
lamb=0.214
dc=1150*2200

elastic_modulus = [38,20.14,14.3,9.97,7.25,5.15,3.4,2.1,1.8] #in MPa
relaxation_times =[0.58,3.13,18.72,125.41,1042,10942,159569,5215397]    #in seconds

PU=LinearViscoelastic(elastic_modulus,relaxation_times)
lenght=0.1
numelem = 20
he=lenght/numelem
dy=0
y=23

L=f1.initL(numelem,he)
T=f1.initT(numelem,y)
M=f1.initM(numelem,he,dc,lamb)
K=f1.initK(numelem,he)
F=f1.initF(PU,lamb,T,f,tau0,numelem,he,dy,y)

T=f1.submit_HT(L,T,M,K,F,dtime,TotalTime,PU,lamb,f,tau0,numelem,he,dy,y)