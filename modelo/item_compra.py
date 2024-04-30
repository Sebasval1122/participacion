class ItemCompra:
    def __init__(self,libro,tipo_libro:int,cantidad:int) -> None:
        self.libro=libro
        self.tipo_libro=tipo_libro
        self.cantidad=cantidad
    def calcular_subtotal(self,cantidad, precio_del_libro):
        subtotal = cantidad * precio_del_libro
        return subtotal
    
