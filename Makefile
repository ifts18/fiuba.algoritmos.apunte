# Makefile for LaTeX files

# Original Makefile from http://www.math.psu.edu/elkin/math/497a/Makefile
# Please check http://www.acoustics.hut.fi/u/mairas/UltimateLatexMakefile
# for new versions.

# Copyright (c) 2005,2006 (in order of appearance):
#	Matti Airas <Matti.Airas@hut.fi>
#	Rainer Jung
#	Antoine Chambert-Loir
#	Timo Kiravuo

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

PDFLATEX   = xelatex -interaction=nonstopmode -halt-on-error
BIBTEX	   = bibtex
MAKEINDEX  = makeindex

RERUN      = "(There were undefined references|Rerun to get (cross-references|the bars) right)"
RERUNBIB   = "No file.*\.bbl|Citation.*undefined"
MAKEIDX    = "^[^%]*\\makeindex"
MPRINT     = "^[^%]*print"
USETHUMBS  = "^[^%]*thumbpdf"

DATE       = $(shell date +%Y-%m-%d)

BASENAME   = $(<:%.tex=%)
LOGFILE    = $(<:%.tex=%.log)
TOCFILE    = $(<:%.tex=%.toc)
TOCBAKFILE = $(<:%.tex=%.toc.bak)

COPY       = if test -r $(TOCFILE); then cp $(TOCFILE) $(TOCBAKFILE); fi
RM         = rm -f
OUTDATED   = echo "EPS-file is out-of-date!" && false

# These are OK

SRC	  := $(shell egrep -l '^[^%]*\\begin\{document\}' *.tex)
TRG	   = $(SRC:%.tex=%.pdf)

define run-pdflatex
	$(COPY); $(PDFLATEX) $<
	egrep $(MAKEIDX) $< && ($(MAKEINDEX) $(BASENAME); $(COPY); $(PDFLATEX) $<) > /dev/null; true
	egrep -c $(RERUNBIB) $(LOGFILE) && ($(BIBTEX) $(BASENAME); $(COPY); $(PDFLATEX) $<); true
	egrep $(RERUN) $(LOGFILE) && ($(COPY); $(PDFLATEX) $<) >/dev/null; true
	egrep $(RERUN) $(LOGFILE) && ($(COPY); $(PDFLATEX) $<) >/dev/null; true
	if cmp -s $(TOCFILE) $(TOCBAKFILE); then true; else $(PDFLATEX) $<; fi
	$(RM) $(TOCBAKFILE)
	# Display relevant warnings
	egrep -i "(Reference|Citation).*undefined" $(LOGFILE); true
endef

define get_dependencies
	deps=`perl -ne '($$_)=/^[^%]*\\\(?:include|input)\{(.*?)\}/;@_=split /,/;foreach $$t (@_) {print "$$t.tex "}' $<`
endef

define getbibs
	bibs=`perl -ne '($$_)=/^[^%]*\\\bibliography\{(.*?)\}/;@_=split /,/;foreach $$b (@_) {print "$$b.bib "}' $< $$deps`
endef

define getpdfs
	pdfs=`perl -ne '@foo=/^[^%]*\\\(includegraphics|psfig)(\[.*?\])?\{(.*?)\}/g;if (defined($$foo[2])) { if ($$foo[2] =~ /.pdf$$/) { print "$$foo[2] "; } else { print "$$foo[2].pdf "; }}' $< $$deps`
endef

define manconf
	mandeps=`if test -r $(basename $@).cnf ; then cat $(basename $@).cnf |tr -d '\n\r' ; fi`
endef

.PHONY	: default all pdf clean veryclean

default : apunte.pdf ejercicios.pdf

all	: $(TRG)

clean	:
	-rm -f $(TRG) $(TRG:%.pdf=%.aux) $(TRG:%.pdf=%.bbl) \
	    $(TRG:%.pdf=%.blg) $(TRG:%.pdf=%.log) $(TRG:%.pdf=%.out) \
	    $(TRG:%.pdf=%.idx) $(TRG:%.pdf=%.ilg) $(TRG:%.pdf=%.ind) \
	    $(TRG:%.pdf=%.toc) $(TRG:%.pdf=%.xtr) $(TRG:%.pdf=%.d) \
	    ejercicios.tex

veryclean : clean
	  -rm -f *.log *.aux *.bbl *.blg *.ilg *.toc *.lof *.lot *.idx *.ind *.ps *~

# This is a rule to generate a file of prerequisites for a given .tex file
%.d	: %.tex
	$(get_dependencies) ; echo $$deps ; \
	$(getbibs) ; echo $$bibs ; \
	$(getpdfs) ; echo $$pdfs ; \
	$(manconf) ; echo  $$mandeps  ;\
	echo "$*.pdf $@ : $< $$deps $$bibs $$pdfs $$mandeps" > $@

-include $(SRC:.tex=.d)

# Dependencia adicional para ejercicios.tex.
ejercicios.tex : apunte.pdf

%.pdf : %.tex | %.d
	@$(run-pdflatex)

pdf    : $(TRG)
