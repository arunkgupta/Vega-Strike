# -*- coding: utf-8 -*-
"""
/***************************************************************************
 A python module to extract translatable texts from CSV files in Vega Strike, 
and put them in another CSV file, formated for csv2po.
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
folder="/home/user/vs_intern/Vega-Strike/data/units"
for file in os.listdir(folder):
    if file.endswith(".csv"):
        print file
        with open(folder+'/'+file , 'r') as csvfile:
            spamreader=csv.reader(csvfile, delimiter=',', quotechar='"')
            i=1
            for row in spamreader:
                if i==1:
                    if row[1]!='Name':
                        break
                if i>3:
                    liste.append([folder+"/"+file+":"+str(i),'"'+row[1]+'"'])
                i=i+1

values = set(map(lambda x:x[1], liste))
newlist = [[';'.join([y[0] for y in liste if y[1]==x]),x] for x in values]

with open('/home/user/vs_intern/Vega-Strike/data/i18n/fr/LC_MESSAGES/vegastrike_csv.csv', 'w') as newfile:
    newfile.write ('"location","source","target"\n')
    for i in newlist:
        newfile.write(','.join(i))
        newfile.write('\n')
newfile.close()
