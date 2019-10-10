
from sqlalchemy import MetaData, create_engine, Table, Column
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker, Session
import pymysql
import config

conn = pymysql.connect(host=config.db_host, user=config.db_user, password=config.db_password, db=config.db_db)
cur = conn.cursor()



uri = config.db_uri
engine = create_engine(uri, echo=False)

Base = automap_base()
Base.prepare(engine, reflect=True)

Company = Base.classes.company
ShippingInfo = Base.classes.shipping_info
session = Session(bind=engine)


def insert_company(**kwargs):
    c = Company(**kwargs)
    session.add(c)
    session.commit()

def insert_shipping_info(**kwargs):
    s = ShippingInfo(**kwargs)
    session.add(s)
    session.commit()

def get_fields(table):
    cur.execute('show fields from %s'%table)

    labels = cur.fetchall()
    fields = [l[0] for l in labels]

    return fields

def get_contents(table):
    cur.execute('select * from %s'%table)
    contents = cur.fetchall()
    return contents

def get_slave_fields(table):
    cur.execute('show fields from %s'%table)
    labels = cur.fetchall()
    fields = [l[0] for l in labels]
    return fields

def get_slave_contents(table, c_id):
    cur.execute('select * from %s where company_id = %d'%(table, c_id))
    contents = cur.fetchall()
    return contents

