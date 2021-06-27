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

-- facility
INSERT INTO `tb_facility` VALUES ('10001', '201病房温度监控', 'temp', 'online', 'Celsius', '60', '201', '00');
INSERT INTO `tb_facility` VALUES ('20001', '201病房湿度监控', 'humi', 'online', '%', '60', '201', '00');
INSERT INTO `tb_facility` VALUES ('30011', '201-01床体温', 'bodyt', 'online', 'Celsius', '30', '201', '01');
INSERT INTO `tb_facility` VALUES ('40011', '201-01床心率', 'rate', 'online', 'BPM', '5', '201', '01');
INSERT INTO `tb_facility` VALUES ('30012', '201-02床体温', 'bodyt', 'online', 'Celsius', '30', '201', '02');
INSERT INTO `tb_facility` VALUES ('40012', '201-02床心率', 'rate', 'online', 'BPM', '5', '201', '02');

INSERT INTO `tb_facility` VALUES ('10008', '208病房温度监控', 'temp', 'error', 'Celsius', '60', '208', '00');
INSERT INTO `tb_facility` VALUES ('20008', '208病房湿度监控', 'humi', 'offline', '%', '60', '208', '00');
INSERT INTO `tb_facility` VALUES ('30081', '208-01床体温', 'bodyt', 'offline', 'Celsius', '30', '208', '01');

-- data
INSERT INTO `tb_data` VALUES ('1000101', '2021-06-27 08:20:00', 120.131042, 30.273052, 'normal', '27.1', '10001');
INSERT INTO `tb_data` VALUES ('1000102', '2021-06-27 08:50:00', 120.130642, 30.272852, 'normal', '24.2', '10001');
INSERT INTO `tb_data` VALUES ('1000103', '2021-06-27 09:20:00', 120.132142, 30.272352, 'normal', '26.6', '10001');
INSERT INTO `tb_data` VALUES ('1000104', '2021-06-27 09:50:00', 120.131342, 30.274252, 'normal', '26.8', '10001');
INSERT INTO `tb_data` VALUES ('1000105', '2021-06-27 10:20:00', 120.132042, 30.274052, 'normal', '27.2', '10001');
INSERT INTO `tb_data` VALUES ('1000106', '2021-06-27 10:50:00', 120.131842, 30.274752, 'normal', '26.9', '10001');
INSERT INTO `tb_data` VALUES ('1000107', '2021-06-27 11:20:00', 120.130742, 30.274952, 'normal', '27.8', '10001');
INSERT INTO `tb_data` VALUES ('1000108', '2021-06-27 11:50:00', 120.130642, 30.273552, 'normal', '28.4', '10001');

INSERT INTO `tb_data` VALUES ('2000101', '2021-06-27 08:20:00', 120.131642, 30.273852, 'warning', '00', '20001');
INSERT INTO `tb_data` VALUES ('2000102', '2021-06-27 08:50:00', 120.130342, 30.273252, 'normal', '65', '20001');
INSERT INTO `tb_data` VALUES ('2000103', '2021-06-27 09:20:00', 120.131642, 30.272552, 'normal', '73', '20001');
INSERT INTO `tb_data` VALUES ('2000104', '2021-06-27 09:50:00', 120.130042, 30.272052, 'normal', '72', '20001');
INSERT INTO `tb_data` VALUES ('2000105', '2021-06-27 10:20:00', 120.131042, 30.273052, 'warning', '98', '20001');
INSERT INTO `tb_data` VALUES ('2000106', '2021-06-27 10:50:00', 120.131142, 30.274352, 'normal', '79', '20001');

INSERT INTO `tb_data` VALUES ('3001101', '2021-06-27 8:00:00', 120.133142, 30.274352, 'normal', '36.5', '30011');
INSERT INTO `tb_data` VALUES ('3001102', '2021-06-27 8:30:00', 120.132142, 30.275352, 'normal', '36.8', '30011');

INSERT INTO `tb_data` VALUES ('4001101', '2021-06-27 8:05:00', 120.133142, 30.274460, 'normal', '80', '40011');
INSERT INTO `tb_data` VALUES ('4001102', '2021-06-27 8:10:00', 120.132142, 30.275952, 'normal', '82', '40011');

-- user
INSERT INTO `tb_user` VALUES ('3180105412', 'Yu Ruohan(test_manager)', "3180105412@zju.edu.cn", '123456', 'manager');
INSERT INTO `tb_user` VALUES ('3180101111', 'test_patient', "12345678@example.com", '123456', 'patient');
INSERT INTO `tb_user` VALUES ('3180102222', 'test_doctor', "87654321@example.com", '123456', 'doctor');

-- own
INSERT INTO `tb_own` (`wardID`, `bedID`, `userID`) VALUES ('201', "01", '3180101111');
