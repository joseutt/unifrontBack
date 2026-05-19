# Modelos sin CRUD (según `backend/app/crud`)

Este archivo compara los modelos existentes en `backend/app/models` contra los CRUD implementados en `backend/app/crud`.

## CRUD existentes (archivos)
En `backend/app/crud` hay CRUD para:
- `Alumno`  (`crud_alumno.py`)
- `Calificacion` (`crud_calificacion.py`)
- `Carrera` (`crud_carrera.py`)
- `Docente` (`crud_docente.py`)
- `Materia` (`crud_materia.py`)
- `Parcial` (`crud_parcial.py`)
- `Periodo` (`crud_periodo.py`)
- `PlanEstudio` (`crud_plan_estudio.py`)
- `Rol` (`crud_rol.py`)
- `Titulacion` (`crud_titulacion.py`)
- `Usuario` (`crud_usuario.py`)

## Modelos sin CRUD implementado
Los siguientes modelos existen en `backend/app/models`, pero **no** tienen un archivo CRUD correspondiente en `backend/app/crud`:

- `AlumnoTutor` (`alumno_tutor.py`)
- `Asistencia` (`asistencia.py`)
- `ContactoEmergencia` (`contacto_emergencia.py`)
- `CargaAcademica` (`carga_academica.py`)
- `Cuatrimestre` (`cuatrimestre.py`)
- `DocumentoAlumno` (`documento_alumno.py`)
- `Empresa` (`empresa.py`)
- `Extraordinario` (`extraordinario.py`)
- `Grupo` (`grupo.py`)
- `GrupoMateria` (`grupo_materia.py`)
- `HistorialAcademico` (`historial_academico.py`)
- `Inscripcion` (`inscripcion.py`)
- `Parcial` **(nota)**: *sí tiene CRUD* (`crud_parcial.py`)
- `PlanMateria` (`plan_materia.py`)
- `PracticaProfesional` (`practica_profesional.py`)
- `ProcedenciaAcademica` (`procedencia_academica.py`)
- `RecepcionDocumento` (`recepcion_documento.py`)
- `SeguroMedico` (`seguro_medico.py`)
- `ServicioSocial` (`servicio_social.py`)
- `Tutor` (`tutor.py`)
- `TipoDocumento` (`tipo_documento.py`)
- `UsuarioRol` (`usuario_rol.py`)

> Nota: La comparación se basa en la existencia de un módulo CRUD dedicado (archivo `crud_*.py`). No se valida si algunas operaciones CRUD se realizan indirectamente desde otros lugares (routers/services), solo si hay un CRUD estándar en `backend/app/crud` para ese modelo.

