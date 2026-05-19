# Modelos usados por CRUD

Este documento resume los modelos de SQLAlchemy que usa cada archivo dentro de `backend/app/crud`.

## Resumen por archivo CRUD

| Archivo CRUD | Modelo principal usado | Archivo del modelo | Tabla SQL | Uso dentro del CRUD |
| --- | --- | --- | --- | --- |
| `crud_alumno.py` | `Alumno` | `app/models/alumno.py` | `alumnos` | Listar, obtener por id, crear, actualizar y eliminar alumnos. |
| `crud_alumno_tutor.py` | `alumno_tutor` | `app/models/alumno_tutor.py` | `alumno_tutor` | Crear, consultar y eliminar relaciones entre alumnos y tutores. |
| `crud_asistencia.py` | `Asistencia` | `app/models/asistencia.py` | `asistencias` | Listar, obtener por id, crear, actualizar y eliminar asistencias. |
| `crud_calificacion.py` | `Calificacion` | `app/models/calificacion.py` | `calificaciones` | Listar, obtener por id, crear, actualizar y eliminar calificaciones. |
| `crud_carrera.py` | `Carrera` | `app/models/carrera.py` | `carreras` | Listar, obtener por id, crear, actualizar y eliminar carreras. |
| `crud_carga_academica.py` | `CargaAcademica` | `app/models/carga_academica.py` | `carga_academica` | Listar, obtener por id, crear, actualizar y eliminar cargas academicas. |
| `crud_contacto_emergencia.py` | `ContactoEmergencia` | `app/models/contacto_emergencia.py` | `contactos_emergencia` | Listar, obtener por id, crear, actualizar y eliminar contactos de emergencia. |
| `crud_cuatrimestre.py` | `Cuatrimestre` | `app/models/cuatrimestre.py` | `cuatrimestres` | Listar, obtener por id, crear, actualizar y eliminar cuatrimestres. |
| `crud_docente.py` | `Docente` | `app/models/docente.py` | `docentes` | Listar, obtener por id, crear, actualizar y eliminar docentes. |
| `crud_documento_alumno.py` | `DocumentoAlumno` | `app/models/documento_alumno.py` | `documentos_alumno` | Listar, obtener por id, crear, actualizar y eliminar documentos de alumno. |
| `crud_empresa.py` | `Empresa` | `app/models/empresa.py` | `empresas` | Listar, obtener por id, crear, actualizar y eliminar empresas. |
| `crud_extraordinario.py` | `Extraordinario` | `app/models/extraordinario.py` | `extraordinarios` | Listar, obtener por id, crear, actualizar y eliminar extraordinarios. |
| `crud_grupo.py` | `Grupo` | `app/models/grupo.py` | `grupos` | Listar, obtener por id, crear, actualizar y eliminar grupos. |
| `crud_grupo_materia.py` | `GrupoMateria` | `app/models/grupo_materia.py` | `grupos_materias` | Listar, obtener por id, crear, actualizar y eliminar relaciones grupo-materia. |
| `crud_historial_academico.py` | `HistorialAcademico` | `app/models/historial_academico.py` | `historial_academico` | Listar, obtener por id, crear, actualizar y eliminar historial academico. |
| `crud_inscripcion.py` | `Inscripcion` | `app/models/inscripcion.py` | `inscripciones` | Listar, obtener por id, crear, actualizar y eliminar inscripciones. |
| `crud_materia.py` | `Materia` | `app/models/materia.py` | `materias` | Listar, obtener por id, crear, actualizar y eliminar materias. |
| `crud_parcial.py` | `Parcial` | `app/models/parcial.py` | `parciales` | Listar, obtener por id, crear, actualizar y eliminar parciales. |
| `crud_periodo.py` | `Periodo` | `app/models/periodo.py` | `periodos` | Listar, obtener por id, crear, actualizar y eliminar periodos. |
| `crud_plan_estudio.py` | `PlanEstudio`, `PlanMateria` | `app/models/plan_estudio.py`, `app/models/plan_materia.py` | `planes_estudio`, `plan_materias` | Crear planes de estudio, asociar materias al plan, consultar planes con relaciones, actualizar y eliminar. |
| `crud_practica_profesional.py` | `PracticaProfesional` | `app/models/practica_profesional.py` | `practicas_profesionales` | Listar, obtener por id, crear, actualizar y eliminar practicas profesionales. |
| `crud_procedencia_academica.py` | `ProcedenciaAcademica` | `app/models/procedencia_academica.py` | `procedencia_academica` | Listar, obtener por id, crear, actualizar y eliminar procedencias academicas. |
| `crud_recepcion_documento.py` | `RecepcionDocumento` | `app/models/recepcion_documento.py` | `recepcion_documentos` | Listar, obtener por id, crear, actualizar y eliminar recepciones de documentos. |
| `crud_rol.py` | `Rol` | `app/models/rol.py` | `roles` | Listar, obtener por id, crear, actualizar y eliminar roles. |
| `crud_seguro_medico.py` | `SeguroMedico` | `app/models/seguro_medico.py` | `seguros_medicos` | Listar, obtener por id, crear, actualizar y eliminar seguros medicos. |
| `crud_servicio_social.py` | `ServicioSocial` | `app/models/servicio_social.py` | `servicio_social` | Listar, obtener por id, crear, actualizar y eliminar servicios sociales. |
| `crud_tipo_documento.py` | `TipoDocumento` | `app/models/tipo_documento.py` | `tipos_documento` | Listar, obtener por id, crear, actualizar y eliminar tipos de documento. |
| `crud_titulacion.py` | `Titulacion` | `app/models/titulacion.py` | `titulacion` | Listar, obtener por id, crear, actualizar y eliminar titulaciones. |
| `crud_tutor.py` | `Tutor` | `app/models/tutor.py` | `tutores` | Listar, obtener por id, crear, actualizar y eliminar tutores. |
| `crud_usuario.py` | `Usuario` | `app/models/usuario.py` | `usuarios` | Listar, obtener por id, crear usuarios con password hasheada, actualizar y eliminar usuarios. |
| `crud_usuario_rol.py` | `usuario_roles` | `app/models/usuario_rol.py` | `usuario_roles` | Crear, consultar y eliminar relaciones entre usuarios y roles. |

