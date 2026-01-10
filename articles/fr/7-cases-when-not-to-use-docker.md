---
title: 7 Cas où vous ne devriez pas utiliser Docker
subtitle: ''
author: Oleh Romanyuk
co_authors: []
series: null
date: '2019-11-19T16:23:17.000Z'
originalURL: https://freecodecamp.org/news/7-cases-when-not-to-use-docker
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/Docker-1.png
tags:
- name: Docker
  slug: docker
- name: Docker Containers
  slug: docker-containers
seo_title: 7 Cas où vous ne devriez pas utiliser Docker
seo_desc: 'Docker is a game-changer. But it is not a one-size-fits-all solution.

  There are many good things about Docker. It packs, ships, and runs applications
  as a lightweight, portable, and self-sufficient containerization tool. Docker is
  great for businesse...'
---

## Docker est révolutionnaire. Mais ce n'est pas une solution universelle.

Il y a beaucoup de bonnes choses à propos de Docker. Il emballe, livre et exécute des applications en tant qu'outil de conteneurisation léger, portable et autonome. Docker est idéal pour les entreprises de toutes tailles. Lorsque vous travaillez sur un morceau de code en petite équipe, il élimine le problème du "mais ça marche sur ma machine". Pendant ce temps, les entreprises peuvent utiliser Docker pour construire des pipelines de livraison de logiciels Agile afin de livrer de nouvelles fonctionnalités plus rapidement et de manière plus sécurisée.

Avec son système de conteneurisation intégré, Docker est un excellent outil pour le cloud computing. À son tour, Docker Swarm fait progresser la clusterisation et la conception décentralisée. Cela semble trop beau pour être vrai, n'est-ce pas ? Eh bien, il existe encore plusieurs cas où il ne faut pas utiliser Docker. En voici sept.

