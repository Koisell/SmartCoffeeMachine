UMLC=plantuml
PNGDIR=Diagrams
SRC= $(wildcard *UML.txt)
OBJ= $(SRC:.txt=.png)

all: $(PNGDIR)/$(OBJ)

%.png: %.txt
	$(UMLC) $< -o $(PNGDIR)