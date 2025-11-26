CREATE OR REPLACE FUNCTION fn_calcular_descuento(
    p_precio_original NUMERIC,
    p_porcentaje NUMERIC
)
RETURNS NUMERIC AS $$
DECLARE
    v_precio_final NUMERIC;
BEGIN
    v_precio_final := p_precio_original * (1 - (p_porcentaje / 100));
    RETURN ROUND(v_precio_final, 2); 
END;
$$ LANGUAGE plpgsql;

--2 validar mail
CREATE OR REPLACE FUNCTION fn_validar_email(
    p_email TEXT
)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN POSITION('@' IN p_email) > 0;
END;
$$ LANGUAGE plpgsql;

--3 devolver productos con bajo stock
CREATE OR REPLACE FUNCTION fn_productos_bajo_stock(
    p_cantidad_minima INT
)
RETURNS SETOF productos AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM productos
    WHERE stock < p_cantidad_minima
    ORDER BY stock ASC;
END;
$$ LANGUAGE plpgsql;

--4 devolver día de la semana
CREATE OR REPLACE FUNCTION fn_dia_de_la_semana(
    p_fecha DATE
)
RETURNS TEXT AS $$
    SELECT TO_CHAR(p_fecha, 'TMDay');
$$ LANGUAGE sql IMMUTABLE;

--5 contar empleados por departamento
CREATE OR REPLACE FUNCTION fn_contar_empleados_depto(
    p_id_depto INT
)
RETURNS INT AS $$
DECLARE
    v_conteo INT;
BEGIN
    SELECT COUNT(*) INTO v_conteo
    FROM empleados
    WHERE id_depto = p_id_depto;

    RETURN v_conteo;
END;
$$ LANGUAGE plpgsql STABLE;
