---
title: Comment simplifier l'emballage RPM des bibliothèques Python avec Mock et Podman
subtitle: ''
author: Jose Vicente Nunez
co_authors: []
series: null
date: '2025-01-15T19:29:16.918Z'
originalURL: https://freecodecamp.org/news/simplify-python-library-rpm-packaging-with-mock-and-podman
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1736952806487/e25f259a-71e0-4998-ad29-b5da286e3fba.png
tags:
- name: Python 3
  slug: python3
- name: rpm
  slug: rpm
- name: mock
  slug: mock
- name: packaging
  slug: packaging
- name: Devops
  slug: devops
seo_title: Comment simplifier l'emballage RPM des bibliothèques Python avec Mock et
  Podman
seo_desc: 'Packaging libraries and applications written in Python comes with its challenges.
  And while virtual environments are great for controlling and standardizing installations,
  there are some scenarios where using them may not be the best.

  For example, sa...'
---

L'emballage des bibliothèques et des applications écrites en Python comporte ses défis. Et [bien que les environnements virtuels soient excellents](https://docs.python.org/3/tutorial/venv.html) pour contrôler et standardiser les installations, il existe certains scénarios où leur utilisation peut ne pas être la meilleure.

Par exemple, disons que vous devez installer une bibliothèque Python à l'échelle du système. Vous pourriez essayer de créer un environnement virtuel dans un répertoire partagé bien connu, ou vous pourriez modifier la variable d'environnement [PYTHONPATH](https://docs.python.org/3/using/cmdline.html) pour changer l'endroit où chercher les packages.

Mais cela peut être plus simple avec un gestionnaire de packages comme [RedHat RPM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/packaging_and_distributing_software/introduction-to-rpm_packaging-and-distributing-software) ou [Debian DPKG](https://www.dpkg.org/), qui peut également vous aider à suivre les dépendances et peut même vérifier si le contenu d'un package a été falsifié après l'installation avec une somme de contrôle.

De plus, les outils d'administration système écrits en Python nécessitent souvent que vous utilisiez un interpréteur avec toutes les bibliothèques requises prêtes à l'emploi. Par exemple, imaginez un Python système avec le module populaire [numpy](https://numpy.org/) installé par défaut, et un tel package est utilisé par l'outil – il suffit d'appeler l'import sans initialiser d'environnements virtuels.

Pour l'argument, disons que vous devez opter pour un emballage RPM. Vous réaliserez rapidement que votre package RPM a des dépendances d'exécution (bibliothèques dont votre bibliothèque Python a besoin pour fonctionner une fois installée) et des dépendances de construction (bibliothèques dont vous avez besoin pour construire votre bibliothèque mais qui ne sont pas requises pour utiliser la bibliothèque).

En particulier, *les dépendances de construction vous forceront à les installer sur les machines où vous emballez votre application*. Par exemple, regardez la balise "BuildRequires" du spec RPM de poetry de RedHat (montrant un fragment ici) :

```plaintext
 This patch moves the vendored requires definition
# from vendors/pyproject.toml to pyproject.toml
# Intentionally contains the removed hunk to prevent patch aging
Patch1:         poetry-core-1.6.1-devendor.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%if %{with tests}
# for tests (only specified via poetry poetry.dev-dependencies with pre-commit etc.)
BuildRequires:  python3-build
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-tomli-w
BuildRequires:  python3-virtualenv
BuildRequires:  gcc 
BuildRequires:  git-core
%endif
```

Pour compliquer les choses, vous pourriez :

* Avoir besoin de construire votre bibliothèque pour un système d'exploitation totalement différent de celui que vous avez installé (disons que vous avez Fedora 42 mais que vous avez besoin d'un RPM pour Alma Linux 9.5)

* Avoir besoin d'installer un RPM provenant d'une source douteuse, et vous voulez vous assurer qu'il ne casse pas votre système pendant que le processus d'emballage est en cours d'exécution (voir les [scriptlets RPM](https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/)).

### Prérequis

Dans ce tutoriel, je vais vous montrer comment vous pouvez gérer ces préoccupations en utilisant un outil Open Source appelé [Mock](https://github.com/rpm-software-management/mock). Mais d'abord, vous aurez besoin des éléments suivants pour pouvoir suivre ce tutoriel :

* Une distribution Linux qui utilise RPM comme outil d'emballage (RedHat Enterprise Edition, Fedora, Alma Linux, Rocky, et ainsi de suite)

* Capacité à installer des packages RPM sur votre serveur de construction (comme [mock](https://fedoraproject.org/wiki/Using_Mock_to_test_package_builds), [rpmdevtools](https://fedoraproject.org/wiki/Rpmdevtools)) en utilisant des outils comme [DNF](https://rpm-software-management.github.io/) ou YUM.

* Compréhension du fonctionnement de l'emballage RPM (si vous n'êtes pas familier, le [guide RPM de Fedora](https://fedoranews.org/alex/tutorial/rpm/) est un excellent point de départ)

* Vous devriez comprendre ce qu'est un [conteneur](https://developers.redhat.com/blog/2018/02/22/container-terminology-practical-introduction#h.j2uq93kgxe0e) et comment [PODMAN](https://docs.podman.io/en/latest/index.html) ou [Docker](https://docker.com/) fonctionne.

* Compréhension du fonctionnement d'un [environnement virtuel Python](https://docs.python.org/3/library/venv.html). Nous n'aborderons pas cela ici, mais il est utile de savoir que [cette alternative existe et comment elle fonctionne](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments).

### Voici ce que nous allons couvrir :

* [Pourquoi Mock](#heading-pourquoi-mock) ?

* [Scénarios d'emballage avec Mock et Podman](#heading-scenarios-demballage-avec-mock-et-podman)

* [Conclusion](#heading-conclusion)

## Pourquoi Mock ?

Comme nous l'avons discuté ci-dessus, nous avons déjà des [environnements virtuels Python](https://docs.python.org/3/library/venv.html) – alors pourquoi se donner la peine d'avoir un RPM de la même bibliothèque ?

Eh bien, si vous voulez garantir un déploiement cohérent sur différents systèmes, l'emballage RPM peut être bénéfique. Il permet une gestion et une distribution plus faciles des logiciels, en particulier dans les environnements où les installations à l'échelle du système sont préférées aux environnements virtuels.

Mock peut nous aider avec cela. D'après le README Git de Mock :

> *Un gestionnaire d'environnement de construction 'simple'* [*chroot*](https://en.wikipedia.org/wiki/Chroot) *pour la construction de RPMs.*
>
> *Mock est utilisé par le système de construction de Fedora pour peupler un environnement chroot, qui est ensuite utilisé pour construire un source-RPM (SRPM). Il peut être utilisé pour la gestion à long terme d'un environnement chroot, mais généralement un chroot est peuplé (en utilisant* [*DNF*](https://rpm-software-management.github.io/)*), un SRPM est construit dans le chroot pour générer des RPMs binaires, et le chroot est ensuite supprimé.*

**Ceci est très important :** cela signifie que mock installera les dépendances dans un environnement [chroot](https://en.wikipedia.org/wiki/Chroot), séparé du système régulier, qui sera supprimé une fois l'emballage terminé.

Mock en lui-même ne fournit pas une isolation parfaite mais [lorsqu'il est utilisé avec un framework d'exécution de conteneur](https://developers.redhat.com/blog/2018/02/22/container-terminology-practical-introduction#h.j2uq93kgxe0e) comme [PODMAN](https://docs.podman.io/en/latest/index.html), il aide à protéger l'intégrité de votre système lors de l'emballage d'un RPM inconnu :

> Mock doit exécuter certaines tâches sous les privilèges root, donc les RPMs malveillants peuvent mettre votre système en danger. Mock n'est pas sûr pour les RPMs inconnus

En exécutant mock à l'intérieur de Podman, vous obtenez le meilleur des deux mondes, car Podman s'exécutera avec des privilèges limités. De plus, Podman, étant un conteneur, peut se supprimer après l'exécution, ce qui aide au nettoyage.

Regardons quelques scénarios qui démontrent où vous pouvez utiliser mock.

## Scénarios d'emballage avec Mock et Podman

### Emballage d'une version plus récente du module sur une ancienne distribution Linux

Dans ce cas, disons que nous voulons réutiliser le package existant [textual 0.6.2](https://textual.textualize.io/) de Fedora 41 dans Fedora 40. Cela est possible avec mock, mais pour le rendre plus sécurisé, nous devons l'exécuter à l'intérieur d'un conteneur Podman. Cela nous donnera plus d'isolation par rapport au système d'exploitation réel.

Lors des tests, j'ai trouvé que mon répertoire personnel était trop petit lors de l'exécution de Podman. Pour corriger cela, j'ai créé une substitution de configuration pour pointer le stockage racine de Podman vers une partition plus grande sur ma machine (/mnt/data/podman/) :

```shell
mkdir --parent ---verbose $HOME/.config/containers/
/bin/cat<<EOF>$HOME/.config/containers/storage.conf
[storage]
driver = "overlay"
runroot = "/mnt/data/podman/"
graphroot = "/mnt/data/podman/"
EOF
```

Ensuite, j'ai réalisé autre chose : j'avais besoin de préserver les résultats de notre génération d'artefacts. Lorsque vous exécutez un conteneur avec le drapeau `--rm` (remove), tout son contenu est détruit. Dans notre cas, nous voulons préserver les fichiers de packages RPM générés. Ce que nous faisons, c'est monter un répertoire externe à l'intérieur du conteneur Podman en utilisant l'option `--mount` : (`--mount type=bind,src=$HOME/tmp,target=/mnt/result`).

Jusqu'à présent, tout va bien, n'est-ce pas ? Pas tout à fait. J'ai découvert qu'une dépendance Python pour Textual manquait également. Elle s'appelle Rich, et elle avait besoin d'un RPM également. Heureusement, vous pouvez "chaîner" une liste de dépendances en tant que Source RPMS (SRPM) lors de la construction de votre package principal, afin que Mock puisse les rendre disponibles pour vous lors de la préparation du package principal (nous devons passer `--localrepo` au lieu de `--resultdir` et nous utilisons le drapeau `--chain`).

Maintenant, nous sommes prêts à construire le package et ses dépendances. Cela nécessite ce qui suit :

1. Créer un répertoire local où les RPMS seront créés

2. Exécuter Podman en mode interactif afin que nous puissions exécuter des commandes à l'intérieur

3. Installer mock à l'intérieur de Podman en utilisant dnf.

4. Créer un utilisateur spécial appelé mockbuilder pour exécuter mock et devenir cet utilisateur

5. Exécuter mock en passant la chaîne

```shell
mkdir --parent --verbose $HOME/tmp
podman run --mount type=bind,src=$HOME/tmp,target=/mnt/result --rm --privileged --interactive --tty fedora:40 bash
dnf install -y mock
useradd mockbuilder
usermod -a -G mock mockbuilder
chown mockbuilder /mnt/result/
su - mockbuilder
mock --localrepo /mnt/result/ --chain https://download.fedoraproject.org/pub/fedora/linux/releases/41/Everything/source/tree/Packages/p/python-rich-13.7.1-5.fc41.src.rpm https://download.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/source/tree/Packages/p/python-textual-0.62.0-2.fc41.src.rpm
```

Par exemple, sur mon Raspberry PI 4 avec Fedora 40, la sortie finale ressemble à ceci :

```shell
...
INFO: Success building python-textual-0.62.0-2.fc41.src.rpm
INFO: Results out to: /mnt/result/results/default
INFO: Packages built: 2
INFO: Packages successfully built in this order:
INFO: /tmp/tmpc6651dxo/python-rich-13.7.1-5.fc41.src.rpm
INFO: /tmp/tmpc6651dxo/python-textual-0.62.0-2.fc41.src.rpm
```

En dehors du conteneur, nous pouvons tester l'installation en installant à la fois Rich et Textual (vous avez besoin de root pour cela) :

```shell
josevnz@raspberypi1:~$ sudo dnf install -y /home/josevnz/tmp/results/default/python-rich-13.7.1-5.fc41/python3-rich-13.7.1-5.fc40.noarch.rpm /home/josevnz/tmp/results/default/python-textual-0.62.0-2.fc41/python3-textual-doc-0.62.0-2.fc40.noarch.rpm /home/josevnz/tmp/results/default/python-textual-0.62.0-2.fc41/python3-textual-0.62.0-2.fc40.noarch.rpm
...
nstalled:
  python3-linkify-it-py-2.0.3-1.fc40.noarch            python3-markdown-it-py-3.0.0-4.fc40.noarch    python3-markdown-it-py+linkify-3.0.0-4.fc40.noarch  
  python3-markdown-it-py+plugins-3.0.0-4.fc40.noarch   python3-mdit-py-plugins-0.4.0-4.fc40.noarch   python3-mdurl-0.1.2-6.fc40.noarch                   
  python3-pygments-2.17.2-3.fc40.noarch                python3-rich-13.7.1-5.fc40.noarch             python3-textual-0.62.0-2.fc40.noarch                
  python3-textual-doc-0.62.0-2.fc40.noarch             python3-uc-micro-py-1.0.3-1.fc40.noarch      

Complete!
```

Notez que le contenu du conteneur a été supprimé de la fenêtre d'origine une fois que vous quittez, à l'exception du volume monté. C'est génial, car nous n'avons pas à nous soucier de désinstaller les packages de construction nous-mêmes.

*Mais est-ce parfait ?*

*Pouvez-vous utiliser Mock pour emballer un code plus récent sur des distributions beaucoup plus anciennes ?*

Mock fonctionne vraiment bien tant que vos dépendances ne sont pas trop éloignées de la version que vous exécutez. Par exemple, disons que vous voulez construire les RPMS pour Fedora 37 au lieu de Fedora 40 :

```shell
sudo rm -rf $HOME/tmp/results/*
podman run --mount type=bind,src=$HOME/tmp,target=/mnt/result --rm --privileged --interactive --tty fedora:37 bash
dnf install -y mock
useradd mockbuilder && usermod -a -G mock mockbuilder && chown mockbuilder /mnt/result/ && su - mockbuilder
mock --nocheck --localrepo /mnt/result/ --chain https://download.fedoraproject.org/pub/fedora/linux/releases/41/Everything/source/tree/Packages/p/python-rich-13.7.1-5.fc41.src.rpm https://download.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/source/tree/Packages/p/python-textual-0.62.0-2.fc41.src.rpm
...
Package python3-poetry-core-1.0.8-3.fc37.noarch is already installed.
Package python3-pytest-7.1.3-2.fc37.noarch is already installed.
Package python3-setuptools-62.6.0-3.fc37.noarch is already installed.
Error: 
 Problem: nothing provides requested (python3dist(pygments) < 3~~ with python3dist(pygments) >= 2.13)
```

Oh oh, Fedora 37 ne fournit pas certaines des dépendances. Pouvez-vous les construire en chaîne ? J'ai essayé d'ajouter le SRPM pour [pygments](https://pygments.org/) (une bibliothèque de surlignage syntaxique générique pour Python), avant de construire [rich](https://rich.readthedocs.io/en/stable/introduction.html), car c'est une dépendance pour celui-ci. Ainsi, la chaîne de dépendances a un peu grandi :

```shell
mock --nocheck --localrepo /mnt/result/ --chain https://download.fedoraproject.org/pub/fedora/linux/releases/39/Everything/source/tree/Packages/p/python-pygments-2.15.1-4.fc39.src.rpm https://download.fedoraproject.org/pub/fedora/linux/releases/41/Everything/source/tree/Packages/p/python-rich-13.7.1-5.fc41.src.rpm https://download.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/source/tree/Packages/p/python-textual-0.62.0-2.fc41.src.rpm
```

Et puis j'ai trouvé que deux autres dépendances Python étaient cassées, cette fois pour textual sur Fedora 37 :

```shell
...
no matching package to install: 'python3-syrupy'
No matching package to install: 'python3-time-machine'
Not all dependencies satisfied
```

Cela ressemble à un jeu d'essais et d'erreurs. *À quel point cela peut-il être mauvais ?*

Plusieurs essais plus tard, j'ai trouvé que [Syrupy (plugin pytest)](https://github.com/syrupy-project/syrupy) a ajouté une dépendance à [Poetry (outil d'emballage)](https://python-poetry.org/), ce qui a compliqué un peu les choses, car Fedora 37 attend une version plus ancienne de Poetry (poetry-1.1.14-1.fc37).

Que pourriez-vous faire ensuite ? Eh bien, vous pourriez essayer d'obtenir une version de Syrupy qui fonctionne avec cette version plus ancienne de Poetry. Mais cela pourrait potentiellement introduire des vulnérabilités sur votre système ou vous forcer à utiliser une version de Syrupy qui ne fonctionne pas du tout avec Textual en raison de changements d'API.

Il est plus facile de travailler vos dépendances vers le haut plutôt que vers le bas. Dans ce cas, j'ai décidé d'arrêter mon expérience car je n'ai pas vraiment besoin d'un RPM pour Fedora 37 moi-même.

### Construction d'une version plus récente non emballée du logiciel

Mock peut-il nous aider avec l'emballage d'une version entièrement nouvelle d'un package ? Textual a apporté d'énormes améliorations et ajouté de nouvelles fonctionnalités dans la première version officielle 1.0.0. Voyons si nous pouvons prendre quelques raccourcis pour construire un RPM que nous pouvons utiliser avec le Python système.

Nous allons recycler le fichier Spec RPM de Textual que nous avons utilisé auparavant, mais avec quelques modifications. Tout d'abord, préparons nos sources à nouveau :

```shell
josevnz@raspberypi1:~$ podman run --mount type=bind,src=$HOME/tmp,target=/mnt/result --rm --privileged --interactive --tty fedora:40 bash
[root@ccae845daa84 /]# dnf install -y rpmdevtool
[root@ccae845daa84 /]# dnf install -y mock && useradd mockbuilder && usermod -a -G mock mockbuilder && chown mockbuilder /mnt/result/ && su - mockbuilder
[root@ccae845daa84 /]# for dep in https://download.fedoraproject.org/pub/fedora/linux/releases/41/Everything/source/tree/Packages/p/python-rich-13.7.1-5.fc41.src.rpm https://download.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/source/tree/Packages/p/python-textual-0.62.0-2.fc41.src.rpm; do rpm -ihv $dep; done
```

Ensuite, nous mettons à jour le [fichier spec RPM](https://rpm-software-management.github.io/rpm/manual/spec.html) pour Textual, qui décrit comment le RPM est créé, en passant la version de 0.62.0 à 1.0.0.

Ce que j'aime faire, c'est créer un nouveau SRPM pour Textual. Pour cela, je fais ce qui suit (je suis toujours à l'intérieur du conteneur Podman – oui, vous pouvez le réutiliser tant qu'il continue de fonctionner) :

1. Installer rpmdevtool, mock, car il contient quelques outils dont j'ai besoin pour configurer l'environnement de construction du SRPM

2. Installer le SRPM original pour 0.6.2. L'installation ne nécessite pas root et crée un nouveau SRPM que je peux utiliser pour démarrer ma nouvelle installation. Les étapes 1 et 2 ci-dessous (c'est facultatif si vous réutilisez le conteneur de l'exemple précédent) :

```bash
[root@ccae845daa84 /]# dnf install -y rpmdevtool
[root@ccae845daa84 /]# dnf install -y mock && useradd mockbuilder && usermod -a -G mock mockbuilder && chown mockbuilder /mnt/result/ && su - mockbuilder
[root@ccae845daa84 /]# for dep in https://download.fedoraproject.org/pub/fedora/linux/releases/41/Everything/source/tree/Packages/p/python-rich-13.7.1-5.fc41.src.rpm https://download.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/source/tree/Packages/p/python-textual-0.62.0-2.fc41.src.rpm; do rpm -ihv $dep; done
```

3. J'ai augmenté la version du package de 0.6.2 dans le fichier SPEC qui est extrait dans ~/rpmbuild/SPECS/python-textual.spec

4. Dire à spectool de récupérer le fichier tar source compressé approprié afin que nous puissions l'utiliser pour préparer un nouveau SRPM

5. Reconstruire le SRPM afin qu'il puisse être utilisé par Mock.

Étapes 3, 4 et 5 ci-dessous :

```shell
[root@ccae845daa84 /]# sed -i 's#0.62.0#1.0.0#' ~/rpmbuild/SPECS/python-textual.spec
[root@ccae845daa84 /]# sed -i 's#%{url}/archive/v%{version}/textual-%{version}.tar.gz#%{url}/archive/refs/tags/v%{version}.tar.gz#' ~/rpmbuild/SPECS/python-textual.spec
[root@ccae845daa84 /]# spectool --get-files ~/rpmbuild/SPECS/python-textual.spec --sourcedir
Downloading: https://github.com/Textualize/textual/archive/refs/tags/v1.0.0.tar.gz
|  28.3 MiB Elapsed Time: 0:00:02                                                                                                                       
Downloaded: v1.0.0.tar.gz
[root@ccae845daa84 /]# rpmbuild -bs ~/rpmbuild/SPECS/python-textual.spec
setting SOURCE_DATE_EPOCH=1717891200
Wrote: /root/rpmbuild/SRPMS/python-textual-1.0.0-2.fc40.src.rpm
```

Maintenant, nous pouvons reconstruire le SRPM et nous assurer que mock peut le trouver lors de l'exécution à partir du volume exposé :

```shell
[root@ccae845daa84 /]# cp -pv /root/rpmbuild/SRPMS/python-textual-1.0.0-2.fc40.src.rpm /tmp/
'/root/rpmbuild/SRPMS/python-textual-1.0.0-2.fc40.src.rpm' -> '/tmp/python-textual-1.0.0-2.fc40.src.rpm'
[root@ccae845daa84 /]# su - mockbuilder
[mockbuilder@ccae845daa84 ~]$ ls -l /tmp/python-textual-1.0.0-2.fc40.src.rpm
-rw-r--r--. 1 root root 29612335 Jan 11 00:12 /tmp/python-textual-1.0.0-2.fc40.src.rpm
```

Moment de vérité, construisons-le :

```shell
[mockbuilder@ccae845daa84 ~]$ mock --nocheck --localrepo /mnt/result/ --chain https://download.fedoraproject.org/pub/fedora/linux/releases/41/Everything/source/tree/Packages/p/python-rich-13.7.1-5.fc41.src.rpm /tmp/python-textual-1.0.0-2.fc40.src.rpm
Wrote: /builddir/build/SRPMS/python-textual-1.0.0-2.fc40.src.rpm
Wrote: /builddir/build/RPMS/python3-textual-1.0.0-2.fc40.noarch.rpm
Wrote: /builddir/build/RPMS/python3-textual-doc-1.0.0-2.fc40.noarch.rpm
INFO: Done(/tmp/python-textual-1.0.0-2.fc40.src.rpm) Config(default) 2 minutes 38 seconds
```

Enfin, testons l'installation en installant les RPMS à l'extérieur du conteneur :

```shell
josevnz@raspberypi1:~$ sudo dnf install /home/josevnz/tmp/results/default/python-rich-13.7.1-5.fc41/python3-rich-13.7.1-5.fc40.noarch.rpm /home/josevnz/tmp/results/default/python-textual-1.0.0-2.fc40/python3-textual-doc-1.0.0-2.fc40.noarch.rpm /home/josevnz/tmp/results/default/python-textual-1.0.0-2.fc40/python3-textual-1.0.0-2.fc40.noarch.rpm
Last metadata expiration check: 3:42:37 ago on Fri 10 Jan 2025 03:50:49 PM EST.
Package python3-rich-13.7.1-5.fc40.noarch is already installed.
Dependencies resolved.
=========================================================================================================================================================
 Package                                    Architecture                 Version                                Repository                          Size
=========================================================================================================================================================
Upgrading:
 python3-textual                            noarch                       1.0.0-2.fc40                           @commandline                       1.3 M
 python3-textual-doc                        noarch                       1.0.0-2.fc40                           @commandline                        24 M
Installing dependencies:
 python3-platformdirs                       noarch                       3.11.0-3.fc40                          fedora                              46 k

Transaction Summary
=========================================================================================================================================================
Install  1 Package
Upgrade  2 Packages

Total size: 25 M
Total download size: 46 k
Is this ok [y/N]: y
Downloading Packages:
python3-platformdirs-3.11.0-3.fc40.noarch.rpm                                                                             53 kB/s |  46 kB     00:00    
---------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                     41 kB/s |  46 kB     00:01     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                 1/1 
  Installing       : python3-platformdirs-3.11.0-3.fc40.noarch                                                                                       1/5 
  Upgrading        : python3-textual-1.0.0-2.fc40.noarch                                                                                             2/5 
  Upgrading        : python3-textual-doc-1.0.0-2.fc40.noarch                                                                                         3/5 
  Cleanup          : python3-textual-0.62.0-2.fc40.noarch                                                                                            4/5 
  Cleanup          : python3-textual-doc-0.62.0-2.fc40.noarch                                                                                        5/5 
  Running scriptlet: python3-textual-doc-0.62.0-2.fc40.noarch                                                                                        5/5 

Upgraded:
  python3-textual-1.0.0-2.fc40.noarch                                       python3-textual-doc-1.0.0-2.fc40.noarch                                      
Installed:
  python3-platformdirs-3.11.0-3.fc40.noarch                                                                                                              

Complete!
```

*Pas mal*, nous pouvons maintenant construire des [TUIs](https://en.wikipedia.org/wiki/Text-based_user_interface) sophistiqués en utilisant Textual et le Python système, sans avoir besoin de créer un environnement virtuel ni de forcer l'installation de packages indésirables sur notre serveur de construction.

## Conclusion

Comme vous pouvez le voir, mock est un outil très précieux qui peut vous aider à automatiser l'emballage des bibliothèques Python qui ne sont pas encore disponibles sur votre plateforme. Il vous permet d'automatiser l'obtention des dépendances pour le RPM et vous alerte lorsque certaines sont manquantes sur votre plateforme.

En bonus, le fait que vous puissiez l'exécuter à l'intérieur de Podman vous offre encore plus d'isolation des RPMs qui pourraient être dangereux lorsqu'ils sont exécutés en tant que root.

### Documentation supplémentaire (RTFM, Lisez le Manuel)

* [RPM-Macros](https://gitlab.com/redhat/centos-stream/rpms/pyproject-rpm-macros/)

* [Mock](https://rpm-software-management.github.io/mock/)

* [Outils de développement RPM](https://fedoraproject.org/wiki/Rpmdevtools)

* [Documentation des macros RPM](https://docs.fedoraproject.org/en-US/packaging-guidelines/Python_201x/#_macros)

* [Emballage des RPMS Python3](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10-beta/html/packaging_and_distributing_software/packaging-python-3-rpms)

* [Spécifications PyPA](https://packaging.python.org/en/latest/specifications/)

* [RPM Textual de Fedora](https://koji.fedoraproject.org/koji/buildinfo?buildID=2466451)