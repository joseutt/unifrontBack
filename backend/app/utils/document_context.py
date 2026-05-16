from app.utils.gramatica import *

def construir_contexto_documento(alumno):

    return {
        "alumno": alumno,
        "txt": {
            "alumno": articulo_alumno(alumno.sexo),
            "inscrito": inscrito(alumno.sexo),
            "egresado": egresado(alumno.sexo),
            "interesado": interesado(alumno.sexo),
        }
    }