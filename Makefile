REMOTE=f
REMOTE_DIR=savva3
sync:
	rsync -r static-dist/ $(REMOTE):$(REMOTE_DIR)/static/
