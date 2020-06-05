CREATE DATABASE  IF NOT EXISTS `employee`;
USE `employee`;

-- Database: employee
-- ------------------------------------------------------

-- Table structure for table `emp`
--

CREATE TABLE `emp` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `sal` decimal(10,0) DEFAULT NULL
) ;
