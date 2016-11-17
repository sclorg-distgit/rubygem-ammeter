%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from ammeter-0.2.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ammeter

Summary: Write specs for your Rails 3+ generators
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.3
Release: 2%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/alexrothenberg/%{gem_name}
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:      %{?scl_prefix_ruby}ruby(release)
Requires:      %{?scl_prefix_ruby}ruby(rubygems)
Requires:      %{?scl_prefix}rubygem(railties) >= 3.0
Requires:      %{?scl_prefix}rubygem(activesupport) >= 3.0
Requires:      %{?scl_prefix}rubygem(rspec-rails) >= 2.2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix}rubygem(activerecord)
BuildRequires: %{?scl_prefix}rubygem(railties)
BuildRequires: %{?scl_prefix}rubygem(rspec-rails) >= 2.2
BuildRequires: %{?scl_prefix}rubygem(sqlite3)
# Dependency is missing
#  - avoids unnecessary dependency in SCL
#BuildRequires: %{?scl_prefix}rubygem(haml)
BuildArch:     noarch
Provides:      %{?scl_prefix}rubygem(%{gem_name}) = %{version}

# Explicitly require runtime subpackage, as long as older scl-utils do not generate it
Requires: %{?scl_prefix}runtime

%description
Write specs for your Rails 3+ generators.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Fix test suite for Ruby 2.3 compatibility.
# File#read is re-defined in spec/spec_helpr.rb#stub_file,
# and File#read is also used in 'require': specification.rb#load.
# If the first "require" for on library is called after the stub definition,
# it is failed.
%{?scl:scl enable %{scl} - << \EOF}
# 4 test are failing due to missing dependency
rspec spec | grep '37 examples, 4 failures'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%{gem_instdir}/LICENSE.txt
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/ammeter.gemspec
%{gem_instdir}/Gemfile
%{gem_instdir}/features
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Wed Apr 06 2016 Pavel Valena <pvalena@redhat.com> - 1.1.3-2
- Add scl macros

* Tue Mar 29 2016 Jun Aruga <jaruga@redhat.com> - 1.1.3-1
- Update to v1.1.3.
- Fix test suite for Ruby 2.3 compatibility.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 Vít Ondruch <vondruch@redhat.com> - 1.1.2-1
- Update to Ammeter 1.1.2.

* Tue Jun 10 2014 Vít Ondruch <vondruch@redhat.com> - 0.2.9-3
- Fix FTBFS in Rawhide (hrbz#1107063).

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 20 2013 Josef Stribny <jstribny@redhat.com> - 0.2.9-1
- Update to 0.2.9
- Rebuilt with Rails 4.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Vít Ondruch <vondruch@redhat.com> - 0.2.8-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2.8-1
- Updated to Ammeter 0.2.8.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2.2-2
- Moved features to doc subpackage (not needed for runtime).
- Moved gemspec and Gemfile to doc.
- Patched the dependencies to require rspec-core.

* Thu Feb 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2.2-1
- Initial package
