import sys

def main():
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        print('Not enough arguments')
        return 1

    month_to_day_count = {'January': 31, 'February' : 28, 'March' : 31, 'April' : 30, 
                          'May' : 31, 'June' : 30, 'July' : 31, 'August' : 31,
                          'September' : 30, 'October' : 31, 'November' : 30, 'December' : 31}

    day_to_amount = {}
    incorrect_data = {}

    with open(file_name, 'r', encoding='utf-8') as f:
        # считываем место, месяц и год
        f.readline()
        place = f.readline().strip()
        month, year = f.readline().split(', ')
        year = int(year)

        # добавляем 1 день февралю, если год високосный
        if  year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            month_to_day_count['February'] = 29

        # считываем корректные и некорректные наборы данных
        line_index = 3
        for line in f:
            line_index += 1
            day_str, amount_str = line.split()
            day = int(day_str)
            amount = float(amount_str)
            if day in day_to_amount:
                incorrect_data[line_index] = [day, 'Repeated']
                pass
            if day < 1 or day > month_to_day_count[month]:
                incorrect_data[line_index] = [day, 'Invalid']
                pass
            day_to_amount[day] = amount

    with open('Report.txt', 'w', encoding='utf-8') as f:
        # выводим шапку
        f.write('Programmer: Yana Barbotka\n\n')
        f.write('Precipitation report for ' + place + ' during ' + str(month) + ', ' + str(year) + '\n\n')

        # выводим ошибки
        f.write(f'{"Error":20}{"Day":>20}{"Line":>20}\n')
        for line, data in incorrect_data.items():
            f.write(f'{data[1]:20}{data[0]:>20}{line:>20}\n')
        f.write('\n')

        # выводим таблицу с данными
        f.write(f'{"Day":>3}{"Amount":>10}{"Graph":>7}\n')
        for i in range(1, month_to_day_count[month] + 1):
            if i in day_to_amount:
                graph = '*' * ((int(day_to_amount[i] * 100) + 24) // 25)
                f.write(f'{i:>3}{day_to_amount[i]:>10}  {graph}\n')
            else:
                f.write(f'{i:>3}{"NA":>10}\n')
        f.write('\n')

        # выводим min, max и average
        f.write(f'{"Minimum"}{"Maximum":>12}{"Average":>12}\n')
        amounts = day_to_amount.values()
        f.write(f'{min(amounts):>7}{max(amounts):>12}{sum(amounts)/month_to_day_count[month]:>12.2f}')
        

main()