drop table resumen_financiero;
CREATE TABLE resumen_financiero (
    id_pago SERIAL PRIMARY KEY,
    cedula VARCHAR(20) NOT NULL,
    ingreso_mensual DECIMAL(15, 2) NOT NULL,
    deuda_total DECIMAL(15, 2) NOT NULL,
    FOREIGN KEY (cedula) REFERENCES usuarios(cedula)
);