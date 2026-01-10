---
title: Construction d'un conteneur Python Data Science avec Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-05T19:00:43.000Z'
originalURL: https://freecodecamp.org/news/building-python-data-science-container-using-docker
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/1_oYWC2Wnc4Nf_mH0WL3ep_w.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Docker
  slug: docker
- name: Docker Containers
  slug: docker-containers
- name: Python
  slug: python
seo_title: Construction d'un conteneur Python Data Science avec Docker
seo_desc: 'By Faizan Bashir


  Photo by Unsplash

  TL;DR

  Artificial Intelligence(AI) and Machine Learning(ML) are literally on fire these
  days. Powering a wide spectrum of use-cases ranging from self-driving cars to drug
  discovery and to God knows what. AI and ML h...'
---

Par Faizan Bashir

![Image](https://cdn-media-1.freecodecamp.org/images/1*oYWC2Wnc4Nf_mH0WL3ep_w.jpeg align="left")

*Photo par* [*Unsplash*](https://unsplash.com/@bryangoffphoto)

### TL;DR

L'intelligence artificielle (IA) et le machine learning (ML) sont littéralement en feu ces jours-ci. Alimentant un large éventail de cas d'utilisation allant des voitures autonomes à la découverte de médicaments et à Dieu sait quoi d'autre. L'IA et le ML ont un avenir brillant et prospère devant eux.

D'un autre côté, Docker a révolutionné le monde informatique avec l'introduction de conteneurs légers éphémères. Les conteneurs empaquettent essentiellement tout le logiciel nécessaire pour fonctionner à l'intérieur d'une image (un ensemble de couches en lecture seule) avec une couche COW (Copy On Write) pour persister les données.

Assez parlé, commençons à construire un conteneur Python pour la data science.

---

### Paquets Python pour la Data Science

Notre conteneur Python pour la data science utilise les paquets Python super cool suivants :

1. **NumPy** : NumPy ou Numeric Python supporte les grands tableaux et matrices multidimensionnels. Il fournit des fonctions précompilées rapides pour les routines mathématiques et numériques. De plus, NumPy optimise la programmation Python avec des structures de données puissantes pour le calcul efficace de tableaux et matrices multidimensionnels.

2. **SciPy** : SciPy fournit des fonctions utiles pour la régression, la minimisation, la transformation de Fourier, et bien plus encore. Basé sur NumPy, SciPy étend ses capacités. La principale structure de données de SciPy est à nouveau un tableau multidimensionnel, implémenté par Numpy. Le paquet contient des outils qui aident à résoudre l'algèbre linéaire, la théorie des probabilités, le calcul intégral, et bien d'autres tâches.

3. **Pandas** : Pandas offre des outils polyvalents et puissants pour manipuler des structures de données et effectuer des analyses de données approfondies. Il fonctionne bien avec des données réelles incomplètes, non structurées et non ordonnées et vient avec des outils pour façonner, agréger, analyser et visualiser des ensembles de données.

4. **SciKit-Learn** : Scikit-learn est un module Python intégrant une large gamme d'algorithmes de machine learning de pointe pour des problèmes supervisés et non supervisés à moyenne échelle. C'est l'une des bibliothèques de machine learning les plus connues pour Python. Le paquet Scikit-learn se concentre sur l'apport du machine learning aux non-spécialistes en utilisant un langage de haut niveau à usage général. L'accent principal est mis sur la facilité d'utilisation, la performance, la documentation et la cohérence de l'API. Avec des dépendances minimales et une distribution facile sous la licence BSD simplifiée, SciKit-Learn est largement utilisé dans les milieux académiques et commerciaux. Scikit-learn expose une interface concise et cohérente aux algorithmes courants de machine learning, ce qui simplifie l'intégration du ML dans les systèmes de production.

5. **Matplotlib** : Matplotlib est une bibliothèque de traçage 2D pour Python, capable de produire des figures de qualité publication dans une grande variété de formats de copie papier et d'environnements interactifs sur différentes plateformes. Matplotlib peut être utilisé dans des scripts Python, le shell Python et IPython, le notebook Jupyter, les serveurs d'applications web, et quatre boîtes à outils d'interface graphique.

6. **NLTK** : NLTK est une plateforme de premier plan pour construire des programmes Python pour travailler avec des données de langage humain. Il fournit des interfaces faciles à utiliser pour plus de 50 corpus et ressources lexicaux tels que WordNet, ainsi qu'une suite de bibliothèques de traitement de texte pour la classification, la tokenisation, la stemmatisation, l'étiquetage, l'analyse et le raisonnement sémantique.

---

### Construction du conteneur Data Science

Python devient rapidement le langage de prédilection pour les data scientists et pour cette raison, nous allons utiliser Python comme langage de choix pour construire notre conteneur de data science.

#### L'image de base Alpine Linux

Alpine Linux est une minuscule distribution Linux conçue pour les utilisateurs avancés qui apprécient la sécurité, la simplicité et l'efficacité des ressources.

Comme revendiqué par [Alpine](https://alpinelinux.org/) :

> *Petite. Simple. Sécurisée. Alpine Linux est une distribution Linux légère et orientée sécurité basée sur musl libc et busybox.*

L'image Alpine est surprenamment minuscule avec une taille ne dépassant pas 8 Mo pour les conteneurs. Avec un minimum de paquets installés pour réduire la surface d'attaque sur le conteneur sous-jacent. Cela fait d'Alpine une image de choix pour notre conteneur de data science.

Télécharger et exécuter un conteneur Alpine Linux est aussi simple que :

```bash
$ docker container run --rm alpine:latest cat /etc/os-release
```

Dans notre Dockerfile, nous pouvons simplement utiliser l'image de base Alpine comme suit :

```bash
FROM alpine:latest
```

---

#### Assez parlé, construisons le Dockerfile

Maintenant, travaillons sur le Dockerfile.

```bash
FROM alpine:latest

LABEL MAINTAINER="Faizan Bashir <faizan.ibn.bashir@gmail.com>"

# Liaison de locale.h en tant que xlocale.h
# Cela est fait pour assurer l'installation réussie du paquet python numpy
# voir https://forum.alpinelinux.org/comment/690#comment-690 pour plus d'informations.

WORKDIR /var/www/

# PAQUETS LOGICIELS
#   * musl: bibliothèque C standard
#   * lib6-compat: bibliothèques de compatibilité pour glibc
#   * linux-headers: souvent nécessaires, et un nom de paquet inhabituel d'Alpine.
#   * build-base: utilisé pour inclure les paquets de développement de base (gcc)
#   * bash: pour que nous puissions accéder à /bin/bash
#   * git: pour faciliter les clones de dépôts
#   * ca-certificates: pour la vérification SSL pendant Pip et easy_install
#   * freetype: bibliothèque utilisée pour rendre le texte sur des bitmaps, et fournit un support pour les opérations liées aux polices
#   * libgfortran: contient une bibliothèque partagée Fortran, nécessaire pour exécuter Fortran
#   * libgcc: contient du code partagé qui serait inefficace à dupliquer chaque fois ainsi que des routines auxiliaires et un support d'exécution
#   * libstdc++: La bibliothèque standard GNU C++. Ce paquet contient une bibliothèque d'exécution supplémentaire pour les programmes C++ construits avec le compilateur GNU
#   * openblas: implémentation open source de l'API BLAS (Basic Linear Algebra Subprograms) avec de nombreuses optimisations artisanales pour des types de processeurs spécifiques
#   * tcl: langage de script
#   * tk: boîte à outils GUI pour le langage de script Tcl
#   * libssl1.0: bibliothèques partagées SSL
ENV PACKAGES="\
    dumb-init \
    musl \
    libc6-compat \
    linux-headers \
    build-base \
    bash \
    git \
    ca-certificates \
    freetype \
    libgfortran \
    libgcc \
    libstdc++ \
    openblas \
    tcl \
    tk \
    libssl1.0 \
"

# PAQUETS PYTHON POUR LA DATA SCIENCE
#   * numpy: support pour les grands tableaux et matrices multidimensionnels
#   * matplotlib: bibliothèque de traçage pour Python et son extension de mathématiques numériques NumPy.
#   * scipy: bibliothèque utilisée pour le calcul scientifique et le calcul technique
#   * scikit-learn: bibliothèque de machine learning qui s'intègre avec NumPy et SciPy
#   * pandas: bibliothèque fournissant des structures de données haute performance, faciles à utiliser et des outils d'analyse de données
#   * nltk: suite de bibliothèques et de programmes pour le traitement du langage naturel symbolique et statistique pour l'anglais
ENV PYTHON_PACKAGES="\
    numpy \
    matplotlib \
    scipy \
    scikit-learn \
    pandas \
    nltk \
" 

RUN apk add --no-cache --virtual build-dependencies python --update py-pip \
    && apk add --virtual build-runtime \
    build-base python-dev openblas-dev freetype-dev pkgconfig gfortran \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && pip install --upgrade pip \
    && pip install --no-cache-dir $PYTHON_PACKAGES \
    && apk del build-runtime \
    && apk add --no-cache --virtual build-dependencies $PACKAGES \
    && rm -rf /var/cache/apk/*

CMD ["python"]
```

La directive `FROM` est utilisée pour définir `alpine:latest` comme image de base. En utilisant la directive `WORKDIR`, nous définissons `/var/www` comme répertoire de travail pour notre conteneur. `ENV PACKAGES` liste les paquets logiciels requis pour notre conteneur comme `git`, `blas` et `libgfortran`. Les paquets Python pour notre conteneur de data science sont définis dans `ENV PACKAGES`.

Nous avons combiné toutes les commandes sous une seule directive `RUN` du Dockerfile pour réduire le nombre de couches, ce qui aide à réduire la taille de l'image résultante.

---

#### Construction et étiquetage de l'image

Maintenant que nous avons défini notre Dockerfile, naviguez vers le dossier avec le Dockerfile en utilisant le terminal et construisez l'image en utilisant la commande suivante :

```bash
$ docker build -t faizanbashir/python-datascience:2.7 -f Dockerfile .
```

Le drapeau `-t` est utilisé pour nommer une étiquette au format 'nom:étiquette'. Le drapeau `-f` est utilisé pour définir le nom du Dockerfile (par défaut, c'est 'PATH/Dockerfile').

---

#### Exécution du conteneur

Nous avons construit et étiqueté avec succès l'image Docker, nous pouvons maintenant exécuter le conteneur en utilisant la commande suivante :

```bash
$ docker container run --rm -it faizanbashir/python-datascience:2.7 python
```

Et voilà, nous sommes accueillis par la vue d'un shell Python prêt à effectuer toutes sortes de tâches cool en data science.

```bash
Python 2.7.15 (default, Aug 16 2018, 14:17:09) [GCC 6.4.0] on linux2 Type "help", "copyright", "credits" or "license" for more information. >>>
```

Notre conteneur vient avec Python 2.7, mais ne soyez pas triste si vous voulez travailler avec Python 3.6. Voici le Dockerfile pour Python 3.6 :

```bash
https://gist.github.com/faizanbashir/9443a7149cc53f81d84d0d356f871ec7#file-datascience-python3-6-dockerfile
```

Construisez et étiquetez l'image comme suit :

```bash
FROM alpine:latest

LABEL MAINTAINER="Faizan Bashir <faizan.ibn.bashir@gmail.com>"

# Liaison de locale.h en tant que xlocale.h
# Cela est fait pour assurer l'installation réussie du paquet python numpy
# voir https://forum.alpinelinux.org/comment/690#comment-690 pour plus d'informations.

WORKDIR /var/www/

# PAQUETS LOGICIELS
#   * musl: bibliothèque C standard
#   * lib6-compat: bibliothèques de compatibilité pour glibc
#   * linux-headers: souvent nécessaires, et un nom de paquet inhabituel d'Alpine.
#   * build-base: utilisé pour inclure les paquets de développement de base (gcc)
#   * bash: pour que nous puissions accéder à /bin/bash
#   * git: pour faciliter les clones de dépôts
#   * ca-certificates: pour la vérification SSL pendant Pip et easy_install
#   * freetype: bibliothèque utilisée pour rendre le texte sur des bitmaps, et fournit un support pour les opérations liées aux polices
#   * libgfortran: contient une bibliothèque partagée Fortran, nécessaire pour exécuter Fortran
#   * libgcc: contient du code partagé qui serait inefficace à dupliquer chaque fois ainsi que des routines auxiliaires et un support d'exécution
#   * libstdc++: La bibliothèque standard GNU C++. Ce paquet contient une bibliothèque d'exécution supplémentaire pour les programmes C++ construits avec le compilateur GNU
#   * openblas: implémentation open source de l'API BLAS (Basic Linear Algebra Subprograms) avec de nombreuses optimisations artisanales pour des types de processeurs spécifiques
#   * tcl: langage de script
#   * tk: boîte à outils GUI pour le langage de script Tcl
#   * libssl1.0: bibliothèques partagées SSL
ENV PACKAGES="\
    dumb-init \
    musl \
    libc6-compat \
    linux-headers \
    build-base \
    bash \
    git \
    ca-certificates \
    freetype \
    libgfortran \
    libgcc \
    libstdc++ \
    openblas \
    tcl \
    tk \
    libssl1.0 \
    "

# PAQUETS PYTHON POUR LA DATA SCIENCE
#   * numpy: support pour les grands tableaux et matrices multidimensionnels
#   * matplotlib: bibliothèque de traçage pour Python et son extension de mathématiques numériques NumPy.
#   * scipy: bibliothèque utilisée pour le calcul scientifique et le calcul technique
#   * scikit-learn: bibliothèque de machine learning qui s'intègre avec NumPy et SciPy
#   * pandas: bibliothèque fournissant des structures de données haute performance, faciles à utiliser et des outils d'analyse de données
#   * nltk: suite de bibliothèques et de programmes pour le traitement du langage naturel symbolique et statistique pour l'anglais
ENV PYTHON_PACKAGES="\
    numpy \
    matplotlib \
    scipy \
    scikit-learn \
    pandas \
    nltk \
    " 

RUN apk add --no-cache --virtual build-dependencies python3 \
    && apk add --virtual build-runtime \
    build-base python3-dev openblas-dev freetype-dev pkgconfig gfortran \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && python3 -m ensurepip \
    && rm -r /usr/lib/python*/ensurepip \
    && pip3 install --upgrade pip setuptools \
    && ln -sf /usr/bin/python3 /usr/bin/python \
    && ln -sf pip3 /usr/bin/pip \
    && rm -r /root/.cache \
    && pip install --no-cache-dir $PYTHON_PACKAGES \
    && apk del build-runtime \
    && apk add --no-cache --virtual build-dependencies $PACKAGES \
    && rm -rf /var/cache/apk/*

CMD ["python3"]
```

Exécutez le conteneur comme suit :

```bash
$ docker container run --rm -it faizanbashir/python-datascience:3.6 python
```

Avec cela, vous avez un conteneur prêt à l'emploi pour faire toutes sortes de choses cool en data science.

---

### Servir le pudding

Bien sûr, vous avez le temps et les ressources pour configurer tout cela. Au cas où vous ne l'auriez pas, vous pouvez tirer les images existantes que j'ai déjà construites et poussées vers le registre de Docker [Docker Hub](https://hub.docker.com/) en utilisant :

```bash
# Pour Python 2.7
$ docker pull faizanbashir/python-datascience:2.7
```

```bash
# Pour Python 3.6
$ docker pull faizanbashir/python-datascience:3.6
```

Après avoir tiré les images, vous pouvez utiliser l'image ou l'étendre dans votre fichier Dockerfile ou l'utiliser comme image dans votre fichier docker-compose ou stack.

---

### Après-coup

Le monde de l'IA et du ML devient assez excitant ces jours-ci et continuera à devenir encore plus excitant. Les grands acteurs investissent massivement dans ces domaines. Il est temps de commencer à exploiter la puissance des données, qui sait où cela pourrait mener à quelque chose de merveilleux.

Vous pouvez consulter le code ici.

[**faizanbashir/python-datascience**](https://github.com/faizanbashir/python-datascience)
[\_Docker image for python datascience container with NumPy, SciPy, Scikit-learn, Matplotlib, nltk, pandas packages26\_github.com](https://github.com/faizanbashir/python-datascience)

J'espère que cet article a aidé à construire des conteneurs pour vos projets de data science. Applaudissez si cela a augmenté vos connaissances, aidez-le à atteindre plus de personnes.