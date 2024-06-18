import psycopg2
from util.config import config


class DBManager:
    """ Класс для соед с БД, и получение информации с выполнением необходимых запросов"""
    def __init__(self, db_name):
        self.__db_name = db_name


    def __execute_quary(self, query):
        """ Устанавливаем соед. с БД, через модуль psycopg2 и сохраняем результат в result"""
        con = psycopg2.connect(dbname=self.__db_name, **config())
        with con:
            with con.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
        con.close()
        return result


    def get_companies_and_vacancies_count(self):
        """ получает список всех компаний и количество вакансий у каждой компании. """
        query = 'SELECT name, COUNT(*) FROM employers GROUP BY name'
        return self.__execute_quary(query)


    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.
        """
        query = 'SELECT * FROM vacancies JOIN employers ON vacancies.employer = employers.id'
        return self.__execute_quary(query)


    def get_avg_salary(self):
        """ получаем среднюю ЗП по вакансиям """
        query = 'SELECT AVG(salary_from) AS payment_avg FROM vacancies'
        return self.__execute_quary(query)


    def get_vacancies_with_higher_salary(self):
        """ получает список всех вакансий, у которых ЗП выше средней по всем вакансиям """
        query = ('SELECT name, salary_from, link FROM vacancies WHERE salary_from > (SELECT AVG(salary_from) '
                 ' FROM vacancies)')
        return self.__execute_quary(query)


    def get_vacancies_with_keyword(self, word_user):
        """ получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python"""
        query = f"SELECT * FROM vacancies WHERE name LIKE '%{word_user}%'"
        return self.__execute_quary(query)




