Name:		scws
Version:	1.2.3
Release:	1%{?dist}
Summary:	SCWS is an acronym for Simple Chinese Word Segmentation (ie, Simple Chinese Word Segmentation System).
License:	BSD
URL:		http://www.xunsearch.com/scws/
Source0:	http://www.xunsearch.com/scws/down/%{name}-%{version}.tar.bz2

%description

SCWS is an acronym for Simple Chinese Word Segmentation (ie, Simple Chinese Word Segmentation System).

This is a mechanical Chinese word segmentation engine based on word frequency dictionaries. It can divide a whole segment of Chinese text into words. Words are the smallest morpheme units in Chinese, but they are not separated by spaces when they are written in English. Therefore, how to accurately and quickly segment words has always been a difficult problem in Chinese word segmentation.

SCWS is developed in pure C language, does not depend on any external library functions, and can directly use dynamic link library to embed applications. Supported Chinese encoding includes GBK, UTF-8 and so on. There is also a PHP extension module for quick and easy use of word segmentation in PHP.

The word segmentation algorithm does not have many innovative components. It uses the word frequency dictionary collected by itself, and is supplemented by a certain proprietary name, name, place name, and digital age rule to achieve basic word segmentation. The accuracy of small-scale test is 90. Between ~ 95%, it can basically meet the needs of some small search engines, keyword extraction and other occasions. The first prototype version was released at the end of 2005.

SCWS was developed by hightman , and is open sourced under the BSD license agreement. The source code is hosted on github .


%prep
%setup -q


%build
%configure --prefix=%{_prefix} --mandir=%{_mandir} --sysconfdir=/etc/scws
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
/etc/scws/
/usr/bin/scws
/usr/bin/scws-gen-dict
/usr/include/scws/
/usr/lib64/libscws.la
/usr/lib64/libscws.so
/usr/lib64/libscws.so.1
/usr/lib64/libscws.so.1.1.0


%changelog
* Thu Apr 12 2018 Kevin Coakley <kcoakley@sdsc.edu>
– Initial rpm build
