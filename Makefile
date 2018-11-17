REMOTE=f
REMOTE_DIR=savva3

push: build sync

build:
	npm run build
sync:
	rsync -r static-dist/ $(REMOTE):$(REMOTE_DIR)/static/

