CREATE TABLE productos (
  id SERIAL PRIMARY KEY,
  nombre TEXT,
  precio NUMERIC(10,2),
  stock INT
);

CREATE TABLE departamentos (
  id_depto SERIAL PRIMARY KEY,
  nombre_depto TEXT NOT NULL
);

CREATE TABLE empleados (
  id_empleado SERIAL PRIMARY KEY,
  nombre TEXT,
  email TEXT,
  id_depto INT REFERENCES departamentos(id_depto)
);
