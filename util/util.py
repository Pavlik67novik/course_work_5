import psycopg2
from util.config import config
from classes.hh_parser import HHParser

def create_database(db_name):
    """ Создание БД"""
    con = psycopg2.connect(dbname='postgres', **config())
    con.autocommit = True
    cur = con.cursor()
    cur.execute(f'DROP DATABASE IF EXISTS {db_name}')
    cur.execute(f'CREATE DATABASE {db_name}')
    con.close()
    con.close()

def create_tables(db_name):
    """" Создание двух таблиц вакансии и компании """
    con = psycopg2.connect(dbname=db_name, **config())
    with con:
        with con.cursor() as cur:
            cur.execute('CREATE TABLE employers (id INTEGER PRIMARY KEY, name VARCHAR(150))')
            cur.execute('CREATE TABLE vacancies (id INTEGER PRIMARY KEY, name VARCHAR(150),'
                        'link VARCHAR(350), salary_from INTEGER, salary_to INTEGER,'
                        'employer INTEGER REFERENCES employers(id))')
    con.close()



def insert_data_in_tables(db_name):
    """ Заполнение созданных таблиц информацией """
    hh = HHParser()
    employers = hh.get_employers()
    vacancies = hh.get_vacancies()
    con = psycopg2.connect(dbname=db_name, **config())
    with con:
        with con.cursor() as cur:
            for employer in employers:
                cur.execute('INSERT INTO employers VALUES (%s, %s)', (employer['id'], employer['name']))
            for vacancy in vacancies:
                cur.execute('INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s)',
                            (vacancy['id'], vacancy['name'], vacancy['link'], vacancy['salary_from']
                             , vacancy['salary_to'], vacancy['employer']))
    con.close()


def delete_database(db_name: str):
    """
    Удаление базы данных
    :return: None
    """
    conn = psycopg2.connect(dbname='postgres', **config())
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f'DROP DATABASE {db_name}')
    cur.close()
    conn.close()




