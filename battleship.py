import os
import random
import time
import sys

GLOBAL_LETTERS = 'ABCDEFGHIJ' 
GLOBAL_NUMS = [' ','|',1,2,3,4,5,6,7,8,9,10]
logo =(
 
    """
 ______     ______     ______   ______   __         ______        ______     __  __     __     ______  
/\  == \   /\  __ \   /\__  _\ /\__  _\ /\ \       /\  ___\      /\  ___\   /\ \_\ \   /\ \   /\  == \ 
\ \  __<   \ \  __ \  \/_/\ \/ \/_/\ \/ \ \ \____  \ \  __\      \ \___  \  \ \  __ \  \ \ \  \ \  _-/ 
 \ \_____\  \ \_\ \_\    \ \_\    \ \_\  \ \_____\  \ \_____\     \/\_____\  \ \_\ \_\  \ \_\  \ \_\   
  \/_____/   \/_/\/_/     \/_/     \/_/   \/_____/   \/_____/      \/_____/   \/_/\/_/   \/_/   \/_/   
 
 
                                                                POWERED by Beata Krzysztof Marcin  BKM ©
     """
)    


def create_board(letters):
    board = []
    for i in range(len(letters)):
        board.append([0]*len(letters))
    return board


def draw_board(board,nums,letters):
    print(*nums)
    print('  -----------')  
    for i in range(len(board)):
        print(letters[i],'|', *board[i])


def check_char(tab):
    while True:
        char = input().upper()
        if char in tab:
            break
        else:
            print('Please a valid input')
    return char


def choose_size_ship(name,table_of_ships,second_player,player2):
    
    names = ''
    for element in table_of_ships:
        if element == 's':
            names = names +'[s]mall'+' '
        else:
            names = names +'[m]edium'+' '
    if second_player == '2' and name == 'Computer':
        print()
    else:
        up_window()
        print(f'{name} which size of ship do you input on board {names}?')
    while True:
        if player2 == 'Computer' and second_player == '2':
            
            size = random.choice(table_of_ships)
            break
        else:
            size = input().lower()
            if size == 's' or 'm':
                break
            
    return size


def fields_all_around(x, y,letters):   
    list_x = [x-1,x+1]       
    list_y = [y-1,y+1]    
    for position in list_x:
        if position <= 0 or position >= (len(letters)+1):
            list_x.remove(position)
    for position in list_y:
        if position <= 0 or position >= (len(letters)+1):
            list_y.remove(position)
    return(list_x,list_y)


def create_all_possibles_on_board(letters):
    
    table = []
    
    for char in letters:
        for num in range(1,len(letters)+1):
            table.append(char+str(num))
    return table


