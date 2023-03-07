/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - mainproject
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`mainproject` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `mainproject`;

/*Table structure for table `addbike` */

DROP TABLE IF EXISTS `addbike`;

CREATE TABLE `addbike` (
  `vid` int(11) NOT NULL AUTO_INCREMENT,
  `mile` varchar(20) DEFAULT NULL,
  `model` int(11) DEFAULT NULL,
  `loc` varchar(110) DEFAULT NULL,
  `name` varchar(110) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `desc` text,
  `img` varchar(110) DEFAULT NULL,
  PRIMARY KEY (`vid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `addbike` */

insert  into `addbike`(`vid`,`mile`,`model`,`loc`,`name`,`price`,`desc`,`img`) values 
(1,'25 km',2021,'Pookkayil','Yamaha R15 V-3',210000,'Speed','20221222164424.jpg'),
(2,'50 km',2022,'Tirur','Yamaha M T-15',130000,'Good','20221222164721.jpg');

/*Table structure for table `bike_list` */

DROP TABLE IF EXISTS `bike_list`;

CREATE TABLE `bike_list` (
  `blid` int(11) NOT NULL AUTO_INCREMENT,
  `bname` varchar(220) DEFAULT NULL,
  PRIMARY KEY (`blid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `bike_list` */

/*Table structure for table `bike_model` */

DROP TABLE IF EXISTS `bike_model`;

CREATE TABLE `bike_model` (
  `bmid` int(11) NOT NULL AUTO_INCREMENT,
  `model_name` varchar(200) DEFAULT NULL,
  `bm_price` int(11) DEFAULT NULL,
  PRIMARY KEY (`bmid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `bike_model` */

insert  into `bike_model`(`bmid`,`model_name`,`bm_price`) values 
(2,'dvshdhj-gdgswku',120000);

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `bbil` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `name` varchar(220) DEFAULT NULL,
  `phone` int(15) DEFAULT NULL,
  `email` varchar(110) DEFAULT NULL,
  `address` varchar(330) DEFAULT NULL,
  `model` varchar(110) DEFAULT NULL,
  PRIMARY KEY (`bbil`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

/*Table structure for table `contact` */

DROP TABLE IF EXISTS `contact`;

CREATE TABLE `contact` (
  `cid` int(10) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `name` varchar(60) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `sub` varchar(50) DEFAULT NULL,
  `mess` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `contact` */

insert  into `contact`(`cid`,`lid`,`name`,`email`,`sub`,`mess`) values 
(1,5,'musfir','povettom@gmail.com','action','asfas'),
(2,6,'akshay','earthworld1374@gmail.com','Service related complaint','wertyuiop[sdfghjkl');

/*Table structure for table `emi` */

DROP TABLE IF EXISTS `emi`;

CREATE TABLE `emi` (
  `emid` int(11) NOT NULL AUTO_INCREMENT,
  `pers_emi` int(111) DEFAULT NULL,
  PRIMARY KEY (`emid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `emi` */

insert  into `emi`(`emid`,`pers_emi`) values 
(4,12);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'admin','123','admin'),
(3,'abhi','123','user'),
(4,'admin12','12','admin'),
(6,'akshay','123','user'),
(8,'akshay','12','user'),
(10,'nihal','123','user');

/*Table structure for table `offer` */

DROP TABLE IF EXISTS `offer`;

CREATE TABLE `offer` (
  `offid` int(11) NOT NULL AUTO_INCREMENT,
  `offname` varchar(110) DEFAULT NULL,
  `oimg` varchar(220) DEFAULT NULL,
  `oname` varchar(110) DEFAULT NULL,
  `oprice` int(11) DEFAULT NULL,
  `omile` int(11) DEFAULT NULL,
  `oyear` int(11) DEFAULT NULL,
  `otorq` int(11) DEFAULT NULL,
  `occ` int(11) DEFAULT NULL,
  PRIMARY KEY (`offid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `offer` */

insert  into `offer`(`offid`,`offname`,`oimg`,`oname`,`oprice`,`omile`,`oyear`,`otorq`,`occ`) values 
(1,'SUPER OFFER','20221223110838.jpg','Yamaha M T-15',119999,50,2022,30,150);

/*Table structure for table `select_service` */

DROP TABLE IF EXISTS `select_service`;

CREATE TABLE `select_service` (
  `ssid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `s_email` varchar(110) DEFAULT NULL,
  `modelname` varchar(110) DEFAULT NULL,
  `regno` varchar(110) DEFAULT NULL,
  `stype` varchar(110) DEFAULT NULL,
  `date` varchar(110) DEFAULT NULL,
  `time` varchar(110) DEFAULT NULL,
  PRIMARY KEY (`ssid`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

/*Data for the table `select_service` */

insert  into `select_service`(`ssid`,`lid`,`s_email`,`modelname`,`regno`,`stype`,`date`,`time`) values 
(5,2,'elitemot7@gmail.com','v3','asdfghj','Engin repair','2023-01-18','11:30-AM'),
(7,6,'darkdestroy555@gmail.com','v3','1234213412q','Physicsl dameges','2023-02-23','1:30-PM'),
(8,6,'darkdestroy555@gmail.com','Yamaha R15 V-3','1234213412','Break repair','2023-02-27','10:00-AM'),
(9,3,'povettom@gmail.com','Yamaha M T-15','KL 55 AD 6765','Engin repair','0000-00-00','3:00-PM'),
(13,3,'povettom@gmail.com','Yamaha R15 V-3','KL 55 AD 6765','Break repair','15','10:00-AM'),
(24,3,'darkdestroy555@gmail.com','MMT','fef','Break repair','2023-03-06','10:00-AM'),
(25,3,'povettom@gmail.com','Yamaha R15 V-3','4567890xsj','Engin repair','2023-03-06','10:00-AM'),
(26,3,'darkdestroy555@gmail.com','MMT','fef','Break repair','2023-02-28','10:00-AM');

/*Table structure for table `slots` */

DROP TABLE IF EXISTS `slots`;

CREATE TABLE `slots` (
  `slid` int(11) NOT NULL AUTO_INCREMENT,
  `sl_date` varchar(220) DEFAULT NULL,
  `slots` int(11) DEFAULT NULL,
  PRIMARY KEY (`slid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `slots` */

insert  into `slots`(`slid`,`sl_date`,`slots`) values 
(1,'2023-02-27',20),
(3,'2023-02-28',23),
(4,'2023-03-31',14),
(6,'2023-03-06',0);

/*Table structure for table `test` */

DROP TABLE IF EXISTS `test`;

CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `test` */

insert  into `test`(`id`,`name`) values 
(1,'anees'),
(2,'rehman');

/*Table structure for table `testdrive` */

DROP TABLE IF EXISTS `testdrive`;

CREATE TABLE `testdrive` (
  `tdid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `tdname` varchar(110) DEFAULT NULL,
  `tdtime` varbinary(110) DEFAULT NULL,
  `tddate` date DEFAULT NULL,
  PRIMARY KEY (`tdid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `testdrive` */

insert  into `testdrive`(`tdid`,`lid`,`tdname`,`tdtime`,`tddate`) values 
(1,3,'Yamaha M T-15','2:00-PM','2022-12-31'),
(2,6,'Yamaha M T-15','11:00-AM','2022-12-16');

/*Table structure for table `trending` */

DROP TABLE IF EXISTS `trending`;

CREATE TABLE `trending` (
  `trid` int(11) NOT NULL AUTO_INCREMENT,
  `trname` varchar(220) DEFAULT NULL,
  `trimg` varchar(220) DEFAULT NULL,
  PRIMARY KEY (`trid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `trending` */

insert  into `trending`(`trid`,`trname`,`trimg`) values 
(1,'Royal Enfield','20221224101759.jpg');

/*Table structure for table `upload` */

DROP TABLE IF EXISTS `upload`;

CREATE TABLE `upload` (
  `upild` int(11) NOT NULL AUTO_INCREMENT,
  `bbil` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `aadar` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`upild`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `upload` */

insert  into `upload`(`upild`,`bbil`,`name`,`phone`,`email`,`address`,`photo`,`aadar`) values 
(1,1,'mus',123,'earthworld1374@gmail.com','xscdvf','20230128194826.jpg','20230128194826.jpg');

/*Table structure for table `user_reg` */

DROP TABLE IF EXISTS `user_reg`;

CREATE TABLE `user_reg` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `phone` int(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `user_reg` */

insert  into `user_reg`(`uid`,`lid`,`name`,`phone`,`email`) values 
(2,3,'abhi',123456,'abhi@gmail.com'),
(4,6,'akshay',12345654,'flutterdart303@gmail.com'),
(6,8,'akshayhhj',12345654,'flutterdart303@gmail.com'),
(8,10,'nihal',12345678,'nihal1999.ae@gmail.com');

/* Procedure structure for procedure `getPatientDetails` */

/*!50003 DROP PROCEDURE IF EXISTS  `getPatientDetails` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`localhost` PROCEDURE `getPatientDetails`(IN `inp` VARCHAR(50))
    NO SQL
SELECT pname,pphone,srfid,bedtype,paddress FROM bookingpatient WHERE hcode=inp */$$
DELIMITER ;

/* Procedure structure for procedure `getUsers` */

/*!50003 DROP PROCEDURE IF EXISTS  `getUsers` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`localhost` PROCEDURE `getUsers`()
    NO SQL
SELECT * FROM user */$$
DELIMITER ;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
