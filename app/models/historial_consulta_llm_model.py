from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from app.core.config import Base

class HistorialConsultaLLM(Base):
    __tablename__ = "historial_consultas_llm"

    Historial_Id = Column("Historial_Id", Integer, primary_key=True, index=True, autoincrement=True)
    Usuario_Id = Column("Usuario_Id", Integer, ForeignKey("usuario.Usuario_Id"), nullable=False)
    Historial_Prompt = Column("Historial_Prompt", Text, nullable=False)
    Historial_Respuesta = Column("Historial_Respuesta", Text, nullable=True)
    Historial_Modelo = Column("Historial_Modelo", String(100), nullable=True)
    Historial_FechaHora = Column("Historial_FechaHora", DateTime, nullable=False)