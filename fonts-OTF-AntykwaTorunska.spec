%define		_name	AntykwaTorunska
Summary:	Twoelement antiqua designed by a famous torunian typographer
Summary(pl):	Dwuelementowa antykwa zaprojektowana przez znanego toru�skiego typografa
Name:		fonts-OTF-AntykwaTorunska
Version:	2.01
Release:	1
License:	GPL
Group:		Fonts
Source0:	http://www.janusz.nowacki.strefa.pl/pliki/%{_name}-otf-%(echo %{version} | tr '.' '_').zip
# Source0-md5:	b8488a6b5b3b025205c322f93711806e
URL:		http://www.janusz.nowacki.strefa.pl/torunska.html
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/OTF
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_otffontsdir	%{_fontsdir}/OTF

%description
Antykwa (typeface based on latin handwriting style) Torunska was cast
in 1960 in Odlewnia Czcionek Grafmasz in Warsaw. It was produced in
the following variants: regural, semi-bold, semi-italic. It was used
mainly for putting together accidences, poetry and titularities. In
1996 the first version of Antykwa Torunska was made in Type1
(Postscript) format. Those fonts, like their lead predecessors,
included regular, regular italic and bold styles. In 2004 works upon
2.01 have been finished. Thanks to the METATYPE1 technology the fonts
are technically correct and greatly extended. Version 2.01 of Antykwa
Torunska includes over 1000 symbols (apart from standard ASCII, nautic
numbers; cyrillic, greek, vietnameese, mathematic characters, etc.).

%description -l pl
Antykw� (kr�j pisma wzorowany na kszta�cie r�cznego pisma �aci�skiego)
Toru�sk� odlano pierwszy raz w 1960 roku w Odlewni Czcionek Grafmasz w
Warszawie. Produkowana by�a w odmianach: zwyk�ej, p�grubej i
pochy�ej. Pismo to u�ywane by�o g��wnie do sk�adania akcydens�w,
poezji i tytulari�w.

W 1996 roku wykonano pierwsz� wersj� font�w Antykwy Toru�skiej w
formacie Type1 (PostScript). Fonty te, tak jak oryginalne o�owiane
czcionki, zawiera�y style regular, regular italic i bold. W 2004 roku
zako�czono prace nad now� wersj� font�w oznaczon� numerem 2.01. Dzi�ki
zastosowaniu oprogramowania METATYPE1 (autorstwa Bogus�awa
Jackowskiego, Janusza M. Nowackiego i Piotra Strzelczyka) fonty s�
poprawione pod wzgl�dem technologicznym oraz znacznie rozszerzone.
Wersja 2.01 Antykwy Toru�skiej zawiera ponad 1000 znak�w (poza
standardowym zestawem r�wnie� cyfry nautyczne, znaki cyryliczne,
greckie, wietnamskie, matematyczne itp.).

%prep
%setup -q -c -n %{_name}-otf-%(echo %{version} | tr '.' '_')

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_otffontsdir}

install *.otf $RPM_BUILD_ROOT%{_otffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%{_otffontsdir}/*
