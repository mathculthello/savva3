REMOTE=f
REMOTE_DIR=savva3

push: build sync

build:
	npm run build
sync:
	rsync -r static-dist/ $(REMOTE):$(REMOTE_DIR)/static/

getbasefix:
	ssh $(REMOTE) "cd $(REMOTE_DIR); venv/bin/python3 savva3/manage.py dumpdata base" > base/fixtures/base.json

getremotedb:
	scp $(REMOTE):$(REMOTE_DIR)/db.sqlite3 ../


fixtures:
	./manage.py dumpdata $(APP) > $(APP)/fixtures/$(APP).json	
