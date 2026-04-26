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
            siata_obj = SIATA(ruta)
            try:
                
                siata_obj = SIATA(ruta)
                gestor.agregar(siata_obj)
                
                # Mostrar informacion y describir
                siata_obj.info_basica()
                
                while True:
                    print("\n-Submenú SIATA-")
                    print("1. Graficar Plot, Boxplot, Histograma")
                    print("2. Realizar operaciones Apply, Map, Suma")
                    print("3. Re-muestreo (Diario, Mensual, Trimestral)")
                    print("4. Volver al menú principal")
                    
                    sub = input("Opción: ")
                    
                    if sub == "1":

                        col = input("Ingrese el nombre de la columna a graficar: ")
                        siata_obj.graficos(col) #realiza y muestra los 3 graficos

                    elif sub == "2":
                        c1 = input("Columna 1: ")
                        c2 = input("Columna 2: ")
                        siata_obj.operaciones(c1, c2)  #realiza y muestra las operaciones de la columna

                    elif sub == "3":
                        
                        col_fecha = input("Ingrese el nombre de la columna de fechas: ")
                        siata_obj.convertir_fecha(col_fecha)
                        col_dato = input("Ingrese columna para re-muestrear: ")
                        siata_obj.remuestreo(col_dato)

                    elif sub == "4":
                        break


            #excepcion por si no se encuentra el archivo
            except Exception as e:
                print(f"Error al cargar CSV: {e}")

        elif opcion == "2":
            ruta = input("Ingrese la ruta del archivo MAT (ej: control.mat): ")
            try:
                eeg_obj = EEG(ruta)
                gestor.agregar(eeg_obj)
                
                # Mostrar llaves 
                eeg_obj.mostrar_llaves()
                key = input("Elija la llave de la matriz a trabajar (ej:data): ")
                matriz = eeg_obj.obtener_matriz(key)
                
                while True:
                    print("\n-Submenú EEG-")
                    print("1. Sumar 3 canales (2D)")
                    print("2. Estadísticas Promedio/STD (3D)")
                    print("3. Volver al menú principal")
                    
                    sub = input("Opción: ")

            #excepcion por si no se encuentra el archivo       
            except Exception as e:
                print(f"Error al cargar MAT: {e}")

        elif opcion == "4":
            print("Sistema cerrado")
            break
            #salir del sistema


        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu_principal()
