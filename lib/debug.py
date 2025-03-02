from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie


engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()


if __name__ == '__main__':

    import ipdb; ipdb.set_trace()

    session.close()
    print("Session closed.")