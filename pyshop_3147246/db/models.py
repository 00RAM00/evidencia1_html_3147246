from .database import Base
from sqlalchemy import column, Integer, String

#Crear la base del modelo (Entidad)
class Categoria(Base):
    __tablename__= "categorias"
    id = column(Integer, 
                PrimaryKey = True
                )
    nombre = column(String(50))
    