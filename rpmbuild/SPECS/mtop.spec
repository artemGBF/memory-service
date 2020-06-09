Name:       mtop
Version:    1
Release:    1
Summary:    Most simple RPM package
License:    gpl
Source0:    mtop.tar.xz

%description
This is my RPM package.

%prep
# we have no source, so nothing here

%build
pwd
tar -xJvf ../SOURCES/mtop.tar.xz

%install
mkdir -p %{buildroot}/usr/bin/mtop
mkdir -p %{buildroot}/etc/systemd/system/
mkdir -p %{buildroot}/usr/share/man/ru/man1/
install -m 755 mtop.sh %{buildroot}/usr/bin/mtop/mtop.sh
install -m 755 mtop.service %{buildroot}/etc/systemd/system/mtop.service
install -m 755 mtop.1.gz %{buildroot}/usr/share/man/ru/man1/

%files
/usr/bin/mtop/mtop.sh
/etc/systemd/system/mtop.service
/usr/share/man/ru/man1/mtop.1.gz

%changelog
# let's skip this for now
