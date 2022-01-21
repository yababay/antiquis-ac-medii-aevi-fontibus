SUBDIRS = frontend backend

init: init_backend
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir; \
	done

init_backend:
	python3 -m venv backend
	@echo Don\'t forget to activate virtual enviroment before developvent session.

