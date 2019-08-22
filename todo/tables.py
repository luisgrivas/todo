# Autor: Luis G Rivas

tasks = """ CREATE TABLE IF NOT EXISTS tasks (
			id integer PRIMARY KEY,
			name text NOT NULL,
			priority integer,
			status_id integer NOT NULL,
			project_id integer NOT NULL,
			begin_date date NOT NULL,
			end_date date
			);
		"""

tb_list = [tasks]