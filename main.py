

import pandas as pd

## Lecture de feuilles Fichier Excel
"""

dataframe1 = pd.read_excel('exemple.xlsx', sheet_name = 0) ## Feuille 1

print(dataframe1)

dataframe2 = pd.read_excel('exemple.xlsx', sheet_name = 1)  ## Feuille 2

print(dataframe2)

"""
## Nombre d'element unique dans une colonne
"""
dataframe1 = pd.read_excel('exemple.xlsx', sheet_name = 0) ## Feuille 1

column = dataframe1.values.itemsize

print(dataframe1["ECOLE"].value_counts())  # Combien de fois la valeur iri present muri colonne 
"""




## Lecture des rows
"""
dataframe1 = pd.read_excel('exemple.xlsx', sheet_name = 0) ## Feuille 1

print(len(dataframe1))

rowSize = len(dataframe1)

for x in range(rowSize):
    print(dataframe1['Nom'].loc[dataframe1.index[x]] + " Etudie a " + dataframe1['ECOLE'].loc[
        dataframe1.index[x]] + " a eu " + str(dataframe1['Pourcentage'].loc[dataframe1.index[x]]))
"""


