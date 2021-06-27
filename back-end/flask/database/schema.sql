DROP database IF EXISTS `BSDB`;
CREATE database `BSDB` charset utf8;

USE `BSDB`;

DROP TABLE IF EXISTS `tb_data`;
DROP TABLE IF EXISTS `tb_facility`;
DROP TABLE IF EXISTS `tb_own`;
DROP TABLE IF EXISTS `tb_user`;

CREATE TABLE `tb_facility` (
  `id` varchar(10) NOT NULL,
  `name` varchar(30) NOT NULL,
  `type` enum('temp','humi','bodyt','rate') NOT NULL,
  `status` enum('online','offline','error') NOT NULL,
  `unit` varchar(10) NOT NULL,
  `step` decimal(4,2) NOT NULL,
  `wardID` varchar(10) DEFAULT NULL,
  `bedID` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `tb_data` (
  `id` varchar(10) NOT NULL,
  `time` datetime NOT NULL,
  `location_lat` decimal(9,6) NOT NULL,
  `location_lng` decimal(9,6) NOT NULL,
  `type` enum('normal','warning') NOT NULL,
  `amount` decimal(5,2) NOT NULL,
  `facID` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `facID` (`facID`),
  CONSTRAINT `tb_data_ibfk_1` FOREIGN KEY (`facID`) REFERENCES `tb_facility` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `tb_user` (
  `id` varchar(10) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `passwd` varchar(30) NOT NULL,
  `role` enum('doctor','patient','manager') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `tb_own` (
  `id` varchar(10) NOT NULL,
  `wardID` varchar(10) NOT NULL,
  `bedID` varchar(10) NOT NULL,
  `userID` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userID` (`userID`),
  CONSTRAINT `tb_own_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `tb_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;