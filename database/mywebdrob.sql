-- MyWebdrob - Esquema de base de datos (MySQL 8+)
-- Codificación recomendada: utf8mb4
-- Motor recomendado: InnoDB

CREATE DATABASE IF NOT EXISTS mywebdrob
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;
USE mywebdrob;

-- ---------------------------------------------------------------------
-- TABLA: usuarios
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS usuarios (
  id            BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre        VARCHAR(100)        NOT NULL,
  email         VARCHAR(190)        NOT NULL,
  password_hash VARCHAR(255)        NOT NULL,
  rol           ENUM('usuario','administrador') NOT NULL DEFAULT 'usuario',
  plan          ENUM('free','premium') NOT NULL DEFAULT 'free',
  created_at    TIMESTAMP            NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY ux_usuarios_email (email)
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------
-- TABLA: prendas
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS prendas (
  id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  usuario_id  BIGINT UNSIGNED NOT NULL,
  categoria   VARCHAR(50)      NOT NULL,
  color       VARCHAR(50)      NULL,
  estilo      VARCHAR(50)      NULL,
  temporada   VARCHAR(50)      NULL,
  imagen_url  VARCHAR(500)     NULL,
  created_at  TIMESTAMP        NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_prendas_usuario
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  KEY ix_prendas_usuario (usuario_id),
  KEY ix_prendas_categoria (categoria),
  KEY ix_prendas_color (color)
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------
-- TABLA: etiquetas
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS etiquetas (
  id      BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre  VARCHAR(100) NOT NULL,
  tipo    VARCHAR(50)  NULL,
  UNIQUE KEY ux_etiquetas_nombre_tipo (nombre, tipo)
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------
-- TABLA puente: prenda_etiqueta (N:M)
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS prenda_etiqueta (
  prenda_id   BIGINT UNSIGNED NOT NULL,
  etiqueta_id BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (prenda_id, etiqueta_id),
  CONSTRAINT fk_pe_prenda   FOREIGN KEY (prenda_id)  REFERENCES prendas(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_pe_etiqueta FOREIGN KEY (etiqueta_id) REFERENCES etiquetas(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------
-- TABLA: looks
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS looks (
  id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  usuario_id  BIGINT UNSIGNED NOT NULL,
  nombre      VARCHAR(120)     NOT NULL,
  descripcion TEXT             NULL,
  created_at  TIMESTAMP        NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_looks_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  KEY ix_looks_usuario (usuario_id)
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------
-- TABLA puente: look_items
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS look_items (
  look_id   BIGINT UNSIGNED NOT NULL,
  prenda_id BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (look_id, prenda_id),
  CONSTRAINT fk_li_look   FOREIGN KEY (look_id)   REFERENCES looks(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_li_prenda FOREIGN KEY (prenda_id) REFERENCES prendas(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------
-- TABLA: calendario_eventos
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS calendario_eventos (
  id         BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  usuario_id BIGINT UNSIGNED NOT NULL,
  fecha      DATE             NOT NULL,
  look_id    BIGINT UNSIGNED NULL,
  notas      VARCHAR(255)     NULL,
  CONSTRAINT fk_ce_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_ce_look FOREIGN KEY (look_id) REFERENCES looks(id)
    ON DELETE SET NULL ON UPDATE CASCADE,
  KEY ix_ce_usuario_fecha (usuario_id, fecha)
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------
-- TABLA: recomendaciones
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS recomendaciones (
  id         BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  usuario_id BIGINT UNSIGNED NOT NULL,
  look_id    BIGINT UNSIGNED NOT NULL,
  score      DECIMAL(5,2)     NOT NULL DEFAULT 0.00,
  fecha      TIMESTAMP        NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_rec_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_rec_look FOREIGN KEY (look_id) REFERENCES looks(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  KEY ix_rec_usuario_fecha (usuario_id, fecha)
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------
-- TABLA: comentarios
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS comentarios (
  id         BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  usuario_id BIGINT UNSIGNED NOT NULL,
  look_id    BIGINT UNSIGNED NOT NULL,
  texto      TEXT             NOT NULL,
  fecha      TIMESTAMP        NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_com_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_com_look FOREIGN KEY (look_id) REFERENCES looks(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  KEY ix_com_look_fecha (look_id, fecha)
) ENGINE=InnoDB;

-- ---------------------------------------------------------------------
-- TABLA: votos
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS votos (
  id         BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  usuario_id BIGINT UNSIGNED NOT NULL,
  look_id    BIGINT UNSIGNED NOT NULL,
  valor      TINYINT          NOT NULL,
  fecha      TIMESTAMP        NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_vot_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_vot_look FOREIGN KEY (look_id) REFERENCES looks(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  UNIQUE KEY ux_voto_unico (usuario_id, look_id)
) ENGINE=InnoDB;

-- =====================================================================
-- DATOS DE EJEMPLO (mínimos)
-- =====================================================================

INSERT INTO usuarios (nombre, email, password_hash, rol, plan) VALUES
('Andrea Tena Fernández', 'andrea@example.com', 'HASH_EJEMPLO', 'administrador', 'premium'),
('Usuario Demo', 'demo@example.com', 'HASH_EJEMPLO_2', 'usuario', 'free');

INSERT INTO prendas (usuario_id, categoria, color, estilo, temporada, imagen_url) VALUES
(1, 'parte_superior', 'blanco', 'casual', 'verano', 'https://res.cloudinary.com/demo/top1.jpg'),
(1, 'pantalon',       'azul',   'casual', 'todas',  'https://res.cloudinary.com/demo/pants1.jpg'),
(1, 'calzado',        'blanco', 'casual', 'todas',  'https://res.cloudinary.com/demo/shoes1.jpg');

INSERT INTO etiquetas (nombre, tipo) VALUES
('blanco', 'color'),
('azul', 'color'),
('casual', 'estilo'),
('verano', 'temporada');

INSERT INTO prenda_etiqueta (prenda_id, etiqueta_id) VALUES
(1, 1),
(2, 2),
(1, 3), (2, 3), (3, 3),
(1, 4);

INSERT INTO looks (usuario_id, nombre, descripcion) VALUES
(1, 'Look casual verano', 'Top blanco + pantalón azul + zapatillas blancas');

INSERT INTO look_items (look_id, prenda_id) VALUES
(1, 1), (1, 2), (1, 3);

INSERT INTO calendario_eventos (usuario_id, fecha, look_id, notas) VALUES
(1, DATE_ADD(CURDATE(), INTERVAL 1 DAY), 1, 'Salida informal');

INSERT INTO comentarios (usuario_id, look_id, texto) VALUES
(2, 1, '¡Me encanta este look!');

INSERT INTO votos (usuario_id, look_id, valor) VALUES
(2, 1, 1);

INSERT INTO recomendaciones (usuario_id, look_id, score) VALUES
(1, 1, 0.95);