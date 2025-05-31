-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dbliverpool
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dbliverpool` ;

-- -----------------------------------------------------
-- Schema dbliverpool
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dbliverpool` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `dbliverpool` ;

-- -----------------------------------------------------
-- Table `dbliverpool`.`cliente`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbliverpool`.`cliente` ;

CREATE TABLE IF NOT EXISTS `dbliverpool`.`cliente` (
  `ID_Cliente` CHAR(10) NOT NULL,
  `Nombre` VARCHAR(50) NOT NULL,
  `Apellido` VARCHAR(50) NOT NULL,
  `Direccion` VARCHAR(100) NULL DEFAULT NULL,
  `Telefono` CHAR(10) NULL DEFAULT NULL,
  `Correo_Electronico` VARCHAR(100) NULL DEFAULT NULL,
  `RFC` CHAR(13) NULL DEFAULT NULL,
  PRIMARY KEY (`ID_Cliente`),
  UNIQUE INDEX `Correo_Electronico` (`Correo_Electronico` ASC) VISIBLE,
  UNIQUE INDEX `RFC` (`RFC` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

INSERT INTO cliente(ID_Cliente, Nombre, Apellido, Direccion, Telefono, Correo_Electronico, RFC) VALUES
	(0000, 'Cliente', 'General', 'N/A', 'N/A', 'N/A', 'N/A'),
	(1234, 'Mauricio', 'Perez', 'Av. Juarez', '1119992223', 'Mauricio@gmail.com', 'HCSKK8890LMM1'),
	(5678, 'Pedro', 'Larez', 'Av. Central', '1119992224', 'Pedro@gmail.com', 'HCXKK8890LMM2'),
	(9922, 'Julio', 'Alvarez', 'Calle Norte', '1119992225', 'Julio@gmail.com', 'HCMLL8890LMM1');

-- -----------------------------------------------------
-- Table `dbliverpool`.`categoria`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbliverpool`.`categoria` ;

