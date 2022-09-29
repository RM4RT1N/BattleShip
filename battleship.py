def create_board():
    letters = 'abcde'
    nums = ['-','|',1,2,3,4,5]
    board = []
    for i in range(len(letters)):
        board.append([0]*5)
    print(*nums)
    print('  -----------')       
    for i in range (len(board)):
        print(letters[i],'|', *board[i])
    return board


def draw_board(board):
    letters = 'abcde'
    nums = ['-','|',1,2,3,4,5]
    print(*nums)
    print('  -----------')  
    for i in range(len(board)):
        print(letters[i],'|', *board[i])


def check_char(tab):
    while True:
        char = input().lower()
        if char in tab:
            break
    return char


def choose_size_ship(name,table_of_ships):
    names = ''
    for element in table_of_ships:
        if element == 's':
            names = names +'[s]mall'+' '
        else:
            names = names +'[m]edium'+' '
    print(f' {name} which size of ship do you input on board {names}?')
    while True:
        size = input().lower()
        if size == 's' or 'm':
            break
    return size


def fields_all_around(x, y):
    list_x = [x-1,x+1]
    list_y = [y-1,y+1]
    for position in list_x:
        if position <= 0 or position >= 6:
            list_x.remove(position)
    for position in list_y:
        if position <= 0 or position >= 6:
            list_y.remove(position)
    return(list_x,list_y)


def create_all_possibles_on_board():
    letters = 'abcde'
    table = []
    
    for char in letters:
        for num in range(1,len(letters)+1):
            table.append(char+str(num))
    return table

def place_ship(size,board,name):
    letters = 'abcde'
    all_shot_possibles = create_all_possibles_on_board()
    pos_of_ships = []
    if size == 's':
        n=1 
    else:
        n=2

    while True:
        while True:
            print(f'Captain {name} please give position to place a ship first letter and second num for example a1 ')
            hit = check_char(all_shot_possibles)
            for char in letters:
                if char == hit[0].lower(): 
                    zmienna = int(letters.index(char)) 
            lista_do_sprawdzenia = available(board,zmienna+1,int(hit[1]),1)
            mozliwe1 = []
            for num in range(0,len(lista_do_sprawdzenia),2):                  
                mozliwe1.append(str(lista_do_sprawdzenia[num])+str(lista_do_sprawdzenia[num+1]))
            num_hits = available(board,zmienna+1,int(hit[1]),0)
        
            if board[zmienna][int(hit[1])-1] != 'X' and num_hits == len(mozliwe1):  
                board[zmienna][int(hit[1])-1] = 'X'
                break
            else:
                print(f'Captain {name} you should choose an available position')
        if n== 2:
            draw_board(board)
            list = available(board,zmienna+1,int(hit[1]),1)
            mozliwe = []
            for num in range(0,len(list),2):                  
                mozliwe.append(str(list[num])+str(list[num+1]))
            na_pewno = check_to_make_sure(mozliwe,board)
            if na_pewno == []:
                board[zmienna][int(hit[1])-1] = '0'
                continue
            while True:
                print(f'Captain {name} please give a second position to place a ship you have only : {na_pewno}')
                hit2 = check_char(na_pewno)
                for char in letters:
                    if char == hit2[0].lower():
                        zmienna2 = int(letters.index(char)) 
                if board[zmienna2][int(hit2[1])-1] != 'X':  
                    board[zmienna2][int(hit2[1])-1] = 'X'
                    break
                else:
                    print(f'Captain {name} you should choose an available position')

        if n == 2:
            pos_of_ships.append(hit)
            pos_of_ships.append(hit2)
        else:
            pos_of_ships.append(hit)
        return board,pos_of_ships


def input_ships(name):
    plansza = create_board()
    print()
    table_of_ships = ['s','s','m']
    table_of_input_ships = []
    while len(table_of_ships) > 0 :
        
        while True:

            size = choose_size_ship(name,table_of_ships)
           
            if size in table_of_ships:
                table_of_ships.remove(size)
                break 
        two_of_var = place_ship(size,plansza,name)
        plansza = two_of_var[0]
        table_of_input_ships.append(two_of_var[1])
        draw_board(plansza)
    return [plansza,table_of_input_ships]


