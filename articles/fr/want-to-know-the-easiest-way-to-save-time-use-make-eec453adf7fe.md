---
title: Voulez-vous connaître le moyen le plus simple d'économiser du temps ? Utilisez
  `make` !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T22:05:17.000Z'
originalURL: https://freecodecamp.org/news/want-to-know-the-easiest-way-to-save-time-use-make-eec453adf7fe
coverImage: https://cdn-media-1.freecodecamp.org/images/0*tag_5co_wBrmCdD3
tags:
- name: Devops
  slug: devops
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Voulez-vous connaître le moyen le plus simple d'économiser du temps ? Utilisez
  `make` !
seo_desc: 'By Piotr Gaczkowski

  People have always looked for ways to make their work easier. It is a matter of
  debate whether using tools and automation are distinct human features. Or do we
  share them with other species? The fact is that we try to outsource ou...'
---

Par Piotr Gaczkowski

Les gens ont toujours cherché des moyens de faciliter leur travail. Il est sujet à débat de savoir si l'utilisation d'outils et l'automatisation sont des caractéristiques distinctement humaines. Ou les partageons-nous avec d'autres espèces ? Le fait est que nous essayons de sous-traiter nos tâches les plus banales aux machines. Et c'est génial !

### Pourquoi automatiser ?

La répétition mène souvent à l'ennui et à la fatigue. L'ennui est la première étape vers l'épuisement professionnel, tandis que la fatigue est l'une des principales sources d'erreurs. Puisque nous ne voulons pas que nos collègues (ou nous-mêmes) s'épuisent autant que nous ne voulons pas commettre des erreurs coûteuses, nous essayons d'automatiser nos tâches quotidiennes.

Il semble y avoir une prolifération de logiciels dédiés à l'automatisation des tâches courantes. Dans l'écosystème Node.JS seul, il existe (ou existait) des solutions comme Bower, Yeoman, Grunt, Gulp et les scripts NPM.

Mais il existe un bon outil UNIX standard. Par standard, je veux dire qu'il dispose d'une documentation robuste, que beaucoup ont oubliée. Ou jamais apprise ? Je parle de `make`. Plus précisément, cet article se concentre sur GNU make. Il est disponible sur macOS, Windows, Linux et la plupart des autres systèmes d'exploitation.

`make` est si standard que vous l'avez déjà installé. Tapez make dans une ligne de commande et vérifiez par vous-même. Ce logiciel est sorti en 1977, ce qui signifie qu'il est largement testé en conditions réelles. Est-il excentrique ? Oui, même selon les standards des années 70. Mais il fait bien son travail et c'est tout ce que nous attendons de lui.

### N'est-ce pas que Make est pour le code C/C++ ?

Lorsque vous lisez à propos de `make`, vous vous souvenez probablement qu'il existait un outil pour construire des projets C/C++ à l'époque. Cela se faisait comme ceci : `./configure && make && make install`. Oui, nous parlons exactement du même outil. Et franchement, il n'est pas limité à la compilation du code C/C++.

Pour être honnête, il ne peut même pas compiler le code. Pretty much tout ce que `make` comprend, ce sont les fichiers. Il sait si un fichier existe ou non et quel fichier est le plus récent. L'autre moitié de sa puissance réside dans le maintien d'un graphe de dépendances. Pas grand-chose, mais ces deux fonctionnalités constituent sa puissance.

Pour que `make` fasse réellement quelque chose, vous écrivez un ensemble de recettes. Chaque recette se compose d'une cible, de zéro ou plusieurs dépendances et de zéro ou plusieurs règles. Les cibles sont les fichiers que vous souhaitez obtenir. Les dépendances sont les fichiers nécessaires pour créer ou mettre à jour les cibles. L'ensemble des règles décrit le processus de transformation des dépendances en cibles. Par exemple, imaginez que vous souhaitez automatiser l'installation des packages Node.js :

```
node_modules: package.json
	npm install
```

Cela signifie que le **fichier** `node_modules` (oui, les répertoires sont aussi des fichiers) peut être dérivé du **fichier** `package.json` en exécutant la règle `npm install`. Toujours avec moi ?

Maintenant, ces dépendances peuvent également être d'autres cibles. Cela signifie que nous pouvons enchaîner différents ensembles de règles et créer des pipelines. Par exemple, rendre le répertoire des résultats de test dépendant du répertoire de construction, le répertoire de construction dépendant du répertoire `node_modules` et `node_modules` dépendant de `package.json`. Heck, nous pouvons même créer `package.json` dynamiquement en faisant de lui une cible d'une autre règle.

