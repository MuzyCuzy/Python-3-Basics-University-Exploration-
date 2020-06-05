CREATE DATABASE  IF NOT EXISTS `login`;
USE `login`;

-- Database: login
-- ------------------------------------------------------
-- Table structure for table `password`

CREATE TABLE `password` (
  `name` varchar(50) DEFAULT NULL,
  `pass` varchar(30) DEFAULT NULL
);

INSERT INTO `password` VALUES ('one','one');
