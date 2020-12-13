%global __cmake_in_source_build

Name:           onednn
Version:        1.6
Release:        1%{?dist}
Summary:        Deep Neural Network Library

License:        ASL 2.0 and BSD and Boost and MIT
URL:            https://github.com/oneapi-src/oneDNN/
Source0:        %{url}/archive/v%{version}/onednn-%{version}.tar.gz

# This package only work in few arches for now
ExclusiveArch:  x86_64 aarch64 ppc64le

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++

# Optionals not yet enabled
#BuildRequires:  pkgconfig(OpenCL)
#BuildRequires:  pkgconfig(tbb)

# Virtual provides mkldnn
Provides: mkldnn = %{version}-%{release}
Provides: mkl-dnn = %{version}-%{release}
Obsoletes: mkl-dnn < 1.3
# Provides oneDNN
Provides: oneDNN = %{version}-%{release}


%description
one-API Deep Neural Network Library (oneDNN) is an open-source performance
library for deep learning applications. The library includes basic
building blocks for neural networks optimized for Intel Architecture
Processors and Intel Processor Graphics.

oneDNN is intended for deep learning applications and framework developers
interested in improving application performance on Intel CPUs and
GPUs. Deep learning practitioners should use one of the applications
enabled with oneDNN:


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n oneDNN-%{version}


%build
mkdir -p build && cd build
%cmake ..

%make_build


%install
cd build
%make_install


# Remove docs
rm -rf %{buildroot}%{_docdir}/dnnl


%ldconfig_scriptlets


%files
%license LICENSE THIRD-PARTY-PROGRAMS
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md
%{_libdir}/libdnnl.so.1
%{_libdir}/libdnnl.so.1.*
%{_libdir}/libmkldnn.so.1
%{_libdir}/libmkldnn.so.1.*


%files devel
%{_includedir}/mkldnn*.h*
%{_includedir}/dnnl*.h*
%{_libdir}/libdnnl.so
%{_libdir}/libmkldnn.so
%dir %{_libdir}/cmake/dnnl
%{_libdir}/cmake/dnnl/*.cmake
%dir %{_libdir}/cmake/mkldnn
%{_libdir}/cmake/mkldnn/*.cmake


%changelog

* Sun Dec 13 2020 sinever <sinever@126.com> - 1.6
- Initial spec file.
