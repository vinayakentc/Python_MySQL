import mysql.connector as connector
import logging
LOG_FORMAT = "%(asctime)s\\%(levelname)s\\%(message)s"

logging.basicConfig(filename='practice.log', level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger()


class DBHelper:
    def __init__(self):

        """This function is used to connect and create  python programme to database """
        try:
            self.con = connector.connect(host='localhost', port='3306',user='root',password='Ganesh@298',database='pythontest')
            query = 'create table if not exits user(userId int primary key,userName varchar(200),phone varchar(12))'
            cur = self.con.cursor()
            cur.execute(query)
            logger.info("created")
        except Exception as e:
            logger.error('Failed to connect database', e)

    # Insert Operation
    def insert_user(self, userid, username, phone):
        """This fuction used to insert data into database"""
        try:
            query = "insert into user(userId,userName,phone)values({},'{}','{}')".format(userid, username, phone)
            print(query)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            logger.info("user saved to db")
        except Exception as e:
            logger.error("Error occured at data insertion ", e)

    # Fetch all
    def Fetch_all(self):
        """This fuction used to Fetch data from database"""

        try:
            query = "select * from user"
            cur = self.con.cursor()
            cur.execute(query)
            for row in cur:
                print("User Id : ", row[0])
                print("User Name : ", row[1])
                print("User Phone : ", row[2])
                print()
        except Exception as e:
            logger.error("Error occured at data selection..", e)

    def delete_user(self, userId):
        """This fuction used to delete data from database"""

        try:
            query = "delete from user where userId = {}".format(userId)
            print(query)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()

            logger.info("Deleted")
        except Exception as e:
            logger.error("Error occured at data deletion..", e)

    def update_user(self, userId, newName, newPhone):
        """This fuction used to update data into database"""

        try:
            query = "update user set userName = '{}', phone='{}' where userId ={}".format(newName, newPhone, userId)
            print(query)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()

            logger.info("updated")
        except Exception as e:
            logger.error("Error occured at data Update ", e)
