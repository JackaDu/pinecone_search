from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
import os
from dotenv import load_dotenv
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
load_dotenv()
SQLALCHEMY_DATABASE_URL = os.environ['PSQL_URL']

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Load and display the contents of each CSV file to check
csv_files = {
    'loan': './test.csv',
}
for table_name, file_path in csv_files.items():
    df = pd.read_csv(file_path)
    df.to_sql(table_name, engine, if_exists='replace', index=False)