from datetime import date
class Usuario:
    def __init__(self,cedula,edad,expectativa_vida,años_renta,total_cuotas,precio_de_la_vivienda,porcentaje_precio_real,valor_de_la_hipoteca,tasa_de_interes_mensual):
        
        self.cedula=cedula
        self.edad=edad
        self.expectativa_vida=expectativa_vida
        self.años_renta=años_renta
        self.total_cuotas=total_cuotas
        self.precio_de_la_vivienda=precio_de_la_vivienda
        self.porcentaje_precio_real=porcentaje_precio_real
        self.valor_de_la_hipoteca=valor_de_la_hipoteca
        self.tasa_de_interes_mensual=tasa_de_interes_mensual
    def esIgual(self,otro):
        assert(self.cedula==otro.cedula)
        assert(self.edad==otro.edad)
        assert(self.expectativa_vida==otro.expectativa_vida)
        assert(self.años_renta==otro.años_renta)
        assert(self.total_cuotas==otro.total_cuotas)
        assert(self.precio_de_la_vivienda==otro.precio_de_la_vivienda)
        assert(self.porcentaje_precio_real==otro.porcentaje_precio_real)
        assert(self.valor_de_la_hipoteca==otro.valor_de_la_hipoteca)
        assert(self.tasa_de_interes_mensual==otro.tasa_de_interes_mensual)