assignments = []


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    for unit in unitlist:
        duals = [ s for s in unit if len(values[s]) == 2 ]
        if (len(duals) == 2 and values[duals[0]] == values[duals[1]]):
            twn = values[duals[0]]
            for key in unit:
                if not (key == duals[0] or key == duals[1]):
                    values[key] = values[key].replace(twn[0], "")
                    values[key] = values[key].replace(twn[1], "")

    # Eliminate the naked twins as possibilities for their peers   
    return values

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"
    return { boxes[i] : elem if elem !='.' else '123456789' for i, elem in enumerate(grid) }

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    pass

def peers(value):

    row_peers = row_units[rows.index(value[0])]
    col_peers = column_units[cols.index(value[1])]
    sqr_peers = []
    for rs in square_units:
        if value in rs:
            sqr_peers += rs

    ans = row_peers + col_peers + sqr_peers

    if value == "E5":
        return ans + left_diag_peers + right_diag_peers
    elif value in left_diag_peers:
        return ans + left_diag_peers 
    elif value in right_diag_peers:
        return ans + right_diag_peers
    else:
        return ans 

def eliminate(values):
    for key in values:
        if len(values[key])==1:
            for peer in peers(key):
                if len(values[peer]) > 1:
                    values[peer] = values[peer].replace(values[key], '')
            
    return values

def only_choice(values):
    for unit in unitlist:
        all_values = ''.join([ values[key] for key in unit ])
        singles = []
        for k in '123456789':
            if all_values.count(k) == 1:
                for key in unit:
                    if( k in values[key] ):
                        values[key] = k
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        values = eliminate(values)

        # Your code here: Use the Only Choice Strategy
        values = only_choice(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    values =  reduce_puzzle(values)
    
    if values == False:
        return False

    unfilled = {k: v for k, v in values.items() if len(v) > 1}
    if(len(unfilled) == 0):
        return values

    # Choose one of the unfilled squares with the fewest possibilities
    # sort all unfilled squares and order them by length of options
    sort = sorted((unfilled.items()), key=lambda x:x[1], reverse=True)
    
    element = sort[0] 
    key = element[0]
    opts = element[1]
    for digit in opts:
        copyValues = values.copy()
        copyValues[key] = digit
        ans = search(copyValues)
        if ans:
            return ans

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    return search(values)

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')

cols = '123456789'
rows = 'ABCDEFGHI'

boxes = cross('ABCDEFGHI', '123456789')

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
left_diag_peers = [ rows[i] + cols[i] for i in range(0, 9) ] 
right_diag_peers = [ rows[8-i] + cols[i] for i in range(0, 9) ]
unitlist = row_units + column_units + square_units + [left_diag_peers] + [right_diag_peers]