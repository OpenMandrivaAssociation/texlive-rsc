# revision 20942
# category Package
# catalog-ctan /macros/latex/contrib/rsc
# catalog-date 2011-01-05 00:05:34 +0100
# catalog-license gpl
# catalog-version 3.1e
Name:		texlive-rsc
Version:	3.1e
Release:	6
Summary:	BibTeX style for use with RSC journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rsc
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rsc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rsc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rsc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The rsc package provides a BibTeX style in accordance with the
requirements of the Royal Society of Chemistry. It was
originally based on the file pccp.bst, but also implements a
number of styles from the achemso package. The package is now a
stub for the chemstyle package, which the author developed to
unify the writing of articles with a chemistry content.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/rsc/angew.bst
%{_texmfdistdir}/bibtex/bst/rsc/rsc.bst
%{_texmfdistdir}/tex/latex/rsc/rsc.sty
%doc %{_texmfdistdir}/doc/latex/rsc/README
%doc %{_texmfdistdir}/doc/latex/rsc/rsc-demo.tex
%doc %{_texmfdistdir}/doc/latex/rsc/rsc.bib
%doc %{_texmfdistdir}/doc/latex/rsc/rsc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/rsc/rsc.dtx
%doc %{_texmfdistdir}/source/latex/rsc/rsc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.1e-2
+ Revision: 755728
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.1e-1
+ Revision: 719466
- texlive-rsc
- texlive-rsc
- texlive-rsc
- texlive-rsc

