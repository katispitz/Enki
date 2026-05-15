# Enki substrate-discipline test runner
# Provides combined Lillu + Enki regression check via single target.
# Lillu has its own Makefile (~/Lillu/Makefile) for Lillu-only test targets.

.PHONY: test test-enki test-all validate help lint lint-fix check

help:
	@echo "Enki — substrate-discipline tasks"
	@echo ""
	@echo "  make test       # Enki tests only"
	@echo "  make test-all   # combined Lillu + Enki regression"
	@echo "  make validate   # canon §30 ↔ engine registry consistency (TBD)"
	@echo "  make lint       # ruff lint (surface bugs only)"
	@echo "  make lint-fix   # ruff lint + safe auto-fix"
	@echo "  make check      # lint + tests"

test:
	@echo "─── Enki tests ───"
	cd $(HOME)/Enki && python3 -m pytest tests/ -q

test-all:
	@echo "─── Enki tests ───"
	cd $(HOME)/Enki && python3 -m pytest tests/ -q
	@echo ""
	@echo "─── Lillu tests ───"
	cd $(HOME)/Lillu && python3 -m pytest tests/ -q
	@echo ""
	@echo "════════════════════════════════════════"
	@echo "ALL SUBSTRATE-DISCIPLINE TESTS PASSED"
	@echo "════════════════════════════════════════"

validate:
	@echo "─── validate_substrate.py ───"
	python3 $(HOME)/Enki/scripts/validate_substrate.py

lint:
	cd $(HOME)/Enki && python3 -m ruff check engines/ tests/

lint-fix:
	cd $(HOME)/Enki && python3 -m ruff check engines/ tests/ --fix

check: lint test
