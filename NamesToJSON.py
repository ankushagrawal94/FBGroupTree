#!/usr/bin/env python

import sys
import json
import UserDict

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
          if node.parent != "none" and node not in self.data[node.parent].children:
            self.data[node.parent].children.append(node)

class NodeJSONEncoder(json.JSONEncoder):
  def default(self, node):
    if type(node) == Node:
      return {"nid":node.nid, "name":node.name, "children":node.children}
    raise TypeError("{} is not an instance of Node".format(node))


nodes = []

with open(sys.argv[1]) as f:
  for row in f.readlines()[:]:
    name, parent, nid = row.split('\t')
    nodes.append(Node(nid, parent, name))

nodeDict = NodeDict()
nodeDict.addNodes(nodes)

rootNodes = [node for nid, node in nodeDict.items() if node.parent == "none"]
print len(rootNodes)
print len(nodeDict.items())
for rootNode in rootNodes:
  print NodeJSONEncoder().encode(rootNode)        