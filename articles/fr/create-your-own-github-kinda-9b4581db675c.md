---
title: Créez votre propre GitHub (en quelque sorte)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-24T14:45:18.000Z'
originalURL: https://freecodecamp.org/news/create-your-own-github-kinda-9b4581db675c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BCZkmZR1_YzDZy22Vn4uUw.png
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: Devops
  slug: devops
- name: Git
  slug: git
- name: General Programming
  slug: programming
seo_title: Créez votre propre GitHub (en quelque sorte)
seo_desc: 'By Shashank Sharma

  In order to do any collaboration in Git, you’ll need to have a remote Git repository.
  Let’s cover step by step how you can create a Git server on an AWS EC2 instance.

  First, let’s cover some of the basics.

  Bare vs Non-bare reposito...'
---

Par Shashank Sharma

Pour effectuer toute collaboration dans Git, vous aurez besoin d'un dépôt Git distant. Couvrons étape par étape comment vous pouvez créer un serveur Git sur une instance AWS EC2.

Tout d'abord, couvrons quelques bases.

#### Dépôt nu vs non-nu

Un dépôt git qui n'a pas de répertoire de travail est appelé un dépôt "nu". Un dépôt "nu" dans Git ne contient que les informations de contrôle de version et aucun fichier de travail (aucun arbre). Il ne contient pas le sous-répertoire spécial .git. Au lieu de cela, il contient tout le contenu du sous-répertoire .git directement dans le répertoire principal lui-même.

```
Créer: git init --bare
```

```
Cloner: git clone --bare $URL
```

Un dépôt **non-nu** a un arbre de travail extrait avec un sous-répertoire .git.

```
Créer: git init
```

```
Cloner: git clone $URL
```

Vous devriez utiliser un dépôt non-nu pour travailler localement et un dépôt nu comme serveur/hub central pour partager vos modifications avec d'autres personnes. Par exemple, lorsque vous créez un dépôt sur github.com, il est créé comme un dépôt nu.

Les dépôts nus sont plus petits que les dépôts non-nus. Comme les dépôts nus n'ont pas de copie de travail, toute modification poussée vers eux ne causera pas de conflits. Par convention, les dépôts nus utilisent des noms avec le suffixe .git.

#### Les Protocoles

Git peut utiliser quatre protocoles principaux pour transférer des données: Local, HTTP, Secure Shell (SSH) et Git.

1. _Protocole Local:_ le protocole le plus basique, où le dépôt distant peut résider sur n'importe quel disque monté partagé. Vous pouvez cloner un dépôt local comme ceci:

```
git clone /var/local/repository
```

2. _Protocole HTTP:_ Ce protocole fonctionne sur les ports HTTP/S standard. Il peut utiliser des choses comme l'authentification de base nom d'utilisateur/mot de passe plutôt que de devoir configurer des clés SSH. Si vous utilisez cela, vous pouvez utiliser la même URL pour visualiser ou cloner le dépôt, comme avec Github.

3. _Protocole SSH:_ Il s'agit du protocole de transport le plus courant pour Git lors de l'auto-hébergement. Cela est dû au fait que l'accès SSH aux serveurs est déjà configuré dans la plupart des endroits — et si ce n'est pas le cas, c'est relativement simple à faire.

4. _Protocole Git:_ Le protocole Git est souvent le protocole de transfert réseau le plus rapide disponible. Il s'agit d'un démon spécial qui est fourni avec Git. Il écoute sur un port dédié (9418) qui fournit un service similaire au protocole SSH, mais sans aucune authentification.

Une explication approfondie de ces protocoles dépasse le cadre de cet article. Pour plus de détails, vous pouvez consulter [https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols](https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols).

#### Configuration du serveur Git sur une instance EC2

Maintenant, commençons à configurer un serveur Git. Si vous n'avez pas encore configuré une instance EC2 avec un accès SSH, suivez [ce guide](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) pour en créer une.

J'utilise une instance Ubuntu t2.micro pour cet exercice.

a) Connectez-vous à votre instance EC2 en utilisant SSH.

```
-> ssh -i ~/.certs/cert.pem ubuntu@54.254.174.183
```

b) Installez Git.

```
-> sudo apt-get install git
```

