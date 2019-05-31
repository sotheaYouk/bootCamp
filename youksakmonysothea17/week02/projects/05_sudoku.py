# check invalid format 
def check_invalid_format(board):
    try:
        for row in range(9): 
            for column in range(9):
                if not 1 <= int(board[row][column]) <= 9:
                    return 0

    except (IndexError, ValueError):
        return 0


# check duplication y row and column 
def check_row_col(my_list, my_range):
    my_row = []
    my_column = []
    
    # check duplication by row and column 
    for row in range(my_range): 

        # get elem by row and by column
        for column in range(my_range):
            my_row.append(my_list[row][column])
            my_column.append(my_list[column][row])
        
        # check duplication in by row 
        for index in range(my_range):
            row_dupes = my_row.count(my_row[index])
            col_dupes = my_column.count(my_column[index])

            if row_dupes > 1 or col_dupes > 1:
                return 0 
        
        my_row.clear()
        my_column.clear()

    
# check region 
def check_region(board):
    mini_array = list()
    nano_array = list()
    row_start = 0 
    row_end = 3 
    col_start = 0 
    col_end = 3

    while row_end <= 9:
        while col_end <= 9:
            for row in range(row_start, row_end):
                for col in range(col_start, col_end):
                    nano_array.append(board[row][col])
                mini_array.append(nano_array)
                nano_array = []
                            
            # check dupes
            check_out =  check_row_col(mini_array, 3)
            
            if check_out == 0:
                return 0

            col_start += 3
            col_end += 3
        
        row_start += 3 
        row_end += 3
        col_start = 0 
        col_end = 3 

# main function
def sudoku(board):

    # check invalid format
    check_out = check_invalid_format(board)

    if check_out == 0:
        print("Invalid Format")

        return "Invalid Format"
    
    else: 

        # check row and column
        check_row_col_return_= check_row_col(board, 9) 

        # check region
        check_region_return = check_region(board)

        if check_row_col_return_ == 0 or check_region_return == 0: 
            print("Not finished")

            return "Not finished"
        
        else:
            print("Finished")

            return "Finished"


sudoku([ [0, 12, 3, 5, 7, 9, 4, 6, 8], [4, 9, 1, 2, 3, 7, 5], [7, 5, 6, 1, 8, 4, 2, 1, 9], [6, 4, 4, 1, 5, 8, 7, 9, 2], [5, 2, 1, 7, 1, 1, 1, 1, 1], [9, 8, 7, 4, 2, 6, 5, 3, 1], [2, 1, 4, 9, 3, 5, 2, 2, 7], [3, 6, 5, 8, 1, 7, 9, 2, 4], [8, 7, 9, 6, 4, 2, 1, 5, 3]]) 
 
