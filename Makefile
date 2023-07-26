.DEFAULT_GOAL := help

SHELL=/bin/bash
VENV = venv

ifeq ($(OS),Windows_NT)
	VENV_BIN=$(VENV)/Scripts
else
	VENV_BIN=$(VENV)/bin
endif

venv:  ## Set up virtual environment. Last step potentially to be replaced with pip install ultima
	python3 -m venv $(VENV)
	$(VENV_BIN)/python -m pip install --upgrade pip
	$(VENV_BIN)/pip install -r requirements.txt
	$(VENV_BIN)/pip install -r requirements-lint.txt
#$(VENV_BIN)/pip install ultibi
#@unset CONDA_PREFIX && source $(VENV_BIN)/activate && cd ../pyultima && maturin develop --features=CRR2 --release

data:
	@mkdir -p ./data/frtb
#	Commenting out since we can't align the same config for tests, book, EFS etc 
# 	This book will have it's own config
#	wget -N -q --no-check-certificate https://ultima-bi.s3.eu-west-2.amazonaws.com/frtb/datasource_config.toml -O ./data/frtb/datasource_config.toml
	wget -N -q --no-check-certificate https://ultima-bi.s3.eu-west-2.amazonaws.com/frtb/Delta.csv              -O ./data/frtb/Delta.csv
	wget -N -q --no-check-certificate https://ultima-bi.s3.eu-west-2.amazonaws.com/frtb/hms.csv                -O ./data/frtb/hms.csv
	wget -N -q --no-check-certificate https://ultima-bi.s3.eu-west-2.amazonaws.com/frtb/TradeAttributes.csv    -O ./data/frtb/TradeAttributes.csv
#	wget -N -q --no-check-certificate https://ultima-bi.s3.eu-west-2.amazonaws.com/titanic.csv    			   -O ./data/titanic.csv

.PHONY: fmt
fmt: venv  ## Run autoformatting and linting
	$(VENV_BIN)/black .
	$(VENV_BIN)/mdformat .

.PHONY: run
run: data
	for f in src/examples/*.py; do $(VENV_BIN)/python $$f; done
# without make: for f in src/examples/*.py; do venv/scripts/python "$f"; done

.PHONY: clean
clean:  ## Clean up caches and build artifacts
	@rm -rf venv/
	@rm -rf target/
	-@rm -fr .venv
	-@rm -fr data
	mdbook clean &>/dev/null

.PHONY: help
help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m\n"
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort
