# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 19:20:12 2020

@author: ygorm
"""

import pandas as pd
import matplotlib.pyplot as plt

covidcities = pd.read_csv("brazil_covid19/brazil_covid19_cities.csv")

covidcordenates = pd.read_csv("brazil_covid19/brazil_cities_coordinates.csv")

idhcities = pd.read_csv("brazilian_cities/BRAZIL_CITIES_2.csv")

gini = pd.read_csv("ginibr_1.csv")

gini.head()

newgini = gini["Municipio"].str.split(" ",n=1,expand=True)

gini["code"] = newgini[0]

giniarrumado = gini[["code","gini"]]

idhcities.head()

covidcordenates.head()

covidcordenateslimpo = covidcordenates[covidcordenates["state_code"] == 31]

covidcordenateslimpo2 = covidcordenateslimpo[["name","lat","long"]]

idhlimpo = idhcities[["name","IDHM","IBGE_RES_POP","IBGE_POP"]]

covidcordenateslimpo.head()

covidcities.head()

covidmg = covidcities[covidcities["state"]  == "MG"]

covidmg.head()

covidmarco = covidmg[covidmg["date"] == "2020-03-31"]

uniao = pd.merge(covidmarco,covidcordenateslimpo2,how='left',on='name')

uniao2 = pd.merge(uniao,idhlimpo,how='left',left_on=uniao["name"].str.lower(),right_on=idhlimpo["name"].str.lower())

tabelafinal = uniao2[["name_x","cases","IDHM","IBGE_POP"]]

covidmarco.head()

tabelafinal.to_csv("covid_31_3.csv")
