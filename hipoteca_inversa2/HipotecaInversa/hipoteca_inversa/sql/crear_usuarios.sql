drop table usuarios;
CREATE TABLE usuarios (
        cedula VARCHAR(20) PRIMARY KEY,
        edad INT NOT NULL,
        expectativa_vida INT NOT NULL,
        anos_renta INT NOT NULL,
        total_cuotas INT NOT NULL,
        precio_vivienda DECIMAL(15, 2) NOT NULL,
        porcentaje_precio_real DECIMAL(5, 2) NOT NULL,  
        valor_hipoteca DECIMAL(15, 2) NOT NULL,
        ingreso_mensual DECIMAL(15, 2) NOT NULL,
        tasa_interes_mensual DECIMAL(5, 4) NOT NULL     
        );