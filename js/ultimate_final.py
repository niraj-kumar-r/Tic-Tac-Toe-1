import random
import pickle
from sys import exit
from time import sleep


def searchname(name, c=0):
    '''searches for a name based on username'''

    with open('user.dat', 'rb') as f:

        flag = False
        index = -1

        while True:
            try:
                rec = pickle.load(f)
                index += 1

                if rec['name'] == name:
                    flag == True

                    if c == 0:
                        return rec
                        # if c is 0 it just returns record
                    else:
                        return rec, index
                        # if c is not 0 it returns
                        # both, record and its index in reclst

            except EOFError:
                break

        if flag == False:
            if c == 0:
                return None
            else:
                return None, None


def makename():
    '''makes a new name'''

    print('\t\tTIC TAC TOE')

    name = input('enter username\n(must be less than 23 characters)\n')

    if len(name) > 23:
        print('\nEntered username is longer than 23 characters')
        print('Please try again\n')
        sleep(1.5)
        makename()

    pwd = input('\nenter password')

    for i in range(50):
        print()
        # brings the screen futher down
        # so that password is not revealed to a bystander

    check = searchname(name)
    # searches for that name

    if check == None:
        rec = {'name': name, 'pwd': pwd, 'win': 0,
               'loss': 0, 'tie': 0, 'point': 0}

        f = open('user.dat', 'ab')
        pickle.dump(rec, f)
        f.close()

        print('Profile successfully created')
        sleep(2)
        main_menu()

    else:
        print('A profile with that username already exists')
        print("Please try another username")
        sleep(2)
        profile_menu()


# updates name after a match
# wtl stands for win tie loss
# wtl holds valuse 1,0,-1 respectively
def nameupdate(name, wtl):

    reclst = give_reclst()
    rec, i = searchname(name, 1)

    if wtl == 1:
        reclst[i]['win'] += 1
        reclst[i]['point'] += 5
        # 5 points awarded for each win

    elif wtl == -1:
        reclst[i]['loss'] += 1
        reclst[i]['point'] -= 5
        # 5 points deducted for each loss
    else:
        reclst[i]['tie'] += 1
        reclst[i]['point'] += 0.1
        # 1 point is awarded for 10 ties
        # so 0.1 points awarded for each tie

    with open('user.dat', 'wb') as f:
        for x in reclst:
            pickle.dump(x, f)


def give_reclst(i=0):
    '''gives a list of all profiles'''

    with open('user.dat', 'rb') as f:
        reclst = []
        while True:
            try:
                rec = pickle.load(f)
                reclst.append(rec)
            except EOFError:
                break

        return reclst


def changepwd():
    '''changes password'''

    print('\t\tTIC TAC TOE')
    name = input('enter username')

    rec, index = searchname(name, 1)
    reclst = give_reclst()

    if rec == None:
        print('You entered the wrong username')
        sleep(2)
        profile_menu()

    else:
        pwd = input('enter original password')
        for i in range(50):
            print()

        if rec['pwd'] != pwd:
            print('You entered the wrong password')
            sleep(2)
            profile_menu()

        else:
            new_pwd = input('enter new password')
            reclst[index]['pwd'] = new_pwd
            for i in range(50):
                print()

            with open('user.dat', 'wb') as f:
                for x in reclst:
                    pickle.dump(x, f)

            print('Password successfully changed')
            sleep(2)
            main_menu()


