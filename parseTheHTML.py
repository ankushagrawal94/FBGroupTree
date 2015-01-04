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
    
    print name + '\t' + addedBy + '\t' + utime

f = open('HTML.txt', 'r')
html_str = ""
for line in f:
  html_str += line

getDetails("Added by")
print '\n\n\n\n\n\n\n\n'
getDetails("Joined about")


