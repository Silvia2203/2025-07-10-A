import datetime

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDCat(self):
        cat = self._model.getCategories()
        for c in cat:
            self._view._ddcategory.options.append(ft.dropdown.Option(text=c.category_name,
                                                                  data=c))
        self._view.update_page()

    def handleCreaGrafo(self, e):
        cat = self._view._ddcategory.value
        self._model.buildGraph(cat, self._view._dp1.value, self._view._dp2.value)
        Nnodes, Nedges = self._model.getGraphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Date selezionate:"))
        self._view.txt_result.controls.append(ft.Text(f"Start date: {self._view._dp1.value.date()}"))
        self._view.txt_result.controls.append(ft.Text(f"End date: {self._view._dp2.value.date()}"))
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato:"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi:{Nnodes}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi:{Nedges}"))
        self._fillDDProds()
        self._view.update_page()

    def handleBestProdotti(self,e):
        bestprodotti = self._model.getBestProdotti()
        self._view.txt_result.controls.append(ft.Text(f"I cinque prodotti più venduti sono:"))
        for p in bestprodotti:
            self._view.txt_result.controls.append(ft.Text(f"{p[0].product_name} with score {p[1]}"))
        self._view.update_page()

    def handleCercaCammino(self, e):
        pass

    def _fillDDProds(self):
        pass



    def setDates(self):
        first, last = self._model.getDateRange()

        self._view._dp1.first_date = datetime.date(first.year, first.month, first.day)
        self._view._dp1.last_date = datetime.date(last.year, last.month, last.day)
        self._view._dp1.current_date = datetime.date(first.year, first.month, first.day)

        self._view._dp2.first_date = datetime.date(first.year, first.month, first.day)
        self._view._dp2.last_date = datetime.date(last.year, last.month, last.day)
        self._view._dp2.current_date = datetime.date(last.year, last.month, last.day)
