---
title: Une introduction adaptée aux débutants sur les conteneurs, les machines virtuelles
  et Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-04T16:40:05.000Z'
originalURL: https://freecodecamp.org/news/a-beginner-friendly-introduction-to-containers-vms-and-docker-79a9e3e119b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*k8n7Jx9UaLRAxum9HMp8nQ.png
tags:
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: Linux
  slug: linux
- name: open source
  slug: open-source
- name: technology
  slug: technology
seo_title: Une introduction adaptée aux débutants sur les conteneurs, les machines
  virtuelles et Docker
seo_desc: 'By Preethi Kasireddy

  If you’re a programmer or techie, chances are you’ve at least heard of Docker: a
  helpful tool for packing, shipping, and running applications within “containers.”
  It’d be hard not to, with all the attention it’s getting these day...'
---

Par Preethi Kasireddy

Si vous êtes un programmeur ou un passionné de technologie, il est probable que vous ayez au moins entendu parler de Docker : un outil utile pour emballer, expédier et exécuter des applications dans des _"conteneurs"_. Il serait difficile de ne pas en avoir entendu parler, avec toute l'attention qu'il reçoit ces jours-ci — de la part des développeurs et des administrateurs système. Même les grands acteurs comme Google, VMware et Amazon construisent des services pour le supporter.

Quoi qu'il en soit, que vous ayez ou non un cas d'utilisation immédiat en tête pour Docker, je pense toujours qu'il est important de comprendre certains des concepts fondamentaux autour de ce qu'est un _"conteneur"_ et comment il se compare à une machine virtuelle (VM). Bien que l'Internet regorge d'excellents guides d'utilisation pour Docker, je n'ai pas pu trouver beaucoup de guides conceptuels adaptés aux débutants, en particulier sur ce qui compose un conteneur. Donc, espérons que cet article résoudra ce problème :)

Commençons par comprendre ce que sont les VM et les conteneurs.

### Qu'est-ce que les "conteneurs" et les "VM" ?

Les conteneurs et les VM sont similaires dans leurs objectifs : isoler une application et ses dépendances dans une unité autonome qui peut s'exécuter n'importe où.

De plus, les conteneurs et les VM éliminent le besoin de matériel physique, permettant une utilisation plus efficace des ressources informatiques, tant en termes de consommation d'énergie que de rentabilité.

La principale différence entre les conteneurs et les VM réside dans leur approche architecturale. Examinons cela de plus près.

### Machines Virtuelles

Une VM est essentiellement une émulation d'un ordinateur réel qui exécute des programmes comme un ordinateur réel. Les VM s'exécutent sur une machine physique en utilisant un _"hyperviseur"_. Un hyperviseur, à son tour, s'exécute soit sur une machine hôte, soit sur du _"bare-metal"_.

Décortiquons le jargon :

Un **hyperviseur** est un logiciel, un micrologiciel ou un matériel sur lequel les VM s'exécutent. Les hyperviseurs eux-mêmes s'exécutent sur des ordinateurs physiques, appelés _"machine hôte"_. La machine hôte fournit aux VM des ressources, y compris la RAM et le CPU. Ces ressources sont divisées entre les VM et peuvent être distribuées comme vous le souhaitez. Donc, si une VM exécute une application plus gourmande en ressources, vous pourriez allouer plus de ressources à celle-ci qu'aux autres VM s'exécutant sur la même machine hôte.

La VM qui s'exécute sur la machine hôte (à nouveau, en utilisant un hyperviseur) est également souvent appelée _"machine invitée"_. Cette machine invitée contient à la fois l'application et tout ce dont elle a besoin pour exécuter cette application (par exemple, les binaires système et les bibliothèques). Elle transporte également une pile matérielle virtualisée complète, y compris des adaptateurs réseau virtualisés, du stockage et un CPU — ce qui signifie qu'elle a également son propre système d'exploitation invité complet. De l'intérieur, la machine invitée se comporte comme sa propre unité avec ses propres ressources dédiées. De l'extérieur, nous savons qu'il s'agit d'une VM — partageant les ressources fournies par la machine hôte.