## Relaciones relevantes usadas o expuestas

### `crud_plan_estudio.py`

Este es el CRUD con mas relaciones cargadas explicitamente.

- Usa directamente `PlanEstudio` para crear, consultar, actualizar y eliminar planes.
- Usa directamente `PlanMateria` para agregar materias a un plan en `crear_plan_estudio`.
- En `obtener_planes` carga relaciones con `joinedload`:
  - `PlanEstudio.carrera`, relacionada con el modelo `Carrera`.
  - `PlanEstudio.materias`, relacionada con el modelo `PlanMateria`.
  - `PlanMateria.materia`, relacionada con el modelo `Materia`.
  - `PlanMateria.cuatrimestre`, relacionada con el modelo `Cuatrimestre`.
- En `transformar_plan` se leen datos de:
  - `plan.carrera`
  - `plan.materias`
  - `pm.materia`
  - `pm.cuatrimestre`

Aunque `Carrera`, `Materia` y `Cuatrimestre` no se importan directamente en `crud_plan_estudio.py`, el CRUD depende de esas relaciones definidas en los modelos.

### `crud_alumno.py`

Usa directamente `Alumno`. El modelo `Alumno` tiene relaciones con:

- `Usuario`
- `Carrera`
- `PlanEstudio`
- `ContactoEmergencia`
- `SeguroMedico`
- `ProcedenciaAcademica`

El CRUD no usa `joinedload` ni consulta esas relaciones de forma explicita, pero pueden aparecer al serializar respuestas si los schemas las incluyen.

### `crud_calificacion.py`

Usa directamente `Calificacion`. El modelo `Calificacion` tiene relaciones con:

- `CargaAcademica`
- `Parcial`
- `Usuario`

El CRUD solo consulta `Calificacion` directamente.

### `crud_titulacion.py`

Usa directamente `Titulacion`. El modelo `Titulacion` tiene relacion con:

- `Alumno`

El CRUD solo consulta `Titulacion` directamente.

## CRUD disponibles en routers

Los routers importan estos CRUD:

| Router | CRUD usado |
| --- | --- |
| `alumnos.py` | `crud_alumno.py` |
| `calificaciones.py` | `crud_calificacion.py` |
| `carreras.py` | `crud_carrera.py` |
| `docentes.py` | `crud_docente.py` |
| `documentos.py` | `crud_alumno.py` (`get_alumno`) |
| `materias.py` | `crud_materia.py` |
| `parciales.py` | `crud_parcial.py` |
| `periodos.py` | `crud_periodo.py` |
| `plan_estudio.py` | `crud_plan_estudio.py` |
| `titulaciones.py` | `crud_titulacion.py` |
| `usuarios.py` | `crud_usuario.py` |

En `routers/roles.py` las importaciones de `crud_rol.py` aparecen comentadas, por lo que actualmente el router de roles no esta usando ese CRUD de forma activa.

## Modelos sin CRUD directo encontrado

Despues de agregar los CRUD faltantes, no quedan modelos de `backend/app/models` sin archivo CRUD directo, considerando tambien las tablas pivote `alumno_tutor` y `usuario_roles`.

Nota: `PlanMateria` no tiene un archivo CRUD independiente porque ya se maneja directamente dentro de `crud_plan_estudio.py`.
