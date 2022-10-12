from bs4 import BeautifulSoup
import pandas as pd
import glob
import os

col = ["id_instance",'nom_instance','type_instance','date_deb','date_fin']
res = []

for filename in glob.glob('/Users/salomecolza/desktop/These_Hugo/AMO30_tous_acteurs_tous_mandats_tous_organes_historique/organe/*.xml'):
    with open(os.path.join(os.getcwd(), filename), 'r') as file:
        soup = BeautifulSoup(file,"xml")

        p_id = soup.find("uid")
        pf_id = p_id.get_text()

        p_type = soup.find("codeType")
        pf_type = p_type.get_text()

        if pf_type != "CIRCONSCRIPTION":

            p_libel_terr = soup.find("libelle")
            pf_libel_terr = p_libel_terr.get_text()
            print(pf_libel_terr)

            p_date_d = soup.find("dateDebut")
            pf_date_d = p_date_d.get_text()

            p_date_f = soup.find("dateFin")
            pf_date_f = p_date_f.get_text()

            res.append({"id_instance": pf_id,'nom_instance': pf_libel_terr,'type_instance': pf_type,'date_deb': pf_date_d,'date_fin': pf_date_f})

        file.close()

out_df = pd.DataFrame(res, columns = col)
out_df.to_excel(r'/Users/salomecolza/desktop/These_Hugo/export_dataframe_instance_AMO30.xlsx', index = False, header=True)

print(len(res))


