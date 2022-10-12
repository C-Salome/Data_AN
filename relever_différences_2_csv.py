import csv
import pandas as pd

with open("/Users/salomecolza/desktop/These_Hugo/ExportCandidats.csv",'r') as file1:
	data1 = list(csv.reader(file1, delimiter=","))
with open("/Users/salomecolza/desktop/These_Hugo/Candidats.csv",'r') as file2:
	data2 = list(csv.reader(file2, delimiter=","))



res = []

for el1 in data1:
	for index in range(0, len(data2), 1):
		if el1 == data2[index]:
			break
		elif index == len(data2)-1 and data2[index] != el1:
			print(el1)
			res.append(el1)

print(len(res))
out_df = pd.DataFrame(res)
out_df.to_csv(r'/Users/salomecolza/desktop/These_Hugo/lignes_refusee_candidats.csv', index = False, header=True)