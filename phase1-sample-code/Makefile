# Requirements:
#
# - curl, tar, and xz (for extracting the typst .tar.xz archive)
# - Assumes 64-bit Linux (amd64/x86_64).
#   If pandoc and typst are already on PATH, they are used
#   directly and nothing is downloaded.
#
# Notes:
#
# - PANDOC_VERSION and TYPST_VERSION pin the versions of these tools
#   if a download is needed. Bump them to pull a newer release.
# - We check whether pandoc and typst are already on PATH. If so, those are
#   used as-is. Otherwise we depend on bin/pandoc / bin/typst, which are
#   downloaded from the project GitHub release pages and extracted into ./bin.
#
# Porting to other platforms:
#
# - macOS: change PANDOC_URL to a "-macOS" asset (a .pkg, so the
#   download/extract recipe would need to change), and TYPST_URL to
#   an "apple-darwin" .tar.xz asset (extraction stays the same).
# - Windows: pandoc ships a .zip/.msi, typst ships a .zip; both the
#   archive extension and extraction commands (tar -> unzip) would
#   need to change accordingly.

SHELL := /bin/bash

.DELETE_ON_ERROR:

REPORT := phase-1-report-group-16

PANDOC_VERSION := 3.10.1
TYPST_VERSION  := 0.15.0

# Prefer tools already on PATH; otherwise fall back to local copies that
# we download into ./bin.
BIN_DIR := bin

PANDOC := $(shell command -v pandoc 2>/dev/null)
ifeq ($(PANDOC),)
PANDOC := $(BIN_DIR)/pandoc
endif

TYPST := $(shell command -v typst 2>/dev/null)
ifeq ($(TYPST),)
TYPST := $(BIN_DIR)/typst
endif

PANDOC_DIST := pandoc-$(PANDOC_VERSION)-linux-amd64
PANDOC_URL  := https://github.com/jgm/pandoc/releases/download/$(PANDOC_VERSION)/$(PANDOC_DIST).tar.gz

TYPST_DIST := typst-x86_64-unknown-linux-musl
TYPST_URL  := https://github.com/typst/typst/releases/download/v$(TYPST_VERSION)/$(TYPST_DIST).tar.xz

.PHONY: all clean

all: $(REPORT).pdf

$(REPORT).pdf: $(REPORT).md $(PANDOC) $(TYPST)
	PATH="$(BIN_DIR):$$PATH" $(PANDOC) --pdf-engine=typst -o $@ $<

# Fetch Pandoc if needed
$(BIN_DIR)/pandoc:
	mkdir -p $(BIN_DIR)
	@echo "Downloading pandoc $(PANDOC_VERSION)..."
	curl -fL -o /tmp/pandoc.tar.gz "$(PANDOC_URL)"
	tar -xzf /tmp/pandoc.tar.gz -C /tmp
	cp /tmp/$(PANDOC_DIST)/bin/pandoc $(BIN_DIR)/pandoc
	chmod +x $(BIN_DIR)/pandoc
	rm -rf /tmp/pandoc.tar.gz /tmp/$(PANDOC_DIST)

# Fetch typst if needed
$(BIN_DIR)/typst:
	mkdir -p $(BIN_DIR)
	@echo "Downloading typst $(TYPST_VERSION)..."
	curl -fL -o /tmp/typst.tar.xz "$(TYPST_URL)"
	tar -xJf /tmp/typst.tar.xz -C /tmp
	cp /tmp/$(TYPST_DIST)/typst $(BIN_DIR)/typst
	chmod +x $(BIN_DIR)/typst
	rm -rf /tmp/typst.tar.xz /tmp/$(TYPST_DIST)

clean:
	rm -f $(REPORT).pdf
