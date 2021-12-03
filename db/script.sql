create database if not exists db_clientes;

use db_clientes;

CREATE TABLE if not exists `tbl_clientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `cpf` varchar(11) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `telefone` varchar(16) DEFAULT NULL,
  `senha` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `tbl_clientes` VALUES (2,'Igor Santana Camargo','08765434554','igor.santana@gmail.com','21998630707','123456'),(3,'Eduardo Sano','98554334567','edu.sano@gmail.com','21998630957','987654'),(4,'Eduardo Maldonado','29876534678','edu.mal@gmail.com','31998630957','456789'),(5,'Fernanda Cabral','01456789065','fe.cabral@gmail.com','21978630757','209765'),(6,'Antônio Fernandes Albuquerque','91456789065','antonio.albuq@gmail.com','11978630757','209745'),(7,'Vinícius de Paula Souza','96456789075','vinícius.paula@gmail.com','31978630757','564789'),(8,'Karina Almeida Fernandes','08765494554','ka.junior@gmail.com','51998630757','987268'),(9,'Luiz Alberto','08765494554','luiz.alberto@gmail.com','31998630757','098543'),(11,'Filipe Lopes Albuquerque','18965434554','filipe.lopes@gmail.com','31998630707','983456'),(12,'Vitor Mendonça','98165434554','vitor.mendonca@gmail.com','41998630707','183456'),(13,'Vinicius Lopes','08165434854','vinicius.lopes@gmail.com','69998630707','1809456'),(14,'Lucas Vasconcelos Lima','18165434854','lucas.vasconcelos@gmail.com','29998630707','18099056'),(15,'Joao Victor Lopes','18965434554','joao.lopes@gmail.com','16998630707','583456'),(16,'Carolina Melo','48965434554','carolina.melo@gmail.com','11998630707','585456'),(21,'Tainara Silva','08165434834','tainara.silva@gmail.com','11998630707','1099056');

CREATE TABLE if not exists `tbl_enderecos` (
  `idCliente` int NOT NULL,
  `idEndereco` int NOT NULL AUTO_INCREMENT,
  `rua` varchar(100) NOT NULL,
  `numero` int NOT NULL,
  `bairro` varchar(60) NOT NULL,
  `cidade` varchar(60) NOT NULL,
  `estado` varchar(60) NOT NULL,
  `cep` varchar(20) NOT NULL,
  PRIMARY KEY (`idEndereco`),
  KEY `idCliente` (`idCliente`),
  CONSTRAINT `tbl_enderecos_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `tbl_clientes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `tbl_enderecos` VALUES (2,1,'Agilio Monteiro',32,'Cidade Nova','Belo Horizonte','MG','03121040'),(3,2,'Camé',132,'Mooca','São Paulo','SP','23121040'),(4,3,'Avenida Ipiranga',25,'Consolação','São Paulo','SP','03121040'),(5,4,'Rua do Estado',295,'Boa Vista','São Paulo','SP','04121040'),(6,5,'Rua dos Passaros',295,'Chacara Bom Retiro','Sorocaba','SP','04151040'),(7,6,'Rua Capitaes Mores',200,'Centro','São Paulo','SP','07151040'),(8,7,'Rua Almeida Barata',97,'Botafogo','Rio de Janeiro','RJ','07151040'),(9,8,'Rua Silveira Neto',1130,'Ipanema','Rio de Janeiro','RJ','01151040'),(2,10,'Rua Antônio de Albuquerque',381,'Savassi','Belo Horizonte','MG','03921060'),(2,11,'Rua Pedro II',381,'Belvedere','Belo Horizonte','MG','03921060'),(2,14,'Ribeiro de Santana',61,'Ribeirão das Neves','Moeda','MG','55121040');

create database if not exists db_servicos;

use db_servicos;

CREATE TABLE if not exists `tbl_passagens` (
  `idPassagem` int NOT NULL AUTO_INCREMENT,
  `origem` varchar(100) NOT NULL,
  `destino` varchar(100) NOT NULL,
  `data` date DEFAULT NULL,
  `preco` float(5,2) NOT NULL,
  PRIMARY KEY (`idPassagem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `tbl_passagens` VALUES (1,'Santa Rita do Sapucaí','São Paulo','2021-03-25',200.00),(2,'Pouso Alegre','Brasília','2021-07-12',350.00),(3,'Salvador','Manaus','2021-09-04',250.00);

CREATE TABLE if not exists `tbl_hospedagens` (
  `idHospedagem` int NOT NULL AUTO_INCREMENT,
  `endereco` varchar(100) NOT NULL,
  `data` date DEFAULT NULL,
  `preco` float(5,2) NOT NULL,
  PRIMARY KEY (`idHospedagem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `tbl_hospedagens` VALUES (1,'Nomaa Hotel ','2021-03-25',150.00),(2,'Emiliano Hotel','2021-07-12',200.00),(3,'Belmond Copacabana Palace','2021-09-04',239.00);
    
CREATE TABLE if not exists `tbl_bilhetes` (
  `idBilhete` int NOT NULL AUTO_INCREMENT,
  `descricao` text NOT NULL,
  `data` date DEFAULT NULL,
  `preco` float(5,2) NOT NULL,
  PRIMARY KEY (`idBilhete`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `tbl_bilhetes` VALUES (1,'Cinema','2021-02-22',15.00),(2,'Teatro','2021-07-18',60.00),(3,'Galeria de Arte','2021-09-07',40.00);
    
CREATE TABLE if not exists `tbl_veiculos` (
  `idVeiculo` int NOT NULL AUTO_INCREMENT,
  `descricao` text NOT NULL,
  `data` date DEFAULT NULL,
  `preco` float(5,2) NOT NULL,
  PRIMARY KEY (`idVeiculo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `tbl_veiculos` VALUES (1,'Fiat Uno','2021-03-25',70.00),(2,'Fiat Uno','2021-06-29',70.00),(3,'Palio','2021-10-05',80.00),(4,'Siena','2021-07-01',95.00),(5,'Celta','2021-05-20',59.00);

create database if not exists db_pedidos;

use db_pedidos;

CREATE TABLE if not exists `tbl_pedidos` (
  `idPedido` int NOT NULL AUTO_INCREMENT,
  `data` date DEFAULT NULL,
  `idCliente` int NOT NULL,
  `dataPagamento` date DEFAULT NULL,
  PRIMARY KEY (`idPedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `tbl_pedidos` VALUES (1,'2021-11-10',2,NULL),(2,'2020-11-12',3,NULL);

CREATE TABLE if not exists `tbl_pedido_itens` (
  `idPedidoItem` int NOT NULL AUTO_INCREMENT,
  `idPedido` int NOT NULL,
  `tipoServico` enum('passagem','hospedagem','bilhete','veiculo') NOT NULL,
  `idServico` int NOT NULL,
  `quantidade` int NOT NULL,
  PRIMARY KEY (`idPedidoItem`),
  CONSTRAINT `tbl_pedido_itens_fk_1` FOREIGN KEY (`idPedido`) REFERENCES `tbl_pedidos` (`idPedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `tbl_pedido_itens` VALUES (1,1,'passagem',1,1),(2,1,'hospedagem',1,1),(3,1,'bilhete',1,2),(4,2,'passagem',2,2),(5,2,'hospedagem',2,2);

