from db import Base
from sqlalchemy import Column, Integer, String

class Criptomonedas(Base):
    __tablename__="Criptomonedas"
    id_Cripto = Column(Integer, primary_key=True,)
    simbolo = Column(String(20))
    nombre = Column(String(20))
    id_api = Column(Integer)
    fecha_creacion= Column(Integer)