CREATE DATABASE  IF NOT EXISTS `concrete6` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `concrete6`;
-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: concrete6
-- ------------------------------------------------------
-- Server version	5.7.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE TABLE `StateHistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Код записи',
  `uid` int(11) NOT NULL COMMENT 'код оборудования',
  `state` int(11) NOT NULL COMMENT 'Состояние',
  `ts_on` timestamp NULL DEFAULT NULL COMMENT 'Момент начала состояния',
  `ts_off` timestamp NULL DEFAULT NULL COMMENT 'Момент окончания состояния',
  `comment_on` varchar(256) DEFAULT NULL COMMENT 'Комментарии (всякое разное)',
  `comment_off` varchar(256) DEFAULT NULL,
  `durance` int(11) DEFAULT '0' COMMENT 'Длительность в мсек',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=705081 DEFAULT CHARSET=utf8;

CREATE TABLE `StateUIDs` (
  `uid` int(11) NOT NULL COMMENT 'UID из StateHistory',
  `description` varchar(64) NOT NULL COMMENT 'Текстовое описание UID\n',
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `Alarms` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID записи',
  `userID` int(11) DEFAULT NULL COMMENT 'ID пользователя в программе (внутренний)',
  `user` varchar(45) DEFAULT NULL COMMENT 'Пользователь (Системы)',
  `group` varchar(255) DEFAULT NULL COMMENT 'Группа сигнализации',
  `ts_on` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Регистрация сигнализации',
  `ts_off` timestamp NULL DEFAULT NULL COMMENT 'Возврат в норму/подтверждение',
  `message` varchar(256) DEFAULT NULL COMMENT 'Описание сигнализации',
  `details_on` varchar(256) DEFAULT NULL COMMENT 'Подробная информация о моменте возникновения сигнализации',
  `details_off` varchar(256) DEFAULT NULL COMMENT 'Подробная информация о моменте возврате в норму сигнализации',
  `tag` text COMMENT 'Пользовательская информация об сигнализации',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `Events` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID записи',
  `ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `description` text NOT NULL COMMENT 'Комментарий события (текстовое/html описание) ',
  `group` varchar(255) DEFAULT NULL COMMENT 'Группа события',
  `user` varchar(45) DEFAULT NULL COMMENT 'Пользователь (Системы)',
  `userID` int(11) DEFAULT NULL COMMENT 'ID пользователя в программе (внутренний)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

--
-- Table structure for table `Batches`
--

DROP TABLE IF EXISTS `Batches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Batches` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `requestID` int(11) NOT NULL COMMENT 'код заявки',
  `complete` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'время внесения записи',
  `weight` double DEFAULT '0',
  `target` double DEFAULT '0',
  `volume` double DEFAULT '0',
  `reologySVG` blob COMMENT 'График тока двигателя',
  `manual` TINYINT(1) COMMENT 'Ручное вмешательство',
  `current` double DEFAULT NULL COMMENT 'Ток при выгрузке',
  `humidity` double DEFAULT NULL COMMENT 'Влажность при выгрузке',
  `faults` INT DEFAULT NULL COMMENT 'Количество нештатных ситуаций',
  PRIMARY KEY (`id`),
  KEY `fk_Batches_Requests` (`requestID`),
  CONSTRAINT `fk_Batches_Requests` FOREIGN KEY (`requestID`) REFERENCES `Requests` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Batches`
--

LOCK TABLES `Batches` WRITE;
/*!40000 ALTER TABLE `Batches` DISABLE KEYS */;
/*!40000 ALTER TABLE `Batches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BatchesCompositions`
--

DROP TABLE IF EXISTS `BatchesCompositions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BatchesCompositions` (
  `batchID` int(11) NOT NULL,
  `componentID` int(11) NOT NULL,
  `m` double(11,2) NOT NULL DEFAULT '0.00',
  `target` double(11,2) DEFAULT NULL,
  `request_id` int(11) DEFAULT NULL COMMENT 'Заказ',
  `humidity` double DEFAULT NULL COMMENT 'Влажность',
  KEY `fk_BatchesCompositions_Compositions` (`componentID`),
  KEY `fk_BatchesCompositions_Batches` (`batchID`),
  CONSTRAINT `fk_BatchesCompositions_Batches` FOREIGN KEY (`batchID`) REFERENCES `Batches` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_BatchesCompositions_Compositions` FOREIGN KEY (`componentID`) REFERENCES `Components` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BatchesCompositions`
--

LOCK TABLES `BatchesCompositions` WRITE;
/*!40000 ALTER TABLE `BatchesCompositions` DISABLE KEYS */;
/*!40000 ALTER TABLE `BatchesCompositions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Clients`
--

DROP TABLE IF EXISTS `Clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Clients` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shortName` varchar(45) DEFAULT NULL,
  `longName` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Clients`
--

LOCK TABLES `Clients` WRITE;
/*!40000 ALTER TABLE `Clients` DISABLE KEYS */;
/*!40000 ALTER TABLE `Clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ComponentTypes`
--

DROP TABLE IF EXISTS `ComponentTypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ComponentTypes` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Уникальный идентификатор записи',
  `type` int(11) DEFAULT NULL COMMENT 'Значения поля type (Из Components.type)',
  `shortName` varchar(45) DEFAULT NULL COMMENT 'Короткое название',
  PRIMARY KEY (`id`),
  UNIQUE KEY `type_UNIQUE` (`type`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ComponentTypes`
