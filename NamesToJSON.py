#!/usr/bin/env python

import sys
import json
import UserDict
import os

class Node(object):
    def __init__(self, nid, parent, name):
        self.nid = name        #Time added (because it should be unique)
        self.parent = parent  #Added by
        self.children = []    #people I added
        self.name = nid      #Name
class NodeDict(UserDict.UserDict):
  def addNodes(self, nodes):
    ''' Add every node as a child to its parent '''
    for i in (1,2):
      for node in nodes:
        self.data[node.nid] = node
        if node.parent in self.data.keys():
          if node.parent != "null" and node not in self.data[node.parent].children:
            self.data[node.parent].children.append(node)

class NodeJSONEncoder(json.JSONEncoder):
  def default(self, node):
    if type(node) == Node:
      return {"name":node.nid, "parent":node.parent, "_children":node.children}
    raise TypeError("{} is not an instance of Node".format(node))


os.system("sort "+ sys.argv[1] +" | uniq > " + "uniq" + sys.argv[1])

nodes = []

with open("uniq" + sys.argv[1]) as f:
  for row in f.readlines()[:]:
    if len(row) < 3:
      continue
    name, parent, nid = row.split('\t')
    if parent == "":
      parent = "MHacks"
    nodes.append(Node(nid.strip(), parent.strip(), name.strip()))
nodes.append(Node("0000000000", "null", "MHacks"))

nodeDict = NodeDict()
nodeDict.addNodes(nodes)

rootNodes = [node for nid, node in nodeDict.items() if node.parent == "null"]

for rootNode in rootNodes:
  print NodeJSONEncoder().encode(rootNode)        