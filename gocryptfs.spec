Name:    gocryptfs
Version: 1.4.2
Release: 1%{?dist}
Summary: Encrypted overlay filesystem written in Go
URL:     https://nuetzlich.net/gocryptfs/
License: MIT
Source0: https://github.com/rfjakob/gocryptfs/releases/download/v1.4.2/gocryptfs_v%{version}_src-deps.tar.gz
BuildRequires: golang
BuildRequires: openssl-devel
BuildRequires: pandoc

%description
gocryptfs uses file-based encryption that is implemented
as a mountable FUSE filesystem. Each file in gocryptfs
is stored one corresponding encrypted file on the hard disk.

%prep
mkdir -p go/src/github.com/rfjakob
rm -Rf   go/src/github.com/rfjakob/gocryptfs
tar xf gocryptfs_v%{version}_src-deps.tar.gz
mv gocryptfs_v%{version}_src-deps go/src/github.com/rfjakob/gocryptfs

%build
echo $PWD
export GOPATH=$PWD/go
cd go/src/github.com/rfjakob/gocryptfs
./build.bash
./Documentation/MANPAGE-render.bash > /dev/null

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 go/bin/gocryptfs %{buildroot}/%{_bindir}

%files
%{_bindir}/gocryptfs

%changelog
