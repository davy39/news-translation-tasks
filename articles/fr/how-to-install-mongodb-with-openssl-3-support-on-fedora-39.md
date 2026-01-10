---
title: Comment installer MongoDB avec le support d'OpenSSL 3 sur Fedora 39
subtitle: ''
author: Matheus Alves dos Santos Freitas
co_authors: []
series: null
date: '2023-12-11T18:52:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-mongodb-with-openssl-3-support-on-fedora-39
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/Post-image.jpg
tags:
- name: Linux
  slug: linux
- name: MongoDB
  slug: mongodb
seo_title: Comment installer MongoDB avec le support d'OpenSSL 3 sur Fedora 39
seo_desc: "In this tutorial, you will learn how to install MongoDB with support for\
  \ the latest version of OpenSSL on the Fedora Linux operating system. \nIf you already\
  \ have it installed, this tutorial will help you fix the mongosh OpenSSL configuration\
  \ error.\nT..."
---

Dans ce tutoriel, vous apprendrez comment installer MongoDB avec le support de la dernière version d'OpenSSL sur le système d'exploitation Fedora Linux. 

Si vous l'avez déjà installé, ce tutoriel vous aidera à corriger l'erreur de configuration OpenSSL de mongosh.

Pour suivre ce guide, vous aurez besoin d'un terminal avec un accès root et d'une connexion Internet pour télécharger les paquets.

Voici ce que nous allons couvrir :

