from bs4 import BeautifulSoup
import pandas as pd
import glob
import os

res = []

for filename in glob.glob('/Users/salomecolza/desktop/These_Hugo/AMO30_tous_acteurs_tous_mandats_tous_organes_historique/acteur/*.xml'):
    with open(os.path.join(os.getcwd(), filename), 'r') as file:
        soup = BeautifulSoup(file,"xml")

        ref = soup.find("causeFin")
        cause_fin = ref.get_text()
        ref = soup.find("causeMandat")
        cause_mandat = ref.get_text()

        t1 = ("F",cause_fin)
        t2 = ("D",cause_mandat)

        if t1 not in res:
            res.append(t1)
            print(t1)

        if t2 not in res:
            res.append(t2)
            print(t2)

    file.close()

out_df = pd.DataFrame(res)
out_df.to_excel('/Users/salomecolza/desktop/These_Hugo/export_dataframe_cause_mandats_fin_dep_AMO30.xlsx', index = True, header=False)
