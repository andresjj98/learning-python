'''
C => Create (INSERT INTO)
R => Read   (SELECT)
U => Update (UPDATE)
D => Delete (DELETE)

UPDATE AND DELETE NEED A WHERE CLAUSE.
'''
from school_db import con, cur
import sys
import os
import bcrypt
from datetime import datetime

status_menu = True
global status_op

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

#Menu inicial----------------------------------------------------------------
def menu():
    os.system('clear')
    print(":::::Menú de selección:::::")
    print("1. Rellenar tablas")
    print("2. Consultas")
    print("3. Salir")
    return input("Seleccione una opción: ")

#Menu insertar datos -----------------------------------------------------------------
def fill_tables_menu():
    os.system('clear')
    print("**Menú de rellenar tablas**")
    print("1. Rellenar tabla de tipos de identificación")
    print("2. Rellenar tabla de Paises")
    print("3. Rellenar tabla de departamentos")
    print("4. Rellenar tabla de ciudades")
    print("5. Rellenar tabla de usuarios")
    print("6. Rellenar tabla de personas")    
    print("7. Rellenar tabla de estudiantes")
    print("8. Volver al menú principal")
    return input("Seleccione una opción: ")

# Crear nuevo tipos de identificacion -----------------------------------------------------------
def create_identification_type():
    os.system('clear')
    print ("::: Complete los campos :::")
    name = input("Tipo de documento: ")
    abrev = input("Abreviatura: ")
    descrip = input("Descripcion: ")
    now = datetime.now()
    created_at = now.strftime("%Y-%m-%d %H:%M:%S")
    updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear la sentencia SQL con placeholders para los valores
    sql = f'''
    INSERT INTO identification_types (name, abrev, descrip, created_at, updated_at) 
    VALUES (?, ?, ?, ?, ?)
'''

# Ejecutar la sentencia SQL con los valores correspondientes
    cur.execute(sql, (name, abrev, descrip, created_at, updated_at))
    con.commit()

    print("::: Nuevo tipo de identificacion ha sido creado con exito :::")
    input("Presiona Enter para continuar...")
    #os.system('pause')
    fill_tables_menu()

# insertar nuevo paises -----------------------------------------------------------
def create_countries():
    os.system('clear')
    print ("::: Complete los campos :::")
    name = input("Nombre del pais: ")
    abrev = input("Abreviatura: ")
    descrip = input("Descripcion: ")
    now = datetime.now()
    created_at = now.strftime("%Y-%m-%d %H:%M:%S")
    updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear la sentencia SQL con placeholders para los valores
    sql = f'''
    INSERT INTO countries (name, abrev, descrip, created_at, updated_at) 
    VALUES (?, ?, ?, ?, ?)
'''

# Ejecutar la sentencia SQL con los valores correspondientes
    cur.execute(sql, (name, abrev, descrip, created_at, updated_at))
    con.commit()

    print("::: Nuevo pais se ha creado con exito :::")
    input("Presiona Enter para continuar...")
    #os.system('pause')
    fill_tables_menu()

# insertar nuevo departamento -----------------------------------------------------------
def create_departaments():
    os.system('clear')
    print ("::: Complete los campos :::")
    name = input("Nombre del departamento: ")
    abrev = input("Abreviatura: ")
    descrip = input("Descripcion: ")
    id_country = input("Id del pais: ")
    now = datetime.now()
    created_at = now.strftime("%Y-%m-%d %H:%M:%S")
    updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear la sentencia SQL con placeholders para los valores
    sql = f'''
    INSERT INTO departaments (name, abrev, descrip, id_country, created_at, updated_at) 
    VALUES (?, ?, ?, ?, ?,?)
'''
# Ejecutar la sentencia SQL con los valores correspondientes
    cur.execute(sql, (name, abrev, descrip, id_country, created_at, updated_at))
    con.commit()

    print("::: Nuevo pais se ha creado con exito :::")
    input("Presiona Enter para continuar...")
    #os.system('pause')
    fill_tables_menu()

# insertar nuevo ciudad -----------------------------------------------------------
def create_cities():
    os.system('clear')
    print ("::: Complete los campos :::")
    name = input("Nombre de la ciudad: ")
    abrev = input("Abreviatura: ")
    descrip = input("Descripcion: ")
    id_dept = input("Id del departamento: ")
    now = datetime.now()
    created_at = now.strftime("%Y-%m-%d %H:%M:%S")
    updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear la sentencia SQL con placeholders para los valores
    sql = f'''
    INSERT INTO cities (name, abrev, descrip, id_dept, created_at, updated_at) 
    VALUES (?, ?, ?, ?, ?,?)
'''

