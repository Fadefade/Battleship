def askBoats(userGrid):
    print("Enter a cell to put your boats on the grid")

    print("Carrier ? (5) (row,column):")
    iCarrier,x,jCarrier = input()
    print(iCarrier,jCarrier)

    print("Vertical or horizontal ? (V/H)")
    dCarrier = input()
    if (dCarrier == V):
        if (jCarrier < 7):
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier][jCarrier])
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier][jCarrier+1])
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier][jCarrier+2])
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier][jCarrier+3])
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier][jCarrier+4])
        else:
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier][jCarrier])
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier][jCarrier-1])
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier][jCarrier-2])
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier][jCarrier-3])
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier][jCarrier-4])

    else:
        if (iCarrier < 7):
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier][jCarrier])
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier+1][jCarrier])
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier+2][jCarrier])
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier+3][jCarrier])
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier+4][jCarrier])
        else:
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier][jCarrier])
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier-1][jCarrier])
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier-2][jCarrier])
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier-3][jCarrier])
            userGrid.ships["Carrier"].cells.append(userGrid.grid[iCarrier-4][jCarrier])

    print("Battleship ? (4) (row,column):")
    iBattleship,x,jBattleship = input()
    print(iBattleship,jBattleship)
    
    
    print("Cruiser ? (3) (row,column):")
    iCruiser,x,jCruiser = input()
    print(iCruiser,jCruiser)

    
    print("Submarine ? (3) (row,column):")
    iSubmarine,x,jSubmarine = input()
    print(iSubmarine,jSubmarine)
    
    
    print("Destroyer ? (2) (row,column):")
    iDestroyer,x,jDestroyer = input()
    print(iDestroyer,jDestroyer)
    

def direction():
    print("Vertical or horizontal ? (V/H)")

putBoats()
