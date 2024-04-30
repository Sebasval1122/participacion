import modelo
import modelo.carro_compra
import modelo.existencias_insuficientes_error
import modelo.libro_agotado_error
class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito = modelo.carro_compra()

    def agregar_libro_a_carrito(self, libro, cantidad):
        if libro.existencias == 0:
            raise modelo.libro_agotado_error(libro.titulo, libro.isbn)
        if cantidad > libro.existencias:
            raise modelo.existencias_insuficientes_error(libro.titulo, libro.isbn, cantidad, libro.existencias)
        self.carrito.agregar_item(libro, cantidad)

    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)
