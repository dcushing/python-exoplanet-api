DROP TABLE IF EXISTS exoplanet;

CREATE TABLE exoplanet (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	host_name TEXT NOT NULL,
	planet_letter TEXT NOT NULL,
	planet_name TEXT NOT NULL,
	num_planets_in_system INTEGER,
	discovery_year INTEGER NOT NULL,
	num_moons INTEGER,
	link_to_wiki: TEXT
)