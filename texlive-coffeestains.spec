Name:		texlive-coffeestains
Version:	59703
Release:	2
Summary:	Add coffee stains to documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/coffeestains
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coffeestains.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coffeestains.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an essential feature that LaTeX has been
missing for too long: It adds coffee stains to your documents.
A lot of time can be saved by printing stains directly on the
page rather than adding them manually.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/coffeestains
%doc %{_texmfdistdir}/doc/latex/coffeestains

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
