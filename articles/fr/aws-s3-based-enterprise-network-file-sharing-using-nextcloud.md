---
title: Comment configurer le partage de fichiers en réseau d'entreprise basé sur AWS
  S3 en utilisant Nextcloud
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-08-13T13:30:00.000Z'
originalURL: https://freecodecamp.org/news/aws-s3-based-enterprise-network-file-sharing-using-nextcloud
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/nextcloud-ui.png
tags:
- name: File sharing
  slug: file-sharing
- name: Linux
  slug: linux
- name: Nextcloud
  slug: nextcloud
seo_title: Comment configurer le partage de fichiers en réseau d'entreprise basé sur
  AWS S3 en utilisant Nextcloud
seo_desc: Nextcloud is an open source software suite that, when installed on a Linux
  server, can leverage storage capacity for saving, editing, and consuming a wide
  range of document types — including services like audio/video call hosting. Nextcloud
  also prov...
---

Nextcloud est une suite logicielle open source qui, une fois installée sur un serveur Linux, peut exploiter la capacité de stockage pour sauvegarder, éditer et consommer une large gamme de types de documents — y compris des services comme l'hébergement d'appels audio/vidéo. Nextcloud fournit également des applications _client_ qui permettent aux utilisateurs sur Linux, Windows, MacOS et les plateformes de smartphones d'interagir avec les ressources multimédias.

Avec Nextcloud, vous pouvez créer vos propres versions privées de Dropbox ou Google Drive, mais selon vos conditions et sans avoir à vous soucier des changements inattendus de disponibilité ou des accords de service/confidentialité.

Donc, c'est génial. Nextcloud a certains avantages réels. Mais se lancer seul signifie que vous êtes responsable des coûts et de la complexité de l'hébergement des données, de la réplication et des sauvegardes. Est-ce vraiment worth tout le trouble et les dépenses lorsque vous pouvez obtenir beaucoup de stockage à peu ou pas de coût en utilisant l'un de ces autres services ?

Bonne nouvelle : vous pouvez avoir les deux. Pour les données particulièrement sensibles, vous pouvez garder le tout en interne. Mais vous pouvez également construire un serveur Nextcloud comme votre front-end (pour contrôler finement comment les utilisateurs interagissent avec vos médias), mais avoir les données elles-mêmes automatiquement et sécurisées sauvegardées sur des services tiers moins chers et fiables, y compris Dropbox, Google Drive et Amazon S3. Si, plus tard, vous trouvez que vous devez migrer vos données loin d'un fournisseur tiers comme S3, vous pouvez le faire sans que vos utilisateurs ne remarquent jamais le changement.

## Prérequis matériels

Basé sur le contenu de mon livre Manning, [Linux in Action](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9), mettons quelque chose ensemble en utilisant Ubuntu.

Il est toujours bon de consulter la documentation d'une application pour s'assurer que vous avez assez de puissance matérielle et logicielle pour gérer la charge. La figure ci-dessous montre la page des exigences système de Nextcloud. Si vous prévoyez d'héberger un serveur simple, peu utilisé, pour seulement quelques dizaines d'utilisateurs, alors vous trouverez que Nextcloud est assez facile à vivre, ne demandant rien qui ne puisse être géré par un conteneur prêt à l'emploi.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-120.png)
_Exigences matérielles et logicielles pour les installations recommandées et minimales de Nextcloud_