Vous vous souvenez quand j'ai mentionné que `make` suit les fichiers les plus récents ? C'est ce qui nous fait réellement gagner du temps. Vous voyez, sans cette fonctionnalité, chaque fois que nous exécutons `make test` (suivant l'exemple ci-dessus), nous devrions exécuter toute la chaîne depuis le début (`npm install`, build, puis test). Mais si rien n'a changé, pourquoi installer les packages une fois de plus ? Pourquoi construire ? Pourquoi exécuter les tests ?

C'est là que `make` brille vraiment. En déterminant l'ordre des tâches, il vérifie les horodatages des cibles et des dépendances. Il suit la règle **uniquement** si

* une ou plusieurs des dépendances est plus récente que la cible, et
* la cible n'existe pas.

Une chose ! Comme `make test` ne créera pas réellement un fichier nommé `test`, nous devons ajouter cette cible comme dépendance d'une cible `.PHONY`. C'est une autre convention. Comme ceci :

```
.PHONY: test

test: build
	npm test
	
build: node_modules
	npm build
	
node_modules: package.json
```

Dans notre exemple ci-dessus, un seul changement dans `package.json` entraînerait la reconstruction de tout à partir de zéro. Mais si nous ne changeons que le code de l'un des tests, `make` sauterait toutes les étapes précédentes aux tests. À condition, bien sûr, que les dépendances soient correctement écrites.

#### Mais le langage que j'utilise a déjà son propre système de construction...

De nombreux langages de programmation modernes et environnements viennent avec leurs propres outils de construction. Java a Ant, Maven et Gradle, Ruby a son Rake, Python utilise setuptools. Et si vous craignez que je sois sur le point de vous enlever ces jouets et de les remplacer par `make`, vous vous trompez.

Voyez les choses ainsi : combien de temps faut-il pour introduire une personne dans votre équipe et rendre cette personne productive ? Cela signifie configurer l'environnement de développement, installer toutes les dépendances, configurer chaque partie mobile, construire le projet, exécuter le projet, peut-être même déployer le projet dans un environnement de développement.

Un nouveau recruté commencera-t-il le travail réel en quelques heures ? Jours ? Espérons pas des semaines. N'oubliez pas que ce n'est pas seulement le temps du nouveau recruté qui est perdu dans le processus de configuration. Quelqu'un sera également dérangé par de nombreuses questions lorsque les choses tournent mal. Et elles le font généralement.

Il existe une convention que j'aime utiliser dans mes projets. Puisqu'il s'agit d'une convention commune à plusieurs projets, les personnes sont libres de migrer entre eux. Chaque nouveau projet ou chaque nouvelle personne introduite doit apprendre cette convention pour atteindre le résultat souhaité. Cette convention suppose que les projets ont leurs propres Makefiles avec un ensemble de cibles prédéfinies :

* `make prepare` installe toutes les applications externes qui pourraient être nécessaires. Normalement, cela se fait avec un `Brewfile` et Homebrew/Linuxbrew. Comme cette étape est facultative, les développeurs peuvent choisir leur propre méthode d'installation à leurs risques et périls.
* `make dev` configure un environnement de développement local. Habituellement, il construit et lance des conteneurs Docker. Mais comme `make` agit comme un wrapper, il peut être facilement remplacé par ce qui est requis (comme `npm serve`).
* `make deploy` déploie le code dans l'environnement sélectionné (par défaut, c'est `development`). Sous le capot, il exécute généralement Ansible.
* `make infrastructure` est un prérequis pour `make deploy` car il utilise Terraform pour créer lesdits environnements en premier lieu.
* `make all` produit tous les artefacts nécessaires pour le déploiement.

Vous savez ce que cela signifie ? Cela signifie que le `README.md` obligatoire peut se concentrer sur les besoins commerciaux du projet et décrire certains processus de collaboration. À la fin, nous joignons la liste ci-dessus afin que tout le monde sache ce que sont ces cibles. Cela signifie que lorsque vous entrez dans un nouveau projet, tout ce que vous avez à faire est de `make prepare` et `make dev`. Après quelques cycles CPU, vous avez un projet fonctionnel devant vous et vous pouvez commencer à coder.

### J'ai un pipeline d'intégration continue pour cela

À ce stade, certaines personnes peuvent remarquer ce que je vise. Artefacts, étapes, déploiement, infrastructure. C'est ce que fait notre pipeline d'intégration continue/déploiement continu. Je suis sûr que c'est le cas ! Mais rappelez-vous que le CI/CD n'est pas seulement là pour exécuter des tests chaque fois qu'un nouveau commit apparaît.

Un CI/CD correctement implémenté peut aider à réduire le débogage en facilitant la reproduction du problème et en effectuant l'analyse de la cause racine. Comment ? Les artefacts versionnés en sont un moyen. Ils peuvent aider à trouver la cause racine, mais pas nécessairement à la corriger.

