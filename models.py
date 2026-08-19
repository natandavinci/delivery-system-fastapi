from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

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

class Pedido(Base):
    __tablename__ = "pedidos"

    #"STATUS_PEDIDO" = (
       # ("PENDENTE", "PENDENTE"),
       # ("CANCELADO","CANCELADO"),
       # ("FINALIZADO", "FINALIZADO")
  #  )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String)
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)

    def __int__(self,status,usuario,preco):
        self.status = status
        self.usuario = usuario
        self.preco = preco

class itemPedido(Base):
    __tablename__ = "itensPedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))

    def __int__(self, quantidade, sabor, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.preco_unitario = preco_unitario
        self.pedido = pedido
        

        