N'importe quelle ancienne configuration matérielle minimale fonctionnera très bien pour les tests technologiques, mais je ne voudrais pas compter sur un seul conteneur LXC fonctionnant sur un ancien PC pour servir des dizaines de milliers d'utilisateurs et des téraoctets de données. Planifiez un déploiement à l'échelle de l'entreprise ? Nextcloud [fournit un guide de recommandations de déploiement utile et multi-niveaux](https://docs.nextcloud.com/server/12/admin_manual/installation/deployment_recommendations.html) pour la provision de plateformes à pleine puissance.

Voici, par exemple, ce que Nextcloud recommande pour un petit groupe de travail avec jusqu'à 150 utilisateurs accédant à jusqu'à 10 To de données :

* Un serveur avec 2 cœurs CPU
* 16 Go de RAM
* Authentification via le protocole Lightweight Directory Access Protocol (LDAP) (un protocole d'information distribué largement utilisé)
* Red Hat Enterprise Linux ou Ubuntu 16.04 _avec_ support du fournisseur
* Apache avec certificat de chiffrement TLS/SSL
* La base de données MySQL ou MariaDB
* Le système de fichiers Btrfs monté avec _nodatacow_ pour les partitions de données Nextcloud afin de permettre des sauvegardes _sans temps d'arrêt_
* Mise en cache avec memcache pour accélérer les performances d'accès

## Construction d'un serveur LAMP

Construire un environnement de base adapté pour tester le package devrait être suffisamment simple. Voici tous les packages dont vous aurez besoin pour votre serveur en une seule commande. J'ai ajouté wget et nano au cas où ils ne seraient pas déjà installés. Dans l'intérêt de garder l'image de base aussi petite que possible, des packages comme nano ne sont souvent pas installés par défaut sur certaines plateformes virtualisées comme les conteneurs LXC.

```
# apt install apache2 mariadb-server libapache2-mod-php7.0 \
 php7.0-gd php7.0-json php7.0-mysql php7.0-curl php7.0-mbstring \
 php7.0-intl php7.0-mcrypt php-imagick php7.0-xml php7.0-zip \
 wget nano
```

Si vous n'êtes pas difficile sur l'utilisation de MySQL plutôt que MariaDB — et que vous êtes sur un serveur Ubuntu — alors vous pourriez tout aussi facilement vous épargner beaucoup de frappe et opter pour le métapaquet du serveur LAMP dont j'ai parlé dans le chapitre précédent. Encore une fois : n'oubliez pas le caret (`^`) à la fin du nom du package.

```
apt install lamp-server^
```

Une fois installé, n'oubliez pas d'exécuter l'outil d'installation sécurisée de MySQL :

```
mysql_secure_installation
```

Si vous avez choisi la voie MariaDB et que vous avez dû utiliser sudo avec cette commande, voici une solution rapide :

```
MariaDB [(none)]> SET PASSWORD = PASSWORD('your-password');
MariaDB [(none)]> update mysql.user set plugin = 'mysql_native_password' where User='root';
MariaDB [(none)]> FLUSH PRIVILEGES;
```

## Configuration d'Apache

Pour garantir qu'Apache pourra communiquer avec Nextcloud, il y a quelques ajustements relativement simples que vous devrez faire. Tout d'abord, vous devriez activer quelques modules Apache via l'outil a2enmod. Le module rewrite est utilisé pour réécrire les URL en temps réel lorsqu'elles sont déplacées entre un client et le serveur. Le module headers effectue une fonction similaire pour les en-têtes HTTP.

```
a2enmod rewrite
a2enmod headers
```

Si vous ne prévoyez pas d'utiliser ce serveur à d'autres fins, placer les fichiers d'application Nextcloud dans la racine des documents Apache fonctionnerait. Puisque la valeur de l'entrée `DocumentRoot` dans le fichier 000-default.conf dans votre répertoire /etc/apache2/sites-available/ pointe déjà vers /var/www/html/, il n'y a vraiment rien de plus à faire.

Cependant, placer les fichiers de données de Nextcloud dans la racine des documents par défaut présente un risque potentiel pour la sécurité, vous voudrez donc probablement que votre application Nextcloud se trouve dans une autre partie de votre système de fichiers.

Il existe deux façons d'indiquer à Apache comment trouver les fichiers de site qui ne sont pas dans la racine des documents. La « méthode Ubuntu » implique l'ajout d'une nouvelle section à votre fichier 000-default.conf existant qui contient toutes les informations nécessaires. Cependant, la plupart des gens semblent préférer créer un nouveau fichier .conf dans le répertoire /etc/apache2/sites-available/ pour chaque nouveau service. Les deux méthodes fonctionnent très bien, mais voici à quoi devrait ressembler le fichier séparé en supposant que vous avez placé l'application dans /var/www/ plutôt que dans la racine des documents :

```
Alias /nextcloud "/var/www/nextcloud/"
<Directory /var/www/nextcloud/>
 Options +FollowSymlinks
 AllowOverride All
<IfModule mod_dav.c>
 Dav off
 </IfModule>
SetEnv HOME /var/www/nextcloud
 SetEnv HTTP_HOME /var/www/nextcloud
</Directory>
```

Notez que la ligne « Alias » associe le contenu du répertoire /var/www/nextcloud/ avec l'hôte « nextcloud » (ou « site »), et les deux lignes « SetEnv » attribuent des variables d'environnement qui définiront le fonctionnement de l'application Nextcloud.

Une directive similaire utilisant la méthode Ubuntu impliquerait l'ajout d'une section dans votre fichier 000-default.conf qui pourrait ressembler à ceci :

```
<VirtualHost *:443> <1>
 ServerName bootstrap-it.com
 DocumentRoot /var/www/nextcloud
 ServerAlias bootstrap-it.com/nextcloud <2>
</VirtualHost>
```

Comme vous pouvez le voir dans la figure, lorsque Apache lit ce fichier, il redirigera tout le trafic entrant adressé à example.com/nextcloud vers les fichiers d'application dans /var/www/ (en supposant, encore une fois, que votre domaine est example.com… comme avant, une adresse IP fonctionnera tout aussi bien).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-121.png)
_Apache lit les fichiers de configuration dans /etc/apache2/sites-enabled/ et utilise leurs paramètres pour rediriger les requêtes_

Enfin, vous devrez créer un lien symbolique dans le répertoire /etc/apache2/sites-enabled/ pointant vers le fichier nextcloud.conf que vous avez créé dans /etc/apache2/sites-available/.

```
ln -s /etc/apache2/sites-available/nextcloud.conf \
    /etc/apache2/sites-enabled/nextcloud.conf
```

Mais pourquoi ? Et qu'est-ce qu'un lien symbolique ?

Lorsque Apache démarre, il lit le contenu de /etc/apache2/sites-enabled/ à la recherche de configurations de site à charger. Ces configurations n'existeront pas réellement dans /etc/apache2/sites/enabled/, mais il y aura des liens symboliques vers les fichiers réels dans /etc/apache2/sites-available/.

Alors pourquoi ne pas simplement dire à Apache de lire /etc/apache2/sites-available/ en premier lieu et éliminer l'intermédiaire ? Parce que tout reposer sur des liens symboliques rend très facile et pratique de désactiver rapidement un site et puis — lorsque vous avez terminé une série d'éditions — de le réactiver une fois de plus. Plutôt que de devoir réellement supprimer et réécrire le fichier réel, vous n'aurez qu'à jouer avec un lien facile à gérer vers celui-ci.

Liens symboliques ? Ce sont simplement des objets qui _représentent_ des fichiers ou des répertoires vivant ailleurs sur un système de fichiers. Ils permettent à un utilisateur d'exécuter ou de visualiser une ressource à un endroit, même si la ressource elle-même est ailleurs.

## Téléchargement et décompression de Nextcloud

Vous pouvez télécharger le package Nextcloud le plus récent depuis la [page d'installation de Nextcloud](https://nextcloud.com/install/). Si vous installez sur un conteneur ou une VM — ou depuis un serveur sans interface graphique de bureau installée — alors l'approche la plus pratique est d'obtenir l'URL de téléchargement du package et de récupérer le package depuis la ligne de commande.

Un moyen rapide d'obtenir cette URL depuis le site Nextcloud (à partir d'une session régulière sur votre propre PC) est de cliquer sur l'onglet Télécharger sous Get Nextcloud Server, puis, comme vous pouvez le voir ci-dessous, sur le bouton Détails et options de téléchargement. Faites un clic droit sur le lien .tar.bz2 et sélectionnez Copier l'adresse du lien dans le menu.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-122.png)
_Liens vers les archives de téléchargement de Nextcloud : les formats .tar.bz2 ou .zip fonctionneront_

Vous pouvez copier cette URL dans une commande `wget` soit en faisant un clic droit dans le terminal et en sélectionnant coller, soit via SHIFT+CTRL+v.

```
wget https://download.nextcloud.com/server/releases/nextcloud-12.0.0.tar.bz2
```

N'oubliez pas de cliquer sur les liens de hachage MD5 ou SHA256 et de confirmer que ces valeurs sont identiques aux hachages que vous générez à partir de l'archive téléchargée. La décompression d'une archive .tar.bz2 nécessite les arguments xjf plutôt que `xzf` que vous utiliseriez pour un .gz.

```
tar xjf nextcloud-12.0.0.tar.bz2
```

L'étape suivante consiste à copier les fichiers et répertoires décompressés dans leur nouvel emplacement — qui, suivant les meilleures pratiques que j'ai mentionnées précédemment — sera dans /var/www/, un emplacement en dehors de la racine des documents. L'ajout de -r à la commande de copie copiera les fichiers « récursivement », pour inclure les sous-répertoires et leur contenu.

```
cp -r nextcloud /var/www/
```

Il ne reste plus que deux petites étapes et vous êtes prêt à partir. Apache aura besoin d'un accès complet à tous les fichiers dans les répertoires Nextcloud pour faire son travail. Vous pourriez faire en sorte que root les possède, mais cela signifie que vous devriez donner aux utilisateurs visiteurs des pouvoirs root pour accéder à ces fichiers. Comme vous pouvez l'imaginer, donner à tout le monde sur internet ce genre d'accès à vos fichiers pose un petit problème. Donc, de nombreux serveurs web utilisent un utilisateur système spécial appelé www-data.

La commande suivante utilisera chown pour transférer la propriété utilisateur et groupe de tous ces fichiers à l'utilisateur du serveur web www-data. L'utilisation du -R majuscule appliquera la commande récursivement à tous les fichiers et répertoires dans la hiérarchie des répertoires.

```
chown -R www-data:www-data /var/www/nextcloud/
```

Apache n'a aucune idée des choses que nous avons faites pendant qu'il ne regardait pas, alors vous feriez mieux de le mettre au courant en redémarrant le service.

```
# systemctl restart apache2
```

Si ce redémarrage n'a pas réussi, notez les messages d'erreur et voyez s'il y a quelque chose que vous pouvez corriger. Vous pouvez également creuser un peu plus dans les logs en affichant les dix dernières entrées dans le Journal. Il pourrait, par exemple, y avoir une référence à une ligne spécifique dans le fichier nextcloud.conf.

```
journalctl | tail
```

Mais si tout s'est bien passé, dirigez votre navigateur vers l'adresse IP de votre conteneur suivie de `nextcloud`. Vous serez dirigé vers une page où l'on vous demandera de créer un nouveau compte administrateur et de fournir des identifiants de connexion valides pour votre base de données MariaDB. À moins que vous n'ayez créé un autre compte utilisateur de base de données à cet effet, vous utiliserez `root` et le mot de passe que vous lui avez donné précédemment.

```
10.0.3.36/nextcloud
```

Une fois vos informations traitées, vous verrez des liens vers les applications client de Nextcloud, puis vous serez dirigé vers la console d'administration que vous pouvez voir dans la figure suivante. C'est là que vous pouvez télécharger, visualiser et partager des documents et des fichiers multimédias.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-123.png)
_La console principale de Nextcloud, complète avec des dossiers et fichiers d'exemple — vous pouvez travailler avec des objets ici comme vous le feriez en utilisant un gestionnaire de fichiers OS_

