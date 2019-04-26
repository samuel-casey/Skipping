import sqlite3
database = 'database.db'
try:
    db = sqlite3.connect(database)
    cur = db.cursor()
    print("connection success to {}".format(database))
except Error as e:
    print(e)
def db_conn(database='database.db'):
    try:
        db = sqlite3.connect(database)
        print("connection success to {}".format(database))
        return db
    except Error as e:
        print(e)
        return None 
def create_db():
    # db.execute('drop table if exists conditions')
    db.execute("""CREATE TABLE IF NOT EXISTS conditions(
	  condition_ID bigint NOT NULL PRIMARY KEY,
	  condition_name varchar(50) NOT NULL,
	  condition_category_id bigint NOT NULL, 
	  description text NULL,
      FOREIGN KEY (condition_category_ID) REFERENCES condition_category(condition_category_ID)
      );""")
    db.execute("""CREATE TABLE IF NOT EXISTS cond_treat(
	  cond_treat_ID bigint NOT NULL PRIMARY KEY,
	  cond_treat_name varchar(50) NOT NULL,
	  condition_ID bigint NOT NULL,
	  treatment_ID bigint NOT NULL,
      FOREIGN KEY (condition_ID) REFERENCES conditions(condition_ID),
      FOREIGN KEY (treatment_ID) REFERENCES treatments(treatment_ID)
      );""")
    db.execute("""CREATE TABLE IF NOT EXISTS treatments(
	  treatment_ID bigint NOT NULL PRIMARY KEY,
	  treatment_name varchar(50) NOT NULL,
	  treatment_category_id bigint NOT NULL, 
	  description text NULL,
      FOREIGN KEY (treatment_category_ID) REFERENCES treatment_category(treatment_category_ID)
      );""")
    db.execute("""CREATE TABLE IF NOT EXISTS treatment_category(
	  treatment_category_ID bigint NOT NULL PRIMARY KEY,
	  treatment_category_name varchar(50) NOT NULL,
	  description varchar(50) NULL); """)
    db.execute("""
	CREATE TABLE IF NOT EXISTS condition_category(
	  condition_category_ID bigint NOT NULL PRIMARY KEY,
	  condition_category_name varchar(50) NOT NULL,
	  description varchar(50) NULL); """)
def insert_condition(condition_ID, condition_name, condition_category_ID, description):   
    string = "INSERT INTO conditions (condition_ID, condition_name, condition_category_ID, description) VALUES ({},'{}',{},'{}')".format(condition_ID,condition_name,category_ID,description)
    print("Executing - - {}".format(string))
    cur.execute(string)
    db.commit()
    return cur .lastrowid
def insert_treatment(treatment_ID, treatment_name, treatment_category_ID, description):   
    string = "INSERT INTO treatments (treatment_ID, treatment_name, treatment_category_ID, description) VALUES ({},'{}',{},'{}')".format(treatment_ID, treatment_name,treatment_category_ID,description)
    print("Executing - - {}".format(string))
    cur.execute(string)
    db.commit()
    return cur .lastrowid
def insert_relationship(cond_treat_ID, cond_treat_name, treatment_ID, condition_ID):   
    string = "INSERT INTO cond_treat (cond_treat_ID, cond_treat_name, treatment_ID, condition_ID) VALUES ({},'{}',{},{})".format(cond_treat_ID, cond_treat_name,treatment_ID,condition_ID)
    print("Executing - - {}".format(string))
    cur.execute(string)
    db.commit()
    return cur .lastrowid
def view_table(table):
    cur = sqlite3.connect(database).cursor()
    query = 'SELECT * FROM {};'.format(table)
    string = ''
    for condition_ID, condition_name, category_ID, description in cur.execute(query):
        string = string+"{},{},{},{}\n".format(condition_ID, condition_name, category_ID, description)
    return string

# create_db()
# insert_condition(1,"Breast Cancer",1,"Cancer of the breast")
# insert_treatment(1,"Coffee Enemas", 1, "Reverse digestion of coffee.")
# insert_relationship(1,'Coffee Enemas for Breast Cancer',1,1)
print(view_table('cond_treat'))