c) Créez un dépôt nu qui sera votre dépôt Git distant.

```
-> mkdir gitserverexcersise.git
-> cd gitserverexcersise.git
-> git init --bare
```

Cela créera votre dépôt nu vide. À ce stade, vous avez déjà un dépôt Git prêt à être cloné. Mais pour le cloner depuis votre système local, vous devez ajouter votre fichier pem à votre configuration ssh.

d) Ouvrez un autre terminal et ajoutez cette instance à la configuration SSH. Vous pouvez trouver le fichier de configuration SSH dans le dossier .ssh du répertoire personnel. Si vous n'avez pas ce dossier, vous pouvez en créer un. Et éditez ou créez le fichier de configuration dans l'éditeur de texte de votre choix.

```
-> vi .ssh/config
```

Ajoutez une entrée pour votre instance comme

```
 Host gitserver
 HostName 54.254.174.183
 User ubuntu
 IdentityFile ~/.certs/cert.pem
```

Et enregistrez.

e) Fermez ce terminal et ouvrez un nouveau terminal. Maintenant, vous devriez pouvoir vous connecter à l'instance ec2 en utilisant

```
-> ssh gitserver
```

Si vous pouvez vous connecter, vous pouvez cloner votre dépôt sur votre système local en utilisant:

```
-> git clone gitserver:gitserverexcersise.git
```

Félicitations! Vous avez réussi à configurer un serveur Git distant et pouvez maintenant pousser et tirer depuis ce serveur.

#### Configuration de GitWeb

Maintenant que vous avez un accès en lecture/écriture et en lecture seule à votre projet, vous pouvez souhaiter configurer un visualisateur basé sur le web. Git est livré avec un script CGI appelé GitWeb qui est parfois utilisé pour cela. Suivez les étapes ci-dessous pour configurer GitWeb.

a. Connectez-vous à votre instance EC2

```
-> ssh gitserver
```

b) Installez apache2

```
-> sudo apt-get update
-> sudo apt-get install apache2
```

c) Installez "make" car il sera nécessaire pour l'étape suivante

```
-> sudo apt-get install make
```

d) Nous allons obtenir le code source de Git, qui inclut GitWeb, et générer le script CGI personnalisé:

```
-> git clone git://git.kernel.org/pub/scm/git/git.git
-> cd git
-> make GITWEB_PROJECTROOT="/home/ubuntu" prefix=/usr gitweb
-> sudo cp -Rf gitweb /var/www/
```

GITWEB_PROJECTROOT est l'emplacement de vos dépôts Git.

e) Ajoutez VirtualHost pour Apache

```
-> cd /etc/apache2/sites-enabled/
```

Mettez à jour la configuration (000-default.conf) pour

```
<VirtualHost *:80>
    DocumentRoot /var/www/gitweb
    <Directory /var/www/gitweb>
        Options +ExecCGI +FollowSymLinks +SymLinksIfOwnerMatch
        AllowOverride All
        order allow,deny
        Allow from all
        AddHandler cgi-script cgi
        DirectoryIndex gitweb.cgi
    </Directory>
</VirtualHost>
```

f) Chargez le module mod_cgi

```
-> sudo a2enmod cgi
```

g) Redémarrez apache

```
-> sudo service apache2 restart
```

Félicitations! GitWeb est prêt. Avant de pouvoir accéder à GitWeb sur [http://54.254.174.183](http://54.254.174.183)/ (pour vous, ce serait l'URL publique de votre instance), il y a une dernière chose que vous devez faire: autoriser le port TCP 80 à s'ouvrir pour votre instance. Vous pouvez le faire en [modifiant le paramètre de votre groupe de sécurité](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/authorizing-access-to-an-instance.html) pour votre instance.

Si tout cela vous semble trop compliqué, vous pouvez opter pour d'autres alternatives comme [GitLab](https://about.gitlab.com/). GitLab est une application web basée sur une base de données, donc son installation est un peu plus impliquée que certains autres serveurs git. Heureusement, ce processus est très bien documenté et soutenu.

*Si vous avez aimé l'article et qu'il vous a aidé à configurer un serveur Git, cliquez sur le cœur ci-dessous et aidez les autres à le voir. Suivez-moi pour d'autres articles de ce genre.*