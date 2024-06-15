import psycopg2

from util.config import config


class DBManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = psycopg2.connect(dbname=self.db_name, **config())

    def get_companies_and_vacancies_count(self):
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT employer.name, COUNT(vacancies.name) AS vacancies_count '
                               'FROM employer LEFT JOIN vacancies ON employer.employer_id = vacancies.company_id '
                               'GROUP BY employer.employer_name')
                resulting = cursor.fetchall()
                self.conn.commit()
                print(resulting)

    # def get_companies_and_vacancies_count(self):
    #     query = 'SELECT name, COUNT(*) FROM employers ' \
    #             'GROUP BY name'
    #
    #     return self.__execute_query(query)

    def get_all_vacancies(self):
        query = 'SELECT vacancies.name, employers.name, vacancies.link, vacancies.salary_from,'\
                 'vacancies.salary_to FROM vacancies '\
                 'JOIN employers ON vacancies.employer = employers.id'

        return self.__execute_query(query)


    def get_avg_salary(self):
        #получаем среднюю ЗП по вакансиям
        query = 'SELECT AVG(salary_from) FROM vacancies '
        return self.__execute_query(query)


    def get_vacancies_with_higher_salary(self):
        #получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT vacancy_name, salary_from, url FROM vacancies "
                           "WHERE salary_from > (select AVG(salary_from) "
                           "FROM vacancies)")
            resulting = cursor.fetchall()
            self.conn.commit()
            print(resulting)

        query = 'SELECT * FROM vacancies WHERE salary_from > AVG(salary_from)'

        return self.__execute_query(query)


    def get_vacancies_with_keyword(self, keyword):
        # получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python
        query = 'SELECT * FROM vacancies WHERE vacancy_title LIKE %s;', ('%' + keyword + '%')
        return self.__execute_query(query)





