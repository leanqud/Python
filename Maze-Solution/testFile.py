from lab04 import *
from Stack import Stack

def test_example():
	maze = [
['+','+','+','+','G','+'],
['+',' ','+',' ',' ','+'],
['+',' ',' ',' ','+','+'],
['+',' ','+','+',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]
	assert solveMaze(maze, 4, 4) == True
	assert maze == [
['+', '+', '+', '+', 'G', '+'],
['+', 8, '+', 11, 12, '+'],
['+', 7, 9, 10, '+', '+'],
['+', 6, '+', '+', 2, '+'],
['+', 5, 4, 3, 1, '+'],
['+', '+', '+', '+', '+', '+'] ]

def test_example2():
	maze2 = [
['+','+','+','+','G','+'],
['+','+','+','+','+','+'],
['+','+',' ','+','+','+'],
['+','+','+','+','+','+'],
['+','+','+','+','+','+'],
['+','+','+','+','+','+'] ]
	assert solveMaze(maze2, 3, 3) == False
	assert maze2 == [
['+','+','+','+','G','+'],
['+','+','+','+','+','+'],
['+','+',' ','+','+','+'],
['+','+','+',1,'+','+'],
['+','+','+','+','+','+'],
['+','+','+','+','+','+']]

def test_example3():
	maze3 = [
['+','+','+','+'],
['+',' ','G','+'],
['+',' ',' ','+'],
['+','+',' ','+'],
['+','+','+','+']]
	assert solveMaze(maze3, 3, 2) == True
	assert maze3 == [
['+','+','+','+'],
['+',' ','G','+'],
['+',' ', 2,'+'],
['+','+', 1,'+'],
['+','+','+','+']]

def test_example4():
	maze4 = [
['+','+','+','+','G','+'],
['+',' ','+',' ',' ','+'],
['+',' ',' ',' ','+','+'],
['+',' ','+','+',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]
	assert solveMaze(maze4, 1, 5) == True
	assert maze4 == [
['+','+','+','+','G','+'],
['+',' ','+',' ', 2, 1],
['+',' ',' ',' ','+', '+'],
['+',' ','+','+',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]

def test_example5():
	maze5 = [
['+','+','G','+'],
['+',' ',' ','+'],
['+','+','+','+']]
	assert solveMaze(maze5, 2, 2) == True
	assert maze5 == [
['+','+','G','+'],
['+',' ',2,'+'],
['+','+', 1,'+']]


def test_example6():
	#def test_example():
	maze6 = [
['+','+','+','+','+','+'],
['+',' ','+',' ',' ','+'],
['+','+','+','+','+','+'],
['+','G',' ',' ',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]
	assert solveMaze(maze6, 3, 5) == True
	assert maze6 == [
['+','+','+','+','+','+'],
['+',' ','+',' ',' ','+'],
['+','+','+','+','+','+'],
['+','G', 4, 3, 2, 1],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+']]


def test_example7():
	maze7 = [
['+','+','+','+','+','+'],
['+',' ',' ',' ',' ','+'],
['+',' ',' ',' ','+','+'],
['+','+','+',' ',' ','+'],
['+','G','+',' ',' ','+'],
['+','+','+','+','+','+'] ]
	assert solveMaze(maze7, 4, 4) == False
	printMaze(maze7)
	assert maze7 == [
['+','+','+','+','+','+'],
['+',7, 6, 5, 10,'+'],
['+', 8, 9, 4, '+','+'],
['+','+','+', 3, 2, '+'],
['+','G','+', 11, 1,'+'],
['+','+','+','+','+','+']]









	
