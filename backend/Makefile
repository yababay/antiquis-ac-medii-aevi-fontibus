all:
	export BACKEND_TEST=123
	@if [ -z "`env | grep VIRTUAL_ENV`"]; then \
		echo "No virtual env detected. Please run\n\n. bin/activate\n\nin this directory.";  \
		else \
		pip3 install -r requirements.txt; \
		fi

