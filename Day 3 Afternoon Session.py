# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:59:04 2019

@author: admin
"""

#Beginner coding Lesson #3
M = "5 milk cholocates,"
d = "3 dark Cholocates,"
w = "and 8 white cholocates."

print("In the box, there are",M,d,w)

print("there")
 t = "armstrong"
 g = "was"
 h = "here"
 
 print("Who was here today?", t,g,h)
 
print("there are")
m = "five nations"
print("there are none!")

print("there are",m,"there are none")


chocolate1= {"milk":5}

chocolate2= {"dark":3}

choloate3= {"white":8}



print("the nubmer of chocolates in the box are", choloatebox)


print("Theses are the pople listed within the profile list",People)

S = {"Steve":32}
L = {"Lia":28}
V = {"Vin":45}
K = {"Katie":38}

print("This profile list both the people and their ages who appiled
      for this job,",S,L,V,K)
    

choloatebox = {"milk":5,"dark":3,"white":8}
print("The number of dark cholocates in cholocate box is", choloatebox["dark"])



print("Lia's age and gender is",People["Lia"])
'''
#Age and Gender
Gender = {"Lia":"Female","Steve":"Male","Vin":"Male","Katie":"Female"}
Age = {"Steve ":32,"Lia":28,"Vin":45,"Katie":38}
print("The age and gender of Vin is",Age["Vin"] ,"and he is a",Gender["Vin"])
print("the age and gender of Lia is",Age["Lia"] , "and she is a",Gender["Lia"]
import(math)

import pandas
dir(pandas)
'''
#panda.Series
life = {"milk":5,"dark":8,"white":3}
lifeinfo = pandas.Series(life)
print(lifeinfo)

print(lifeinfo)

InsectWorld = {"ladybug":34,"beetles":43,"moths":89}
InsectWorldinfo = pandas.Series(InsectWorld)
print(InsectWorldinfo)


#panda.DataFrames
chocolatedata =(InsectWorld)
print(chocolatedata)
      
chocolatedf = pandas.DataFrame(chocolatedata, index=["quantity","list"])
print(chocolatedf)


Age = {"Brianna":23,"Masafa":24,"Christopher":24,"Darrion":25}
Gender = {"Brianna":"Female","Masafa":"Male","Christopher":"Male","Darrion":"Male"}

AG =(Age,Gender)
print(AG)

Agdf = pandas.DataFrame(AG, columns=["Name","Age","Gender"])
print(AGdf)

import pandas
dir(pandas)

studentallinfo = (["Brianna",23,"Female"],["Masafa",24,"Male"],["Christopher",24,"Male"],[
        "Darrion",25,"Male"])
df=pandas.DataFrame(studentallinfo)
print(df)

df1=pandas.DataFrame(studentallinfo)
print(df1)

df2=pandas.DataFrame(studentallinfo, columns=["Name","Age","Gender"])
print(df2)