* [Le Cœur du Problème](#heading-le-coeur-du-probleme)
* [Solution de Contournement pour Installer MongoDB](#heading-solution-de-contournement-pour-installer-mongodb)
* [Comprendre l'Erreur OpenSSL de Mongosh](#heading-comprendre-l-erreur-openssl-de-mongosh)
* [Solution de Contournement pour Corriger l'Erreur sur les Installations Existantes de MongoDB](#heading-solution-de-contournement-pour-corriger-l-erreur-sur-les-installations-existantes-de-mongodb)
* [Comment Installer MongoDB avec le Support d'OpenSSL 3 à partir de Zéro](#heading-comment-installer-mongodb-avec-le-support-d-openssl-3-a-partir-de-zero)
* [Conclusion](#heading-conclusion)

## Le Cœur du Problème

Si vous consultez la documentation officielle de MongoDB et cherchez des instructions sur la façon de l'installer sur le système d'exploitation Fedora Workstation, vous ne trouverez rien. Mais vous pouvez trouver des instructions sur la façon de l'installer sur le système d'exploitation Red Hat Enterprise Linux.

> "Le projet Fedora est la distribution communautaire en amont de Red Hat® Enterprise Linux." ([Source : Red Hat](https://www.redhat.com/en/topics/linux/fedora-vs-red-hat-enterprise-linux))

En d'autres termes, Fedora et Red Hat Enterprise Linux sont très similaires.

> "La principale différence entre les distributions communautaires et entreprises réside dans la décision de ce qui est important pour les utilisateurs. La direction d'une distribution communautaire est définie par les contributeurs, qui choisissent et maintiennent les paquets parmi la large variété d'options open source. La direction d'une distribution entreprise est définie par un fournisseur, en fonction des besoins de ses clients." ([Source : Red Hat](https://www.redhat.com/en/topics/linux/fedora-vs-red-hat-enterprise-linux))

Maintenant, vous pourriez penser que vous pouvez installer MongoDB sur Fedora en suivant le tutoriel pour l'installer sur Red Hat. D'ailleurs, ce tutoriel est disponible à l'adresse [Installer MongoDB Community Edition sur Red Hat ou CentOS](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-red-hat/#install-mongodb-community-edition-on-red-hat-or-centos).

Le problème est que cela ne fonctionnera pas – et pour le prouver, je vais essayer de l'installer et vous montrer ce qui se passe.

**Note** : J'utilise le pilote MongoDB pour Node.js qui, au moment où j'écris cet article, ne supporte pas la version actuelle de MongoDB (7.0). Je vais donc essayer d'installer sa version précédente (6.0).

Les étapes requises pour installer MongoDB sur Fedora sont les suivantes :

1. Configurer le système de gestion des paquets
2. Installer les paquets MongoDB

Pour effectuer la première étape, ouvrez votre terminal, obtenez un accès root et tapez ce qui suit :

```text
# touch /etc/yum.repos.d/mongodb-org-6.0.repo
```

Maintenant, ouvrez le fichier en utilisant votre éditeur de texte préféré (j'utilise l'éditeur de texte Gnome, car il est fourni avec Fedora) :

```text
# gnome-text-editor /etc/yum.repos.d/mongodb-org-6.0.repo
```

Et collez ces lignes :

```text
[mongodb-org-6.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/6.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc
```

Enregistrez le fichier et fermez-le.

La deuxième étape peut être effectuée en exécutant la commande suivante :

```text
# dnf install -y mongodb-org

```

Après avoir exécuté la commande, vous obtiendrez une erreur similaire à celle-ci :

```text
Fedora 39 - x86_64 - Updates                     34 kB/s |  46 kB     00:01    
MongoDB Repository                               63  B/s | 391  B     00:06    
Errors during downloading metadata for repository 'mongodb-org-6.0':
  - Status code: 404 for https://repo.mongodb.org/yum/redhat/39/mongodb-org/6.0/x86_64/repodata/repomd.xml (IP: 65.8.214.17)
Error: Failed to download metadata for repo 'mongodb-org-6.0': Cannot download repomd.xml: Cannot download repodata/repomd.xml: All mirrors were tried
Ignoring repositories: mongodb-org-6.0
Last metadata expiration check: 0:00:02 ago on Thu 30 Nov 2023 09:15:21 AM -03.
No match for argument: mongodb-org
Error: Unable to find a match: mongodb-org

```

Il s'agit d'une erreur `404`, ce qui signifie que vous devez changer le `baseurl` du fichier qui configure le dépôt.

Si vous essayez d'ouvrir le `baseurl` dans votre navigateur, vous obtiendrez également une erreur `404` :

![Capture d'écran de l'erreur 404 que vous obtiendrez si vous visitez le baseurl dans un navigateur.](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-from-2023-11-30-17-05-28.png)
_Erreur `404` de `baseurl`_

C'est le cœur du problème.

## Solution de Contournement pour Installer MongoDB

Vous pouvez déduire que pour résoudre le problème, vous devez changer la valeur assignée au `baseurl`. La question devient : quelle est l'URL qui mène à la page contenant les paquets ?

La réponse est offerte par la documentation officielle de MongoDB :

> "Vous pouvez également télécharger les fichiers `.rpm` directement depuis le dépôt MongoDB. Les téléchargements sont organisés par version de Red Hat / CentOS (par exemple, `7`), puis par version de MongoDB (par exemple, `6.0`), puis par architecture (par exemple, `x86_64`)." ([Source : MongoDB](https://www.mongodb.com/docs/v6.0/tutorial/install-mongodb-on-red-hat/#install-mongodb-community-edition))

Maintenant, en visitant le [dépôt MongoDB](https://repo.mongodb.org/yum/redhat/), vous arriverez sur cette page :

![Capture d'écran de la page du dépôt MongoDB. Le titre de la page est "Index of RedHat". La page liste les dépôts avec d'anciennes versions de MongoDB, ainsi que des dépôts avec des versions plus récentes pour différentes versions de RedHat OS.](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-from-2023-11-30-17-20-57.png)
_Page du dépôt MongoDB_

À partir de là, j'ai navigué vers le dépôt approprié, en sélectionnant ma version préférée de MongoDB et l'architecture du système. Vous devriez faire de même.

J'ai abouti à l'URL suivante :

```text
https://repo.mongodb.org/yum/redhat/9Server/mongodb-org/6.0/x86_64/RPMS/
```

Cette URL mène au dépôt où se trouvent les paquets de MongoDB 6.0 pour les systèmes basés sur une architecture x86_64.

Voici ce que j'ai trouvé là-bas :

![Capture d'écran du dépôt MongoDB qui contient les paquets de sa sixième version pour les systèmes basés sur une architecture x86_64.](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-from-2023-11-30-17-27-37.png)
_Paquets MongoDB 6.0 pour les systèmes x86_64_

Après m'être assuré que les paquets pouvaient être trouvés, j'ai mis à jour le fichier qui configure le dépôt. Mais le `baseurl` doit pointer vers le parent du répertoire `RPMS`, ce qui a abouti à l'URL suivante :

```text
https://repo.mongodb.org/yum/redhat/9Server/mongodb-org/6.0/x86_64/
```

J'ai exécuté :

```text
# gnome-text-editor /etc/yum.repos.d/mongodb-org-6.0.repo
```

J'ai mis à jour le `baseurl` :

```text
[mongodb-org-6.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/9Server/mongodb-org/6.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc
```

Et j'ai installé les paquets :

```text
# dnf install -y mongodb-org
```

Voici les paquets qui ont été installés :

```text
Installed:
  mongodb-database-tools-100.9.3-1.x86_64                                       
  mongodb-mongosh-2.1.0-1.el8.x86_64                                           
  mongodb-org-6.0.12-1.el9.x86_64                                               
  mongodb-org-database-6.0.12-1.el9.x86_64                                     
  mongodb-org-database-tools-extra-6.0.12-1.el9.x86_64                         
  mongodb-org-mongos-6.0.12-1.el9.x86_64                                       
  mongodb-org-server-6.0.12-1.el9.x86_64                                       
  mongodb-org-tools-6.0.12-1.el9.x86_64                                         
  openssl-1:3.1.1-4.fc39.x86_64 
```

## Comprendre l'Erreur OpenSSL de Mongosh

Pour confirmer l'installation du serveur de base de données, exécutez cette commande :

```text
# mongod --version
```

Vous obtiendrez un message similaire à celui-ci :

```text
db version v6.0.12
Build Info: {
    "version": "6.0.12",
    "gitVersion": "21e6e8e11a45dfbdb7ca6cf95fa8c5f859e2b118",
    "openSSLVersion": "OpenSSL 3.1.1 30 May 2023",
    "modules": [],
    "allocator": "tcmalloc",
    "environment": {
        "distmod": "rhel90",
        "distarch": "x86_64",
        "target_arch": "x86_64"
    }
}
```

Pour confirmer l'installation du shell, exécutez cette commande :

```text
# mongosh --version
```

Et voici le message que vous obtiendrez :

```text
mongosh: OpenSSL configuration error:
00899523A67F0000:error:030000A9:digital envelope routines:alg_module_init:unknown option:../deps/openssl/openssl/crypto/evp/evp_cnf.c:61:name=rh-allow-sha1-signatures, value=yes
```

Oups ! Il y a eu une erreur.

J'ai vérifié la version installée d'OpenSSL en exécutant cette commande :

```text
# openssl version
```

Et j'ai obtenu ce résultat :

```text
OpenSSL 3.1.1 30 May 2023 (Library: OpenSSL 3.1.1 30 May 2023)
```

Avec cela, j'ai écarté une éventuelle incompatibilité entre les versions installées et requises d'OpenSSL.

Après quelques recherches, j'ai découvert que :

> "Il y a deux nouveaux paquets PPA créés à partir de la source mongosh : En plus de mongodb-mongosh, mongodb-mongosh-shared-openssl11 et mongodb-mongosh-shared-openssl3 sont également fournis. Ceux-ci sont liés à une bibliothèque OpenSSL dynamique installée sur le système." ([Source : MongoDB Jira](https://jira.mongodb.org/browse/MONGOSH-1231?jql=text%20~%20%22mongodb-mongosh-shared-openssl3%22))

Lorsque j'ai regardé les paquets qui étaient installés, j'ai vu le paquet _mongodb-mongosh_. J'ai donc su que je devais le remplacer par _mongodb-mongosh-shared-openssl3_.

D'ailleurs,

> "Le nom du paquet indique qu'il s'agit de la version de mongosh compilée contre openssl3." – Jack Woehr

Maintenant que nous comprenons le problème, corrigeons-le.

## Solution de Contournement pour Corriger l'Erreur sur les Installations Existantes de MongoDB

Si vous avez déjà installé MongoDB, voici les étapes nécessaires pour résoudre le problème :

1. Arrêter MongoDB
2. Supprimer le paquet _mongodb-org_
3. Supprimer le paquet _mongodb-mongosh_
4. Installer le paquet _mongodb-mongosh-shared-openssl3_
5. Activer MongoDB

Vous devez effectuer ces étapes dans le bon ordre. Si vous essayez d'installer le paquet _mongodb-mongosh-shared-openssl3_ sans désinstaller d'abord le paquet _mongodb-mongosh_, vous obtiendrez une erreur de conflit :

```text
Error: Transaction test error:
  file /usr/bin/mongosh from install of mongodb-mongosh-shared-openssl3-2.1.0-1.el8.x86_64 conflicts with file from package mongodb-mongosh-2.1.0-1.el8.x86_64
```

Si vous essayez de désinstaller le paquet _mongodb-mongosh_ sans désinstaller d'abord le paquet _mongodb-org_, vous obtiendrez une erreur de dépendance :

```text
error: Failed dependencies:
	mongodb-mongosh is needed by (installed) mongodb-org-6.0.12-1.el9.x86_64
```

Pour arrêter MongoDB, exécutez cette commande :

```
# systemctl stop mongod
```

**Note** : La commande ne produira aucune sortie si tout se passe bien.

Pour supprimer les paquets _mongodb-org_ et _mongodb-mongosh_, exécutez :

```text
# rpm -e mongodb-org mongodb-mongosh
```

**Note** : Je n'utilise pas la commande `dnf` car elle supprimerait _mongodb-org_ et toutes ses dépendances.

Vous pouvez également confirmer que seuls les deux paquets ont été supprimés en exécutant :

```text
# rpm -qa | grep mongodb-*
```

La sortie devrait être :

```text
mongodb-org-database-tools-extra-6.0.12-1.el9.x86_64
mongodb-database-tools-100.9.3-1.x86_64
mongodb-org-tools-6.0.12-1.el9.x86_64
mongodb-org-server-6.0.12-1.el9.x86_64
mongodb-org-mongos-6.0.12-1.el9.x86_64
mongodb-org-database-6.0.12-1.el9.x86_64
```

Pour installer les paquets _mongodb-org_ et _mongodb-mongosh-shared-openssl3_, exécutez :

```
# dnf install -y mongodb-org mongodb-mongosh-shared-openssl3
```

Enfin, pour démarrer MongoDB avec votre système d'exploitation, exécutez :

```text
# systemctl start mongod
```

Si vous voulez être sûr que la solution de contournement a fonctionné, exécutez :

```text
# mongod --version
```

Puis ceci :

```text
# mongosh --version
```

Maintenant, si vous êtes préoccupé par la destruction des données, sachez que les journaux et les bases de données ne seront supprimés que si vous exécutez les commandes suivantes :

```text
# rm -r /var/log/mongodb

```

Et ceci :

```text
# rm -r /var/lib/mongo
```

Une dernière chose : si vous exécutez `mongosh` et obtenez l'erreur suivante :

```text
MongoNetworkError: connect ECONNREFUSED 127.0.0.1:27017
```

redémarrez votre machine. Cela résoudra le problème.

## Comment Installer MongoDB avec le Support d'OpenSSL 3 à partir de Zéro

Si vous installez MongoDB pour la première fois, vous n'avez qu'à effectuer deux étapes :

1. Configurer le système de gestion des paquets
2. Installer les paquets MongoDB en les spécifiant individuellement

Vous pouvez effectuer la première étape en suivant ce que j'ai fait dans les sections [Le Cœur du Problème](#heading-le-coeur-du-probleme) et [Solution de Contournement pour Installer MongoDB](#heading-solution-de-contournement-pour-installer-mongodb) de cet article.

Cependant, pour installer les bons paquets, vous devriez remplacer cette commande :

```text
# dnf install -y mongodb-org
```

par celle-ci :

```text
# dnf install -y mongodb-org mongodb-mongosh-shared-openssl3 openssl mongodb-org-database-tools-extra mongodb-database-tools mongodb-org-tools mongodb-org-server mongodb-org-mongos mongodb-org-database
```

Vous pouvez confirmer que tous les paquets ont été installés en exécutant :

```text
# rpm -qa | grep mongodb-*
```

Ce qui devrait produire une sortie similaire à celle-ci :

```text
mongodb-org-database-tools-extra-6.0.12-1.el9.x86_64
mongodb-database-tools-100.9.3-1.x86_64
mongodb-org-tools-6.0.12-1.el9.x86_64
mongodb-org-server-6.0.12-1.el9.x86_64
mongodb-org-mongos-6.0.12-1.el9.x86_64
mongodb-org-database-6.0.12-1.el9.x86_64
mongodb-mongosh-shared-openssl3-2.1.0-1.el8.x86_64
mongodb-org-6.0.12-1.el9.x86_64
```

Gardez à l'esprit que la commande précédente ne produira que les paquets _liés à mongodb_. Pour confirmer l'installation d'OpenSSL, exécutez :

```text
# openssl version
```

Vous devriez obtenir quelque chose comme ceci :

```text
OpenSSL 3.1.1 30 May 2023 (Library: OpenSSL 3.1.1 30 May 2023)
```

Les paquets seront mis à jour avec votre système comme vous pouvez le voir dans la capture d'écran ci-dessous.

![Capture d'écran du paquet mongodb-mongosh-shared-openssl3 étant automatiquement mis à jour avec le système d'exploitation.](https://www.freecodecamp.org/news/content/images/2023/12/Screenshot-from-2023-12-05-01-26-14.png)
_Mise à jour de `mongodb-mongosh-shared-openssl3`_

## Conclusion

Les mises à jour des paquets sont importantes, car elles apportent de nouvelles fonctionnalités et/ou augmentent la sécurité des applications. Mais elles peuvent également causer des maux de tête lorsqu'elles provoquent des erreurs comme celle que nous avons traitée dans cet article.

Bien que vous puissiez être tenté de revenir en arrière pour vous débarrasser du problème, ne faites pas cela. Essayez plutôt de le résoudre.

Prêter attention aux messages d'erreur, lire la documentation officielle et rechercher sur le Web sera probablement suffisant pour résoudre la majorité des problèmes que vous rencontrez.

De plus, savoir comment différentes commandes affectent la manière dont les paquets sont installés/désinstallés sur votre système d'exploitation peut vous faire gagner du temps et des données (si vous êtes sur une connexion mesurée).

Si cet article vous a été utile, marquez-le et partagez-le avec vos amis. Vous pouvez également me suivre sur [Twitter](https://twitter.com/matheus4lvesfcc).

À la prochaine !