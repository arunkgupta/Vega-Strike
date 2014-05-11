# -*- coding: utf-8 -*-
"""
/***************************************************************************
 A python module to extract translatable texts from CSV files in Vega Strike, 
and put them in another CSV file, formates for csv2po.
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import csv
import os

liste=[]
folder="/home/vincent/vs_intern/Vega-Strike/data/units"
for file in os.listdir(folder):
    if file.endswith(".csv"):
        print file
        with open(folder+'/'+file , 'r') as csvfile:
            spamreader=csv.reader(csvfile, delimiter=',', quotechar='"')
            i=1
            for row in spamreader:
                if i==1:
                    if row[1]!='Name':
                        print 'pas bon fichier'
                        break
                if i>3:
                    liste.append([folder+"/"+file+":"+str(i),'"'+row[1]+'"'])
                i=i+1

#il me faut les valeurs au format [[loc1,txt1],[loc2,txt1],[loc3,txt2]...]  OK

values = set(map(lambda x:x[1], liste))
newlist = [[';'.join([y[0] for y in liste if y[1]==x]),x] for x in values]
#newtext=', '.join(str(x) for x in newlist)
#newtext2=', '.join(str(x) for x in newtext)

#la première ligne : map permet d'attribuer à chaque valeur de list une fonction créée "à la volée" (c'est à ca que sert "lambda"), qui associe à chaque élément x de liste la valeur x[1] = le second élément de chaque item de list.
#2ème ligne : pour chaque item de values (=les seconds éléments de chaque item de list), on fait une liste des 1ers élements de list (y) qui lui correspondent si le second élément =x. Cela créée une liste de tous les 1ers élements qui correspondent à un 2ème élément.
#cf. http://stackoverflow.com/questions/5695208/group-list-by-values

# problème :  l'outil .write exige des chaînes de caractères, et je lui offre des listes. transformer avec .join?
# problème résolu en indiquant "newfile.write(str(i)) (et pas (i) seulement).
# en revanche, le séparateur entre les locations est le même qu'entre les locations et la source. A améliorer pour que toutes les locations soient dans une colonne du csv.
#Résolu avec un ";".join()( sur les listes de localisation => chaines séparées par un ;
#Pb résolu : choisir les fichiers CSV qui ont la bonne configuration ('Name' dans 2nde colonne) : ajout d'un test "if row[1]!='Name' dans la boucle For.
#pb : virer les crochets. Résolu avec un "','.join(i)" au moment d'écrire dans le fichier cible.
#pb : qd plusieurs locations, les séparer avec un espace, sans que les / deviennent "%2F".

with open('/home/vincent/vs_intern/Vega-Strike/data/i18n/fr/LC_MESSAGES/vegastrike_csv.csv', 'w') as newfile:
    newfile.write ('"location","source","target"\n')
    for i in newlist:
        newfile.write(','.join(i))
        newfile.write('\n')
newfile.close()
