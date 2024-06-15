from util.util import create_database, create_tables, insert_data_in_tables


db_name = 'course_work'
create_database(db_name)
create_tables(db_name)
insert_data_in_tables(db_name)