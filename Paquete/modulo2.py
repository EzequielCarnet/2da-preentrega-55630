#metodos


def comprar(cliente):
        while True:
            try:
                producto = int(input("elija el producto que desea comprar:\n1-Computadora\n2-Celular\n3-Tablet\n"))
                if producto == 1:
                    print(f"{cliente.nombre} has comprado una Computadora! felicitaciones!")
                elif producto == 2:
                    print(f"{cliente.nombre} has comprado un Celular! felicitaciones!")
                elif producto == 3:
                    print(f"{cliente.nombre} has comprado una Tablet! felicitaciones!")
                else:
                    print(f"{cliente.nombre} has seleccionado una opcion incorrecta. vuelvé a intentar.")
                    continue                
            except ValueError:
                print("Opción inválida. Por favor, elija una opción válida (1, 2 o 3).")
                continue
            else:
                cliente.productos_comprados.append(producto)
                respuesta = input("¿Deseas realizar otra compra? (s/n): ")
            if respuesta.lower() == 'n':
                print(f"Productos comprados por {cliente.nombre}: {cliente.productos_comprados}")
                break
            

        return cliente.productos_comprados 

