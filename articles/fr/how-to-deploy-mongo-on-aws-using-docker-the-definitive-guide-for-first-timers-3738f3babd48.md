---
title: 'Comment déployer Mongo sur AWS en utilisant Docker : le guide définitif pour
  les débutants'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T20:01:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-mongo-on-aws-using-docker-the-definitive-guide-for-first-timers-3738f3babd48
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/banner_1200_complete.png
tags:
- name: AWS
  slug: aws
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: mongo
  slug: mongo
- name: 'tech '
  slug: tech
seo_title: 'Comment déployer Mongo sur AWS en utilisant Docker : le guide définitif
  pour les débutants'
seo_desc: 'By Eric Burel

  Why you need this?

  Because JS + Python + Mongo = full data development

  I am a Meteor developer. More precisely I use Vulcan.js, but that’s a whole other
  story. Meteor is a full-fledged Node.js framework, pretty nice for SaaS, real-time
  ...'
---

Par Eric Burel

### Pourquoi en avez-vous besoin ?

#### Parce que JS + Python + Mongo = développement de données complet

Je suis un développeur Meteor. Plus précisément, j'utilise Vulcan.js, [mais c'est une toute autre histoire](https://medium.com/dailyjs/write-less-code-ship-more-apps-how-vulcan-js-makes-me-an-efficient-developer-71c829c76417). Meteor est un framework Node.js complet, assez bien pour les SaaS, les applications en temps réel, le prototypage, les logiciels de gestion et beaucoup d'autres cas d'utilisation.

Par défaut, il fonctionne avec MongoDB. MongoDB est un système de gestion de base de données NoSQL (SGBD). Il stocke les documents en JSON et son shell utilise JavaScript, ce qui explique pourquoi il est si apprécié par les développeurs Node.js.

Il existe un outil pratique appelé [Meteor Up](http://meteor-up.com/) pour déployer automatiquement les applications Meteor et les bases de données Mongo associées sur des serveurs de production. Pratique est en fait un euphémisme, c'est carrément génial.

Et je suis aussi un développeur Python. Python est excellent pour le web scraping et la science des données. Il est à la fois facile à utiliser et adapté pour les hautes performances.

Parfois, j'aime utiliser à la fois Python pour extraire et traiter les données et Meteor pour créer l'interface utilisateur. J'appelle cela le **"développement de données complet"**, car il va de la source de données brute à l'interface utilisateur finale.

![Image](https://cdn-media-1.freecodecamp.org/images/FTRA0udkWF2CTm79qN6y82lab05vx3Sy-f9S)
_Le trio sacré du développeur de données complet : Meteor, Mongo, Python_

**Mais il y a un problème :** Meteor Up n'expose actuellement pas la base de données Mongo, seule l'application Meteor locale peut s'y connecter. Je ne peux donc pas connecter mes serveurs Python à mes bases de données gérées par Meteor directement :(

Un service payant ferait le travail en fournissant une URL pour la base de données hébergée, comme celle-ci :

```
mongo://username:password@somedomain.com:27017 
```

Mais pourquoi dépenser de l'argent quand vous pouvez passer des heures à configurer votre propre base de données Mongo sur AWS en utilisant Docker, et apprendre des tonnes d'astuces utiles en cours de route ? **C'est encore mieux si quelqu'un, disons moi, le fait d'abord et écrit un long tutoriel pour vous faciliter les choses !**

_Note importante :_ il est parfaitement normal si ce long tutoriel vous prend plusieurs sessions pour le terminer. Ne lâchez pas ! Le résultat vaut bien l'effort, car maîtriser Docker et AWS sont deux compétences très appréciées par les employeurs, et très utiles dans la vie réelle. Postez vos questions en commentaires si vous en avez, je ferai de mon mieux pour répondre à toutes.

![Image](https://cdn-media-1.freecodecamp.org/images/g0v26UG99TkEksA8pBDgkjcEzSH9LnLxWe9a)

### 1 — Découvrons Docker

#### Notre premier conteneur

Je vous invite à lire [la documentation officielle d'installation de Docker ici](https://docs.docker.com/get-started/) et à l'installer, ce qui ne prend que quelques minutes. Ensuite, jouons un peu. Exécutez les commandes suivantes dans votre terminal et observez les résultats :

```
docker run --name my-lame-db -d mongo
docker ps
```

![Image](https://cdn-media-1.freecodecamp.org/images/xCHkKOqT4f-VdvcBzbllxKAdAvqgcO-1uIDr)

Aussi simple que cela, nous venons de créer un conteneur isolé qui exécute Mongo !

Vous pouvez accéder aux fichiers Docker officiels de Mongo quelque part [dans ce dossier hébergé sur GitHub](https://github.com/docker-library/mongo) pour mieux comprendre ce qui se passe ici. Selon les dernières lignes du [Dockerfile](https://github.com/docker-library/mongo/blob/master/4.1/Dockerfile), notre base de données est disponible sur le port "27017" par défaut :

```
EXPOSE 27017 CMD ["mongod"] 
```

Mais Mongo s'expose sur ce port À L'INTÉRIEUR du conteneur. Mais le conteneur est isolé, donc seuls les programmes À L'INTÉRIEUR du conteneur peuvent parler à Mongo. Notre base de données est opérationnelle mais piégée seule dans son conteneur :/

**C'est nul ! Libérons-la !**

#### Ouvrir le conteneur, mapper les ports

Si vous voulez accéder à Mongo depuis L'EXTÉRIEUR du conteneur, vous devrez mapper le port exposé et un port de la machine. L'option `-p` est spécifiquement destinée à cela :

```
docker run -p 27017:27017 --name my-local-db -d mongo 
```

Si vous aviez un serveur Node, vous écriviez `docker run -p 80:3000 my-node-app` par exemple. Votre serveur fonctionnant sur le port 3000 serait ainsi disponible via HTTP (port 80). D'abord le port du conteneur, puis le port de l'image.

Essayons d'accéder à notre base de données dans le navigateur, juste pour le plaisir :

![Image](https://cdn-media-1.freecodecamp.org/images/xfsKKgSd0F9AGSpXXwrciUTUH2rLwsPrWnPj)
_Bien ! Notre base de données est en cours d'exécution ! Vous pouvez essayer les commandes `docker stop my-awesome-db` et `docker start my-awesome-db`. Vous verrez cette adresse devenir non disponible puis disponible à nouveau._

Comme prévu, vous ne pouvez pas vous connecter à votre base de données via le navigateur. Mais ce message de rejet provient de Mongo, ce qui est un bon signe. Essayons à nouveau en utilisant l'outil CLI officiel :

```
mongo localhost:27017 #ou simplement "mongo", car c'est l'uri par défaut
```

**Vous pouvez accéder à votre shell de base de données, nous progressons !**

Mais... je veux que ma base de données soit sur un serveur distant, pas en cours d'exécution localement sur ma machine isolée.

![Image](https://cdn-media-1.freecodecamp.org/images/7FeX2tR6yc47JAmWRjm6LFt4Y94Mf3iwUE7J)

### 2 — Accéder à AWS depuis votre terminal

Nous avons choisi AWS comme fournisseur de cloud car il est largement répandu, mais gardez à l'esprit que ce n'est qu'un exemple. AWS offre aux nouveaux utilisateurs un hébergement gratuit pendant 12 mois pour une instance de serveur, donc vous n'avez pas besoin de payer pour suivre ce tutoriel. Les étapes sont principalement similaires si vous choisissez un autre service d'hébergement.

La première étape consiste à créer un accès programmatique à Amazon Web Services en utilisant le service IAM (Identity and Access Management). Cette clé sera utilisée par Docker Machine (voir ci-dessous) pour effectuer certaines opérations, comme créer une instance AWS EC2 pour vous.

La configuration de cela dépasse le cadre de notre tutoriel. Par conséquent, je vous invite à lire [la première partie de cet article de Vishal Kumar](https://blog.codeship.com/running-mean-web-application-docker-containers-aws/). Suivez les 8 premières étapes jusqu'à ce que vous obteniez les identifiants AWS. Le reste de l'article est également intéressant mais un peu avancé à ce stade et ciblé sur la stack MEAN. Concentrons-nous uniquement sur Mongo pour le moment.

**À ce stade, vous devriez avoir vos identifiants.**

```
[default] 
aws_access_key_id = [clé d'accès du fichier d'identifiants téléchargé] 
aws_secret_access_key = [clé d'accès secrète du fichier d'identifiants téléchargé]
```

**Gardez-les en sécurité !** Vous devrez recréer une paire de clés si vous les perdez... et vous ne voulez certainement PAS que quelqu'un les découvre non plus !

![Image](https://cdn-media-1.freecodecamp.org/images/HK4A0Xh2ZoWhu74aTjMdBPjNyPOu9w5J5TXN)

### 3 — Mettre Docker dans le cloud avec Docker Machine

#### Plus besoin de la console AWS

Docker Machine est un utilitaire pour gérer les différentes machines hébergeant vos conteneurs (machines locales, serveurs cloud). D'où le nom, Docker... Machine. Vous pouvez le configurer pour plusieurs fournisseurs de cloud et il fonctionne très bien avec AWS.

[La documentation officielle](https://docs.docker.com/machine/drivers/aws/) donne toutes les informations dont vous avez besoin pour AWS. J'ai simplement sauté la partie VPC, c'est un peu trop avancé pour le moment, mais le reste est très utile.

#### Créer l'instance EC2

Vous finirez par écrire une commande similaire à celle ci-dessous.

```
docker-machine create \
--driver amazonec2 \
--amazonec2-access-key ***** --amazonec2-secret-key **** \
--amazonec2-region ***** \
--amazonec2-open-port 27017 my-awesome-server
```

Décomposons cela.

* J'utilise le pilote EC2, puisque je suis un utilisateur AWS.
* Je passe les identifiants en ligne car j'ai plusieurs comptes à gérer
* Je passe la région où j'héberge habituellement mes applications ("eu-west-3" pour moi),
* N'oubliez pas d'ouvrir le port 27017 (`--amazonec2-open-port 27017`), sinon AWS bloquera les connexions même si votre conteneur est correctement configuré.

Si vous n'avez pas spécifié la région correctement, vous pourriez avoir du mal à trouver votre instance sur la console AWS. Je ne comprends toujours pas pourquoi vous ne pouvez pas avoir toutes les zones affichées facilement dans cette interface, mais c'est ainsi que cela fonctionne.

Vous devriez également pouvoir vous débarrasser de la clé d'accès et de la clé secrète d'une manière ou d'une autre en définissant les identifiants AWS de votre machine locale, ou en les stockant comme variables d'environnement. Je préfère personnellement les avoir dans la ligne de commande car je peux les remplacer par des variables d'environnement.

![Image](https://cdn-media-1.freecodecamp.org/images/mZheBUCZ7JyCgxueh060ejYwNKpetat87YQA)

**À ce stade, vous pouvez vérifier la console AWS et voir votre instance configurée comme prévu !**

![Image](https://cdn-media-1.freecodecamp.org/images/sKiD1G-AvQe43Ch54y1FXOqT2opVHCGh3wJh)

### 4 — Exécuter un conteneur Mongo sur votre instance

#### Activer la machine correcte

Maintenant, la partie délicate, il m'a fallu un certain temps pour la comprendre. Le rôle de Docker Machine est de gérer vos machines distantes, de lancer des instances et d'installer Docker dessus. C'est tout. Ce n'est PAS Docker.

Vous devez donc toujours utiliser Docker. **Mais comment Docker sait-il à quelle machine se connecter ?**

Essayez ceci et observez le résultat :

```
docker-machine env my-awesome-server 
```

Il affichera un petit script shell pour configurer les variables d'environnement.

![Image](https://cdn-media-1.freecodecamp.org/images/YjV8Su28WDjQfeUJOwvqBUj7j-bURkNq5eYb)

Il vous indique également d'exécuter cette commande :

```
eval $(docker-machine env my-awesome-server)
```

Cela exécutera simplement le script affiché dans votre shell. Lorsque ces variables d'environnement sont définies, votre machine devient "active".

Tapez `docker-machine active` pour vérifier que la machine correcte est listée.

![Image](https://cdn-media-1.freecodecamp.org/images/3ySinraesoaVe-SxlGzHhCjfuueAdzkvRCqv)
_\o/_

Maintenant, tapez `docker info`, vous devriez voir que le `Name` correspond à votre application. **Magique !** Docker est "connecté" à la machine active, configurée par Docker Machine.

Nous pouvons maintenant exécuter la même commande que précédemment :

```
docker run -p 27017:27017 --name my-awesome-db -d mongo .
```

Il créera la base de données non pas sur notre machine locale, mais sur le serveur distant. Aussi simple que cela !

Exécutez cette commande pour obtenir l'IP de votre machine :

```
docker-machine ip my-awesome-server
```

Et ouvrez l'adresse `http://<ip-donnée-par-docker-machine>`:27017 : vous devriez obtenir un beau message d'erreur, vous indiquant que vous essayez d'accéder à MongoDB via HTTPS : ça marche !!!

Exécutez `mongo <ip-donnée-par-docker-machine>`:27017 ... **et... vous êtes connecté ! Félicitations, vous venez de configurer votre conteneur Docker sur un serveur de production.**

D'accord, maintenant, nous ne voulons définitivement PAS que le monde entier accède à notre base de données, donc la prochaine étape est de configurer l'authentification.

![Image](https://cdn-media-1.freecodecamp.org/images/vSa6Azoo6UzMD5zXyH-OuwJLxU0w3Dr0sXKW)

### 5 — Configurer l'authentification — solution à 2 conteneurs

Désolé, mais vous pouvez déjà supprimer le conteneur que vous venez de créer (exercice : je vous laisse trouver les commandes d'arrêt et de suppression du conteneur). Ce n'était qu'un exemple. Malheureusement, vous ne pourrez pas configurer l'authentification avec celui-ci.

Restez concentré car le processus est un peu plus compliqué que vous ne le pensez :

* Nous allons créer un premier conteneur, appelons-le "Conteneur #1", SANS authentification.
* Nous allons configurer ce conteneur de sorte que les données soient sauvegardées sur le disque du serveur, créer un administrateur, et supprimer le conteneur.
* Nous allons créer un deuxième conteneur, "Conteneur #2" AVEC authentification. Les identifiants de l'utilisateur administrateur seront toujours valides, car ils sont sauvegardés sur le disque.

Il pourrait y avoir des solutions plus simples dont je ne suis pas encore conscient, par exemple en fournissant les identifiants de l'utilisateur administrateur lors de la création du conteneur, alors n'hésitez pas à commenter si vous êtes un super-héros Docker/Mongo ! Et une solution à un conteneur est également fournie dans les annexes à la fin de l'article.

#### Partager les données entre les conteneurs

À ce stade, vous devriez penser "bien, les conteneurs sont isolés, alors comment le Conteneur #1 et le Conteneur #2 peuvent-ils partager le même utilisateur administrateur" ? Et vous avez raison. La solution réside dans le stockage des fichiers sur le serveur.

Vous souvenez-vous lorsque nous avons mappé les ports, de sorte que le port ouvert du conteneur mappe le port de Mongo ? Nous allons appliquer la même logique au système de fichiers : nous pouvons mapper des dossiers sur le conteneur et des dossiers sur le serveur.

Ajoutons une option à notre commande, et appelons-la la **Commande finale pour le Conteneur #1** :

```
docker run \
-d \
-p 27017:27017 \
--name my-awesome-db \
-v ~/dataMongo:/data/db mongo \
mongod
```

Intelligent ! **Maintenant, lorsque nos conteneurs Mongo liront/écriront leurs données dans `data/db`, elles seront également disponibles pour le serveur hôte**, dans le dossier `~/dataMongo` (dossier hôte d'abord, puis dossier conteneur).

#### Créer l'utilisateur administrateur

Tout est dans le titre : vous allez maintenant vous connecter à votre nouvelle instance Mongo et créer l'utilisateur administrateur.

```
docker-machine ip my-awesome-server
mongo <resulting-ip>
```

Maintenant, vous devriez être connecté à votre shell de base de données. Vous devez simplement créer un super utilisateur administrateur :

```
db.createUser(
  {
    user: "admin",
    pwd: "yourpassword",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ],
    passwordDigestor : "server"
  }
)
```

Vous pouvez consulter [la documentation officielle](https://docs.mongodb.com/manual/tutorial/enable-authentication/), [cet article](https://ianlondon.github.io/blog/mongodb-auth/) et [ce fil de discussion stack overflow](https://stackoverflow.com/questions/34559557/how-to-enable-authentication-on-mongodb-through-docker/46645243#comment93826825_46645243) pour plus d'informations.

De plus, [voir ce fil](https://stackoverflow.com/questions/23943651/mongodb-admin-user-not-authorized) sur la différence entre le rôle `root`, qui est un véritable super administrateur, et le rôle `userAdminAnyDatabase`, qui est une sorte de "créateur d'utilisateurs".

#### Supprimer le conteneur et activer l'authentification

Nous pouvons supprimer le Conteneur #1, son rôle était uniquement de nous permettre d'accéder à un shell Mongo sur notre serveur, mais il manquait d'authentification.

```
docker stop my-awesome-db
docker rm my-awesome-db
```

Nous pouvons ensuite créer notre conteneur final, avec l'authentification activée. Puisqu'il sera également connecté au système de fichiers du serveur, les données créées à l'aide du Conteneur #1 sont toujours disponibles, y compris notre utilisateur administrateur.

Nous ajoutons simplement l'option `--auth` à la commande initiale, elle indique à Mongo... eh bien, d'activer l'authentification. Vous avez deviné juste.

**Commande finale pour le Conteneur #2** :

```
docker run \
-d \
-p 27017:27017 \
--name my-awesome-db \
-v ~/dataMongo:/data/db mongo \
--auth
mongod
```

Maintenant, reconnectez-vous à votre instance Mongo et exécutez :

```
db.createCollection('IAMAHACKER')
```

**Vous obtiendrez un beau message d'erreur comme prévu !**

![Image](https://cdn-media-1.freecodecamp.org/images/vPDNkLmy6ItmfpXUyiQp7TkMYU4FrqcBnGC3)

Et maintenant, essayez à nouveau en étant authentifié :

```
mongo $(docker-machine ip my-awesome-server):27017 -u admin -p yourpassword
```

**Si cela fonctionne, vous avez terminé ! Félicitations ;)**

### Et maintenant ?

Votre base de données Mongo est opérationnelle dans le cloud, en toute sécurité isolée dans son conteneur Docker, et sécurisée avec une authentification par nom d'utilisateur/mot de passe.

Les prochaines étapes consisteront à connecter vos applications à cette base de données. N'oubliez pas que vous pouvez accéder à l'IP de votre serveur en utilisant la commande `docker-machine ip my-awesome-server`. Vous devrez certainement créer des utilisateurs supplémentaires pour administrer vos bases de données.

De plus, vous ne voudrez probablement pas que n'importe qui se connecte à votre shell de base de données, même avec l'authentification configurée. AWS vous permettra de mettre sur liste blanche quelques IP, correspondant à vos applications et à votre propre ordinateur, afin que seules les sources de confiance puissent se connecter à votre base de données.

En dessous de cet article, vous trouverez un glossaire, le script final, et une solution à un conteneur pour configurer l'authentification, ainsi que quelques conseils supplémentaires.

**J'espère que vous avez trouvé ce tutoriel utile !** Si c'est le cas, n'oubliez pas d'applaudir ;) Et n'oubliez pas de consulter les annexes ci-dessous...

<a href="https://twitter.com/LBKE_FR" target="_blank"><img src="https://cdn-media-1.freecodecamp.org/images/HbDwt-Vv483gfb6SdD1uCZQ8YyifxJYOE6AY"/></a>

### Annexe 1 — Script final

```bash
# Lancer une instance EC2
docker-machine create \
--driver amazonec2 \
--amazonec2-access-key ***** --amazonec2-secret-key **** \
--amazonec2-region ***** \
--amazonec2-open-port 27017 my-awesome-server
# Activer l'instance
eval $(docker-machine env my-awesome-server)
# Créer le conteneur 1
docker run \
-d \
-p 27017:27017 \
--name my-awesome-db \
-v ~/dataMongo:/data/db mongo \
mongod
# Se connecter à votre base de données
mongo $(docker-machine ip my-awesome-server):27017
# DANS LE SHELL MONGO créer un super administrateur
db.createUser(
  {
    user: "admin",
    pwd: "yourpassword",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ],
    passwordDigestor : "server"
  }
)
# QUITTER LE SHELL MONGO
# Supprimer le conteneur et en recréer un avec authentification
docker stop my-awesome-db
docker rm my-awesome-db
# Exécuter le conteneur final
docker run \
-d \
-p 27017:27017 \
--name my-awesome-db \
-v ~/dataMongo:/data/db mongo \
--auth \
mongod
# SI CA ÉCHOUE AVEC UNE ERREUR DE PERMISSION REFUSÉE
# voir https://github.com/kubernetes/minikube/issues/3083
# sudo vim /var/lib/snapd/apparmor/profiles/snap.docker.docker
# Ajouter la ligne suivante dans le fichier (par exemple à côté des autres lignes "owner") : 
# owner @{HOME}/.docker/machine/machines/** r,
# sudo apparmor_parser -r /var/lib/snapd/apparmor/profiles/snap.docker.docker
```

### Annexe 2 — Astuces pratiques que j'aurais préféré ne pas avoir à apprendre par moi-même

* Si vous êtes dans le domaine du devops, vous finirez par avoir une mémoire musculaire des commandes Docker. Sinon, si vous configurez des projets pour la production seulement une fois par an, ÉCRIVEZ TOUT. Par exemple, vous pourriez écrire un article sur Medium.  
Sérieusement, j'ai perdu quelques heures de travail parce que je n'ai pas écrit ma progression. La semaine suivante, j'avais tout oublié. Docker n'est pas trivial.
* J'ai rencontré un problème de permission avec l'authentification par certificat lors de l'utilisation de Docker Machine, la solution est dans les commentaires de ce fil : [https://github.com/kubernetes/minikube/issues/3083](https://github.com/kubernetes/minikube/issues/3083)
* `docker ps -a` imprimera tous les conteneurs, **y compris les inactifs**, tandis que `docker ps` n'imprime que les conteneurs actifs.
* Une image n'est PAS un Dockerfile. **Un Dockerfile est un fichier de configuration**. Pensez au plan d'un bateau. **Une image est un fichier Docker construit**. Pensez à un bateau QUI N'EST PAS ENCORE dans la mer. **Un conteneur est une image que vous exécutez**. Pensez à un bateau NAVIGUANT SUR LES MERS.

[**Différences entre un Dockerfile, une image Docker et un conteneur Docker**](https://nickjanetakis.com/blog/differences-between-a-dockerfile-docker-image-and-docker-container)  
[_Quick Jump: It All Starts With a Dockerfile | If You Build It, They Will Run (Usually) In casual conversation you may…_nickjanetakis.com](https://nickjanetakis.com/blog/differences-between-a-dockerfile-docker-image-and-docker-container)

* `docker pull mongo` tirera par exemple une image Docker Mongo, déjà construite. Mais comment afficher le Dockerfile associé ? Vous ne pouvez pas. Si vous voulez le vérifier, vous pouvez chercher le dépôt GitHub pertinent (s'il existe). C'est exactement la même relation entre un package NPM installé et son code. `npm install` installe une version construite (une "image") mais ne télécharge pas nécessairement le code (un "Dockerfile" ici), qui vit généralement sur GitHub mais peut aussi être privé.

[**Comment puis-je voir le Dockerfile dans une image ?**](https://forums.docker.com/t/how-can-i-view-the-dockerfile-in-an-image/5687/3)  
[_Hi, Looking at some images in the repository (this one, for example: https://hub.docker.com/r/filippobosi/mfi/) I do…_forums.docker.com](https://forums.docker.com/t/how-can-i-view-the-dockerfile-in-an-image/5687/3)

* Sur EC2, votre IP d'instance peut changer après les redémarrages ! Vous devrez régénérer les certificats pour continuer à vous connecter à l'instance en utilisant `docker-machine regenerate-certs my-awesome-server`

### Annexe 3— Configurer l'authentification — solution à un conteneur

Il existe également une solution "un conteneur". Elle est moins instructive, mais plus rapide et ne nécessite qu'un seul conteneur.

Note : si vous avez déjà configuré l'authentification en utilisant l'approche à 2 conteneurs, vous avez déjà terminé. Si vous souhaitez toujours essayer l'approche à 1 conteneur, vous devrez créer une nouvelle instance sur EC2 ou supprimer le dossier `~/dataMongo` du serveur.

**Vous devez toujours partager vos dossiers avec l'hôte, sinon vos données sont liées au conteneur, ce qui ne devrait pas arriver !** Les conteneurs doivent être facilement supprimables sans aucune perte de données, donc les documents doivent être stockés ailleurs.

L'idée est de se connecter à votre serveur et d'accéder à Mongo depuis là-bas, au lieu d'accéder à Mongo depuis votre machine locale. C'est une différence très subtile mais c'est ce qui nous fait gagner une étape.

Si vous vous connectez à Mongo tout en étant connecté à votre serveur, vous aurez plus de permissions et serez en mesure de configurer un utilisateur administrateur même si l'authentification est déjà activée, car Mongo vous considère comme un utilisateur "local". Pour reformuler, puisque vous avez été en mesure de vous connecter à la machine sur laquelle Mongo est en cours d'exécution, votre instance AWS, Mongo vous considère déjà comme un utilisateur "sûr", car un pirate ne devrait pas être là en premier lieu.

Exécutez uniquement la **Commande finale pour le Conteneur #2**

```
docker run \
-d \
-p 27017:27017 \
--name my-awesome-db \
-v ~/dataMongo:/data/db mongo \
--auth
mongod
```

Vous pouvez toujours vous connecter à votre serveur en utilisant `docker-machine ssh`:

```
docker-machine ssh my-awesome-server
```

L'exécution de `mongo` ouvrira le shell Mongo. À partir de là, vous pouvez ajouter un utilisateur administrateur MÊME si l'authentification est activée, comme nous l'avons fait précédemment.

### Annexe 4— Glossaire

Un peu de jargon de devops.

**AWS:** Amazon Web Services, une célèbre collection de services cloud avec des offres économiques.

**AWS EC2:** service pour héberger des instances de serveur. C'est là que vous hébergeriez votre API ou votre site web complet. Notez qu'il peut y avoir des services plus adaptés pour l'hébergement de bases de données, mais puisque EC2 est un incontournable, c'est mon choix en tant que débutant.

**Docker:** c'est un... eh bien, un programme ? En résumé, c'est un ensemble de choses qui vous aident à exécuter des programmes dans des conteneurs, isolés des autres programmes en cours d'exécution sur le serveur, sans coûter autant de ressources qu'une machine virtuelle. Les conteneurs sont également utiles pour gérer des services (API, bases de données, etc.) au quotidien : les tuer/redémarrer, créer une nouvelle instance en une ligne...

**Conteneur:** ce sera ma définition simplifiée, pensez à une machine virtuelle sans système d'exploitation. Il fournit de l'isolation tout en ne consommant pas trop de ressources informatiques.

**Dockerfile:** c'est un fichier de configuration pour docker, qui définit tous les programmes/fichiers/commandes/options dont vous avez besoin pour exécuter votre application.

**Docker Machine:** un CLI pour pousser vos conteneurs Docker où vous voulez, dans le cloud ou sur vos propres serveurs.

Je suis le co-fondateur de l'entreprise française Lebrun Burel Knowledge Engineering (LBKE) — [https://www.lbke.fr](https://www.lbke.fr)

_Toujours heureux de parler de code, d'apprentissage automatique, d'innovation et d'entrepreneuriat !_