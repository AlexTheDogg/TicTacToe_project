print('Приветствую, давайте сыграем в крестики-нолики!')
player1, player2 = input('Игрок 1, введите свое имя: '), input('Игрок 2, введите свое имя: ')
players = {'x': player1, 'o': player2}
curr_plr = 'x'
free_cells = ['левая верхняя', 'средняя верхняя', 'правая верхняя', 'левая средняя',
              'средняя', 'правая средняя', 'левая нижняя', 'средняя нижняя', 'правая нижняя']
all_cells = {'левая верхняя': '-', 'средняя верхняя': '-', 'правая верхняя': '-',
             'левая средняя': '-', 'средняя': '-', 'правая средняя': '-',
             'левая нижняя': '-', 'средняя нижняя': '-', 'правая нижняя': '-'}
print('Чтобы сделать свой ход, необходимо будет скопировать и ввести название одной из свободных клеток, список которых будет приведен ниже.')


def change_player():
    if curr_plr == 'x':
        return 'o'
    return 'x'


def print_the_field():
    print(all_cells['левая верхняя'], all_cells['средняя верхняя'], all_cells['правая верхняя'])
    print(all_cells['левая средняя'], all_cells['средняя'], all_cells['правая средняя'])
    print(all_cells['левая нижняя'], all_cells['средняя нижняя'], all_cells['правая нижняя'])


def is_valid_name_of_ceil(cell):
    if cell in all_cells.keys():
        if all_cells[cell] != '-':
            print('Данная клетка уже занята, введите название другой')
            return False
        return True
    print('Название клетки некорректно')
    return False


def is_win(field, player):
    field = list(field.values())
    for i in range(9):
        if field[i] == player:
            field[i] = 1
        else:
            field[i] = 0
    if field[0] + field[4] + field[8] == 3 or field[2] + field[4] + field[6] == 3:
        return True
    for j in range(3):
        if sum(field[3*j:3*j+3]) == 3 or sum(field[j::3]) == 3:
            return True
    return False


print('Свободные клетки:', *free_cells, sep='\n')
print('Ход игрока', players[curr_plr])
print_the_field()
for _ in range(9):
    cell = input(f'''{players[curr_plr]}, введите название клетки, которую хотите заполнить: ''')
    while not is_valid_name_of_ceil(cell):
        cell = input(f'''{players[curr_plr]}, введите название клетки, которую хотите заполнить: ''')
    all_cells[cell] = curr_plr
    free_cells.remove(cell)
    if is_win(all_cells, curr_plr):
        print_the_field()
        print(f'Игрок {players[curr_plr]} победил. Игра окончена')
        break
    curr_plr = change_player()
    print('Свободные клетки:', *free_cells, sep='\n')
    print('Ход игрока', players[curr_plr])
    print_the_field()
else:
    print('Ничья')
