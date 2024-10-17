%{?_javapackages_macros:%_javapackages_macros}
Name:           maven-dependency-analyzer
Version:        1.5
Release:        1.4
Summary:        Maven dependency analyzer
Group:		Development/Java
License:        ASL 2.0
URL:            https://maven.apache.org/shared/maven-dependency-analyzer/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(asm:asm)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-tools)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

# This is a replacement package for maven-shared-dependency-analyzer
Provides:       maven-shared-dependency-analyzer = %{version}-%{release}
Obsoletes:      maven-shared-dependency-analyzer < %{version}-%{release}

%description
Analyzes the dependencies of a project for undeclared or unused artifacts.

Warning: Analysis is not done at source but bytecode level, then some cases are
not detected (constants, annotations with source-only retention, links in
javadoc) which can lead to wrong result if they are the only use of a
dependency.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
%{summary}

%prep
%setup -q

# Needed for tests only. However, the right groupId:artifactId of jmock in
# Fedora is org.jmock:jmock
%pom_remove_dep jmock:jmock

%build
# org.jmock.core package is needed, we don't have it
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-1
- Update to upstream version 1.4

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-7
- Build with xmvn

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.3-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-4
- Replace asm2 R with objectweb-asm
- Resolves: rhbz#902641

* Fri Dec 21 2012 Tomas Radej <tradej@redhat.com> - 1.3-3
- Added missing Provides/Obsoletes

* Thu Dec 20 2012 Tomas Radej <tradej@redhat.com> - 1.3-2
- Removed xmvn + reworked building without it

* Tue Dec 18 2012 Tomas Radej <tradej@redhat.com> - 1.3-1
- Initial package

