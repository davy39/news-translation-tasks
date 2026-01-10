---
title: Comment commencer avec FPM
subtitle: ''
author: Jose Vicente Nunez
co_authors: []
series: null
date: '2024-01-19T16:42:55.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-fpm
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725458454908/8564e5d2-939a-4297-b619-801d0fe695cb.jpeg
tags:
- name: Linux
  slug: linux
seo_title: Comment commencer avec FPM
seo_desc: 'FPM is a powerful wrapper that allows you to create packages for multiple
  programs in multiple operating systems.

  In this tutorial I will show you how you can replace some of the tedious packaging
  of third party applications.

  What You Need to Complet...'
---

[FPM](https://fpm.readthedocs.io/en/latest/getting-started.html) est un wrapper puissant qui vous permet de créer des packages pour plusieurs programmes dans plusieurs systèmes d'exploitation.

Dans ce tutoriel, je vais vous montrer comment vous pouvez remplacer certains des emballages fastidieux des applications tierces.

## Ce dont vous avez besoin pour compléter ce tutoriel

* Une distribution Linux (j'ai utilisé Fedora mais cela fonctionne avec n'importe quelle distribution)

* Des privilèges élevés (si vous souhaitez installer vos propres packages)

## Quand votre gestionnaire de packages n'est pas assez simple

Souvent, vous voudrez avoir le contrôle ultime sur la façon dont vous emballez une application. Mais il y a quelques occasions où cela peut être excessif :

1. L'application tierce est suffisamment simple ou petite pour qu'un tar soit suffisant pour l'installer. Pourtant, vous voulez profiter des avantages des mises à jour et des retours en arrière, comme ceux offerts par RPM.

2. Vous devez ou voulez emballer une application d'un format (par exemple .tar.gz) vers Debian '.deb' ou RPM.

3. Vous devez emballer plusieurs applications qui ne sont offertes qu'au format source ou en binaires préemballés, comme lors de la mise à niveau du système d'exploitation. Et vous ne voulez pas passer une éternité à réemballer les applications tierces.

## Comment emballer une application existante à l'ancienne

J'ai écrit une petite application de démonstration qui extrait des faits système (comme l'utilisation du disque) au format JSON, appelée `[jdumpertools](https://github.com/josevnz/jdumpertools)`. L'application est très simple, est écrite en C, et dispose d'un [fichier spec RPM](https://github.com/josevnz/jdumpertools/blob/main/jdumpertools.spec) que vous pouvez utiliser pour emballer le logiciel.

Il y a quelques étapes manuelles nécessaires pour créer le RPM :

1. Télécharger la distribution source (ou binaire) : *git clone* [*https://github.com/josevnz/jdumpertools.git*](https://github.com/josevnz/jdumpertools.git)

2. Préparer le [fichier spec RPM](https://github.com/josevnz/jdumpertools/blob/main/jdumpertools.spec), qui devrait prendre en charge la compilation (ou simplement l'emballage) du logiciel, ainsi que l'emplacement pour l'installation

3. Vérifier le fichier spec, corriger les erreurs courantes

Alors, voyons comment fonctionne le fichier spec RPM de `jdumpertools`.

Tout d'abord, regardez le fichier spec :

```python
Name:           jdumpertools
# TODO: Trouver un meilleur moyen de mettre à jour la version ici et dans le Makefile
%global major 0
Version:        v%{major}.2
Release:        1%{?dist}
Summary:        Programmes qui peuvent être utilisés pour extraire les données d'utilisation de Linux au format JSON

License:        ASL 2.0
URL:            https://github.com/josevnz/jdumpertools
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  bash,tar,gzip,rpmdevtools,rpmlint,make,gcc >= 10.2.1
Requires:       bash

%global debug_package %{nil}

%description

Jdumpertools est une collection de programmes qui peuvent être utilisés pour extraire
les données d'utilisation de Linux au format JSON, afin qu'elles puissent être ingérées par d'autres outils.

* jdu: Similaire à la commande UNIX '/bin/du'.
* jutmp: Extracteur de la base de données UTMP

%prep
%setup -q -n jdumpertools

%build
make all

%install

/usr/bin/mkdir -p %{buildroot}/%{_bindir}
/usr/bin/mkdir -p %{buildroot}/%{_mandir}/man8
/usr/bin/cp -v -p jdu jutmp %{buildroot}/%{_bindir}
/usr/bin/cp -v -p jdu.1 jutmp.1 %{buildroot}/%{_mandir}/man8/
/usr/bin/gzip %{buildroot}/%{_mandir}/man8/*
/usr/bin/mkdir -p %{buildroot}/%{_libdir}
/usr/bin/cp -v -p libjdumpertools.so.%{major} %{buildroot}/%{_libdir}
/usr/bin/strip %{buildroot}/%{_bindir}/{jdu,jutmp}
/usr/bin/strip %{buildroot}/%{_libdir}/*

%clean
rm -rf %{buildroot}

%files
%{_bindir}/jdu
%{_bindir}/jutmp
%{_libdir}/libjdumpertools.so.%{major}
%{_libdir}/libjdumpertools.so
%license LICENSE
%doc README.md
%doc %{_mandir}/man8/jdu.1.gz
%doc %{_mandir}/man8/jutmp.1.gz


%changelog
* Sun Oct  3 2021 Jose Vicente Nunez <kodegeek.com@protonmail.com> - v0.2-1
- Corrections appliquées depuis rpmlint : page de manuel, fautes de frappe dans le fichier spec, binaires dépouillés, etc.
* Mon Jan  4 2021 Jose Vicente Nunez <kodegeek.com@protonmail.com> - v0.1-1
- Première version emballée
```

Et maintenant, construisons-le :

```shell
[josevnz@dmaf5 jdumpertools]$ sudo dnf install -y rpmdevtools rpmlint
...
[josevnz@dmaf5 test]$ git clone https://github.com/josevnz/jdumpertools.git
Cloning into 'jdumpertools'...
remote: Enumerating objects: 228, done.
remote: Counting objects: 100% (228/228), done.
remote: Compressing objects: 100% (137/137), done.
remote: Total 228 (delta 132), reused 157 (delta 79), pack-reused 0
Receiving objects: 100% (228/228), 3.15 MiB | 9.67 MiB/s, done.
Resolving deltas: 100% (132/132), done.

[josevnz@dmaf5 test]$ cd jdumpertools/
[josevnz@dmaf5 jdumpertools]$ rpmbuild -ba jdumpertools.spec
...
+ exit 0
Provides: jdumpertools = v0.2-1.fc37 jdumpertools(x86-64) = v0.2-1.fc37 libjdumpertools.so()(64bit)
Requires(rpmlib): rpmlib(CompressedFileNames) <= 3.0.4-1 rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires: libc.so.6()(64bit) libc.so.6(GLIBC_2.2.5)(64bit) libc.so.6(GLIBC_2.3)(64bit) libjdumpertools.so()(64bit) rtld(GNU_HASH)
Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/josevnz/rpmbuild/BUILDROOT/jdumpertools-v0.2-1.fc37.x86_64
Wrote: /home/josevnz/rpmbuild/SRPMS/jdumpertools-v0.2-1.fc37.src.rpm
Wrote: /home/josevnz/rpmbuild/RPMS/x86_64/jdumpertools-v0.2-1.fc37.x86_64.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.42keBq
+ umask 022
+ cd /home/josevnz/rpmbuild/BUILD
+ cd jdumpertools
+ rm -rf /home/josevnz/rpmbuild/BUILDROOT/jdumpertools-v0.2-1.fc37.x86_64
+ RPM_EC=0
++ jobs -p
+ exit 0
Executing(rmbuild): /bin/sh -e /var/tmp/rpm-tmp.aZjb6s
+ umask 022
+ cd /home/josevnz/rpmbuild/BUILD
+ rm -rf jdumpertools jdumpertools.gemspec
+ RPM_EC=0
++ jobs -p
+ exit 0
...
[josevnz@dmaf5 jdumpertools]$ ls -l $HOME/rpmbuild/RPMS/x86_64/jdumpertools-v0.2-1.fc37.x86_64.rpm
-rw-r--r--. 1 josevnz josevnz 22118 Jun  2 14:03 /home/josevnz/rpmbuild/RPMS/x86_64/jdumpertools-v0.2-1.fc37.x86_64.rpm
```

Ensuite, vous installez le RPM comme n'importe quel autre RPM :

```shell
[josevnz@dmaf5 jdumpertools]$ sudo dnf install -y $HOME/rpmbuild/RPMS/x86_64/jdumpertools-v0.2-1.fc37.x86_64.rpm
Last metadata expiration check: 1:36:46 ago on Fri 02 Jun 2023 12:30:31 PM EDT.
Dependencies resolved.
=================================================================================================================================
 Package                         Architecture              Version                         Repository                       Size
=================================================================================================================================
Installing:
 jdumpertools                    x86_64                    v0.2-1.fc37                     @commandline                     22 k

Transaction Summary
=================================================================================================================================
Install  1 Package

Total size: 22 k
Installed size: 57 k
Downloading Packages:
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                         1/1 
  Installing       : jdumpertools-v0.2-1.fc37.x86_64                                                                         1/1 
  Running scriptlet: jdumpertools-v0.2-1.fc37.x86_64                                                                         1/1 
  Verifying        : jdumpertools-v0.2-1.fc37.x86_64                                                                         1/1 

Installed:
  jdumpertools-v0.2-1.fc37.x86_64                                                                                                

Complete!
```

Ce n'est pas terrible, surtout si vous prévoyez de faire des mises à jour, mais pouvons-nous faire cela d'une manière plus facile ?

## Comment installer FPM

Le document [getting started](https://fpm.readthedocs.io/en/latest/getting-started.html) est la référence la plus simple à laquelle vous pouvez vous référer pour faire fonctionner FPM.

Tout d'abord, vous installerez quelques dépendances, par exemple sur Fedora :

```shell
[josevnz@dmaf5 jdumpertools]$ sudo dnf install -y gem
[josevnz@dmaf5 jdumpertools]$ sudo dnf install -y rpm-build squashfs-tools
```

Et ensuite, vous installerez FPM lui-même :

```shell
[josevnz@dmaf5 jdumpertools]$ gem install --user-install fpm
Fetching insist-1.0.0.gem
Fetching clamp-1.0.1.gem
Fetching stud-0.0.23.gem
Fetching rexml-3.2.5.gem
Fetching mustache-0.99.8.gem
Fetching dotenv-2.8.1.gem
Fetching cabin-0.9.0.gem
Fetching pleaserun-0.0.32.gem
Fetching fpm-1.15.1.gem
Fetching backports-3.24.1.gem
...
Done installing documentation for stud, rexml, mustache, insist, dotenv, clamp, cabin, pleaserun, backports, arr-pm, fpm after 5 seconds
11 gems installed
```

## Comment emballer `jdumpertools` en tant que RPM, sans fichier Spec

Eh bien, nous avons besoin de quelques fichiers à emballer. Cette [distribution](https://github.com/josevnz/jdumpertools) est livrée avec un *Makefile*, donc c'est facile comme bonjour, nous faisons :

```shell
[josevnz@dmaf5 jdumpertools]$ make
gcc -Wall -g -Og -Wextra -Werror -Werror=format-security -std=c11   -DJDUMPERTOOLS_VERSION=v0.2 -fPIC jdumpertools.h jdumpertools.c -I /home/josevnz/test/jdumpertools -shared -Wl,-soname,libjdumpertools.so -o libjdumpertools.so.0
gcc jdumpertools.h jdu.c libjdumpertools.so.0 -Wall -g -Og -Wextra -Werror -Werror=format-security -std=c11   -DJDUMPERTOOLS_VERSION=v0.2 -L /home/josevnz/test/jdumpertools -l jdumpertools -o jdu
gcc jdumpertools.h jutmp.c -Wall -g -Og -Wextra -Werror -Werror=format-security -std=c11   -DJDUMPERTOOLS_VERSION=v0.2 -L /home/josevnz/test/jdumpertools -l jdumpertools -o jutmp
...
[josevnz@dmaf5 jdumpertools]$ ls
CODE_OF_CONDUCT.md  INSTALL.md  jdu.c           jdumpertools.spec  jutmp.c               Makefile        SECURITY.md
CONTRIBUTING.md     jdu         jdumpertools.c  jutmp              libjdumpertools.so.0  mazinger-z.png
Dockerfile          jdu.1       jdumpertools.h  jutmp.1            LICENSE               README.md
[josevnz@dmaf5 jdumpertools]$ fpm -t rpm -s dir --name jdumpertools --rpm-autoreq --rpm-os linux --rpm-summary 'Programmes qui peuvent être utilisés pour extraire les données d\'utilisation de Linux au format JSON' --license 'ASL 2.0' --version v0.21 --depends bash --maintainer 'Jose Vicente Nunez <kodegeek.com@protonmail.com>' --url https://github.com/josevnz/jdumpertools jdu=/usr/bin/jdu jutmp=/usr/bin/jutmp jdu.1=/usr/share/man/man1/jdu.1.gz jutmp.1=/usr/share/man/man8/jutmp.1.gz
Created package {:path=>"jdumpertools-v0.21-1.x86_64.rpm"}
```

Donc, pas de fichier spec, et nous avons un RPM.

Et si je veux créer des packages pour d'autres distributions ? Je dois simplement faire quelques changements sur la ligne de commande :

Package Debian :

```shell
[josevnz@dmaf5 jdumpertools]$ fpm -t deb -s dir --name jdumpertools --rpm-autoreq --rpm-os linux --rpm-summary 'Programmes qui peuvent être utilisés pour extraire les données d\'utilisation de Linux au format JSON' --license 'ASL 2.0' --version v0.21 --depends bash --maintainer 'Jose Vicente Nunez <kodegeek.com@protonmail.com>' --url https://github.com/josevnz/jdumpertools jdu=/usr/bin/jdu jutmp=/usr/bin/jutmp jdu.1=/usr/share/man/man1/jdu.1.gz jutmp.1=/usr/share/man/man8/jutmp.1.gz
Debian 'Version' field needs to start with a digit. I was provided 'v0.21' which seems like it just has a 'v' prefix to an otherwise-valid Debian version, I'll remove the 'v' for you. {:level=>:warn}
Created package {:path=>"jdumpertools_0.21_amd64.deb"}
```

Script auto-extractible :

```shell
[josevnz@dmaf5 jdumpertools]$ fpm -t sh -s dir --name jdumpertools --rpm-autoreq --rpm-os linux --rpm-summary 'Programmes qui peuvent être utilisés pour extraire les données d\'utilisation de Linux au format JSON' --license 'ASL 2.0' --version v0.21 --depends bash --maintainer 'Jose Vicente Nunez <kodegeek.com@protonmail.com>' --url https://github.com/josevnz/jdumpertools jdu=/usr/bin/jdu jutmp=/usr/bin/jutmp jdu.1=/usr/share/man/man1/jdu.1.gz jutmp.1=/usr/share/man/man8/jutmp.1.gz
Created package {:path=>"jdumpertools.sh"}
```

Fichier tar :

```shell
[josevnz@dmaf5 jdumpertools]$ fpm -t tar -s dir --name jdumpertools --rpm-autoreq --rpm-os linux --rpm-summary 'Programmes qui peuvent être utilisés pour extraire les données d\'utilisation de Linux au format JSON' --license 'ASL 2.0' --version v0.21 --depends bash --maintainer 'Jose Vicente Nunez <kodegeek.com@protonmail.com>' --url https://github.com/josevnz/jdumpertools jdu=/usr/bin/jdu jutmp=/usr/bin/jutmp jdu.1=/usr/share/man/man1/jdu.1.gz jutmp.1=/usr/share/man/man8/jutmp.1.gz
Created package {:path=>"jdumpertools.tar"}
```

Cela est déjà très pratique. Maintenant, je veux vous montrer un autre cas d'utilisation pour FPM.

## Comment réemballer un logiciel existant

Disons que vous voulez distribuer un module CPAN qui n'a pas de RPM. Vous pourriez passer du temps de qualité, ou vous pourriez utiliser FPM pour faire le travail à votre place.

Tout d'abord, installons une nouvelle dépendance pour Fedora :

```shell
[josevnz@dmaf5 jdumpertools]$ sudo dnf install -y perl-App-cpanminus
```

Et ensuite, construisons notre RPM

```shell
[josevnz@dmaf5 jdumpertools]$ fpm -t rpm -s cpan Archive::Tar
Created package {:path=>"perl-Archive-Tar-3.02-1.noarch.rpm"}
```

Est-ce que cela a fonctionné ?

```shell
[josevnz@dmaf5 jdumpertools]$ rpm -qil perl-Archive-Tar-3.02-1.noarch.rpm
Name        : perl-Archive-Tar
Version     : 3.02
Release     : 1
Architecture: noarch
Install Date: (not installed)
Group       : default
Size        : 177677
License     : perl_5
Signature   : (none)
Source RPM  : perl-Archive-Tar-3.02-1.src.rpm
Build Date  : Fri 02 Jun 2023 04:36:45 PM EDT
Build Host  : dmaf5
Relocations : / 
Packager    : <josevnz@dmaf5>
Vendor      : Jos Boumans <kane[at]cpan.org>
URL         : http://example.com/no-uri-given
Summary     : Manipulates TAR archives
Description :
Manipulates TAR archives
/usr/local/bin/ptar
/usr/local/bin/ptardiff
/usr/local/bin/ptargrep
/usr/local/share/man/man1/ptar.1
/usr/local/share/man/man1/ptardiff.1
/usr/local/share/man/man1/ptargrep.1
/usr/local/share/man/man3/Archive::Tar.3pm
/usr/local/share/man/man3/Archive::Tar::File.3pm
/usr/local/share/perl5/5.36/Archive/Tar.pm
/usr/local/share/perl5/5.36/Archive/Tar/Constant.pm
/usr/local/share/perl5/5.36/Archive/Tar/File.pm
```

Maintenant, je vais vous montrer comment emballer le module [clickhouse-driver](https://clickhouse-driver.readthedocs.io/en/latest/installation.html#installation-from-pypi) de PyPi.

```shell
[josevnz@dmaf5 jdumpertools]$ fpm -t rpm -s python 'clickhouse-driver'
Created package {:path=>"python-clickhouse-driver-0.2.6-1.x86_64.rpm"}
```

Disons que maintenant vous voulez créer un RPM pour OpenJDK 17. Pas de problème, obtenez le fichier tar et emballez-le avec un peu d'aide :

```shell
[josevnz@dmaf5 jdumpertools]$ curl --fail --location --remote-name https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.7%2B7/OpenJDK17U-jdk_x64_linux_hotspot_17.0.7_7.tar.gz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  182M  100  182M    0     0  10.9M      0  0:00:16  0:00:16 --:--:-- 11.1M
[josevnz@dmaf5 jdumpertools]$ fpm -t rpm -s tar --url 'https://adoptium.net/' --description 'Eclipse Temurin est le nom de la distribution OpenJDK d\'Adoptium' --version '17.0.7+7' --prefix /usr/local/openjdk OpenJDK17U-jdk_x64_linux_hotspot_17.0.7_7.tar.gz
[josevnz@dmaf5 jdumpertools]$ rpm -qil OpenJDK17U-jdk_x64_linux_hotspot_17-17.0.7+7-1.x86_64.rpm
Name        : OpenJDK17U-jdk_x64_linux_hotspot_17
Version     : 17.0.7+7
Release     : 1
Architecture: x86_64
Install Date: (not installed)
Group       : default
Size        : 329508762
License     : unknown
Signature   : (none)
Source RPM  : OpenJDK17U-jdk_x64_linux_hotspot_17-17.0.7+7-1.src.rpm
Build Date  : Fri 02 Jun 2023 05:05:05 PM EDT
Build Host  : dmaf5
Relocations : /usr/local/openjdk 
Packager    : <josevnz@dmaf5>
Vendor      : none
URL         : https://adoptium.net/
Summary     : Eclipse Temurin est le nom de la distribution OpenJDK d\'Adoptium
Description :
Eclipse Temurin est le nom de la distribution OpenJDK d\'Adoptium
/usr/local/openjdk/jdk-17.0.7+7/NOTICE
/usr/local/openjdk/jdk-17.0.7+7/bin/jar
/usr/local/openjdk/jdk-17.0.7+7/bin/jarsigner
/usr/local/openjdk/jdk-17.0.7+7/bin/java
...
```

Je pourrais continuer, mais je pense que vous avez compris à quel point vous pouvez faire avec FPM.

## Qu'est-ce qui suit ?

Nous avons couvert certains cas d'utilisation importants, mais l'outil a beaucoup plus à offrir :

* FPM a [de nombreuses autres utilisations](https://fpm.readthedocs.io/en/latest/cli-reference.html), y compris la transformation de packages existants d'autres formats vers celui que vous souhaitez.

* FPM prend également en charge [les fichiers de configuration](https://fpm.readthedocs.io/en/latest/getting-started.html). Si vous l'utilisez souvent, vous devriez lire comment utiliser un fichier de configuration pour FPM plutôt que d'utiliser une longue ligne de commande.

* Vous pouvez également envisager d'exécuter FPM [à partir d'un conteneur](https://fpm.readthedocs.io/en/latest/docker.html), pour éviter d'installer des dépendances.

* Si vous êtes curieux de savoir comment exécuter les binaires jumpertools, vous pouvez consulter le [README.md](https://github.com/josevnz/jdumpertools) du dépôt.