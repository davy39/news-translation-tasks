---
title: Le manuel NGINX – Apprendre NGINX pour les débutants
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2021-04-26T23:56:38.000Z'
originalURL: https://freecodecamp.org/news/the-nginx-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/NGINX-Handbook-Mockup.png
tags:
- name: nginx
  slug: nginx
- name: servers
  slug: servers
seo_title: Le manuel NGINX – Apprendre NGINX pour les débutants
seo_desc: A young Russian developer named Igor Sysoev was frustrated by older web
  servers' inability to handle more than 10 thousand concurrent requests. This is
  a problem referred to as the C10k problem. As an answer to this, he started working
  on a new web s...
---

Un jeune développeur russe nommé [Igor Sysoev](https://en.wikipedia.org/wiki/Igor_Sysoev) était frustré par l'incapacité des anciens serveurs web à gérer plus de 10 000 requêtes simultanées. C'est un problème connu sous le nom de [problème C10k](https://en.wikipedia.org/wiki/C10k_problem). En guise de réponse, il a commencé à travailler sur un nouveau serveur web en 2002.

[NGINX](https://nginx.org/) a été publié pour la première fois au public en 2004 sous les termes de la licence [2-clause BSD](https://en.wikipedia.org/wiki/2-clause_BSD). Selon l'étude [March 2021 Web Server Survey](https://news.netcraft.com/archives/2021/03/29/march-2021-web-server-survey.html), NGINX détient 35,3 % du marché avec un total de 419,6 millions de sites.

Grâce à des outils comme [NGINXConfig](https://www.digitalocean.com/community/tools/nginx) par [DigitalOcean](https://digitalocean.com/) et une abondance de fichiers de configuration pré-écrits sur Internet, les gens ont tendance à faire beaucoup de copier-coller au lieu d'essayer de comprendre lorsqu'il s'agit de configurer NGINX.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/177962736_1410222585999736_5618677227291897851_n.jpg)
_Croyez-moi, ce n'est pas si difficile..._

Je ne dis pas que copier du code est mal, mais copier du code sans comprendre est un grand "non non".

De plus, NGINX est le genre de logiciel qui doit être configuré exactement selon les exigences de l'application à servir et les ressources disponibles sur l'hôte.

C'est pourquoi, au lieu de copier aveuglément, vous devriez comprendre puis affiner ce que vous copiez – et c'est là que ce manuel intervient.

Après avoir parcouru l'intégralité de ce livre, vous devriez être capable de :

* Comprendre les fichiers de configuration générés par les outils populaires ainsi que ceux trouvés dans diverses documentations.
* Configurer NGINX en tant que serveur web, reverse proxy et équilibreur de charge à partir de zéro.
* Optimiser NGINX pour obtenir les performances maximales de votre serveur.

## Prérequis

* Familiarité avec le terminal Linux et les programmes Unix courants tels que `ls`, `cat`, `ps`, `grep`, `find`, `nproc`, `ulimit` et `nano`.
* Un ordinateur assez puissant pour faire tourner une machine virtuelle ou un serveur privé virtuel (VPS) à 5 $.
* Compréhension des applications web et d'un langage de programmation tel que JavaScript ou PHP.

## Table des matières

- [Introduction à NGINX](#heading-introduction-a-nginx)
- [Comment installer NGINX](#heading-comment-installer-nginx)
    - [Comment provisionner une machine virtuelle locale](#heading-comment-provisionner-une-machine-virtuelle-locale)
    - [Comment provisionner un serveur privé virtuel](#heading-comment-provisionner-un-serveur-prive-virtuel)
    - [Comment installer NGINX sur un serveur provisionné ou une machine virtuelle](#heading-comment-installer-nginx-sur-un-serveur-provisionne-ou-une-machine-virtuelle-2)
- [Introduction aux fichiers de configuration de NGINX](#heading-introduction-aux-fichiers-de-configuration-de-nginx)
- [Comment configurer un serveur web de base](#heading-comment-configurer-un-serveur-web-de-base)
    - [Comment écrire votre premier fichier de configuration](#heading-comment-ecrire-votre-premier-fichier-de-configuration)
    - [Comment valider et recharger les fichiers de configuration](#heading-comment-valider-et-recharger-les-fichiers-de-configuration)
    - [Comment comprendre les directives et les contextes dans NGINX](#heading-comment-comprendre-les-directives-et-les-contextes-dans-nginx)
    - [Comment servir du contenu statique avec NGINX](#heading-comment-servir-du-contenu-statique-avec-nginx)
    - [Gestion des types de fichiers statiques dans NGINX](#heading-gestion-des-types-de-fichiers-statiques-dans-nginx)
    - [Comment inclure des fichiers de config partiels](#heading-comment-inclure-des-fichiers-de-config-partiels)
- [Routage dynamique dans NGINX](#heading-routage-dynamique-dans-nginx)
    - [Correspondances de location](#heading-correspondances-de-location)
    - [Variables dans NGINX](#heading-variables-dans-nginx)
    - [Redirections et réécritures](#heading-redirections-et-reecritures)
    - [Comment essayer plusieurs fichiers](#heading-comment-essayer-plusieurs-fichiers)
- [Journalisation dans NGINX](#heading-journalisation-dans-nginx)
- [Comment utiliser NGINX comme reverse proxy](#heading-comment-utiliser-nginx-comme-reverse-proxy)
    - [Node.js avec NGINX](#heading-nodejs-avec-nginx)
    - [PHP avec NGINX](#heading-php-avec-nginx)
- [Comment utiliser NGINX comme équilibreur de charge](#heading-comment-utiliser-nginx-comme-equilibreur-de-charge)
- [Comment optimiser NGINX pour des performances maximales](#heading-comment-optimiser-nginx-pour-des-performances-maximales)
    - [Comment configurer les Worker Processes et les Worker Connections](#heading-comment-configurer-les-worker-processes-et-les-worker-connections)
    - [Comment mettre en cache le contenu statique](#heading-comment-mettre-en-cache-le-contenu-statique)
    - [Comment compresser les réponses](#heading-comment-compresser-les-reponses)
- [Comment comprendre le fichier de configuration principal](#heading-comment-comprendre-le-fichier-de-configuration-principal-1)
- [Comment configurer SSL et HTTP/2](#heading-comment-configurer-ssl-et-http2)
    - [Comment configurer SSL](#heading-comment-configurer-ssl)
    - [Comment activer HTTP/2](#heading-comment-activer-http2)
    - [Comment activer le Server Push](#heading-comment-activer-le-server-push)
- [Conclusion](#heading-conclusion)

## Code du projet

Vous pouvez trouver le code des exemples de projets dans le dépôt suivant :

%[https://github.com/fhsinchy/nginx-handbook-projects]

## Introduction à NGINX

[NGINX](https://nginx.org/) est un serveur web haute performance développé pour répondre aux besoins croissants du web moderne. Il se concentre sur la haute performance, la haute simultanéité et une faible utilisation des ressources. Bien qu'il soit principalement connu comme un serveur web, NGINX est à la base un serveur [reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy).

NGINX n'est cependant pas le seul serveur web sur le marché. L'un de ses plus grands concurrents est [Apache HTTP Server (httpd)](https://httpd.apache.org/), publié pour la première fois en 1995. Bien qu'Apache HTTP Server soit plus flexible, les administrateurs serveurs préfèrent souvent NGINX pour deux raisons principales :

* Il peut gérer un plus grand nombre de requêtes simultanées.
* Il offre une livraison de contenu statique plus rapide avec une faible utilisation des ressources.

Je n'irai pas plus loin dans le débat Apache vs NGINX. Mais si vous souhaitez en savoir plus sur les différences détaillées entre eux, cet excellent [article](https://www.digitalocean.com/community/tutorials/apache-vs-nginx-practical-considerations) de [Justin Ellingwood](https://www.digitalocean.com/community/users/jellingwood) pourrait vous aider.

En fait, pour expliquer la technique de gestion des requêtes de NGINX, j'aimerais citer deux paragraphes de l'article de Justin ici :

> Nginx est apparu après Apache, avec une meilleure conscience des problèmes de simultanéité auxquels les sites à grande échelle seraient confrontés. En s'appuyant sur ces connaissances, Nginx a été conçu dès le départ pour utiliser un algorithme de gestion des connexions asynchrone, non bloquant et piloté par les événements.
>   
> Nginx lance des worker processes, dont chacun peut gérer des milliers de connexions. Les worker processes y parviennent en implémentant un mécanisme de boucle rapide qui vérifie et traite continuellement les événements. Le découplage du travail réel des connexions permet à chaque worker de ne s'occuper d'une connexion que lorsqu'un nouvel événement a été déclenché.

Si cela semble un peu compliqué à comprendre, ne vous inquiétez pas. Avoir une compréhension de base du fonctionnement interne suffira pour l'instant.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/wQszK2rvq-1.png)

NGINX est plus rapide pour la livraison de contenu statique tout en restant relativement léger en ressources car il n'intègre pas de processeur de langage de programmation dynamique. Lorsqu'une requête pour du contenu statique arrive, NGINX répond simplement avec le fichier sans exécuter de processus supplémentaires.

Cela ne signifie pas que NGINX ne peut pas gérer les requêtes nécessitant un processeur de langage dynamique. Dans de tels cas, NGINX délègue simplement les tâches à des processus séparés tels que [PHP-FPM](https://www.php.net/manual/en/install.fpm.php), [Node.js](https://nodejs.org/) ou [Python](https://python.org/). Ensuite, une fois que ce processus a terminé son travail, NGINX renvoie la réponse au client via le reverse proxy.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/_nT7rcdjG.png)

NGINX est également beaucoup plus facile à configurer grâce à une syntaxe de fichier de configuration inspirée de divers langages de script, ce qui donne des fichiers de configuration compacts et faciles à maintenir.

## Comment installer NGINX

Installer NGINX sur un système basé sur [Linux](https://en.wikipedia.org/wiki/Linux) est assez simple. Vous pouvez soit utiliser un serveur privé virtuel (VPS) sous [Ubuntu](https://ubuntu.com/) comme terrain de jeu, soit provisionner une machine virtuelle sur votre système local à l'aide de Vagrant.

Dans la plupart des cas, provisionner une machine virtuelle locale suffira et c'est la méthode que j'utiliserai dans cet article.

### Comment provisionner une machine virtuelle locale

Pour ceux qui ne le savent pas, [Vagrant](https://vagrantup.com/) est un outil open-source de [Hashicorp](https://www.hashicorp.com/) qui vous permet de provisionner des machines virtuelles à l'aide de simples fichiers de configuration.

Pour que cette approche fonctionne, vous aurez besoin de [VirtualBox](https://www.virtualbox.org/wiki/Downloads/) et de [Vagrant](https://www.vagrantup.com/downloads/), alors allez-y et installez-les d'abord. Si vous avez besoin d'une petite introduction sur le sujet, ce [tutoriel](https://learn.hashicorp.com/collections/vagrant/getting-started/) peut vous aider.

Créez un répertoire de travail quelque part dans votre système avec un nom explicite. Le mien est le répertoire `~/vagrant/nginx-handbook`.

À l'intérieur du répertoire de travail, créez un fichier nommé `Vagrantfile` et mettez-y le contenu suivant :

```vagrantfile
Vagrant.configure("2") do |config|

    config.vm.hostname = "nginx-handbook-box"
  
    config.vm.box = "ubuntu/focal64"
  
    config.vm.define "nginx-handbook-box"
  
    config.vm.network "private_network", ip: "192.168.20.20"
  
    config.vm.provider "virtualbox" do |vb|
      vb.cpus = 1
      vb.memory = "1024"
      vb.name = "nginx-handbook"
    end
  
  end
```

Ce `Vagrantfile` est le fichier de configuration dont j'ai parlé plus tôt. Il contient des informations telles que le nom de la machine virtuelle, le nombre de processeurs, la taille de la RAM, l'adresse IP, et plus encore.

Pour démarrer une machine virtuelle à l'aide de cette configuration, ouvrez votre terminal dans le répertoire de travail et exécutez la commande suivante :

```shell
vagrant up

# Démarrage de la machine 'nginx-handbook-box' avec le fournisseur 'virtualbox'...
# ==> nginx-handbook-box: Importation de la box de base 'ubuntu/focal64'...
# ==> nginx-handbook-box: Correspondance de l'adresse MAC pour le réseau NAT...
# ==> nginx-handbook-box: Vérification si la version '20210415.0.0' de la box 'ubuntu/focal64' est à jour...
# ==> nginx-handbook-box: Définition du nom de la VM : nginx-handbook
# ==> nginx-handbook-box: Effacement de toutes les interfaces réseau précédemment définies...
# ==> nginx-handbook-box: Préparation des interfaces réseau basées sur la configuration...
#     nginx-handbook-box: Adaptateur 1 : nat
#     nginx-handbook-box: Adaptateur 2 : hostonly
# ==> nginx-handbook-box: Transfert de ports...
#     nginx-handbook-box: 22 (invité) => 2222 (hôte) (adaptateur 1)
# ==> nginx-handbook-box: Exécution des personnalisations de la VM 'pre-boot'...
# ==> nginx-handbook-box: Démarrage de la VM...
# ==> nginx-handbook-box: Attente du démarrage de la machine. Cela peut prendre quelques minutes...
#     nginx-handbook-box: Adresse SSH : 127.0.0.1:2222
#     nginx-handbook-box: Nom d'utilisateur SSH : vagrant
#     nginx-handbook-box: Méthode d'authentification SSH : clé privée
#     nginx-handbook-box: Attention : Déconnexion de la connexion distante. Réessai...
#     nginx-handbook-box: Attention : Réinitialisation de la connexion. Réessai...
#     nginx-handbook-box: 
#     nginx-handbook-box: Clé non sécurisée Vagrant détectée. Vagrant va automatiquement remplacer
#     nginx-handbook-box: celle-ci par une nouvelle paire de clés générée pour une meilleure sécurité.
#     nginx-handbook-box: 
#     nginx-handbook-box: Insertion de la clé publique générée dans l'invité...
#     nginx-handbook-box: Suppression de la clé non sécurisée de l'invité si elle est présente...
#     nginx-handbook-box: Clé insérée ! Déconnexion et reconnexion à l'aide de la nouvelle clé SSH...
# ==> nginx-handbook-box: Machine démarrée et prête !
# ==> nginx-handbook-box: Vérification des additions invité dans la VM...
# ==> nginx-handbook-box: Définition du nom d'hôte...
# ==> nginx-handbook-box: Configuration et activation des interfaces réseau...
# ==> nginx-handbook-box: Montage des dossiers partagés...
#     nginx-handbook-box: /vagrant => /home/fhsinchy/vagrant/nginx-handbook

vagrant status

# États actuels de la machine :

# nginx-handbook-box           running (virtualbox)

```

La sortie de la commande `vagrant up` peut différer sur votre système, mais tant que `vagrant status` indique que la machine est en cours d'exécution (`running`), tout est bon.

Étant donné que la machine virtuelle est maintenant en cours d'exécution, vous devriez pouvoir vous y connecter en SSH. Pour ce faire, exécutez la commande suivante :

```shell
vagrant ssh nginx-handbook-box

# Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-72-generic x86_64)
# vagrant@nginx-handbook-box:~$

```

Si tout a été fait correctement, vous devriez être connecté à votre machine virtuelle, ce qui sera évident par la ligne `vagrant@nginx-handbook-box` sur votre terminal.

Cette machine virtuelle sera accessible sur **http://192.168.20.20** sur votre machine locale. Vous pouvez même attribuer un domaine personnalisé comme **http://nginx-handbook.test** à la machine virtuelle en ajoutant une entrée à votre fichier **hosts** :

```shell
# sur terminal mac et linux
sudo nano /etc/hosts

# sur l'invite de commande windows en tant qu'administrateur
notepad c:\windows\system32\drivers\etc\hosts
```

Ajoutez maintenant la ligne suivante à la fin du fichier :

```
192.168.20.20   nginx-handbook.test

```

Maintenant, vous devriez pouvoir accéder à la machine virtuelle sur l'URI **http://nginx-handbook.test** dans votre navigateur.

Vous pouvez arrêter ou détruire la machine virtuelle en exécutant les commandes suivantes dans le répertoire de travail :

```shell
# pour arrêter la machine virtuelle
vagrant halt

# pour détruire la machine virtuelle
vagrant destroy

```

Si vous voulez en savoir plus sur les commandes Vagrant, ce [pense-bête](https://gist.github.com/wpscholar/a49594e2e2b918f4d0c4) peut s'avérer utile.

Maintenant que vous avez une machine virtuelle Ubuntu fonctionnelle sur votre système, il ne reste plus qu'à [installer NGINX](#heading-comment-installer-nginx-sur-un-serveur-provisionne-ou-une-machine-virtuelle-2).

### Comment provisionner un serveur privé virtuel

Pour cette démonstration, j'utiliserai [Vultr](https://vultr.com/) comme fournisseur, mais vous pouvez utiliser [DigitalOcean](https://digitalocean.com/) ou tout autre fournisseur que vous aimez.

En supposant que vous ayez déjà un compte chez votre fournisseur, connectez-vous au compte et déployez un nouveau serveur :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/ZUAu_Tpxx-2.jpg)

Sur DigitalOcean, on l'appelle généralement un "droplet". Sur l'écran suivant, choisissez un emplacement proche de vous. J'habite au Bangladesh, c'est pourquoi j'ai choisi Singapour :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/zH08EnmGq.jpg)

À l'étape suivante, vous devrez choisir le système d'exploitation et la taille du serveur. Choisissez Ubuntu 20.04 et la plus petite taille de serveur possible :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/G8mEC13pp.jpg)

Bien que les serveurs de production aient tendance à être beaucoup plus grands et plus puissants que cela, un minuscule serveur sera plus que suffisant pour cet article.

Enfin, pour la dernière étape, mettez quelque chose de approprié comme **nginx-handbook-demo-server** comme hôte et étiquette du serveur. Vous pouvez même les laisser vides si vous le souhaitez.

Une fois que vous êtes satisfait de vos choix, allez-y et appuyez sur le bouton **Deploy Now**.

Le processus de déploiement peut prendre un certain temps, mais une fois terminé, vous verrez le nouveau serveur sur votre tableau de bord :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/server-list.png)

Faites également attention au **Status** – il devrait indiquer **Running** et non **Preparing** ou **Stopped**. Pour vous connecter au serveur, vous aurez besoin d'un nom d'utilisateur et d'un mot de passe.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/server-overview.png)

Allez sur la page d'aperçu de votre serveur et vous devriez y voir l'adresse IP du serveur, le nom d'utilisateur et le mot de passe :

La commande générique pour se connecter à un serveur via SSH est la suivante :

```shell
ssh <username>@<ip address>

```

Donc, dans le cas de mon serveur, ce sera :

```shell
ssh root@45.77.251.108

# Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
# Warning: Permanently added '45.77.251.108' (ECDSA) to the list of known hosts.

# root@45.77.251.108's password: 
# Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-65-generic x86_64)

# root@localhost:~#

```

On vous demandera si vous souhaitez continuer à vous connecter à ce serveur ou non. Répondez par `yes`, puis on vous demandera le mot de passe. Copiez le mot de passe de la page d'aperçu du serveur et collez-le dans votre terminal.

Si vous faites tout correctement, vous devriez être connecté à votre serveur – vous verrez la ligne `root@localhost` sur votre terminal. Ici, `localhost` est le nom d'hôte du serveur et peut différer dans votre cas.

Vous pouvez accéder à ce serveur directement par son adresse IP. Ou si vous possédez un domaine personnalisé, vous pouvez également l'utiliser.

Tout au long de l'article, vous me verrez ajouter des domaines de test au fichier `hosts` de mon système d'exploitation. Dans le cas d'un serveur réel, vous devrez configurer ces serveurs via votre fournisseur DNS.

Rappelez-vous que vous serez facturé tant que ce serveur est utilisé. Bien que les frais soient très minimes, je vous préviens quand même. Vous pouvez détruire le serveur à tout moment en cliquant sur l'icône de la corbeille sur la page d'aperçu du serveur :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-90.png)

Si vous possédez un nom de domaine personnalisé, vous pouvez attribuer un sous-domaine à ce serveur. Maintenant que vous êtes à l'intérieur du serveur, il ne reste plus qu'à [installer NGINX](#heading-comment-installer-nginx-sur-un-serveur-provisionne-ou-une-machine-virtuelle-2).

### Comment installer NGINX sur un serveur provisionné ou une machine virtuelle

En supposant que vous soyez connecté à votre serveur ou machine virtuelle, la première chose à faire est d'effectuer une mise à jour. Exécutez la commande suivante pour ce faire :

```shell
sudo apt update && sudo apt upgrade -y

```

Après la mise à jour, installez NGINX en exécutant la commande suivante :

```shell
sudo apt install nginx -y
```

Une fois l'installation terminée, NGINX devrait être automatiquement enregistré en tant que service `systemd` et devrait être en cours d'exécution. Pour vérifier, exécutez la commande suivante :

```shell
sudo systemctl status nginx

# ● nginx.service - A high performance web server and a reverse proxy server
#      Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
#      Active: active (running)

```

Si le statut indique `running`, alors tout est bon. Sinon, vous pouvez démarrer le service en exécutant cette commande :

```shell
sudo systemctl start nginx
```

Enfin, pour une vérification visuelle que tout fonctionne correctement, visitez votre serveur/machine virtuelle avec votre navigateur préféré et vous devriez voir la page d'accueil par défaut de NGINX :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-89.png)

NGINX est généralement installé dans le répertoire `/etc/nginx` et la majorité de notre travail dans les sections à venir se fera ici.

Félicitations ! Vous avez maintenant NGINX opérationnel sur votre serveur/machine virtuelle. Il est maintenant temps de plonger tête la première dans NGINX.

## Introduction aux fichiers de configuration de NGINX

En tant que serveur web, le travail de NGINX est de servir des contenus statiques ou dynamiques aux clients. Mais la manière dont ce contenu va être servi est généralement contrôlée par des fichiers de configuration.

Les fichiers de configuration de NGINX se terminent par l'extension `.conf` et se trouvent généralement dans le répertoire `/etc/nginx/`. Commençons par nous déplacer (`cd`) dans ce répertoire et obtenir une liste de tous les fichiers :

```shell
cd /etc/nginx

ls -lh

# drwxr-xr-x 2 root root 4.0K Apr 21  2020 conf.d
# -rw-r--r-- 1 root root 1.1K Feb  4  2019 fastcgi.conf
# -rw-r--r-- 1 root root 1007 Feb  4  2019 fastcgi_params
# -rw-r--r-- 1 root root 2.8K Feb  4  2019 koi-utf
# -rw-r--r-- 1 root root 2.2K Feb  4  2019 koi-win
# -rw-r--r-- 1 root root 3.9K Feb  4  2019 mime.types
# drwxr-xr-x 2 root root 4.0K Apr 21  2020 modules-available
# drwxr-xr-x 2 root root 4.0K Apr 17 14:42 modules-enabled
# -rw-r--r-- 1 root root 1.5K Feb  4  2019 nginx.conf
# -rw-r--r-- 1 root root  180 Feb  4  2019 proxy_params
# -rw-r--r-- 1 root root  636 Feb  4  2019 scgi_params
# drwxr-xr-x 2 root root 4.0K Apr 17 14:42 sites-available
# drwxr-xr-x 2 root root 4.0K Apr 17 14:42 sites-enabled
# drwxr-xr-x 2 root root 4.0K Apr 17 14:42 snippets
# -rw-r--r-- 1 root root  664 Feb  4  2019 uwsgi_params
# -rw-r--r-- 1 root root 3.0K Feb  4  2019 win-utf
```

Parmi ces fichiers, il devrait y en avoir un nommé **nginx.conf**. C'est le fichier de configuration principal de NGINX. Vous pouvez jeter un œil au contenu de ce fichier en utilisant le programme `cat` :

```shell
cat nginx.conf

# user www-data;
# worker_processes auto;
# pid /run/nginx.pid;
# include /etc/nginx/modules-enabled/*.conf;

# events {
#     worker_connections 768;
#     # multi_accept on;
# }

# http {

#     ##
#     # Paramètres de base
#     ##

#     sendfile on;
#     tcp_nopush on;
#     tcp_nodelay on;
#     keepalive_timeout 65;
#     types_hash_max_size 2048;
#     # server_tokens off;

#     # server_names_hash_bucket_size 64;
#     # server_name_in_redirect off;

#     include /etc/nginx/mime.types;
#     default_type application/octet-stream;

#     ##
#     # Paramètres SSL
#     ##

#     ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Abandon de SSLv3, ref: POODLE
#     ssl_prefer_server_ciphers on;

#     ##
#     # Paramètres de journalisation
#     ##

#     access_log /var/log/nginx/access.log;
#     error_log /var/log/nginx/error.log;

#     ##
#     # Paramètres Gzip
#     ##

#     gzip on;

#     # gzip_vary on;
#     # gzip_proxied any;
#     # gzip_comp_level 6;
#     # gzip_buffers 16 8k;
#     # gzip_http_version 1.1;
#     # gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

#     ##
#     # Configs d'hôtes virtuels
#     ##

#     include /etc/nginx/conf.d/*.conf;
#     include /etc/nginx/sites-enabled/*;
# }


# #mail {
# #    # Voir l'exemple de script d'authentification sur :
# #    # http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
# # 
# #    # auth_http localhost/auth.php;
# #    # pop3_capabilities "TOP" "USER";
# #    # imap_capabilities "IMAP4rev1" "UIDPLUS";
# # 
# #    server {
# #        listen     localhost:110;
# #        protocol   pop3;
# #        proxy      on;
# #    }
# # 
# #    server {
# #        listen     localhost:143;
# #        protocol   imap;
# #        proxy      on;
# #    }
# #}
```

Waouh ! C'est beaucoup de choses. Essayer de comprendre ce fichier dans son état actuel serait un cauchemar. Alors renommons le fichier et créons-en un nouveau vide :

```shell
# renomme le fichier
sudo mv nginx.conf nginx.conf.backup

# crée un nouveau fichier
sudo touch nginx.conf
```

Je vous **déconseille fortement** de modifier le fichier `nginx.conf` original à moins que vous ne sachiez absolument ce que vous faites. À des fins d'apprentissage, vous pouvez le renommer, mais [plus tard](#heading-comment-comprendre-le-fichier-de-configuration-principal-1), je vous montrerai comment vous devriez procéder pour configurer un serveur dans un scénario réel.

## Comment configurer un serveur web de base

Dans cette section du livre, vous allez enfin mettre la main à la pâte en configurant un serveur web statique de base à partir de zéro. L'objectif de cette section est de vous présenter la syntaxe et les concepts fondamentaux des fichiers de configuration NGINX.

### Comment écrire votre premier fichier de configuration

Commencez par ouvrir le fichier `nginx.conf` nouvellement créé à l'aide de l'éditeur de texte [nano](https://www.nano-editor.org/) :

```shell
sudo nano /etc/nginx/nginx.conf
```

Tout au long du livre, j'utiliserai nano comme éditeur de texte. Vous pouvez utiliser quelque chose de plus moderne si vous le souhaitez, mais dans un scénario réel, vous êtes plus susceptible de travailler avec [nano](https://www.nano-editor.org/) ou [vim](https://www.vim.org/) sur les serveurs plutôt qu'autre chose. Utilisez donc ce livre comme une opportunité pour affiner vos compétences sur nano. De plus, le [pense-bête officiel](https://www.nano-editor.org/dist/latest/cheatsheet.html) est là pour que vous puissiez le consulter en cas de besoin.

Après avoir ouvert le fichier, mettez à jour son contenu pour qu'il ressemble à ceci :

```conf
events {

}

http {

    server {

        listen 80;
        server_name nginx-handbook.test;

        return 200 "Bonjour, mon ami!\n";
    }

}
```

Si vous avez de l'expérience dans la création d'API REST, vous pouvez deviner d'après la ligne `return 200 "Bonjour, mon ami!\n";` que le serveur a été configuré pour répondre avec un code d'état 200 et le message "Bonjour, mon ami !".

Ne vous inquiétez pas si vous ne comprenez rien de plus pour le moment. J'expliquerai ce fichier ligne par ligne, mais voyons d'abord cette configuration en action.

### Comment valider et recharger les fichiers de configuration

Après avoir écrit un nouveau fichier de configuration ou mis à jour un ancien, la première chose à faire est de vérifier le fichier pour toute erreur de syntaxe. Le binaire `nginx` inclut une option `-t` pour faire exactement cela.

```shell
sudo nginx -t

# nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
# nginx: configuration file /etc/nginx/nginx.conf test is successful
```

Si vous avez des erreurs de syntaxe, cette commande vous en informera, y compris le numéro de ligne.

Bien que le fichier de configuration soit correct, NGINX ne l'utilisera pas. La façon dont NGINX fonctionne est qu'il lit le fichier de configuration une fois et continue de travailler sur cette base.

Si vous mettez à jour le fichier de configuration, vous devrez alors demander explicitement à NGINX de recharger le fichier de configuration. Il y a deux façons de le faire.

* Vous pouvez redémarrer le service NGINX en exécutant la commande `sudo systemctl restart nginx`.
* Vous pouvez envoyer un signal `reload` à NGINX en exécutant la commande `sudo nginx -s reload`.

L'option `-s` est utilisée pour envoyer divers signaux à NGINX. Les signaux disponibles sont `stop`, `quit`, `reload` et `reopen`. Parmi les deux façons que je viens de mentionner, je préfère la seconde simplement parce qu'elle nécessite moins de frappe.

Une fois que vous avez rechargé le fichier de configuration en exécutant la commande `nginx -s reload`, vous pouvez le voir en action en envoyant une simple requête GET au serveur :

```shell
curl -i http://nginx-handbook.test

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Wed, 21 Apr 2021 10:03:33 GMT
# Content-Type: text/plain
# Content-Length: 18
# Connection: keep-alive

# Bonjour, mon ami!
```

Le serveur répond avec un code d'état 200 et le message attendu. Félicitations d'être arrivé jusqu'ici ! Il est maintenant temps de passer aux explications.

### Comment comprendre les directives et les contextes dans NGINX

Les quelques lignes de code que vous avez écrites ici, bien que semblant simples, introduisent deux des terminologies les plus importantes des fichiers de configuration NGINX. Ce sont les **directives** et les **contextes**.

Techniquement, tout ce qui se trouve dans un fichier de configuration NGINX est une **directive**. Les directives sont de deux types :

* Directives simples
* Directives de bloc

Une directive simple se compose du nom de la directive et des paramètres délimités par des espaces, comme `listen`, `return` et d'autres. Les directives simples se terminent par des points-virgules.

Les directives de bloc sont similaires aux directives simples, sauf qu'au lieu de se terminer par des points-virgules, elles se terminent par une paire d'accolades `{ }` enfermant des instructions supplémentaires.

Une directive de bloc capable de contenir d'autres directives à l'intérieur est appelée un contexte, c'est-à-dire `events`, `http` et ainsi de suite. Il existe quatre contextes principaux dans NGINX :

* `events { }` – Le contexte `events` est utilisé pour définir la configuration globale concernant la manière dont NGINX va gérer les requêtes à un niveau général. Il ne peut y avoir qu'un seul contexte `events` dans un fichier de configuration valide.
* `http { }` – Comme son nom l'indique, le contexte `http` est utilisé pour définir la configuration concernant la manière dont le serveur va gérer spécifiquement les requêtes HTTP et HTTPS. Il ne peut y avoir qu'un seul contexte `http` dans un fichier de configuration valide.
* `server { }` – Le contexte `server` est imbriqué dans le contexte `http` et utilisé pour configurer des serveurs virtuels spécifiques au sein d'un seul hôte. Il peut y avoir plusieurs contextes `server` dans un fichier de configuration valide imbriqués dans le contexte `http`. Chaque contexte `server` est considéré comme un hôte virtuel.
* `main` – Le contexte `main` est le fichier de configuration lui-même. Tout ce qui est écrit en dehors des trois contextes mentionnés précédemment se trouve dans le contexte `main`.

Vous pouvez traiter les contextes dans NGINX comme des portées (scopes) dans d'autres langages de programmation. Il existe également un sentiment d'héritage entre eux. Vous pouvez trouver un [index alphabétique des directives](https://nginx.org/en/docs/dirindex.html) sur la documentation officielle de NGINX.

J'ai déjà mentionné qu'il peut y avoir plusieurs contextes `server` dans un fichier de configuration. Mais lorsqu'une requête atteint le serveur, comment NGINX sait-il lequel de ces contextes doit gérer la requête ?

La directive `listen` est l'un des moyens d'identifier le bon contexte `server` au sein d'une configuration. Considérons le scénario suivant :

```
http {
    server {
        listen 80;
        server_name nginx-handbook.test;

        return 200 "hello from port 80!\n";
    }


    server {
        listen 8080;
        server_name nginx-handbook.test;

        return 200 "hello from port 8080!\n";
    }
}

```

Maintenant, si vous envoyez une requête à http://nginx-handbook.test:80, vous recevrez "hello from port 80!" en réponse. Et si vous envoyez une requête à http://nginx-handbook.test:8080, vous recevrez "hello from port 8080!" en réponse :

```
curl nginx-handbook.test:80

# hello from port 80!

curl nginx-handbook.test:8080

# hello from port 8080!
```

Ces deux blocs serveurs sont comme deux personnes tenant des récepteurs téléphoniques, attendant de répondre lorsqu'une requête atteint l'un de leurs numéros. Leurs numéros sont indiqués par les directives `listen`.

En dehors de la directive `listen`, il y a aussi la directive `server_name`. Considérons le scénario suivant d'une application imaginaire de gestion de bibliothèque :

```
http {
    server {
        listen 80;
        server_name library.test;

        return 200 "your local library!\n";
    }


    server {
        listen 80;
        server_name librarian.library.test;

        return 200 "welcome dear librarian!\n";
    }
}

```

Ceci est un exemple basique de l'idée d'hôtes virtuels. Vous exécutez deux applications distinctes sous des noms de serveur différents sur le même serveur.

Si vous envoyez une requête à http://library.test, vous obtiendrez "your local library!" en réponse. Si vous envoyez une requête à http://librarian.library.test, vous obtiendrez "welcome dear librarian!" en réponse.

```shell
curl http://library.test

# your local library!

curl http://librarian.library.test

# welcome dear librarian!
```

Pour faire fonctionner cette démo sur votre système, vous devrez mettre à jour votre fichier `hosts` pour inclure également ces deux noms de domaine :

```hosts
192.168.20.20   library.test
192.168.20.20   librarian.library.test
```

Enfin, la directive `return` est responsable du renvoi d'une réponse valide à l'utilisateur. Cette directive prend deux paramètres : le code d'état et le message sous forme de chaîne à renvoyer.

### Comment servir du contenu statique avec NGINX

Maintenant que vous avez une bonne compréhension de la manière d'écrire un fichier de configuration de base pour NGINX, améliorons la configuration pour servir des fichiers statiques au lieu de réponses en texte brut.

Pour servir du contenu statique, vous devez d'abord les stocker quelque part sur votre serveur. Si vous listez les fichiers et répertoires à la racine de votre serveur à l'aide de `ls`, vous y trouverez un répertoire appelé `/srv` :

```shell
ls -lh /

# lrwxrwxrwx   1 root    root       7 Apr 16 02:10 bin -> usr/bin
# drwxr-xr-x   3 root    root    4.0K Apr 16 02:13 boot
# drwxr-xr-x  16 root    root    3.8K Apr 21 09:23 dev
# drwxr-xr-x  92 root    root    4.0K Apr 21 09:24 etc
# drwxr-xr-x   4 root    root    4.0K Apr 21 08:04 home
# lrwxrwxrwx   1 root    root       7 Apr 16 02:10 lib -> usr/lib
# lrwxrwxrwx   1 root    root       9 Apr 16 02:10 lib32 -> usr/lib32
# lrwxrwxrwx   1 root    root       9 Apr 16 02:10 lib64 -> usr/lib64
# lrwxrwxrwx   1 root    root      10 Apr 16 02:10 libx32 -> usr/libx32
# drwx------   2 root    root     16K Apr 16 02:15 lost+found
# drwxr-xr-x   2 root    root    4.0K Apr 16 02:10 media
# drwxr-xr-x   2 root    root    4.0K Apr 16 02:10 mnt
# drwxr-xr-x   2 root    root    4.0K Apr 16 02:10 opt
# dr-xr-xr-x 152 root    root       0 Apr 21 09:23 proc
# drwx------   5 root    root    4.0K Apr 21 09:59 root
# drwxr-xr-x  26 root    root     820 Apr 21 09:47 run
# lrwxrwxrwx   1 root    root       8 Apr 16 02:10 sbin -> usr/sbin
# drwxr-xr-x   6 root    root    4.0K Apr 16 02:14 snap
# drwxr-xr-x   2 root    root    4.0K Apr 16 02:10 srv
# dr-xr-xr-x  13 root    root       0 Apr 21 09:23 sys
# drwxrwxrwt  11 root    root    4.0K Apr 21 09:24 tmp
# drwxr-xr-x  15 root    root    4.0K Apr 16 02:12 usr
# drwxr-xr-x   1 vagrant vagrant   38 Apr 21 09:23 vagrant
# drwxr-xr-x  14 root    root    4.0K Apr 21 08:34 var
```

Ce répertoire `/srv` est destiné à contenir des données spécifiques au site qui sont servies par ce système. Maintenant, faites un `cd` dans ce répertoire et clonez le dépôt de code qui accompagne ce livre :

```
cd /srv

sudo git clone https://github.com/fhsinchy/nginx-handbook-projects.git
```

À l'intérieur du répertoire `nginx-handbook-projects`, il devrait y avoir un répertoire appelé `static-demo` contenant quatre fichiers au total :

```shell
ls -lh /srv/nginx-handbook-projects/static-demo

# -rw-r--r-- 1 root root 960 Apr 21 11:27 about.html
# -rw-r--r-- 1 root root 960 Apr 21 11:27 index.html
# -rw-r--r-- 1 root root 46K Apr 21 11:27 mini.min.css
# -rw-r--r-- 1 root root 19K Apr 21 11:27 the-nginx-handbook.jpg
```

Maintenant que vous avez le contenu statique à servir, mettez à jour votre configuration comme suit :

```conf
events {

}

http {

    server {

        listen 80;
        server_name nginx-handbook.test;

        root /srv/nginx-handbook-projects/static-demo;
    }

}

```

Le code est presque le même, sauf que la directive `return` a maintenant été remplacée par une directive `root`. Cette directive est utilisée pour déclarer le répertoire racine d'un site.

En écrivant `root /srv/nginx-handbook-projects/static-demo`, vous dites à NGINX de chercher les fichiers à servir à l'intérieur du répertoire `/srv/nginx-handbook-projects/static-demo` si une requête arrive sur ce serveur. Comme NGINX est un serveur web, il est assez intelligent pour servir le fichier `index.html` par défaut.

Voyons si cela fonctionne ou non. Testez et rechargez le fichier de configuration mis à jour et visitez le serveur. Vous devriez être accueilli par un site HTML quelque peu cassé :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-91.png)

Bien que NGINX ait correctement servi le fichier index.html, à en juger par l'apparence des trois liens de navigation, il semble que le code CSS ne fonctionne pas.

Vous pourriez penser qu'il y a un problème dans le fichier CSS. Mais en réalité, le problème vient du fichier de configuration.

### Gestion des types de fichiers statiques dans NGINX

Pour déboguer le problème auquel vous êtes confronté actuellement, envoyez une requête pour le fichier CSS au serveur :

```shell
curl -I http://nginx-handbook/mini.min.css

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Wed, 21 Apr 2021 12:17:16 GMT
# Content-Type: text/plain
# Content-Length: 46887
# Last-Modified: Wed, 21 Apr 2021 11:27:06 GMT
# Connection: keep-alive
# ETag: "60800c0a-b727"
# Accept-Ranges: bytes
```

Faites attention au **Content-Type** et voyez comment il indique **text/plain** et non **text/css**. Cela signifie que NGINX sert ce fichier comme du texte brut au lieu d'une feuille de style.

Bien que NGINX soit assez intelligent pour trouver le fichier `index.html` par défaut, il est assez limité lorsqu'il s'agit d'interpréter les types de fichiers. Pour résoudre ce problème, mettez à jour votre configuration une fois de plus :

```conf
events {

}

http {

    types {
        text/html html;
        text/css css;
    }

    server {

        listen 80;
        server_name nginx-handbook.test;

        root /srv/nginx-handbook-projects/static-demo;
    }
}
```

Le seul changement que nous avons apporté au code est un nouveau contexte `types` imbriqué dans le bloc `http`. Comme vous l'avez peut-être déjà deviné d'après son nom, ce contexte est utilisé pour configurer les types de fichiers.

En écrivant `text/html html` dans ce contexte, vous dites à NGINX d'analyser comme `text/html` tout fichier se terminant par l'extension `html`.

Vous pourriez penser que configurer le type de fichier CSS devrait suffire car le HTML est déjà analysé correctement – mais non.

Si vous introduisez un contexte `types` dans la configuration, NGINX devient encore plus limité et n'analyse que les fichiers configurés par vous. Donc, si vous ne définissez que `text/css css` dans ce contexte, NGINX commencera à analyser le fichier HTML comme du texte brut.

Validez et rechargez le fichier de config nouvellement mis à jour et visitez à nouveau le serveur. Envoyez une requête pour le fichier CSS une fois de plus, et cette fois le fichier devrait être analysé comme un fichier **text/css** :

```shell
curl -I http://nginx-handbook.test/mini.min.css

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Wed, 21 Apr 2021 12:29:35 GMT
# Content-Type: text/css
# Content-Length: 46887
# Last-Modified: Wed, 21 Apr 2021 11:27:06 GMT
# Connection: keep-alive
# ETag: "60800c0a-b727"
# Accept-Ranges: bytes
```

Visitez le serveur pour une vérification visuelle, et le site devrait avoir une meilleure apparence cette fois-ci :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-92.png)

Si vous avez mis à jour et rechargé le fichier de configuration correctement et que vous voyez toujours l'ancien site, effectuez un rafraîchissement forcé (hard refresh).

### Comment inclure des fichiers de config partiels

Mappé les types de fichiers dans le contexte `types` peut fonctionner pour de petits projets, mais pour des projets plus importants, cela peut être fastidieux et sujet aux erreurs.

NGINX propose une solution à ce problème. Si vous listez à nouveau les fichiers dans le répertoire `/etc/nginx`, vous verrez un fichier nommé `mime.types`.

```shell
ls -lh /etc/nginx

# drwxr-xr-x 2 root root 4.0K Apr 21  2020 conf.d
# -rw-r--r-- 1 root root 1.1K Feb  4  2019 fastcgi.conf
# -rw-r--r-- 1 root root 1007 Feb  4  2019 fastcgi_params
# -rw-r--r-- 1 root root 2.8K Feb  4  2019 koi-utf
# -rw-r--r-- 1 root root 2.2K Feb  4  2019 koi-win
# -rw-r--r-- 1 root root 3.9K Feb  4  2019 mime.types
# drwxr-xr-x 2 root root 4.0K Apr 21  2020 modules-available
# drwxr-xr-x 2 root root 4.0K Apr 17 14:42 modules-enabled
# -rw-r--r-- 1 root root 1.5K Feb  4  2019 nginx.conf
# -rw-r--r-- 1 root root  180 Feb  4  2019 proxy_params
# -rw-r--r-- 1 root root  636 Feb  4  2019 scgi_params
# drwxr-xr-x 2 root root 4.0K Apr 17 14:42 sites-available
# drwxr-xr-x 2 root root 4.0K Apr 17 14:42 sites-enabled
# drwxr-xr-x 2 root root 4.0K Apr 17 14:42 snippets
# -rw-r--r-- 1 root root  664 Feb  4  2019 uwsgi_params
# -rw-r--r-- 1 root root 3.0K Feb  4  2019 win-utf
```

Jetons un coup d'œil au contenu de ce fichier :

```shell
cat /etc/mime.types

# types {
#     text/html                             html htm shtml;
#     text/css                              css;
#     text/xml                              xml;
#     image/gif                             gif;
#     image/jpeg                            jpeg jpg;
#     application/javascript                js;
#     application/atom+xml                  atom;
#     application/rss+xml                   rss;

#     text/mathml                           mml;
#     text/plain                            txt;
#     text/vnd.sun.j2me.app-descriptor      jad;
#     text/vnd.wap.wml                      wml;
#     text/x-component                      htc;

#     image/png                             png;
#     image/tiff                            tif tiff;
#     image/vnd.wap.wbmp                    wbmp;
#     image/x-icon                          ico;
#     image/x-jng                           jng;
#     image/x-ms-bmp                        bmp;
#     image/svg+xml                         svg svgz;
#     image/webp                            webp;

#     application/font-woff                 woff;
#     application/java-archive              jar war ear;
#     application/json                      json;
#     application/mac-binhex40              hqx;
#     application/msword                    doc;
#     application/pdf                       pdf;
#     application/postscript                ps eps ai;
#     application/rtf                       rtf;
#     application/vnd.apple.mpegurl         m3u8;
#     application/vnd.ms-excel              xls;
#     application/vnd.ms-fontobject         eot;
#     application/vnd.ms-powerpoint         ppt;
#     application/vnd.wap.wmlc              wmlc;
#     application/vnd.google-earth.kml+xml  kml;
#     application/vnd.google-earth.kmz      kmz;
#     application/x-7z-compressed           7z;
#     application/x-cocoa                   cco;
#     application/x-java-archive-diff       jardiff;
#     application/x-java-jnlp-file          jnlp;
#     application/x-makeself                run;
#     application/x-perl                    pl pm;
#     application/x-pilot                   prc pdb;
#     application/x-rar-compressed          rar;
#     application/x-redhat-package-manager  rpm;
#     application/x-sea                     sea;
#     application/x-shockwave-flash         swf;
#     application/x-stuffit                 sit;
#     application/x-tcl                     tcl tk;
#     application/x-x509-ca-cert            der pem crt;
#     application/x-xpinstall               xpi;
#     application/xhtml+xml                 xhtml;
#     application/xspf+xml                  xspf;
#     application/zip                       zip;

#     application/octet-stream              bin exe dll;
#     application/octet-stream              deb;
#     application/octet-stream              dmg;
#     application/octet-stream              iso img;
#     application/octet-stream              msi msp msm;

#     application/vnd.openxmlformats-officedocument.wordprocessingml.document    docx;
#     application/vnd.openxmlformats-officedocument.spreadsheetml.sheet          xlsx;
#     application/vnd.openxmlformats-officedocument.presentationml.presentation  pptx;

#     audio/midi                            mid midi kar;
#     audio/mpeg                            mp3;
#     audio/ogg                             ogg;
#     audio/x-m4a                           m4a;
#     audio/x-realaudio                     ra;

#     video/3gpp                            3gpp 3gp;
#     video/mp2t                            ts;
#     video/mp4                             mp4;
#     video/mpeg                            mpeg mpg;
#     video/quicktime                       mov;
#     video/webm                            webm;
#     video/x-flv                           flv;
#     video/x-m4v                           m4v;
#     video/x-mng                           mng;
#     video/x-ms-asf                        asx asf;
#     video/x-ms-wmv                        wmv;
#     video/x-msvideo                       avi;
# }
```

Le fichier contient une longue liste de types de fichiers et leurs extensions. Pour utiliser ce fichier dans votre fichier de configuration, mettez à jour votre configuration comme suit :

```conf
events {

}

http {

    include /etc/nginx/mime.types;

    server {

        listen 80;
        server_name nginx-handbook.test;

        root /srv/nginx-handbook-projects/static-demo;
    }

}
```

L'ancien contexte `types` a maintenant été remplacé par une nouvelle directive `include`. Comme son nom l'indique, cette directive vous permet d'inclure le contenu d'autres fichiers de configuration.

Validez et rechargez le fichier de configuration et envoyez une requête pour le fichier `mini.min.css` une fois de plus :

```shell
curl -I http://nginx-handbook.test/mini.min.css

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Wed, 21 Apr 2021 12:29:35 GMT
# Content-Type: text/css
# Content-Length: 46887
# Last-Modified: Wed, 21 Apr 2021 11:27:06 GMT
# Connection: keep-alive
# ETag: "60800c0a-b727"
# Accept-Ranges: bytes
```

Dans la section ci-dessous sur la compréhension du fichier de configuration principal, je démontrerai comment `include` peut être utilisé pour modulariser vos configurations de serveurs virtuels.

## Routage dynamique dans NGINX

La configuration que vous avez écrite dans la section précédente était une configuration de serveur de contenu statique très simple. Tout ce qu'elle faisait était de faire correspondre un fichier de la racine du site correspondant à l'URI visité par le client et de répondre.

Ainsi, si le client demande des fichiers existant à la racine tels que `index.html`, `about.html` ou `mini.min.css`, NGINX renverra le fichier. Mais si vous visitez une route telle que http://nginx-handbook.test/nothing, il répondra avec la page 404 par défaut :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-93.png)

Dans cette section du livre, vous découvrirez le contexte `location`, les variables, les redirections, les réécritures et la directive `try_files`. Il n'y aura pas de nouveaux projets dans cette section, mais les concepts que vous apprendrez ici seront nécessaires dans les sections à venir.

De plus, la configuration changera très fréquemment dans cette section, n'oubliez donc pas de valider et de recharger le fichier de configuration après chaque mise à jour.

### Correspondances de location

Le premier concept que nous aborderons dans cette section est le contexte `location`. Mettez à jour la configuration comme suit :

```conf
events {

}

http {

    server {

        listen 80;
        server_name nginx-handbook.test;

        location /agatha {
            return 200 "Miss Marple.\nHercule Poirot.\n";
        }
    }
}
```

Nous avons remplacé la directive `root` par un nouveau contexte `location`. Ce contexte est généralement imbriqué dans les blocs `server`. Il peut y avoir plusieurs contextes `location` au sein d'un contexte `server`.

Si vous envoyez une requête à http://nginx-handbook.test/agatha, vous obtiendrez un code de réponse 200 et une liste de personnages créés par [Agatha Christie](https://en.wikipedia.org/wiki/Agatha_Christie).

```shell
curl -i http://nginx-handbook.test/agatha

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Wed, 21 Apr 2021 15:59:07 GMT
# Content-Type: text/plain
# Content-Length: 29
# Connection: keep-alive

# Miss Marple.
# Hercule Poirot.
```

Maintenant, si vous envoyez une requête à http://nginx-handbook.test/agatha-christie, vous obtiendrez la même réponse :

```shell
curl -i http://nginx-handbook.test/agatha-christie

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Wed, 21 Apr 2021 15:59:07 GMT
# Content-Type: text/plain
# Content-Length: 29
# Connection: keep-alive

# Miss Marple.
# Hercule Poirot.
```

Cela se produit parce qu'en écrivant `location /agatha`, vous dites à NGINX de faire correspondre tout URI commençant par "agatha". Ce type de correspondance est appelé une **correspondance de préfixe**.

Pour effectuer une **correspondance exacte**, vous devrez mettre à jour le code comme suit :

```conf
events {

}

http {

    server {

        listen 80;
        server_name nginx-handbook.test;

        location = /agatha {
            return 200 "Miss Marple.\nHercule Poirot.\n";
        }
    }

}
```

L'ajout d'un signe `=` avant l'URI de location demandera à NGINX de ne répondre que si l'URL correspond exactement. Maintenant, si vous envoyez une requête à autre chose que `/agatha`, vous obtiendrez une réponse 404.

```shell
curl -I http://nginx-handbook.test/agatha-christie

# HTTP/1.1 404 Not Found
# Server: nginx/1.18.0 (Ubuntu)
# Date: Wed, 21 Apr 2021 16:14:29 GMT
# Content-Type: text/html
# Content-Length: 162
# Connection: keep-alive

curl -I http://nginx-handbook.test/agatha

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Wed, 21 Apr 2021 16:15:04 GMT
# Content-Type: text/plain
# Content-Length: 29
# Connection: keep-alive
```

Un autre type de correspondance dans NGINX est la **correspondance regex**. En utilisant cette correspondance, vous pouvez vérifier les URL de location par rapport à des expressions régulières complexes.

```conf
events {

}

http {

    server {

        listen 80;
        server_name nginx-handbook.test;

        location ~ /agatha[0-9] {
        	return 200 "Miss Marple.\nHercule Poirot.\n";
        }
    }

}
```

En remplaçant le signe `=` précédemment utilisé par un signe `~`, vous dites à NGINX d'effectuer une correspondance par expression régulière. Définir la location sur `~ /agatha[0-9]` signifie que NGINX ne répondra que s'il y a un chiffre après le mot "agatha" :

```shell
curl -I http://nginx-handbook.test/agatha

# HTTP/1.1 404 Not Found
# Server: nginx/1.18.0 (Ubuntu)
# Date: Wed, 21 Apr 2021 16:14:29 GMT
# Content-Type: text/html
# Content-Length: 162
# Connection: keep-alive

curl -I http://nginx-handbook.test/agatha8

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Wed, 21 Apr 2021 16:15:04 GMT
# Content-Type: text/plain
# Content-Length: 29
# Connection: keep-alive
```

Une correspondance regex est par défaut sensible à la casse, ce qui signifie que si vous mettez en majuscule l'une des lettres, la location ne fonctionnera pas :

```shell
curl -I http://nginx-handbook.test/Agatha8

# HTTP/1.1 404 Not Found
# Server: nginx/1.18.0 (Ubuntu)
# Date: Wed, 21 Apr 2021 16:14:29 GMT
# Content-Type: text/html
# Content-Length: 162
# Connection: keep-alive
```

Pour rendre cela insensible à la casse, vous devrez ajouter un `*` après le signe `~`.

```conf
events {

}

http {

    server {

        listen 80;
        server_name nginx-handbook.test;

        location ~* /agatha[0-9] {
        	return 200 "Miss Marple.\nHercule Poirot.\n";
        }
    }

}
```

Cela dira à NGINX d'ignorer la sensibilité à la casse et de faire correspondre la location de toute façon.

```shell
curl -I http://nginx-handbook.test/agatha8

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Wed, 21 Apr 2021 16:15:04 GMT
# Content-Type: text/plain
# Content-Length: 29
# Connection: keep-alive

curl -I http://nginx-handbook.test/Agatha8

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Wed, 21 Apr 2021 16:15:04 GMT
# Content-Type: text/plain
# Content-Length: 29
# Connection: keep-alive
```

NGINX attribue des valeurs de priorité à ces correspondances, et une correspondance regex a plus de priorité qu'une correspondance de préfixe.

```conf
events {

}

http {

    server {

        listen 80;
        server_name nginx-handbook.test;

		location /Agatha8 {
        	return 200 "prefix matched.\n";
        }
        
        location ~* /agatha[0-9] {
        	return 200 "regex matched.\n";
        }
    }

}
```

Maintenant, si vous envoyez une requête à http://nginx-handbook.test/Agatha8, vous obtiendrez la réponse suivante :

```shell
curl -i http://nginx-handbook.test/Agatha8

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Thu, 22 Apr 2021 08:08:18 GMT
# Content-Type: text/plain
# Content-Length: 15
# Connection: keep-alive

# regex matched.
```

Mais cette priorité peut être un peu modifiée. Le dernier type de correspondance dans NGINX est une **correspondance de préfixe préférentielle**. Pour transformer une correspondance de préfixe en une correspondance préférentielle, vous devez inclure le modificateur `^~` avant l'URI de location :

```conf
events {

}

http {

    server {

        listen 80;
        server_name nginx-handbook.test;

		location ^~ /Agatha8 {
        	return 200 "prefix matched.\n";
        }
        
        location ~* /agatha[0-9] {
        	return 200 "regex matched.\n";
        }
    }

}
```

Maintenant, si vous envoyez une requête à http://nginx-handbook.test/Agatha8, vous obtiendrez la réponse suivante :

```shell
curl -i http://nginx-handbook.test/Agatha8

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Thu, 22 Apr 2021 08:13:24 GMT
# Content-Type: text/plain
# Content-Length: 16
# Connection: keep-alive

# prefix matched.
```

Cette fois, la correspondance de préfixe gagne. Ainsi, la liste de toutes les correspondances par ordre décroissant de priorité est la suivante :

| Correspondance        | Modificateur | 
| --------------------- | ----------- | 
| Exacte                | `=`         | 
| Préfixe préférentiel  | `^~`        | 
| REGEX                 | `~` ou `~*` | 
| Préfixe               | `Aucun`     | 

### Variables dans NGINX

Les variables dans NGINX sont similaires aux variables dans d'autres langages de programmation. La directive `set` peut être utilisée pour déclarer de nouvelles variables n'importe où dans le fichier de configuration :

```conf
set $<variable_name> <variable_value>;

# set name "Farhan"
# set age 25
# set is_working true
```

Les variables peuvent être de trois types :

* Chaîne de caractères (String)
* Entier (Integer)
* Booléen (Boolean)

En plus des variables que vous déclarez, il existe des variables intégrées dans les modules NGINX. Un [index alphabétique des variables](https://nginx.org/en/docs/varindex.html) est disponible dans la documentation officielle.

Pour voir certaines variables en action, mettez à jour la configuration comme suit :

```conf
events {

}

http {

    server {

        listen 80;
        server_name nginx-handbook.test;

        return 200 "Host - $host\nURI - $uri\nArgs - $args\n";
    }

}
```

Maintenant, en envoyant une requête au serveur, vous devriez obtenir une réponse comme celle-ci :

```shell
# curl http://nginx-handbook.test/user?name=Farhan

# Host - nginx-handbook.test
# URI - /user
# Args - name=Farhan
```

Comme vous pouvez le voir, les variables `$host` et `$uri` contiennent respectivement l'adresse racine et l'URI demandé par rapport à la racine. La variable `$args`, comme vous pouvez le voir, contient toutes les chaînes de requête (query strings).

Au lieu d'afficher la forme littérale des chaînes de requête, vous pouvez accéder aux valeurs individuelles en utilisant la variable `$arg`.

```conf
events {

}

http {

    server {

        listen 80;
        server_name nginx-handbook.test;
        
        set $name $arg_name; # $arg_<nom de la query string>

        return 200 "Name - $name\n";
    }

}
```

Maintenant, la réponse du serveur devrait ressembler à ceci :

```shell
curl http://nginx-handbook.test?name=Farhan

# Name - Farhan
```

Les variables que j'ai démontrées ici sont intégrées dans le module [ngx_http_core_module](https://nginx.org/en/docs/http/ngx_http_core_module.html). Pour qu'une variable soit accessible dans la configuration, NGINX doit être construit avec le module intégrant la variable. La construction de NGINX à partir des sources et l'utilisation de modules dynamiques sortent légèrement du cadre de cet article. Mais j'écrirai sûrement à ce sujet sur mon blog.

### Redirections et réécritures

Une redirection dans NGINX est identique aux redirections sur n'importe quelle autre plateforme. Pour démontrer le fonctionnement des redirections, mettez à jour votre configuration pour qu'elle ressemble à ceci :

```conf
events {

}

http {

    include /etc/nginx/mime.types;

    server {

        listen 80;
        server_name nginx-handbook.test;

        root /srv/nginx-handbook-projects/static-demo;

        location = /index_page {
                return 307 /index.html;
        }

        location = /about_page {
                return 307 /about.html;
        }
    }
}
```

Maintenant, si vous envoyez une requête à http://nginx-handbook.test/about_page, vous serez redirigé vers http://nginx-handbook.test/about.html :

```shell
curl -I http://nginx-handbook.test/about_page

# HTTP/1.1 307 Temporary Redirect
# Server: nginx/1.18.0 (Ubuntu)
# Date: Thu, 22 Apr 2021 18:02:04 GMT
# Content-Type: text/html
# Content-Length: 180
# Location: http://nginx-handbook.test/about.html
# Connection: keep-alive
```

Comme vous pouvez le voir, le serveur a répondu avec un code d'état 307 et la location indique http://nginx-handbook.test/about.html. Si vous visitez http://nginx-handbook.test/about_page depuis un navigateur, vous verrez que l'URL changera automatiquement pour http://nginx-handbook.test/about.html.

Une directive `rewrite`, cependant, fonctionne un peu différemment. Elle modifie l'URI en interne, sans en informer l'utilisateur. Pour la voir en action, mettez à jour votre configuration comme suit :

```conf
events {

}

http {

    include /etc/nginx/mime.types;

    server {

        listen 80;
        server_name nginx-handbook.test;

        root /srv/nginx-handbook-projects/static-demo;

        rewrite /index_page /index.html;

        rewrite /about_page /about.html;
    }
}
```

Maintenant, si vous envoyez une requête à l'URI http://nginx-handbook/about_page, vous obtiendrez un code de réponse 200 et le code HTML du fichier about.html en réponse :

```shell
curl -i http://nginx-handbook.test/about_page

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Thu, 22 Apr 2021 18:09:31 GMT
# Content-Type: text/html
# Content-Length: 960
# Last-Modified: Wed, 21 Apr 2021 11:27:06 GMT
# Connection: keep-alive
# ETag: "60800c0a-3c0"
# Accept-Ranges: bytes

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>NGINX Handbook Static Demo</title>
#     <link rel="stylesheet" href="mini.min.css">
#     <style>
#         .container {
#             max-width: 1024px;
#             margin-left: auto;
#             margin-right: auto;
#         }
# 
#         h1 {
#             text-align: center;
#         }
#     </style>
# </head>
# <body class="container">
#     <header>
#         <a class="button" href="index.html">Index</a>
#         <a class="button" href="about.html">About</a>
#         <a class="button" href="nothing">Nothing</a>
#     </header>
#     <div class="card fluid">
#         <img src="./the-nginx-handbook.jpg" alt="The NGINX Handbook Cover Image">
#     </div>
#     <div class="card fluid">
#         <h1>this is the <strong>about.html</strong> file</h1>
#     </div>
# </body>
# </html>
```

Et si vous visitez l'URI à l'aide d'un navigateur, vous verrez la page about.html tandis que l'URL reste inchangée :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/rewrite.png)

En dehors de la manière dont le changement d'URI est géré, il existe une autre différence entre une redirection et une réécriture. Lorsqu'une réécriture se produit, le contexte `server` est réévalué par NGINX. Ainsi, une réécriture est une opération plus coûteuse qu'une redirection.

### Comment essayer plusieurs fichiers

Le dernier concept que je vais montrer dans cette section est la directive `try_files`. Au lieu de répondre avec un seul fichier, la directive `try_files` vous permet de vérifier l'existence de plusieurs fichiers.

```conf
events {

}

http {

    include /etc/nginx/mime.types;

    server {

        listen 80;
        server_name nginx-handbook.test;

        root /srv/nginx-handbook-projects/static-demo;

        try_files /the-nginx-handbook.jpg /not_found;

        location /not_found {
                return 404 "sadly, you've hit a brick wall buddy!\n";
        }
    }
}
```

Comme vous pouvez le voir, une nouvelle directive `try_files` a été ajoutée. En écrivant `try_files /the-nginx-handbook.jpg /not_found;`, vous demandez à NGINX de chercher un fichier nommé the-nginx-handbook.jpg à la racine chaque fois qu'une requête est reçue. S'il n'existe pas, allez à l'emplacement `/not_found`.

Ainsi, maintenant, si vous visitez le serveur, vous verrez l'image :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-94.png)

Mais si vous mettez à jour la configuration pour essayer un fichier inexistant tel que blackhole.jpg, vous obtiendrez une réponse 404 avec le message "sadly, you've hit a brick wall buddy!".

Le problème avec l'écriture d'une directive `try_files` de cette manière est que peu importe l'URL que vous visitez, tant qu'une requête est reçue par le serveur et que le fichier the-nginx-handbook.jpg est trouvé sur le disque, NGINX le renverra.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/try-files.png)

C'est pourquoi `try_files` est souvent utilisé avec la variable NGINX `$uri`.

```conf
events {

}

http {

    include /etc/nginx/mime.types;

    server {

        listen 80;
        server_name nginx-handbook.test;

        root /srv/nginx-handbook-projects/static-demo;

        try_files $uri /not_found;

        location /not_found {
                return 404 "sadly, you've hit a brick wall buddy!\n";
        }
    }
}
```

En écrivant `try_files $uri /not_found;`, vous demandez à NGINX d'essayer d'abord l'URI demandé par le client. S'il ne le trouve pas, essayez le suivant.

Ainsi, maintenant, si vous visitez http://nginx-handbook.test/index.html, vous devriez obtenir l'ancienne page index.html. Il en va de même pour la page about.html :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-95.png)

Mais si vous demandez un fichier qui n'existe pas, vous obtiendrez la réponse de l'emplacement `/not_found` :

```shell
curl -i http://nginx-handbook.test/nothing

# HTTP/1.1 404 Not Found
# Server: nginx/1.18.0 (Ubuntu)
# Date: Thu, 22 Apr 2021 20:01:57 GMT
# Content-Type: text/plain
# Content-Length: 38
# Connection: keep-alive

# sadly, you've hit a brick wall buddy!
```

Une chose que vous avez peut-être déjà remarquée est que si vous visitez la racine du serveur http://nginx-handbook.test, vous obtenez la réponse 404.

C'est parce que lorsque vous atteignez la racine du serveur, la variable `$uri` ne correspond à aucun fichier existant, donc NGINX vous sert l'emplacement de secours. Si vous voulez résoudre ce problème, mettez à jour votre configuration comme suit :

```conf
events {

}

http {

    include /etc/nginx/mime.types;

    server {

        listen 80;
        server_name nginx-handbook.test;

        root /srv/nginx-handbook-projects/static-demo;

        try_files $uri $uri/ /not_found;

        location /not_found {
                return 404 "sadly, you've hit a brick wall buddy!\n";
        }
    }
}
```

En écrivant `try_files $uri $uri/ /not_found;`, vous demandez à NGINX d'essayer d'abord l'URI demandé. Si cela ne fonctionne pas, essayez l'URI demandé en tant que répertoire, et chaque fois que NGINX aboutit dans un répertoire, il commence automatiquement à chercher un fichier index.html.

Maintenant, si vous visitez le serveur, vous devriez obtenir le fichier index.html correctement :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-95.png)

La directive `try_files` est le genre de directive qui peut être utilisée dans un certain nombre de variations. Dans les sections à venir, vous rencontrerez quelques autres variations, mais je vous suggère de faire quelques recherches sur Internet concernant les différentes utilisations de cette directive par vous-même.

## Journalisation dans NGINX

Par défaut, les fichiers journaux (logs) de NGINX sont situés dans `/var/log/nginx`. Si vous listez le contenu de ce répertoire, vous verrez peut-être quelque chose comme ceci :

```shell
ls -lh /var/log/nginx/

# -rw-r----- 1 www-data adm     0 Apr 25 07:34 access.log
# -rw-r----- 1 www-data adm     0 Apr 25 07:34 error.log
```

Commençons par vider les deux fichiers.

```shell
# supprime les anciens fichiers
sudo rm /var/log/nginx/access.log /var/log/nginx/error.log

# crée de nouveaux fichiers
sudo touch /var/log/nginx/access.log /var/log/nginx/error.log

# réouvre les fichiers de log
sudo nginx -s reopen
```

Si vous n'envoyez pas de signal `reopen` à NGINX, il continuera à écrire les logs dans les flux précédemment ouverts et les nouveaux fichiers resteront vides.

Maintenant, pour créer une entrée dans le journal d'accès (access log), envoyez une requête au serveur.

```
curl -I http://nginx-handbook.test

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Sun, 25 Apr 2021 08:35:59 GMT
# Content-Type: text/html
# Content-Length: 960
# Last-Modified: Sun, 25 Apr 2021 08:35:33 GMT
# Connection: keep-alive
# ETag: "608529d5-3c0"
# Accept-Ranges: bytes

sudo cat /var/log/nginx/access.log 

# 192.168.20.20 - - [25/Apr/2021:08:35:59 +0000] "HEAD / HTTP/1.1" 200 0 "-" "curl/7.68.0"
```

Comme vous pouvez le voir, une nouvelle entrée a été ajoutée au fichier access.log. Toute requête au serveur sera enregistrée dans ce fichier par défaut. Mais nous pouvons changer ce comportement en utilisant la directive `access_log`.

```conf
events {

}

http {

    include /etc/nginx/mime.types;

    server {

        listen 80;
        server_name nginx-handbook.test;
        
        location / {
            return 200 "this will be logged to the default file.\n";
        }
        
        location = /admin {
            access_log /var/logs/nginx/admin.log;
            
            return 200 "this will be logged in a separate file.\n";
        }
        
        location = /no_logging {
            access_log off;
            
            return 200 "this will not be logged.\n";
        }
    }
}
```

La première directive `access_log` à l'intérieur du bloc de location /admin demande à NGINX d'écrire tout journal d'accès de cet URI dans le fichier `/var/logs/nginx/admin.log`. La seconde, à l'intérieur de la location /no_logging, désactive complètement les journaux d'accès pour cette location.

Validez et rechargez la configuration. Maintenant, si vous envoyez des requêtes à ces emplacements et inspectez les fichiers journaux, vous devriez voir quelque chose comme ceci :

```shell
curl http://nginx-handbook.test/no_logging
# this will not be logged

sudo cat /var/log/nginx/access.log
# vide

curl http://nginx-handbook.test/admin
# this will be logged in a separate file.

sudo cat /var/log/nginx/access.log
# vide

sudo cat /var/log/nginx/admin.log 
# 192.168.20.20 - - [25/Apr/2021:11:13:53 +0000] "GET /admin HTTP/1.1" 200 40 "-" "curl/7.68.0"

curl  http://nginx-handbook.test/
# this will be logged to the default file.

sudo cat /var/log/nginx/access.log 
# 192.168.20.20 - - [25/Apr/2021:11:15:14 +0000] "GET / HTTP/1.1" 200 41 "-" "curl/7.68.0"
```

Le fichier error.log, quant à lui, contient les journaux d'erreurs. Pour créer une entrée dans le error.log, vous devrez faire planter NGINX. Pour ce faire, mettez à jour votre configuration comme suit :

```conf
events {

}

http {

    include /etc/nginx/mime.types;

    server {

        listen 80;
        server_name nginx-handbook.test;

        return 200 "..." "...";
    }

}
```

Comme vous le savez, la directive `return` ne prend que deux paramètres – mais nous en avons donné trois ici. Maintenant, essayez de recharger la configuration et vous recevrez un message d'erreur :

```shell
sudo nginx -s reload

# nginx: [emerg] invalid number of arguments in "return" directive in /etc/nginx/nginx.conf:14
```

Vérifiez le contenu du journal d'erreurs et le message devrait également y être présent :

```shell
sudo cat /var/log/nginx/error.log 

# 2021/04/25 08:35:45 [notice] 4169#4169: signal process started
# 2021/04/25 10:03:18 [emerg] 8434#8434: invalid number of arguments in "return" directive in /etc/nginx/nginx.conf:14
```

Les messages d'erreur ont des niveaux. Une entrée `notice` dans le journal d'erreurs est inoffensive, mais une entrée `emerg` ou d'urgence doit être traitée immédiatement.

Il existe huit niveaux de messages d'erreur :

* `debug` – Informations de débogage utiles pour aider à déterminer où se situe le problème.
* `info` – Messages d'information qui ne sont pas nécessaires à lire mais qui peuvent être bons à savoir.
* `notice` – Quelque chose de normal s'est produit et mérite d'être noté.
* `warn` – Quelque chose d'inattendu s'est produit, mais n'est pas une cause d'inquiétude.
* `error` – Quelque chose a échoué.
* `crit` – Il y a des problèmes qui doivent être traités de manière critique.
* `alert` – Une action immédiate est requise.
* `emerg` – Le système est dans un état inutilisable et nécessite une attention immédiate.

Par défaut, NGINX enregistre tous les niveaux de messages. Vous pouvez outrepasser ce comportement en utilisant la directive `error_log`. Si vous souhaitez définir le niveau minimum d'un message à `warn`, mettez à jour votre fichier de configuration comme suit :

```conf
events {

}

http {

    include /etc/nginx/mime.types;

    server {

        listen 80;
        server_name nginx-handbook.test;
	
    	error_log /var/log/error.log warn;

        return 200 "..." "...";
    }

}
```

Validez et rechargez la configuration, et à partir de maintenant, seuls les messages de niveau `warn` ou supérieur seront enregistrés.

```shell
cat /var/log/nginx/error.log

# 2021/04/25 11:27:02 [emerg] 12769#12769: invalid number of arguments in "return" directive in /etc/nginx/nginx.conf:16
```

Contrairement à la sortie précédente, il n'y a pas d'entrées `notice` ici. `emerg` est une erreur de niveau supérieur à `warn` et c'est pourquoi elle a été enregistrée.

Pour la plupart des projets, laisser la configuration d'erreur telle quelle devrait convenir. La seule suggestion que j'ai est de définir le niveau d'erreur minimum sur `warn`. De cette façon, vous n'aurez pas à regarder des entrées inutiles dans le journal d'erreurs.

Mais si vous voulez en savoir plus sur la personnalisation de la journalisation dans NGINX, ce [lien](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/) vers la documentation officielle peut vous aider.

## Comment utiliser NGINX comme reverse proxy

Lorsqu'il est configuré comme un reverse proxy, NGINX se situe entre le client et un serveur back-end. Le client envoie des requêtes à NGINX, puis NGINX transmet la requête au back-end.

Une fois que le serveur back-end a fini de traiter la requête, il la renvoie à NGINX. À son tour, NGINX renvoie la réponse au client.

Pendant tout le processus, le client n'a aucune idée de qui traite réellement la requête. Cela semble compliqué à l'écrit, mais une fois que vous le ferez par vous-même, vous verrez à quel point NGINX rend cela facile.

Voyons un exemple très basique et peu pratique de reverse proxy :

```conf
events {

}

http {

    include /etc/nginx/mime.types;

    server {
        listen 80;
        server_name nginx.test;

        location / {
                proxy_pass "https://nginx.org/";
        }
    }
}

```

En plus de valider et de recharger la configuration, vous devrez également ajouter cette adresse à votre fichier `hosts` pour faire fonctionner cette démo sur votre système :

```hosts
192.168.20.20   nginx.test
```

Maintenant, si vous visitez http://nginx.test, vous serez accueilli par le site original [https://nginx.org](https://nginx.org) tandis que l'URI reste inchangé.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/nginx-org-proxy.png)

Vous devriez même pouvoir naviguer sur le site dans une certaine mesure. Si vous visitez http://nginx.test/en/docs/, vous devriez obtenir la page [http://nginx.org/en/docs/](http://nginx.org/en/docs/) en réponse.

Ainsi, comme vous pouvez le voir, à un niveau de base, la directive `proxy_pass` transmet simplement la requête d'un client à un serveur tiers et renvoie la réponse au client via le reverse proxy.

### Node.js avec NGINX

Maintenant que vous savez comment configurer un serveur reverse proxy de base, vous pouvez servir une application Node.js via le reverse proxy de NGINX. J'ai ajouté une application de démonstration dans le dépôt qui accompagne cet article.

> Je suppose que vous avez de l'expérience avec Node.js et que vous savez comment démarrer une application Node.js en utilisant PM2.

Si vous avez déjà cloné le dépôt dans `/srv/nginx-handbook-projects`, alors le projet `node-js-demo` devrait être disponible dans le répertoire `/srv/nginx-handbook-projects/node-js-demo`.

Pour que cette démo fonctionne, vous devrez installer Node.js sur votre serveur. Vous pouvez le faire en suivant les instructions trouvées [ici](https://github.com/nodesource/distributions#debinstall).

L'application de démonstration est un simple serveur HTTP qui répond avec un code d'état 200 et une charge utile JSON. Vous pouvez démarrer l'application en exécutant simplement `node app.js`, mais une meilleure façon est d'utiliser [PM2](https://pm2.keymetrics.io).

Pour ceux d'entre vous qui ne le savent pas, PM2 est un gestionnaire de processus daemon largement utilisé en production pour les applications Node.js. Si vous voulez en savoir plus, ce [lien](https://pm2.keymetrics.io/docs/usage/quick-start/) peut vous aider.

Installez PM2 globalement en exécutant `sudo npm install -g pm2`. Une fois l'installation terminée, exécutez la commande suivante tout en étant à l'intérieur du répertoire `/srv/nginx-handbook-projects/node-js-demo` :

```shell
pm2 start app.js

# [PM2] Processus démarré avec succès
# ┌────┬────────────────────┬──────────┬──────┬───────────┬──────────┬──────────┐
# │ id │ name               │ mode     │ ↺    │ status    │ cpu      │ memory   │
# ├────┼────────────────────┼──────────┼──────┼───────────┼──────────┼──────────┤
# │ 0  │ app                │ fork     │ 0    │ online    │ 0%       │ 21.2mb   │
# └────┴────────────────────┴──────────┴──────┴───────────┴──────────┴──────────┘
```

Alternativement, vous pouvez également faire `pm2 start /srv/nginx-handbook-projects/node-js-demo/app.js` de n'importe où sur le serveur. Vous pouvez arrêter l'application en exécutant la commande `pm2 stop app`.

L'application devrait maintenant être en cours d'exécution mais ne devrait pas être accessible de l'extérieur du serveur. Pour vérifier si l'application fonctionne ou non, envoyez une requête GET à http://localhost:3000 depuis l'intérieur de votre serveur :

```shell
curl -i localhost:3000

# HTTP/1.1 200 OK
# X-Powered-By: Express
# Content-Type: application/json; charset=utf-8
# Content-Length: 62
# ETag: W/"3e-XRN25R5fWNH2Tc8FhtUcX+RZFFo"
# Date: Sat, 24 Apr 2021 12:09:55 GMT
# Connection: keep-alive
# Keep-Alive: timeout=5

# { "status": "success", "message": "You're reading The NGINX Handbook!" }
```

Si vous obtenez une réponse 200, alors le serveur fonctionne correctement. Maintenant, pour configurer NGINX en tant que reverse proxy, ouvrez votre fichier de configuration et mettez à jour son contenu comme suit :

```conf
events {

}
  
http {
    listen 80;
    server_name nginx-handbook.test

    location / {
        proxy_pass http://localhost:3000;
    }
}
```

Rien de nouveau à expliquer ici. Vous transmettez simplement la requête reçue à l'application Node.js s'exécutant sur le port 3000. Maintenant, si vous envoyez une requête au serveur depuis l'extérieur, vous devriez obtenir une réponse comme celle-ci :

```shell
curl -i http://nginx-handbook.test

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Sat, 24 Apr 2021 14:58:01 GMT
# Content-Type: application/json
# Transfer-Encoding: chunked
# Connection: keep-alive

# { "status": "success", "message": "You're reading The NGINX Handbook!" }
```

Bien que cela fonctionne pour un serveur de base comme celui-ci, vous devrez peut-être ajouter quelques directives supplémentaires pour le faire fonctionner dans un scénario réel en fonction des exigences de votre application.

Par exemple, si votre application gère des connexions web socket, vous devriez alors mettre à jour la configuration comme suit :

```conf
events {

}
  
http {
    listen 80;
    server_name nginx-handbook.test

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
    }
}
```

La directive `proxy_http_version` définit la version HTTP pour le serveur. Par défaut, c'est 1.0, mais le web socket nécessite qu'elle soit au moins 1.1. La directive `proxy_set_header` est utilisée pour définir un en-tête sur le serveur back-end. La syntaxe générique de cette directive est la suivante :

```conf
proxy_set_header <nom de l'en-tête> <valeur de l'en-tête>
```

Ainsi, en écrivant `proxy_set_header Upgrade $http_upgrade;`, vous demandez à NGINX de transmettre la valeur de la variable `$http_upgrade` en tant qu'en-tête nommé `Upgrade` – de même pour l'en-tête `Connection`.

Si vous souhaitez en savoir plus sur le proxying de web sockets, ce [lien](https://nginx.org/en/docs/http/websocket.html) vers la documentation officielle de NGINX peut vous aider.

Selon les en-têtes requis par votre application, vous devrez peut-être en définir davantage. Mais la configuration mentionnée ci-dessus est très couramment utilisée pour servir des applications Node.js.

### PHP avec NGINX

PHP et NGINX vont ensemble comme le pain et le beurre. Après tout, le E et le P dans la pile LEMP signifient NGINX et PHP.

> Je suppose que vous avez de l'expérience avec PHP et que vous savez comment exécuter une application PHP.

J'ai déjà inclus une application PHP de démonstration dans le dépôt qui accompagne cet article. Si vous l'avez déjà cloné dans le répertoire `/srv/nginx-handbook-projects`, alors l'application devrait se trouver dans `/srv/nginx-handbook-projects/php-demo`.

Pour que cette démo fonctionne, vous devrez installer un paquet appelé PHP-FPM. Pour installer le paquet, vous pouvez exécuter la commande suivante :

```shell
sudo apt install php-fpm -y
```

Pour tester l'application, démarrez un serveur PHP en exécutant la commande suivante tout en étant à l'intérieur du répertoire `/srv/nginx-handbook-projects/php-demo` :

```shell
php -S localhost:8000

# [Sat Apr 24 16:17:36 2021] PHP 7.4.3 Development Server (http://localhost:8000) started
```

Alternativement, vous pouvez également faire `php -S localhost:8000 /srv/nginx-handbook-projects/php-demo/index.php` de n'importe où sur le serveur.

L'application devrait s'exécuter sur le port 8000 mais elle ne peut pas être accédée de l'extérieur du serveur. Pour vérifier, envoyez une requête GET à http://localhost:8000 depuis l'intérieur de votre serveur :

```shell
curl -I localhost:8000

# HTTP/1.1 200 OK
# Host: localhost:8000
# Date: Sat, 24 Apr 2021 16:22:42 GMT
# Connection: close
# X-Powered-By: PHP/7.4.3
# Content-type: application/json

# {"status":"success","message":"You're reading The NGINX Handbook!"}
```

Si vous obtenez une réponse 200, alors le serveur fonctionne correctement. Tout comme la configuration Node.js, vous pouvez maintenant simplement `proxy_pass` les requêtes vers localhost:8000 – mais avec PHP, il existe une meilleure façon.

La partie FPM dans PHP-FPM signifie FastCGI Process Module. FastCGI est un protocole tout comme HTTP pour l'échange de données binaires. Ce protocole est légèrement plus rapide que HTTP et offre une meilleure sécurité.

Pour utiliser FastCGI au lieu de HTTP, mettez à jour votre configuration comme suit :

```conf
events {

}

http {

      include /etc/nginx/mime.types;

      server {

          listen 80;
          server_name nginx-handbook.test;
          root /srv/nginx-handbook-projects/php-demo;

          index index.php;

          location / {
              try_files $uri $uri/ =404;
          }

          location ~ \.php$ {
              fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
              fastcgi_param REQUEST_METHOD $request_method;
              fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
      }
   }
}
```

Commençons par la nouvelle directive `index`. Comme vous le savez, NGINX cherche par défaut un fichier index.html à servir. Mais dans le projet de démonstration, il s'appelle index.php. Ainsi, en écrivant `index index.php`, vous demandez à NGINX d'utiliser le fichier index.php comme racine à la place.

Cette directive peut accepter plusieurs paramètres. Si vous écrivez quelque chose comme `index index.php index.html`, NGINX cherchera d'abord index.php. S'il ne trouve pas ce fichier, il cherchera un fichier index.html.

La directive `try_files` à l'intérieur du premier contexte `location` est la même que celle que vous avez vue dans une section précédente. Le `=404` à la fin indique l'erreur à renvoyer si aucun des fichiers n'est trouvé.

Le deuxième bloc `location` est l'endroit où la magie principale opère. Comme vous pouvez le voir, nous avons remplacé la directive `proxy_pass` par une nouvelle `fastcgi_pass`. Comme son nom l'indique, elle est utilisée pour transmettre une requête à un service FastCGI.

Le service PHP-FPM s'exécute par défaut sur le port 9000 de l'hôte. Ainsi, au lieu d'utiliser une socket Unix comme je l'ai fait ici, vous pouvez transmettre la requête directement à `http://localhost:9000`. Mais l'utilisation d'une socket Unix est plus sécurisée.

Si vous avez plusieurs versions de PHP-FPM installées, vous pouvez simplement lister tous les emplacements des fichiers socket en exécutant la commande suivante :

```shell
sudo find / -name *fpm.sock

# /run/php/php7.4-fpm.sock
# /run/php/php-fpm.sock
# /etc/alternatives/php-fpm.sock
# /var/lib/dpkg/alternatives/php-fpm.sock
```

Le fichier `/run/php/php-fpm.sock` fait référence à la dernière version de PHP-FPM installée sur votre système. Je préfère utiliser celui avec le numéro de version. De cette façon, même si PHP-FPM est mis à jour, je serai certain de la version que j'utilise.

Contrairement à la transmission de requêtes via HTTP, la transmission de requêtes via FPM nécessite que nous transmettions des informations supplémentaires.

La manière générale de transmettre des informations supplémentaires au service FPM est d'utiliser la directive `fastcgi_param`. Au minimum, vous devrez transmettre la méthode de requête et le nom du script au service back-end pour que le proxying fonctionne.

La ligne `fastcgi_param REQUEST_METHOD $request_method;` transmet la méthode de requête au back-end et la ligne `fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;` transmet l'emplacement exact du script PHP à exécuter.

À ce stade, votre configuration devrait fonctionner. Pour la tester, visitez votre serveur et vous devriez être accueilli par quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/500-on-fastcgi.png)

Eh bien, c'est bizarre. Une erreur 500 signifie que NGINX a planté pour une raison quelconque. C'est là que les journaux d'erreurs peuvent être utiles. Jetons un coup d'œil à la dernière entrée du fichier error.log :

```shell
tail -n 1 /var/log/nginx/error.log

# 2021/04/24 17:15:17 [crit] 17691#17691: *21 connect() to unix:/var/run/php/php7.4-fpm.sock failed (13: Permission denied) while connecting to upstream, client: 192.168.20.20, server: nginx-handbook.test, request: "GET / HTTP/1.1", upstream: "fastcgi://unix:/var/run/php/php7.4-fpm.sock:", host: "nginx-handbook.test"
```

Il semble que le processus NGINX se voit refuser la permission d'accéder au processus PHP-FPM.

L'une des principales raisons d'obtenir une erreur de permission refusée est une discordance d'utilisateur. Jetez un œil à l'utilisateur possédant le worker process NGINX.

```shell
ps aux | grep nginx

# root         677  0.0  0.4   8892  4260 ?        Ss   14:31   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
# nobody     17691  0.0  0.3   9328  3452 ?        S    17:09   0:00 nginx: worker process
# vagrant    18224  0.0  0.2   8160  2552 pts/0    S+   17:19   0:00 grep --color=auto nginx
```

Comme vous pouvez le voir, le processus appartient actuellement à `nobody`. Inspectez maintenant le processus PHP-FPM.

```shell
# ps aux | grep php

# root       14354  0.0  1.8 195484 18924 ?        Ss   16:11   0:00 php-fpm: master process (/etc/php/7.4/fpm/php-fpm.conf)
# www-data   14355  0.0  0.6 195872  6612 ?        S    16:11   0:00 php-fpm: pool www
# www-data   14356  0.0  0.6 195872  6612 ?        S    16:11   0:00 php-fpm: pool www
# vagrant    18296  0.0  0.0   8160   664 pts/0    S+   17:20   0:00 grep --color=auto php
```

Ce processus, en revanche, appartient à l'utilisateur `www-data`. C'est pourquoi NGINX se voit refuser l'accès à ce processus.

Pour résoudre ce problème, mettez à jour votre configuration comme suit :

```conf
user www-data;

events {

}

http {

      include /etc/nginx/mime.types;

      server {

          listen 80;
          server_name nginx-handbook.test;
          root /srv/nginx-handbook-projects/php-demo;

          index index.php;

          location / {
              try_files $uri $uri/ =404;
          }

          location ~ \.php$ {
              fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
              fastcgi_param REQUEST_METHOD $request_method;
              fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
      }
   }
}
```

La directive `user` est responsable de la définition du propriétaire des worker processes NGINX. Inspectez maintenant à nouveau le processus NGINX :

```shell
# ps aux | grep nginx

# root         677  0.0  0.4   8892  4264 ?        Ss   14:31   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
# www-data   20892  0.0  0.3   9292  3504 ?        S    18:10   0:00 nginx: worker process
# vagrant    21294  0.0  0.2   8160  2568 pts/0    S+   18:18   0:00 grep --color=auto nginx
```

Sans aucun doute, le processus appartient maintenant à l'utilisateur `www-data`. Envoyez une requête à votre serveur pour vérifier s'il fonctionne ou non :

```shell
# curl -i http://nginx-handbook.test

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Sat, 24 Apr 2021 18:22:24 GMT
# Content-Type: application/json
# Transfer-Encoding: chunked
# Connection: keep-alive

# {"status":"success","message":"You're reading The NGINX Handbook!"}
```

Si vous obtenez un code d'état 200 avec une charge utile JSON, vous êtes prêt.

Cette configuration simple convient à l'application de démonstration, mais dans les projets réels, vous devrez transmettre des paramètres supplémentaires.

Pour cette raison, NGINX inclut une configuration partielle appelée `fastcgi_params`. Ce fichier contient une liste des paramètres FastCGI les plus courants.

```shell
cat /etc/nginx/fastcgi_params

# fastcgi_param  QUERY_STRING       $query_string;
# fastcgi_param  REQUEST_METHOD     $request_method;
# fastcgi_param  CONTENT_TYPE       $content_type;
# fastcgi_param  CONTENT_LENGTH     $content_length;

# fastcgi_param  SCRIPT_NAME        $fastcgi_script_name;
# fastcgi_param  REQUEST_URI        $request_uri;
# fastcgi_param  DOCUMENT_URI       $document_uri;
# fastcgi_param  DOCUMENT_ROOT      $document_root;
# fastcgi_param  SERVER_PROTOCOL    $server_protocol;
# fastcgi_param  REQUEST_SCHEME     $scheme;
# fastcgi_param  HTTPS              $https if_not_empty;

# fastcgi_param  GATEWAY_INTERFACE  CGI/1.1;
# fastcgi_param  SERVER_SOFTWARE    nginx/$nginx_version;

# fastcgi_param  REMOTE_ADDR        $remote_addr;
# fastcgi_param  REMOTE_PORT        $remote_port;
# fastcgi_param  SERVER_ADDR        $server_addr;
# fastcgi_param  SERVER_PORT        $server_port;
# fastcgi_param  SERVER_NAME        $server_name;

# PHP uniquement, requis si PHP a été construit avec --enable-force-cgi-redirect
# fastcgi_param  REDIRECT_STATUS    200;
```

Comme vous pouvez le voir, ce fichier contient également le paramètre `REQUEST_METHOD`. Au lieu de le transmettre manuellement, vous pouvez simplement inclure ce fichier dans votre configuration :

```conf
user www-data;

events {

}

http {

      include /etc/nginx/mime.types;

      server {

          listen 80;
          server_name nginx-handbook.test;
          root /srv/nginx-handbook-projects/php-demo;

          index index.php;

          location / {
              try_files $uri $uri/ =404;
          }

          location ~ \.php$ {
              fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
              fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
              include /etc/nginx/fastcgi_params;
      }
   }
}
```

Votre serveur devrait se comporter exactement de la même manière. En plus du fichier `fastcgi_params`, vous pouvez également rencontrer le fichier `fastcgi.conf` qui contient un ensemble de paramètres légèrement différent. Je vous suggère d'éviter cela en raison de certaines incohérences dans son comportement.

## Comment utiliser NGINX comme équilibreur de charge

Grâce à la conception de reverse proxy de NGINX, vous pouvez facilement le configurer comme un équilibreur de charge (load balancer).

J'ai déjà ajouté une démo au dépôt qui accompagne cet article. Si vous avez déjà cloné le dépôt dans le répertoire `/srv/nginx-handbook-projects/`, alors la démo devrait se trouver dans le répertoire `/srv/nginx-handbook-projects/load-balancer-demo/`.

Dans un scénario réel, l'équilibrage de charge peut être requis sur des projets à grande échelle répartis sur plusieurs serveurs. Mais pour cette simple démo, j'ai créé trois serveurs Node.js très simples répondant avec un numéro de serveur et un code d'état 200.

Pour que cette démo fonctionne, vous aurez besoin de Node.js installé sur le serveur. Vous pouvez trouver des instructions dans ce [lien](https://github.com/nodesource/distributions#debinstall) pour vous aider à l'installer.

En plus de cela, vous aurez également besoin de [PM2](https://pm2.keymetrics.io/) pour daemoniser les serveurs Node.js fournis dans cette démo.

Si vous ne l'avez pas encore fait, installez PM2 en exécutant `sudo npm install -g pm2`. Une fois l'installation terminée, exécutez les commandes suivantes pour démarrer les trois serveurs Node.js :

```shell
pm2 start /srv/nginx-handbook-projects/load-balancer-demo/server-1.js

pm2 start /srv/nginx-handbook-projects/load-balancer-demo/server-2.js

pm2 start /srv/nginx-handbook-projects/load-balancer-demo/server-3.js

pm2 list

# ┌────┬────────────────────┬──────────┬──────┬───────────┬──────────┬──────────┐
# │ id │ name               │ mode     │ ↺    │ status    │ cpu      │ memory   │
# ├────┼────────────────────┼──────────┼──────┼───────────┼──────────┼──────────┤
# │ 0  │ server-1           │ fork     │ 0    │ online    │ 0%       │ 37.4mb   │
# │ 1  │ server-2           │ fork     │ 0    │ online    │ 0%       │ 37.2mb   │
# │ 2  │ server-3           │ fork     │ 0    │ online    │ 0%       │ 37.1mb   │
# └────┴────────────────────┴──────────┴──────┴───────────┴──────────┴──────────┘
```

Trois serveurs Node.js devraient s'exécuter respectivement sur localhost:3001, localhost:3002 et localhost:3003.

Maintenant, mettez à jour votre configuration comme suit :

```conf
events {

}

http {

    upstream backend_servers {
        server localhost:3001;
        server localhost:3002;
        server localhost:3003;
    }

    server {

        listen 80;
        server_name nginx-handbook.test;

        location / {
            proxy_pass http://backend_servers;
        }
    }
}
```

La configuration à l'intérieur du contexte `server` est la même que celle que vous avez déjà vue. Le contexte `upstream`, par contre, est nouveau. Un upstream dans NGINX est une collection de serveurs qui peuvent être traités comme un seul backend.

Ainsi, les trois serveurs que vous avez démarrés à l'aide de PM2 peuvent être placés dans un seul upstream et vous pouvez laisser NGINX équilibrer la charge entre eux.

Pour tester la configuration, vous devrez envoyer un certain nombre de requêtes au serveur. Vous pouvez automatiser le processus en utilisant une boucle `while` en bash :

```shell
while sleep 0.5; do curl http://nginx-handbook.test; done

# response from server - 2.
# response from server - 3.
# response from server - 1.
# response from server - 2.
# response from server - 3.
# response from server - 1.
# response from server - 2.
# response from server - 3.
# response from server - 1.
# response from server - 2.
```

Vous pouvez annuler la boucle en appuyant sur `Ctrl + C` sur votre clavier. Comme vous pouvez le voir d'après les réponses du serveur, NGINX équilibre automatiquement la charge entre les serveurs.

Bien sûr, selon l'échelle du projet, l'équilibrage de charge peut être beaucoup plus compliqué que cela. Mais l'objectif de cet article est de vous faire démarrer, et je crois que vous avez maintenant une compréhension de base de l'équilibrage de charge avec NGINX. Vous pouvez arrêter les trois serveurs en cours d'exécution en exécutant la commande `pm2 stop server-1 server-2 server-3` (et c'est une bonne idée ici).

## Comment optimiser NGINX pour des performances maximales

Dans cette section de l'article, vous découvrirez un certain nombre de façons d'obtenir les performances maximales de votre serveur.

Certaines de ces méthodes seront spécifiques à l'application, ce qui signifie qu'elles nécessiteront probablement des ajustements en tenant compte des exigences de votre application. Mais certaines d'entre elles seront des techniques d'optimisation générales.

Tout comme dans les sections précédentes, les changements de configuration seront fréquents dans celle-ci, n'oubliez donc pas de valider et de recharger votre fichier de configuration à chaque fois.

### Comment configurer les Worker Processes et les Worker Connections

Comme je l'ai déjà mentionné dans une section précédente, NGINX peut lancer plusieurs worker processes capables de gérer chacun des milliers de requêtes.

```shell
sudo systemctl status nginx

# ● nginx.service - A high performance web server and a reverse proxy server
#      Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
#      Active: active (running) since Sun 2021-04-25 08:33:11 UTC; 5h 45min ago
#        Docs: man:nginx(8)
#    Main PID: 3904 (nginx)
#       Tasks: 2 (limit: 1136)
#      Memory: 3.2M
#      CGroup: /system.slice/nginx.service
#              ├─ 3904 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
#              └─16443 nginx: worker process
```

Comme vous pouvez le voir, il n'y a actuellement qu'un seul worker process NGINX sur le système. Ce nombre peut toutefois être modifié en apportant une petite modification au fichier de configuration.

```conf
worker_processes 2;

events {

}

http {

    server {

        listen 80;
        server_name nginx-handbook.test;

        return 200 "worker processes and worker connections configuration!\n";
    }
}
```

La directive `worker_processes` écrite dans le contexte `main` est responsable de la définition du nombre de worker processes à lancer. Vérifiez maintenant à nouveau le service NGINX et vous devriez voir deux worker processes :

```shell
sudo systemctl status nginx

# ● nginx.service - A high performance web server and a reverse proxy server
#      Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
#      Active: active (running) since Sun 2021-04-25 08:33:11 UTC; 5h 54min ago
#        Docs: man:nginx(8)
#     Process: 22610 ExecReload=/usr/sbin/nginx -g daemon on; master_process on; -s reload (code=exited, status=0/SUCCESS)
#    Main PID: 3904 (nginx)
#       Tasks: 3 (limit: 1136)
#      Memory: 3.7M
#      CGroup: /system.slice/nginx.service
#              ├─ 3904 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
#              ├─22611 nginx: worker process
#              └─22612 nginx: worker process
```

Définir le nombre de worker processes est facile, mais déterminer le nombre optimal de worker processes nécessite un peu plus de travail.

Les worker processes sont asynchrones par nature. Cela signifie qu'ils traiteront les requêtes entrantes aussi vite que le matériel le permet.

Considérez maintenant que votre serveur fonctionne sur un processeur monocœur. Si vous définissez le nombre de worker processes sur 1, ce processus unique utilisera 100 % de la capacité du processeur. Mais si vous le réglez sur 2, les deux processus pourront utiliser chacun 50 % du processeur. Ainsi, augmenter le nombre de worker processes ne signifie pas nécessairement de meilleures performances.

Une règle empirique pour déterminer le nombre optimal de worker processes est **nombre de worker processes = nombre de cœurs de processeur**.

Si vous travaillez sur un serveur avec un processeur double cœur, le nombre de worker processes doit être réglé sur 2. Sur un quadricœur, il doit être réglé sur 4... et vous avez compris l'idée.

Déterminer le nombre de processeurs sur votre serveur est très facile sous Linux.

```shell
nproc

# 1
```

Je suis sur une machine virtuelle à un seul processeur, donc `nproc` détecte qu'il y a un seul processeur. Maintenant que vous connaissez le nombre de processeurs, il ne reste plus qu'à définir le nombre dans la configuration.

C'est très bien, mais chaque fois que vous augmenterez la capacité du serveur et que le nombre de processeurs changera, vous devrez mettre à jour manuellement la configuration du serveur.

NGINX propose une meilleure façon de gérer ce problème. Vous pouvez simplement définir le nombre de worker processes sur `auto` et NGINX définira automatiquement le nombre de processus en fonction du nombre de processeurs.

```conf
worker_processes auto;

events {

}

http {

    server {

        listen 80;
        server_name nginx-handbook.test;

        return 200 "worker processes and worker connections configuration!\n";
    }
}
```

Inspectez à nouveau le processus NGINX :

```shell
sudo systemctl status nginx

# ● nginx.service - A high performance web server and a reverse proxy server
#      Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
#      Active: active (running) since Sun 2021-04-25 08:33:11 UTC; 6h ago
#        Docs: man:nginx(8)
#     Process: 22610 ExecReload=/usr/sbin/nginx -g daemon on; master_process on; -s reload (code=exited, status=0/SUCCESS)
#    Main PID: 3904 (nginx)
#       Tasks: 2 (limit: 1136)
#      Memory: 3.2M
#      CGroup: /system.slice/nginx.service
#              ├─ 3904 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
#              └─23659 nginx: worker process
```

Le nombre de worker processes est revenu à un, car c'est ce qui est optimal pour ce serveur.

En plus des worker processes, il y a aussi la worker connection, indiquant le nombre maximal de connexions qu'un seul worker process peut gérer.

Tout comme le nombre de worker processes, ce nombre est également lié au nombre de cœurs de votre processeur et au nombre de fichiers que votre système d'exploitation est autorisé à ouvrir par cœur.

Découvrir ce nombre est très facile sous Linux :

```shell
ulimit -n

# 1024
```

Maintenant que vous avez le nombre, il ne reste plus qu'à le définir dans la configuration :

```conf
worker_processes auto;

events {
    worker_connections 1024;
}

http {

    server {

        listen 80;
        server_name nginx-handbook.test;

        return 200 "worker processes and worker connections configuration!\n";
    }
}
```

La directive `worker_connections` est responsable de la définition du nombre de worker connections dans une configuration. C'est également la première fois que vous travaillez avec le contexte `events`.

Dans une section précédente, j'ai mentionné que ce contexte est utilisé pour définir des valeurs utilisées par NGINX à un niveau général. La configuration des worker connections en est un exemple.

### Comment mettre en cache le contenu statique

La deuxième technique pour optimiser votre serveur est la mise en cache du contenu statique. Quelle que soit l'application que vous servez, il y a toujours une certaine quantité de contenu statique servi, comme des feuilles de style, des images, etc.

Considérant que ce contenu n'est pas susceptible de changer très fréquemment, c'est une bonne idée de le mettre en cache pendant un certain temps. NGINX facilite également cette tâche.

```conf
worker_processes auto;

events {
    worker_connections 1024;
}

http {

    include /env/nginx/mime.types;

    server {

        listen 80;
        server_name nginx-handbook.test;

        root /srv/nginx-handbook-demo/static-demo;
        
        location ~* \.(css|js|jpg)$ {
            access_log off;
            
            add_header Cache-Control public;
            add_header Pragma public;
            add_header Vary Accept-Encoding;
            expires 1M;
        }
    }
}
```

En écrivant `location ~* .(css|js|jpg)$`, vous demandez à NGINX de faire correspondre les requêtes demandant un fichier se terminant par `.css`, `.js` et `.jpg`.

Dans mes applications, je stocke généralement les images au format [WebP](https://developers.google.com/speed/webp) même si l'utilisateur soumet un format différent. De cette façon, la configuration du cache statique devient encore plus facile pour moi.

Vous pouvez utiliser la directive `add_header` pour inclure un en-tête dans la réponse au client. Précédemment, vous avez vu la directive `proxy_set_header` utilisée pour définir des en-têtes sur une requête en cours vers le serveur backend. La directive `add_header`, en revanche, ajoute uniquement un en-tête donné à la réponse.

En définissant l'en-tête `Cache-Control` sur public, vous dites au client que ce contenu peut être mis en cache de n'importe quelle manière. L'en-tête `Pragma` est juste une version plus ancienne de l'en-tête `Cache-Control` et fait plus ou moins la même chose.

L'en-tête suivant, `Vary`, est responsable de faire savoir au client que ce contenu mis en cache peut varier.

La valeur de `Accept-Encoding` signifie que le contenu peut varier en fonction de l'encodage du contenu accepté par le client. Cela sera clarifié davantage dans la section suivante.

Enfin, la directive `expires` vous permet de définir l'en-tête `Expires` de manière pratique. La directive `expires` prend la durée pendant laquelle ce cache sera valide. En la réglant sur `1M`, vous demandez à NGINX de mettre le contenu en cache pendant un mois. Vous pouvez également régler cela sur `10m` pour 10 minutes, `24h` pour 24 heures, et ainsi de suite.

Maintenant, pour tester la configuration, envoyez une requête pour le fichier the-nginx-handbook.jpg depuis le serveur :

```shell
curl -I http://nginx-handbook.test/the-nginx-handbook.jpg

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Sun, 25 Apr 2021 15:58:22 GMT
# Content-Type: image/jpeg
# Content-Length: 19209
# Last-Modified: Sun, 25 Apr 2021 08:35:33 GMT
# Connection: keep-alive
# ETag: "608529d5-4b09"
# Expires: Tue, 25 May 2021 15:58:22 GMT
# Cache-Control: max-age=2592000
# Cache-Control: public
# Pragma: public
# Vary: Accept-Encoding
# Accept-Ranges: bytes
```

Comme vous pouvez le voir, les en-têtes ont été ajoutés à la réponse et tout navigateur moderne devrait pouvoir les interpréter.

### Comment compresser les réponses

La dernière technique d'optimisation que je vais montrer aujourd'hui est assez simple : compresser les réponses pour réduire leur taille.

```conf
worker_processes auto;

events {
    worker_connections 1024;
}

http {
    include /env/nginx/mime.types;

    gzip on;
    gzip_comp_level 3;

    gzip_types text/css text/javascript;

    server {

        listen 80;
        server_name nginx-handbook.test;

        root /srv/nginx-handbook-demo/static-demo;
        
        location ~* \.(css|js|jpg)$ {
            access_log off;
            
            add_header Cache-Control public;
            add_header Pragma public;
            add_header Vary Accept-Encoding;
            expires 1M;
        }
    }
}
```

Si vous ne le connaissez pas déjà, [GZIP](https://www.gnu.org/software/gzip/) est un format de fichier populaire utilisé par les applications pour la compression et la décompression de fichiers. NGINX peut utiliser ce format pour compresser les réponses à l'aide des directives `gzip`.

En écrivant `gzip on` dans le contexte `http`, vous demandez à NGINX de compresser les réponses. La directive `gzip_comp_level` définit le niveau de compression. Vous pouvez le régler sur un nombre très élevé, mais cela ne garantit pas une meilleure compression. Régler un nombre entre 1 et 4 vous donne un résultat efficace. Par exemple, j'aime le régler sur 3.

Par défaut, NGINX compresse les réponses HTML. Pour compresser d'autres formats de fichiers, vous devrez les passer en paramètres à la directive `gzip_types`. En écrivant `gzip_types text/css text/javascript;`, vous dites à NGINX de compresser tout fichier ayant les types MIME text/css et text/javascript.

Configurer la compression dans NGINX ne suffit pas. Le client doit demander la réponse compressée au lieu de la réponse non compressée. J'espère que vous vous souvenez de la ligne `add_header Vary Accept-Encoding;` dans la section précédente sur la mise en cache. Cet en-tête permet au client de savoir que la réponse peut varier en fonction de ce que le client accepte.

À titre d'exemple, si vous souhaitez demander la version non compressée du fichier mini.min.css au serveur, vous pouvez faire quelque chose comme ceci :

```shell
curl -I http://nginx-handbook.test/mini.min.css

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Sun, 25 Apr 2021 16:30:32 GMT
# Content-Type: text/css
# Content-Length: 46887
# Last-Modified: Sun, 25 Apr 2021 08:35:33 GMT
# Connection: keep-alive
# ETag: "608529d5-b727"
# Expires: Tue, 25 May 2021 16:30:32 GMT
# Cache-Control: max-age=2592000
# Cache-Control: public
# Pragma: public
# Vary: Accept-Encoding
# Accept-Ranges: bytes
```

Comme vous pouvez le voir, il n'y a rien concernant la compression. Maintenant, si vous voulez demander la version compressée du fichier, vous devrez envoyer un en-tête supplémentaire.

```shell
curl -I -H "Accept-Encoding: gzip" http://nginx-handbook.test/mini.min.css

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Sun, 25 Apr 2021 16:31:38 GMT
# Content-Type: text/css
# Last-Modified: Sun, 25 Apr 2021 08:35:33 GMT
# Connection: keep-alive
# ETag: W/"608529d5-b727"
# Expires: Tue, 25 May 2021 16:31:38 GMT
# Cache-Control: max-age=2592000
# Cache-Control: public
# Pragma: public
# Vary: Accept-Encoding
# Content-Encoding: gzip
```

Comme vous pouvez le voir dans les en-têtes de réponse, le `Content-Encoding` est maintenant réglé sur `gzip`, ce qui signifie qu'il s'agit de la version compressée du fichier.

Maintenant, si vous voulez comparer la différence de taille de fichier, vous pouvez faire quelque chose comme ceci :

```shell
cd ~
mkdir compression-test && cd compression-test

curl http://nginx-handbook.test/mini.min.css > uncompressed.css

curl -H "Accept-Encoding: gzip" http://nginx-handbook.test/mini.min.css > compressed.css

ls -lh

# -rw-rw-r-- 1 vagrant vagrant 9.1K Apr 25 16:35 compressed.css
# -rw-rw-r-- 1 vagrant vagrant  46K Apr 25 16:35 uncompressed.css
```

La version non compressée du fichier fait `46K` et la version compressée fait `9.1K`, soit presque six fois moins. Sur les sites réels où les feuilles de style peuvent être beaucoup plus volumineuses, la compression peut rendre vos réponses plus petites et plus rapides.

## Comment comprendre le fichier de configuration principal

J'espère que vous vous souvenez du fichier `nginx.conf` original que vous avez renommé dans une section précédente. Selon le [Debian wiki](https://wiki.debian.org/Nginx/DirectoryStructure), ce fichier est destiné à être modifié par les mainteneurs de NGINX et non par les administrateurs serveurs, à moins qu'ils ne sachent exactement ce qu'ils font.

Mais tout au long de l'article, je vous ai appris à configurer vos serveurs dans ce fichier même. Dans cette section, cependant, je vais vous montrer comment vous devriez configurer vos serveurs sans modifier le fichier `nginx.conf`.

Pour commencer, supprimez ou renommez d'abord votre fichier `nginx.conf` modifié et ramenez l'original :

```shell
sudo rm /etc/nginx/nginx.conf

sudo mv /etc/nginx/nginx.conf.backup /etc/nginx/nginx.conf

sudo nginx -s reload
```

Maintenant, NGINX devrait revenir à son état d'origine. Jetons à nouveau un coup d'œil au contenu de ce fichier en exécutant la commande `sudo cat /etc/nginx/nginx.conf` :

```conf
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 768;
	# multi_accept on;
}

http {

	##
	# Paramètres de base
	##

	sendfile on;
	tcp_nopush on;
	tcp_nodelay on;
	keepalive_timeout 65;
	types_hash_max_size 2048;
	# server_tokens off;

	# server_names_hash_bucket_size 64;
	# server_name_in_redirect off;

	include /etc/nginx/mime.types;
	default_type application/octet-stream;

	##
	# Paramètres SSL
	##

	ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Abandon de SSLv3, ref: POODLE
	ssl_prefer_server_ciphers on;

	##
	# Paramètres de journalisation
	##

	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;

	##
	# Paramètres Gzip
	##

	gzip on;

	# gzip_vary on;
	# gzip_proxied any;
	# gzip_comp_level 6;
	# gzip_buffers 16 8k;
	# gzip_http_version 1.1;
	# gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

	##
	# Configs d'hôtes virtuels
	##

	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
}


#mail {
#	# Voir l'exemple de script d'authentification sur :
#	# http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
# 
#	# auth_http localhost/auth.php;
#	# pop3_capabilities "TOP" "USER";
#	# imap_capabilities "IMAP4rev1" "UIDPLUS";
# 
#	server {
#		listen     localhost:110;
#		protocol   pop3;
#		proxy      on;
#	}
# 
#	server {
#		listen     localhost:143;
#		protocol   imap;
#		proxy      on;
#	}
#}
```

Vous devriez maintenant être capable de comprendre ce fichier sans trop de difficulté. Dans le contexte principal, les lignes `user www-data;` et `worker_processes auto;` devraient vous être facilement reconnaissables.

La ligne `pid /run/nginx.pid;` définit l'ID de processus pour le processus NGINX et `include /etc/nginx/modules-enabled/*.conf;` inclut tout fichier de configuration trouvé dans le répertoire `/etc/nginx/modules-enabled/`.

Ce répertoire est destiné aux modules dynamiques NGINX. Je n'ai pas couvert les modules dynamiques dans cet article, donc je vais passer cela.

Maintenant, à l'intérieur du contexte `http`, sous les paramètres de base, vous pouvez voir certaines techniques d'optimisation courantes appliquées. Voici ce que font ces techniques :

* `sendfile on;` désactive la mise en mémoire tampon pour les fichiers statiques.
* `tcp_nopush on;` permet d'envoyer l'en-tête de réponse dans un seul paquet.
* `tcp_nodelay on;` désactive l'[algorithme de Nagle](https://en.wikipedia.org/wiki/Nagle's_algorithm), ce qui permet une livraison plus rapide des fichiers statiques.

La directive `keepalive_timeout` indique combien de temps garder une connexion ouverte et la directive `types_hash_maxsize` définit la taille de la table de hachage des types. Elle inclut également le fichier `mime.types` par défaut.

Je passerai les paramètres SSL simplement parce que nous ne les avons pas couverts dans cet article. Nous avons déjà discuté des paramètres de journalisation et de gzip. Vous verrez peut-être certaines des directives concernant gzip commentées. Tant que vous comprenez ce que vous faites, vous pouvez personnaliser ces paramètres.

Vous utilisez le contexte `mail` pour configurer NGINX comme un serveur de messagerie. Nous n'avons parlé de NGINX qu'en tant que serveur web jusqu'à présent, donc je vais également passer cela.

Maintenant, sous les paramètres des hôtes virtuels, vous devriez voir deux lignes comme suit :

```conf
##
# Configs d'hôtes virtuels
##

include /etc/nginx/conf.d/*.conf;
include /etc/nginx/sites-enabled/*;
```

Ces deux lignes demandent à NGINX d'inclure tous les fichiers de configuration trouvés dans les répertoires `/etc/nginx/conf.d/` et `/etc/nginx/sites-enabled/`.

Après avoir vu ces deux lignes, les gens considèrent souvent ces deux répertoires comme l'endroit idéal pour placer leurs fichiers de configuration, mais ce n'est pas tout à fait exact.

Il existe un autre répertoire `/etc/nginx/sites-available/` qui est destiné à stocker les fichiers de configuration pour vos hôtes virtuels. Le répertoire `/etc/nginx/sites-enabled/` est destiné à stocker les liens symboliques vers les fichiers du répertoire `/etc/nginx/sites-available/`.

En fait, il existe une configuration d'exemple :

```shell
ln -lh /etc/nginx/sites-enabled/

# lrwxrwxrwx 1 root root 34 Apr 25 08:33 default -> /etc/nginx/sites-available/default
```

Comme vous pouvez le voir, le répertoire contient un lien symbolique vers le fichier `/etc/nginx/sites-available/default`.

L'idée est d'écrire plusieurs hôtes virtuels dans le répertoire `/etc/nginx/sites-available/` et d'activer certains d'entre eux en créant des liens symboliques vers le répertoire `/etc/nginx/sites-enabled/`.

Pour démontrer ce concept, configurons un simple serveur statique. Tout d'abord, supprimez le lien symbolique de l'hôte virtuel par défaut, désactivant ainsi cette configuration par la même occasion :

```shell
sudo rm /etc/nginx/sites-enabled/default

ls -lh /etc/nginx/sites-enabled/

# lrwxrwxrwx 1 root root 41 Apr 25 18:01 nginx-handbook -> /etc/nginx/sites-available/nginx-handbook
```

Créez un nouveau fichier en exécutant `sudo touch /etc/nginx/sites-available/nginx-handbook` et mettez-y le contenu suivant :

```
server {
    listen 80;
    server_name nginx-handbook.test;

    root /srv/nginx-handbook-projects/static-demo;
}
```

Les fichiers à l'intérieur du répertoire `/etc/nginx/sites-available/` sont destinés à être inclus dans le contexte `http` principal, ils ne doivent donc contenir que des blocs `server`.

Maintenant, créez un lien symbolique vers ce fichier dans le répertoire `/etc/nginx/sites-enabled/` en exécutant la commande suivante :

```shell
sudo ln -s /etc/nginx/sites-available/nginx-handbook /etc/nginx/sites-enabled/nginx-handbook

ls -lh /etc/nginx/sites-enabled/

# lrwxrwxrwx 1 root root 34 Apr 25 08:33 default -> /etc/nginx/sites-available/default
# lrwxrwxrwx 1 root root 41 Apr 25 18:01 nginx-handbook -> /etc/nginx/sites-available/nginx-handbook
```

Avant de valider et de recharger le fichier de configuration, vous devrez réouvrir les fichiers journaux. Sinon, vous pourriez obtenir une erreur de permission refusée. Cela se produit car l'ID de processus est différent cette fois-ci suite au remplacement de l'ancien fichier `nginx.conf`.

```shell
sudo rm /var/log/nginx/*.log

sudo touch /var/log/nginx/access.log /var/log/nginx/error.log

sudo nginx -s reopen
```

Enfin, validez et rechargez le fichier de configuration :

```
sudo nginx -t

# nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
# nginx: configuration file /etc/nginx/nginx.conf test is successful

sudo nginx -s reload
```

Visitez le serveur et vous devriez être accueilli par la bonne vieille page du manuel NGINX :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-100.png)

Si vous avez configuré le serveur correctement et que vous obtenez toujours l'ancienne page d'accueil NGINX, effectuez un rafraîchissement forcé. Le navigateur conserve souvent d'anciens éléments et nécessite un petit nettoyage.

## Comment configurer SSL et HTTP/2

[HTTP/2](https://en.wikipedia.org/wiki/HTTP/2) est la version la plus récente du protocole Hyper Text Transport Protocol, mondialement populaire. Basé sur le protocole expérimental [SPDY](https://en.wikipedia.org/wiki/SPDY) de Google, HTTP/2 offre de meilleures performances en introduisant des fonctionnalités telles que le multiplexage complet des requêtes et des réponses, une meilleure compression des champs d'en-tête, le server push et la priorisation des requêtes.

Certaines des fonctionnalités notables de HTTP/2 sont les suivantes :

1. **Protocole binaire** - Alors que HTTP/1.x était un protocole basé sur du texte, HTTP/2 est un protocole binaire, ce qui réduit les erreurs lors du processus de transfert de données.
2. **Flux multiplexés** - Toutes les connexions HTTP/2 sont des flux multiplexés, ce qui signifie que plusieurs fichiers peuvent être transférés dans un seul flux de données binaires.
3. **En-tête compressé** - HTTP/2 compresse les données d'en-tête dans les réponses, ce qui accélère le transfert des données.
4. **Server Push** - Cette capacité permet au serveur d'envoyer automatiquement des ressources liées au client, réduisant considérablement le nombre de requêtes au serveur.
5. **Priorisation des flux** - HTTP/2 peut prioriser les flux de données en fonction de leur type, ce qui permet une meilleure allocation de la bande passante là où c'est nécessaire.

> Si vous voulez en savoir plus sur les améliorations de HTTP/2, cet [article](https://kinsta.com/learn/what-is-http2/) de [Kinsta](https://kinsta.com/) peut vous aider.

Bien qu'il s'agisse d'une mise à niveau significative par rapport à son prédécesseur, HTTP/2 n'est pas aussi largement adopté qu'il devrait l'être. Dans cette section, je vais vous présenter certaines des nouvelles fonctionnalités mentionnées précédemment et je vous montrerai également comment activer HTTP/2 sur votre serveur web propulsé par NGINX.

Pour cette section, j'utiliserai le projet `static-demo`. Je suppose que vous avez déjà cloné le dépôt dans le répertoire `/srv/nginx-handbook-projects`. Si ce n'est pas le cas, c'est le moment de le faire. De plus, cette section doit être réalisée sur un serveur privé virtuel (VPS) plutôt que sur une machine virtuelle.

Par simplicité, j'utiliserai le fichier `/etc/nginx/sites-available/default` comme configuration. Ouvrez le fichier en utilisant `nano` ou `vi` si vous préférez.

```shell
nano /etc/nginx/sites-available/default
```

Mettez à jour le contenu du fichier comme suit :

```conf
server {
        listen 80;
        server_name nginx-handbook.farhan.dev;  

        root /srv/nginx-handbook-projects/static-demo;
}
```

Comme vous pouvez le voir, le répertoire `/srv/nginx-handbook-projects/static-demo;` a été défini comme racine de ce site et `nginx-handbook.farhan.dev` a été défini comme nom de serveur. Si vous n'avez pas de domaine personnalisé configuré, vous pouvez utiliser l'adresse IP de votre serveur comme nom de serveur ici.

```shell
nginx -t

# nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
# nginx: configuration file /etc/nginx/nginx.conf test is successful

nginx -s reload
```

Testez la configuration en exécutant `nginx -t` et rechargez la configuration en exécutant les commandes `nginx -s reload`.

Enfin, visitez votre serveur et vous devriez être accueilli par une simple page HTML statique.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/OCHoJEYdm.jpg)

L'un des prérequis pour faire fonctionner HTTP/2 sur votre serveur est d'avoir un certificat SSL valide. Faisons cela d'abord.

### Comment configurer SSL

Pour ceux d'entre vous qui ne le savent peut-être pas, un certificat SSL est ce qui permet à un serveur de passer de HTTP à HTTPS. Ces certificats sont délivrés par une autorité de certification (CA). La plupart des autorités facturent des frais pour la délivrance de certificats, mais des autorités à but non lucratif telles que [Let's Encrypt](https://letsencrypt.org/) délivrent des certificats gratuitement.

> Si vous voulez comprendre la théorie du SSL un peu plus en détail, cet [article](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/) sur le [Cloudflare Learning Center](https://www.cloudflare.com/learning/) peut vous aider.

Grâce à des outils open-source comme [Certbot](https://github.com/certbot/certbot), l'installation d'un certificat gratuit est un jeu d'enfant. Rendez-vous sur le lien [certbot.eff.org](https://certbot.eff.org/). Sélectionnez maintenant le logiciel et le système qui propulsent votre serveur.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/A13UVsSsE.jpg)

J'utilise NGINX sur Ubuntu 20.04 et si vous avez suivi cet article, vous devriez avoir la même combinaison.

Après avoir sélectionné votre combinaison de logiciel et de système, vous serez redirigé vers une nouvelle page contenant des instructions étape par étape pour installer certbot et un nouveau certificat SSL.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/27NSXHEp2.jpg)

Les étapes d'installation de certbot peuvent différer d'un système à l'autre, mais le reste des instructions devrait rester le même. Sur Ubuntu, la méthode recommandée est d'utiliser [snap](https://snapcraft.io/).

```shell
snap install --classic certbot

# certbot 1.14.0 from Certbot Project (certbot-eff✓) installed

certbot --version

# certbot 1.14.0
```

Certbot est maintenant installé et prêt à être utilisé. Avant d'installer un nouveau certificat, assurez-vous que le fichier de configuration NGINX contient tous les noms de serveur nécessaires. Par exemple, si vous souhaitez installer un nouveau certificat pour `votre-domaine.tld` et `www.votre-domaine.tld`, vous devrez inclure les deux dans votre configuration.

Une fois que vous êtes satisfait de votre configuration, vous pouvez installer un certificat nouvellement provisionné pour votre serveur. Pour ce faire, exécutez le programme `certbot` avec l'option `--nginx`.

```shell
certbot --nginx

# Saving debug log to /var/log/letsencrypt/letsencrypt.log
# Plugins selected: Authenticator nginx, Installer nginx
# Enter email address (used for urgent renewal and security notices)
#  (Enter 'c' to cancel): shovik.is.here@gmail.com

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Please read the Terms of Service at
# https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf. You must
# agree in order to register with the ACME server. Do you agree?
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# (Y)es/(N)o: Y

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Would you be willing, once your first certificate is successfully issued, to
# share your email address with the Electronic Frontier Foundation, a founding
# partner of the Let's Encrypt project and the non-profit organization that
# develops Certbot? We'd like to send you email about our work encrypting the web,
# EFF news, campaigns, and ways to support digital freedom.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# (Y)es/(N)o: N
# Account registered.

# Which names would you like to activate HTTPS for?
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 1: nginx-handbook.farhan.dev
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Select the appropriate numbers separated by commas and/or spaces, or leave input
# blank to select all options shown (Enter 'c' to cancel): 
# Requesting a certificate for nginx-handbook.farhan.dev
# Performing the following challenges:
# http-01 challenge for nginx-handbook.farhan.dev
# Waiting for verification...
# Cleaning up challenges
# Deploying Certificate to VirtualHost /etc/nginx/sites-enabled/default
# Redirecting all traffic on port 80 to ssl in /etc/nginx/sites-enabled/default

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Congratulations! You have successfully enabled
# https://nginx-handbook.farhan.dev
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# IMPORTANT NOTES:
#  - Congratulations! Your certificate and chain have been saved at:
#    /etc/letsencrypt/live/nginx-handbook.farhan.dev/fullchain.pem
#    Your key file has been saved at:
#    /etc/letsencrypt/live/nginx-handbook.farhan.dev/privkey.pem
#    Your certificate will expire on 2021-07-30. To obtain a new or
#    tweaked version of this certificate in the future, simply run
#    certbot again with the "certonly" option. To non-interactively
#    renew *all* of your certificates, run "certbot renew"
#  - If you like Certbot, please consider supporting our work by:

#    Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
#    Donating to EFF:                    https://eff.org/donate-le
```

On vous demandera une adresse e-mail de contact d'urgence, l'acceptation de la licence et si vous souhaitez recevoir des e-mails de leur part ou non.

Le programme certbot lira automatiquement les noms de serveur à partir de votre fichier de configuration et vous en montrera une liste. Si vous avez plusieurs hôtes virtuels sur votre serveur, certbot les reconnaîtra également.

Enfin, si l'installation réussit, vous serez félicité par le programme. Pour vérifier si tout fonctionne ou non, visitez votre serveur avec HTTPS cette fois-ci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/mCbapBf9n.jpg)

Comme vous pouvez le voir, HTTPS a été activé avec succès et vous pouvez confirmer que le certificat est vérifié par l'autorité [Let's Encrypt](https://letsencrypt.org/). Plus tard, si vous ajoutez de nouveaux hôtes virtuels à ce serveur avec de nouveaux domaines ou sous-domaines, vous devrez réinstaller les certificats.

Il est également possible d'installer un certificat wildcard tel que `*.votre-domaine.tld` pour certains gestionnaires DNS pris en charge. Des instructions détaillées peuvent être trouvées sur la page d'instructions d'installation montrée précédemment.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/PLFcZoO8P.jpg)

Un certificat nouvellement installé sera valide pendant 90 jours. Après cela, un renouvellement sera nécessaire. Certbot effectue le renouvellement automatiquement. Vous pouvez exécuter la commande `certbot renew` avec l'option `--dry-run` pour tester la fonction de renouvellement automatique.

```shell
certbot renew --dry-run

# Saving debug log to /var/log/letsencrypt/letsencrypt.log

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Processing /etc/letsencrypt/renewal/nginx-handbook.farhan.dev.conf
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Cert not due for renewal, but simulating renewal for dry run
# Plugins selected: Authenticator nginx, Installer nginx
# Account registered.
# Simulating renewal of an existing certificate for nginx-handbook.farhan.dev
# Performing the following challenges:
# http-01 challenge for nginx-handbook.farhan.dev
# Waiting for verification...
# Cleaning up challenges

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# new certificate deployed with reload of nginx server; fullchain is
# /etc/letsencrypt/live/nginx-handbook.farhan.dev/fullchain.pem
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Congratulations, all simulated renewals succeeded: 
#   /etc/letsencrypt/live/nginx-handbook.farhan.dev/fullchain.pem (success)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```

La commande simulera un renouvellement de certificat pour tester s'il est correctement configuré ou non. Si elle réussit, vous serez félicité par le programme. Cette étape termine la procédure d'installation d'un certificat SSL sur votre serveur.

Pour comprendre ce que certbot a fait en coulisses, ouvrez à nouveau le fichier `/etc/nginx/sites-available/default` et voyez comment son contenu a été modifié.

```conf
server {

    server_name nginx-handbook.farhan.dev;  

    root /srv/nginx-handbook-projects/static-demo;

    listen [::]:443 ssl ipv6only=on; # managed by Certbot
    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/nginx-handbook.farhan.dev/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/nginx-handbook.farhan.dev/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}
server {
    if ($host = nginx-handbook.farhan.dev) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80;
    listen [::]:80;

    server_name nginx-handbook.farhan.dev;
    return 404; # managed by Certbot
}
```

Comme vous pouvez le voir, certbot a ajouté pas mal de lignes ici. J'expliquerai les plus notables.

```conf
server {
    # ...
    listen [::]:443 ssl ipv6only=on; # managed by Certbot
    listen 443 ssl; # managed by Certbot
    # ...
}
```

Tout comme le port 80, le port 443 est largement utilisé pour écouter les requêtes HTTPS. En écrivant `listen 443 ssl;`, certbot demande à NGINX d'écouter toute requête HTTPS sur le port 443. La ligne `listen [::]:443 ssl ipv6only=on;` sert à gérer les connexions IPv6.

```conf


server {
    # ...
    ssl_certificate /etc/letsencrypt/live/nginx-handbook.farhan.dev/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/nginx-handbook.farhan.dev/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
    # ...
}
```

La directive `ssl_certificate` est utilisée pour indiquer l'emplacement du certificat et du fichier de clé privée sur votre serveur. Le fichier `/etc/letsencrypt/options-ssl-nginx.conf;` inclut certaines directives communes nécessaires pour le SSL.

Enfin, `ssl_dhparam` indique le fichier définissant comment OpenSSL va effectuer l'[échange de clés Diffie–Hellman](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange). Si vous voulez en savoir plus sur l'utilité du fichier `/etc/letsencrypt/ssl-dhparams.pem;`, ce [fil de discussion](https://security.stackexchange.com/questions/94390/whats-the-purpose-of-dh-parameters) sur Stack Exchange peut vous aider.

```conf
server {
    if ($host = nginx-handbook.farhan.dev) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80;
    listen [::]:80;

    server_name nginx-handbook.farhan.dev;
    return 404; # managed by Certbot
}
```

Ce bloc serveur nouvellement ajouté est responsable de la redirection de toutes les requêtes HTTP vers HTTPS, désactivant ainsi complètement l'accès HTTP.

### Comment activer HTTP/2

Une fois que vous avez installé avec succès un certificat SSL valide sur votre serveur, vous êtes prêt à activer HTTP/2. Le SSL est un prérequis pour HTTP/2, donc d'emblée, vous pouvez voir que la sécurité n'est pas optionnelle avec HTTP/2.

Le support de HTTP/2 pour NGINX est fourni par le module [ngx_http_v2_module](https://nginx.org/en/docs/http/ngx_http_v2_module.html). Les binaires pré-construits de NGINX sur la plupart des systèmes sont livrés avec ce module intégré. Si vous avez construit NGINX à partir des sources, vous devrez cependant inclure ce module manuellement.

Avant de passer à HTTP/2, envoyez une requête à votre serveur et voyez la version actuelle du protocole.

```shell
curl -I -L https://nginx-handbook.farhan.dev

# HTTP/1.1 200 OK
# Server: nginx/1.18.0 (Ubuntu)
# Date: Sat, 01 May 2021 10:46:36 GMT
# Content-Type: text/html
# Content-Length: 960
# Last-Modified: Fri, 30 Apr 2021 20:14:48 GMT
# Connection: keep-alive
# ETag: "608c6538-3c0"
# Accept-Ranges: bytes

```

Comme vous pouvez le voir, par défaut, le serveur utilise le protocole HTTP/1.1. À l'étape suivante, nous mettrons à jour le fichier de configuration comme nécessaire pour activer HTTP/2.

Pour activer HTTP/2 sur votre serveur, ouvrez à nouveau le fichier `/etc/nginx/sites-available/default`. Trouvez partout où il est écrit `listen [::]:443 ssl ipv6only=on;` ou `listen 443 ssl;` et mettez-les à jour respectivement en `listen [::]:443 ssl http2 ipv6only=on;` et `listen 443 ssl http2;`.

```conf
server {

    server_name nginx-handbook.farhan.dev;  

    root /srv/nginx-handbook-projects/static-demo;

    listen [::]:443 ssl http2 ipv6only=on; # managed by Certbot
    listen 443 ssl http2; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/nginx-handbook.farhan.dev/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/nginx-handbook.farhan.dev/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}
server {
    if ($host = nginx-handbook.farhan.dev) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80;
    listen [::]:80;

    server_name nginx-handbook.farhan.dev;
    return 404; # managed by Certbot
}
```

Testez le fichier de configuration en exécutant `nginx -t` et rechargez la configuration en exécutant les commandes `nginx -s reload`. Maintenant, envoyez à nouveau une requête à votre serveur.

```shell
curl -I -L https://nginx-handbook.farhan.dev

# HTTP/2 200 
# server: nginx/1.18.0 (Ubuntu)
# date: Sat, 01 May 2021 09:03:10 GMT
# content-type: text/html
# content-length: 960
# last-modified: Fri, 30 Apr 2021 20:14:48 GMT
# etag: "608c6538-3c0"
# accept-ranges: bytes
```

Comme vous pouvez le voir, HTTP/2 a été activé pour tout client supportant le nouveau protocole.

### Comment activer le Server Push

Le server push est l'une des nombreuses fonctionnalités que HTTP/2 apporte. Cela signifie que le serveur peut envoyer des fichiers au client sans que celui-ci n'ait à les demander. Sur un serveur HTTP/1.x, une requête typique pour du contenu statique peut ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/f49aVyg9h.jpg)

Mais sur un serveur HTTP/2 avec server push activé, cela peut ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/wLod0KcsB.jpg)

Sur une seule requête pour le fichier index.html, le serveur répond également avec le fichier style.css, minimisant ainsi le nombre de requêtes dans le processus.

Dans cette section, j'utiliserai un client HTTP open-source nommé [Nghttp2](https://nghttp2.org/) pour tester le serveur.

```shell
apt install nghttp2-client -y

# Reading package lists... Done
# Building dependency tree       
# Reading state information... Done
# The following additional packages will be installed:
#   libev4 libjansson4 libjemalloc2
# The following NEW packages will be installed:
#   libev4 libjansson4 libjemalloc2 nghttp2-client
# 0 upgraded, 4 newly installed, 0 to remove and 0 not upgraded.
# Need to get 447 kB of archives.
# After this operation, 1,520 kB of additional disk space will be used.
# Get:1 http://archive.ubuntu.com/ubuntu focal/main amd64 libjansson4 amd64 2.12-1build1 [28.9 kB]
# Get:2 http://archive.ubuntu.com/ubuntu focal/universe amd64 libjemalloc2 amd64 5.2.1-1ubuntu1 [235 kB]
# Get:3 http://archive.ubuntu.com/ubuntu focal/universe amd64 libev4 amd64 1:4.31-1 [31.2 kB]
# Get:4 http://archive.ubuntu.com/ubuntu focal/universe amd64 nghttp2-client amd64 1.40.0-1build1 [152 kB]
# Fetched 447 kB in 1s (359 kB/s)     
# Selecting previously unselected package libjansson4:amd64.
# (Reading database ... 107613 files and directories currently installed.)
# Preparing to unpack .../libjansson4_2.12-1build1_amd64.deb ...
# Unpacking libjansson4:amd64 (2.12-1build1) ...
# Selecting previously unselected package libjemalloc2:amd64.
# Preparing to unpack .../libjemalloc2_5.2.1-1ubuntu1_amd64.deb ...
# Unpacking libjemalloc2:amd64 (5.2.1-1ubuntu1) ...
# Selecting previously unselected package libev4:amd64.
# Preparing to unpack .../libev4_1%3a4.31-1_amd64.deb ...
# Unpacking libev4:amd64 (1:4.31-1) ...
# Selecting previously unselected package nghttp2-client.
# Preparing to unpack .../nghttp2-client_1.40.0-1build1_amd64.deb ...
# Unpacking nghttp2-client (1.40.0-1build1) ...
# Setting up libev4:amd64 (1:4.31-1) ...
# Setting up libjemalloc2:amd64 (5.2.1-1ubuntu1) ...
# Setting up libjansson4:amd64 (2.12-1build1) ...
# Setting up nghttp2-client (1.40.0-1build1) ...
# Processing triggers for man-db (2.9.1-1) ...
# Processing triggers for libc-bin (2.31-0ubuntu9.2) ...

nghttp --version

# nghttp nghttp2/1.40.0
```

Testons en envoyant une requête au serveur sans server push.

```shell
nghttp --null-out --stat https://nginx-handbook.farhan.dev/index.html

# id  responseEnd requestStart  process code size request path
#  13      +836us       +194us    642us  200  492 /index.html

nghttp --null-out --stat --get-assets https://nginx-handbook.farhan.dev/index.html

# id  responseEnd requestStart  process code size request path
#  13      +836us       +194us    642us  200  492 /index.html
#  15     +3.11ms      +2.65ms    457us  200  45K /mini.min.css
#  17     +3.23ms      +2.65ms    578us  200  18K /the-nginx-handbook.jpg
```

Sur la première requête, `--null-out` signifie ignorer les données téléchargées et `--stat` signifie imprimer les statistiques sur le terminal. Sur la deuxième requête, `--get-assets` signifie également télécharger les ressources telles que les feuilles de style, les images et les scripts liés à ces fichiers. En conséquence, vous pouvez voir par les temps `requestStart` que le fichier css et l'image ont été téléchargés peu de temps après le téléchargement du fichier html.

Maintenant, activons le server push pour les feuilles de style et les images. Ouvrez le fichier `/etc/nginx/sites-available/default` et mettez à jour son contenu comme suit :

```conf
server {

    server_name nginx-handbook.farhan.dev;

    root /srv/nginx-handbook-projects/static-demo;

    listen [::]:443 ssl http2 ipv6only=on; # managed by Certbot
    listen 443 ssl http2; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/nginx-handbook.farhan.dev/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/nginx-handbook.farhan.dev/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

    location = /index.html {
        http2_push /mini.min.css;
        http2_push /the-nginx-handbook.jpg;
    }

    location = /about.html {
        http2_push /mini.min.css;
        http2_push /the-nginx-handbook.jpg;
    }

}
server {
    if ($host = nginx-handbook.farhan.dev) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80;
    listen [::]:80;

    server_name nginx-handbook.farhan.dev;
    return 404; # managed by Certbot
}
```

Deux blocs de location ont été ajoutés pour correspondre exactement aux emplacements `/index.html` et `/about.html`. La directive `http2_push` est utilisée pour renvoyer une réponse supplémentaire. Désormais, chaque fois que NGINX reçoit une requête pour l'un de ces deux emplacements, il renverra automatiquement le fichier css et le fichier image.

Testez la configuration en exécutant `nginx -t` et rechargez la configuration en exécutant les commandes `nginx -s reload`.

```shell
nginx -t

# nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
# nginx: configuration file /etc/nginx/nginx.conf test is successful

nginx -s reload
```

Maintenant, envoyez une autre requête au serveur en utilisant `nghttp` et n'incluez pas l'option `--get-assets`.

```shell
nghttp --null-out --stat https://nginx-handbook.farhan.dev/index.html

# id  responseEnd requestStart  process code size request path
#  13     +1.49ms       +254us   1.23ms  200  492 /index.html
#   2     +1.56ms *    +1.35ms    212us  200  45K /mini.min.css
#   4     +1.71ms *    +1.39ms    318us  200  18K /the-nginx-handbook.jpg
```

Comme vous pouvez le voir, bien que les ressources n'aient pas été demandées, le serveur les a envoyées au client. En regardant les mesures de temps, le temps de traitement a diminué et les trois réponses se sont terminées presque simultanément.

C'était un exemple très simple de server push, mais selon les nécessités de votre projet, cette configuration peut devenir beaucoup plus complexe. Cet [article](https://www.nginx.com/blog/nginx-1-13-9-http2-server-push/) d'[Owen Garrett](https://www.nginx.com/people/owen-garrett/) sur le blog officiel de NGINX peut vous aider avec des configurations de server push plus complexes.

## Conclusion

Je tiens à vous remercier du fond du cœur pour le temps que vous avez passé à lire cet article. J'espère que vous avez apprécié votre temps et que vous avez appris tous les essentiels de NGINX.

En plus de celui-ci, j'ai écrit des manuels complets sur d'autres sujets complexes disponibles gratuitement sur [freeCodeCamp](https://www.freecodecamp.org/news/author/farhanhasin/).

Ces manuels font partie de ma mission visant à simplifier les technologies difficiles à comprendre pour tout le monde. Chacun de ces manuels demande beaucoup de temps et d'efforts à écrire.

Si vous avez apprécié mon écriture et que vous voulez me garder motivé, envisagez de laisser des étoiles sur [GitHub](https://github.com/fhsinchy/) et de me recommander pour des compétences pertinentes sur [LinkedIn](https://www.linkedin.com/in/farhanhasin/). J'accepte également les parrainages, vous pouvez donc envisager de [m'offrir un café](https://www.buymeacoffee.com/farhanhasin) si vous le souhaitez.

Je suis toujours ouvert aux suggestions et aux discussions sur [Twitter](https://twitter.com/frhnhsin) ou [LinkedIn](https://www.linkedin.com/in/farhanhasin/). N'hésitez pas à m'envoyer des messages directs.

Enfin, pensez à partager les ressources avec d'autres, car

> Partager la connaissance est l'acte d'amitié le plus fondamental. Car c'est une façon de donner quelque chose sans rien perdre. — Richard Stallman

D'ici le prochain, restez en sécurité et continuez d'apprendre.