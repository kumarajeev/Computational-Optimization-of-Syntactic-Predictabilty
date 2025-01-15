# Using NetworkX package and conllu package
import os
from io import open
from conllu import parse
import networkx as nx
from operator import itemgetter
from Measures import *
import random
from collections import Counter
import cliqs.entropy as entropy

directory = "./SUD"                   # directory containing the UD scheme tree files in CONLLU format
ud_files = []
for root, dirs, files in os.walk(directory):     
    for file in files:
        if file.endswith('train.conllu'):
            fullpath = os.path.join(root, file)
            ud_files.append(fullpath)            # creates a list of path of all files (file of each language) from the directory

for i in ud_files:                                       # reads file of each language one by one
    if 'sud' in str(i):                                   # selects a language
        lang = str(i).replace("./SUD", "")        
        lang=lang.replace("-sud-train.conllu", "")            # lang variable stores the language code
        #lang=lang.replace("\\", "")
        data_file = open(str(i),'r',encoding='utf-8').read()
        sentences = []
        sentences = parse(data_file)                         # parses the CONLLU format           
        print(lang)
        tree_list = []
        for sentence in sentences[0:]:
            tree = nx.DiGraph()                              # An empty directed graph (i.e., edges are uni-directional)  
            for nodeinfo in sentence[0:]:                    # retrieves information of each node from dependency tree in UD format     
                entry=list(nodeinfo.items())
                if not entry[7][1]=='punct':
                    tree.add_node(entry[0][1], form=entry[1][1], lemma=entry[2][1], upostag=entry[3][1], xpostag=entry[4][1], feats=entry[5][1], head=entry[6][1], deprel=entry[7][1], deps=entry[8][1], misc=entry[9][1])                #adds node to the directed graph 
                    ROOT=0
                    tree.add_node(ROOT)                            # adds an abstract root node to the directed graph
                                     
                for nodex in tree.nodes:
                    if not nodex==0:
                        if tree.has_node(tree.nodes[nodex]['head']):                                         # to handle disjoint trees
                            tree.add_edge(tree.nodes[nodex]['head'],nodex,drel=tree.nodes[nodex]['deprel'])       # adds edges as relation between nodes
                            if tree.nodes[nodex]['head']==0:
                                real_root=nodex
                                    
            tree_list.append(tree)

        tree_list[2]
        def gen():
            for s in tree_list:
                for h, d in s.edges():
                    if h != 0:
                        head = s.nodes[h]['upostag']
                        dep = s.nodes[d]['upostag']
                        yield head, dep

        counts = Counter(gen())
        print(counts)
        
        collected_pmi = entropy.pointwise_mutual_informations(counts)
        
        for (h, d), pmi in collected_pmi:
            results = open('Real_languages_MI_data.csv','a')
            results.write(str(lang)+"\t"+str(h)+"\t"+str(d)+"\t"+str(pmi)+"\n")
            results.close()