En tant qu'administrateur du site, vous pouvez également créer des groupes et des utilisateurs, attribuer des permissions et des quotas, et gérer le fonctionnement du site.

## Utilisation d'AWS S3 comme stockage principal de Nextcloud

Le problème avec le stockage des choses est que vous devez trouver de l'espace pour tout mettre. Et, puisque tous les dispositifs de stockage finiront par tomber en panne sans avertissement, vous aurez besoin de plusieurs copies de chaque dispositif. Déterminer comment provisionner, connecter et maintenir de tels tableaux de stockage est chronophage, et le maintenir en marche est relativement coûteux.

Le stockage dans le cloud, en revanche, est comparativement bon marché et — comme vous pouvez le lire dans mon livre Manning « [Learn Amazon Web Services in a Month of Lunches](https://www.manning.com/books/learn-amazon-web-services-in-a-month-of-lunches?a_aid=bootstrap-it&amp;a_bid=1c1b5e27) » — simple à configurer. Puisque les grands fournisseurs de cloud investissent des fonds considérables dans la sécurité et la résilience des données, leurs services sont pratiquement garantis pour être plus fiables que tout ce que vous pourriez assembler.

Par conséquent, l'utilisation de données basées sur le cloud comme backend pour votre site Nextcloud hébergé localement est une option sérieuse à explorer. Voici comment cela fonctionne.

Vous devrez d'abord activer le bundle d'applications External storage support. À partir de l'icône d'engrenage en haut à droite, cliquez sur l'élément Apps, puis sur le lien Disabled apps dans le panneau de gauche. Comme le montre la figure, l'option External storage support apparaît dans la liste. Cliquez sur Enable.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-124.png)
_La liste des applications actuellement disponibles, y compris External storage support_