def place_ship(size,board,name,nums,letters,second_player):
    all_shot_possibles = create_all_possibles_on_board(letters)
    pos_of_ships = []
    if size == 's':
        n=1 
    else:
        n=2

    while True:
        while True:
            
            if second_player == '2' and name == 'Computer':
                all_shot_possibles_ai = create_all_possibles_on_board(letters)
                hit = random.choice(all_shot_possibles_ai)
                all_shot_possibles_ai.remove(hit)
            else:
                up_window()
                print(f'Captain {name} please give position to place a ship first letter and second num for example a1 ')
                draw_board(board,nums,letters)
                hit = check_char(all_shot_possibles)
                up_window()
            for char in letters:
                if char == hit[0].upper(): 
                    zmienna = int(letters.index(char)) 
            lista_do_sprawdzenia = available(board,zmienna+1,int(hit[1]),1,letters)  
            mozliwe1 = []
            for num in range(0,len(lista_do_sprawdzenia),2):                  
                mozliwe1.append(str(lista_do_sprawdzenia[num])+str(lista_do_sprawdzenia[num+1]))
            num_hits = available(board,zmienna+1,int(hit[1]),0,letters)
        
            if board[zmienna][int(hit[1])-1] != 'X' and num_hits == len(mozliwe1):  
                board[zmienna][int(hit[1])-1] = 'X'
                break
            else:
                if second_player == '2' and name == 'Computer':
                    print()
                else:
                    print(f'Captain {name} you should choose an available position, ships are too close')
                    time.sleep(1)
        if n== 2:
            if second_player == '2' and name == 'Computer':
                print()
            else:
                draw_board(board,nums,letters)
            list = available(board,zmienna+1,int(hit[1]),1,letters)
            mozliwe = []
            for num in range(0,len(list),2):                  
                mozliwe.append(str(list[num])+str(list[num+1]))
            na_pewno = check_to_make_sure(mozliwe,board,letters)
            if na_pewno == []:
                board[zmienna][int(hit[1])-1] = '0'
                continue
            while True:
                
                if second_player == '2' and name == 'Computer':
                    hit2 = random.choice(na_pewno)
                else:
                    up_window()
                    draw_board(board,nums,letters)
                    print(f'Captain {name} please give a second position to place a ship you have only : {na_pewno}')
                    hit2 = check_char(na_pewno)
                for char in letters:
                    if char == hit2[0].upper():
                        zmienna2 = int(letters.index(char)) 
                if board[zmienna2][int(hit2[1])-1] != 'X':  
                    board[zmienna2][int(hit2[1])-1] = 'X'
                    break
                else:
                    if second_player == '2' and name == 'Computer':
                        print()
                    else:
                        print(f'Captain {name} you should choose an available position , ships are too close')
                        time.sleep(1)

        if n == 2:
            pos_of_ships.append(hit)
            pos_of_ships.append(hit2)
        else:
            pos_of_ships.append(hit)
        return board,pos_of_ships


def input_ships(name,nums,letters,second_player,player2):
    plansza = create_board(letters)
    table_of_ships = ['s','s','m']
    table_of_input_ships = []
    while len(table_of_ships) > 0 :
        
        while True:

            size = choose_size_ship(name,table_of_ships,second_player,player2)
           
            if size in table_of_ships:
                table_of_ships.remove(size)
                break 
        two_of_var = place_ship(size,plansza,name,nums,letters,second_player)
        plansza = two_of_var[0]
        table_of_input_ships.append(two_of_var[1])
        if second_player == '2' and name == 'Computer':
            print()
        else:
            draw_board(plansza,nums,letters)
    return [plansza,table_of_input_ships]


def available(board,x,y,type,letters):
    table = fields_all_around(x,y,letters) 
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
        
        row[0] = letters[row[0]]
        tab_new = tab_new+row
    
    if type == 1:
        return tab_new
    elif type == 2:
        return hits
    else:
        return number_of_capabilities


def check_to_make_sure(tab,board,letters):
    
    list = []
    for row in tab:
        varofx = row[0]
        for char in letters:
            if varofx == char:
                varx = int(letters.index(char))+ 1
        vary = int(row[1])
        if available(board,varx,vary,2,letters) == 1:
            list.append(str(row))
            
    return list


def check_shots(shot,inp_list):
    status = 0
    char= ''
    new_list = []
    if shot in inp_list:
        status = 1
        new_list = list(inp_list)
        inp_list.remove(shot)
        if len(inp_list) != 0:
            print("You've hit a ship!")
            char = 'H'
    

        else:
            print("You've sunk a ship!")
            char = 'S'

            

    return inp_list, status, char, new_list


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def ai(tab):
    return random.choice(tab)


