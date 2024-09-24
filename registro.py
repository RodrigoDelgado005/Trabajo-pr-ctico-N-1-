Alumnos = [
    {'nombre': 'Lucio', 'apellido': 'Aguilar', 'edad': 19, 'especialidad': 'Informatica'},
    {'nombre': 'Federico', 'apellido': 'Caracciolo', 'edad': 19, 'especialidad': 'Informatica'},
    {'nombre': 'Luca', 'apellido': 'Pons', 'edad': 18, 'especialidad': 'Construcciones'},
    {'nombre': 'Marcos', 'apellido': 'Funes', 'edad': 19, 'especialidad': 'Informatica'},
    {'nombre': 'Lautaro', 'apellido': 'Montes', 'edad': 19, 'especialidad': 'Informatica'},
    {'nombre': 'Martin', 'apellido': 'Gonzalez', 'edad': 38, 'especialidad': 'Informatica'},
    {'nombre': 'Gonzalo', 'apellido': 'Beckhman', 'edad': 19, 'especialidad': 'Informatica'},
    {'nombre': 'Carlos', 'apellido': 'Colosimo', 'edad': 19, 'especialidad': 'Informatica'},
    {'nombre': 'Giuliano', 'apellido': 'De Giusto', 'edad': 22, 'especialidad': 'Informatica'},
    {'nombre': 'Gaspar', 'apellido': 'Barea', 'edad': 19, 'especialidad': 'Informatica'}
]

print("Lista de Alumnos:")
for Alumno in Alumnos:
    print(f"Nombre: {Alumno.get('nombre')}, Apellido: {Alumno.get('apellido')}, Edad: {Alumno.get('edad')}, Especialidad: {Alumno.get('especialidad')}")

def actualizar_alumno(nombre, apellido, nuevos_datos):
    for alumno in Alumnos:
        if alumno['nombre'] == nombre and alumno['apellido'] == apellido:
            for clave, valor in nuevos_datos.items():
                if clave in alumno:
                    alumno[clave] = valor
            return alumno
    return None

def eliminar_alumno(nombre, apellido):
    global Alumnos
    global alumnos_eliminados  
    alumnos_eliminados = []  
    for alumno in Alumnos:
        if alumno['nombre'] == nombre and alumno['apellido'] == apellido:
            alumnos_eliminados.append(alumno)  
    Alumnos = [alumno for alumno in Alumnos if not (alumno['nombre'] == nombre and alumno['apellido'] == apellido)]

actualizados = []  

actualizados.append(actualizar_alumno('Lucio', 'Aguilar', {'edad': 20, 'especialidad': 'Ingenieria'}))
actualizados.append(actualizar_alumno('Federico', 'Caracciolo', {'edad': 21, 'especialidad': 'Matematica'}))
actualizados.append(actualizar_alumno('Luca', 'Pons', {'edad': 19, 'especialidad': 'Construcciones Avanzadas'}))

actualizados = [alumno for alumno in actualizados if alumno is not None]

print("\nAlumnos actualizados:")
for Alumno in actualizados:
    print(f"Nombre: {Alumno.get('nombre')}, Apellido: {Alumno.get('apellido')}, Edad: {Alumno.get('edad')}, Especialidad: {Alumno.get('especialidad')}")

eliminar_alumno('Martin', 'Gonzalez')

print("\nAlumnos eliminados:")
for Alumno in alumnos_eliminados:
    print(f"Nombre: {Alumno.get('nombre')}, Apellido: {Alumno.get('apellido')}, Edad: {Alumno.get('edad')}, Especialidad: {Alumno.get('especialidad')}")

print("\nLista de Alumnos después de la eliminación:")
for Alumno in Alumnos:
    print(f"Nombre: {Alumno.get('nombre')}, Apellido: {Alumno.get('apellido')}, Edad: {Alumno.get('edad')}, Especialidad: {Alumno.get('especialidad')}")
