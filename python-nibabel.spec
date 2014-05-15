%define module	nibabel
# Need git version as the upstream one does not work with invesalius

Summary:	Access a cacophony of neuro-imaging file formats

Name:		python-%{module}
Version:	0.2.20100816
Release:	2
# git clone http://github.com/hanke/nibabel.git python-nibabel
# cd python-nibabel
# git archive --format tar 4f062e8a4f4bcceea4e8e1ff3fc7f897af06fa46 --prefix python-nibabel-0.2.20100816/ | bzip2 > python-nibabel.tar.bz2
Source0:	python-nibabel.tar.bz2
License:	BSD
Group:		Development/Python
Url:		http://nipy.sourceforge.net
Requires: 	python-dicom
Requires:	python-nifti
Requires: 	python-numpy
Requires: 	python-scipy
BuildArch:	noarch
BuildRequires:  python-devel

%description
NiBabel is a pure-Python package for reading and writing a variety of
medical and neuro-imaging file formats. This includes: ANALYZE (plain,
SPM99, SPM2), GIFTI, NIfTI1, MINC, as well as PAR/REC. NiBabel is the
successor of PyNIfTI.

%prep
%setup -q

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST

%clean

%files -f FILELIST


