Name:		texlive-tex-virtual-academy-pl
Version:	20180303
Release:	1
Summary:	TeXLive tex-virtual-academy-pl package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-virtual-academy-pl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-virtual-academy-pl.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive tex-virtual-academy-pl package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/tex-virtual-academy-pl

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
