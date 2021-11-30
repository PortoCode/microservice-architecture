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
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `tbl_enderecos` VALUES (2,1,'Agilio Monteiro',32,'Cidade Nova','Belo Horizonte','MG','03121040'),(3,2,'Camé',132,'Mooca','São Paulo','SP','23121040'),(4,3,'Avenida Ipiranga',25,'Consolação','São Paulo','SP','03121040'),(5,4,'Rua do Estado',295,'Boa Vista','São Paulo','SP','04121040'),(6,5,'Rua dos Passaros',295,'Chacara Bom Retiro','Sorocaba','SP','04151040'),(7,6,'Rua Capitaes Mores',200,'Centro','São Paulo','SP','07151040'),(8,7,'Rua Almeida Barata',97,'Botafogo','Rio de Janeiro','RJ','07151040'),(9,8,'Rua Silveira Neto',1130,'Ipanema','Rio de Janeiro','RJ','01151040'),(2,10,'Rua Antônio de Albuquerque',381,'Savassi','Belo Horizonte','MG','03921060'),(2,11,'Rua Pedro II',381,'Belvedere','Belo Horizonte','MG','03921060'),(2,14,'Ribeiro de Santana',61,'Ribeirão das Neves','Moeda','MG','55121040');

create database if not exists db_produtos;

use db_produtos;

CREATE TABLE if not exists `tbl_cursos` (
  `idCurso` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) NOT NULL,
  `descricao` text,
  `carga` int unsigned DEFAULT NULL,
  `totaulas` int unsigned DEFAULT NULL,
  `ano` year DEFAULT '2016',
  `preco` float(5,2) DEFAULT NULL,
  `ativo` enum('S','N') DEFAULT NULL,
  PRIMARY KEY (`idCurso`),
  UNIQUE KEY `nome` (`nome`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;

INSERT INTO `tbl_cursos` VALUES (2,'Algoritmos','Lógica de Programação',20,15,2014,200.00,'S'),(3,'Photoshop5','Dicas de Photoshop CC',10,8,2014,59.90,'S'),(4,'PHP','Curso de PHP para iniciantes',40,20,2015,99.99,'S'),(5,'Java','Introdução à Linguagem Java',40,29,2015,99.99,'S'),(6,'MySQL','Bancos de Dados MySQL',30,15,2016,59.90,'S'),(7,'Word','Curso completo de Word',40,30,2016,200.00,'S'),(8,'Python','Curso de Python',40,18,2017,300.00,'N'),(9,'POO','Curso de Programação Orientada a Objetos',60,35,2016,900.00,'S'),(10,'Excel','Curso completo de Excel',40,30,2017,59.99,'S'),(11,'Responsividade','Curso de Responsividade',30,15,2018,600.00,'S'),(12,'C++','Curso de C++ com Orientação a Objetos',40,25,2017,600.00,'S'),(13,'C#','Curso de C#',30,12,2017,500.00,'S'),(14,'Android','Curso de Desenvolvimento de Aplicativos para Android',60,30,2018,200.00,'S'),(15,'JavaScript','Curso de JavaScript',35,18,2017,100.00,'S'),(16,'PowerPoint','Curso completo de PowerPoint',30,12,2018,100.00,'S'),(17,'Swift','Curso de Desenvolvimento de Aplicativos para iOS',60,30,2019,300.00,'S'),(18,'Hardware','Curso de Montagem e Manutenção de PCs',30,12,2017,350.00,'S'),(19,'Redes','Curso de Redes para Iniciantes',40,15,2016,500.00,'S'),(20,'Segurança','Curso de Segurança',15,8,2018,600.00,'S'),(21,'SEO','Curso de Otimização de Sites',30,12,2017,700.00,'S'),(22,'Premiere','Curso de Edição de Vídeos com Premiere',20,10,2017,800.00,'S'),(23,'After Effects','Curso de Efeitos em Vídeos com After Effects',20,10,2018,200.00,'S'),(24,'WordPress','Curso de Criação de Sites com WordPress',60,30,2019,300.00,'S'),(25,'Joomla','Curso de Criação de Sites com Joomla',60,30,2019,700.00,'S'),(26,'Magento','Curso de Criação de Lojas Virtuais com Magento',50,25,2019,400.00,'S'),(27,'Modelagem de Dados','Curso de Modelagem de Dados',30,12,2020,100.00,'S'),(28,'HTML4','Curso Básico de HTML, versão 4.0',20,9,2010,200.00,'S'),(29,'PHP7','Curso de PHP, versão 7.0',40,20,2020,300.00,'S'),(30,'PHP4','Curso de PHP, versão 4.0',30,11,2010,500.00,'S'),(31,'Inglês Instrumental','Inglês básico para iniciantes',80,40,2021,300.00,'S'),(32,'Lingua Portuguesa','Português para estrangeiros',80,40,2021,300.00,'N'),(33,'Francês I','Básico I - Francês',40,30,2021,500.00,'S'),(34,'HTML5','Curso de HTML5',40,37,2014,100.00,'N'),(35,'Cobol','Curso de Cobol',80,50,2021,500.00,'N'),(36,'Lua','Curso de Lua',40,20,2021,300.00,'S');

create database if not exists db_vendas;

use db_vendas;

CREATE TABLE if not exists `tbl_cliente_compra_cursos` (
  `idCompra` int NOT NULL AUTO_INCREMENT,
  `data` date DEFAULT NULL,
  `idCliente` int DEFAULT NULL,
  `idCurso` int DEFAULT NULL,
  PRIMARY KEY (`idCompra`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `tbl_cliente_compra_cursos` VALUES (1,'2020-04-12',2,11),(2,'2020-03-25',4,8),(3,'2020-04-01',3,7),(4,'2020-04-12',3,8),(5,'2020-04-12',4,10);

