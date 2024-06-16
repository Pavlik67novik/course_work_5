from util.util import create_database, create_tables, insert_data_in_tables, delete_database
from classes.db_manager import DBManager

db_name = input('Введите название для Базы Данных\n')
create_database(db_name)
db = DBManager(db_name)
create_tables(db_name)
insert_data_in_tables(db_name)

try:
    while True:
        print("Выберете число от 1 до 5:\n"
              "1. Получить список всех компаний и количество вакансий у каждой компании.\n"
              "2. Получить список всех вакансий с указанием названия компании, названия вакансии, "
              "зарплаты и ссылки на вакансию.\n"
              "3. Получить среднюю зарплату по вакансиям.\n"
              "4. Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n"
              "5. Получить список всех вакансий, в названии которых содержатся переданные "
              "в метод слова, например 'python'.\n")
        number_user = input().strip()
        if number_user == '1':
            print(db.get_companies_and_vacancies_count())
        elif number_user == '2':
            print(db.get_all_vacancies())
        elif number_user == '3':
            print(db.get_avg_salary())
        elif number_user == '4':
            print(db.get_vacancies_with_higher_salary())
        elif number_user == '5':
            word_user = input("Введите слово для поиска вакансий\n")
            print(db.get_vacancies_with_keyword(word_user))
        elif number_user != '1' or '2' or '3' or '4' or '5':
            exit_user = input("Вы ввели не верные данные:\n"
                              "введите 'exit' для выхода, или повторите ввод\n").strip()
            if exit_user == 'exit':
                break
            else:
                continue

        user_question = input("Желаете продолжить: 1-ДА, 2-НЕТ\n").strip()
        if user_question == '1':
            continue
        else:
            break

finally:
    print("Удаление базы данных!\n")
    delete_database(db_name)
    print("Всего Хорошего!")
# print(db.get_all_vacancies())
# print('______________')
# print(db.get_companies_and_vacancies_count())
# print('______________')
# print(db.get_avg_salary())
# print('______________')
# print(db.get_vacancies_with_higher_salary())
# print('______________')
# print(db.get_vacancies_with_keyword('Слесарь'))