Comme mentionné ci-dessus, une machine invitée peut s'exécuter soit sur un **hyperviseur hébergé**, soit sur un **hyperviseur bare-metal**. Il existe quelques différences importantes entre eux.

Tout d'abord, un hyperviseur de virtualisation hébergé s'exécute sur le système d'exploitation de la machine hôte. Par exemple, un ordinateur exécutant OSX peut avoir une VM (par exemple, VirtualBox ou VMware Workstation 8) installée sur ce système d'exploitation. La VM n'a pas d'accès direct au matériel, elle doit donc passer par le système d'exploitation hôte (dans notre cas, le OSX du Mac).

L'avantage d'un hyperviseur hébergé est que le matériel sous-jacent est moins important. Le système d'exploitation de l'hôte est responsable des pilotes de matériel au lieu de l'hyperviseur lui-même, et est donc considéré comme ayant plus de "compatibilité matériel". D'un autre côté, cette couche supplémentaire entre le matériel et l'hyperviseur crée plus de surcharge de ressources, ce qui diminue les performances de la VM.

Un environnement d'hyperviseur bare-metal résout le problème de performance en s'installant et en s'exécutant à partir du matériel de la machine hôte. Parce qu'il interagit directement avec le matériel sous-jacent, il n'a pas besoin d'un système d'exploitation hôte pour s'exécuter. Dans ce cas, la première chose installée sur le serveur d'une machine hôte en tant que système d'exploitation sera l'hyperviseur. Contrairement à l'hyperviseur hébergé, un hyperviseur bare-metal a ses propres pilotes de périphériques et interagit directement avec chaque composant pour toute tâche d'E/S, de traitement ou spécifique au système d'exploitation. Cela se traduit par de meilleures performances, une meilleure évolutivité et une meilleure stabilité. Le compromis ici est que la compatibilité matériel est limitée car l'hyperviseur ne peut avoir qu'un nombre limité de pilotes de périphériques intégrés.

Après tout ce discours sur les hyperviseurs, vous vous demandez peut-être pourquoi nous avons besoin de cette couche supplémentaire d'_"hyperviseur"_ entre la VM et la machine hôte.

Eh bien, puisque la VM a son propre système d'exploitation virtuel, l'hyperviseur joue un rôle essentiel en fournissant aux VM une plateforme pour gérer et exécuter ce système d'exploitation invité. Il permet aux ordinateurs hôtes de partager leurs ressources entre les machines virtuelles qui s'exécutent en tant qu'invitées sur eux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RKPXdVaqHRzmQ5RPBH_d-g.png)
_Diagramme de Machine Virtuelle_

Comme vous pouvez le voir dans le diagramme, les VM empaquetent le matériel virtuel, un noyau (c'est-à-dire le système d'exploitation) et l'espace utilisateur pour chaque nouvelle VM.

### Conteneur

Contrairement à une VM qui fournit une virtualisation matérielle, un conteneur fournit une virtualisation au niveau du système d'exploitation en abstraisant l'"espace utilisateur". Vous verrez ce que je veux dire lorsque nous décortiquerons le terme _conteneur_.

Pour toutes les intentions et tous les usages, les conteneurs ressemblent à une VM. Par exemple, ils ont un espace privé pour le traitement, peuvent exécuter des commandes en tant que root, ont une interface réseau privée et une adresse IP, permettent des routes personnalisées et des règles iptable, peuvent monter des systèmes de fichiers, etc.

La grande différence entre les conteneurs et les VM est que les conteneurs *partagent* le noyau du système hôte avec d'autres conteneurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*V5N9gJdnToIrgAgVJTtl_w.png)
_Diagramme de Conteneur_

