import networkx as nx
import csv
A = nx.Graph()
#This code takes a file where every line is a list of Author ID #s that relate to each other.  This code adds the edges and nodes to the networkX graph and saves the result to a .gml file
with open('Apgraph.csv',"r") as data:
    csvdata = csv.reader(data)
    i = 0
    j = 0
    for line in csvdata:
        authors = line

        idlist = []
        A.add_node(line[i])
        idlist.append(line[i])
        i+=1

        for item in idlist:
            while j < len(idlist):
               if idlist[j] != item:
                   A.add_edge(idlist[j], item)
            i+=1
    #Write the resultant Authors Graph file out to a gml file to be loaded later
    nx.write_gml(A,"AuthorsGraph.gml")
