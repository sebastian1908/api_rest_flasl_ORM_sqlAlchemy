from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

engine  = create_engine('mysql+pymysql://root:@localhost/prueba')
Base = declarative_base()

class Admin(Base):
    __tablename__ = 'Admins'

    id = Column(Integer(), primary_key=True)
    rol = Column(String(20), nullable=False, unique=True)
    nombres = Column(String(20), nullable=False, unique=True)

    def __str__(self):
        return self.rol

Session = sessionmaker(engine)
session = Session()


if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    # print("Tabla creada con exito")
    Base.metadata.create_all(engine)

    # usuario = Admin(rol='Administrador', nombres='Juan')
    # usuario2 = Admin(rol='Estudiante', nombres='quesito alpina')
    
    # session.add(usuario)
    # session.add(usuario2)
    # session.commit()


    # usuarioActuali = session.query(Admin).filter(Admin.id == 1).first()
    # usuarioActuali.rol = 'Juan la rata cubo minecraft'
    # usuario.nombres = 'como queso alpina juan'

    # session.add(usuarioActuali)
    # session.commit()


    eliminar = session.query(Admin).filter(Admin.id == 2).delete()
    session.commit()
