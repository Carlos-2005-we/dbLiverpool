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
  `Existencia` INT NULL,
  `Articulos_proveedor` CHAR(10) NOT NULL,
  `No_Lote_Almacen` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`No_Lote_Almacen`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dbliverpool`.`articulo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbliverpool`.`articulo` ;

CREATE TABLE IF NOT EXISTS `dbliverpool`.`articulo` (
  `ID_Articulo` CHAR(10) NOT NULL,
  `Nombre` VARCHAR(100) NOT NULL,
  `Precio` FLOAT NOT NULL,
  `Existencia` INT NULL,
  `categoria` CHAR(10) NOT NULL,
  `Almacen` INT NOT NULL,
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


-- -----------------------------------------------------
-- Table `dbliverpool`.`detalle_venta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dbliverpool`.`detalle_venta` ;

CREATE TABLE IF NOT EXISTS `dbliverpool`.`detalle_venta` (
  `Cantidad` INT NOT NULL,
  `Subtotal` FLOAT NOT NULL,
  `venta` CHAR(10) NOT NULL,
  `articulo` CHAR(10) NOT NULL,
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