Ce diagramme vous montre que les conteneurs empaquetent uniquement l'espace utilisateur, et non le noyau ou le matériel virtuel comme le fait une VM. Chaque conteneur obtient son propre espace utilisateur isolé pour permettre à plusieurs conteneurs de s'exécuter sur une seule machine hôte. Nous pouvons voir que toute l'architecture de niveau système d'exploitation est partagée entre les conteneurs. Les seules parties qui sont créées à partir de zéro sont les binaires et les bibliothèques. C'est ce qui rend les conteneurs si légers.

### Où intervient Docker ?

Docker est un projet open-source basé sur les conteneurs Linux. Il utilise des fonctionnalités du noyau Linux comme les espaces de noms et les groupes de contrôle pour créer des conteneurs sur un système d'exploitation.

Les conteneurs ne datent pas d'hier ; Google utilise sa propre technologie de conteneurs depuis des années. D'autres technologies de conteneurs Linux incluent Solaris Zones, BSD jails et LXC, qui existent depuis de nombreuses années.

Alors, pourquoi Docker gagne-t-il soudainement en popularité ?

1. **Facilité d'utilisation :** Docker a grandement facilité pour quiconque — développeurs, administrateurs système, architectes et autres — de tirer parti des conteneurs afin de construire et tester rapidement des applications portables. Il permet à quiconque d'emballer une application sur son ordinateur portable, qui à son tour peut s'exécuter sans modification sur n'importe quel cloud public, cloud privé, ou même sur du bare-metal. La devise est : "construire une fois, exécuter n'importe où".

2. **Vitesse :** Les conteneurs Docker sont très légers et rapides. Puisque les conteneurs sont simplement des environnements en bac à sable s'exécutant sur le noyau, ils consomment moins de ressources. Vous pouvez créer et exécuter un conteneur Docker en quelques secondes, contrairement aux VM qui peuvent prendre plus de temps car elles doivent démarrer un système d'exploitation virtuel complet à chaque fois.

3. **Docker Hub :** Les utilisateurs de Docker bénéficient également de l'écosystème de plus en plus riche de Docker Hub, que vous pouvez considérer comme un "magasin d'applications pour les images Docker". Docker Hub dispose de dizaines de milliers d'images publiques créées par la communauté qui sont prêtes à être utilisées. Il est incroyablement facile de rechercher des images qui répondent à vos besoins, prêtes à être téléchargées et utilisées avec peu ou pas de modification.

4. **Modularité et évolutivité :** Docker facilite la division des fonctionnalités de votre application en conteneurs individuels. Par exemple, vous pourriez avoir votre base de données Postgres s'exécutant dans un conteneur et votre serveur Redis dans un autre, tandis que votre application Node.js est dans un autre. Avec Docker, il est devenu plus facile de lier ces conteneurs ensemble pour créer votre application, ce qui facilite la mise à l'échelle ou la mise à jour des composants indépendamment à l'avenir.

Enfin, qui n'aime pas la baleine Docker ? ;)

