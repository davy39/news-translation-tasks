---
title: Comment configurer facilement votre environnement de développement Ruby on
  Rails avec Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-15T21:17:03.000Z'
originalURL: https://freecodecamp.org/news/painless-rails-development-environment-setup-with-docker
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/image-136-2.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: Ruby on Rails
  slug: ruby-on-rails
seo_title: Comment configurer facilement votre environnement de développement Ruby
  on Rails avec Docker
seo_desc: 'By Jonathan Cunanan

  You''ve likely heard about Docker terms like containers, images, services, volumes,
  network, Dockerfile, docker-compose file, right? Or you''ve watched some videos
  about what it is, but you''re not sure how can it apply to your daily...'
---

Par Jonathan Cunanan

Vous avez probablement entendu parler des termes Docker comme conteneurs, images, services, volumes, réseau, Dockerfile, fichier docker-compose, n'est-ce pas ? Ou vous avez regardé des vidéos sur ce que c'est, mais vous n'êtes pas sûr de comment cela peut s'appliquer à votre vie quotidienne en tant que développeur ?

C'est ce que j'ai d'abord pensé après avoir regardé des vidéos sur Docker. Non seulement Docker peut exécuter des applications web, des serveurs et des bases de données, mais il peut également être un environnement de développement local ! J'ai écrit cet article non seulement pour que vous puissiez apprendre à le faire, mais aussi pour moi, afin de ne pas l'oublier. Commençons !

## Table des matières

