# TODO - Historial académico por carrera

- [ ] Agregar campo `carrera` al modelo de respuesta `HistorialAcademicoDetalleResponse`.
- [ ] Incluir `carrera` en el JSON armado en `crud_detalles.py` (mapper `_historial`).
- [ ] Cargar relación `Alumno.carrera` con `joinedload` para no romper el JSON.
- [ ] Agregar query param `carrera_id` al router `GET /historiales-academicos/`.
- [ ] Implementar filtro por `carrera_id` en `get_historiales_academicos_detalle`.
- [ ] Verificar que `GET /historiales-academicos/{id}` incluya `carrera` automáticamente.

