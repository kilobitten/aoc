f = open("/storage/emulated/0/Code/2022/input07.txt", "r")

def getNext():
  n = f.readline().rstrip()
  if n:
    n = n.split(' ')
  return n

def getDir(tree, path):
  curr = tree
  for d in path:
    curr = curr[0][d]
  return curr


def addDir(tree, path, d):
  getDir(tree, path)[0][d] = [{}, 0]


def addSize(tree, path, s):
  for i in range(len(path) + 1):
    p = path[:i]
    #print(f'{i} {p}')
    getDir(tree, p)[1] += s


def getInput():
  head = [{}, 0]
  curr = []

  line = getNext()
  
  while line:
    #print(f'{head} {curr} {line}')
    #input('Press enter to continue')
    if line[0] != '$':
      quit('confused ;_;')
    
    if line[1] == 'cd':
      if line[2] == '..':
        curr = curr[:-1]
      elif line[2] == '/':
        curr = []      
      else:
        curr.append(line[2])
      line = getNext()
    elif line[1] == 'ls':
      line = getNext()
      while line and line[0] != '$':
        #print(line)
        if line[0] == 'dir':
          addDir(head, curr, line[1])
        else:
          addSize(head, curr, int(line[0]))
        line = getNext()
                
  #print(f'{head} {curr}')
  
  return head


def getClosest(need, tree):
  c = 70000000
  if tree[1] >= need:
    c = tree[1]
  for d in tree[0].values():
    c = min(c, getClosest(need, d))
  return c


def run():
  tree = getInput()
  print(tree)
  
  need = tree[1] - 40000000
  print(f'need {need}')
  
  c = getClosest(need, tree)
  print(c)

run()
f.close()

