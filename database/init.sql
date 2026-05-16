
CREATE DATABASE unifront;
USE unifront;

CREATE TABLE usuarios (
    id_usuario BIGINT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido_paterno VARCHAR(100) NOT NULL,
    apellido_materno VARCHAR(100),
    correo VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    telefono VARCHAR(20),
    estado ENUM('ACTIVO','INACTIVO') DEFAULT 'ACTIVO',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE roles (
    id_rol INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) UNIQUE NOT NULL
) ENGINE=InnoDB;

CREATE TABLE usuario_roles (
    id_usuario BIGINT,
    id_rol INT,

    PRIMARY KEY (id_usuario, id_rol),

    CONSTRAINT fk_usuario_roles_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id_usuario),

    CONSTRAINT fk_usuario_roles_rol
        FOREIGN KEY (id_rol)
        REFERENCES roles(id_rol)
) ENGINE=InnoDB;

CREATE TABLE carreras (
    id_carrera INT PRIMARY KEY AUTO_INCREMENT,
    clave VARCHAR(20) UNIQUE,
    nombre VARCHAR(150) NOT NULL,
    nivel ENUM('TSU','LICENCIATURA','MAESTRIA', 'INGENIERIA') NOT NULL,
    duracion_cuatrimestres INT NOT NULL,
    estado BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

CREATE TABLE planes_estudio (
    id_plan INT PRIMARY KEY AUTO_INCREMENT,
    id_carrera INT NOT NULL,
    nombre_plan VARCHAR(100) NOT NULL,
    fecha_inicio DATE,
    fecha_fin DATE,
    vigente BOOLEAN DEFAULT TRUE,

    CONSTRAINT fk_plan_carrera
        FOREIGN KEY (id_carrera)
        REFERENCES carreras(id_carrera)
) ENGINE=InnoDB;

CREATE TABLE cuatrimestres (
    id_cuatrimestre INT PRIMARY KEY AUTO_INCREMENT,
    numero INT NOT NULL,
    nombre VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE materias (
    id_materia BIGINT PRIMARY KEY AUTO_INCREMENT,
    clave VARCHAR(20) UNIQUE,
    nombre VARCHAR(150) NOT NULL,
    creditos DECIMAL(5,2) NOT NULL,
    estado BOOLEAN DEFAULT TRUE,

    CONSTRAINT chk_creditos
        CHECK (creditos >= 0)
) ENGINE=InnoDB;

CREATE TABLE plan_materias (
    id_plan_materia BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_plan INT NOT NULL,
    id_materia BIGINT NOT NULL,
    id_cuatrimestre INT NOT NULL,
    obligatoria BOOLEAN DEFAULT TRUE,

    CONSTRAINT uq_plan_materia
        UNIQUE (id_plan, id_materia),

    CONSTRAINT fk_plan_materias_plan
        FOREIGN KEY (id_plan)
        REFERENCES planes_estudio(id_plan),

    CONSTRAINT fk_plan_materias_materia
        FOREIGN KEY (id_materia)
        REFERENCES materias(id_materia),

    CONSTRAINT fk_plan_materias_cuatrimestre
        FOREIGN KEY (id_cuatrimestre)
        REFERENCES cuatrimestres(id_cuatrimestre)
) ENGINE=InnoDB;

CREATE TABLE materias_prerrequisito (
    id_prerrequisito BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_materia BIGINT NOT NULL,
    id_materia_requerida BIGINT NOT NULL,
    tipo ENUM('OBLIGATORIO','RECOMENDADO') NOT NULL,

    CONSTRAINT fk_prerrequisito_materia
        FOREIGN KEY (id_materia)
        REFERENCES materias(id_materia),

    CONSTRAINT fk_prerrequisito_requerida
        FOREIGN KEY (id_materia_requerida)
        REFERENCES materias(id_materia)
) ENGINE=InnoDB;

CREATE TABLE alumnos (
    id_alumno BIGINT PRIMARY KEY AUTO_INCREMENT,
    matricula VARCHAR(20) NOT NULL UNIQUE,
    numero_control VARCHAR(30) UNIQUE,
    id_usuario BIGINT NOT NULL,
    id_carrera INT NOT NULL,
    id_plan INT NOT NULL,
    fecha_nacimiento DATE,
    ciudad_nacimiento VARCHAR(100),
    municipio_nacimiento VARCHAR(100),
    nacionalidad VARCHAR(100),
    sexo ENUM('M','F'),
    curp VARCHAR(18),
    direccion TEXT,
    ciudad VARCHAR(100),
    estado VARCHAR(100),
    correo_contacto VARCHAR(150),
    fecha_ingreso DATE,
    estatus ENUM('ACTIVO','BAJA','EGRESADO','TITULADO') DEFAULT 'ACTIVO',
    foto VARCHAR(255),

    CONSTRAINT fk_alumno_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id_usuario),

    CONSTRAINT fk_alumno_carrera
        FOREIGN KEY (id_carrera)
        REFERENCES carreras(id_carrera),

    CONSTRAINT fk_alumno_plan
        FOREIGN KEY (id_plan)
        REFERENCES planes_estudio(id_plan)
) ENGINE=InnoDB;

CREATE TABLE procedencia_academica (
    id_procedencia BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_alumno BIGINT NOT NULL,
    escuela_procedencia VARCHAR(255),
    nivel_academico ENUM('BACHILLERATO','UNIVERSIDAD','OTRO'),
    estado_procedencia VARCHAR(100),
    promedio_general DECIMAL(5,2),
    fecha_egreso DATE,

    CONSTRAINT chk_promedio_procedencia
        CHECK (promedio_general >= 0 AND promedio_general <= 100),

    CONSTRAINT fk_procedencia_alumno
        FOREIGN KEY (id_alumno)
        REFERENCES alumnos(id_alumno)
) ENGINE=InnoDB;

CREATE TABLE tutores (
    id_tutor BIGINT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(150) NOT NULL,
    parentesco VARCHAR(50),
    telefono VARCHAR(20),
    correo VARCHAR(100),
    ocupacion VARCHAR(100)
) ENGINE=InnoDB;

CREATE TABLE alumno_tutor (
    id_alumno BIGINT,
    id_tutor BIGINT,

    PRIMARY KEY (id_alumno, id_tutor),

    CONSTRAINT fk_alumno_tutor_alumno
        FOREIGN KEY (id_alumno)
        REFERENCES alumnos(id_alumno),

    CONSTRAINT fk_alumno_tutor_tutor
        FOREIGN KEY (id_tutor)
        REFERENCES tutores(id_tutor)
) ENGINE=InnoDB;

CREATE TABLE contactos_emergencia (
    id_contacto BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_alumno BIGINT NOT NULL,
    nombre VARCHAR(150) NOT NULL,
    parentesco VARCHAR(50),
    telefono VARCHAR(20),
    correo VARCHAR(150),
    direccion TEXT,
    contacto_principal BOOLEAN DEFAULT FALSE,

    CONSTRAINT fk_contacto_alumno
        FOREIGN KEY (id_alumno)
        REFERENCES alumnos(id_alumno)
) ENGINE=InnoDB;

CREATE TABLE seguros_medicos (
    id_seguro BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_alumno BIGINT NOT NULL,
    tiene_seguro BOOLEAN DEFAULT FALSE,
    institucion VARCHAR(150),
    numero_poliza VARCHAR(100),

    CONSTRAINT fk_seguro_alumno
        FOREIGN KEY (id_alumno)
        REFERENCES alumnos(id_alumno)
) ENGINE=InnoDB;

CREATE TABLE recepcion_documentos (
    id_recepcion BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_alumno BIGINT NOT NULL,
    ficha_inscripcion BOOLEAN DEFAULT FALSE,
    acta_original BOOLEAN DEFAULT FALSE,
    acta_copias BOOLEAN DEFAULT FALSE,
    certificado_original BOOLEAN DEFAULT FALSE,
    constancia_terminacion BOOLEAN DEFAULT FALSE,
    fotografias BOOLEAN DEFAULT FALSE,
    curp_documento BOOLEAN DEFAULT FALSE,
    fecha_recepcion DATE,
    recibido_por BIGINT,
    observaciones TEXT,

    CONSTRAINT fk_recepcion_alumno
        FOREIGN KEY (id_alumno)
        REFERENCES alumnos(id_alumno),

    CONSTRAINT fk_recepcion_usuario
        FOREIGN KEY (recibido_por)
        REFERENCES usuarios(id_usuario)
) ENGINE=InnoDB;

CREATE TABLE docentes (
    id_docente BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_usuario BIGINT NOT NULL,
    numero_empleado VARCHAR(20) UNIQUE,
    especialidad VARCHAR(150),
    grado_academico VARCHAR(100),
    fecha_ingreso DATE,
    estado BOOLEAN DEFAULT TRUE,

    CONSTRAINT fk_docente_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES usuarios(id_usuario)
) ENGINE=InnoDB;

CREATE TABLE periodos (
    id_periodo INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    fecha_inicio DATE,
    fecha_fin DATE,
    estado ENUM('ACTIVO','CERRADO') DEFAULT 'ACTIVO'
) ENGINE=InnoDB;

CREATE TABLE grupos (
    id_grupo BIGINT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    id_carrera INT,
    id_cuatrimestre INT,
    turno ENUM('MATUTINO','VESPERTINO'),

    CONSTRAINT fk_grupo_carrera
        FOREIGN KEY (id_carrera)
        REFERENCES carreras(id_carrera),

    CONSTRAINT fk_grupo_cuatrimestre
        FOREIGN KEY (id_cuatrimestre)
        REFERENCES cuatrimestres(id_cuatrimestre)
) ENGINE=InnoDB;

CREATE TABLE grupos_materias (
    id_grupo_materia BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_grupo BIGINT,
    id_materia BIGINT,
    id_docente BIGINT,
    id_periodo INT,
    aula VARCHAR(20),
    cupo_maximo INT,

    CONSTRAINT fk_grupo_materia_grupo
        FOREIGN KEY (id_grupo)
        REFERENCES grupos(id_grupo),

    CONSTRAINT fk_grupo_materia_materia
        FOREIGN KEY (id_materia)
        REFERENCES materias(id_materia),

    CONSTRAINT fk_grupo_materia_docente
        FOREIGN KEY (id_docente)
        REFERENCES docentes(id_docente),

    CONSTRAINT fk_grupo_materia_periodo
        FOREIGN KEY (id_periodo)
        REFERENCES periodos(id_periodo)
) ENGINE=InnoDB;

CREATE TABLE inscripciones (
    id_inscripcion BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_alumno BIGINT,
    id_grupo BIGINT,
    id_periodo INT,
    fecha_inscripcion DATE,
    estado ENUM('ACTIVO','BAJA','FINALIZADO') DEFAULT 'ACTIVO',

    CONSTRAINT fk_inscripcion_alumno
        FOREIGN KEY (id_alumno)
        REFERENCES alumnos(id_alumno),

    CONSTRAINT fk_inscripcion_grupo
        FOREIGN KEY (id_grupo)
        REFERENCES grupos(id_grupo),

    CONSTRAINT fk_inscripcion_periodo
        FOREIGN KEY (id_periodo)
        REFERENCES periodos(id_periodo)
) ENGINE=InnoDB;

CREATE TABLE carga_academica (
    id_carga BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_alumno BIGINT,
    id_grupo_materia BIGINT,
    oportunidad ENUM('ORDINARIO','EXTRAORDINARIO'),
    intento INT,
    estatus ENUM('CURSANDO','APROBADA','REPROBADA','NP','BAJA') DEFAULT 'CURSANDO',
    fecha_inscripcion DATE,

    CONSTRAINT chk_intento
        CHECK (intento >= 1),

    CONSTRAINT fk_carga_alumno
        FOREIGN KEY (id_alumno)
        REFERENCES alumnos(id_alumno),

    CONSTRAINT fk_carga_grupo_materia
        FOREIGN KEY (id_grupo_materia)
        REFERENCES grupos_materias(id_grupo_materia)
) ENGINE=InnoDB;

CREATE TABLE parciales (
    id_parcial INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    porcentaje DECIMAL(5,2)
) ENGINE=InnoDB;

CREATE TABLE calificaciones (
    id_calificacion BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_carga BIGINT,
    id_parcial INT,
    calificacion DECIMAL(5,2),
    fecha_captura TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    capturado_por BIGINT,

    CONSTRAINT chk_calificacion
        CHECK (calificacion >= 0 AND calificacion <= 100),

    CONSTRAINT fk_calificacion_carga
        FOREIGN KEY (id_carga)
        REFERENCES carga_academica(id_carga),

    CONSTRAINT fk_calificacion_parcial
        FOREIGN KEY (id_parcial)
        REFERENCES parciales(id_parcial),

    CONSTRAINT fk_calificacion_usuario
        FOREIGN KEY (capturado_por)
        REFERENCES usuarios(id_usuario)
) ENGINE=InnoDB;

CREATE TABLE extraordinarios (
    id_extraordinario BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_alumno BIGINT,
    id_materia BIGINT,
    intento INT,
    fecha_examen DATE,
    calificacion DECIMAL(5,2),
    estatus ENUM('APROBADO','REPROBADO','NP'),
    observaciones TEXT,

    CONSTRAINT chk_extra_intento
        CHECK (intento >= 2 AND intento <= 4),

    CONSTRAINT chk_extra_calificacion
        CHECK (calificacion >= 0 AND calificacion <= 80),

    CONSTRAINT fk_extra_alumno
        FOREIGN KEY (id_alumno)
        REFERENCES alumnos(id_alumno),

    CONSTRAINT fk_extra_materia
        FOREIGN KEY (id_materia)
        REFERENCES materias(id_materia)
) ENGINE=InnoDB;

CREATE TABLE historial_academico (
    id_historial BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_alumno BIGINT,
    id_materia BIGINT,
    id_periodo INT,
    tipo_evaluacion ENUM('ORDINARIO','EXTRAORDINARIO'),
    oportunidad INT,
    calificacion_final DECIMAL(5,2),
    resultado ENUM('APROBADO','REPROBADO','NP'),
    fecha_cierre DATE,

    CONSTRAINT chk_historial_calificacion
        CHECK (calificacion_final >= 0 AND calificacion_final <= 100),

    CONSTRAINT fk_historial_alumno
        FOREIGN KEY (id_alumno)
        REFERENCES alumnos(id_alumno),

    CONSTRAINT fk_historial_materia
        FOREIGN KEY (id_materia)
        REFERENCES materias(id_materia),

    CONSTRAINT fk_historial_periodo
        FOREIGN KEY (id_periodo)
        REFERENCES periodos(id_periodo)
) ENGINE=InnoDB;

CREATE TABLE asistencias (
    id_asistencia BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_carga BIGINT,
    fecha DATE,
    asistencia BOOLEAN,

    CONSTRAINT fk_asistencia_carga
        FOREIGN KEY (id_carga)
        REFERENCES carga_academica(id_carga)
) ENGINE=InnoDB;

CREATE TABLE tipos_documento (
    id_tipo_documento INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100)
) ENGINE=InnoDB;