## Connecter Nextcloud à un bucket S3

À partir de la ligne de commande sur n'importe quel ordinateur avec l'AWS CLI installé et configuré pour votre compte AWS (voir [le chapitre 12 de mon livre AWS in a Month of Lunches](https://livebook.manning.com/#!/book/learn-amazon-web-services-in-a-month-of-lunches/chapter-12/) pour plus de détails), créez un nouveau bucket avec un nom globalement unique.

```
$ aws s3 mb nextcloud32327
```

Récupérez un ensemble de clés d'accès de compte à partir de la page Vos informations d'identification de sécurité dans la console AWS ([chapitre 7 dans le livre AWS](https://livebook.manning.com/#!/book/learn-amazon-web-services-in-a-month-of-lunches/chapter-7/)). Vous pouvez également utiliser un ensemble de clés existant si vous en avez un disponible.

Maintenant, retournez à votre console Nextcloud, cliquez sur Admin dans le menu déroulant de l'engrenage, puis sur le lien External storages qui devrait être visible dans le panneau de gauche. Cela ouvrira la page External storages, où vous pouvez cliquer sur le menu déroulant Add storage et sélectionner Amazon S3 dans la liste — qui inclut également Dropbox et Google Drive.

Vous serez invité à entrer le bucket S3 que vous souhaitez utiliser ainsi que vos clés d'accès et secrètes. Tous les autres champs — qui vous permettent de personnaliser votre configuration en utilisant des choses comme des ports non standard ou le chiffrement SSL — sont optionnels. Une fois terminé, cliquer sur la coche à droite enregistrera vos paramètres et lancera Nextcloud pour essayer de s'authentifier avec AWS.

Si vous réussissez, vous verrez un cercle vert heureux à gauche, comme visible dans la figure. Si cela ne fonctionne pas, la cause la plus probable est que vous avez utilisé des clés d'authentification invalides. Cela ne peut pas faire de mal de confirmer la connectivité réseau à internet et, en particulier, AWS.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-125.png)
_La page de configuration des stockages externes pour Amazon S3, montrant une connexion réussie à mon bucket S3_

Vous pouvez tester votre nouvelle configuration de stockage en copiant et collant un fichier de votre ordinateur dans le dossier de votre console Nextcloud. Ensuite, à partir de votre AWS CLI, listez le contenu de votre bucket.

```
aws s3 ls s3://nextcloud32327
testfile.pdf
```

Bien sûr, vous devrez également le tester dans l'autre sens. Copiez un fichier local dans le bucket à partir de votre ligne de commande.

```
aws s3 cp test.txt s3://nextcloud32327
```

Ce fichier test.txt devrait apparaître dans votre console. Intégration de stockage multi-plateforme glorieux.

_Cet article est extrait de mon livre Manning « Linux in Action ». Il y a beaucoup plus de plaisir [d'où cela vient](https://bootstrap-it.com/index.php/books/), y compris un cours hybride appelé [Linux in Motion](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1) qui est composé de plus de deux heures de vidéo et d'environ 40% du texte de Linux in Action. Qui sait… vous pourriez également apprécier mon [Learn Amazon Web Services in a Month of Lunches](https://www.manning.com/books/learn-amazon-web-services-in-a-month-of-lunches?a_aid=bootstrap-it&amp;a_bid=1c1b5e27)._