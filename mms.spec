Summary:	Matt's MP3 Selector (mms)
Summary(pl):	Textowy frontend na mpg123
Name:		mms
Version:	0.89a
Release:	1
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Source0:	%{name}_%{version}.orig.tar.gz
Patch0:		%{name}-DEBIAN.patch
URL:		http://www.bitchx.org/~bytor/mms.html
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	gpm-devel
Requires:	mpg123
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A nice and quite powerful console mpg123 frontend mms is (as author
said it) the program from which xmms ripped off his name :> It's also
a nice and very nifty (in maintainer's opinion) mpg123 frontend. Much
better than others around. However, contact with author has been lost,
and there are no new versions. But it's still usable :> It was
slightly modified, so try it even if you've seen it and not liked it!

%description -l pl
Mi³a i porêczna nak³adka na mpg123. O wiele lepsza ni¿ wszystkie inne.
Kontakt z autorem zosta³ utracony i nie program ma ju¿ nowych wersji.
Ale ci±gle jest u¿yteczny. Zosta³ nieco zmienony wiêc spróbuj go nawet
je¿eli ju¿ go widzia³e¶ i nie polubi³e¶.

%prep
%setup0 -q
%patch0 -p1 

%build
%{__make} all \
	CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses -DVERSION=\\\"%{version}\\\" -DGPM_SUPPORT" \
	LIBS="-lncurses -lpanel -lgpm"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5}}

install mms $RPM_BUILD_ROOT%{_bindir}
install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install debian/*.5 $RPM_BUILD_ROOT%{_mandir}/man5

gzip -9nf README* BUGS TODO INSTRUCTIONS slrnrc.mms currentmusic.sl mmsrc.example muttrc.mms

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
