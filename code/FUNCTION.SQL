CREATE OR REPLACE FUNCTION quantidade_generos()
RETURNS integer AS $$
	DECLARE
		valor integer;
	BEGIN
		SELECT count(genero.id) FROM genero INTO valor;
			RETURN valor;
	END;
$$ LANGUAGE plpgsql;