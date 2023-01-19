--CREATE DATABASE courses_app;

--USE courses_app;

CREATE TABLE `instructors` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) DEFAULT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `courses` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) DEFAULT NULL,
    `description` VARCHAR(255) DEFAULT NULL,
    `instructor_id` INT NOT NULL,
    `start_date` DATE DEFAULT NULL,
    `duration` INT DEFAULT NULL,
    `price` INT DEFAULT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`instructor_id`) REFERENCES `instructors`(`id`)
);