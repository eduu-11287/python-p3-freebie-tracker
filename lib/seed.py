#!/usr/bin/env python3

# Script goes here!
#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)  
Session = sessionmaker(bind=engine)
session = Session()

session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

company1 = Company(name="Coca cola", founding_year=1988)
company2 = Company(name="Pepsi", founding_year=1980)
company3 = Company(name="Nvida", founding_year=1980)
session.add(company1)
session.add(company2)
session.add(company3)

dev1 = Dev(name="John")
dev2 = Dev(name="Janet")
dev3 = Dev(name="Ken")
session.add(dev1)
session.add(dev2)
session.add(dev3)

session.commit()

Freebie1 = Freebie(item_name= "T-shirt", value=15, dev=dev1, company= company1)
Freebie2 = Freebie(item_name= "Mug", value=10, dev=dev2, company=company2)
Freebie3 = Freebie(item_name= "Sticker", value=5, dev=dev1, company=company2)
session.add(Freebie1)
session.add(Freebie2)
session.add(Freebie3)

session.commit()
session.close()
print ("Data added successfully!")

