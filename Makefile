SUBDIRS = frontend backend
IMAGE_NAME = "fontibus.azurecr.io/history/antiquis-ac-medii-aevi"

init: init_backend
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir; \
	done

init_backend:
	@python3 -m venv backend
	@echo Don\'t forget to activate virtual enviroment before developvent session.

docker: docker_clean
	@docker build -t ${IMAGE_NAME} .

docker_run:
	@docker run --rm -it -p 8080:8080 ${IMAGE_NAME}

docker_clean:
	@docker images | grep antiquis-ac-medii-aevi | egrep '[a-z0-9]{10}' -o | while read l; do docker rmi $$l; done

