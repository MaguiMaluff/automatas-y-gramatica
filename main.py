from lector_csv import Lector

def main():
    lector = Lector()
    usuario = input("Que usuario?")
    fecha_inicio = str(input("Inicio?"))
    fecha_fin = str(input("Fin?"))
    user_list = lector.get_user_ID(usuario, lector.data)
    fecha_list = lector.get_day(fecha_inicio, fecha_fin, user_list[:-1])
    results = lector.get_results(fecha_list)
    for i in results:
        print(i, '\n')
    print("Conexiones Totales: ", len(results))


if __name__ == '__main__':
    main()


