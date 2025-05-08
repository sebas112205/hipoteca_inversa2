class ResumenFinanciero:
    """CREATE TABLE pagos_hipoteca (
    id_pago SERIAL PRIMARY KEY,
    cedula VARCHAR(20) NOT NULL,
    numero_cuota INT NOT NULL,
    fecha_pago DATE NOT NULL,
    monto_pago DECIMAL(15, 2) NOT NULL,
    saldo_restante DECIMAL(15, 2) NOT NULL,
    FOREIGN KEY (cedula) REFERENCES usuarios(cedula)
);"""
    def __init__(self,cedula,ingreso_mensual,deuda_total):
        self.cedula=cedula
        self.ingreso_mensual=ingreso_mensual
        self.deuda_total=deuda_total
    def esIgual(self,otro):
        assert(self.cedula==otro.cedula)
        assert(self.ingreso_mensual==otro.ingreso_mensual)
        assert(self.deuda_total==otro.deuda_total)