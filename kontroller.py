class Kontroller:
    def __init__(self, model):
        self.model = model
        self.view = None

    def maara_vaade(self, view):
        self.view = view

    def teosta_otsing(self, otsingusona):
        faili_tee = self.model.valitud_faili_tee
        if faili_tee:
            andmed = self.model.loe_csv_fail(faili_tee)
            filtreeritud_andmed = self.model.filtreeri_andmed(andmed, otsingusona)
            self.view.tuhjenda_tulemused()
            if filtreeritud_andmed:
                for i, rida in enumerate(filtreeritud_andmed, start=1):
                    self.view.kuva_tulemus(rida)
            else:
                self.view.kuva_sonum("Otsingule ei leitud vastet.")
        else:
            self.view.kuva_sonum("Palun valige kõigepealt CSV-fail.")

    def salvesta_valitud_faili_tee(self, faili_tee):
        self.model.valitud_faili_tee = faili_tee
