f = open("/storage/emulated/0/Code/2022/input08.txt", "r")

def getNext():
  return f.readline().rstrip()


def getInput():
  grid = []

  line = getNext()
  
  while line:
    grid.append([int(h) for h in line])
    line = getNext()
                
  return grid

def printGrid(g):
  for r in g:
    print(''.join([str(i) for i in r]))
  print()


def getScores(trees):
  scores = [[getScore(trees, x, y) for x in range(len(trees[0]))] for y in range(len(trees))]
  
  return scores


def getScore(trees, x, y):
 
  if x == 0 or y == 0 or x == (len(trees[0]) - 1) or y == (len(trees) - 1):
    return 0
 
  score = 1  
  th = trees[y][x]
  
  dist = 1
  xx = x + 1
  while xx < (len(trees[0]) - 1) and trees[y][xx] < th:
    dist += 1
    xx += 1
  score *= dist
  
  dist = 1
  xx = x - 1
  while xx > 0 and trees[y][xx] < th:
    dist += 1
    xx -= 1
  score *= dist

  dist = 1
  yy = y + 1
  while yy < (len(trees) - 1) and trees[yy][x] < th:
    dist += 1
    yy += 1
  score *= dist
  
  dist = 1
  yy = y - 1
  while yy > 0 and trees[yy][x] < th:
    dist += 1
    yy -= 1
  score *= dist
    
  return score


def run():
  trees = getInput()
  printGrid(trees)
  
  scores = getScores(trees)
        
  print(scores)
  
  print(max([max(r) for r in scores]))

run()
f.close()