CREATE TABLE IF NOT EXISTS `dbliverpool`.`categoria` (
  `ID_Categoria` CHAR(10) NOT NULL,
  `Nombre` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`ID_Categoria`),
  UNIQUE INDEX `Nombre` (`Nombre` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

INSERT INTO categoria(ID_Categoria, Nombre) VALUES
	(1, 'Muebles'), (2, 'Electronica'), (3, 'Electrodomesticos'), (4, 'Deportes'), (5, 'Alimentos y Bebidas');


-- -----------------------------------------------------
-- Table `dbliverpool`.`empleado`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbliverpool`.`empleado` ;

CREATE TABLE IF NOT EXISTS `dbliverpool`.`empleado` (
  `ID_Empleado` CHAR(10) NOT NULL,
  `Nombre` VARCHAR(50) NOT NULL,
  `Apellido` VARCHAR(50) NOT NULL,
  `Puesto` VARCHAR(50) NULL DEFAULT NULL,
  `Departamento` VARCHAR(50) NULL DEFAULT NULL,
  `Salario` FLOAT NULL DEFAULT NULL,
  PRIMARY KEY (`ID_Empleado`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

INSERT INTO empleado(ID_Empleado, Nombre, Apellido, Puesto, Departamento, Salario) VALUES
	(12345, 'Juan', 'Nuñez', 'Cajero', 'Caja', 1500),
	(67890, 'Fabricio', 'Ruiz', 'Conserje', 'Limpieza', 1200);


-- -----------------------------------------------------
-- Table `dbliverpool`.`Factura`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbliverpool`.`Factura` ;

CREATE TABLE IF NOT EXISTS `dbliverpool`.`Factura` (
  `idFactura` INT NOT NULL,
  `Nombre_Establecimiento` VARCHAR(45) NULL,
  `Importe` DECIMAL(10,2) NULL,
  `Direc_Establecimiento` VARCHAR(45) NULL,
  `Fecha` DATE NULL,
  `Metodo_Pago` VARCHAR(45) NULL,
  `Cantidad_pagada` FLOAT NULL,
  `Cambio` FLOAT NULL,
  PRIMARY KEY (`idFactura`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dbliverpool`.`ventas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbliverpool`.`ventas` ;

CREATE TABLE IF NOT EXISTS `dbliverpool`.`ventas` (
  `ID_Venta` CHAR(10) NOT NULL,
  `Fecha` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `Monto_Total` FLOAT NOT NULL,
  `empleado` CHAR(10) NOT NULL,
  `cliente` CHAR(10) NOT NULL,
  `Factura` INT NOT NULL,
  PRIMARY KEY (`ID_Venta`),
  INDEX `fk_venta_empleado1_idx` (`empleado` ASC) VISIBLE,
  INDEX `fk_ventas_cliente1_idx` (`cliente` ASC) VISIBLE,
  INDEX `fk_ventas_Factura1_idx` (`Factura` ASC) VISIBLE,
  CONSTRAINT `fk_venta_empleado1`
    FOREIGN KEY (`empleado`)
    REFERENCES `dbliverpool`.`empleado` (`ID_Empleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ventas_cliente1`
    FOREIGN KEY (`cliente`)
    REFERENCES `dbliverpool`.`cliente` (`ID_Cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ventas_Factura1`
    FOREIGN KEY (`Factura`)
    REFERENCES `dbliverpool`.`Factura` (`idFactura`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbliverpool`.`Almacen`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbliverpool`.`Almacen` ;

CREATE TABLE IF NOT EXISTS `dbliverpool`.`Almacen` (
  `No_Lote_Almacen` INT NOT NULL AUTO_INCREMENT,
  `Existencia` INT NULL,
  `Articulos_proveedor` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`No_Lote_Almacen`))
ENGINE = InnoDB;

INSERT INTO Almacen(No_Lote_Almacen, Existencia, Articulos_proveedor) VALUES
	(1, 100, 'Refrescos'), (2, 200, 'Electronica'), (3, 250,'Muebles'), (4, 90, 'Electrodomesticos'), (5, 100, 'Articulos Deportivos');


-- -----------------------------------------------------
-- Table `dbliverpool`.`articulo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbliverpool`.`articulo` ;

CREATE TABLE IF NOT EXISTS `dbliverpool`.`articulo` (
  `ID_Articulo` CHAR(13) NOT NULL,
  `Nombre` VARCHAR(100) NOT NULL,
  `Precio` FLOAT NOT NULL,
  `Existencia` INT NULL,
  `categoria` CHAR(10) NOT NULL,
  `Almacen` INT NOT NULL,
  `Costo` FLOAT NULL,
  PRIMARY KEY (`ID_Articulo`),
  INDEX `fk_articulo_categoria1_idx` (`categoria` ASC) VISIBLE,
  INDEX `fk_articulo_Almacen1_idx` (`Almacen` ASC) VISIBLE,
  CONSTRAINT `fk_articulo_categoria1`
    FOREIGN KEY (`categoria`)
    REFERENCES `dbliverpool`.`categoria` (`ID_Categoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_articulo_Almacen1`
    FOREIGN KEY (`Almacen`)
    REFERENCES `dbliverpool`.`Almacen` (`No_Lote_Almacen`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

INSERT INTO articulo(ID_Articulo, Nombre, Precio, Existencia, Categoria, Almacen, Costo) VALUES
	('1169005156', 'Sofá Tarte ', 19790.00, 20, 1, 3, 1600),
    ('1132739532', 'Mesa centro Coffee', 1799.00, 50, 1, 3, 1500),
    ('1164135451', 'Sillón Selena', 11029.00, 10, 1, 3, 10000),
    ('9936499631', 'Funda sofá antideslizante protector', 1319.00, 35, 1, 3, 1200),
    ('1155395202', 'Sofá cama Milán', 17999.00, 20, 1, 3, 14000),
    ('1170167321', 'Laptop HP AL2Q6LT#ABM 14 pulgadas Full HD Intel Core i7 Intel Iris Plus 8 GB RAM 512 GB SSD', 16798.00, 40, 2, 2, 14000),
    ('1100125681', 'Protector de Voltajer PV-2500 d negro', 719.00, 30, 2, 2, 400),
    ('1160613404', 'Pantalla Smart TV LED de 55 pulgadas 4K UHD 55UR7800PSB', 11549.00, 25, 2, 2, 9000),
    ('1171137426', 'Proyector Pro-260', 1490.00, 20, 2, 2, 900),
    ('1097521774', 'Barra de sonido HT-S20R con subwoofer', 7499.00, 45, 2, 2, 5000),
    ('1094212215', 'Refrigerador Unipuerta 7 pies RR63D6WBX', 10599.00, 10, 3, 4, 7000),
    ('1159708809', 'Estufa de piso a gas LP Focaris 76.60 cm em7654bfis3 de 6 quemadores', 12599.00, 15, 3, 4, 10000),
    ('1096115578', 'Horno eléctrico rosticero 30 L', 4109.00, 15, 3, 4, 2000),
    ('1104750318', 'Aire acondicionado mini split frío y calor 12000 BTU MMT12HABWCAM2 115 V ', 12199.00, 20, 3, 4, 10000),
    ('1161090201', 'Caminadora semiprofesional ce-8610 plegable', 12649.00, 30, 4, 5, 10000),
	('1112212848', 'Bicicleta fija fitness MKZ-703-18 kg', 12999.00, 30, 4, 5, 11000),
	('1128812586', 'Elíptica magnética Sunny Fitness Cross SF-E3955', 9999.00, 20, 4, 5, 7000),
	('1136993441', 'Maleta deportiva Project Rock Duffle', 2999.00, 30, 4, 5, 1200),
	('1109389095', 'Botella de hidratación de acero inoxidable', 799.00, 50, 4, 5, 350),
    ('7501022014080', 'Refresco 7up 1.5 lts', 30.00, 100, 5, 1, 22);


-- -----------------------------------------------------
-- Table `dbliverpool`.`detalle_venta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbliverpool`.`detalle_venta` ;

CREATE TABLE IF NOT EXISTS `dbliverpool`.`detalle_venta` (
  `venta` CHAR(10) NOT NULL,
  `articulo` CHAR(13) NOT NULL,
  `Cantidad` INT NOT NULL,
  `Subtotal` FLOAT NOT NULL,
  PRIMARY KEY (`venta`, `articulo`),
  INDEX `fk_detalle_venta_venta1_idx` (`venta` ASC) VISIBLE,
  INDEX `fk_detalle_venta_articulo1_idx` (`articulo` ASC) VISIBLE,
  CONSTRAINT `fk_detalle_venta_venta1`
    FOREIGN KEY (`venta`)
    REFERENCES `dbliverpool`.`ventas` (`ID_Venta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_detalle_venta_articulo1`
    FOREIGN KEY (`articulo`)
    REFERENCES `dbliverpool`.`articulo` (`ID_Articulo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbliverpool`.`proveedor`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbliverpool`.`proveedor` ;

CREATE TABLE IF NOT EXISTS `dbliverpool`.`proveedor` (
  `ID_Proveedor` CHAR(10) NOT NULL,
  `Nombre` VARCHAR(100) NOT NULL,
  `Contacto` VARCHAR(100) NULL DEFAULT NULL,
  `Telefono` CHAR(10) NULL DEFAULT NULL,
  `Direccion` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`ID_Proveedor`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

INSERT INTO proveedor(ID_Proveedor, Nombre, Contacto, Telefono, Direccion) VALUES
	(9999, 'Pepsi', 'Horacio', 5557771118, 'Av. Venustiano Carranza'),
	(8888, 'Muebleria Twoson', 'Paula', 4443330002, 'Calle 3 de Mayo'),
	(7777, 'Electrodomesticos Onett', 'Mariano', 8881110002, 'Av Solovino'),
	(6666, 'Electronica Fourside', 'Ernesto', 7774443339, 'Calle 9na poniente');

-- -----------------------------------------------------
-- Table `dbliverpool`.`Compras`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbliverpool`.`Compras` ;

CREATE TABLE IF NOT EXISTS `dbliverpool`.`Compras` (
  `Almacen` INT NOT NULL,
  `proveedor` CHAR(10) NOT NULL,
  INDEX `fk_Compras_Almacen1_idx` (`Almacen` ASC) VISIBLE,
  INDEX `fk_Compras_proveedor1_idx` (`proveedor` ASC) VISIBLE,
  CONSTRAINT `fk_Compras_Almacen1`
    FOREIGN KEY (`Almacen`)
    REFERENCES `dbliverpool`.`Almacen` (`No_Lote_Almacen`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Compras_proveedor1`
    FOREIGN KEY (`proveedor`)
    REFERENCES `dbliverpool`.`proveedor` (`ID_Proveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
