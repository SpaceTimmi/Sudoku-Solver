# In progress

#VAL is any Natural from [1, 9]
#Position is a list of size 81 and can contain any VAL



# Natural, Natural -> Natural
# Convert a give row and column into a position
def rc_to_col(row, column):
   return ((row * 9) + column)

ALL_VALS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
B = False

BD1 =  [B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B, B]
 
BD2  = [2, 7, 4, B, 9, 1, B, B, 5,
        1, B, B, 5, B, B, B, 9, B,
        6, B, B, B, B, 3, 2, 8, B,
        B, B, 1, 9, B, B, B, B, 8,
        B, B, 5, 1, B, B, 6, B, B,
        7, B, B, B, 8, B, B, B, 3,
        4, B, 2, B, B, B, B, B, 9,
        B, B, B, B, B, B, B, 7, B,
        8, B, B, 3, 4, 9, B, B, B]

#solution to 2
BD2s = [2, 7, 4, 8, 9, 1, 3, 6, 5,
        1, 3, 8, 5, 2, 6, 4, 9, 7,
        6, 5, 9, 4, 7, 3, 2, 8, 1,
        3, 2, 1, 9, 6, 4, 7, 5, 8,
        9, 8, 5, 1, 3, 7, 6, 4, 2,
        7, 4, 6, 2, 8, 5, 9, 1, 3,
        4, 6, 2, 7, 5, 8, 1, 3, 9,
        5, 9, 3, 6, 1, 2, 8, 7, 4,
        8, 1, 7, 3, 4, 9, 5, 2, 6]
 
BD3 =  [5, B, B, B, B, 4, B, 7, B,
        B, 1, B, B, 5, B, 6, B, B,
        B, B, 4, 9, B, B, B, B, B,
        B, 9, B, B, B, 7, 5, B, B,
        1, 8, B, 2, B, B, B, B, B, 
        B, B, B, B, B, 6, B, B, B, 
        B, B, 3, B, B, B, B, B, 8,
        B, 6, B, B, 8, B, B, B, 9,
        B, B, 8, B, 7, B, B, 3, 1]

#solution to 3 
BD3s = [5, 3, 9, 1, 6, 4, 8, 7, 2,
        8, 1, 2, 7, 5, 3, 6, 9, 4,
        6, 7, 4, 9, 2, 8, 3, 1, 5,
        2, 9, 6, 4, 1, 7, 5, 8, 3,
        1, 8, 7, 2, 3, 5, 9, 4, 6,
        3, 4, 5, 8, 9, 6, 1, 2, 7,
        9, 2, 3, 5, 4, 1, 7, 6, 8,
        7, 6, 1, 3, 8, 2, 4, 5, 9,
        4, 5, 8, 6, 7, 9, 2, 3, 1]
 
#no solution
BD4 =  [1, 2, 3, 4, 5, 6, 7, 8, B, 
        B, B, B, B, B, B, B, B, 2, 
        B, B, B, B, B, B, B, B, 3, 
        B, B, B, B, B, B, B, B, 4, 
        B, B, B, B, B, B, B, B, 5,
        B, B, B, B, B, B, B, B, 6,
        B, B, B, B, B, B, B, B, 7,
        B, B, B, B, B, B, B, B, 8,
        B, B, B, B, B, B, B, B, 9] 








