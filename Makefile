dbinit:
	sudo -u postgres dropdb lolth
	sudo -u postgres createdb -O lolth lolth
	echo "CREATE EXTENSION postgis;\
	CREATE EXTENSION postgis_topology;" | sudo -u postgres psql lolth

	python manage.py syncdb
	python manage.py shell < load-load.py
	
