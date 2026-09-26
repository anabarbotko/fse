import sys

def main():
    if len(sys.argv) == 2:
            file_name = sys.argv[1]
    else:
        print('Not enough arguments')
        return 1

    # открываем файл, пропускаем первые 2 строки и записываем данные построчно в массив
    with open(file_name, 'r', encoding='utf-8') as f:
        f.readline()
        f.readline()
        data = f.readlines()

    # формула для расчета WC temp: 35.74 + 0.6125 * T + (0.4275 * T - 35.75) * V ^ 0.16
    # T - температура по Фаренгейту, V - скорость ветра
    # формула для расчета WC effect: WC temp - T

    with open(file_name[0] + '.WindChillReport.txt', 'w', encoding='utf-8') as f:
        # записываем в новый файл первые 2 строки
        f.write("Time          WC temp            WC Effect\n")
        f.write('-' * 200 +'\n')
        wc_temp_sum = 0
        count = 0
        for d in data:
            # каждую строку разбиваем на значения, вычисляем по формуле и записываем в новый файл
            time, temp, speed = d.split()
            temp = int(temp)
            speed = int(speed)
            wc_temp = 35.74 + 0.6125 * temp + (0.4275 * temp - 35.75) * speed ** 0.16
            wc_effect = wc_temp - temp
            f.write(f'{time:14}{wc_temp:<19.1f}{wc_effect:.1f}\n')
            wc_temp_sum += wc_temp
            count += 1
        f.write('-' * 200 +'\n')
        f.write(f'The average adjusted temperature, based on {count} observations, was {wc_temp_sum/count:.1f}\n')

main()