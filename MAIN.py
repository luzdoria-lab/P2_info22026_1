from clases import SIATA, EEG, Gestor, validar_entero

def menu_principal():
    gestor = Gestor()
    
    while True:
        print("\n-SISTEMA DE EXPLORACIÓN NEUROAMBIENTAL-")
        print("1. Cargar y procesar archivo SIATA")
        print("2. Cargar y procesar archivo EEG")
        print("3. Ver objetos en el Gestor")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ruta = input("Ingrese el nombre del archivo (ej: siata_enero.csv): ")
            try:
              
                siata_obj = SIATA(ruta)
                gestor.agregar(siata_obj)
                
                # Mostrar informacion y describir
                siata_obj.info_basica()
                

            except Exception as e:
                #excepcion por si no se encuentra el archivo
                print(f"Error al cargar el archivo: {e}")

        elif opcion == "4":
            print("Sistema cerrado")
            break
            #salir del sistema
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()
