import time

first_time = time.time()

almacen_uno = [[[[3, 5, 2], [6, 1, 9], [8, 7, 4]], 
                [[3, 5, 2], [6, 1, 9], [8, 7, 4]], 
                [[3, 5, 2], [6, 1, 9], [8, 7, 4]]], 
               [[[3, 5, 2], [6, 1, 9], [8, 7, 4]], 
                [[3, 5, 2], [6, 1, 9], [8, 7, 4]], 
                [[3, 5, 2], [6, 1, 9], [8, 7, 4]]],
               [[[3, 5, 2], [6, 1, 9], [8, 7, 4]], 
                [[3, 5, 2], [6, 1, 9], [8, 7, 4]], 
                [[3, 5, 2], [6, 1, 9], [8, 7, 4]]]]

string = "".join([str(col_two) for row in almacen_uno for col in row for row_two in col for col_two in row_two])
print(string)

second_time = time.time()

print(second_time - first_time)

first_time = time.time()

almacen_dos = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]


string = "".join([str(col) for row in almacen_dos for col in row])
print(string)



second_time = time.time()

print(second_time - first_time)
