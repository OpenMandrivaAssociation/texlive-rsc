Name:		texlive-rsc
Version:	3.1f
Release:	2
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
%{_texmfdistdir}/bibtex/bst/rsc
%{_texmfdistdir}/tex/latex/rsc
%doc %{_texmfdistdir}/doc/latex/rsc
#- source
%doc %{_texmfdistdir}/source/latex/rsc

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
