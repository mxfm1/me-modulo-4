from dataclasses import dataclass

@dataclass
class Proveedor:
    rut:str
    nombre_legal:str
    razon_social:str
    pais:str
    persona_juridica:str
    attr_op = str