SET NAMES utf8mb4;

-- ------------------------
-- Table structure for user
-- ------------------------
-- DROP TABLE IF NOT EXISTS `user`;
CREATE TABLE `user`(
    `id` int NOT NULL AUTO_INCREMENT,
    `openid` varchar(32) NOT NULL,
    `nickname` varchar(30) NOT NULL,
    `avatar` varchar(100) NOT NULL,
    `create_time` datetime DEFAULT NULL,
    `update_time` datetime DEFAULT NULL,
    PRIMARY KEY(`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET = utf8mb4 COMMENT '用户表';