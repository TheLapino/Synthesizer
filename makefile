path := .

# Path: src
src_path := $(path)/src

.PHONY: run-windows
# run the main.py of the project and export the PYTHONPATH
run-windows:
	@echo "Running main.py"
	@set PYTHONPATH=%PYTHONPATH%;$(src_path) && python $(src_path)/main.py
