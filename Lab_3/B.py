import sys

total_dist_mouse = 0
total_dist_cat = 0
winner = 'Mouse evaded Cat'

def main():
    global total_dist_mouse, total_dist_cat, winner
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        print('Not enough arguments')
        return 1

    with open(file_name, 'r', encoding='utf-8') as f:
        # записываем количество строк и столбцов
        ROWS, COLUMNS = map(int, f.readline().split())
        # создаем массив массивов с действиями, считываемыми из файла
        MOVES = [line.split() for line in f]

    print('Cat and Mouse')
    print(f'{"Cat":^15}{"Mouse":^15}{"Distance":^15}')
    print('-' * 45)

    cat_pos = [1, 1]
    mouse_pos = [1, 1]
    for m in MOVES:
        if (m[0] == 'P'):
            print_positions(cat_pos, mouse_pos)
        elif (m[0] == 'C'):
            total_dist_cat += abs(int(m[1]) - cat_pos[0]) + abs(int(m[2]) - cat_pos[1])
            make_move(cat_pos, ROWS, COLUMNS, int(m[1]), int(m[2]))
        elif (m[0] == 'M'):
            total_dist_mouse += abs(int(m[1]) - mouse_pos[0]) + abs(int(m[2]) - mouse_pos[1])
            make_move(mouse_pos, ROWS, COLUMNS, int(m[1]), int(m[2]))
        if cat_pos == mouse_pos:
            print_positions(cat_pos, mouse_pos)
            winner = 'Cat caught Mouse'
            return;
            

def print_positions(cat_pos, mouse_pos):
    cat = ['?', '?'] if cat_pos == [1, 1] else cat_pos
    mouse = ['?', '?'] if mouse_pos == [1, 1] else mouse_pos
    distance = ''
    if cat != ['?', '?'] and mouse != ['?', '?']:
        distance = abs(cat_pos[0] - mouse_pos[0]) + abs(cat_pos[1] - mouse_pos[1])

    print(f'({cat[0]:>3},{cat[1]:>3})        ({mouse[0]:>3},{mouse[1]:>3})         {distance:<15}')


def make_move(pos, rows, clms, add_rows, add_clms):
    pos[0] = (pos[0] + add_rows - 1) % rows + 1
    pos[1] = (pos[1] + add_clms - 1) % clms + 1

main()

print('-' * 45)
print(f'{"Distance":<15}{"Mouse":>15}{"Cat":>15}')
print(f'{total_dist_mouse:>30}{total_dist_cat:>15}')
print(winner)