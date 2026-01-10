---
title: Comment accélérer l'accès aux fichiers partagés dans Docker pour Mac
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-17T21:41:52.000Z'
originalURL: https://freecodecamp.org/news/speed-up-file-access-in-docker-for-mac-fbeee65d0ee7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pH318KUH_V10gogDY13Nog.jpeg
tags:
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment accélérer l'accès aux fichiers partagés dans Docker pour Mac
seo_desc: 'By Sebastian Sigl

  Docker just released a native MacOS runtime environment to run containers on Macs
  with ease. They fixed many issues, but the bitter truth is they missed something
  important. The read and write access for mounted volumes is terrible....'
---

Par Sebastian Sigl

[Docker](https://www.docker.com/) vient de publier un environnement d'exécution natif pour MacOS afin de faciliter l'exécution de conteneurs sur Mac. Ils ont résolu de nombreux problèmes, mais la vérité amère est qu'ils ont oublié quelque chose d'important. L'accès en lecture et en écriture pour les volumes montés est terrible.

### Benchmarks

Nous pouvons démarrer un conteneur et écrire dans un volume monté en exécutant les commandes suivantes :

1. Démarrer un conteneur
2. Monter le répertoire courant
3. Écrire des données aléatoires dans un fichier de ce répertoire

```
docker run --rm -it -v "$(PWD):/pwd" -w /pwd alpine time dd if=/dev/zero of=speedtest bs=1024 count=100000
```

Comparons les résultats de Windows, Cent OS et Mac OS :

### Windows 10

```
100000+0 records in
100000+0 records out
real    0m 0.29s
user    0m 0.03s
sys     0m 0.21s
```

### Cent OS

```
100000+0 records in
100000+0 records out
real    0m 0.21s
user    0m 0.02s
sys     0m 0.14s
```

### Mac OS

```
100000+0 records in
100000+0 records out
real 0m 19.32s
user 0m 0.42s
sys 0m 1.46s
```

Le gagnant est... 19 secondes pour l'écriture. Pour la lecture, c'est similaire. Lorsque vous développez une grande application dockerisée, vous êtes dans une mauvaise posture. Habituellement, vous travailleriez sur votre code source et vous ne vous attendriez à aucun ralentissement pour la construction. Mais la vérité amère est que cela prendra une éternité.

Ce [problème GitHub](https://github.com/docker/for-mac/issues/77) suit l'état actuel. Il y a beaucoup de haine, il est donc préférable d'écouter les "membres" plutôt que de lire toutes les frustrations.

@dsheetz de l'équipe Docker pour Mac a cerné le problème :

> Peut-être la chose la plus importante à comprendre est que **les performances du système de fichiers partagé sont multidimensionnelles**. Cela signifie que, selon votre charge de travail, vous pouvez rencontrer des performances exceptionnelles, adéquates ou médiocres avec `osxfs`, le serveur de système de fichiers dans Docker pour Mac. Les API du système de fichiers sont très larges (20-40 types de messages) avec de nombreuses sémantiques complexes impliquant l'état sur disque, l'état du cache en mémoire et l'accès concurrent par plusieurs processus. De plus, `osxfs` intègre une cartographie entre l'API _FSEvents_ d'OS X et l'API _inotify_ de Linux, qui est implémentée à l'intérieur du système de fichiers lui-même, compliquant davantage les choses (comportement du cache en particulier).

> Au plus haut niveau, il y a deux dimensions aux performances du système de fichiers : le _débit_ (lecture/écriture E/S) et la _latence_ (temps aller-retour). Dans un système de fichiers traditionnel sur un SSD moderne, les applications peuvent généralement s'attendre à un débit de quelques Go/s. Avec de grandes opérations E/S séquentielles, `osxfs` peut atteindre un débit d'environ 250 Mo/s, ce qui, bien que ce ne soit pas la vitesse native, ne sera pas le goulot d'étranglement pour la plupart des applications qui fonctionnent de manière acceptable sur les HDD.

> La _latence_ est le temps nécessaire pour qu'un appel système de système de fichiers se termine. Par exemple, le temps entre un thread émettant _write_ dans un conteneur et reprenant avec le nombre d'octets écrits. Avec un système de fichiers classique basé sur des blocs, cette latence est généralement inférieure à 10 µs (microsecondes). Avec `osxfs`, la latence est actuellement d'environ 200 µs pour la plupart des opérations, soit 20 fois plus lente. Pour les charges de travail qui demandent de nombreux allers-retours séquentiels, cela entraîne un ralentissement significatif observable. Pour réduire la latence, nous devons raccourcir le chemin des données d'un appel système Linux à OS X et vice versa. Cela nécessite de régler _chaque composant_ dans le chemin des données à son tour -- certains d'entre eux nécessitent un effort d'ingénierie significatif. Même si nous réalisons une énorme réduction de latence de 100 µs/aller-retour, nous ne verrons toujours "que" un doublement des performances. Cela est typique de l'ingénierie des performances, qui nécessite un effort significatif pour analyser les ralentissements et développer des composants optimisés.

De nombreuses personnes ont créé des solutions de contournement avec différentes approches. Certaines d'entre elles utilisent nfs, Docker dans Docker, la synchronisation bidirectionnelle Unison ou rsync. J'ai essayé certaines solutions, mais aucune d'entre elles n'a fonctionné pour mon conteneur Docker qui contient un grand monolithe Java. Soit elles installent des outils supplémentaires comme vagrant pour réduire la douleur. Vagrant utilise nfs, mais cela reste lent par rapport aux performances natives d'écriture et de lecture. Soit elles sont peu fiables, difficiles à configurer et difficiles à maintenir.

J'ai fait un pas en arrière et j'ai repensé au problème racine. Une approche très bonne est [docker-sync](https://github.com/EugenMayer/docker-sync). C'est une application ruby avec beaucoup d'options. Une option très mature est la synchronisation de fichiers basée sur rsync.

### Rsync

La première version de Rsync date de 1996 (il y a 20 ans). Il est utilisé pour transférer des fichiers entre des systèmes informatiques. Un cas d'utilisation important est la synchronisation unidirectionnelle.

Cela semble bien... n'est-ce pas ?

Docker-sync supporte rsync pour la synchronisation. Au début, cela fonctionnait, mais quelques jours plus tard, j'ai eu des problèmes de connexion entre mon hôte et mon conteneur.

Connaissez-vous ce sentiment lorsque vous voulez corriger quelque chose, mais que cela semble si loin ? Vous réalisez que vous ne comprenez pas ce qui se passe en coulisses.

L'approche rsync semble correcte. Elle s'attaque à la racine du problème : opérer sur des fichiers montés est actuellement extrêmement lent.

J'ai essayé d'autres solutions, mais sans réel succès.

### Construire une image personnalisée

Alors, essayons de nous retrousser les manches. Vous démarrez un serveur rsync dans le conteneur et vous vous y connectez en utilisant rsync. Cette approche fonctionne depuis de nombreuses années pour d'autres cas d'utilisation.

Configurons un conteneur Docker Centos 6 avec un service rsync installé et configuré.

1. Le Dockerfile

```
FROM centos:6
# installer rsync
RUN yum update -y
RUN yum -y install rsync xinetd
# configurer rsync
ADD ./rsyncd.conf /root/
RUN sed -i 's/disable[[:space:]]*=[[:space:]]*yes/disable = no/g' /etc/xinetd.d/rsync # activer rsync
RUN cp /root/rsyncd.conf /etc/rsyncd.conf
RUN /etc/rc.d/init.d/xinetd start
RUN chkconfig xinetd on
# créer le répertoire qui sera synchronisé
RUN mkdir /home/share
# juste pour garder le conteneur en cours d'exécution
CMD /etc/rc.d/init.d/xinetd start && tail -f /dev/null
```

2. Construire le conteneur dans le répertoire du dépôt.

```
docker build . -t docker-rsync
```

3. Démarrer le conteneur et mapper le port du serveur rsync à un port spécifique de l'hôte.

```
docker run -p 10873:873 docker-rsync
```

Maintenant, nous devons synchroniser notre répertoire de partage et synchroniser à nouveau tout changement dès que quelque chose change. Rsync ne synchronisera les changements qu'après une synchronisation initiale.

```
# synchronisation initiale
rsync -avP ./share --delete rsync://localhost:10873/example/
# synchronisation en cas de changement
fswatch -0 ./share | xargs -0 -n 1 -I {} rsync -avP ./share --delete rsync://localhost:10873/example/
```

Fswatch utilise rsync pour communiquer avec le conteneur dès que quelque chose change. Nous n'utilisons aucun type de montage de volume Docker. Par conséquent, toutes les opérations de fichiers resteront dans le conteneur et seront rapides. Chaque fois que nous changeons quelque chose, rsync le transfère dans le conteneur. Bien sûr, vous pouvez utiliser toutes les fonctionnalités de rsync comme les règles de suppression ou les motifs d'exclusion.

Si nous changeons quelque chose (peu importe si c'est un petit projet ou un gros), alors nous voyons quelque chose comme

```
2 files to consider
share/helloWorld.txt
           5 100%    0.00kB/s    0:00:00 (xfer#1, to-check=0/2)
sent 159 bytes  received 44 bytes  406.00 bytes/sec
total size is 5  speedup is 0.02
```

0,02 seconde, super !

Fswatch utilise les événements du système de fichiers sur Mac OS. Ainsi, c'est toujours très rapide et vous pouvez même l'optimiser. Par exemple, en excluant les répertoires liés à la construction comme _target_ ou _node_modules_.

Les sources sont disponibles sur [GitHub](https://github.com/Journerist/docker-rsync-example).

Pour les petits projets, les mauvaises performances ne sont pas un problème critique. Pour les grandes applications, rsync est notre héros. De bons vieux outils, toujours fiables et importants.

Surtout pour tous ceux qui aiment Mac OS et doivent utiliser une VM, connaissent la douleur. Des problèmes comme le mappage de la touche de commande sont ennuyeux. Soit vous la mappez à la touche Windows, soit à la fin vous ne l'utilisez plus. Donc sur Mac OS vous utilisez cmd+c pour copier quelque chose et dans votre conteneur vous utilisez control. Bien sûr, vous pouvez aussi mapper votre contrôle hôte à la commande, mais alors vous avez à nouveau d'autres problèmes. Tout est mieux lorsque vous pouvez travailler dans Mac OS plutôt que dans une machine virtuelle en tant qu'utilisateur Mac.

J'espère que vous avez apprécié l'article. Si vous l'aimez et ressentez le besoin d'une salve d'applaudissements, [suivez-moi sur Twitter](https://twitter.com/sesigl). Je travaille chez eBay Kleinanzeigen, l'une des plus grandes entreprises de petites annonces au monde. Au fait, [nous recrutons](https://jobs.ebayclassifiedsgroup.com/ebay-kleinanzeigen) !

Bon codage :)