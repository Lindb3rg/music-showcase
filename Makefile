APP_NAME = musicshowcase
MANAGE = python manage.py

# Get current migration
current_migration = $(shell python -c "import os, re; \
	files = sorted([f for f in os.listdir('$(APP_NAME)/migrations') if re.match(r'^[0-9]{4}.*\.py$$', f)]); \
	applied = [f.replace('.py', '') for f in files]; \
	print(applied[-1] if applied else '')")

prev_migration = $(shell python -c "import os, re; \
	files = sorted([f for f in os.listdir('$(APP_NAME)/migrations') if re.match(r'^[0-9]{4}.*\.py$$', f)]); \
	applied = [f.replace('.py', '') for f in files]; \
	print(applied[-2] if len(applied) > 1 else '')")


.PHONY: migrate migratedown list showmigrations makemigrations

run:
	$(MANAGE) runserver

migrateup:
	$(MANAGE) migrate

makemigrations:
	$(MANAGE) makemigrations $(APP_NAME)

list showmigrations:
	$(MANAGE) showmigrations $(APP_NAME)

migratedown:
	@if [ -z "$(prev_migration)" ]; then \
		echo "No previous migration found"; \
	else \
		echo "Rolling back from $(current_migration) to $(prev_migration)"; \
		$(MANAGE) migrate $(APP_NAME) $(prev_migration); \
	fi