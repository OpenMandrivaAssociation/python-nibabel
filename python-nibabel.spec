%define module	nibabel
%define name	python-%{module}
# Need git version as the upstream one does not work with invesalius
%define version	0.2.20100816
%define release	%mkrel 1

Summary:	Access a cacophony of neuro-imaging file formats
Name:		%{name}
Version:	%{version}
Release:	%{release}
# git clone http://github.com/hanke/nibabel.git python-nibabel
# cd python-nibabel
# git archive --format tar 4f062e8a4f4bcceea4e8e1ff3fc7f897af06fa46 --prefix python-nibabel-0.2.20100816/ | bzip2 > python-nibabel.tar.bz2
Source0:	python-nibabel.tar.bz2
License:	BSD
Group:		Development/Python
Url:		http://nipy.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	python-dicom
Requires:	python-nifti
Requires: 	python-numpy
Requires: 	python-scipy
BuildArch:	noarch
%py_requires -d

%description
NiBabel is a pure-Python package for reading and writing a variety of
medical and neuro-imaging file formats. This includes: ANALYZE (plain,
SPM99, SPM2), GIFTI, NIfTI1, MINC, as well as PAR/REC. NiBabel is the
successor of PyNIfTI.

%prep
%setup -q

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
