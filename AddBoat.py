def addBoats(userGrid):
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

    print("Vertical or horizontal ? (V/H)")
    dBattleship = input()
    if (dBattleship == V):
        if (jBattleship < 8):
            userGrid.ships["Battleship"].cells.append(userGrid.grid[iBattleship][jBattleship])
            userGrid.ships["Battleship"].cells.append(userGrid.grid[iBattleship][jBattleship+1])
            userGrid.ships["Battleship"].cells.append(userGrid.grid[iBattleship][jBattleship+2])
            userGrid.ships["Battleship"].cells.append(userGrid.grid[iBattleship][jBattleship+3])
        else:
            userGrid.ships["Battleship"].cells.append(userGrid.grid[iBattleship][jBattleship])
            userGrid.ships["Battleship"].cells.append(userGrid.grid[iBattleship][jBattleship-1])
            userGrid.ships["Battleship"].cells.append(userGrid.grid[iBattleship][jBattleship-2])
            userGrid.ships["Battleship"].cells.append(userGrid.grid[iBattleship][jBattleship-3])
    else:
        if (iBattleship < 8):
            userGrid.ships["Battleship"].cells.append(userGrid.grid[iBattleship][jBattleship])
            userGrid.ships["Battleship"].cells.append(userGrid.grid[iBattleship+1][jBattleship])
            userGrid.ships["Battleship"].cells.append(userGrid.grid[iBattleship+2][jBattleship])
            userGrid.ships["Battleship"].cells.append(userGrid.grid[iBattleship+3][jBattleship])
        else:
            userGrid.ships["Battleship"].cells.append(userGrid.grid[iBattleship][jBattleship])
            userGrid.ships["Battleship"].cells.append(userGrid.grid[iBattleship-1][jBattleship])
            userGrid.ships["Battleship"].cells.append(userGrid.grid[iBattleship-2][jBattleship])
            userGrid.ships["Battleship"].cells.append(userGrid.grid[iBattleship-3][jBattleship])
    
    
    print("Cruiser ? (3) (row,column):")
    iCruiser,x,jCruiser = input()
    print(iCruiser,jCruiser)

    print("Vertical or horizontal ? (V/H)")
    dCruiser = input()
    if (dCruiser == V):
        if (jCruiser < 9):
            userGrid.ships["Cruiser"].cells.append(userGrid.grid[iCruiser][jCruiser])
            userGrid.ships["Cruiser"].cells.append(userGrid.grid[iCruiser][jCruiser+1])
            userGrid.ships["Cruiser"].cells.append(userGrid.grid[iCruiser][jCruiser+2])
        else:
            userGrid.ships["Cruiser"].cells.append(userGrid.grid[iCruiser][jCruiser])
            userGrid.ships["Cruiser"].cells.append(userGrid.grid[iCruiser][jCruiser-1])
            userGrid.ships["Cruiser"].cells.append(userGrid.grid[iCruiser][jCruiser-2])
    else:
        if (iCruiser < 9):
            userGrid.ships["Cruiser"].cells.append(userGrid.grid[iCruiser][jCruiser])
            userGrid.ships["Cruiser"].cells.append(userGrid.grid[iCruiser+1][jCruiser])
            userGrid.ships["Cruiser"].cells.append(userGrid.grid[iCruiser+2][jCruiser])
        else:
            userGrid.ships["Cruiser"].cells.append(userGrid.grid[iCruiser][jCruiser])
            userGrid.ships["Cruiser"].cells.append(userGrid.grid[iCruiser-1][jCruiser])
            userGrid.ships["Cruiser"].cells.append(userGrid.grid[iCruiser-2][jCruiser])

    
    print("Submarine ? (3) (row,column):")
    iSubmarine,x,jSubmarine = input()
    print(iSubmarine,jSubmarine)

    print("Vertical or horizontal ? (V/H)")
    dSubmarine = input()
    if (dSubmarine == V):
        if (jSubmarine < 9):
            userGrid.ships["Submarine"].cells.append(userGrid.grid[iSubmarine][jSubmarine])
            userGrid.ships["Submarine"].cells.append(userGrid.grid[iSubmarine][jSubmarine+1])
            userGrid.ships["Submarine"].cells.append(userGrid.grid[iSubmarine][jSubmarine+2])
        else:
            userGrid.ships["Submarine"].cells.append(userGrid.grid[iSubmarine][jSubmarine])
            userGrid.ships["Submarine"].cells.append(userGrid.grid[iSubmarine][jSubmarine-1])
            userGrid.ships["Submarine"].cells.append(userGrid.grid[iSubmarine][jSubmarine-2])
    else:
        if (iSubmarine < 9):
            userGrid.ships["Submarine"].cells.append(userGrid.grid[iSubmarine][jSubmarine])
            userGrid.ships["Submarine"].cells.append(userGrid.grid[iSubmarine+1][jSubmarine])
            userGrid.ships["Submarine"].cells.append(userGrid.grid[iSubmarine+2][jSubmarine])
        else:
            userGrid.ships["Submarine"].cells.append(userGrid.grid[iSubmarine][jSubmarine])
            userGrid.ships["Submarine"].cells.append(userGrid.grid[iSubmarine-1][jSubmarine])
            userGrid.ships["Submarine"].cells.append(userGrid.grid[iSubmarine-2][jSubmarine])
    
    
    print("Destroyer ? (2) (row,column):")
    iDestroyer,x,jDestroyer = input()
    print(iDestroyer,jDestroyer)

    print("Vertical or horizontal ? (V/H)")
    dDestroyer = input()
    if (dDestroyer == V):
        if (jDestroyer < 10):
            userGrid.ships["Destroyer"].cells.append(userGrid.grid[iDestroyer][jDestroyer])
            userGrid.ships["Destroyer"].cells.append(userGrid.grid[iDestroyer][jDestroyer+1])
        else:
            userGrid.ships["Destroyer"].cells.append(userGrid.grid[iDestroyer][jDestroyer])
            userGrid.ships["Destroyer"].cells.append(userGrid.grid[iDestroyer][jDestroyer-1])
    else:
        if (iDestroyer < 10):
            userGrid.ships["Destroyer"].cells.append(userGrid.grid[iDestroyer][jDestroyer])
            userGrid.ships["Destroyer"].cells.append(userGrid.grid[iDestroyer+1][jDestroyer])
        else:
            userGrid.ships["Destroyer"].cells.append(userGrid.grid[iDestroyer][jDestroyer])
            userGrid.ships["Destroyer"].cells.append(userGrid.grid[iDestroyer-1][jDestroyer])

addBoats()
