import sys

def findnth(fullStr, shortStr, n):
    parts= fullStr.split(shortStr, n+1)
    if len(parts)<=n+1:
        return -1
    return len(fullStr)-len(parts[-1])-len(shortStr)

def getDetails(startPhrase):
  numAdded = html_str.count(startPhrase)
  for i in range(0, numAdded):
    addedByStartIdx = findnth(html_str, startPhrase, i)
    tmp = html_str[addedByStartIdx: addedByStartIdx + html_str[addedByStartIdx:].find('<')]
    addedBy = tmp[8:]

    newEnd = html_str[:addedByStartIdx].rfind('>')
    for i in range(0,5):
      newEnd = html_str[:newEnd-1].rfind('>')
    name = html_str[newEnd+1: newEnd + html_str[newEnd:].find('<')]

    tmp = html_str[addedByStartIdx + html_str[addedByStartIdx:].find("data-utime=") : addedByStartIdx + html_str[addedByStartIdx:].find("class=")]
    utime = tmp[12:len(tmp) - 2]
    
    if name not in name_dict:
      name_dict[name] = (name, addedBy, utime, startPhrase)
    print name + '\t' + addedBy + '\t' + utime

#from ete2 import Tree
f = open(sys.argv[1], 'r')
html_str = ""
for line in f:
  html_str += line

name_dict = {}
contribution_dict = {}
getDetails("Added by")
print '\n\n'
getDetails("Joined")
print '\n\n'

for person in name_dict:
  if name_dict[person][1] not in contribution_dict:
    contribution_dict[name_dict[person][1]] = [name_dict[person][0]]
  else:
    contribution_dict[name_dict[person][1]].append(name_dict[person][0])

#for person in contribution_dict:
  #print person + "\t" + str(len(contribution_dict[person]))
#roots = []
#for name in name_dict:
#  if name_dict[person][3] == "Joined":
#    roots.append(name_dict[person][0])

#roots = [x for x in name_dict.keys() if x not in contribution_dict.keys()]
#print roots

#t = Tree()
#for root in roots:
#  t.add_child(name: root)

#print t