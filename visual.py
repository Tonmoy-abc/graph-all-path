graph1 = [[1, 7],
 [2, 8],
 [3, 9],
 [4, 10],
 [5, 11],
 [6, 12],
 [13],
 [8, 14],
 [9, 15],
 [10, 16],
 [11, 17],
 [12, 18],
 [13, 19],
 [20],
 [15, 21],
 [16, 22],
 [17, 23],
 [18, 24],
 [19, 25],
 [20, 26],
 [27],
 [22, 28],
 [23, 29],
 [24, 30],
 [25, 31],
 [26, 32],
 [27, 33],
 [34],
 [29, 35],
 [30, 36],
 [31, 37],
 [32, 38],
 [33, 39],
 [34, 40],
 [41],
 [36],
 [37],
 [38],
 [39],
 [40],
 [41],
 [],
 ]

for index, item in enumerate(graph1):
    print(index, " ".join(map(lambda x:str(x),item)))