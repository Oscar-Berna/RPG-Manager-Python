CREATE DATABASE IF NOT EXISTS rpg_manager;
USE rpg_manager;

CREATE TABLE IF NOT EXISTS personaje (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    clase VARCHAR(20) NOT NULL,
    nivel INT DEFAULT 1,
    vida DOUBLE DEFAULT 100,
    vida_maxima DOUBLE DEFAULT 100,
    ataque INT DEFAULT 10,
    defensa INT DEFAULT 5
);

INSERT INTO personaje (nombre, clase, nivel, vida, vida_maxima, ataque, defensa) VALUES
('Aragorn', 'Guerrero', 5, 100, 100, 18, 12),
('Gandalf', 'Mago', 8, 70, 70, 28, 5),
('Legolas', 'Arquero', 6, 85, 85, 22, 8);
