from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

# Conection
db = create_engine("sqlite:///banco.db")

# Base of the database
Base = declarative_base()

# Create tables
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=True)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean,default=False)

    def __init__(self, nome, email, ativo=True, admin=False):

        self.nome = nome
        self.email = email
        self.ativo = ativo
        self.admin = admin







