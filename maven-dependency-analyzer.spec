%_javapackages_macros
Name:           maven-dependency-analyzer
Version:        1.4
Release:        2.0%{?dist}
Summary:        Maven dependency analyzer
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-dependency-analyzer/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(asm:asm)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-tools)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components)
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
