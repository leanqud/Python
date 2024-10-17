from Stack import Stack

def printMaze(maze):
	for row in range(len(maze)):
		for col in range(len(maze[0])):
			print("|{:<2}".format(maze[row][col]), sep='',end='')
		print("|")
	return

def solveMaze(maze, startX, startY):
        s = Stack()
        maze[startX][startY] = 1
        counter = 1
        s.push([startX, startY])
        while s.isEmpty() == False:
                p = s.peek()
                x = p[0]
                y = p[1]
                if maze[x-1][y] == 'G':
                        return True
                elif maze[x-1][y] == ' ':
                        counter += 1
                        maze[x-1][y] = counter
                        s.push([x-1, y])
                elif maze[x][y-1] == 'G':
                        return True
                elif maze[x][y-1] == ' ':
                        counter += 1
                        maze[x][y-1] = counter
                        s.push([x, y-1])
                elif maze[x+1][y] == 'G':
                        return True
                elif maze[x+1][y] == ' ':
                        counter += 1
                        maze[x+1][y] = counter
                        s.push([x+1, y])
                elif maze[x][y+1] == 'G':
                        return True
                elif maze[x][y+1] == ' ':
                        counter += 1
                        maze[x][y+1] = counter
                        s.push([x, y+1])
                elif maze[x-1][y] != ' ' and maze[x][y-1] != ' ' and maze[x+1][y] != ' ' and maze[x][y+1] != ' ':
                        s.pop()
                else:
                        break
        return False

# pop off stack when cant move in any direction










