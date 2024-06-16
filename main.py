from util.util import create_database, create_tables, insert_data_in_tables
from classes.db_manager import DBManager

db_name = 'course_work'
create_database(db_name)
create_tables(db_name)
insert_data_in_tables(db_name)


db = DBManager(db_name)
print(db.get_all_vacancies())
print('______________')
print(db.get_companies_and_vacancies_count())
print('______________')
print(db.get_avg_salary())
print('______________')
print(db.get_vacancies_with_higher_salary())
print('______________')
print(db.get_vacancies_with_keyword('Слесарь'))