%global tl_name rsc
%global tl_revision 41923

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1f
Release:	%{tl_revision}.1
Summary:	BibTeX style for use with RSC journals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rsc
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rsc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rsc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rsc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The rsc package provides a BibTeX style in accordance with the
requirements of the Royal Society of Chemistry. It was originally based
on the file pccp.bst, but also implements a number of styles from the
achemso package. The package is now a stub for the chemstyle package,
which the author developed to unify the writing of articles with a
chemistry content.