# Ejecutar la sentencia SQL con los valores correspondientes
    cur.execute(sql, (name, abrev, descrip, id_dept, created_at, updated_at))
    con.commit()

    print("::: Nuevo departamento se ha creado con exito :::")
    input("Presiona Enter para continuar...")
    #os.system('pause')
    fill_tables_menu()

# insertar nuevo user -----------------------------------------------------------
def create_user():
    os.system('clear')
    print ("::: Complete los campos :::")
    email = input("Su correo: ")
    password = input("Su contraseña: ")
    password_hashed = hash_password(password)
    status = input("Estado: ")
    now = datetime.now()
    created_at = now.strftime("%Y-%m-%d %H:%M:%S")
    updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear la sentencia SQL con placeholders para los valores
    sql = f'''
    INSERT INTO user (email, password, status, created_at, updated_at) 
    VALUES (?, ?, ?,?,?)
'''

# Ejecutar la sentencia SQL con los valores correspondientes
    cur.execute(sql, (email, password_hashed, status, created_at, updated_at))
    con.commit()

    print("::: Nuevo usuario se ha creado con exito :::")
    input("Presiona Enter para continuar...")
    #os.system('pause')
    fill_tables_menu()

# insertar nuevo user -----------------------------------------------------------
def create_persons():
    os.system('clear')
    print ("::: Complete los campos :::")
    first_name = input("Ingrese su nombre: ")
    last_name = input("Ingrese sus apellidos: ")
    id_ident_type = input("Id tipo de indentificacion: ")
    ident_number = input("Numero de identidad: ")
    id_exp_city = input("Id ciudad: ")
    address = input("Direccion: ")
    mobile = input("Celular: ")
    id_user = input("Id de usuario: ")
    now = datetime.now()
    created_at = now.strftime("%Y-%m-%d %H:%M:%S")
    updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear la sentencia SQL con placeholders para los valores
    sql = f'''
    INSERT INTO persons (first_name, last_name, id_ident_type, ident_number, id_exp_city, address, mobile, id_user, created_at, updated_at) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

# Ejecutar la sentencia SQL con los valores correspondientes
    cur.execute(sql, (first_name, last_name, id_ident_type, ident_number, id_exp_city, address, mobile, id_user, created_at, updated_at))
    con.commit()

    print("::: Nuevo persona se ha creado con exito :::")
    input("Presiona Enter para continuar...")
    #os.system('pause')
    fill_tables_menu()

# insertar nuevo estudiante -----------------------------------------------------------
def create_students():
    os.system('clear')
    print ("::: Complete los campos :::")
    code = input("codigo de estudiante: ")
    id_person = input("Id persona: ")
    status = input("Estado: ")
    now = datetime.now()
    created_at = now.strftime("%Y-%m-%d %H:%M:%S")
    updated_at = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Crear la sentencia SQL con placeholders para los valores
    sql = f'''
    INSERT INTO students (code, id_person, status, created_at, updated_at) 
    VALUES (?, ?, ?,?,?)
'''

# Ejecutar la sentencia SQL con los valores correspondientes
    cur.execute(sql, (code, id_person, status, created_at, updated_at))
    con.commit()

    print("::: Nuevo estudiante se ha creado con exito :::")
    input("Presiona Enter para continuar...")
    #os.system('pause')
    fill_tables_menu()
    
# Función para manejar la opción de rellenar tablas---------------------------------------------------------
def fill_tables():
    while True:
        choice = fill_tables_menu()
        if choice =='1':
            # Lógica para rellenar tabla de tipos de identificación
            create_identification_type()
        elif choice == '2':
            # Lógica para rellenar tabla de Paises
            create_countries()
        elif choice == '3':
            # Lógica para rellenar tabla de departamentos
            create_departaments()
        elif choice == '4':
            # Lógica para rellenar tabla de ciudades
            create_cities()
        elif choice == '5':
            # Lógica para rellenar tabla de usuarios
            create_user()
        elif choice == '6':
            # Lógica para rellenar tabla de personas
            create_persons()
        elif choice == '7':
            # Lógica para rellenar tabla de estudiantes
            create_students()
        elif choice == '8':
            menu()
        else:
            input("Opción inválida. Presione Enter para continuar.")

# Función para manejar el menu inicial ------------------------------------------------------------
while True:
    choice = menu()
    if choice == "1":
        fill_tables()
    elif choice == "2":
        # Aquí puedes agregar la lógica para consultas
        print("Aun no hay consultas en el script")
        input("Presione cualquier tecla + enter para volver: ")
        menu()
        #pass
    elif choice == "3":
        print("Saliendo...")
        sys.exit()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        input("Presione enter para volver")
        menu()


        
# Llamada a la función fill_tables_menu para mostrar el menú
#menu()

#Close connection
con.close()




