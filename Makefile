.DEFAULT_GOAL := check

REQUIRED_FILES := README.md LICENSE ATTRIBUTION.md CHANGELOG.md Makefile \
	docs/PROJECT.md docs/ROADMAP.md docs/STATUS.md docs/EDITORIAL_GUIDE.md \
	docs/ARCHITECTURE.md docs/DECISIONS.md docs/QA_PROTOCOL.md

.PHONY: check check-files check-diff check-scope

check: check-files check-diff check-scope

check-files:
	@set -e; for file in $(REQUIRED_FILES); do \
		if [ ! -s "$$file" ]; then \
			printf 'Archivo obligatorio ausente o vacío: %s\n' "$$file" >&2; \
			exit 1; \
		fi; \
	done

check-diff:
	git diff --check HEAD

check-scope:
	@set -e; files="$$(git ls-files --cached --others --exclude-standard -- \
		original/ translation/ assets/ ':(icase,glob)**/*.pdf' \
		':(exclude,glob)**/.gitkeep')"; \
	if [ -n "$$files" ]; then \
		printf 'Archivos fuera de esta fase:\n%s\n' "$$files" >&2; \
		exit 1; \
	fi