![ne pas utiliser docker](https://images.ctfassets.net/6xhdtf1foerq/2JJ68pTAT6ZhVo05jVwbWI/d79861dd9b194ee83a313ce18f8b624e/Infographics__3_-min.png?fm=png&q=85&w=1000)

Passons en revue ces cas un par un.

## **Ne pas utiliser Docker si vous avez besoin d'augmenter la vitesse**

Les conteneurs Docker sont plus petits et nécessitent moins de ressources qu'une machine virtuelle avec un serveur et une base de données. En même temps, Docker utilisera autant de ressources système que le planificateur de noyau de l'hôte le permettra. Vous ne devez pas vous attendre à ce que Docker accélère une application de quelque manière que ce soit.

De plus, Docker pourrait même la rendre plus lente. Si vous travaillez avec, vous devez définir des limites sur la quantité de mémoire, de CPU ou d'E/S de bloc que le conteneur peut utiliser. Sinon, si le noyau détecte que la mémoire de la machine hôte est trop faible pour effectuer des fonctions système importantes, il pourrait commencer à tuer des processus importants. Si le mauvais processus est tué (y compris Docker lui-même), le système sera instable.

Malheureusement, les ajustements de mémoire de Docker – la priorité de manque de mémoire sur le démon Docker – ne résolvent pas ce problème. En revanche, une couche supplémentaire entre une application et le système d'exploitation pourrait également entraîner une réduction de la vitesse. Pourtant, cette diminution sera insignifiante. Les conteneurs Docker ne sont pas entièrement isolés et ne contiennent pas un système d'exploitation complet comme toute machine virtuelle.

## **Ne pas utiliser Docker si vous privilégiez la sécurité**

Le plus grand avantage de sécurité de Docker est qu'il divise l'application en parties plus petites. Si la sécurité d'une partie est compromise, le reste ne sera pas affecté.

Cependant, bien que les processus isolés dans les conteneurs promettent une sécurité améliorée, tous les conteneurs partagent l'accès à un seul système d'exploitation hôte. Vous risquez d'exécuter des conteneurs Docker avec un isolement incomplet. Tout code malveillant peut accéder à la mémoire de votre ordinateur.

Il existe une pratique populaire consistant à exécuter de nombreux conteneurs dans un seul environnement. C'est ainsi que vous rendez votre application prédisposée aux attaques de type Abus de Ressources, sauf si vous limitez les capacités des ressources du conteneur. Pour une efficacité et un isolement maximum, chaque conteneur doit traiter une zone spécifique de préoccupation.

Un autre problème est la configuration par défaut de Docker – les utilisateurs ne sont pas espacés par noms. Les espaces de noms permettent aux ressources logicielles d'utiliser d'autres ressources uniquement si elles appartiennent à un espace de noms spécifique.

L'exécution d'applications avec Docker implique l'exécution du démon Docker avec des privilèges root. Tout processus qui sort du conteneur Docker aura les mêmes privilèges sur l'hôte que dans le conteneur. L'exécution de vos processus à l'intérieur des conteneurs en tant qu'utilisateur non privilégié ne peut pas garantir la sécurité. Cela dépend des capacités que vous ajoutez ou supprimez. Pour atténuer les risques de sortie de conteneur Docker, vous ne devez pas télécharger des conteneurs prêts à l'emploi à partir de sources non fiables.

## **Ne pas utiliser Docker si vous développez une application GUI de bureau**

Docker ne convient pas aux applications nécessitant une interface utilisateur riche. Docker est principalement destiné aux conteneurs isolés avec des applications basées sur la console. Les applications basées sur une interface graphique ne sont pas une priorité, leur support dépendra du cas spécifique et de l'application. Les conteneurs Windows sont basés soit sur Nano soit sur Core Server – cela ne permet pas aux utilisateurs de démarrer une interface basée sur une interface graphique ou un serveur RDP Docker dans le conteneur Docker.

Pourtant, vous pouvez toujours [<ins>exécuter des applications basées sur une interface graphique</ins>](https://hub.docker.com/r/tzutalin/py2qt4/) développées avec Python et le framework QT dans un conteneur Linux. Vous pouvez également utiliser le transfert X11, mais cette solution est quelque peu maladroite.

## **Ne pas utiliser Docker si vous souhaitez simplifier le développement et le débogage**

Docker a été créé par des développeurs et pour des développeurs. Il offre une stabilité de l'environnement : un conteneur sur la machine de développement fonctionnera exactement de la même manière sur les environnements de staging, de production ou tout autre environnement. Cela élimine le problème des différentes versions de programmes dans différents environnements.

Avec l'aide de Docker, vous pouvez facilement ajouter une nouvelle dépendance à votre application. Aucun développeur de votre équipe n'aura besoin de répéter cette manipulation sur sa machine. Tout sera opérationnel dans le conteneur et distribué à toute l'équipe.

En même temps, vous devez faire une configuration supplémentaire pour coder votre application dans Docker. De plus, avec le débogage Docker, vous devez configurer la sortie des logs et définir les ports de débogage. Vous devrez peut-être également mapper les ports pour vos applications et services dans les conteneurs. Donc, si vous avez un processus de déploiement compliqué et fastidieux, Docker vous aidera beaucoup. Si vous avez une application simple, cela ajoute simplement une complexité inutile.

## **Ne pas utiliser Docker si vous devez utiliser différents systèmes d'exploitation ou noyaux**

Avec les machines virtuelles, l'hyperviseur peut abstraire un appareil entier. Vous pouvez utiliser Microsoft Azure pour exécuter à la fois des instances de Windows Server et de Linux Server en même temps. Cependant, une image Docker nécessite le même système d'exploitation pour lequel elle a été créée.

Il existe une grande base de données d'images de conteneurs Docker – Docker Hub. Pourtant, si une image a été créée sur Linux Ubuntu, elle ne fonctionnera que sur le même Ubuntu exact.

Si une application est développée sur Windows, mais que la production s'exécute sur Linux, vous ne pourrez pas utiliser Docker efficacement. Parfois, il est plus facile de configurer un serveur si vous avez plusieurs applications statiques.

## **Ne pas utiliser Docker si vous avez beaucoup de données précieuses à stocker**

Par conception, tous les fichiers Docker sont créés à l'intérieur d'un conteneur et stockés sur une couche de conteneur inscriptible. Il peut être difficile de récupérer les données hors du conteneur si un autre processus en a besoin. De plus, la couche inscriptible d'un conteneur est connectée à la machine hôte sur laquelle le conteneur s'exécute. Si vous devez déplacer les données ailleurs, vous ne pouvez pas le faire facilement. De plus, toutes les données stockées à l'intérieur d'un conteneur seront perdues à jamais une fois le conteneur arrêté.

Vous devez penser à des moyens de sauvegarder vos données ailleurs d'abord. Pour garder les données en sécurité dans Docker, vous devez employer un outil supplémentaire – Docker Data Volumes. Pourtant, cette solution est encore assez maladroite et doit être améliorée.

## **Ne pas utiliser Docker si vous cherchez la technologie la plus facile à gérer**

Introduit en 2012, Docker est encore une technologie nouvelle. En tant que développeur, vous devrez peut-être mettre à jour les versions de Docker régulièrement. Malheureusement, la compatibilité ascendante n'est pas garantie. De plus, la documentation prend du retard par rapport à l'avancement de la technologie. En tant que développeur, vous devrez découvrir certaines choses par vous-même.

De plus, les options de surveillance que Docker offre sont assez pauvres. Vous pouvez obtenir un aperçu rapide de certaines statistiques simples. Pourtant, si vous souhaitez voir certaines fonctionnalités de surveillance avancées, Docker n'a rien à offrir.

De plus, dans le cas d'une application grande et complexe, l'implémentation de Docker a un coût. La construction et la maintenance de la communication entre de nombreux conteneurs sur de nombreux serveurs prendront beaucoup de temps et d'efforts. Pourtant, il existe un outil utile qui facilite le travail avec les applications Docker multi-conteneurs – Docker Compose. Docker Compose définit les services, les réseaux et les volumes dans un seul fichier YAML.

Néanmoins, l'écosystème Docker est assez fracturé – tous les produits de conteneurs de support ne fonctionnent pas bien ensemble. Chaque produit est soutenu par une certaine entreprise ou communauté. La concurrence acharnée entre ceux-ci entraîne une incompatibilité des produits.

## **Pour conclure**

Les professionnels de KeenEthics aiment travailler avec Docker et l'utilisent souvent pour le développement d'applications. Malgré quelques inconvénients, vous pouvez facilement l'utiliser pour exécuter et gérer des applications côte à côte dans des conteneurs isolés.

L'installation d'une application peut être aussi simple que l'exécution d'une seule commande – <docker run>. Docker fournit également un environnement d'isolement propre et original pour chaque test, ce qui en fait un outil important et utile pour les tests d'automatisation.

Les fonctionnalités de Docker offrent des avantages en termes de gestion des dépendances et de sécurité. Augmenté d'outils utiles tels que Docker Hub, Docker Swarm et Docker Compose, Docker est une solution populaire et conviviale.

Malgré tous les avantages de Docker, vous ne devriez pas l'utiliser pour conteneuriser chaque application que vous développez.

_Rappel : Docker est révolutionnaire. Mais ce n'est pas une solution universelle._

Docker n'est pas le seul outil de ce type sur le marché non plus. Les alternatives à Docker sont [<ins>rkt</ins>](https://coreos.com/rkt/), prononcé "rocket", [<ins>Linux Containers</ins>](https://linuxcontainers.org/), ou [<ins>OpenVZ</ins>](https://openvz.org/). Chacun de ceux-ci, avec ses avantages et ses inconvénients, est assez similaire à Docker. La popularité croissante et les taux d'utilisation de Docker sont causés uniquement par la décision des entreprises de l'adopter.

Avant de sauter aux conclusions quant à savoir si vous devez utiliser Docker ou non, recherchez les exigences du projet. Parlez à vos coéquipiers ou pairs et laissez-les vous aider à décider quand utiliser Docker, quand ne pas utiliser de conteneurs, et s'il s'agit de l'un de ces cas d'utilisation de Docker.

Que vous l'aimiez ou non, cette technologie a un avenir. Il y a des développeurs et des agences de développement qui détestent Docker et essaient de l'éliminer de tous leurs projets en cours. En même temps, il y a des spécialistes qui conteneurisent tout ce qu'ils peuvent parce qu'ils voient Docker comme une panacée. Peut-être ne devriez-vous rejoindre aucun des deux camps. Restez impartial, restez objectif et prenez une décision en fonction d'une situation particulière.

## Avez-vous une idée pour un projet Docker ?

Mon entreprise KeenEthics est une équipe de développeurs expérimentés en [applications web](https://keenethics.com/services-web-development). Si vous avez besoin d'une estimation gratuite d'un projet similaire, n'hésitez pas à [nous contacter](https://keenethics.com/contacts?activeForm=estimate).

Vous pouvez lire plus d'articles similaires sur mon Keen Blog. Permettez-moi de vous suggérer de lire [Pourquoi refactoriser votre code ?](https://keenethics.com/blog/1554572000000-refactoring) ou [Modèles de développement de logiciels expliqués : Externalisation vs Outstaffing, Prix fixe vs Temps et Matériel ?](https://keenethics.com/blog/outsourcing-vs-outstaffing)

## P.S.

De plus, je voudrais dire "merci" à [Alex Pletnov](https://www.linkedin.com/in/oleksiy-pletnov-212b3764/) pour la co-rédaction de cet article ainsi qu'aux lecteurs pour l'avoir lu jusqu'au bout !

L'article original publié sur le blog de KeenEthics peut être trouvé ici : [7 Cas où ne pas utiliser Docker](https://keenethics.com/blog/1517306255770-docker-5-cases-when-you-should-not-use-it).