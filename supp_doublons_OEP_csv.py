import csv
import pandas as pd

with open("/Users/salomecolza/desktop/These_Hugo/liste_organismes_extra_parlementaires_libre_office",'r') as file:
    data = list(csv.reader(file, delimiter=","))
    lig = []
    for el in data:
        if el not in lig:
            lig.append(el)
            print(el)


out_df = pd.DataFrame(lig)
out_df.to_csv(r'/Users/salomecolza/desktop/These_Hugo/export_dataframe_oep.csv', index = False, header=True)