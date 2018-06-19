# #Q1
import pymysql as p
#
# try:
#     con = p.connect(host='localhost', database='', user='')

#     cursor = con.cursor()
#
#     query1 = 'create table books(bookID int(5) primary key, location varchar(20) , genre varchar(10),titleID int(5),foreign key(titleID) references titles(titleID));'
#     query2 = 'create table titles(titleID int(5) primary key,title varchar(20),ISBN int(5),publication_year int(4), publisherID int(5), foreign key(publisherID) references publishers(publisherID) );'
#     query3 = 'create table publishers(publisherID int(5) primary key, name varchar(20), street_address varchar(20), suite_number int(5), ZipCodeID int(5),foreign key(ZipCodeID) references zipcodes(ZipCodeID))'
#     query4 = 'create table zipcodes(ZipCodeID int(5) primary key, city varchar(20), state varchar(30), zip_code int(5))'
#     query5 = 'create table author_titles(AuthorTitleID int(5) primary key, authorID int(5),foreign key(authorID) references authors(authorID),titleID int(5), foreign key(titleID) references titles(titleID));'
#     query6 = 'create table authors(authorID int(5) primary key, first_name varchar(20), middle_name varchar(20), last_name varchar(20))'
#     cursor.execute(query6)
#     cursor.execute(query4)
#     cursor.execute(query3)
#     cursor.execute(query2)
#     cursor.execute(query1)
#     cursor.execute(query5)
#     print('Table created successfully!!')
#
# except p.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('Problem occured: ', e)
#
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
#     print('Done!!')
#
# #Q2
# try:
#     con = p.connect(host='localhost', database='', user='')
#
#     cursor = con.cursor()
#
#     query = "insert into authors(authorID,first_name,middle_name,last_name) \
#     values(%s, %s, %s, %s)"
#
#     records = [(3321,'Amish','-','tripathi')]
#     query1="insert into authors(authorID,first_name,middle_name,last_name) \
#     values(%s, %s, %s, %s)"
#     #cursor.executemany(query, records)
#
#     con.commit()
#
# except p.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('Problem occured: ', e)
#
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
#     print('Done!!')

#Q3
# try:
#     con = p.connect(host='localhost', database='', user='')
#
#     cursor = con.cursor()
#
#     query = 'select * from authors'
#
#     cursor.execute(query)
#
#     data = cursor.fetchall()
#
#     for row in data:
#         print('AuthorID: {}, First Name: {}, Middle Name: {}, Last Name: {}' \
#               .format(row[0], row[1], row[2], row[3]))
#
# except p.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('Problem occured: ', e)
#
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
#     print('Done!!')