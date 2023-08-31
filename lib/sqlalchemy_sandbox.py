#!/usr/bin/env python3
# imports
# sqlalchemy_sandbox.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Step 1: Define the Base
Base = declarative_base()

# Step 2: Define the Data Model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

# Step 3: Persist the Schema
if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)


# Step 4: Make the Script Executable

# In your terminal, navigate to the directory containing sqlalchemy_sandbox.py and run the following command to make the script executable:

# bash

# chmod +x sqlalchemy_sandbox.py

# Step 5: Run the Script

# Now run the script using the following command:

# bash

# ./sqlalchemy_sandbox.py
# Step 5: Verify the Database

# You can verify that the database and table were created by opening the SQLite database file using a SQLite client, or you can use a tool like DB Browser for SQLite or VSCode's SQLite extension.

# That's it! You've successfully defined a data model for a students table using SQLAlchemy ORM and created the corresponding SQLite database table.

# Remember that this example uses SQLite as the database backend. You can replace 'sqlite:///students.db' with a different database URL if you want to use a different database system like MySQL or PostgreSQL.

# Please note that the code provided assumes you have the necessary dependencies (SQLAlchemy) installed in your environment. If not, you'll need to install them using something like pip install sqlalchemy.


