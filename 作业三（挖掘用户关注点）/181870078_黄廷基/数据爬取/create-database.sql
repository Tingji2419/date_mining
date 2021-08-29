DROP DATABASE IF EXISTS `taobao`;
CREATE DATABASE `taobao`; 
USE `taobao`;

SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;

CREATE TABLE `product` (
  `pro_name` VARCHAR(255) NOT NULL,
  `pro_price` VARCHAR(255) DEFAULT NULL,
  `pro_freight` VARCHAR(255) DEFAULT NULL,
  `pro_promise` VARCHAR(255) DEFAULT NULL,
  `pro_pay` VARCHAR(255) DEFAULT NULL,
  `pro_service` VARCHAR(255) DEFAULT NULL,  
  `pro_collect` VARCHAR(255) DEFAULT NULL,  
  `pro_review_num` INT(100) DEFAULT NULL, 
  `pro_sell_num` VARCHAR(100) DEFAULT NULL,
  `re_pic_num` VARCHAR(100) DEFAULT NULL,
  `re_good_num` VARCHAR(100) DEFAULT NULL,
  `re_neutral_num` VARCHAR(100) DEFAULT NULL, 
  `re_bad_num` VARCHAR(100) DEFAULT NULL,
  `re_append_num` VARCHAR(100) DEFAULT NULL,
  `charity_name` VARCHAR(255) DEFAULT NULL, 
  `charity_price` VARCHAR(255) DEFAULT NULL,
  `charity_amount` VARCHAR(255) DEFAULT NULL, 
  `charity_detail` VARCHAR(1000) DEFAULT NULL,
  `url` VARCHAR(500) DEFAULT NULL,
  `input_time` VARCHAR(225) DEFAULT NULL,
  PRIMARY KEY (`pro_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `review` (
  `tb_num` INT(11) NOT NULL,
  `url` VARCHAR(500) NOT NULL,
  `cus_id` VARCHAR(255) DEFAULT NULL,
  `cus_name` VARCHAR(255) DEFAULT NULL,
  `cus_rank` VARCHAR(255) DEFAULT NULL,
  `re_content` VARCHAR(3000) DEFAULT NULL,
  `re_pic` VARCHAR(2000) DEFAULT NULL,
  `re_video` VARCHAR(1000) DEFAULT NULL,
  `re_append_pic` VARCHAR(1000) DEFAULT NULL,
  `re_append_video` VARCHAR(1000) DEFAULT NULL,
  `re_reply` VARCHAR(3000) DEFAULT NULL,
  `re_zp` VARCHAR(3000) DEFAULT NULL,
  `re_time` VARCHAR(200) DEFAULT NULL,
  `re_pro` VARCHAR(255) DEFAULT NULL,
  `re_useful_num` VARCHAR(20) DEFAULT NULL,
  PRIMARY KEY (`tb_num`, `url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `shop` (
  `shop_name` VARCHAR(255) NOT NULL,
  `shop_url` VARCHAR(255) DEFAULT NULL,
  `shop_age` VARCHAR(255) DEFAULT NULL,
  `shop_seller` VARCHAR(255) DEFAULT NULL,
  `shop_qua` VARCHAR(255) DEFAULT NULL,
  `shop_rate` VARCHAR(255) DEFAULT NULL,
  `url` VARCHAR(500) NOT NULL,
  PRIMARY KEY (`shop_name`, `url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;