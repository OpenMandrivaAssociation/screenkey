Name:		screenkey
Version:	1.5
Release:	1
Summary:	A screen-cast tool to show your keys and based on key-mon project
Group:		Video/Utilities
License:	GPLv2+
URL:		https://gitlab.com/screenkey/screenkey/
Source0:	https://www.thregr.org/~wavexx/software/screenkey/releases/%{name}-%{version}.tar.gz
Patch1:		0001-Port-to-Ayatana-AppIndicator.patch
BuildArch:	noarch
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
#BuildRequires:	python3dist(setuptools-git)
BuildRequires:	python3dist(babel)

Recommends:	slop

%description
A screen-cast tool to show your keys inspired by Screenflick and based on
the key-mon project.

%prep
%autosetup -p1

# Remove bundled egg-info
rm -rf %{name}.egg-info

sed -i 's/^Categories=.*/Categories=AudioVideo;Video;Recorder;/' data/screenkey.desktop
sed -i '/^Version=/d' data/screenkey.desktop

%build
%py_build

%install
%py_install

%find_lang %{name}

%files -f %{name}.lang
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/org.thregr.%{name}.metainfo.xml
%dir %{python_sitelib}/Screenkey/
%{python_sitelib}/Screenkey/__pycache__/
%{python_sitelib}/Screenkey/images/
%{python_sitelib}/Screenkey/*.py*
%{python_sitelib}/%{name}-%{version}-py%{python_version}.egg-info
