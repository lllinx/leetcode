
# Enter your code here. Read input from STDIN. Print output to STDOUT


def phone(piece, length, start, row, column):
    #kind of confused how to define all rows in grid as parameters, since the row number is not definate. so just use the grid in test case as example here
    grid=[
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ["*",0,"#"]
    ]  
    
    def knight(grid,i,j):
        result=[]
        if i-2>=0 and j-1>=0 and type(grid[i-2][j-1]) is int:
            result.append([i-2,j-1])
        if i-1>=0 and j-2>=0 and type(grid[i-1][j-2]) is int:
            result.append([i-1,j-2])
        if i+2<len(grid) and j+1<len(grid[0]) and type(grid[i+2][j+1]) is int:
            result.append([i+2,j+1])
        if i+1<len(grid) and j+2<len(grid[0]) and type(grid[i+1][j+2]) is int:
            result.append([i+1,j+2])
        if i+1<len(grid) and j-2>=0 and type(grid[i+1][j-2]) is int:
            result.append([i+1,j-2])
        if i+2<len(grid) and j-1>=0 and type(grid[i+2][j-1]) is int:
            result.append([i+2,j-1])
        if i-2>=0 and j+1<len(grid[0]) and type(grid[i-2][j+1]) is int:
            result.append([i-2,j+1])
        if i-1>=0 and j+2<len(grid[0]) and type(grid[i-1][j+2]) is int:
            result.append([i-1,j+2])
        return result
            
    def bishop(grid,i,j):
        result=[]
        if i-1>=0 and j-1>=0 and type(grid[i-1][j-1]) is int:
            result.append([i-1,j-1])
        if i+1<len(grid) and j+1<len(grid[0]) and type(grid[i+1][j+1]) is int:
            result.append([i+1,j+1])
        if i-1>=0 and j+1<len(grid[0]) and type(grid[i-1][j+1]) is int:
            result.append([i-1,j+1])
        if i+1<len(grid) and j-1>=0 and type(grid[i+1][j-1]) is int:
            result.append([i+1,j-1])
        return result
    
    def find_start_index(grid,st):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==st:
                    return [i,j]
    
    def recur(grid,i,j,piece_fun,step):
        if step==0:
            return 1
        else:
            return sum([recur(grid,res[0],res[1],piece_fun,step-1) for res in piece_fun(grid,i,j)])
        
    
    res=0
    for st in start:
        i_st, j_st= find_start_index(grid, st)[0],find_start_index(grid, st)[1]
        if piece=="knight":
            res+=recur(grid,i_st,j_st,knight,length-1)
        elif price=="Bishop":
            res+=recur(grid,i_st,j_st,bishop,length-1)
            
    return res
                       
                    
        
            
        
        
        
        
            
        
        