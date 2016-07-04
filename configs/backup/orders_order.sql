CREATE TABLE `orders_order` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `name` varchar(200) NOT NULL COMMENT '订单名称',
  `product_id` int(11) NOT NULL COMMENT '产品编号',
  `project_id` int(11) NOT NULL COMMENT '项目编号',
  `parent_id` bigint(20) unsigned NOT NULL COMMENT '父订单编号',
  `user_id` int(11) NOT NULL COMMENT '投资人编号',
  `start_time` datetime(6) NOT NULL COMMENT '起息日',
  `period` smallint(5) unsigned NOT NULL COMMENT '投资期限',
  `payment_number` bigint(20) NOT NULL COMMENT '交易流水号',
  `quantity` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '购买份额',
  `gross` bigint(20) NOT NULL COMMENT '应付金额',
  `total_fee` bigint(20) NOT NULL COMMENT '实付金额',
  `refund` bigint(20) NOT NULL DEFAULT '0' COMMENT '退款金额',
  `status` smallint(6) NOT NULL COMMENT '订单状态',
  `payment_service_id` int(11) NOT NULL COMMENT '第三方交易号',
  `is_active` tinyint(1) NOT NULL COMMENT '是否有效',
  `address` varchar(200) DEFAULT '',
  `phone_number` varchar(20) DEFAULT '',
  `description` varchar(2000) DEFAULT '',
  `remark` varchar(1000) DEFAULT '',
  `created_time` datetime(6) NOT NULL COMMENT '创建时间',
  `updated_time` datetime(6) NOT NULL COMMENT '更新时间',
  `contract_urls` varchar(2000) DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `idx_payment_number` (`payment_number`) USING BTREE,
  KEY `idx_user_id` (`user_id`) USING BTREE,
  KEY `idx_project_product_id` (`project_id`,`product_id`,`status`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
