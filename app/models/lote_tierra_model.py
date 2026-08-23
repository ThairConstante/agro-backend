from sqlalchemy import Column, Integer, String, Text, Numeric, ForeignKey
from app.core.config import Base


class LoteTierra(Base):
    __tablename__ = "lotes_tierra"

    Lote_Id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    Zona_Id = Column(
        Integer,
        ForeignKey("zonas_geograficas.Zona_Id"),
        nullable=False
    )

    TipoSuelo_Id = Column(
        Integer,
        ForeignKey("tipos_suelo.TipoSuelo_Id"),
        nullable=False
    )

    Lote_Nombre = Column(String(150), nullable=False)
    Lote_Descripcion = Column(Text, nullable=True)
    Lote_Area = Column(Numeric(12, 2), nullable=True)