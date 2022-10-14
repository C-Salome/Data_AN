from bs4 import BeautifulSoup
import pandas as pd
import glob
import os

col = ["id_indiv",'id_territoire','id_legis','id_mandat','id_inves','id_motif_deb','id_motif_fin','remporte','id_suppleant','date_deb','date_fin']
res = []

for filename in glob.glob('/Users/salomecolza/desktop/These_Hugo/AMO30_tous_acteurs_tous_mandats_tous_organes_historique_v2/acteur/*.xml'):
    with open(os.path.join(os.getcwd(), filename), 'r') as file:
        soup = BeautifulSoup(file,"xml")

        mandat = soup.find_all("mandat")
        for i in mandat:

            ref = i.find("codeQualite")
            id_fonction = ref.get_text()

            if not id_fonction:
                ref = i.find("libQualite")
                id_fonction = ref.get_text()

            ref = i.find("organeRef")
            id_instance = ref.get_text()

            if id_fonction == "membre" and (id_instance == 'PO230434' or id_instance == 'PO384266' or id_instance == 'PO644420' or id_instance == 'PO717460' or id_instance == 'PO791932'):

                ref = i.find("acteurRef")
                id_indiv = ref.get_text()
                print(id_indiv)

                ref = i.find("legislature")
                id_legis = ref.get_text()

                ref = i.find("dateDebut")
                date_deb = ref.get_text()

                ref = i.find("dateFin")
                date_fin = ref.get_text()

                ref = i.find("refCirconscription")
                id_circo = ref.get_text()

                ref = i.find("suppleantRef")

                if ref:
                    id_supp = ref.get_text()
                else:
                    id_supp = None

                ref = i.find("causeFin")
                cause_fin = ref.get_text()

                if not cause_fin:
                    cause_fin = 0
                if cause_fin == 'Fin de législature':
                    cause_fin = 3
                elif cause_fin == 'Décès':
                    cause_fin = 5
                elif cause_fin == "Reprise de l'exercice du mandat d'un ancien membre du Gouvernement":
                    cause_fin = 6
                elif cause_fin == "Nomination comme membre du Gouvernement":
                    cause_fin = 7
                elif cause_fin == "Prolongation de mission temporaire":
                    cause_fin = 9
                elif cause_fin == "Démission":
                    cause_fin = 11
                elif cause_fin == "Annulation de l'élection sur décision du Conseil constitutionnel":
                    cause_fin = 12
                elif cause_fin == "Démission pour cause d’incompatibilité prévue aux articles LO 137, LO 137-1, LO 141 ou LO 141-1 du code électoral":
                    cause_fin = 17
                elif cause_fin == "Élection au Sénat":
                    cause_fin = 18
                elif cause_fin == "Démission avant entrée en fonction":
                    cause_fin = 22

                ref = i.find("causeMandat")
                cause_mandat = ref.get_text()

                if not cause_mandat:
                    cause_mandat = 0
                elif cause_mandat == "élections générales":
                    cause_mandat = 1
                elif cause_mandat == "remplacement d'un député nommé au Gouvernement":
                    cause_mandat = 4
                elif cause_mandat == "remplacement d'un député ayant démissionné pour cause d’incompatibilité prévue aux articles LO 137, LO 137-1, LO 141 ou LO 141-1 du code électoral":
                    cause_mandat = 8
                elif cause_mandat == "reprise de l'exercice du mandat d'un ancien membre du Gouvernement":
                    cause_mandat = 10
                elif cause_mandat == "remplacement d'un député décédé":
                    cause_mandat = 13
                elif cause_mandat == "élection partielle, remplacement d'un député élu au Sénat":
                    cause_mandat = 14
                elif cause_mandat == "élection partielle, suite à l'annulation de l'élection d'un député":
                    cause_mandat = 15
                elif cause_mandat == "remplacement d'un député en mission au-delà de 6 mois":
                    cause_mandat = 16
                elif cause_mandat == "élection partielle":
                    cause_mandat = 19
                elif cause_mandat == "élection partielle, remplacement d'un député démissionnaire":
                    cause_mandat = 20
                elif cause_mandat == "élection partielle, remplacement d'un député démissionnaire d'office":
                    cause_mandat = 21
                elif cause_mandat == "élection partielle, en remplacement d'un député décédé et sans suppléant":
                    cause_mandat = 23
                elif cause_mandat == "remplacement d'un député nommé au Conseil Constitutionnel":
                    cause_mandat = 24
                elif cause_mandat == "élection partielle, remplacement d'un député démissionnaire d'office (pour incompatibilité)":
                    cause_mandat = 25

                res.append({"id_indiv" : id_indiv,'id_territoire' : id_circo, 'id_legis' : id_legis, 'id_mandat' : 1, 'id_inves' : None , 'id_motif_deb' : cause_mandat , 'id_motif_fin' : cause_fin , 'remporte' : True , 'id_suppleant' : id_supp, 'date_deb' : date_deb,'date_fin' : date_fin})

    file.close()

out_df = pd.DataFrame(res, columns = col)
out_df.to_excel('/Users/salomecolza/desktop/These_Hugo/export_df_candidats_XVI.xlsx', index = False, header=True, columns= col, encoding= 'utf-8')

print(len(res))