# sorts according to points by default
# if p specified, sorts wrt p
# order=1 means ascending and 2 means descending
def leaderboard(p='point', order=2):
    print('\n\t\t\tTIC TAC TOE')

    reclst = give_reclst()
    l = len(reclst)

    # bubble sorting reclst based on p
    for i in range(0, l):

        for j in range(0, l-1-i):

            if order == 1:
                # order 1 means ascending
                if reclst[j][p] > reclst[j+1][p]:

                    reclst[j], reclst[j+1] = reclst[j+1], reclst[j]

            else:
                # if order 2 then descending
                if reclst[j][p] < reclst[j+1][p]:

                    reclst[j], reclst[j+1] = reclst[j+1], reclst[j]

    # \t is used for tab space
    print()
    print('*'*60)
    print('   Name\t\t\t\tpoints\twins\tlosses\tties')
    print('*'*60)
    print()
    i = 1

    for x in reclst:

        char_name = x['name']+(' '*(23-len(x['name'])))
        # so that all names will
        # have a fixed length of 23

        print(i, ') ', char_name, '\t', int(x['point']), end='', sep='')

        print('\t', x['win'], '\t', x['loss'], end='', sep='')

        print('\t', x['tie'], sep='')
        i += 1

    print()
    print()

    print('1) Main menu')
    print('2) Sorting options')
    h = ask(1, 2)
    if h == 1:
        main_menu()
    else:
        sorting_option()


# other options to sort leader boards
def sorting_option():

    print('1) Sort alphabetically')
    print('2) Sort by points')
    print('3) Sort by wins')
    print('4) Sort by losses')
    print('5) Sort by ties')

    h = ask(1, 5)

    print()
    print('1) Ascending')
    print('2) Descending')
    g = ask(1, 2)

    if h == 1:
        leaderboard('name', g)
    elif h == 2:
        leaderboard('point', g)
    elif h == 3:
        leaderboard('win', g)
    elif h == 4:
        leaderboard('loss', g)
    elif h == 5:
        leaderboard('tie', g)


def delete_name():
    '''deletes a profile'''

    print('\t\tTIC TAC TOE')

    name = input('enter username')

    rec, index = searchname(name, 1)
    reclst = give_reclst()

    if rec == None:
        print('You entered the wrong username')
        sleep(2)
        profile_menu()

    else:
        pwd = input('enter your password')
        for i in range(50):
            print()

        if rec['pwd'] != pwd:
            print('You entered the wrong password')
            sleep(2)
            profile_menu()

        else:
            with open('user.dat', 'wb') as f:
                for x in reclst:
                    if x['name'] == name:
                        continue
                    pickle.dump(x, f)

            print('Profile successfully deleted')
            sleep(2)
            main_menu()


def display(z):
    '''displays the square grid of any size
            z is any grid in form of list of lists'''
    print()
    print()
    l = len(z)

    for i in range(l+1):
        if i == 0:
            print('  ', end=' ')
        else:
            print(i, end='   ')

    print()
    print()

    for i in range(l):
        print(i+1, end='  ')

        for j in range(l):
            print(z[i][j], end='   ')
        print()
    print()
    print()


def ask(s, e, w='no.'):
    '''asks the user for a no.
    returns that no. if it is an integer
    between s and e (both included)'''
    try:
        print()
        print('enter', w)
        k = int(input())
        if k in range(s, e+1):
            return k
        else:
            print('invalid number, try again')
            k = ask(s, e, w)
            return k
    except:
        print('invalid number, try again')
        k = ask(s, e, w)
        return k


def win_check(z, side=3):
    '''win_check condition, generalised
    the side is the grid size(eg 3,4,etc.)
    It sums up all the elements, along rows
    columns, and both diagonals,and adds them to list w'''
    w = []
    dia_1 = 0
    dia_2 = 0

    for i in range(side):

        row_sum = 0
        col_sum = 0

        for j in range(side):

            row_element = z[i][j]
            row_sum += row_element

            col_element = z[j][i]
            col_sum += col_element

        dia_1 += z[i][i]
        dia_2 += z[i][side-i-1]

        w.append(row_sum)
        w.append(col_sum)

    w.append(dia_1)
    w.append(dia_2)

    # Note that in w the order of sum(for side=3) is
    # row1,col1,row2,col2,row3,col3,dia1,dia2

    # also note, if grid size is 4
    # the matching condition, is also
    # assumed to be 4, for size 5, matching is also 5

    if side in w:
        return 1  # if 3 ones found O wins, returns 1
    elif -side in w:
        return -1  # if 3 -ve ones found X wins, returns -1
    else:
        return 0  # if nobody is winning returns 0


