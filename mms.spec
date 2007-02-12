Summary:	Matt's MP3 Selector (mms)
Summary(pl.UTF-8):   Textowy frontend na mpg123
Name:		mms
Version:	0.89a
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	%{name}_%{version}.orig.tar.gz
# Source0-md5:	13c15deb92437b1a8dc5126df3c55bcf
#Source0:	http://www.bitchx.org/bytor/%{name}-%{version}.tgz
Patch0:		%{name}-DEBIAN.patch
# dead
#URL:		http://www.bitchx.org/bytor/mms.html
BuildRequires:	gpm-devel
BuildRequires:	ncurses-ext-devel >= 5.2
Requires:	mpg123
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A nice and quite powerful console mpg123 frontend mms is (as author
said it) the program from which xmms ripped off his name :> It's also
a nice and very nifty (in maintainer's opinion) mpg123 frontend. Much
better than others around. However, contact with author has been lost,
and there are no new versions. But it's still usable :> It was
slightly modified, so try it even if you've seen it and not liked it!

%description -l pl.UTF-8
Miła i poręczna nakładka na mpg123. O wiele lepsza niż wszystkie inne.
Kontakt z autorem został utracony i nie program ma już nowych wersji.
Ale ciągle jest użyteczny. Został nieco zmieniony więc spróbuj go nawet
jeżeli już go widziałeś i nie polubiłeś.

%prep
%setup -q
%patch0 -p1

%build
%{__make} all \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	LIBS="-lncurses -lpanel -lgpm" \
	PWD=`pwd`

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5}}

install mms $RPM_BUILD_ROOT%{_bindir}
install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install debian/*.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* BUGS TODO INSTRUCTIONS slrnrc.mms currentmusic.sl mmsrc.example muttrc.mms
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
