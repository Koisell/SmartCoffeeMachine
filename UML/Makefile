UMLC=plantuml
PNGDIR=Diagrams
SRC= $(wildcard *UML.txt)
OBJ= $(SRC:.txt=.png)
MKFIL_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))

all: $(PNGDIR)/$(OBJ)

$(PNGDIR)/%png: %txt
	$(UMLC) $< -o $(PNGDIR)

%.png: %.txt
	$(UMLC) $< -o $(PNGDIR)

clean:
	find ./Diagrams -type f -name "*UML.png" -delete