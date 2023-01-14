Summary:	Access a cacophony of neuro-imaging file formats
Name:		python-nibable
Version:	5.0.0
Release:	1
License:	MIT and BSD
Group:		Development/Python
Url:		http://nipy.sourceforge.net
#Source0:	https://github.com/nipy/nibabel/archive/refs/tags/%{version}/nibabel-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/n/nibabel/nibabel-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(h5py)
BuildRequires:  python3dist(hatchling)
BuildRequires:	python3dist(matplotlib)
BuildRequires:	python3dist(mock)
BuildRequires:	python3dist(nose)
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(pillow)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(pydicom)
BuildRequires:	python3dist(scipy)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(six)
BuildRequires:	python3dist(wheel)

Requires:	python-six
Requires:	python-numpy
Recommends:	python-scipy
Recommends:	python-pydicom

BuildArch:	noarch

%description
Read / write access to some common neuroimaging file formats

This package provides read +/- write access to some common medical and
neuroimaging file formats, including: ANALYZE (plain, SPM99, SPM2 and
later), GIFTI, NIfTI1, NIfTI2, CIFTI-2, MINC1, MINC2, AFNI BRIK/HEAD,
MGH and ECAT as well as Philips PAR/REC. It can read and write
FreeSurfer geometry, annotation and morphometry files. There is some
very limited support for DICOM. NiBabel is the successor of PyNIfTI.

The various image format classes give full or selective access to header
(meta) information and access to the image data is made available via
NumPy arrays.

%files
%license COPYING
%doc AUTHOR Changelog README.rst TODO
%{_bindir}/*
%{py_puresitedir}/nibabel/
%{py_puresitedir}/nibabel-*.*-info/
%{python3_sitelib}/nisext/

#---------------------------------------------------------------------------

%prep
%autosetup -n nibabel-%{version}

%build
%py_build

%install
%py_install
