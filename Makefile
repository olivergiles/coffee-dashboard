.PHONY: test
test:
	pytest

.PHONY: local-dev
	streamlit run run.py --reload
