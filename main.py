# main.py

from src.logica.logicaAlarma import crear_usuario, crear_alarma, obtener_usuarios, obtener_alarmas, cerrar_sesion
from datetime import time


def main():
    # Crear usuarios
    usuario1 = crear_usuario('Alice', 'alice@example.com')
    usuario2 = crear_usuario('Bob', 'bob@example.com')

    # Crear alarmas
    crear_alarma(time(7, 0), 'Despertar para el trabajo', usuario1.id)
    crear_alarma(time(8, 0), 'Despertar para el ejercicio', usuario2.id)

    # Obtener y mostrar usuarios y alarmas
    usuarios = obtener_usuarios()
    alarmas = obtener_alarmas()

    print("Usuarios:")
    for usuario in usuarios:
        print(f'{usuario.id}: {usuario.nombre} ({usuario.email})')

    print("\nAlarmas:")
    for alarma in alarmas:
        print(f'{alarma.id}: {alarma.hora} - {alarma.descripcion} (Usuario ID: {alarma.usuario_id})')

    # Cerrar la sesión
    cerrar_sesion()


if __name__ == '__main__':
    main()
