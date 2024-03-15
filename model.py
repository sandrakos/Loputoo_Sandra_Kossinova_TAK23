import csv

class Model:
    def __init__(self):
        self.valitud_faili_tee = ""

    def loe_csv_fail(self, faili_tee):
        andmed = []
        with open(faili_tee, 'r', newline='', encoding='utf-8') as fail:
            lugeja = csv.reader(fail, delimiter=';')
            for rida in lugeja:
                andmed.append(rida)
        return andmed

    def filtreeri_andmed(self, andmed, otsingusona):
        filtreeritud_andmed = []
        for rida in andmed:
            if any(otsingusona.lower() in veerg.lower() for veerg in rida):
                filtreeritud_andmed.append(rida)
        return filtreeritud_andmed
