.DEFAULT_GOAL := check

REQUIRED_FILES := README.md LICENSE ATTRIBUTION.md CHANGELOG.md Makefile \
	docs/PROJECT.md docs/ROADMAP.md docs/STATUS.md docs/EDITORIAL_GUIDE.md \
	docs/ARCHITECTURE.md docs/DECISIONS.md docs/QA_PROTOCOL.md \
	reports/source-audit.md original/source-v3/INVENTORY.md original/source-v3/SHA256SUMS

.PHONY: check check-files check-diff check-scope check-source

check: check-files check-diff check-scope check-source

check-files:
	@set -e; for file in $(REQUIRED_FILES); do \
		if [ ! -s "$$file" ]; then \
			printf 'Archivo obligatorio ausente o vacío: %s\n' "$$file" >&2; \
			exit 1; \
		fi; \
	done

# Preserve the original TeX bytes, including upstream whitespace.
check-diff:
	git diff --check HEAD -- . ':(exclude)original/source-v3/book.tex'

check-scope:
	@set -e; files="$$(git ls-files --cached --others --exclude-standard -- \
		original/ translation/ assets/ ':(icase,glob)**/*.pdf' \
		':(exclude,glob)**/.gitkeep' ':(exclude)original/source-v3/')"; \
	if [ -n "$$files" ]; then \
		printf 'Archivos fuera de esta fase:\n%s\n' "$$files" >&2; \
		exit 1; \
	fi

check-source:
	@set -e; cd original/source-v3; \
	sha256sum --strict --quiet --check SHA256SUMS; \
	expected="$$( { cut -c67- SHA256SUMS; printf '%s\n' INVENTORY.md SHA256SUMS; } | LC_ALL=C sort)"; \
	actual="$$(find . -mindepth 1 ! -type d | cut -c3- | LC_ALL=C sort)"; \
	if [ "$$actual" != "$$expected" ]; then \
		printf 'El inventario de original/source-v3 no coincide con los archivos.\n' >&2; \
		exit 1; \
	fi
