class CarroCompras:
    def __init__(self,items:list):
        self.items = items

    def agregar_item(self, libro, cantidad):
        nuevo_item = self.ItemCompra(libro, cantidad)
        self.items.append(nuevo_item)
        return nuevo_item

    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item.calcular_subtotal()
        return total

    def quitar_item(self, isbn):
        self.items = [item for item in self.items if item.libro.isbn != isbn]

    pass
    # Defina metodo inicializador __init__(self)

    # Defina el metodo agregar_item

    # Defina el metodo calcular_total

    # Defina el metodo quitar_item
