from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship 
from sqlalchemy.ext.declarative import declarative_base

# Crear una extancia de la base de datos para crear tablas 

Base = declarative_base()

# Listado de modelos de la aplicación
# Usuario
class Usuario(Base): #En el parentesis se pone la base de datos
    #pass # Cuando uno no sabe que poner, pone pass 
    __tablename__ = 'usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nomres=Column(String(50))
    edad=Column(Integer)
    telefono=Column(String(12))
    correo=Column(String(20))
    contraseña=Column(String(10))
    fechaRegistro=Column(Date)
    ciudad=Column(Integer(50)) 

# gasto
class Gasto(Base):
    id=Column(Integer, primary_key=True, autoincrement=True)
    monto=Column(Integer)
    fecha=Column(Date)
    descripcion=Column(String(250))
    nombre=(String(50))

# Categoría 

class Categoría(Base):
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreCategoria=Column(String(50))
    fotoicono=Column(String(50))

# Producto

# Metodo de pago
class MetodoPago(Base):
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreMetodo=Column(String(50))
    descripcion=Column(String(250))

# Factura 
class Factura(Base):
    pass