def update(t, matrix, zmatrix, p_avail, side=3):
    '''if t is 1, O turn, if t=-1, X turn'''

    a = ask(1, side, 'row')
    b = ask(1, side, 'column')

    if (a*10)+b in p_avail:
        if t == 1:
            k = 'O'
        elif t == -1:
            k = 'X'
        matrix[a-1][b-1] = k
        zmatrix[a-1][b-1] = t
        p_avail.remove((a*10)+b)
        return matrix

    else:
        print('place is already filled, try another one')
        u = update(t, matrix, zmatrix, p_avail, side)
        return u


def comp_algo(t, zmat, places_available, side=3):

    print('( -__-)', end='', flush=True)  # delay to animate
    display_str = '....'  # thinking

    for i in range(len(display_str)):
        print(display_str[i], end='', flush=True)
        sleep(0.9)

    for ab in places_available:

        zmat[int(ab/10)-1][(ab % 10)-1] = t
        j = win_check(zmat, side)
        zmat[int(ab/10)-1][(ab % 10)-1] = 0
        if t == j:
            return(int(ab/10), (ab % 10))

    for ab in places_available:
        zmat[int(ab/10)-1][(ab % 10)-1] = -t
        j = win_check(zmat, side)
        zmat[int(ab/10)-1][(ab % 10)-1] = 0
        if j == -t:
            return(int(ab/10), (ab % 10))

    if 22 in places_available:
        return(2, 2)
    else:
        ab = random.choice(places_available)
        return(int(ab/10), (ab % 10))


def gr3by3_2p(rank=0, user1='O', user2='X'):

    mat = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    zmat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    p_avail = [11, 12, 13, 21, 22, 23, 31, 32, 33]

    print('\t\tTIC TAC TOE')
    display(mat)

    for i in range(0, 9):

        if i % 2 == 0:
            j = 1
            print(user1, 'turn')
        else:
            j = -1
            print(user2, 'turn')
        mat = update(j, mat, zmat, p_avail)

        print('\t\tTIC TAC TOE')
        display(mat)

        p = win_check(zmat)
        if p == 1:
            print(user1, 'wins')
            print('o:-)')
            if rank != 0:
                nameupdate(user1, 1)
                nameupdate(user2, -1)
                # in nameupdate 1 is win
                #0 is tie and -1 is loss
            break

        elif p == -1:
            print(user2, 'wins')
            print(':-P')
            if rank != 0:
                nameupdate(user1, -1)
                nameupdate(user2, 1)
                # in nameupdate 1 is win
                #0 is tie and -1 is loss
            break
        else:
            pass
    else:
        print('tie')
        if rank != 0:
            nameupdate(user1, 0)
            nameupdate(user2, 0)
            # in nameupdate 1 is win
            #0 is tie and -1 is loss

    print()
    print()
    print('1) Play again')
    print('2) Main menu')
    e = ask(1, 2)
    if e == 1:
        gr3by3_2p(rank, user1, user2)
    elif e == 2:
        main_menu()