* [Pourquoi Docker ?](#heading-pourquoi-docker)
* [Installation de Docker et fichiers Ignore](#heading-installation-de-docker-et-fichiers-ignore)
* [Dockerfile et Docker-Compose](#heading-dockerfile-et-docker-compose)
* [Construction et exécution du conteneur](#heading-construction-et-execution-du-conteneur)
* [Création d'une nouvelle application rails et démarrage du serveur](#heading-test-execution-dune-application-rails)
* [Nettoyage](#heading-nettoyage)
* [Conclusion et dépôt](#heading-conclusion)

## Pourquoi Docker ?

Pourquoi utiliser Docker ? Pourquoi ne pas simplement l'installer sur votre machine locale et installer Ruby Version Manager (rvm) ou Ruby Environment (rbenv) ?

Configurer Ruby On Rails avec ces outils est génial. Cela m'a pris plus de 3 heures d'installation, de dépannage et de recherche dans la documentation pour le faire fonctionner. Mais récemment, j'ai reformatté mon mac. Mais je n'ai pas listé ou noté les sites que j'ai visités pour le faire fonctionner sur ma machine. J'ai oublié comment l'installer à nouveau et c'est pénible de répéter les étapes.

C'est là que Docker brille. Installez Docker, chargez vos Dockerfiles, exécutez quelques commandes dans votre terminal, et vous êtes déjà configuré ! Et aussi, que se passe-t-il si vous voulez tout désinstaller ? Il est difficile de suivre les étapes à annuler. Avec Docker, ce n'est que quelques commandes pour nettoyer.

Lorsque je regardais un [tutoriel en ligne sur Docker](https://www.pluralsight.com/courses/docker-web-development), Dan Wahlin, l'enseignant, a dit que l'un des avantages de Docker est d'accélérer l'intégration des développeurs. Dan a dit dans son tutoriel :

>  _"Docker peut aider car nous pouvons créer une ou plusieurs images qui peuvent ensuite être converties en conteneurs en cours d'exécution, et ces conteneurs peuvent fonctionner sur nos différentes machines de développeurs, et même sur celles des designers."_

Disons que vous avez une équipe de développeurs, de designers et de testeurs, et une application avec un serveur backend, un serveur de base de données et un serveur de cache. Vous avez 12 machines propres, avec une combinaison de linux et de mac. Voulez-vous vraiment installer, dépanner et suivre des instructions d'installation variables qui dépendent de la machine ? Puis faire fonctionner les pièces, une par une sur chaque machine, sans l'assurance qu'ils ne rencontreront pas d'erreurs variables en cours de route ?

C'est pourquoi j'ai pris le temps d'étudier Docker. Avec quelques commandes et quelques lignes de fichier de configuration, vous êtes déjà configuré. Dans la section suivante, nous allons nous salir les mains avec la configuration de Docker.

## Installation de Docker et inclusion des fichiers Ignore

### 1. Installer Docker

Je ne vais pas trop parler de l'installation de Docker, il y a beaucoup de vidéos là-bas. Mais généralement, il suffit de télécharger et d'ouvrir l'installateur, de créer un compte sur dockerhub, et vous êtes prêt à partir. Consultez la [documentation d'installation de Docker](https://docs.docker.com/install/).

### 2. Créer un fichier `.dockerignore`

Qu'est-ce qu'un fichier dockerignore ? Le fichier dockerignore indique simplement à Docker quels fichiers ignorer dans son conteneur. Un exemple est lorsque vous avez des actifs minifiés, des fichiers js, css, qui changent de temps en temps lorsque vous modifiez le code original. Cela s'applique également aux fichiers gitignore. Généralement, la liste des fichiers recommandés à ignorer se trouve généralement sur Internet. Vous pouvez [copier ce gist](https://gist.github.com/neckhair/ace5d1679dd896b71403fda4bc217b9e) dans votre propre `.dockerignore`.

Et si vous utilisez git, mettez [ce snippet de code](https://www.gitignore.io/api/node,ruby,rails,linux,macos) dans votre `.gitignore`.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-140.png)
_L'apparence de votre dossier de projet ressemblera à ceci._

Les fichiers ignore sont un peu longs, c'est pourquoi je n'ai mis que des liens.

## Dockerfile et fichier docker-compose

C'est là que se déroule la plupart des opérations. Considérez ces deux fichiers comme un ensemble d'instructions que Docker suit pour configurer votre conteneur virtuel. Le Dockerfile et le fichier docker-compose fonctionnent main dans la main. Vous pouvez avoir plusieurs Dockerfiles pour différents services, et un fichier docker-compose pour les lier ensemble.

### 3. Créer un fichier nommé `Dockerfile`

Un Dockerfile est un fichier avec un ensemble de règles que vous allez définir et que Docker suivra. Il existe des ensembles de règles pré-construits sur [Docker Hub](https://hub.docker.com/). Un exemple est les instructions d'installation pré-construites pour MySQL, ou PHP, ou Node.js. Après avoir créé votre `Dockerfile`, mettez ce code dans votre Dockerfile. Et je vais passer en revue une brève explication de ce que font ces lignes.

```dockerfile
FROM ruby

WORKDIR /home/app

ENV PORT 3000

EXPOSE $PORT

RUN gem install rails bundler
RUN gem install rails
RUN apt-get update -qq && apt-get install -y nodejs

ENTRYPOINT [ "/bin/bash" ]

```

* `FROM ruby` - cela signifie que Docker va récupérer une configuration pré-construite par ruby. Vous n'avez pas besoin de penser à mettre à jour ou à installer sur votre machine la dernière version de ruby. Vous verrez la liste des images pré-construites de Docker [sur leur Dockerhub](https://hub.docker.com/). Pensez-y comme npm.
* `WORKDIR /home/app` - Répertoire de travail. Le répertoire de travail signifie que ce sera votre emplacement de dossier par défaut lorsque vous démarrerez votre environnement de développement. Vous pouvez le nommer comme vous voulez.
* `ENV PORT 3000` - Variable d'environnement. Cela définira une variable nommée `$PORT` sur votre terminal bash pour être '3000'.
* `EXPOSE $PORT` - expose le port 3000 (que nous avons défini précédemment) du conteneur virtuel à votre machine locale.
* `RUN` - Les commandes Run sont des instructions de configuration que vous voulez que le terminal exécute avant de l'utiliser. Dans notre cas, nous avons installé ruby on rails, bundler et node.js avant même d'utiliser l'environnement de développement afin que tout soit prêt lorsque nous l'utiliserons.
* `ENTRYPOINT ["/bin/bash"]` - cette commande indique à Docker quelle commande exécuter lorsque nous exécutons le conteneur. Dans notre cas, nous devons exécuter le terminal bash afin d'avoir accès à rails.

Notez que ces explications sont seulement brèves. Vous pouvez voir plus d'explications ou vous pouvez faire une plongée profonde sur la [documentation de référence Dockerfile](https://docs.docker.com/engine/reference/builder/).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-141.png)
_Votre Dockerfile ressemblera à quelque chose comme ceci._

Vous pouvez faire toutes sortes de choses cool avec Dockerfile. Dans mon cas, j'ai essayé d'installer zsh et [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) sur mon conteneur car il a des fonctionnalités de complétion automatique cool. Mais dans notre exemple, nous n'en avons pas vraiment besoin, cela ne ferait qu'augmenter la taille de notre image, donc je ne l'ai pas inclus.

### 4. Créer un fichier nommé `docker-compose.yml`

Le fichier docker-compose est un fichier qui lie différents services ensemble. Un bon exemple est lorsque vous connectez votre application rails à différents serveurs comme un serveur de base de données MySQL ou un serveur de cache redis. Vous pouvez facilement les faire fonctionner avec ce fichier. Mais pour notre cas, nous allons nous en tenir à la configuration minimale pour des raisons de clarté. Un fichier YAML est un type de fichier markdown avec différentes règles sur la façon de formater votre fichier. Pensez simplement à cela comme un fichier JSON, sans les accolades. Mettez ceci dans votre fichier `docker-compose.yml`.

```yaml
version: "3.7"

services:
  ruby_dev:
    build: .
    container_name: ruby_container
    ports:
      - "3000:3000"
    volumes:
      - ./:/home/app

```

Comme vous pouvez le voir, cela ressemble un peu au Dockerfile, mais avec un peu d'indentation. Passons en revue les lignes.

* `version` - Au fil du temps, le fichier docker-compose a subi des changements. C'est pourquoi dans les fichiers docker-compose, ils doivent spécifier quelle version ils utilisent. Dans notre cas, nous utilisons simplement la dernière version à ce jour.
* `services` - Spécifiez la liste des services. Comme je l'ai dit plus tôt, vous pouvez avoir de nombreux services comme un serveur rails et un serveur MySQL dans votre projet. Vous pouvez nommer vos services comme vous le souhaitez. Je l'ai nommé `ruby_dev`.
* `build: .` - Le point ici signifie un chemin de fichier où trouver le Dockerfile, qui sont les instructions de construction.
* `container_name` - Le nom du conteneur.
* `ports:` - ce sont les ports à exposer du conteneur Docker à notre machine locale hôte. Le modèle ici est `HOST:CONTAINER`. Dans notre cas, c'est "3000:3000". Ce qui signifie que nous permettons au port du serveur Rails par défaut (3000) d'être disponible sur notre machine locale "localhost:3000".
* `volumes:` - volume signifie que même si nous quittons ou supprimons Docker, nous pouvons spécifier quels fichiers nous pouvons conserver sur notre machine locale. Nous avons mis `./:/home/app` là parce que nous avons nommé dans notre Dockerfile plus tôt le workdir comme étant `/home/app`.

Vous pouvez voir plus d'explications sur la [documentation de référence Docker Compose](https://docs.docker.com/compose/compose-file/).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-142.png)
_Votre docker-compose.yml ressemblera à quelque chose comme ceci._

## Construction et exécution du conteneur

Avec tous nos fichiers de configuration configurés, construisons et exécutons le conteneur ! Après les nombreux termes que nous avons rencontrés, la construction et l'exécution du conteneur sont beaucoup plus simples. Cela n'impliquera que quelques commandes.

### 5. Dans votre terminal, exécutez `docker-compose build`

L'exécution de cette commande récupérera le Dockerfile et installera toutes les choses nécessaires pour créer un environnement de développement rails. Notez que l'installation peut prendre un certain temps car Docker devra télécharger les packages nécessaires.

### 6. Dans votre terminal, exécutez `docker-compose run --rm --service-ports ruby_dev`

Cette commande démarrera un terminal bash qui sera votre environnement de développement rails où les commandes rails sont disponibles. Avec seulement ces deux commandes et deux fichiers de configuration, vous avez déjà un environnement rails sans même passer par un journal de dépannage ! Remarquez que notre commande a quelques drapeaux, `--rm` signifie supprimer le conteneur après l'avoir utilisé, et `--service-ports` signifie utiliser le port 3000 dans notre conteneur afin que nous puissions voir notre serveur rails en action. Le nom `ruby_dev` provient également des services trouvés dans notre docker-compose.yml.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-143.png)
_Votre terminal pourrait ressembler à ceci après avoir exécuté la commande run. Vérifiez s'il y a rails en exécutant la commande `rails -v`. Les versions peuvent varier._

## Test d'exécution d'une application rails

Maintenant que nous avons réussi à créer notre environnement de développement rails, nous allons tester une application rails exemple.

### 1. Exécutez `rails new myapp && cd myapp`

Cette commande créera une nouvelle application rails dans un dossier nommé myapp. Après cela, le terminal ira dans le dossier. Vous pouvez le nommer comme vous le souhaitez.

### 2. Mettez à jour et installez les gems. Exécutez `bundle update && bundle install`

Assurez-vous simplement d'être dans le bon dossier, dans `myapp`, qui contient les fichiers de l'application rails. Cette commande mettra à jour et installera vos dépendances.

### 3. Testez le serveur en exécutant `rails server -p $PORT -b 0.0.0.0`

Vous souvenez-vous du port que nous avons spécifié dans notre Dockerfile auparavant ? C'est là que nous pouvons l'utiliser. Dans notre cas, rails utilisera le port 3000 pour démarrer le serveur. N'oubliez pas de mettre `-b 0.0.0.0` car vous ne verrez pas l'application sur votre machine locale sans cela.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-144.png)
_Hello rails splash screen. Yeah rails!!!_

### 4. Arrêtez le serveur en appuyant sur `ctrl-d` sur votre clavier.



## Nettoyage

Après avoir terminé tout, vous pouvez quitter votre conteneur en exécutant `exit` sur le terminal bash de votre conteneur. Le drapeau `--rm` que vous avez tapé auparavant supprimera le conteneur, mais vous conserverez vos fichiers ruby on rails.

### Exécutez `docker-compose down` pour nettoyer

Le nettoyage est lorsque vous avez terminé avec le projet et que vous souhaitez supprimer votre environnement de développement afin de gagner de l'espace. Si vous avez vraiment terminé, vous pouvez utiliser cette commande. Docker supprimera toute votre configuration et les images que vous avez téléchargées. C'est si puissant, car imaginez que vous avez suivi beaucoup d'étapes et beaucoup d'installations sur votre mac. La seule façon de supprimer cette configuration est de les désinstaller une par une. Avec Docker de notre côté, ce n'est qu'une seule commande. Aww yeah !

## Conclusion

Content que vous ayez parcouru tout cela ! Regardons le tableau d'ensemble. La configuration d'un environnement de développement dans Docker peut être décomposée en 2 étapes :

1. Listez les instructions dont vous avez besoin dans votre Dockerfile et votre fichier docker-compose.
2. Démarrez, arrêtez ou nettoyez votre environnement de développement avec la commande `docker-compose`.

C'est une grande victoire pour nous. Vous devez simplement conserver le Dockerfile et le fichier compose et chaque fois que vous changez de machine, vous exécutez simplement deux commandes ! Configurez une fois et oubliez.

### Dépôt

Vous pouvez voir le dépôt sur la façon dont la configuration est faite, et les commandes supplémentaires dont vous avez besoin ici en consultant le [dépôt github complet ici.](https://github.com/jcunanan05/rails-docker)

Si vous trouvez l'article utile, ou si vous avez des questions supplémentaires, posez-les dans les commentaires. Je serai ravi de vous aider !

Cet article a été écrit par Jonathan Cunanan sur [freeCodeCamp News](https://www.freecodecamp.org/news/painless-rails-development-environment-setup-with-docker/).

[? Twitter](https://twitter.com/devJonathanC_) - [? freeCodeCamp](https://www.freecodecamp.org/jcunanan05) -  [? Portfolio](https://jonathancunanan.com) - [F527FE0F Github](https://github.com/jcunanan05)