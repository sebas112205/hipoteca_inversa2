import unittest

import sys
sys.path.append("src")

from hipoteca_inversa.src.model.model.usuario import Usuario
from hipoteca_inversa.src.controller.usuario_controller import ControladorUsuario

class TestUsuario(unittest.TestCase):
    def setUpClass():
        """ Test Fixtures que se ejecuta al inicio de las pruebas solamente"""
        ControladorUsuario.eliminar_tabla()
        ControladorUsuario.crear_tabla()
    def test_insert_1( self ):
        usuario=Usuario(edad=80,expectativa_vida=10,años_renta=10,total_cuotas=3,precio_de_la_vivienda=500000000,porcentaje_precio_real=250000000,valor_de_la_hipoteca=10000000,tasa_de_interes_mensual=1.5)
        ControladorUsuario.InsertarUsuario(usuario)
        