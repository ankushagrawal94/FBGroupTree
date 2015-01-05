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
          if node.parent != "null" and node not in self.data[node.parent].children:
            self.data[node.parent].children.append(node)

class NodeJSONEncoder(json.JSONEncoder):
  def default(self, node):
    if type(node) == Node:
      return {"name":node.nid, "parent":node.parent, "children":node.children}
    raise TypeError("{} is not an instance of Node".format(node))


nodes = []

with open(sys.argv[1]) as f:
  for row in f.readlines()[:]:
    if len(row) < 3:
      continue
    name, parent, nid = row.split('\t')
    if parent == "":
      parent = "HackathonHackers"
    nodes.append(Node(nid.strip(), parent.strip(), name.strip()))
nodes.append(Node("0000000000", "null", "HackathonHackers"))

dupChecker = {}
for node in nodes:
  if node.name in dupChecker:
    nodes.remove(node)
  else:
    dupChecker[node] = 1
nodeDict = NodeDict()
nodeDict.addNodes(nodes)

lst = []
for node in nodes:
  lst.append(node.nid)

print sorted(lst)
rootNodes = [node for nid, node in nodeDict.items() if node.parent == "null"]

for rootNode in rootNodes:
  print NodeJSONEncoder().encode(rootNode)        