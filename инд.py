#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
   base = []
   while True:
      command = input(">>> ").lower()
      if command == 'exit':
        break
      elif command == 'add':
          name = input("Фамилия, Имя? ")
          number = input("Номер телефона? ")
          print("Дата рождения:")
          day =input("День")
          month = input("Месяц")
          year = input("Год")
          bases = {
            'name': name,
            'number': number,
            'day': day,
            'month': month,
            'year': year
          }
          base.append(bases)
          if len(base) > 1:
             base.sort(key=lambda item: item.get('name', ''))
      elif command == 'list':
          line = '+-{}-+-{}-+-{}-+-{}-+'.format(
               '-' * 4,
               '-' * 30,
               '-' * 20,
               '-' * 8
          )
          print(line)
          print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                 "№",
                 "Ф.И.",
                 "Номер телефона",
                 "Дата рождения"
            )
          )
          print(line)
          for idx, bases in enumerate(base, 1):
            print(
               '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                  idx,
                  bases.get('name', ''),
                  bases.get('number', ''),
                  bases.get('month', 0)
               )
            )
          print(line)
      elif command.startswith('select '):
         parts = command.split(' ', maxsplit=2)
         sel = (parts[1])
         count = 0
         for bases in base:
            if bases.get('month') == sel:
              count += 1
              print(
                 '{:>4}: {}'.format(count, bases.get('name', ''))
              )
         if count == 0:
          print("В этом месяце ни у кого нет дня рождения.")
      elif command == 'help':
         print("Список команд:\n")
         print("add - добавить работника;")
         print("list - вывести список работников;")
         print("select <месяц> - запросить людей, у которых в этом месяце день рождения;")
         print("help - отобразить справку;")
         print("exit - завершить работу с программой.")
      else:
         print(f"Неизвестная команда {command}", file=sys.stderr)