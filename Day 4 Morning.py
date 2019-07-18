# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:03:57 2019

@author: admin
"""


import pandas
import plotly 

studentlist =[["steve",32,"male"],["Lia",28,"female"],["Vin",45,"male"],["jason"
              ,36,"male"]]
print(studentlist)

studentlistdf = pandas.DataFrame(studentlist, columns = ["name","age","gender"], 
                                 index = [1,2,3,4])
print(studentlistdf)


#graph our data
import plotly
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go

agename = go.Bar(x=studentlistdf["name"], y=studentlistdf["age"])
 plot([agename])

import pd
from plotly.offline import plot
import plotly.graph_objs as go

df = pd.read_excel("GISdata.xls)
