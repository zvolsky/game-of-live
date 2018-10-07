#!/usr/bin/env python3

import sys


def get_next_one(wint):
    """
        returns next generation as list of rows where each row contain string of 0|1 characters
        
        :param  wint      array of integers 0|1  older generation
        :retval next_one  list of rows           next generation
    """

    next_one = []
    rows = len(wint)
    cols = len(wint[0])

    def fixed_i(i):
        # return divmod(i, rows)[1] , but lets optimize this a little
        if 0 <= i < rows:
            return i
        return i % rows

    def fixed_j(j):
        if 0 <= j < cols:
            return j
        return divmod(j, cols)[1]

    def neighbors_include_me(center_i, center_j):
        neighbors_and_me = 0
        for i in range(center_i - 1, center_i + 2):
            for j in range(center_j - 1, center_j + 2):
                neighbors_and_me += wint[fixed_i(i)][fixed_j(j)]
        return neighbors_and_me

    for i, row in enumerate(wint):
        next_row = ''
        for j, elem in enumerate(row):
            neighbors = neighbors_include_me(i, j) - elem
            if elem and 2 <= neighbors <= 3 or not elem and neighbors == 3:
                next_row += '1'
            else:
                next_row += '0'
        next_one.append(next_row)
    
    return next_one

def word_to_int(world):
    """
        converts list of strings (where each char is an element) into array of integers 0|1
        array means list of rows where each row contains list of elements 0|1
    """
    wint = []
    for row in world:
        wint.append(tuple(map(int, tuple(row))))
    return wint

def validated_world(world):
    if type(world) not in (tuple, list) or len(world) == 0:
        raise TypeError('need a non empty list')
    cols = None
    for row in world:
        if type(row) != str:
            raise TypeError('list elements must be strings') 
        if cols is None:
            cols = len(row)
            if not cols:
                raise TypeError('strings inside the list must be non empty')
        elif len(row) != cols:
            raise TypeError('strings inside the list must have the same length')
        if row.replace('0', '').replace('1', ''):
            raise TypeError('allowed characters are: 01')
    return world

def from_stdin():
    console = sys.stdin.isatty()
    world = []
    row_no = 1
    while True:
        try:
            row = input(('row %s (empty to start) : ' % row_no) if console else '')
        except EOFError:
            break
        if not row:
            break
        world.append(row)
        row_no += 1
    main(world)

def main(world):
    for row in get_next_one(word_to_int(validated_world(world))):
        print(row)

if __name__ == '__main__':
    from_stdin()
