from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,Date,ForeignKey,Boolean

class ServerDB:
    def __init__(self):
        db_uri = 'sqlite:///chatdb.sqlite'
        self.engine = create_engine(db_uri)        
    
    def createdb(self):
        meta = MetaData(self.engine)
    
        users=Table('users',meta,
            Column('id', Integer, primary_key=True),
            Column('name',String), 
            Column('ip',String),
            Column('status',Boolean))

        message_pool = Table('message_pool',meta,
                Column('id', Integer, primary_key=True),
                Column('sender_name',String), 
                Column('recipient_name',String), 
                Column('message',String),
                Column('Date',Date),
                Column('delivered',Boolean))

        try:
            meta.create_all()  
        except Exception as error:            
            print(error)  

    def execute_query(self,query=''):
        if query == '' : return

        with self.engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    D=ServerDB()
    D.createdb()