def gr3by3_comp(rank=0, user1='O', user2='X'):

    mat = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    zmat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    p_avail = [11, 12, 13, 21, 22, 23, 31, 32, 33]

    print('\t\tTIC TAC TOE')
    display(mat)

    for i in range(0, 9):
        if i % 2 == 0:
            j = 1
            f = 'O'
            print(user1, 'turn')
            mat = update(j, mat, zmat, p_avail)

            print('\t\tTIC TAC TOE')
        else:
            j = -1
            f = 'X'
            print(user2, 'turn')
            a, b = comp_algo(j, zmat, p_avail)
            mat[a-1][b-1] = f
            zmat[a-1][b-1] = j
            p_avail.remove((a*10)+b)

            print('comp chooses, row ', a)
            print('comp chooses, column ', b)
            print('\n\t\tTIC TAC TOE')

        display(mat)

        p = win_check(zmat)
        if p == 1:
            print('you win')
            print('I will be back for revenge, (*_*)')
            if rank != 0:
                nameupdate(user1, 1)
            break
        elif p == -1:
            print('comp wins')
            print('you are a loser, :-P')
            if rank != 0:
                nameupdate(user1, -1)
            break
        else:
            pass
    else:
        print('tie')
        print('lets play once more, (>.<)')
        if rank != 0:
            nameupdate(user1, 0)

    print()
    print()
    print('1) Play again')
    print('2) Main menu')
    e = ask(1, 2)
    if e == 1:
        gr3by3_comp(rank, user1, user2)
    elif e == 2:
        main_menu()


def gr4by4_2p(rank=0, user1='O', user2='X'):

    mat = [['-', '-', '-', '-'], ['-', '-', '-', '-'],
           ['-', '-', '-', '-'], ['-', '-', '-', '-']]
    zmat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    p_avail = [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44]

    print('\t\tTIC TAC TOE')
    display(mat)

    for i in range(0, 16):
        if i % 2 == 0:
            j = 1
            print(user1, 'turn')
        else:
            j = -1
            print(user2, 'turn')
        mat = update(j, mat, zmat, p_avail, 4)

        print('\t\tTIC TAC TOE')

        display(mat)

        p = win_check(zmat, side=4)
        if p == 1:
            print(user1, 'wins')
            print(':-P')
            if rank != 0:
                nameupdate(user1, 1)
                nameupdate(user2, -1)
            break

        elif p == -1:
            print(user2, 'wins')
            print('o:-)')
            if rank != 0:
                nameupdate(user1, -1)
                nameupdate(user2, 1)
            break
        else:
            pass
    else:
        print('tie')
        print('(+_+)')
        if rank != 0:
            nameupdate(user1, 0)
            nameupdate(user2, 0)

    print()
    print()
    print('1) Play again')
    print('2) Main menu')
    e = ask(1, 2)
    if e == 1:
        gr4by4_2p(rank, user1, user2)
    elif e == 2:
        main_menu()


def gr4by4_comp(rank=0, user1='O', user2='X'):

    mat = [['-', '-', '-', '-'], ['-', '-', '-', '-'],
           ['-', '-', '-', '-'], ['-', '-', '-', '-']]
    zmat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    p_avail = [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44]

    print('\t\tTIC TAC TOE')
    display(mat)

    for i in range(0, 16):
        if i % 2 == 0:
            j = 1
            f = 'O'
            print(user1, 'turn')
            mat = update(j, mat, zmat, p_avail, 4)

            print('\t\tTIC TAC TOE')
        else:
            j = -1
            f = 'X'
            print('x turn')
            a, b = comp_algo(j, zmat, p_avail, 4)
            mat[a-1][b-1] = f
            zmat[a-1][b-1] = j
            p_avail.remove((a*10)+b)

            print('comp chooses, row ', a)
            print('comp chooses, column ', b)
            print('\n\t\tTIC TAC TOE')

        display(mat)

        p = win_check(zmat, side=4)
        if p == 1:
            print('you win')
            print('I will be back for revenge, o:-)')
            if rank != 0:
                nameupdate(user1, 1)
            break
        elif p == -1:
            print('comp wins')
            print('you are a loser,(*_*)')
            if rank != 0:
                nameupdate(user1, -1)
            break
        else:
            pass
    else:
        print('tie')
        print('lets play once more,(>.<)')
        if rank != 0:
            nameupdate(user1, 0)

    print()
    print()
    print('1) Play again')
    print('2) Main menu')
    e = ask(1, 2)
    if e == 1:
        gr4by4_comp(rank, user1, user2)
    elif e == 2:
        main_menu()


