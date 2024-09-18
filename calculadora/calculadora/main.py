import flet as ft
from calculadora import main

def calc_suma(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1+num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error Ingresa valores correctos"
        
        
def calc_resta(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1+num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error Ingresa valores correctos"


ft.app(main)
