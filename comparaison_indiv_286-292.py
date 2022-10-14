import csv
import pandas as pd

with open("/Users/salomecolza/desktop/These_Hugo/dep_XII-XV.csv",'r') as file1: # Député de la XII à la XV
	data1 = list(csv.reader(file1, delimiter=";"))
with open("/Users/salomecolza/desktop/These_Hugo/export_df_XVI_2.csv",'r') as file2: #fichier importé députés XVI
	data2 = list(csv.reader(file2, delimiter=","))

res1 = []
res2 = []


for el1 in data1:
	trouve = False
	for el2 in data2:
		print(el1)
		print(el2)
		if el1 == el2: # on trouve une correspondance
			res1.append(el1)
			trouve = True
			break
	if trouve == False:
		res2.append(el1) # pas de correspondance

print("Nombre d'individus réélus :",len(res1))
print("Nombre d'individu sortant ou nouveau",len(res2))

out_df1 = pd.DataFrame(res1)
out_df1.to_csv(r'/Users/salomecolza/desktop/These_Hugo/res1.csv', index = False, header=True)

out_df2 = pd.DataFrame(res2)
out_df2.to_csv(r'/Users/salomecolza/desktop/These_Hugo/res2.csv', index = False, header=True)