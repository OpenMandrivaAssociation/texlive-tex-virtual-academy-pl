%global tl_name tex-virtual-academy-pl
%global tl_revision 67718

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	TeX usage web pages, in Polish
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/tex-virtual-academy-pl
License:	fdl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-virtual-academy-pl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-virtual-academy-pl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
TeX Virtual Academy is a bundle of Polish documentation in HTML format
about TeX and Co. It contains information for beginners, LaTeX packages,
descriptions, etc.

