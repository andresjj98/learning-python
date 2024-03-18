import sqlite3

con = sqlite3.connect('school.db')

cur = con.cursor()

user_table = '''
   CREATE TABLE IF NOT EXISTS students (
    id INT NOT NULL PRIMARY KEY,
    code VARCHAR(50) NOT NULL,
    id_person INT NOT NULL,
    status BOOLEAN NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    deleted_at DATETIME,
    FOREIGN KEY (id_person) REFERENCES persons(id)
);

CREATE TABLE IF NOT EXISTS identification_types (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    abrev VARCHAR(10) NOT NULL,
    descrip VARCHAR(100) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    deleted_at DATETIME NULL
);

CREATE TABLE IF NOT EXISTS persons (
    id INT NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    id_ident_type INT NOT NULL,
    ident_number VARCHAR(15) NOT NULL,
    id_exp_city INT NOT NULL,
    address VARCHAR(150) NOT NULL,
    mobile VARCHAR(50) NOT NULL,
    id_user INT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    deleted_at DATETIME NULL,
    FOREIGN KEY (id_ident_type) REFERENCES identification_types(id),
    FOREIGN KEY (id_exp_city) REFERENCES cities(id),
    FOREIGN KEY (id_user) REFERENCES user(id)
);

CREATE TABLE IF NOT EXISTS user (
    id INT NOT NULL PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(250) NOT NULL,
    status BOOLEAN NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    deleted_at DATETIME NULL
);

CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    abrev VARCHAR(10) NOT NULL,
    descrip VARCHAR(10) NOT NULL,
    id_dept INT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    deleted_at DATETIME NULL,
    FOREIGN KEY (id_dept) REFERENCES departaments(id)
);

CREATE TABLE IF NOT EXISTS departaments (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    abrev VARCHAR(10) NOT NULL,
    descrip VARCHAR(10) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    deleted_at DATETIME NULL
);
'''

# Ejecutar las consultas
cur.executescript(user_table)

#Save changes in database => Push to database
con.commit()
