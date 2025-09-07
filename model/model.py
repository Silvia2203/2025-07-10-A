import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._products = []
        self._idMap = {}
        self._idMapCat = {}

    def getDateRange(self):
        return DAO.getDateRange()

    def getCategories(self):
        return DAO.getAllCat()

    def buildGraph(self, cat, date1, date2):
        self._graph.clear()
        for c in DAO.getAllCat():
            self._idMapCat[c.category_name] = c
        self._products = DAO.getAllProductsbyCategory(cat, self._idMapCat)
        for p in self._products:
            self._idMap[p.product_id] = p

        self._graph.add_nodes_from(self._products)

        allEdges = DAO.getEdges(cat, date1, date2, self._idMap, self._idMapCat)
        for e in allEdges:
            self._graph.add_edge(e[0], e[1], weight=e[2])

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getBestProdotti(self):
        bestprodotti = []
        for n in self._graph.nodes:
            score = 0
            for e_out in self._graph.out_edges(n, data=True):
                score += e_out[2]["weight"]
            for e_in in self._graph.in_edges(n, data=True):
                score -= e_in[2]["weight"]

            bestprodotti.append((n, score))

        bestprodotti.sort(reverse=True, key=lambda x: x[1])
        return bestprodotti[0:5]