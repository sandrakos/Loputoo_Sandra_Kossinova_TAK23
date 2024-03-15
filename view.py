import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import csv
import os


class View:
    def __init__(self, app, kontroller):
        self.app = app
        self.kontroller = kontroller
        self.kontroller.maara_vaade(self)

        self.app.title("Päring")

        # Faili tee kuvamine
        self.faili_tee_silt = tk.Label(self.app, text="")
        self.faili_tee_silt.pack()

        # Otsingusõna sisestamine
        self.otsing_entry = tk.Entry(self.app)
        self.otsing_entry.pack()

        # Nupp et fail avada
        self.faili_valik_nupp = tk.Button(self.app, text="Vali fail kus päring teha", command=self.vali_fail)
        self.faili_valik_nupp.pack()

        # Nupp et otsida
        self.otsing_nupp = tk.Button(self.app, text="Otsi", command=lambda: self.teosta_otsing())
        self.otsing_nupp.pack()

        # Treeview tulemuste kuvamiseks
        self.tulemused_tree = ttk.Treeview(self.app)
        self.tulemused_tree.pack()

        # Kerimisriba
        self.scrollbar_y = ttk.Scrollbar(self.app, orient='vertical', command=self.tulemused_tree.yview)
        self.scrollbar_y.pack(side='right', fill='y')
        self.tulemused_tree.configure(yscrollcommand=self.scrollbar_y.set)
        self.scrollbar_x = ttk.Scrollbar(self.app, orient='horizontal', command=self.tulemused_tree.xview)
        self.scrollbar_x.pack(side='bottom', fill='x')

    def teosta_otsing(self):
        otsingusona = self.otsing_entry.get()  # Hangi otsingusõna vaate kaudu
        if self.kontroller.model.valitud_faili_tee:  # Kontrolli, kas fail on valitud
            self.kontroller.teosta_otsing(otsingusona)  # Edasta otsingusõna kontrollerisse
        else:
            # Kuva sõnum kasutajale
            tk.messagebox.showinfo("Faili valimata", "Sa pole .csv faili veel valinud.")

    def vali_fail(self):
        faili_tee = filedialog.askopenfilename(title="Vali CSV fail",
                                                filetypes=(("CSV failid", "*.csv"), ("Kõik failid", "*.*")))
        if faili_tee:
            self.kontroller.salvesta_valitud_faili_tee(faili_tee)
            self.kontroller.model.loe_csv_fail(faili_tee)
            faili_nimi = os.path.basename(faili_tee)  # Võta faili nimi
            self.faili_tee_silt.config(text="Valitud fail: " + faili_nimi)  # Näita valitud faili teed
            # Uuenda Treeview tulpade nimed
            tulbad = self.loe_csv_tulbad(faili_tee)
            self.tulemused_tree["columns"] = tulbad
            for tulp in tulbad:
                self.tulemused_tree.heading(tulp, text=tulp)
        else:
            print("Faili valimine tühistati.")

    def kuva_tulemus(self, tulemus):
        # Kuvage tulemus Treeview'is
        self.tulemused_tree.insert('', 'end', values=tulemus)

    def kuva_sonum(self, sonum):
        # Kuva sõnum vaates (nt dialoogiboksis)
        tk.messagebox.showinfo("Teade", sonum)

    def tuhjenda_tulemused(self):
        # Tühjendage tulemused Treeview'st
        for i in self.tulemused_tree.get_children():
            self.tulemused_tree.delete(i)

    def loe_csv_tulbad(self, faili_tee):
        # Loeme CSV faili esimese rea tulbad
        with open(faili_tee, 'r', newline='', encoding='utf-8') as fail:
            lugeja = csv.reader(fail, delimiter=';')
            esimene_rida = next(lugeja)
        return esimene_rida
