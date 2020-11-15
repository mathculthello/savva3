# DEPENDS ON
# node npm rsync scp
#
REMOTE=savvateev.xyz
REMOTE_DIR=/app/savva3
TAG=aeifn/savva3

build:
	docker build -t $(TAG) . 
	docker build -t $(TAG)-nginx nginx

push:
	docker push $(TAG)
	docker push $(TAG)-nginx

.PHONY: node_modules
node_modules:
	docker run --rm -v $(PWD):/code -w /code node:10 npm install

frontend-install:
	rsync -r static-dist/ $(REMOTE):$(REMOTE_DIR)/static/

getbasefix:
	ssh $(REMOTE) "cd $(REMOTE_DIR); venv/bin/python3 savva3/manage.py dumpdata base" > base/fixtures/base.json

syncdb:
	scp $(REMOTE):$(REMOTE_DIR)/db.sqlite3 ../


fixtures:
	./manage.py dumpdata $(APP) > $(APP)/fixtures/$(APP).json	
