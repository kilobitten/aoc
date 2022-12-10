f = open("/storage/emulated/0/Code/2022/input09.txt", "r")

K = 10

def getNext():
  return f.readline().rstrip()


def getInput():
  moves = []

  line = getNext()
  while line:
    move = line.split(' ')
    moves.append([move[0], int(move[1])])
    line = getNext()
                
  return moves


def printGrid(g):
  minMax = [
      [min([min(p) for p in g.values()]),
       max([max(p) for p in g.values()])],
       [min(g.keys()), max(g.keys())]
  ]
  print(minMax)
  for y in range(minMax[1][0], minMax[1][1]+1):
    out = ['.' for x in range(minMax[0][0], minMax[0][1]+1)]
    if y in g:
      for x in g[y]:
        out[x-minMax[0][0]] = '#'
    print(''.join(out))
  print()
        

deltas = {
  'U': [0, -1],
  'D': [0, 1],
  'L': [-1, 0],
  'R': [1, 0],
}


def processMove(move, pos, grid):
  delta = deltas[move[0]]
  for _ in range(move[1]):
    moveHead(delta, pos)
    for k in range(K-1):
      moveKnot(pos[k:k+2])
    recordTail(pos[K-1], grid)
    #print(pos)
    
    
def recordTail(tail, grid):
    if tail[1] not in grid:
      grid[tail[1]] = {tail[0]}
    else:
      grid[tail[1]].add(tail[0])


def moveHead(delta, pos):
  pos[0] = [pos[0][i] + delta[i] for i in range(2)]


def moveKnot(pos):
  head, tail = pos
  diff = [head[i] - tail[i] for i in range(2)]
  for i in range(2):
    if abs(diff[i]) == 2:
      tail[i] += int(diff[i] / 2)
      j = (i+1)%2
      if diff[j] != 0:
        tail[j] += int(diff[j] / abs(diff[j]))
      return
    

def run():
  moves = getInput()
  grid = {0: {0}}
  pos = [[0, 0] for k in range(K)]
  
  print(moves)
  
  for move in moves:
    processMove(move, pos, grid)
  
  printGrid(grid)

  print(sum([len(p) for p in grid.values()]))

run()
f.close()