# rank =0 means quick game
# rank=1 or anything else means ranked game
def quick_game(rank=0):

    print('\t\tTIC TAC TOE')

    print()
    print()
    print('1) 3*3 grid')
    print('2) 4*4 grid')
    print()
    print('3) Main menu')
    y = ask(1, 3)
    if y == 1:
        gr3by3(rank)
    elif y == 2:
        gr4by4(rank)
    elif y == 3:
        main_menu()


def gr3by3(rank=0):
    '''the 3*3 grid menu options'''
    print('\t\tTIC TAC TOE')

    print()
    print()
    print('1) Player vs Computer')
    print('2) Player vs Player')
    print()
    print('3) Main menu')
    x = ask(1, 3)

    user1 = 'O'
    user2 = 'X'

    if rank != 0 and x != 3:
        user1, user2 = get_ranked_user(x)
        # if x=1 returns one name and comp
        # if x=2 returns two names

        # gets ranked user name for ranked game
        # if rank is not 0

    if x == 1:
        gr3by3_comp(rank, user1, user2)
    elif x == 2:
        gr3by3_2p(rank, user1, user2)
    elif x == 3:
        main_menu()


def gr4by4(rank=0):
    '''the 4*4 grid menu options'''
    print('\t\tTIC TAC TOE')

    print()
    print()
    print('1) Player vs Computer')
    print('2) Player vs Player')
    print()
    print('3) Main menu')
    x = ask(1, 3)

    user1 = 'O'
    user2 = 'X'

    if rank != 0 and x != 3:
        user1, user2 = get_ranked_user(x)
        # if x=1 returns one name and comp
        # if x=2 returns two names

        # gets ranked user name for ranked game
        # if rank is not 0

    if x == 1:
        gr4by4_comp(rank, user1, user2)
    elif x == 2:
        gr4by4_2p(rank, user1, user2)
    elif x == 3:
        main_menu()


def get_ranked_user(n):

    mlist = []

    while True:
        print('\t\tTIC TAC TOE')
        user = input('Enter username ')
        pwd = input('Enter password')

        for i in range(50):
            print()

        rec = searchname(user)

        if rec == None:
            print('Invalid input')
            print('You will be redirected to main menu')
            sleep(2)
            main_menu()

        elif user == rec['name'] and pwd == rec['pwd']:
            mlist.append(user)

        else:
            print('Invalid input')
            print('You will be redirected to main menu')
            sleep(2)
            main_menu()

        if n == 1:
            mlist.append('comp')
            break
        else:
            n = 1

    return mlist[0], mlist[1]


def profile_menu():
    '''it is the profile menu'''
    print('\n\t\tTIC TAC TOE\n')
    print('1) Make a new profile')
    print('2) Change password of an existing profile')
    print('3) Delete an existing profile')
    print('4) Main menu')
    h = ask(1, 4)
    if h == 1:
        makename()
    elif h == 2:
        changepwd()
    elif h == 3:
        delete_name()
    elif h == 4:
        main_menu()


def help():
    print('\n\t\tTIC TAC TOE\n')
    with open('help.txt', 'r') as f:
        j = f.read()
        print(j)

    g = input('Enter anything to go to main menu')
    main_menu()


def main_menu():
    print('\n\t\tTIC TAC TOE')
    print()
    print('1) Quick game')
    print('2) Ranked game')
    print('3) Profile')
    print('4) Leaderboards')
    print('5) Help')
    print('6) Quit')
    h = ask(1, 6)
    if h == 1:
        quick_game()
    elif h == 2:
        quick_game(1)
    elif h == 3:
        profile_menu()
    elif h == 4:
        leaderboard()
    elif h == 5:
        help()
    elif h == 6:
        print('Game Over')
        exit(0)
        # imported from sys module at start
        # ends the program explicitly


f = open('user.dat', 'ab')
f.close()
main_menu()
