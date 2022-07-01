.PHONY: test
test:
	pytest

.PHONY: local-dev
local-dev:
	streamlit run run.py