def set_shoots():
    shoots = 0
    difficulty = input("""
Set dificulty level 
Press 1 - easy (20 shoots)
Press 2 - medium (15 shoots)
Press 3 - hard (10 shoots)

Insert Your Choice:  """)
    if difficulty == "1":
        print("So easy! You do this!")
        shoots = 20
    elif difficulty == "2":
        print("That's a spirit!")
        shoots = 15
    elif difficulty == "3":
        print("Awesome! Are you ready?")
        shoots = 10
    elif difficulty == "quit":
        print("""
                 _______  _______  _______  ______   ______            _______ 
                (  ____ \(  ___  )(  ___  )(  __  \ (  ___ \ |\     /|(  ____ \
                | (    \/| (   ) || (   ) || (  \  )| (   ) )( \   / )| (    \/
                | |      | |   | || |   | || |   ) || (__/ /  \ (_) / | (__    
                | | ____ | |   | || |   | || |   | ||  __ (    \   /  |  __)   
                | | \_  )| |   | || |   | || |   ) || (  \ \    ) (   | (      
                | (___) || (___) || (___) || (__/  )| )___) )   | |   | (____/\
                (_______)(_______)(_______)(______/ |/ \___/    \_/   (_______/
                """
              )
        sys.exit()
    else:
        up_window()
        print("You must select dificulty!")
        set_shoots()
    return shoots


def up_window():
    clear_console()
    print(logo)


def get_player():
    player = ""
    while player == "":
        up_window()
        player = input("Get Nick of gamer:")
    return player 


def get_menu_trouble():
    while True:
        menuYtB ="""
What is Your Choice:
Please input number from 5 to 10
            """
        
        print(menuYtB)
        yourTrouble = input("Choice size of board:  ")
        if int(yourTrouble) >= 5 and int(yourTrouble)<=10:
            break
        else:
            print("bad choice, try again") 
            time.sleep(1)
            up_window()
    return yourTrouble


def get_menu_option():
    while True:
        menuGetoption ="""
What is Your Choice:
1. Human vs Human
2. Human vs (Computer)
            """
        
        print(menuGetoption)
        yourChoice = input("Insert Your Choice:  ")
        if is_valid(yourChoice):
            break
        else:
            print("bad choice, try again ")
            time.sleep(1)
            up_window()
    return yourChoice


def is_valid(operator): 
    if operator in ["1","2"]:
        return True
    else:
        return False 


