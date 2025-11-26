import psycopg2
from decimal import Decimal
import datetime

DB_CONFIG = {
    'dbname': 'test_db',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

def test_fn_calcular_descuento():
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        cur.execute("SELECT fn_calcular_descuento(100.00, 20.0);")
        resultado1 = cur.fetchone()[0]
        assert resultado1 == Decimal('80.00')

        cur.execute("SELECT fn_calcular_descuento(250.50, 15.5);")
        resultado2 = cur.fetchone()[0]
        assert resultado2 == Decimal('211.67')

    finally:
        if conn:
            conn.rollback()
            if cur:
                cur.close()
            conn.close()

def test_fn_validar_email():
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        cur.execute("SELECT fn_validar_email('test@dominio.com');")
        assert cur.fetchone()[0] == True

        cur.execute("SELECT fn_validar_email('test.dominio.com');")
        assert cur.fetchone()[0] == False

        cur.execute("SELECT fn_validar_email('');")
        assert cur.fetchone()[0] == False

    finally:
        if conn:
            conn.rollback()
            if cur:
                cur.close()
            conn.close()

def test_fn_productos_bajo_stock():
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        cur.execute("SELECT nombre FROM fn_productos_bajo_stock(3);")

        resultados = cur.fetchall()
        nombres = [row[0] for row in resultados]

        assert len(nombres) == 2
        assert "Celular" in nombres
        assert "Cargador" in nombres

    finally:
        if conn:
            conn.rollback()
            if cur:
                cur.close()
            conn.close()

def test_fn_dia_de_la_semana():
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        test_date = datetime.date(2025, 1, 1)

        cur.execute("SELECT fn_dia_de_la_semana(%s);", (test_date,))

        dia_semana = cur.fetchone()[0]

        assert dia_semana in ("Miércoles", "Wednesday")

    finally:
        if conn:
            conn.rollback()
            if cur:
                cur.close()
            conn.close()

def test_fn_contar_empleados_depto():
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        cur.execute("SELECT fn_contar_empleados_depto(2);")
        conteo_ing = cur.fetchone()[0]
        assert conteo_ing == 2

        cur.execute("SELECT fn_contar_empleados_depto(1);")
        conteo_ventas = cur.fetchone()[0]
        assert conteo_ventas == 2

        cur.execute("SELECT fn_contar_empleados_depto(99);")
        conteo_nulo = cur.fetchone()[0]
        assert conteo_nulo == 0

    finally:
        if conn:
            conn.rollback()
            if cur:
                cur.close()
            conn.close()
