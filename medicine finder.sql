/*
SQLyog Enterprise - MySQL GUI v8.02 RC
MySQL - 5.5.5-10.4.32-MariaDB : Database - govind
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`govind` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `govind`;

/*Table structure for table `admin_data` */

DROP TABLE IF EXISTS `admin_data`;

CREATE TABLE `admin_data` (
  `namee` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `admin_data` */

insert  into `admin_data`(`namee`,`address`,`contact`,`email`) values ('a1','a1','a1','aa@gmail.com'),('Govind Singh Tanwar\'kota Rajasthan','kota Rajasthan','9660837005','aghsdt323@gmail.com'),('alice everet','D 15 B OLD JAWAHAR NAGAR KOTA RAJASTHAN 324005','9660837005','alice@gmail.com'),('Madhav Sharma','Kansua, Kota, Rajasthan','6262176261','gdhsgd@gmail.com'),('Govind Singh','D 15 B OLD JAWAHAR NAGAR','9660837005','gs343@gmail.com'),('Mohit Sharma','D 15 B OLD JAWAHAR NAGAR KOTA RAJASTHAN 324005','9660025300','madhav4543@gmail.com');

/*Table structure for table `login_data` */

DROP TABLE IF EXISTS `login_data`;

CREATE TABLE `login_data` (
  `email` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `login_data` */

insert  into `login_data`(`email`,`password`,`usertype`) values ('aa@gmail.com','aa','admin'),('ab@gmail.com','aabb','medical'),('aghsdt323@gmail.com','aaa','admin'),('alice@gmail.com','Alice@1','admin'),('c3@gmail.com','cc','medical'),('gdhsgd@gmail.com','123','admin'),('gs343@gmail.com','Govind45454','admin'),('J@GMAIL.COM','JJ','medical'),('jhdtcjh454@gmail.com','kdh765','medical'),('JY@GMAIL.COM','JY','medical'),('M@GMAIL.COM','mm','medical'),('madhav4543@gmail.com','MoHiT3456@67','admin');

/*Table structure for table `medical_data` */

DROP TABLE IF EXISTS `medical_data`;

CREATE TABLE `medical_data` (
  `mname` varchar(100) DEFAULT NULL,
  `owner` varchar(100) DEFAULT NULL,
  `lno` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `photo_medical` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `medical_data` */

insert  into `medical_data`(`mname`,`owner`,`lno`,`address`,`contact`,`email`,`photo_medical`) values ('GOVIND MEDICOZ','Govind Singh','AABB','D-15 Old Jawahar Nagar','9660837005','ab@gmail.com','no'),('Karan Pharmecy','Karan Singh','GS76354278T','dadabari','8642358764','c3@gmail.com',NULL),('JEENA SIKHO LIFECARE','HARSHIL CHATURVEDI','TR556644TRTT','1-D-14 SHEELA CHOUDHARY ROAD','7867564534','J@GMAIL.COM',NULL),('MADHAV MEDICAL  CENTRE','Madhav Sharma','HJ7654938JK','C-16 kansua ','7944364587','jhdtcjh454@gmail.com',NULL),('JYOTI MEDICALS','JYOTI RAJAWAT','7856TFGHY','1-B-27, COMMERCE COLLAGE ROAD,KOTA,RAJASTHAN','8267453782','JY@GMAIL.COM',NULL),('MEDZEPP PHARMACY','HARI SINGH','HJ223399KK','SHOP NO. B, A-11, JAWAH NAGAR,KOTA RAJASTHAN','9876543467','M@GMAIL.COM',NULL);

/*Table structure for table `medicine_data` */

DROP TABLE IF EXISTS `medicine_data`;

CREATE TABLE `medicine_data` (
  `med_id` int(11) NOT NULL AUTO_INCREMENT,
  `med_name` varchar(100) DEFAULT NULL,
  `company` varchar(100) DEFAULT NULL,
  `l_no` varchar(100) DEFAULT NULL,
  `price` double DEFAULT NULL,
  `remark` varchar(100) DEFAULT NULL,
  `email_medical` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`med_id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `medicine_data` */

insert  into `medicine_data`(`med_id`,`med_name`,`company`,`l_no`,`price`,`remark`,`email_medical`) values (1,'UROTONE','SAMARTH LIFE SCIENCE','226655',55,'Place in cool storage','ab@gmail.com'),(3,'ARTEBET','ZEELAM PHARMACY CORPORATIONS','ABC123ABC',9.9,'KEEP AWAY FROM CHILDRENS','ab@gmail.com'),(4,'ACARTEX-25	','JAIN FEB','DEF564DBT',30,'KEEP IN DRY PLACE','ab@gmail.com'),(5,'ASOZEN-SR','ZEELAB PHARMACY	','JKJG784635JHDSJ',12.17,'KEEP IN DRY AND DARK PLACE','ab@gmail.com'),(6,'ACICLOVIR','ASPIRIN','HGDF6565HGFHD',3.7,'KEEP AWAY FROM DIRECT SUNLIGHT','ab@gmail.com'),(7,'GEMFIBROCILS','CIPROBAY','HGFDH7896SHGDJH',98.67,'PLACE AT ROOM TEMPRATURE','ab@gmail.com'),(8,'PARACETAMOL','DOLO','637846',5.5,'KEEP AWAY FROM CHILDRENS','ab@gmail.com'),(9,'DYAPHARM','CIPLA','98364',15,'DONT PLACE IN DIRECT SUNLIGHT','ab@gmail.com'),(10,'PARACETAMOL','DOLO','637846',5.5,'KEEP AWAY FROM CHILDRENS','cd@gmail.com'),(11,'DYAPHARM','CIPLA','98364',15,'DONT PLACE IN DIRECT SUNLIGHT','cd@gmail.com'),(12,'ARTEBET','ZEELAM PHARMACY CORPORATIONS','ABC123ABC',9.9,'KEEP AWAY FROM CHILDRENS','cd@gmail.com'),(13,'ASOZEN-SR','ZEELAM PHARMACY CORPORATIONS','JKJG784635JHDSJ',12.17,'KEEP IN DRY AND DARK PLACE','cd@gmail.com'),(14,'Vitamin D 50','Drisdol','3434',10,'KEEP AWAY FROM CHILDRENS','cd@gmail.com'),(15,'HUMAN MIXTARD','LUPIN',NULL,147,'KEEP IN DRY AND DARK PLACE','cd@gmail.com'),(16,'HUMAN ACTRAPID','LUPIN',NULL,150,'KEEP AWAY FROM CHILDRENS','cd@gmail.com'),(17,'OMEGA 3 FISH OIL','ZEELAM PHARMACY CORPORATIONS','4996',25,'PLACE AT ROOM TEMPRATURE','cd@gmail.com'),(18,'Vitamin D 50','Drisdol','3434',12.17,'KEEP IN DRY AND DARK PLACE','c3@gmail.com'),(19,'Glycopyrrolate','LUPIN','5964',55,'DONT PLACE IN DIRECT SUNLIGHT','c3@gmail.com'),(20,'OMEGA 3 FISH OIL','AEROBINDO PHARMA','466567',3.6,'KEEP AWAY FROM CHILDRENS','c3@gmail.com'),(21,'HUMAN MIXTARD','AEROBINDO PHARMA','434455',147,'PLACE AT COLD STORAGE','c3@gmail.com'),(22,'HUMAN MIXTARD','LUPIN','232323',147,'PLACE AT COLD STORAGE','c3@gmail.com'),(23,'ASOZEN-SR','ZEELAM PHARMACY CORPORATIONS','676778',5.78,'KEEP AWAY FROM CHILDRENS','c3@gmail.com'),(24,'HUMAN ACTRAPID','LUPIN','8675645',150,'PLACE AT COLD STORAGE','c3@gmail.com'),(25,'ARTEBET','ZEELAM PHARMACY CORPORATIONS','54332',10.1,'KEEP IN DRY AND DARK PLACE','c3@gmail.com'),(26,'CODE LIVER OIL','ABBOTT INDIA LTD','6543',199.99,'KEEP AWAY FROM CHILDRENS','c3@gmail.com'),(27,'HUMAN ACTRAPID','LUPIN','8675645',150,'PLACE AT COLD STORAGE','J@GMAIL.COM'),(28,'Glycopyrrolate','LUPIN','5964',55,'DONT PLACE IN DIRECT SUNLIGHT','J@GMAIL.COM'),(29,'Vitamin D 50','LUPIN','3434',23,'KEEP IN DRY AND DARK PLACE','J@GMAIL.COM'),(30,'ACICLOVIR','ASPIRIN','HGDF6565HGFHD',34,'PLACE AT COLD STORAGE','J@GMAIL.COM'),(31,'ASOZEN-SR','ZEELAM PHARMACY CORPORATIONS','676778',5.78,'KEEP AWAY FROM CHILDRENS','J@GMAIL.COM'),(32,'OMEGA 3 FISH OIL','AEROBINDO PHARMA','466567',3.6,'KEEP AWAY FROM CHILDRENS','J@GMAIL.COM'),(33,'ACARTEX-25	','JAIN FEB','DEF564DBT',30,'KEEP IN DRY PLACE','J@GMAIL.COM'),(34,'DYNAFUR','CIPLA','221122',35,'PLACE AT DRY PLACE','J@GMAIL.COM'),(35,'UROTONE','SAMARTH LIFE SCIENCE','226655',55,'Place in cool storage','J@GMAIL.COM'),(36,'HUMAN MIXTARD','AEROBINDO PHARMA','434455',147,'PLACE AT COLD STORAGE','J@GMAIL.COM'),(37,'ARTEBET','ZEELAM PHARMACY CORPORATIONS','54332',10.1,'KEEP IN DRY AND DARK PLACE','J@GMAIL.COM'),(38,'CODE LIVER OIL','ABBOTT INDIA LTD','6543',199.99,'KEEP AWAY FROM CHILDRENS','J@GMAIL.COM'),(48,'UROTONE','SAMARTH LIFE SCIENCE','226655',55,'Place in cool storage','M@GMAIL.COM'),(49,'ARTEBET','ZEELAM PHARMACY CORPORATIONS','ABC123ABC',9.9,'KEEP AWAY FROM CHILDRENS','M@GMAIL.COM'),(50,NULL,NULL,NULL,NULL,NULL,'M@GMAIL.COM'),(51,NULL,NULL,NULL,NULL,NULL,'M@GMAIL.COM'),(52,NULL,NULL,NULL,NULL,NULL,'M@GMAIL.COM'),(53,NULL,NULL,NULL,NULL,NULL,'M@GMAIL.COM'),(54,NULL,NULL,NULL,NULL,NULL,'M@GMAIL.COM'),(55,NULL,NULL,NULL,NULL,NULL,'M@GMAIL.COM'),(56,NULL,NULL,NULL,NULL,NULL,'M@GMAIL.COM'),(57,NULL,NULL,NULL,NULL,NULL,'M@GMAIL.COM');

/*Table structure for table `photo_data` */

DROP TABLE IF EXISTS `photo_data`;

CREATE TABLE `photo_data` (
  `email` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `photo_data` */

insert  into `photo_data`(`email`,`photo`) values ('aa@gmail.com','1719299614.jpg');

/*Table structure for table `st_data` */

DROP TABLE IF EXISTS `st_data`;

CREATE TABLE `st_data` (
  `roll_no` int(11) DEFAULT NULL,
  `namee` varchar(40) DEFAULT NULL,
  `branch` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `st_data` */

insert  into `st_data`(`roll_no`,`namee`,`branch`) values (1001,'Govind Singh','soft'),(1002,'Karan Singh','ELC');

/*Table structure for table `medicine_medical` */

DROP TABLE IF EXISTS `medicine_medical`;

/*!50001 DROP VIEW IF EXISTS `medicine_medical` */;
/*!50001 DROP TABLE IF EXISTS `medicine_medical` */;

/*!50001 CREATE TABLE `medicine_medical` (
  `med_id` int(11) NOT NULL,
  `med_name` varchar(100) DEFAULT NULL,
  `company` varchar(100) DEFAULT NULL,
  `l_no` varchar(100) DEFAULT NULL,
  `price` double DEFAULT NULL,
  `remark` varchar(100) DEFAULT NULL,
  `email_medical` varchar(100) DEFAULT NULL,
  `mname` varchar(100) DEFAULT NULL,
  `owner` varchar(100) DEFAULT NULL,
  `lno` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `contact` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `photo_medical` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci */;

/*View structure for view medicine_medical */

/*!50001 DROP TABLE IF EXISTS `medicine_medical` */;
/*!50001 DROP VIEW IF EXISTS `medicine_medical` */;

/*!50001 CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `medicine_medical` AS (select `medicine_data`.`med_id` AS `med_id`,`medicine_data`.`med_name` AS `med_name`,`medicine_data`.`company` AS `company`,`medicine_data`.`l_no` AS `l_no`,`medicine_data`.`price` AS `price`,`medicine_data`.`remark` AS `remark`,`medicine_data`.`email_medical` AS `email_medical`,`medical_data`.`mname` AS `mname`,`medical_data`.`owner` AS `owner`,`medical_data`.`lno` AS `lno`,`medical_data`.`address` AS `address`,`medical_data`.`contact` AS `contact`,`medical_data`.`email` AS `email`,`medical_data`.`photo_medical` AS `photo_medical` from (`medicine_data` join `medical_data` on(`medicine_data`.`email_medical` = `medical_data`.`email`))) */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
