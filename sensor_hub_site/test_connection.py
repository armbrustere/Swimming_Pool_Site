from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from sqlalchemy_utils import database_exists, create_database

engine = create_engine('mysql://admin:Fzo3rXcAPgXkzPNVBZMJ@swim-pool-db-1.capjadvh5mfr.us-east-1.rds.amazonaws.com:3306/Pool_Temps', echo=True)
# engine = create_engine('mysql://test_user:test_user@192.168.1.173:3306/pool_sensor_hub', echo=True)
#engine = create_engine('mysql://test_user:test_user@192.168.1.173:3306/sensor_readings', echo=True)
#mysql://admin:Fzo3rXcAPgXkzPNVBZMJ@swim-pool-db-1.capjadvh5mfr.us-east-1.rds.amazonaws.com:3306/Temperature_Data'

print(engine)
Base = declarative_base()
Base.metadata.reflect(engine)
Session = sessionmaker(bind=engine)
session = Session()
