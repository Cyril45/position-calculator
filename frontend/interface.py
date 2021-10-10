from tkinter import *
from backend.moneymanagement import MoneyManagement
import sys, os


class Interface:
    def __init__(self, fields):
        self.master_window = Tk()
        self.master_window.title("Position calulator")
        self.master_window.iconbitmap(
            default=self.resource_path("frontend/icon/logo_position_calculator.ico")
        )
        self.master_window.minsize(480, 360)
        self.background = "#3B3B3B"
        self.master_window.config(background=self.background)
        self.texte_color = "white"
        self.fields = fields
        self.result = None
        self.generate_button(self.makeform())
        self.master_window.mainloop()

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def generate_button(self, entries):
        row = Frame(self.master_window, bg=self.background)
        b1 = Button(
            row,
            text="Calculate position",
            command=(lambda e=entries: self.calcul_position(e)),
        )
        b1.pack(side=LEFT, padx=5, pady=5)
        self.master_window.bind("<Return>", lambda x: self.calcul_position(entries))

        b2 = Button(row, text="Quit", command=self.master_window.quit)
        b2.pack(side=RIGHT, padx=5, pady=5)
        row.pack(side=TOP, fill=X, padx=5, pady=5)

    def makeform(self):
        entries = {}
        for field in self.fields:
            row = Frame(self.master_window, bg=self.background)
            lab = Label(
                row,
                width=22,
                text=field + ": ",
                anchor="w",
                bg=self.background,
                fg=self.texte_color,
            )
            ent = Entry(row)
            ent.insert(0, "0")
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries[field] = ent
        return entries

    def calcul_position(self, entries):
        calcul = []
        for entry in entries:
            try:
                if entry != "Minimal buy" and float(entries[entry].get()) > 0:
                    calcul.append(float(entries[entry].get()))
                elif entry == "Minimal buy" and float(entries[entry].get()) >= 0:
                    calcul.append(float(entries[entry].get()))
            except ValueError:
                print("Oops! No valid number. Try again...")

        if len(calcul) == len(entries):
            money = MoneyManagement(*calcul)
            result = {
                "risk": money.calcul_risk(),
                "nb_action": money.calcul_buy_nb_action(),
                "investment_price": money.investment_price(),
                "envisaged_loss": money.envisaged_loss(),
                "envisaged_profit": money.envisaged_profit(),
            }
            self.view_result(result)

    def view_result(self, result):
        if self.result != None:
            self.result.destroy()
        self.result = Frame(self.master_window, bg=self.background)
        if result["risk"]:
            Label(
                self.result,
                text="Vous devez acheter {} cryptomonnaie soit {} Euros\nPertes possible : {} Euros soit {} % de votre capital\nGain possible : {} Euros soit {} % de votre capital\n".format(
                    result["nb_action"],
                    result["investment_price"],
                    result["envisaged_loss"][0],
                    result["envisaged_loss"][1],
                    result["envisaged_profit"][0],
                    result["envisaged_profit"][1],
                ),
                anchor="w",
                justify=LEFT,
                font=("Arial", 12, "bold"),
                bg=self.background,
                fg=self.texte_color,
            ).pack(side=LEFT)
            self.result.pack(side=LEFT, fill=X, padx=5, pady=5)

        else:
            Label(
                self.result,
                text="Vous ne devriez pas investir",
                anchor="w",
                justify=LEFT,
                font=("Arial", 12, "bold"),
                bg=self.background,
                fg=self.texte_color,
            ).pack(side=LEFT)
            self.result.pack(side=LEFT, fill=X, padx=5, pady=5)
