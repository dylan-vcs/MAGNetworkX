import csv
from itertools import groupby
import json
affilsfile = file.open("PaperAuthorAffiliations.txt","r")
authorsfile = file.open("Authors.txt","r")
outfile = file.open("AGraph.csv", "w")

authors = csv.reader(authorsfile, delimiter="\t")
affils = csv.reader(affilsfile, delimiter="\t")
out = csv.writer(outfile)

authorsdict = dict()
IDtoName = []
for row in authors:
    IDtoName.append([row[0],row[2]])


papers = []
for row in affils:
    papers.append(row[0],row[1])

for key,group in groupby(papers, lambda x: x[0]):
    line = []
    aline = []
    line.append(group)
    for thing in group:
        aline.append(thing)
    line[1] = aline
    #writes out a completed line of author ID #s that relate to each other
    out.writerow(line)