def available(board,x,y,type):
    table = fields_all_around(x,y)
    hits = 0
    number_of_capabilities = 0
    tab = []
    for pos in table[0]:
        if board[int(pos)-1][y-1] != "X":
            board[int(pos)-1][y-1] = "D"
            number_of_capabilities += 1
        else:
            hits +=1
            number_of_capabilities += 1

    for pos in table[1]:
        if board[x-1][int(pos)-1] !="X":
            board[x-1][int(pos)-1] ="D"
            number_of_capabilities += 1
        else:
            hits +=1
            number_of_capabilities += 1
    for row in range(len(board)):
        for sign in range(len(board[row])):
            if board[row][sign] == "D":
                tab.append([row,sign+1])
                board[row][sign] = "0"
    tab_new = []
    for row in tab:
        letters = 'abcde'
        row[0] = letters[row[0]]
        tab_new = tab_new+row
    
    if type == 1:
        return tab_new
    elif type == 2:
        return hits
    else:
        return number_of_capabilities


def check_to_make_sure(tab,board):
    letters = 'abcde'
    list = []
    for row in tab:
        varofx = row[0]
        for char in letters:
            if varofx == char:
                varx = int(letters.index(char))+ 1
        vary = int(row[1])
        if available(board,varx,vary,2) == 1:
            list.append(str(row))
            
    return list


def check_shots(shot,list):
    status = 0
    if shot in list:
        status = 1
        list.remove(shot)
        if len(list) != 0:
            print('trafiony')
        else:
            print('trafiony, zatopiony')
    return list, status
        

player1 = input('Player1 please your name ') 
data_first = input_ships(player1)
board_of_player_1 = data_first[0]
list_with_ships_player1 = data_first[1]
player1_1ship = list_with_ships_player1[0]
player1_2ship = list_with_ships_player1[1]
player1_3ship = list_with_ships_player1[2]
player2 = input('Player2 please your name ')
data_second = input_ships(player2)
board_of_player_2 = data_second[0]
list_with_ships_player2 = data_second[1]
player2_1ship = list_with_ships_player2[0]
player2_2ship = list_with_ships_player2[1]
player2_3ship = list_with_ships_player2[2]
letters = 'abcde'
board_to_shots_player1 = create_board()
board_to_shots_player2 = create_board()
active_player = [player1,player2]
shots_player1 = 10
shots_player2 = 10
all_possibles = create_all_possibles_on_board()
while True:
    if shots_player1 == 0 and shots_player2 == 0:
        print (' End game nobody wins')
        break
    else:
        
        draw_board(board_to_shots_player1)
        print(f'Captain {active_player[0]} please shot to board player {active_player[1]}')
        shot = check_char(all_possibles)
        shots_player1 -= 1
        for char in letters:
                if char == shot[0].lower(): 
                    zmienna = int(letters.index(char))
        player2_1ship_data = check_shots(shot,player2_1ship)
        player2_2ship_data = check_shots(shot,player2_2ship)
        player2_3ship_data = check_shots(shot,player2_3ship)
        player2_1ship = player2_1ship_data[0]
        player2_2ship = player2_2ship_data[0]
        player2_3ship = player2_3ship_data[0]
        if  player2_1ship_data[1] == 0 and player2_2ship_data[1] == 0 and player2_3ship_data[1] == 0:
            print('Oooops you missed....')
            char_shot = 'M'
        else:
            char_shot = 'H'
         
        board_to_shots_player1[zmienna][int(shot[1])-1] = char_shot
        if  len(player2_1ship) == 0 and len(player2_2ship) == 0 and len(player2_3ship) == 0:
            print(f'Captain {active_player[0]} you win')
            break
    if shots_player1 == 0 and shots_player2 == 0:
        print (' End game nobody wins')
        break
    else:
        draw_board(board_to_shots_player2)
        print(f'Captain {active_player[1]} please shot to board player {active_player[0]}')
        shot = check_char(all_possibles)
        shots_player2 -= 1
        player1_1ship_data = check_shots(shot,player1_1ship)
        player1_2ship_data = check_shots(shot,player1_2ship)
        player1_3ship_data = check_shots(shot,player1_3ship)
        player1_1ship = player1_1ship_data[0]
        player1_2ship = player1_2ship_data[0]
        player1_3ship = player1_3ship_data[0]
        if  player1_1ship_data[1] == 0 and player1_2ship_data[1] == 0 and player1_3ship_data[1] ==0:
            print('Oooops you missed....')
            char_shot = 'M'
        else:
            char_shot = 'H'
         
        board_to_shots_player2[zmienna][int(shot[1])-1] = char_shot
        if  len(player1_1ship) == 0 and len(player1_2ship) == 0 and len(player1_3ship) ==0:
            print(f'Captain {active_player[1]} you win') 
            break  
        
print('You reached to end of game bravo')
             