import sys

def main():
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        print('Not enough arguments')
        return 1

    with open(file_name, 'r', encoding='utf-8') as f:
        first_line = f.readline()
        distances = f.readlines()

    places, scale = first_line.split()
    print('Yana Barbotka')
    print('Simple Map Distance Computations')
    print('Map Scale Factor: ', scale, ' miles per inch')
    print(' ' * 7, 'Map', ' ' * 5, 'Mileage')
    print(' ' * 7, 'Measure', ' ' * 1, 'Distance')
    print('=' * 100)

    count = 1
    total_miles = 0
    for distance in distances:
        real_distance = float(distance) * float(scale)
        print(f'#  {count}{' ' * 4}{distance.strip()}{' ' * 7}{real_distance:.1f}')
        total_miles += real_distance
        count += 1
    print('=' * 100)
    print(f'Total Distance:   {total_miles:.1f}')

main()