/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - patient_data
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`patient_data` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `patient_data`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add dept_table',7,'add_dept_table'),
(26,'Can change dept_table',7,'change_dept_table'),
(27,'Can delete dept_table',7,'delete_dept_table'),
(28,'Can view dept_table',7,'view_dept_table'),
(29,'Can add doctor_table',8,'add_doctor_table'),
(30,'Can change doctor_table',8,'change_doctor_table'),
(31,'Can delete doctor_table',8,'delete_doctor_table'),
(32,'Can view doctor_table',8,'view_doctor_table'),
(33,'Can add login_table',9,'add_login_table'),
(34,'Can change login_table',9,'change_login_table'),
(35,'Can delete login_table',9,'delete_login_table'),
(36,'Can view login_table',9,'view_login_table'),
(37,'Can add patient_table',10,'add_patient_table'),
(38,'Can change patient_table',10,'change_patient_table'),
(39,'Can delete patient_table',10,'delete_patient_table'),
(40,'Can view patient_table',10,'view_patient_table'),
(41,'Can add medical_record_table',11,'add_medical_record_table'),
(42,'Can change medical_record_table',11,'change_medical_record_table'),
(43,'Can delete medical_record_table',11,'delete_medical_record_table'),
(44,'Can view medical_record_table',11,'view_medical_record_table'),
(45,'Can add hospital_table',12,'add_hospital_table'),
(46,'Can change hospital_table',12,'change_hospital_table'),
(47,'Can delete hospital_table',12,'delete_hospital_table'),
(48,'Can view hospital_table',12,'view_hospital_table'),
(49,'Can add appointment_table',13,'add_appointment_table'),
(50,'Can change appointment_table',13,'change_appointment_table'),
(51,'Can delete appointment_table',13,'delete_appointment_table'),
(52,'Can view appointment_table',13,'view_appointment_table');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(13,'patient_data_app','appointment_table'),
(7,'patient_data_app','dept_table'),
(8,'patient_data_app','doctor_table'),
(12,'patient_data_app','hospital_table'),
(9,'patient_data_app','login_table'),
(11,'patient_data_app','medical_record_table'),
(10,'patient_data_app','patient_table'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-02-11 03:18:39.693928'),
(2,'auth','0001_initial','2024-02-11 03:18:40.612664'),
(3,'admin','0001_initial','2024-02-11 03:18:40.833367'),
(4,'admin','0002_logentry_remove_auto_add','2024-02-11 03:18:40.849379'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-02-11 03:18:40.865305'),
(6,'contenttypes','0002_remove_content_type_name','2024-02-11 03:18:40.975573'),
(7,'auth','0002_alter_permission_name_max_length','2024-02-11 03:18:41.042893'),
(8,'auth','0003_alter_user_email_max_length','2024-02-11 03:18:41.070515'),
(9,'auth','0004_alter_user_username_opts','2024-02-11 03:18:41.085522'),
(10,'auth','0005_alter_user_last_login_null','2024-02-11 03:18:41.183950'),
(11,'auth','0006_require_contenttypes_0002','2024-02-11 03:18:41.198386'),
(12,'auth','0007_alter_validators_add_error_messages','2024-02-11 03:18:41.198386'),
(13,'auth','0008_alter_user_username_max_length','2024-02-11 03:18:41.309353'),
(14,'auth','0009_alter_user_last_name_max_length','2024-02-11 03:18:41.435484'),
(15,'auth','0010_alter_group_name_max_length','2024-02-11 03:18:41.453601'),
(16,'auth','0011_update_proxy_permissions','2024-02-11 03:18:41.467390'),
(17,'auth','0012_alter_user_first_name_max_length','2024-02-11 03:18:41.593692'),
(18,'patient_data_app','0001_initial','2024-02-11 03:18:42.676133'),
(19,'sessions','0001_initial','2024-02-11 03:18:42.737773'),
(20,'patient_data_app','0002_auto_20240211_1000','2024-02-11 04:30:05.682821'),
(21,'patient_data_app','0003_hospital_table_proof','2024-02-16 07:42:33.688472'),
(22,'patient_data_app','0004_patient_table_health_id','2024-03-01 03:16:43.413602'),
(23,'patient_data_app','0005_appointment_table_otp','2024-03-03 04:36:21.530302'),
(24,'patient_data_app','0006_hospital_table_district','2024-03-10 07:35:34.325274');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('91kv34wxsgkot575xmraur4vo7z4sljb','.eJyrVsrJTFGyMtRRSkktKIkHsY10lIpLEtPSYJyUIjDLREcpIy8xN1XJSsmzsCgxUSEjv7ggsyQxR6kWAOkIFfs:1rZSJY:Jb_NA5cSRNt5ZfioCx9ZPADq3z5UKMuCLyZ80PPOYmY','2024-02-26 09:09:24.619306'),
('dxlyfotetd14l8shavngtlm1kn695wcm','.eJyrVsrJTFGyMjHWUcrIS8xNVbJS8iwsSkxUyMgvLsgsScxR0lECKTA001EqSCxJzcwrAXGVDA2BEimpBSXxIK6FjlIpWNgEJFwAFqoFAPsSGt8:1roLl9:N6UjOe-O-jqZpoMMpAoTRc6kY5J6GnnVaiTsd0uR3MQ','2024-04-07 11:11:27.716513'),
('eo80gqh6q9vryg68spm7bch210y6p3tg','eyJsaWQiOjF9:1rd3NO:WGHwhjNgthSgzHtCFhafsAomvawRXqubWOzqnY3WvrI','2024-03-07 07:20:14.347436'),
('jekprt8d8hr6xyi9bkfmrxqznxhkqnan','eyJsaWQiOjEsImhuYW1lIjoibW1jIGhvc3BpdGFsICIsImRlcHRfaWQiOjcsImRyX2lkIjo5fQ:1rd1WJ:B-16BllJ8HfVnoWsyqLwJ-4ST_KAcNcT3Bxn_RjVonE','2024-03-07 05:21:19.901758'),
('ovj307uml3e93wcd5aysv9cmd79q28w1','eyJsaWQiOjEsImhuYW1lIjoiSXFyYWEgaG9zcGl0YWwiLCJkZXB0X2lkIjozLCJkcl9pZCI6NH0:1rathU:4JbHLuXcPylWhsna9eqY5ZKOq9w4RdEJJyTqeOeNesg','2024-03-01 08:36:04.644179'),
('qz652wrzjxsi5xa4ze3xjrd832b7efjs','.eJyrVsrJTFGyMtJRyshLzE1VslLKzU1WyMgvLsgsScxRUNJRKkgsSc3MKwGpUrIA8lNSC0riQTwzILsIzDI00FEC06a1APc7GEU:1rjEym:nzFfuYqK6l5i28tPN11_uDCmpX1K6Kt_3bsdYd-ZLkU','2024-03-24 08:56:24.044912'),
('rw2clf5phdci67ugf3mz3l2tc6ewf8tz','eyJsaWQiOjQsImhuYW1lIjoiSXFyYWEgaG9zcGl0YWwiLCJkZXB0X2lkIjo4LCJkcl9pZCI6NiwicGF0ZWludGlkIjoiOCJ9:1rh8zb:reiRPxA0U5mo3eAgGry5g11sC621wI3M9wjxJPmBc-o','2024-03-18 14:08:35.654909');

/*Table structure for table `patient_data_app_appointment_table` */

DROP TABLE IF EXISTS `patient_data_app_appointment_table`;

CREATE TABLE `patient_data_app_appointment_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` varchar(100) NOT NULL,
  `status` varchar(30) NOT NULL,
  `DOCTOR_id` bigint NOT NULL,
  `PATIENT_id` bigint NOT NULL,
  `otp` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `patient_data_app_app_DOCTOR_id_ed5e34d6_fk_patient_d` (`DOCTOR_id`),
  KEY `patient_data_app_app_PATIENT_id_2e4f875b_fk_patient_d` (`PATIENT_id`),
  CONSTRAINT `patient_data_app_app_DOCTOR_id_ed5e34d6_fk_patient_d` FOREIGN KEY (`DOCTOR_id`) REFERENCES `patient_data_app_doctor_table` (`id`),
  CONSTRAINT `patient_data_app_app_PATIENT_id_2e4f875b_fk_patient_d` FOREIGN KEY (`PATIENT_id`) REFERENCES `patient_data_app_patient_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `patient_data_app_appointment_table` */

insert  into `patient_data_app_appointment_table`(`id`,`date`,`time`,`status`,`DOCTOR_id`,`PATIENT_id`,`otp`) values 
(15,'2024-03-05','13:03','accepted',7,8,6767),
(16,'2024-03-06','13:19','accepted',7,8,5932),
(20,'2024-03-19','12:42','pending',10,15,0),
(21,'2024-03-20','14:00','pending',12,17,0),
(22,'2024-03-28','18:26','accepted',12,8,4540),
(23,'2024-03-27','21:52','pending',8,8,0),
(24,'2024-03-25','19:27','pending',8,8,0),
(25,'2024-03-25','19:27','pending',8,10,0),
(26,'2024-03-25','18:28','pending',8,11,0);

/*Table structure for table `patient_data_app_dept_table` */

DROP TABLE IF EXISTS `patient_data_app_dept_table`;

CREATE TABLE `patient_data_app_dept_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(50) NOT NULL,
  `details` longtext NOT NULL,
  `HOSPITAL_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `patient_data_app_dep_HOSPITAL_id_da41b3fd_fk_patient_d` (`HOSPITAL_id`),
  CONSTRAINT `patient_data_app_dep_HOSPITAL_id_da41b3fd_fk_patient_d` FOREIGN KEY (`HOSPITAL_id`) REFERENCES `patient_data_app_hospital_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `patient_data_app_dept_table` */

insert  into `patient_data_app_dept_table`(`id`,`dept_name`,`details`,`HOSPITAL_id`) values 
(3,'Cardiology Department','The cardiology department is where patients go for the diagnosis and treatment of heart-related conditions, such as heart disease, heart attacks, and arrhythmias. The cardiology department is staffed by cardiologists, nurses, and other healthcare providers who are trained to provide specialized care to patients with heart conditions. The cardiology department is equipped with advanced medical equipment, such as electrocardiograms (ventilators, and neonatal intensive care units.',2),
(4,'Psychiatry Department','The psychiatry department is where patients go for the diagnosis and treatment of mental health conditions, such as depression, anxiety, and bipolar disorder. The psychiatry department is staffed by psychiatrists, psychologists, and other mental health professionals who are trained to provide specialized care to patients with mental health conditions. The psychiatry department is equipped with specialized therapy rooms and other equipment, such as electroconvulsive therapy (ECT) machines.',2),
(5,'Cardiology Department','The cardiology department is where patients go for the diagnosis and treatment of heart-related conditions, such as heart disease, heart attacks, and arrhythmias. The cardiology department is staffed by cardiologists, nurses, and other healthcare providers who are trained to provide specialized care to patients with heart conditions. The cardiology department is equipped with advanced medical equipment, such as electrocardiograms (ventilators, and neonatal intensive care units.',2),
(6,'Oncology','Its for Cancer related ',1),
(7,'Phychiatristry','its for the mental health',1),
(8,'oncology','asdfrtgb',2);

/*Table structure for table `patient_data_app_doctor_table` */

DROP TABLE IF EXISTS `patient_data_app_doctor_table`;

CREATE TABLE `patient_data_app_doctor_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `gender` varchar(35) NOT NULL,
  `dob` date NOT NULL,
  `place` varchar(50) NOT NULL,
  `pin` bigint NOT NULL,
  `post` varchar(30) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(50) NOT NULL,
  `qualification` longtext NOT NULL,
  `specialization` varchar(100) NOT NULL,
  `experience` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `DEPARTMENT_id` bigint NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `patient_data_app_doc_LOGIN_id_2e8c567c_fk_patient_d` (`LOGIN_id`),
  KEY `patient_data_app_doc_DEPARTMENT_id_10c1d6b8_fk_patient_d` (`DEPARTMENT_id`),
  CONSTRAINT `patient_data_app_doc_DEPARTMENT_id_10c1d6b8_fk_patient_d` FOREIGN KEY (`DEPARTMENT_id`) REFERENCES `patient_data_app_dept_table` (`id`),
  CONSTRAINT `patient_data_app_doc_LOGIN_id_2e8c567c_fk_patient_d` FOREIGN KEY (`LOGIN_id`) REFERENCES `patient_data_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `patient_data_app_doctor_table` */

insert  into `patient_data_app_doctor_table`(`id`,`name`,`gender`,`dob`,`place`,`pin`,`post`,`phone`,`email`,`qualification`,`specialization`,`experience`,`photo`,`DEPARTMENT_id`,`LOGIN_id`) values 
(5,'Nadha Najeeb K C','Female','1994-06-18','Elettil ',673572,'Elettil',9207873206,'nadhanjb7@gmail.com','asdfghj','sdfghjk','6 years','IMG_0321.JPG',4,41),
(7,'Najeeb Muhammed','Male','1972-05-10','Elettil',673572,'Elettil',9846279448,'najeebyaz@gmail.com','asdfghjkl','asdfghjk','18 years','hush-naidoo-jade-photography-ZCO_5Y29s8k-unsplash.jpg',3,43),
(8,'Suhara Najeeb','Female','1984-01-16','Elettil',673572,'Elettil',9846743210,'suharanjb09@gmail.com','qwertyuio','asdfghjk','3 years','niranjan-_-photographs-cc32Aoa_n94-unsplash.jpg',4,44),
(10,'Abhinandh','Male','1998-12-15','Kozhikkode',876789,'Kozhikkode',9820787320,'abhinandh06@gmail.com','Phd.oncology','oncologist','3 YEARS','Despite-Low-Confidence-in-Crypto-Bitcoin-Moves-Past-30k_PdFRSdw.jpg',6,55),
(11,'hinu','Female','1998-12-10','asdfgh',897654,'asdfgh',9876545678,'hinu@gmail.com','asdfghj','asdfgh','7 years','system student allo.png',5,59),
(12,'Aiswarya','Female','1998-12-10','Kakkodi',789876,'Kakkodi',7898765643,'aiswarya@gmail.com','Phd.Phychiatristry','Phychiatry','5 years','0_h_bQ78miwT80BFMN.jpg',7,73),
(13,'Muhammed','Male','1998-09-18','Kummanam',897656,'Kummanam',7898765678,'muhammed@gmail.com','Ph.d','oncologist','10 Years','1_Ryci2os9ss3nIMMlmBTmOw.jpg',6,74);

/*Table structure for table `patient_data_app_hospital_table` */

DROP TABLE IF EXISTS `patient_data_app_hospital_table`;

CREATE TABLE `patient_data_app_hospital_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `hosp_name` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `pin` varchar(50) NOT NULL,
  `post` varchar(50) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(50) NOT NULL,
  `license_no` varchar(30) NOT NULL,
  `status` varchar(30) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `proof` varchar(100) NOT NULL,
  `district` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `patient_data_app_hos_LOGIN_id_d590fa5f_fk_patient_d` (`LOGIN_id`),
  CONSTRAINT `patient_data_app_hos_LOGIN_id_d590fa5f_fk_patient_d` FOREIGN KEY (`LOGIN_id`) REFERENCES `patient_data_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `patient_data_app_hospital_table` */

insert  into `patient_data_app_hospital_table`(`id`,`hosp_name`,`place`,`pin`,`post`,`phone`,`email`,`license_no`,`status`,`LOGIN_id`,`proof`,`district`) values 
(1,'mmc hospital ','Calicut','123467','Calicut',9844434345,'mmc@gmail.com','ABC1234111','Verified',2,'og (10)_WzK7kgR.pdf','Kozhikkod'),
(2,'Iqraa hospital','Calicut','654321','Calicut',9207396756,'iqraa@gmail.com','ABCD123456','Verified',4,'og (10)_WzK7kgR.pdf','Kozhikkod'),
(3,'E H elettil','Elettil','673572','Elettil',8765342190,'ehelettil@gmail.com','CDE1237890','Verified',12,'og (10)_WzK7kgR.pdf','Kozhikkod'),
(4,'Baby Memorial Hospital','Kozhikkode','564321','Kozhikkode',9078787890,'bmh@gmail.com','REW1234567','Rejected',13,'og (10)_WzK7kgR.pdf','Kozhikkod'),
(5,'A.J. Hospital','Thiruvananthapuram','695582','Kazhakuttam',9995664355,'ajhospital@gmai.com','WER1234567','Verified',14,'og (10)_WzK7kgR.pdf','Thiruvanthapuram'),
(6,'A.P.Varkey Mission Hospital','Ernakulam','682313','Arakunnam',9876453218,'varkeymission@gmail.com','MNBQ123987','Verified',15,'og (10)_WzK7kgR.pdf','Eranakulam'),
(7,'Al Shifa Hospital Pvt Ltd','Malapuram','679322','Perintalmanna',9846225293,'alshifa@gmail.com','PUTQ123456','Verified',16,'og (10)_WzK7kgR.pdf','Malappuram'),
(8,'Ashoka Hospital','Kannur','670002','South Bazar',8976270458,'ashoka@gmail.com','DSAQ765430','pending',18,'og (10)_WzK7kgR.pdf','Kannur'),
(9,'Bishop Benziger Hospital','Kollam','691001','Kollam',9645545125,'bbhospital@gmail.com','POIU789054','Verified',19,'og (10)_WzK7kgR.pdf','Kollam'),
(10,'Deva Matha Hospital','Ernakulam','686662','Koothattukulam',9207873209,'devamatha@gmail.com','DCWM456789','pending',20,'og (10)_WzK7kgR.pdf','Eranakulam'),
(11,'Divine Medical Centre','Thrissur','680590','Wadakkanchery',8943588711,'divine@gmail.com','FJKW123476','pending',21,'og (10)_WzK7kgR.pdf','Thrissur'),
(12,'Fathima Hospital','Kozhikkode','673014','Kozhikkode',9826754248,'fathima@gmail.com','KDOE123875','Verified',22,'og (10)_WzK7kgR.pdf','Kozhikkod'),
(13,'Karuna hospital','Idukki','685553','Nedumkandam',7865320916,'karuna@gmail.com','LANQ874563','pending',23,'og (10)_WzK7kgR.pdf','Idukki'),
(14,'Malabar Hospitals','Palakkad','678001','West Yakara',9400598393,'malabarhospital@gmail.com','KSVQ108945','Verified',24,'og (10)_WzK7kgR.pdf','Palakkad'),
(15,'Mes Medical College Hospital','Malappuram','679338','Perinthalmanna',9846490136,'mesmedicalhospital@gmail.com','MACF785430','Verified',25,'og (10)_WzK7kgR.pdf','Malappuram'),
(16,'Najath Super Speciality Hospital','Eranakulam','683101','Aluva',8089565198,'najath@gmail.com','POMN340941','pending',26,'og (10)_WzK7kgR.pdf','Eranakulam'),
(17,'Nila Hospital Pvt Ltd','Pattambi','679303','Pallipuram',8934672019,'nilahospital@gmail.com','SMZP785632','pending',27,'og (10)_WzK7kgR.pdf','Palakkad'),
(18,'S.K. Hospital','Trivandrum','695006','Pangode',9605916990,'skhospital@gmail.com','POCH674310','pending',28,'og (10)_WzK7kgR.pdf','Thiruvanthapuram'),
(19,'Sree Kantapuram Hospital','Mavelikara','690103','Kandiyoor',9447192224,'sreekantapuramhospital@gmail.com','MAZO873021','Rejected',29,'og (10)_WzK7kgR.pdf','Kollam'),
(20,'St. Thomas Hosptial','Pathanamthitta','689532','Edayaranmulla',9834218927,'stthomashos@gmail.com','MXPZ093642','Rejected',30,'og (10)_WzK7kgR.pdf','Pathanamthitta'),
(21,'Sridhar Hospital','Kozhikkode','673014','West Nadakav',7854134609,'sridharhospital@gmail.com','XCBW653190','Verified',31,'og (10)_WzK7kgR.pdf','Kozhikkod'),
(22,'St.Jude Hospitals','Trivandrum','695002','Trivandrum',9876342176,'stjudhospital@gmail.com','XHSW984521','pending',32,'og (10)_WzK7kgR.pdf','Thiruvanthapuram'),
(23,'Thengana Medical Mission Hospital','Kottayam','686536','Perumpananchy',7898453210,'thengana@gmail.com','FGYT236789','pending',33,'og (10)_WzK7kgR.pdf','Kottayam'),
(24,'Upasana Hospital','Kollam','691001','Kollam',7087245612,'upasanahospital@gmail.com','SNFA348971','pending',34,'og (10)_WzK7kgR.pdf','Kollam'),
(25,'Vatheyayath Hospital','Ernakulam','683542','Perumbavoor',8943218904,'vatheyayathhosp@gmail.com','GBHS189043','pending',35,'og (10)_WzK7kgR.pdf','Eranakulam'),
(26,'Vimala Hospital','Ernakulam','683575','Kanjoor',9946085085,'vimalahospital@gmail.com','MJAL245609','Verified',36,'og (10)_WzK7kgR.pdf','Eranakulam'),
(27,'Vinayaka Hospital','Wayanad','673592','Sulthan Bathery',6783093217,'vinayaka@gmail.com','KOWI267819','Verified',37,'og (10)_WzK7kgR.pdf','Wayanad'),
(28,'West Fort Hospital','Thrissur','680002','Punkunnam ',8954231097,'westfort@gmail.com','UIAP452098','Verified',38,'og (10)_WzK7kgR.pdf','Thrissur'),
(29,'West Side Hospital Pvt Ltd','Ernakulam','682002','Kappalandimukku',8943562189,'westside@gmail.com','POAM764320','Verified',39,'og (10)_WzK7kgR.pdf','Eranakulam'),
(30,'Zensa Hospital','Trivandrum','246092','Manacaud',8765350919,'zensahospital@gmail.com','JFPO894367','Rejected',40,'og (10)_WzK7kgR.pdf','Thiruvanthapuram'),
(31,'Kims hospital','Koduvally','456798','Koduvally',9846490158,'kimsmedicalhospital@gmail.com','AMVC345678','Verified',45,'og (10)_WzK7kgR.pdf','Kozhikkod');

/*Table structure for table `patient_data_app_login_table` */

DROP TABLE IF EXISTS `patient_data_app_login_table`;

CREATE TABLE `patient_data_app_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `patient_data_app_login_table` */

insert  into `patient_data_app_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin@123','admin'),
(2,'mmc@gmail.com','Mmc@1234','hospital'),
(4,'iqraa@gmail.com','Iqra@1234','hospital'),
(12,'ehelettil@gmail.com','Eh@12345','hospital'),
(13,'bmh@gmail.com','Bmc@1234','rejected'),
(14,'ajhospital@gmai.com','Jj@12345','hospital'),
(15,'varkeymission@gmail.com','Varkey@123','hospital'),
(16,'alshifa@gmail.com','Alshifa@123','hospital'),
(17,'nidhalkc369@gmail.com','123','doctor'),
(18,'ashoka@gmail.com','Ashoka@123','pending'),
(19,'bbhospital@gmail.com','Bbhosp@123','hospital'),
(20,'devamatha@gmail.com','Devamatha@123','pending'),
(21,'divine@gmail.com','Divine@123','pending'),
(22,'fathima@gmail.com','Fathima@123','hospital'),
(23,'karuna@gmail.com','Karuna@123','pending'),
(24,'malabarhospital@gmail.com','Malabar@123','hospital'),
(25,'mesmedicalhospital@gmail.com','Mesmedical@123','hospital'),
(26,'najath@gmail.com','Najath@123','pending'),
(27,'nilahospital@gmail.com','Nila@1234','pending'),
(28,'skhospital@gmail.com','Skhospital@123','pending'),
(29,'sreekantapuramhospital@gmail.com','Sk@123456','rejected'),
(30,'stthomashos@gmail.com','Stthomas@123','rejected'),
(31,'sridharhospital@gmail.com','Sridhar@123','hospital'),
(32,'stjudhospital@gmail.com','Stjude@123','pending'),
(33,'thengana@gmail.com','Thengana@123','pending'),
(34,'upasanahospital@gmail.com','Upasana@123','pending'),
(35,'vatheyayathhosp@gmail.com','Vatheyayath@123','pending'),
(36,'vimalahospital@gmail.com','Vimala@123','hospital'),
(37,'vinayaka@gmail.com','Vinayaka@123','hospital'),
(38,'westfort@gmail.com','Westfort@123','hospital'),
(39,'westside@gmail.com','Westside@123','hospital'),
(40,'zensahospital@gmail.com','Zensa@123','rejected'),
(41,'nadhanjb7@gmail.com','Nadha@4321','doctor'),
(42,'nadhilnjb06@gmail.com','Nadhil@123','doctor'),
(43,'najeebyaz@gmail.com','Najeeb@123','doctor'),
(44,'suharanjb09@gmail.com','Suhara@123','doctor'),
(45,'mimsmedicalhospital@gmail.com','Mims@123','hospital'),
(46,'kvhospital@gmail.com','Kv@123456','pending'),
(47,'mus@gmail.com','Mus@12345','pending'),
(52,'nadha','Nadha@123','patient'),
(53,'aleefa','12345','patient'),
(54,'suhara@gmail.com','Suhara@123','doctor'),
(55,'abhinandh06@gmail.com','Abhinandh@123','doctor'),
(56,'salha','Salha@123','patient'),
(57,'amrutha','Amrutha@123','patient'),
(58,'neenu','Neenu@123 ','patient'),
(59,'hinu@gmail.com','Hinu@123','doctor'),
(60,'hinu','Hinu@123','patient'),
(61,'niya','Niya@123','patient'),
(62,'renu','Renu@123','patient'),
(63,'aju','Aju@123','patient'),
(64,'sainaba','Sainaba@123','patient'),
(65,'Muhammed_ali','Muhammedali@123','patient'),
(66,'arifa_muha','Arifa@123','patient'),
(67,'uppoyin','Uppoyin@123','patient'),
(68,'Khadeeja','Khadeeja@123','patient'),
(69,'vaheeda','Vaheeda@1234','patient'),
(70,'salam ','Salam@123','patient'),
(71,'nargeesa','Nargeesa@123','patient'),
(72,'najadh','Najadh@123','patient'),
(73,'aiswarya@gmail.com','Aiswarya@123','doctor'),
(74,'muhammed@gmail.com','Muhammed@123','doctor');

/*Table structure for table `patient_data_app_medical_record_table` */

DROP TABLE IF EXISTS `patient_data_app_medical_record_table`;

CREATE TABLE `patient_data_app_medical_record_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `disease` varchar(50) NOT NULL,
  `duration` varchar(20) NOT NULL,
  `test_name` varchar(30) NOT NULL,
  `test_result` varchar(100) NOT NULL,
  `test_result_conclusion` varchar(100) NOT NULL,
  `desc` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `DOCTOR_id` bigint NOT NULL,
  `PATIENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `patient_data_app_med_DOCTOR_id_e238cc9c_fk_patient_d` (`DOCTOR_id`),
  KEY `patient_data_app_med_PATIENT_id_1a5d801f_fk_patient_d` (`PATIENT_id`),
  CONSTRAINT `patient_data_app_med_DOCTOR_id_e238cc9c_fk_patient_d` FOREIGN KEY (`DOCTOR_id`) REFERENCES `patient_data_app_doctor_table` (`id`),
  CONSTRAINT `patient_data_app_med_PATIENT_id_1a5d801f_fk_patient_d` FOREIGN KEY (`PATIENT_id`) REFERENCES `patient_data_app_patient_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `patient_data_app_medical_record_table` */

insert  into `patient_data_app_medical_record_table`(`id`,`disease`,`duration`,`test_name`,`test_result`,`test_result_conclusion`,`desc`,`date`,`DOCTOR_id`,`PATIENT_id`) values 
(1,'fever','2 weeks','Blood test','litrat_RF0Yc74.pdf','asda','ASda','2024-03-24',7,8);

/*Table structure for table `patient_data_app_patient_table` */

DROP TABLE IF EXISTS `patient_data_app_patient_table`;

CREATE TABLE `patient_data_app_patient_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `gender` varchar(35) NOT NULL,
  `dob` date NOT NULL,
  `place` varchar(50) NOT NULL,
  `pin` bigint NOT NULL,
  `post` varchar(30) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(50) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `health_id` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `patient_data_app_pat_LOGIN_id_c9121f32_fk_patient_d` (`LOGIN_id`),
  CONSTRAINT `patient_data_app_pat_LOGIN_id_c9121f32_fk_patient_d` FOREIGN KEY (`LOGIN_id`) REFERENCES `patient_data_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `patient_data_app_patient_table` */

insert  into `patient_data_app_patient_table`(`id`,`fname`,`lname`,`gender`,`dob`,`place`,`pin`,`post`,`phone`,`email`,`photo`,`LOGIN_id`,`health_id`) values 
(8,'Nadha','Najeeb','FEMALE','2022-02-02','Elettil',673572,'Elettil',8976543210,'nadhanjb7@gmail.com','IMG-20240207-WA0002_Ygi4afr.jpg',52,'1000'),
(10,'Salha','Fathima','FEMALE','2020-02-15','Madavoor',876543,'Padanilam',8796543267,'fathimasalhank@gmail.com','IMG-20240207-WA0002_KjTZac4.jpg',56,'1002'),
(11,'Amrutha','K','FEMALE','2023-02-02','Kozhikkode',876545,'Edakkad',9876567898,'amruthak@gmail.com','IMG20240219090647.jpg',57,'1003'),
(12,'Neenu','A S','FEMALE','2018-02-15','Balussery',786598,'Balussery',7034657885,'neenuajithkumar@gmail.com','Screenshot_2024-02-25-22-38-41-90_1c337646f29875672b5a61192b9010f9.jpg',58,'1004'),
(13,'Hinu','P M','Female','2015-02-07','Maavoor',457865,'Mavoor',7865432190,'hinu@gmail.com','lab_dash.png',60,'1005'),
(14,'Niya','Fathima','FEMALE','2001-02-09','Poonoor',765432,'Poonoor',8976567897,'niya@gmsil.com','Screenshot_2024-02-24-16-32-09-64_439a3fec0400f8974d35eed09a31f914.jpg',61,'1006'),
(15,'Aswin','Das','MALE','2002-02-23','Korangad',678876,'Thamarassery',9876678987,'aswin@gmail.com','Screenshot_2024-02-25-22-38-41-90_1c337646f29875672b5a61192b9010f9_F6Bl6tj.jpg',62,'1007'),
(16,'Aju','K','Male','2005-02-28','Manipuram',678765,'Koduvally',9876789890,'aju@gmail.com','lab_dash_fBZqZPV.png',63,'1008'),
(17,'Sainaba','K C','Female','1974-10-15','Thamarassery',876545,'Korangad',7890654532,'sainaba@gmail.com','view sys st_RV7Pp64.png',64,'1009'),
(18,'Muhammed','Ali','Male','1972-01-10','Narikkuni',786567,'Narikkuni',9876567865,'muhammedali@gmail.com','istockphoto-1413249877-2048x2048.jpg',65,'1010'),
(19,'Arifa','Muhammed Ali','Female','1980-10-05','Narikkuni',789876,'Narikkuni',8978656789,'arifamuh@gmail.com','vlcsnap-2023-10-12-04h54m48s751.png',66,'1011'),
(20,'Uppoyin','K C','Male','1960-10-10','Elettil',786578,'Elettil',9867543214,'uppoyin@gmail.com','istockphoto-1433795500-1024x1024.jpg',67,'1012'),
(21,'Khadeeja','T V','Female','1964-12-27','Karuvanpoyil',678987,'Karuvanpoyil',8767676745,'kadeeja@gmail.com','edit exam.png',68,'1013'),
(22,'Vaheeda','Salam','Female','1989-10-17','Elettil',6735728,'Elettil',8976567890,'vahheda34@gmail.com','vlcsnap-2023-10-12-04h54m48s751_FAGR55z.png',69,'1014'),
(23,'Salam','V M','Male','1971-12-28','Elettil',897654,'Elettil',8767898765,'salamvm@gmail.com','bank.jpg',70,'1015'),
(24,'Nargeesa','Fathima','Female','2010-06-24','Elettil',567876,'Elettil',8767898790,'nargeesasalam@gmail.com','add exam.png',71,'1016'),
(25,'Najadh','V M','Male','2021-02-09','Elettil',787656,'Elettil',7876787654,'najadhvm@gmail.com','edit exam_UsrUSiR.png',72,'1017');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
