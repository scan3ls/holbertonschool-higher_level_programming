-- create db hbtn_0d_2 and user user_0d_2
-- comment 2
DROP USER IF EXISTS 'user_0d_2'@'localhost';
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER 'user_0d_2'@'localhost'
	IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
