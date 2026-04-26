import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
def validar_entero(valor, minimo=None, maximo=None):
    try:
        valor = int(valor)
        if minimo is not None and valor < minimo:
            return None
        if maximo is not None and valor > maximo:
            return None
        return valor
    except:
        return None

class SIATA:
    def __init__(self, ruta):
        self.df = pd.read_csv(ruta)

    def info_basica(self):
        print("\nINFO:")
        self.df.info()
        print("\nDESCRIBE:\n", self.df.describe())

    def convertir_fecha(self, columna):
        self.df[columna] = pd.to_datetime(self.df[columna])
        self.df.set_index(columna, inplace=True)

    def eliminar_nulos(self):
        connulos = len(self.df)
        self.df.dropna(inplace=True)
        sinnulos = len(self.df)
        print(f"\nEliminados: {connulos - sinnulos} registros con nulos.")

    def graficos(self, columna):
        fig, axs = plt.subplots(3, 1, figsize=(10, 8))

        self.df[columna].plot(ax=axs[0], title="Plot")
        axs[0].set_ylabel("Valor")

        self.df[columna].plot.box(ax=axs[1])
        axs[1].set_title("Boxplot")

        self.df[columna].hist(ax=axs[2])
        axs[2].set_title("Histograma")

        plt.tight_layout()
        plt.savefig(f"{columna}_graficos.png")
        plt.show()

    def operaciones(self, col1, col2):
        print("\nAPPLY (*2):\n", self.df[col1].apply(lambda x: x * 2).head())

        print("\nMAP (+1):\n", self.df[col1].map(lambda x: x + 1).head())

        print("\nSUMA:\n", (self.df[col1] + self.df[col2]).head())

    def remuestreo(self, columna):
        df_num = self.df.select_dtypes(include=['number'])

        diario = df_num.resample('D').mean()
        mensual = df_num.resample('ME').mean()
        trimestral = df_num.resample('QE').mean()

        diario[columna].plot(title="Diario")
        mensual[columna].plot(title="Mensual")
        trimestral[columna].plot(title="Trimestral")

        plt.tight_layout()
        plt.savefig("resample.png")
        plt.show()

class EEG:
    def __init__(self, ruta):
        self.data = sio.loadmat(ruta)

    def mostrar_llaves(self):
        print("\nLlaves del archivo:")
        for key in self.data.keys():
            print(key)

    def obtener_matriz(self, key):
        return self.data[key]
    
    def sumar_canales(self, matriz, canales, inicio, fin):
        matriz_2d = matriz.reshape(matriz.shape[0], -1)

        c1, c2, c3 = canales

        suma = (
            matriz_2d[c1, inicio:fin] +
            matriz_2d[c2, inicio:fin] +
            matriz_2d[c3, inicio:fin]
        )

        t = np.arange(inicio, fin) / 1000  # 1kHz

        plt.figure(figsize=(10, 6))

        plt.subplot(2, 1, 1)
        plt.plot(t, matriz_2d[c1, inicio:fin], label=f"Canal {c1}")
        plt.plot(t, matriz_2d[c2, inicio:fin], label=f"Canal {c2}")
        plt.plot(t, matriz_2d[c3, inicio:fin], label=f"Canal {c3}")
        plt.xlabel("Segundos")
        plt.ylabel("µV")
        plt.title("Canales originales")
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(t, suma, label="Suma", color="black")
        plt.xlabel("Segundos")
        plt.ylabel("µV")
        plt.title("Suma de canales")
        plt.legend()

        plt.tight_layout()
        plt.savefig("eeg_suma.png")
        plt.show()
 
    def estadisticas(self, matriz, indice_canal):
         
        promedio_total = np.mean(matriz, axis=2) 
        std_total = np.std(matriz, axis=2)

        # Extraemos solo el canal que el usuario eligió
        # Usamos los primeros 500 puntos para que el gráfico 'stem' no se sature
        señal_promedio = promedio_total[indice_canal, :500]
        señal_std = std_total[indice_canal, :500]

        plt.figure(figsize=(12, 7))

        # Subplot 1: Promedio
        plt.subplot(2, 1, 1)
        plt.stem(señal_promedio)
        plt.title(f"Señal Promedio - Canal {indice_canal}")
        plt.ylabel("µV") # Unidad obligatoria por requerimiento 7b

        # Subplot 2: Desviación Estándar
        plt.subplot(2, 1, 2)
        plt.stem(señal_std, linefmt='r-', markerfmt='ro') # En rojo para diferenciar
        plt.title(f"Desviación Estándar - Canal {indice_canal}")
        plt.ylabel("µV")

        plt.tight_layout()
        plt.savefig("estadisticas_eeg.png") # Guarda el resultado
        plt.show()

class Gestor:
    def __init__(self):
        self.objetos = []

    def agregar(self, obj):
        self.objetos.append(obj)

    def listar(self):
        for i, obj in enumerate(self.objetos):
            print(f"{i}: {type(obj).__name__}")

    def buscar(self, tipo):
        return [o for o in self.objetos if isinstance(o, tipo)]
