INSTALL_DIR := /usr/local/bin
SCRIPT_NAME := json_to_csv.py
INSTALL_PATH := $(INSTALL_DIR)/$(SCRIPT_NAME)

all: install

install: $(INSTALL_PATH)

$(INSTALL_PATH): $(SCRIPT_NAME)
	install $(SCRIPT_NAME) $(INSTALL_PATH)