Pour corriger le bug, vous devez modifier le code et produire votre propre build. Voyez-vous ce que je vise ? Si votre pipeline CI/CD peut être reproduit localement, les développeurs peuvent tester et déployer de minuscules changements sans avoir besoin d'utiliser réellement le pipeline CI/CD, raccourcissant ainsi le cycle. Et le moyen le plus simple de rendre votre pipeline CI/CD disponible localement est d'en faire un wrapper léger autour de `make`.

Supposons que vous avez un backend et un frontend et que vous avez également des tests pour eux (si ce n'est pas le cas, vous êtes fou de faire du CD sans tests !). Cela ferait quatre travaux CI distincts. Et ils pourraient être résumés à peu près à l'appel de `make backend`, `make test-backend`, `make frontend`, `make test-frontend`. Ou toute autre convention que vous souhaitez suivre.

De cette manière, que ce soit sur une machine locale ou sur CI, le code est construit exactement de la même manière. Exactement les mêmes étapes sont impliquées. Moins il y a de commandes dans votre `Jenkinsfile` ou `.travis.yml` (ou autre), moins vous dépendez d'une machine de construction sacrée.

### Ok, mais quelqu'un utilise-t-il réellement Make ?

Il s'avère que oui. Si vous regardez autour de vous, vous trouverez des articles comme « Time for Makefiles to Make a Comeback » (par Jason Olson). « The Power Of Makefile » (par Ahmad Farag). « Rewriting our deploy tooling: from Makefile to Bash and back again » (par Paul David). Ou « Makefile for Node.js developers » (par Patrick Heneise). Et ce sont des articles de l'année dernière, pas des souvenirs du siècle dernier.

Oui, j'admets que `make` est maladroit. Je connais ses nombreux défauts et ses fonctionnalités linguistiques étranges. Mais montrez-moi un meilleur outil pour l'automatisation réelle du flux de travail de développement et je serai ravi de passer à autre chose. En attendant, je vais ROTFL en regardant ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qb7VuJIDBwyg9MOLyh9rUg.gif)
_[https://asciinema.org/a/dQb0jENCYWsBOCC9UiKxxKG4x](https://asciinema.org/a/dQb0jENCYWsBOCC9UiKxxKG4x" rel="noopener" target="_blank" title=")_

Il est [disponible sur GitHub](https://github.com/DoomHammer/uss_enterprise), si vous voulez le piloter.

### Cool, maintenant montrez-moi le code

Voici quelques extraits pour vous montrer ce qui est possible avec `make`.

```
.PHONY: dev

.stamps:
	@mkdir -p $@

.stamps/git-hooks.installed: | .stamps
	# Cela vérifie si git-hooks est un exécutable et l'installe avec
	# Homebrew/Linuxbrew si possible.
	@if ! command -v git-hooks >/dev/null 2>&1; then \
	  if command -v brew >/dev/null 2>&1; then \
	    brew install git-hooks; \
	  else \
	    echo "Vous devez installer https://github.com/icefox/git-hooks"; \
	    exit 1; \
	  fi; \
	fi
	@touch $@

.git/hooks.old: | .stamps/git-hooks.installed
	git hooks --install

dev: | .git/hooks.old
	pip install -e .[dev]
```

Cet extrait configure un environnement de développement simple. Puisque nous voulons nous assurer que tous les développeurs utilisent le même ensemble de hooks pré-commit tout en travaillant avec Git, nous installons ces hooks pour eux.

Pour ce faire, nous devons installer git-hooks (c'est le nom du gestionnaire de hooks). Nous tirons parti de la connaissance que git-hooks déplace les hooks originaux vers `.git/hooks.old`, donc nous vérifions la présence d'un tel fichier pour déterminer si nous voulons exécuter `git hooks install` ou non.

Un truc que nous utilisons ici est `|` pour désigner des dépendances d'ordre uniquement. Si vous voulez simplement vous assurer que quelque chose existe, et non qu'il change plus récemment qu'une cible, les dépendances d'ordre uniquement sont la solution. Jusqu'à présent, tout va bien, je suppose ?

Maintenant, imaginez que nous voulons construire un conteneur Docker qui contient un fichier que nous ne pouvons pas distribuer dans notre code source.

```
WEBAPP_SOURCES = $(sort $(notdir $(wildcard webapp/**/*)))

all: webapp

.stamps: Makefile
	@mkdir -p $@

third-party/top_secret.xml:
	# WEB_USER et WEB_AUTH_TOKEN sont des variables qui doivent contenir des identifiants
	# requis pour obtenir le fichier.
	@curl -u "$(WEB_USER):$(WEB_AUTH_TOKEN)" https://example.com/downloads/this_is_a_secret.xml -L -o $@

webapp: .stamps/webapp.stamp
.stamps/webapp.stamp: .stamps webapp/Dockerfile third-party/top_secret.xml $(WEBAPP_SOURCES)
	docker build -t example/webapp -f webapp/Dockerfile webapp
	@touch $@

.PHONY: all webapp
```

Puisque nous ne pouvons pas utiliser le fichier réel créé par Docker (car les images ont des permissions strictes), nous faisons la deuxième meilleure chose. Nous créons un fichier vide qui indique que nous avons exécuté avec succès `docker build` à un moment donné.

Une convention courante pour de tels fichiers les appelle « stamps ». Notre stamp d'image Docker dépend évidemment du `Dockerfile`, des fichiers sources et d'une autre cible, qui exécute `curl` pour récupérer le fichier en obtenant les identifiants des variables d'environnement.

Puisque nous ne voulons pas imprimer nos identifiants dans la sortie, nous préférons la commande avec `@`. Cela signifie que la règle elle-même n'est pas imprimée à l'écran. La sortie de la règle, cependant, n'est pas silencieuse. Gardez cela à l'esprit si l'un des programmes que vous souhaitez exécuter a tendance à journaliser des informations sensibles vers stdout ou stderr.

D'accord, nous pouvons configurer des hooks git et nous pouvons construire des images Docker. Pourquoi ne pas laisser les développeurs créer leurs propres environnements dans le cloud et y déployer ?

```
# Nous incluons le Makefile précédent afin de pouvoir construire l'image
include previous.mk

.stamps/webapp_pushed.stamp: .stamps/webapp.stamp
        docker push example/webapp
        @touch $@

infrastructure: $(INFRASTRUCTURE_SOURCES)
        cd deployment/terraform && terraform apply

deploy: all infrastructure
        cd deployment && ansible-playbook -i inventories/hosts deploy.yml

.PHONY: infrastructure deploy
```

L'infrastructure réelle en tant que code et la gestion de la configuration sont hors du cadre de cet article. Laissez-moi vous dire que `terraform apply` gère les ressources cloud et que `ansible-playbook` effectue la configuration sur des machines distantes. Vous savez probablement ce que fait `docker push`. En bref, il pousse l'image locale vers Docker Hub (ou tout autre registre) afin que vous puissiez y accéder de n'importe où. À ce stade, je suis sûr que vous pouvez comprendre ce que fait l'extrait ci-dessus.

### Alors, à qui s'adresse cet outil ?

Bien que DevOps soit en vogue récemment, il existe encore une grande séparation entre les Dev et les Ops. Certains outils sont utilisés uniquement par les Dev, d'autres uniquement par les Ops. Il y a un peu de terrain commun, mais jusqu'où il s'étend dépend de chaque équipe.

La gestion des packages de développement, la disposition du code source, les directives de codage sont tous les domaines des Dev. L'infrastructure en tant que code, la gestion de la configuration et l'orchestration sont des jouets pour les Ops. Le système de construction et le pipeline d'intégration continue peuvent être divisés entre les deux ou appartenir à l'une ou l'autre partie. Pouvez-vous voir comment le terrain commun est étiré à l'extrême ?

`make` change les choses, permettant une collaboration plus large. Puisqu'il sert les besoins à la fois des Dev et des Ops, c'est un terrain commun. Tout le monde parle son langage et tout le monde peut contribuer. Mais parce qu'il est si facile à utiliser même lorsque vous voulez faire des choses complexes (comme dans notre exemple ci-dessus), le vrai pouvoir de DevOps est donné entre les mains de chaque personne de l'équipe. Tout le monde peut exécuter `make test` et tout le monde peut modifier ses règles et dépendances. Tout le monde pourrait exécuter `make infrastructure` et provisionner un beau cluster pour le développement ou la production. Après tout, ils sont documentés dans le même code !

Bien sûr, lorsqu'il y a un terrain commun, il est bon de s'assurer de savoir qui est responsable de quelle partie. La dernière chose que vous voulez, c'est que les gens de Dev et Ops écrasent le travail des uns et des autres ! Mais un excellent travail d'équipe repose toujours sur une excellente communication, donc cela pourrait arriver avec ou sans `make`.

Donc, peu importe si vous utilisez l'une des technologies à la mode associées à DevOps. Vous n'avez peut-être pas besoin et ne voulez pas de Docker, Cloud, Terraform ou Travis. Vous pouvez écrire des applications de bureau, pour ce que cela vaut, et un `Makefile` soigneusement écrit serait toujours un facilitateur DevOps.