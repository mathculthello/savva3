REMOTE=f
REMOTE_DIR=savva3

frontend: build install

build:
	npm run build
install:
	rsync -r static-dist/ $(REMOTE):$(REMOTE_DIR)/static/

getbasefix:
	ssh $(REMOTE) "cd $(REMOTE_DIR); venv/bin/python3 savva3/manage.py dumpdata base" > base/fixtures/base.json

getdb:
	scp $(REMOTE):$(REMOTE_DIR)/db.sqlite3 ../


fixtures:
	./manage.py dumpdata $(APP) > $(APP)/fixtures/$(APP).json	