![Image](https://cdn-media-1.freecodecamp.org/images/1*sGHbxxLdm87_n7tKQS3EUg.png)
_Source : [https://www.docker.com/docker-birthday](https://www.docker.com/docker-birthday" rel="noopener" target="_blank" title=")_

### Concepts Fondamentaux de Docker

Maintenant que nous avons une vue d'ensemble, passons en revue les parties fondamentales de Docker pièce par pièce :

![Image](https://cdn-media-1.freecodecamp.org/images/1*K7p9dzD9zHuKEMgAcbSLPQ.png)

#### Moteur Docker

Le moteur Docker est la couche sur laquelle Docker s'exécute. C'est un runtime léger et des outils qui gèrent les conteneurs, les images, les builds, et plus encore. Il s'exécute nativement sur les systèmes Linux et est composé de :

1. Un démon Docker qui s'exécute sur l'ordinateur hôte.  
2. Un client Docker qui communique ensuite avec le démon Docker pour exécuter des commandes.  
3. Une API REST pour interagir avec le démon Docker à distance.

#### Client Docker

Le client Docker est ce avec quoi vous, en tant qu'utilisateur final de Docker, communiquez. Considérez-le comme l'interface utilisateur de Docker. Par exemple, lorsque vous faites...

```bash
docker build -t mon-image .
```

vous communiquez avec le client Docker, qui transmet ensuite vos instructions au démon Docker.

#### Démon Docker

Le démon Docker est ce qui exécute réellement les commandes envoyées au client Docker — comme la construction, l'exécution et la distribution de vos conteneurs. Le démon Docker s'exécute sur la machine hôte, mais en tant qu'utilisateur, vous ne communiquez jamais directement avec le démon. Le client Docker peut également s'exécuter sur la machine hôte, mais ce n'est pas obligatoire. Il peut s'exécuter sur une machine différente et communiquer avec le démon Docker qui s'exécute sur la machine hôte.

#### Dockerfile

Un Dockerfile est l'endroit où vous écrivez les instructions pour construire une image Docker. Ces instructions peuvent être :

* **RUN apt-get install some-package** : pour installer un paquet logiciel
* **EXPOSE 8000** : pour exposer un port
* **ENV ANT_HOME /usr/local/apache-ant** : pour passer une variable d'environnement

et ainsi de suite. Une fois que vous avez configuré votre Dockerfile, vous pouvez utiliser la commande **docker build** pour construire une image à partir de celui-ci. Voici un exemple de Dockerfile :

```dockerfile
# Exemple de Dockerfile
FROM ubuntu:18.04

# Installer les dépendances
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . .

# Installer les dépendances Python
RUN pip3 install -r requirements.txt

# Exposer le port
EXPOSE 8000

# Commande pour exécuter l'application
CMD ["python3", "app.py"]
```

#### Image Docker

Les images sont des modèles en lecture seule que vous construisez à partir d'un ensemble d'instructions écrites dans votre Dockerfile. Les images définissent à la fois ce que vous voulez que votre application emballée et ses dépendances soient, *et* quels processus exécuter lorsqu'elle est lancée.

L'image Docker est construite en utilisant un Dockerfile. Chaque instruction dans le Dockerfile ajoute une nouvelle "couche" à l'image, les couches représentant une portion du système de fichiers de l'image qui ajoute ou remplace la couche en dessous. Les couches sont essentielles à la structure légère mais puissante de Docker. Docker utilise un système de fichiers Union pour y parvenir :

#### Systèmes de Fichiers Union

Docker utilise les systèmes de fichiers Union pour construire une image. Vous pouvez penser à un système de fichiers Union comme un système de fichiers empilable, ce qui signifie que les fichiers et répertoires de systèmes de fichiers séparés (connus sous le nom de branches) peuvent être superposés de manière transparente pour former un seul système de fichiers.

Le contenu des répertoires qui ont le même chemin dans les branches superposées est vu comme un seul répertoire fusionné, ce qui évite la nécessité de créer des copies séparées de chaque couche. Au lieu de cela, ils peuvent tous être donnés des pointeurs vers la même ressource ; lorsque certaines couches doivent être modifiées, cela créera une copie et modifiera une copie locale, laissant l'original inchangé. C'est ainsi que les systèmes de fichiers peuvent *sembler* modifiables sans permettre réellement les écritures. (En d'autres termes, un système "copie-sur-écriture").

Les systèmes en couches offrent deux avantages principaux :

1. **Sans duplication :** les couches aident à éviter de dupliquer un ensemble complet de fichiers chaque fois que vous utilisez une image pour créer et exécuter un nouveau conteneur, rendant l'instantiation des conteneurs Docker très rapide et économique.  
2. **Ségrégation des couches :** Apporter une modification est beaucoup plus rapide — lorsque vous modifiez une image, Docker ne propage les mises à jour qu'à la couche qui a été modifiée.

#### Volumes

Les volumes sont la partie "données" d'un conteneur, initialisés lors de la création d'un conteneur. Les volumes vous permettent de persister et de partager les données d'un conteneur. Les volumes de données sont séparés du système de fichiers Union par défaut et existent sous forme de répertoires et de fichiers normaux sur le système de fichiers hôte. Ainsi, même si vous détruisez, mettez à jour ou reconstruisez votre conteneur, les volumes de données resteront intacts. Lorsque vous souhaitez mettre à jour un volume, vous apportez des modifications directement à celui-ci. (En bonus, les volumes de données peuvent être partagés et réutilisés parmi plusieurs conteneurs, ce qui est plutôt pratique.)

#### Conteneurs Docker

Un conteneur Docker, comme discuté ci-dessus, enveloppe le logiciel d'une application dans une boîte invisible avec tout ce dont l'application a besoin pour s'exécuter. Cela inclut le système d'exploitation, le code de l'application, le runtime, les outils système, les bibliothèques système, etc. Les conteneurs Docker sont construits à partir d'images Docker. Puisque les images sont en lecture seule, Docker ajoute un système de fichiers en lecture-écriture sur le système de fichiers en lecture seule de l'image pour créer un conteneur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hZgRPWerZVbaGT8jJiJZVQ.png)
_Source : Docker_

De plus, lors de la création du conteneur, Docker crée une interface réseau afin que le conteneur puisse communiquer avec l'hôte local, attache une adresse IP disponible au conteneur et exécute le processus que vous avez spécifié pour exécuter votre application lors de la définition de l'image.

Une fois que vous avez créé avec succès un conteneur, vous pouvez ensuite l'exécuter dans n'importe quel environnement sans avoir à apporter de modifications.

### Approfondissement des "conteneurs"

Ouf ! C'est beaucoup de pièces mobiles. Une chose qui m'a toujours rendu curieux était de savoir comment un conteneur est réellement implémenté, surtout puisque il n'y a pas de frontière d'infrastructure abstraite autour d'un conteneur. Après beaucoup de lectures, tout cela a du sens, alors voici ma tentative de vous l'expliquer ! :)

Le terme "conteneur" est vraiment juste un concept abstrait pour décrire comment quelques fonctionnalités différentes fonctionnent ensemble pour visualiser un "conteneur". Passons-les en revue rapidement :

#### 1) Espaces de noms

Les espaces de noms fournissent aux conteneurs leur propre vue du système Linux sous-jacent, limitant ce que le conteneur peut voir et accéder. Lorsque vous exécutez un conteneur, Docker crée des espaces de noms que le conteneur spécifique utilisera.

Il existe plusieurs types différents d'espaces de noms dans un noyau que Docker utilise, par exemple :

a. **NET :** Fournit à un conteneur sa propre vue de la pile réseau du système (par exemple, ses propres périphériques réseau, adresses IP, tables de routage IP, répertoire /proc/net, numéros de port, etc.).  
b. **PID :** PID signifie Identifiant de Processus. Si vous avez déjà exécuté **ps aux** dans la ligne de commande pour vérifier quels processus s'exécutent sur votre système, vous aurez vu une colonne nommée "PID". L'espace de noms PID donne aux conteneurs leur propre vue des processus qu'ils peuvent voir et avec lesquels ils peuvent interagir, y compris un init indépendant (PID 1), qui est "l'ancêtre de tous les processus".  
c. **MNT :** Donne à un conteneur sa propre vue des ["montages" sur le système](http://www.linfo.org/mounting.html). Ainsi, les processus dans différents espaces de noms de montage ont différentes vues de la hiérarchie du système de fichiers.  
d. **UTS :** UTS signifie UNIX Timesharing System. Il permet à un processus d'identifier les identifiants système (c'est-à-dire le nom d'hôte, le nom de domaine, etc.). UTS permet aux conteneurs d'avoir leur propre nom d'hôte et nom de domaine NIS qui est indépendant des autres conteneurs et du système hôte.  
e. **IPC :** IPC signifie InterProcess Communication. L'espace de noms IPC est responsable de l'isolement des ressources IPC entre les processus s'exécutant à l'intérieur de chaque conteneur.  
f. **USER :** Cet espace de noms est utilisé pour isoler les utilisateurs à l'intérieur de chaque conteneur. Il fonctionne en permettant aux conteneurs d'avoir une vue différente des plages d'uid (identifiant d'utilisateur) et de gid (identifiant de groupe), par rapport au système hôte. Par conséquent, l'uid et le gid d'un processus peuvent être différents à l'intérieur et à l'extérieur d'un espace de noms utilisateur, ce qui permet également à un processus d'avoir un utilisateur non privilégié à l'extérieur d'un conteneur sans sacrifier le privilège root à l'intérieur d'un conteneur.

Docker utilise ces espaces de noms ensemble afin d'isoler et de commencer la création d'un conteneur. La fonctionnalité suivante est appelée groupes de contrôle.

#### 2) **Groupes de contrôle**

Les groupes de contrôle (également appelés cgroups) est une fonctionnalité du noyau Linux qui isole, priorise et comptabilise l'utilisation des ressources (CPU, mémoire, E/S disque, réseau, etc.) d'un ensemble de processus. En ce sens, un cgroup garantit que les conteneurs Docker n'utilisent que les ressources dont ils ont besoin — et, si nécessaire, établit des limites aux ressources qu'un conteneur *peut* utiliser. Les cgroups garantissent également qu'un seul conteneur n'épuise pas l'une de ces ressources et ne fait pas tomber l'ensemble du système.

Enfin, les systèmes de fichiers union sont une autre fonctionnalité utilisée par Docker :

#### 3) **Système de fichiers Union isolé :**

Décrit ci-dessus dans la section Images Docker :)

C'est vraiment tout ce qu'il y a dans un conteneur Docker (bien sûr, le diable est dans les détails d'implémentation — comme la gestion des interactions entre les différents composants).

### L'avenir de Docker : Docker et les VM coexisteront

Bien que Docker gagne certainement en popularité, je ne pense pas qu'il deviendra une réelle menace pour les VM. Les conteneurs continueront à gagner du terrain, mais il existe de nombreux cas d'utilisation où les VM sont toujours mieux adaptées.

Par exemple, si vous devez exécuter plusieurs applications sur plusieurs serveurs, il est probablement judicieux d'utiliser des VM. D'un autre côté, si vous devez exécuter de nombreuses *copies* d'une seule application, Docker offre certains avantages convaincants.

De plus, bien que les conteneurs vous permettent de diviser votre application en parties discrètes plus fonctionnelles pour créer une séparation des préoccupations, cela signifie également qu'il y a un nombre croissant de parties à gérer, ce qui peut devenir ingérable.

La sécurité a également été une préoccupation avec les conteneurs Docker — puisque les conteneurs partagent le même noyau, la barrière entre les conteneurs est plus fine. Alors qu'une VM complète ne peut émettre que des hyperappels vers l'hyperviseur hôte, un conteneur Docker peut effectuer des appels système vers le noyau hôte, ce qui crée une surface d'attaque plus grande. Lorsque la sécurité est particulièrement importante, les développeurs sont susceptibles de choisir les VM, qui sont isolées par du matériel abstrait — ce qui rend beaucoup plus difficile l'interférence entre elles.

Bien sûr, des problèmes comme la sécurité et la gestion sont certains d'évoluer à mesure que les conteneurs obtiennent plus d'exposition en production et un examen plus approfondi de la part des utilisateurs. Pour l'instant, le débat sur les conteneurs par rapport aux VM est vraiment mieux laissé aux experts dev ops qui vivent et respirent avec eux tous les jours !

### Conclusion

J'espère que vous êtes maintenant équipé des connaissances nécessaires pour en apprendre davantage sur Docker et peut-être même l'utiliser dans un projet un jour.

Comme toujours, laissez-moi un mot dans les commentaires si j'ai fait des erreurs ou si je peux être utile de quelque manière que ce soit ! :)