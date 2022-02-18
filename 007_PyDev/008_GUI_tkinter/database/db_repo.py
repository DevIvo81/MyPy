from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker

from database import PasswordStore

engine = create_engine('sqlite:///database/PasswordStore.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

def get_passwords(session):
    return session.query(PasswordStore).all()


def create_and_update_password_entry(password_entry):
    password_entry_from_db = (
        session.query(PasswordStore)
        .filter(
            and_(
                PasswordStore.password == password_entry.password,
                PasswordStore.user_name == password_entry.user_name,
                PasswordStore.url == password_entry.url,
            )
        )
        .one_or_none()
    )
    
    if password_entry_from_db is not None:
        password_entry_from_db.password = password_entry.password
        password_entry_from_db.user_name = password_entry.user_name
        password_entry_from_db.url = password_entry.url
    
    else:
        password_entry_from_db = password_entry
        session.add(password_entry_from_db)
        
    session.commit()