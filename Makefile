install:
	uv sync

brain-games:
	uv run brain-games

even:
	uv run brain-even
	
calc:
	uv run brain-calc
	
gcd:
	uv run brain-gcd
	
progression:
	uv run brain-progression

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-upgrade:
	uv tool upgrade hexlet-code

package-uninstall:
	uv tool uninstall hexlet-code

lint:
	uv run ruff check

fix:
	uv run ruff check --fix
