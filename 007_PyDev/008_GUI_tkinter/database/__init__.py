from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PasswordStore(Base):
    __tablename__ = 'password-store'
    
    id = Column(Integer(), primary_key=True)
    password = Column(String(40))
    user_name = Column(String(250))
    url = Column(String(1500))
    
    def __repr__(self) -> str:
        return f"PasswordStore(\
                    password='{self.password}'\
                    user_name = '{self.user_name}'\
                    url = '{self.url}')"
                    

def create_db():
    engine = create_engine('sqlite:///database/PasswordStore.sqlite')
    # Sve klase koje nasljeđuju base biti će dodane u bazu
    # u tabelu
    
    Base.metadata.create_all(engine)
