#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys

# Использовать словарь, содержащий следующие ключи: название пункта назначения; номер
# поезда; время отправления. Написать программу, выполняющую следующие действия: ввод
# с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть упорядочены по номерам поездов; вывод на экран информации о поезде, номер
# которого введен с клавиатуры; если таких поездов нет, выдать на дисплей соответствующее
# сообщение.

if __name__ == '__main__':
    trains = []

    while True:
        command = input(">>> ")

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Пункт назначения ")
            number = input("Номер поезда ")
            time = input("Время отправления ")

            train = {
                'name': name,
                'number': number,
                'time': time,
            }
            trains.append(train)
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get('number', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 25,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^25} | {:^20} | {:^20} |'.format(
                    "№",
                    "Пункт назначения",
                    "Номер поезда",
                    "Время отправления"
                )
            )
            print(line)

            for idx, train in enumerate(trains, 1):
                print(
                    '| {:>4} | {:<25} | {:<20} | {:>20} |'.format(
                        idx,
                        train.get('name', ''),
                        train.get('number', 0),
                        train.get('time', 0)
                    )
                )

            print(line)

        elif command.startswith('select '):

            parts = command.split(' ', maxsplit=1)
            period = parts[1]
            count = 0

            for train in trains:
                if period == train.get('number'):
                    count += 1
                    print(
                        '{:>4}: Пункт назначения - {}, время отправления - {}'.format(count, train.get('name', ''),
                                                                                      train.get('time', '')
                                                                                      )
                    )
            if count == 0:
                print("Поездов с таким номером  не найдено.")

        elif command.startswith('load '):
            parts = command.split(' ', maxsplit=1)
            with open(parts[1], 'r') as f:
                trains = json.load(f)

        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)
            with open(parts[1], 'w') as f:
                json.dump(trains, f)

        elif command == 'help':
            print("Список команд:\n")
            print("add - Добавить данные;")
            print("list - Вывести данные;")
            print("select <номер> - Вывести всю информацию по поезду с введенным номером;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
