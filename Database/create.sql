CREATE DATABASE IF NOT EXISTS courses_app;

USE courses_app;

CREATE TABLE IF NOT EXISTS `instructors` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) DEFAULT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `courses` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) DEFAULT NULL,
    `description` VARCHAR(255) DEFAULT NULL,
    `instructor_id` INT DEFAULT NULL,
    `start_date` DATE DEFAULT NULL,
    `duration` INT DEFAULT NULL,
    `price` INT DEFAULT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`instructor_id`) REFERENCES `instructors`(`id`)
);