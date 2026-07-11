%global tl_name coffeestains
%global tl_revision 59703

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5.1
Release:	%{tl_revision}.1
Summary:	Add coffee stains to documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/coffeestains
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/coffeestains.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/coffeestains.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an essential feature that LaTeX has been missing
for too long: It adds coffee stains to your documents. A lot of time can
be saved by printing stains directly on the page rather than adding them
manually.