CREATE TABLE documentos_alumno (
    id_documento BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_alumno BIGINT,
    id_tipo_documento INT,
    nombre_archivo VARCHAR(255),
    ruta_archivo VARCHAR(500),
    fecha_subida TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    validado BOOLEAN DEFAULT FALSE,
    observaciones TEXT,

    CONSTRAINT fk_documento_alumno
        FOREIGN KEY (id_alumno)
        REFERENCES alumnos(id_alumno),

    CONSTRAINT fk_documento_tipo
        FOREIGN KEY (id_tipo_documento)
        REFERENCES tipos_documento(id_tipo_documento)
) ENGINE=InnoDB;

CREATE TABLE empresas (
    id_empresa BIGINT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(150),
    direccion TEXT,
    telefono VARCHAR(20),
    correo VARCHAR(100)
) ENGINE=InnoDB;

CREATE TABLE servicio_social (
    id_servicio BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_alumno BIGINT,
    id_empresa BIGINT,
    horas_requeridas INT,
    horas_completadas INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    estado ENUM('EN_PROCESO','COMPLETADO'),

    CONSTRAINT fk_servicio_alumno
        FOREIGN KEY (id_alumno)
        REFERENCES alumnos(id_alumno),

    CONSTRAINT fk_servicio_empresa
        FOREIGN KEY (id_empresa)
        REFERENCES empresas(id_empresa)
) ENGINE=InnoDB;