--

LOCK TABLES `ComponentTypes` WRITE;
/*!40000 ALTER TABLE `ComponentTypes` DISABLE KEYS */;
INSERT INTO `ComponentTypes` VALUES (1,0,'ЦЕМЕНТ'),(2,1,'КРУПНЫЙ НАПОЛНИТЕЛЬ'),(3,2,'МЕЛКИЙ НАПОЛНИТЕЛЬ'),(4,3,'ВОДА'),(5,4,'ХД');
/*!40000 ALTER TABLE `ComponentTypes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Components`
--

DROP TABLE IF EXISTS `Components`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Components` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shortName` varchar(45) DEFAULT NULL COMMENT 'краткое название компонента',
  `deleted` tinyint(1) DEFAULT '0' COMMENT 'маркер что компонент не используется',
  `type` int(11) DEFAULT '-1' COMMENT 'Тип/Класс компонента\nБывает цемент, крупны инертные, мелкие инертные, вода, добавка',
  `k` double(5,3) DEFAULT '0.000' COMMENT 'коэффициент запесоченности/загравийности',
  `humidity` double(5,3) DEFAULT '0.000' COMMENT 'влажность (для инертных)',
  `accumulating` tinyint(1) DEFAULT '0',
  `total` double(10,3) DEFAULT '0.000',
  `rho` double DEFAULT '0',
  `mtv` double DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Components`
--

LOCK TABLES `Components` WRITE;
/*!40000 ALTER TABLE `Components` DISABLE KEYS */;
/*!40000 ALTER TABLE `Components` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Compositions`
--

DROP TABLE IF EXISTS `Compositions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Compositions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `receiptID` int(11) NOT NULL,
  `componentID` int(11) NOT NULL,
  `m` double(11,2) DEFAULT '0.00',
  `order` int(11) DEFAULT '-1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniqueReceiptComponent` (`receiptID`,`componentID`),
  KEY `fk_Compositions_Components` (`componentID`),
  KEY `fk_Compositions_Receipts` (`receiptID`),
  CONSTRAINT `fk_Compositions_Components` FOREIGN KEY (`componentID`) REFERENCES `Components` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Compositions_Receipts` FOREIGN KEY (`receiptID`) REFERENCES `Receipts` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Compositions`
--

LOCK TABLES `Compositions` WRITE;
/*!40000 ALTER TABLE `Compositions` DISABLE KEYS */;
/*!40000 ALTER TABLE `Compositions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ContainersBalance`
--

DROP TABLE IF EXISTS `ContainersBalance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ContainersBalance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `deleted` tinyint(4) NOT NULL DEFAULT '0',
  `ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `operator` varchar(128) NOT NULL DEFAULT 'система',
  `lineId` int(11) NOT NULL DEFAULT -1,
  `containerId` int(11) NOT NULL,
  `debet` double DEFAULT NULL,
  `credit` double DEFAULT NULL,
  `comment` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ContainersBalance`
--

LOCK TABLES `ContainersBalance` WRITE;
/*!40000 ALTER TABLE `ContainersBalance` DISABLE KEYS */;
/*!40000 ALTER TABLE `ContainersBalance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MixersInfo`
--

DROP TABLE IF EXISTS `MixersInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MixersInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '№ записи',
  `line` int(11) NOT NULL COMMENT 'Код линии',
  `mixer` int(11) NOT NULL COMMENT 'Код смесителя',
  `shortName` varchar(45) DEFAULT NULL COMMENT 'Наименование смесителя',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MixersInfo`
--

LOCK TABLES `MixersInfo` WRITE;
/*!40000 ALTER TABLE `MixersInfo` DISABLE KEYS */;
INSERT INTO `MixersInfo` VALUES (1,0,0,'СМ-1');
/*!40000 ALTER TABLE `MixersInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Receipts`
--

DROP TABLE IF EXISTS `Receipts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Receipts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shortName` varchar(45) DEFAULT NULL,
  `group` varchar(45) DEFAULT NULL COMMENT 'группа, например\nраствор/бетон',
  `number` varchar(15) DEFAULT NULL,
  `rho` decimal(10,0) DEFAULT '0',
  `rclass` varchar(15) DEFAULT NULL,
  `fsize` varchar(45) DEFAULT NULL,
  `mobility` varchar(45) DEFAULT NULL,
  `humidity` decimal(10,0) DEFAULT '0',
  `brand` varchar(45) DEFAULT NULL,
  `mixT` int(11) DEFAULT NULL COMMENT 'время перемешивания в секундах',
  `unloadT` int(11) DEFAULT NULL COMMENT 'время выгрузки в секундах',
  `deleted` tinyint(1) DEFAULT '0',
  `waterAdd` double DEFAULT NULL COMMENT 'долив воды',
  `capacity` double DEFAULT NULL COMMENT 'вместимость смесителя под этот состав',
  `disabled` tinyint(1) DEFAULT '0',
  `noreport` tinyint(1) DEFAULT '0',
  `frostResistance` varchar(45) DEFAULT '' COMMENT 'Морозостойкость',
  `waterProof` varchar(45) DEFAULT '' COMMENT 'Водонепроницаемость',
  `waterT` double DEFAULT '0' COMMENT 'Температура воды на приготовление',
  `fillersM` double DEFAULT '0',
  `minC` double DEFAULT NULL COMMENT 'Минимальный ток смесителя',
  `maxC` double DEFAULT NULL COMMENT 'Максимальный ток смесителя',
  `waterPart` double DEFAULT NULL COMMENT 'Часть воды, которую можно налить',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Receipts`
--

LOCK TABLES `Receipts` WRITE;
/*!40000 ALTER TABLE `Receipts` DISABLE KEYS */;
/*!40000 ALTER TABLE `Receipts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Requests`
--

DROP TABLE IF EXISTS `Requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Requests` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'код заявки',
  `machine` varchar(45) DEFAULT NULL COMMENT 'гос номер машины',
  `receiptID` int(11) NOT NULL COMMENT 'код рецепта',
  `clientID` int(11) DEFAULT NULL COMMENT 'код клиента',
  `volume` double(11,2) DEFAULT NULL COMMENT 'объем заявки',
  `closed` tinyint(1) DEFAULT '0' COMMENT 'флаг завершенности заявки (больше не требует обработки)',
  `accepted` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'время поступления заявки в очередь',
  `started` datetime DEFAULT NULL COMMENT 'время начала выполнения заявки',
  `finished` datetime DEFAULT NULL COMMENT 'время закрытия заявки',
  `state` int(1) DEFAULT '2' COMMENT 'состояние заказа\n0 - в работе\n1 - остановлен\n2 - в очереди\n3 - закончен',
  `line` int(1) DEFAULT '0',
  `mixer` int(1) DEFAULT '-1' COMMENT 'номер смесителя, которому поручено выполнять заявку',
  `queued` timestamp NULL DEFAULT NULL,
  `mixT` int(11) DEFAULT NULL,
  `unloadT` int(11) DEFAULT NULL,
  `batch_volume` double DEFAULT NULL COMMENT 'Объем одного замеса',
  `refId` VARCHAR(128) DEFAULT NULL COMMENT 'Связанный Документ 1С',
  PRIMARY KEY (`id`),
  KEY `fk_Requests_Receipts` (`receiptID`),
  KEY `fk_Requests_Clients` (`clientID`),
  CONSTRAINT `fk_Requests_Clients` FOREIGN KEY (`clientID`) REFERENCES `Clients` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Requests_Receipts` FOREIGN KEY (`receiptID`) REFERENCES `Receipts` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Requests`
--

LOCK TABLES `Requests` WRITE;
/*!40000 ALTER TABLE `Requests` DISABLE KEYS */;
/*!40000 ALTER TABLE `Requests` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `concrete6`.`Requests_AFTER_INSERT` AFTER INSERT ON `Requests` FOR EACH ROW
BEGIN
INSERT INTO RequestsCompositions (request_id,component_id,m,mpu,k,humidity) 
		SELECT NEW.id,cs.`componentID`,cs.`m`,cs.`m`,c.`k`,c.`humidity` 
        FROM Compositions cs INNER JOIN Components c ON (cs.`componentID`=c.`id`) 
        WHERE cs.`receiptID`=NEW.`receiptID`;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `RequestsCompositions`
--

DROP TABLE IF EXISTS `RequestsCompositions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RequestsCompositions` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id записи',
  `request_id` int(11) NOT NULL COMMENT 'id заявки',
  `component_id` int(11) NOT NULL COMMENT 'id компонента',
  `m` double NOT NULL COMMENT 'Кол-во по составу на момент создания заказа',
  `mpb` double DEFAULT NULL COMMENT 'Итоговая дозировка на 1 замес',
  `mpu` double DEFAULT NULL,
  `k` double DEFAULT NULL COMMENT 'Параметр k компонента',
  `humidity` double DEFAULT NULL COMMENT 'Влажность на момент приготовления',
  `comments` varchar(255) DEFAULT NULL COMMENT 'Для пояснений',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RequestsCompositions`
--

LOCK TABLES `RequestsCompositions` WRITE;
/*!40000 ALTER TABLE `RequestsCompositions` DISABLE KEYS */;
/*!40000 ALTER TABLE `RequestsCompositions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `requeststotals`
--

DROP TABLE IF EXISTS `RequestsTotals`;
/*!50001 DROP VIEW IF EXISTS `RequestsTotals`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `RequestsTotals` AS SELECT 
 1 AS `request_id`,
 1 AS `component_id`,
 1 AS `m`,
 1 AS `target`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `validcomponents`
--

DROP TABLE IF EXISTS `ValidComponents`;
/*!50001 DROP VIEW IF EXISTS `ValidComponents`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `ValidComponents` AS SELECT 
 1 AS `id`,
 1 AS `shortName`,
 1 AS `deleted`,
 1 AS `type`,
 1 AS `k`,
 1 AS `humidity`,
 1 AS `accumulating`,
 1 AS `total`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping events for database 'concrete6'
--

--
-- Dumping routines for database 'concrete6'
--

--
-- Final view structure for view `requeststotals`
--

/*!50001 DROP VIEW IF EXISTS `RequestsTotals`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `RequestsTotals` AS select `r`.`id` AS `request_id`,`rc`.`component_id` AS `component_id`,sum(`bc`.`m`) AS `m`,(sum(`rc`.`mpu`) * `r`.`volume`) AS `target` from (`Requests` `r` join (`RequestsCompositions` `rc` join `BatchesCompositions` `bc`) on(((`r`.`id` = `rc`.`request_id`) and (`bc`.`componentID` = `rc`.`component_id`) and (`bc`.`request_id` = `r`.`id`)))) group by `request_id`,`rc`.`component_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `validcomponents`
--

/*!50001 DROP VIEW IF EXISTS `ValidComponents`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `ValidComponents` AS select `c`.`id` AS `id`,`c`.`shortName` AS `shortName`,`c`.`deleted` AS `deleted`,`c`.`type` AS `type`,`c`.`k` AS `k`,`c`.`humidity` AS `humidity`,`c`.`accumulating` AS `accumulating`,`c`.`total` AS `total` from `Components` c where (`c`.`deleted` = 0) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-06 13:22:04

CREATE USER operator;
GRANT ALL PRIVILEGES ON concrete6.* to operator;