def game():
    up_window()
    size_of_board = get_menu_trouble()
    up_window()
    number_of_shots = set_shoots()
    up_window()
    second_player = get_menu_option()
    up_window()
    letters = GLOBAL_LETTERS[:int(size_of_board)]
    nums = GLOBAL_NUMS[:(int(size_of_board)+2)]
    player2 = ''
    player1 = get_player() 
    up_window()
    data_first = input_ships(player1,nums,letters,second_player,player2)
    up_window()
    print ('Please any key to start place ships next player')
    input()
    if second_player == 1:
        player2 = get_player()
    else:
        player2 = 'Computer'
        all_shots = create_all_possibles_on_board(letters)
    data_second = input_ships(player2,nums,letters,second_player,player2)
    temp_of_hits_player_1 = []
    temp_of_hits_player_2 = []

    board_to_shots_player1 = create_board(letters)
    board_to_shots_player2 = create_board(letters)
    active_player = [player1,player2]
    shots_player1 = number_of_shots

    shots_player2 = number_of_shots
    all_possibles = create_all_possibles_on_board(letters)
    all_possibles2 = create_all_possibles_on_board(letters)

    while True:
        if shots_player1 == 0 and shots_player2 == 0:
            print (' End game nobody wins')
            break
        else:
            up_window()
            draw_board(board_to_shots_player1,nums,letters)
            print(f'Captain {active_player[0]} please shot to board player {active_player[1]}')
            shot = check_char(all_possibles)
            all_possibles.remove(shot)
            shots_player1 -= 1
            for char in letters:
                if char == shot[0].upper(): 
                    zmienna = int(letters.index(char))
            player2_1ship_data = check_shots(shot,data_second[1][0])
            player2_2ship_data = check_shots(shot,data_second[1][1])
            player2_3ship_data = check_shots(shot,data_second[1][2])
        
        
        if  player2_1ship_data[1] == 0 and player2_2ship_data[1] == 0 and player2_3ship_data[1] == 0:
            print('Oooops you missed....')
            char_shot = 'M'
        else:
            if player2_1ship_data[2] != '':
                char_shot = player2_1ship_data[2]
            elif player2_2ship_data[2] != '':
                char_shot = player2_2ship_data[2]
            else:
                char_shot = player2_3ship_data[2]
        if char_shot == 'H':    
            temp_of_hits_player_1+= player2_1ship_data[3]
            temp_of_hits_player_1+= player2_2ship_data[3]
            temp_of_hits_player_1+= player2_3ship_data[3]      
        if char_shot == 'S':
            if shot in temp_of_hits_player_1:
                if temp_of_hits_player_1.index(shot)%2 == 0:
                    to_change = temp_of_hits_player_1[(temp_of_hits_player_1.index(shot))+1]
                    board_to_shots_player1[letters.index(to_change[0])][int(to_change[1])-1] = 'S'
                else:
                    to_change = temp_of_hits_player_1[(temp_of_hits_player_1.index(shot))-1]
                    board_to_shots_player1[letters.index(to_change[0])][int(to_change[1])-1] = 'S'

           
        board_to_shots_player1[zmienna][int(shot[1])-1] = char_shot
        draw_board(board_to_shots_player1,nums,letters)
        if  len(player2_1ship_data[0]) == 0 and len(player2_2ship_data[0]) == 0 and len(player2_3ship_data[0]) == 0:
            print(f'Captain {active_player[0]} you win')
            break
        input()
        up_window()
        if shots_player1 == 0 and shots_player2 == 0:
            print (' End game nobody wins')
            break
        else:
            up_window()
            draw_board(board_to_shots_player2,nums,letters)
            print(f'Captain {active_player[1]} please shot to board player {active_player[0]}')
            if second_player == '1':
                shot = check_char(all_possibles2)
                all_possibles2.remove(shot)
            else: 
                shot = ai(all_shots) 
                all_shots.remove(shot)

            shots_player2 -= 1
            for char in letters:
                if char == shot[0].upper(): 
                    zmienna = int(letters.index(char))
            player1_1ship_data = check_shots(shot,data_first[1][0])
            player1_2ship_data = check_shots(shot,data_first[1][1])
            player1_3ship_data = check_shots(shot,data_first[1][2])
        

        if  player1_1ship_data[1] == 0 and player1_2ship_data[1] == 0 and player1_3ship_data[1] == 0:
            print('Oooops you missed....')
            char_shot = 'M'
        else:
            if player1_1ship_data[2] != '':
                char_shot = player1_1ship_data[2]
            elif player1_2ship_data[2] != '':
                char_shot = player1_2ship_data[2]
            else:
                char_shot = player1_3ship_data[2]
        if char_shot == 'H':    
            temp_of_hits_player_2+= player1_1ship_data[3]
            temp_of_hits_player_2+= player1_2ship_data[3]
            temp_of_hits_player_2+= player1_3ship_data[3]
            

        if char_shot == 'S':
            if shot in temp_of_hits_player_2:
                if temp_of_hits_player_2.index(shot)%2 == 0:
                    to_change = temp_of_hits_player_2[(temp_of_hits_player_2.index(shot))+1]
                    board_to_shots_player2[letters.index(to_change[0])][int(to_change[1])-1] = 'S'
                else:
                    to_change = temp_of_hits_player_2[(temp_of_hits_player_2.index(shot))-1]
                    board_to_shots_player2[letters.index(to_change[0])][int(to_change[1])-1] = 'S'
        board_to_shots_player2[zmienna][int(shot[1])-1] = char_shot
        draw_board(board_to_shots_player2,nums,letters)
        input()
        up_window()
        if  len(player1_1ship_data[0]) == 0 and len(player1_2ship_data[0]) == 0 and len(player1_3ship_data[0]) == 0:
            print(f'Captain {active_player[1]} you win') 
            break  
        
    print('You reached to end of game bravo')



if __name__ == "__main__":
    
    game()