CREATE TABLE practicas_profesionales (
    id_practica BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_alumno BIGINT,
    id_empresa BIGINT,
    proyecto VARCHAR(255),
    asesor_empresa VARCHAR(150),
    asesor_universidad VARCHAR(150),
    fecha_inicio DATE,
    fecha_fin DATE,
    estado ENUM('EN_PROCESO','COMPLETADO'),

    CONSTRAINT fk_practica_alumno
        FOREIGN KEY (id_alumno)
        REFERENCES alumnos(id_alumno),

    CONSTRAINT fk_practica_empresa
        FOREIGN KEY (id_empresa)
        REFERENCES empresas(id_empresa)
) ENGINE=InnoDB;

CREATE TABLE titulacion (
    id_titulacion BIGINT PRIMARY KEY AUTO_INCREMENT,
    id_alumno BIGINT,
    modalidad ENUM('PROMEDIO','TESIS','TESINA'),
    cumple_promedio BOOLEAN,
    servicio_social_liberado BOOLEAN,
    practicas_liberadas BOOLEAN,
    certificado_emitido BOOLEAN,
    pagos_titulacion_completos BOOLEAN,
    numero_autorizacion VARCHAR(100),
    acta_examen VARCHAR(255),
    titulo_emitido BOOLEAN,
    fecha_titulacion DATE,
    observaciones TEXT,

    CONSTRAINT fk_titulacion_alumno
        FOREIGN KEY (id_alumno)
        REFERENCES alumnos(id_alumno)
) ENGINE=InnoDB;

-- =========================================================
-- INDICES IMPORTANTES
-- =========================================================

CREATE INDEX idx_alumnos_matricula
ON alumnos(matricula);

CREATE INDEX idx_alumnos_numero_control
ON alumnos(numero_control);

CREATE INDEX idx_alumnos_curp
ON alumnos(curp);

CREATE INDEX idx_historial_alumno
ON historial_academico(id_alumno);

CREATE INDEX idx_historial_materia
ON historial_academico(id_materia);

CREATE INDEX idx_carga_alumno
ON carga_academica(id_alumno);

CREATE INDEX idx_calificacion_carga
ON calificaciones(id_carga);

CREATE INDEX idx_asistencia_carga
ON asistencias(id_carga);

CREATE INDEX idx_usuario_correo
ON usuarios(correo);
