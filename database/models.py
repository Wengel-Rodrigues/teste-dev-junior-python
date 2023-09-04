from sqlalchemy import Column, Integer, String, DateTime, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class NFE(Base):
    __tablename__ = 'nfe'

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    cUF = Column(Integer)
    cNF = Column(String)
    natOp = Column(String)
    mod = Column(Integer)
    serie = Column(Integer)
    nNF = Column(Integer)
    
    emitente_CNPJ = Column(String)
    emitente_xNome = Column(String)
    emitente_xFant = Column(String)
    
    destinatario_CPF = Column(String)
    destinatario_xNome = Column(String)
    
    cProd = Column(String)
    xProd = Column(String)
    vProd = Column(Float)
    
    vNF = Column(Float)
    vICMS = Column(Float)
