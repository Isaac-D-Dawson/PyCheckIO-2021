#V1.0: initial program, which meets all requirements provided.
#V1.1: added comments explaining logic.

#I am ashamed to admit I used the hints on this one. I'm not sure how the solution used here differs from the solution I used, but it...works..somehow.
# I clearly need to work on this more.

#An issue with my original solution for this rework was pawns occasionally being counted twice.
#In hindsight, this is fixable, but honetly I'm just kinda..done with this, emotionally.
#Still, I can work on this.

#Almost everyone in the world knows about the ancient game Chess and has at least a basic understanding of its rules. It has various units with a wide range of movement patterns allowing for a huge number of possible different game positions (for example Number of possible chess games at the end of the n-th plies. ) For this mission, we will examine the movements and behavior of chess pawns.
#Chess is a two-player strategy game played on a checkered game board laid out in eight rows (called ranks and denoted with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares. Each square of the chessboard is identified by a unique coordinate pair — a letter and a number (ex, "a1", "h8", "d6"). For this mission we only need to concern ourselves with pawns. A pawn may capture an opponent's piece on a square diagonally in front of it on an adjacent file, by moving to that square. For white pawns the front squares are squares with greater row number than the square they currently occupy.
#A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall. With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square. We have several white pawns on the chess board and only white pawns. You should design your code to find how many pawns are safe.
#You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

#Input: Placed pawns coordinates as a set of strings.
#Output: The number of safe pawns as a integer.
#Precondition:
#0 < pawns ≤ 8

#Is it possible to ducktype ranges?
#EG: "safe_pawns(0 < pawns: set <= 8) -> int:"
def safe_pawns(pawns: set) -> int:
    '''
        Takes a set of chess piece locations, assumes all are pawns, and returns the number of those pices that are "Safe"
    '''
    
    pawns_indexes = set()	#uses a set for the indexes to remove duplicates
    for p in pawns:			#iterates through pawns
        row = int(p[1]) - 1		#converts the piece row to an accurate int
        col = ord(p[0]) - 97	#and the rank to an int as well
        pawns_indexes.add((row, col))	#saves them
    count = 0
    for row, col in pawns_indexes:	#cycles through all the unique pawns, now that we've sorted them.
        is_safe = ((row - 1, col - 1) in pawns_indexes) or ((row - 1, col + 1) in pawns_indexes)	#checks if a pawn is safe by checking it';s covering tiles.
        if is_safe:
            count += 1	#if it is safe, add to the count.
    
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")