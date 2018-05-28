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
    print(values)

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    for unit in unitlist:

        ## create a new dictionary where key is options for a box in the unit 
        ## and the corresponding value as the an array of boxes in the unit that hold the key
        new_dict = {}
        for elems in unit:
            new_dict.setdefault(values[elems], []).append(elems)
        
        for v in new_dict.keys():
            ## find two boxes that contain only two options
            if len(new_dict[v]) == 2 and len(v) == 2:
                for key in unit:
                    ## skip any box with assigned value
                    if len(values[key])==1:
                        continue;
                    ## for other boxes, remove the twin values from their options
                    if not (key == new_dict[v][0] or key == new_dict[v][1]):
                        val = values[key].replace(v[0], "")
                        val = val.replace(v[1], "")
                        assign_value(values, key, val)

    # Eliminate the naked twins as possibilities for their peers   
    return values


def peers(value):
    """Returns the peers of a particular box.
    Args:
        value(string): A box value

    Returns:
        array of box values that are peers of the given value
    """
    row_peers = row_units[rows.index(value[0])]
    col_peers = column_units[cols.index(value[1])]
    sqr_peers = []
    for rs in square_units:
        if value in rs:
            sqr_peers += rs

    ## add all normal peers
    ans = row_peers + col_peers + sqr_peers

    ## add peers for diagonal sudoku
    ## if central box, both diagonals are peers
    if value == "E5":
        return ans + left_diag_peers + right_diag_peers
    ## value belongs to left diagonal
    elif value in left_diag_peers:
        return ans + left_diag_peers 
    ## value belongs to right diagonal
    elif value in right_diag_peers:
        return ans + right_diag_peers
    else:
        return ans 

def eliminate(values):
    """Eliminate values from peers that are assigned to a box
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the assigned values eliminated from peers.
    """
    for key in values:
        if len(values[key])==1:
            for peer in peers(key):
                ## check that peer is not key, since peers array contains the original value also
                if not peer == key: 
                    assign_value(values, peer, values[peer].replace(values[key], ''))
            
    return values

def only_choice(values):
    """Assign a value to the box if only that box contains that option amongst all the peers in that unit
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the only choice strategy implemented.
    """
    for unit in unitlist:
        all_values = ''.join([ values[key] for key in unit ]) ## join all the options in all the boxes of the unit
        singles = []
        for k in '123456789': ## count instances of 1-9 in the all_Values string
            if all_values.count(k) == 1: 
                ## find the box that contains the singleton value and assign it to that box
                for key in unit:
                    if( k in values[key] ):
                        assign_value(values, key, k)
    return values

def reduce_puzzle(values):
    """Reduce the puzzle using different strategies
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the reduced options
    """
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        eliminate(values)

        # Your code here: Use the Only Choice Strategy
        only_choice(values)

        # add the naked-twins
        naked_twins(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

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
    for key in values:
        assign_value(values, key, values[key])

    return search(values)


if __name__ == '__main__':
    #diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    diag_sudoku_grid ='9.1....8.8.5.7..4.2.4....6...7......5..............83.3..6......9................'
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