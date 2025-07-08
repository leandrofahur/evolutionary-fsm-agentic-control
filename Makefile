lint:
	ruff check . --fix
	format:
	black .
	lint-fix: format lint
