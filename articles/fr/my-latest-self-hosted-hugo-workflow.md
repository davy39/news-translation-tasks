---
title: Comment héberger soi-même une application web Hugo
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-29T18:10:07.000Z'
originalURL: https://freecodecamp.org/news/my-latest-self-hosted-hugo-workflow
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Self-hosted-Hugo.png
tags:
- name: containerization
  slug: containerization
- name: FreeBSD
  slug: freebsd
- name: Hugo
  slug: hugo
- name: self hosting
  slug: self-hosting
seo_title: Comment héberger soi-même une application web Hugo
seo_desc: 'By Jared Wolff

  After hosting with Netlify for a few years, I decided to head back to self hosting.
  There are a few reasons for that, but the main reasoning was that I had more control
  over how things worked.

  In this post, I''ll show you my workflow fo...'
---

Par Jared Wolff

Après avoir hébergé avec Netlify pendant quelques années, j'ai décidé de revenir à l'auto-hébergement. Il y a plusieurs raisons à cela, mais la principale était que j'avais plus de contrôle sur le fonctionnement des choses.

Dans cet article, je vais vous montrer mon flux de travail pour déployer mon site généré par [Hugo](https://gohugo.io) ([www.jaredwolff.com](https://www.jaredwolff.com)).

Au lieu d'utiliser ce que la plupart des gens choisiraient, je vais faire tout cela en utilisant un serveur basé sur des jails FreeBSD. De plus, je vais vous montrer quelques astuces que j'ai apprises au fil des années sur le redimensionnement d'images en masse et plus encore.

Commençons.

## Où héberger ?

Si vous souhaitez héberger votre propre service, vous aurez besoin d'un serveur. C'est là qu'intervient un fournisseur de VPS comme Digital Ocean ou Vultr. J'utilise Digital Ocean depuis un moment et je suis un fan.

Pour configurer un nouveau serveur, voici quelques étapes :

1. Connectez-vous à Digital Ocean. Si vous n'avez pas de compte Digital Ocean et que vous souhaitez soutenir ce blog, cliquez [ici](https://m.do.co/c/9574d3846a29) pour créer un compte.
2. Allez dans `Paramètres du compte` -> `Sécurité` et assurez-vous d'avoir une clé SSH configurée.
3. Créez une nouvelle droplet FreeBSD. Assurez-vous d'utiliser la version UFS ![Créer une droplet](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/images/Screen_Shot_2020-04-15_at_9.41.21_AM.png) ![Choisir FreeBSD 12.1 UFS](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/images/Screen_Shot_2020-04-15_at_9.43.21_AM.png)
4. Assurez-vous de sélectionner le plan à 5 $ par mois. Pour les installations simples, c'est plus que suffisant ! ![$5 Plan](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/images/Screen_Shot_2020-04-15_at_9.44.13_AM.png)
1. Assurez-vous que votre clé SSH est sélectionnée ![Sélectionner la clé SSH](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/images/Screen_Shot_2020-04-15_at_9.45.26_AM.png)
1. Enfin, cliquez sur ce bouton vert **Créer une droplet** ! ![Créer une droplet](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/images/Screen_Shot_2020-04-15_at_9.45.24_AM.png)
5. Connectez-vous en SSH une fois terminé : `ssh root@<votre_ip_serveur>`

## Configuration de votre serveur FreeBSD avec Bastille

![images/bastille.png](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/images/bastille.png)

Jusqu'à récemment, tout fonctionnait sur une plateforme basée sur Docker utilisant [Exoframe](https://github.com/exoframejs/exoframe). C'était facile et presque sans effort.

L'inconvénient était que Docker consomme beaucoup trop de ressources. De plus, gérer des fichiers dans un conteneur Docker est autant, sinon plus, de travail que de l'héberger nativement. Oh, et avez-vous vérifié combien d'espace Docker a utilisé sur votre machine récemment ? Sur ma machine de développement, c'était environ 19 Go d'espace. ?

Alors, quelle est l'alternative ?

Les jails FreeBSD utilisant Bastille.

J'utilise Bastille depuis quelques mois maintenant. Plus je l'utilise, plus cela a 100 % de sens.

Bastille vous permet de créer des jails FreeBSD légères et portables. Ces jails sont des "conteneurs" qui ont virtuellement aucun surcoût. Il n'y a pas de démon (le système d'exploitation est le "démon" !). De plus, les jails sont sécurisées par rapport à la boîte de Pandore qu'est Docker. Oui, vous devrez peut-être compiler et porter certains utilitaires. La plupart sont déjà pris en charge dans le gestionnaire de paquets de FreeBSD `pkg`.

Dans cette section, vous apprendrez comment faire fonctionner une jail avec `caddy` pour que vous puissiez héberger votre site de manière sécurisée.

Continuons !

Une fois que vous avez l'adresse IP de votre serveur, vous devriez vous connecter :

    ssh root@123.456.789.10

Vous devriez obtenir un message MOTD et une invite `sh`. Woo !

    FreeBSD 12.1-RELEASE-p2 GENERIC

    Bienvenue sur FreeBSD !
    ...

    #

Installons quelques éléments importants en utilisant `pkg` (le gestionnaire de paquets de FreeBSD) :

    pkg install restic rsync bastille

Nous utiliserons `restic` pour les sauvegardes, `rsync` pour transférer des fichiers et `bastille` pour la configuration de la jail.

Vous devez également configurer quelques routes statiques dans votre `pf.conf`. Voici un exemple du mien :

```shell
ext_if="vtnet0"

# Caddy related
caddy_addr=10.10.2.20

set block-policy return
scrub in on $ext_if all fragment reassemble
set skip on lo

table <jails> persist
nat on $ext_if from <jails> to any -> $ext_if

# container routes
rdr pass inet proto tcp from any to port 80 -> $caddy_addr port 8880
rdr pass inet proto tcp from any to port 443 -> $caddy_addr port 4443

# Enable dynamic rdr (see below)
rdr-anchor "rdr/*"

block in all
pass out quick modulate state
antispoof for $ext_if inet
pass in inet proto tcp from any to any port ssh flags S/SA keep state
```

Ceci est un fichier `pf.conf` standard pour `bastille`. Assurez-vous de modifier `caddy_addr` avec l'IP que vous avez choisie.

Maintenant, démarrons le pare-feu. Vous serez déconnecté de votre session `ssh` :

```
sysrc pf_enable="YES"
service pf start
```

Ensuite, configurons `bastille` :

```
# set up bastille networking
sysrc cloned_interfaces+=lo1
sysrc ifconfig_lo1_name="bastille0"
service netif cloneup

# bootstrap the base jail and start bastille
bastille bootstrap 12.1-RELEASE update
sysrc bastille_enable="YES"
service bastille start
```

Cela configurera votre réseau et récupérera la dernière jail de base par défaut que vous utiliserez plus tard.

Ensuite, configurons la jail :

```
bastille create caddy 12.1-STABLE 10.10.2.20
bastille start caddy
```

Puis installez `caddy`

```
#install the binary
fetch https://github.com/caddyserver/caddy/releases/download/v1.0.4/caddy_v1.0.4_freebsd_amd64.tar.gz
tar xvf caddy_v1.0.4_freebsd_amd64.tar.gz caddy
bastille cp caddy caddy /usr/local/bin/
rm caddy

#create the caddy user
bastille cmd caddy pw useradd caddy -m -s /usr/sbin/nologin

#install ca root file
bastille pkg caddy install ca_root_nss
```

Lors de l'installation de `ca_root_nss`, `pkg` devra s'initialiser. Acceptez les invites. Une fois terminé, nous passerons à l'étape suivante !

Une fois l'installation terminée, nous devons également configurer `caddy` pour qu'il démarre au démarrage. La manière la plus simple de le faire est d'utiliser ce script `rc.d` :

```sh
#!/bin/sh

# $FreeBSD: head/net/caddy/files/caddy.in 452063 2017-10-14 12:58:24Z riggs $
#
# PROVIDE: caddy
# REQUIRE: LOGIN
# KEYWORD: shutdown
#
# Add the following lines to /etc/rc.conf.local or /etc/rc.conf
# to enable this service:
#
# caddy_enable (bool):	Set to NO by default.
#				Set it to YES to enable caddy.
# caddy_user (user):		Set user to run caddy.
#				Default is "caddy".
# caddy_group (group):	Set group to run caddy.
#				Default is "caddy".
# caddy_conf (path):		Path to caddy configuration file.
#				Default is /usr/local/etc/caddyfile.conf

. /etc/rc.subr

name=caddy
rcvar=caddy_enable

load_rc_config $name

: ${caddy_enable:="NO"}
: ${caddy_user:="caddy"}
: ${caddy_group:="caddy"}
: ${caddy_conf:="/usr/local/etc/caddyfile.conf"}
: ${caddy_log:="/home/caddy/caddy.log"}
: ${caddy_env:="CADDYPATH=/home/caddy/"}
: ${caddy_https_port:="4443"}
: ${caddy_http_port:="8880"}

pidfile="/var/run/caddy.pid"
procname="/usr/local/bin/caddy"
command="/usr/sbin/daemon"
command_args="-f -p ${pidfile} /usr/bin/env ${caddy_env} ${procname} -agree -http-port ${caddy_http_port}  -https-port ${caddy_https_port} -conf=${caddy_conf} -log=${caddy_log} ${caddy_args}"
extra_commands="reload"

start_precmd=caddy_startprecmd
reload_cmd=caddy_reloadcmd

caddy_startprecmd()
{
      if [ ! -e ${pidfile} ]; then
              install -o ${caddy_user} -g ${caddy_group} /dev/null ${pidfile};
      fi
}

caddy_reloadcmd()
{
      kill -s USR1 $(cat ${pidfile})
}

run_rc_command "$1"
```

Supprimez l'exécutable `caddy` si vous ne l'avez pas déjà fait. Ensuite, créez un nouveau fichier avec `vi`. Ce sera votre script `rc.d` !

```
vi caddy
```

Collez le contenu du script ci-dessus, sauvegardez et quittez.

Assurez-vous que le fichier est exécutable en utilisant `chmod` et copiez-le dans le conteneur Caddy.

```
chmod +x caddy
bastille cp caddy caddy /usr/local/etc/rc.d/
```

Enfin, nous aurons besoin d'un Caddyfile. Voici un exemple :

```
stage.jaredwolff.com {
  tls hello@jaredwolff.com
  log /home/caddy/stage.jaredwolff.com.log
  root /var/www/stage.jaredwolff.com/
  gzip
  log stderr
}
```

`log` fait référence au journal d'accès spécifique à ce site.

`root` fait référence à l'emplacement du dossier racine `public` sur votre machine. Dans mon cas, c'est le chemin commun `/var/www/<nom du site>`. Définissez vos chemins et retenez-les. Nous en aurons besoin plus tard !

Pour que Caddy génère des certificats pour ce sous-domaine, vous devrez définir l'option *tls*. Un email est tout ce dont vous avez besoin.

Pour plus d'informations sur la structure du Caddyfile, [consultez la documentation](https://caddyserver.com/docs/caddyfile).

Créez un fichier appelé `caddyfile.conf` et copiez-le dans `/usr/local/etc/` dans votre conteneur Caddy :

```
vi caddyfile.conf
# Collez le contenu de votre caddyfile et sauvegardez
bastille cp caddy caddyfile.conf /usr/local/etc/
```

Vous devriez maintenant rediriger votre DNS vers l'IP du serveur. Ainsi, Caddy pourra générer/récupérer les certificats corrects. Ensuite, vous pouvez démarrer Caddy avec :

```
bastille service caddy caddy start
```

Vous pouvez vérifier le journal à `/usr/home/caddy/caddy.log` pour vous assurer que votre domaine a été provisionné correctement.

***Note de côté :*** La configuration avec les certificats SSL est difficile au début, surtout si vous migrez depuis un autre serveur. Votre site devra être indisponible pendant un petit moment pendant que vous changez vos paramètres DNS et démarrez `caddy`.

(C'est si vous utilisez `caddy` 1.0 standard. Vous pouvez également utiliser les plugins de fournisseur DNS [ici](https://github.com/caddyserver/dnsproviders) qui rendent les choses un peu plus faciles.)

Maintenant que nous avons `caddy` en cours d'exécution, il est temps de copier nos actifs générés par `hugo` en utilisant `rsync`. Nous passons à l'étape suivante !

## *Make* la construction et le déploiement faciles

![images/make.png](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/images/make.png)

Je passe beaucoup de temps à écrire du code C, et cela signifie que je passe beaucoup de temps à utiliser des Makefiles. Pour beaucoup, `make` (ou `gmake` pour GNU make) est le fléau de leur existence.

Pour la construction et le déploiement, `make` facilite la création de recettes réutilisables. Ainsi, vous savez que vous pouvez déployer en toute confiance à chaque fois.

Mon Makefile s'inspire de celui que [Victoria Drake avait publié](https://victoria.dev/blog/a-portable-makefile-for-continuous-delivery-with-hugo-and-github-pages/) il n'y a pas si longtemps. Je l'ai un peu modifié pour répondre à mes besoins.

Faisons un tour et voyons ce qu'il y a à l'intérieur :

```Makefile
.POSIX:

HUGO_VERSION := 0.66.0

OPTIMIZED_DIR := optimized
CONTENT_DIR := content
DEST_DIR := public

SERVER := 123.456.789.10
USER := user
```

La première section contient toutes les variables que j'utilise pour indiquer aux fonctions plus tard ce qu'elles doivent faire. Elle contient également une référence à la cible `.POSIX`. Cela signifie que le Makefile sera aussi portable entre différentes versions de `make`.

Ensuite, j'ai ajouté une logique pour déterminer si je déploie en *stage* ou en *production* :

```Makefile
# Définir l'endroit où il est déployé.
ifdef PRODUCTION
$(info Construction pour la production. ?)
TARGET := www
else
$(info Construction pour le développement. ?)
BASEURL := --baseURL "https://stage.jaredwolff.com"
TARGET := stage
endif
```

Par défaut, les recettes ci-dessous utiliseront le flux de travail de développement. Pour utiliser le flux de travail de production, vous pouvez invoquer `make` comme ceci :

```Makefile
PRODUCTION=1 make build
```

Cela ajoute une friction supplémentaire au processus de déploiement. C'est une bonne étape cependant. Ainsi, vous êtes sûr que le déploiement se fait au bon endroit !

```Makefile
# Chemin complet
DEPLOY_DIR := /usr/local/bastille/jails/caddy/root/path/to/$(TARGET).jaredwolff.com
```

En utilisant la variable `TARGET` ci-dessus, je définis ensuite le chemin vers mes actifs serveur. J'utilise Bastille pour organiser mes jails, donc le chemin est extra long. (oui, très long) Cela nous permet d'utiliser `rsync` pour déployer les fichiers avec facilité.

Maintenant, voici les parties amusantes. Pour effectuer un redimensionnement en masse complet, j'utilise la fonctionnalité `wildcard` du Makefile.

```Makefile
IMAGES := \
$(wildcard $(CONTENT_DIR)/*/images/*.jpg) \
$(wildcard $(CONTENT_DIR)/*/images/*.JPG) \
$(wildcard $(CONTENT_DIR)/*/images/*.jpeg) \
$(wildcard $(CONTENT_DIR)/*/images/*.png) \
$(wildcard $(CONTENT_DIR)/*/*/images/*.jpg) \
$(wildcard $(CONTENT_DIR)/*/*/images/*.jpeg) \
$(wildcard $(CONTENT_DIR)/*/*/images/*.png) \
$(wildcard $(CONTENT_DIR)/*/*/images/*.JPG) \
```

Dans ce cas, il créera une liste délimitée par des espaces de chaque image qui se trouve dans mon répertoire de contenu. Le plus gros inconvénient de cette méthode est qu'elle n'est pas tolérante aux espaces. Une solution facile à ce problème est de s'assurer que toutes mes photos n'ont pas d'espaces.

Voici une commande bash rapide et sale que vous pouvez utiliser pour renommer les fichiers qui ont des espaces et les remplacer par des caractères '_' :

```Makefile
for f in *\ *; do mv "$f" "${f// /_}"; done
```

Ensuite, nous renommons ces entrées de sorte que le préfixe soit maintenant le répertoire cible. Cela sera utile lorsque nous voudrons redimensionner :

```Makefile
OPTIMIZED_IMAGES := \
$(subst $(CONTENT_DIR)/,$(OPTIMIZED_DIR)/,$(IMAGES))
```

Maintenant, regardez la recette `optimize` :

```Makefile
.PHONY: optimize
optimize: build $(OPTIMIZED_IMAGES)
@echo "? Optimisation des images"
rsync -r $(OPTIMIZED_DIR)/ $(DEST_DIR)/
du -sh $(CONTENT_DIR)/
du -sh $(DEST_DIR)/

$(OPTIMIZED_IMAGES):
convert -strip -compress JPEG -resize '730>' $(subst $(OPTIMIZED_DIR)/,$(CONTENT_DIR)/,$@) $@
```

Il appelle d'abord la recette `build` puis aussi la recette `$(OPTIMIZED_IMAGES)`. Cette dernière optimisera l'image en utilisant la commande `convert` de [Imagemagick](https://imagemagick.org/script/convert.php). Dans ce cas, je ne redimensionne que les fichiers qui sont plus larges que 730px. Changez le vôtre en conséquence pour que vous puissiez profiter des avantages d'un [site optimisé](https://www.jaredwolff.com/seven-ways-to-optimize-your-site-for-speed/).

Après le redimensionnement, la recette utilise `rsync` pour copier les fichiers du `OPTIMIZED_DIR` vers `DEST_DIR`.

Si nous regardons la recette `build`, je construis d'abord les actifs. Ensuite, je copie les photos du répertoire `content` vers le répertoire `optimized`. Le point positif est que `rsync` ne déplacera que les fichiers qui ont changé. Ainsi, il n'a pas à copier les fichiers encore et encore à chaque fois que vous construisez.

Enfin, la recette `deploy`.

```Makefile
.PHONY: deploy
deploy:
@echo rsync vers $(DEPLOY_DIR)
@rsync -r --del public/ $(USER)@$(SERVER):$(DEPLOY_DIR)/
@echo création d'un instantané restic
@scp scripts/backup.sh $(USER)@$(SERVER):/root/backup.sh
@ssh $(USER)@$(SERVER) sh /root/backup.sh $(DEPLOY_DIR)
@echo "? Le site est déployé !"
```

Vous pouvez voir à nouveau que j'utilise rsync pour synchroniser le contenu de `public/` avec le serveur. Assurez-vous de définir `USER`, `SERVER` et `DEPLOY_DIR`. Dans mon cas, `DEPLOY_DIR` devient `/usr/local/bastille/jails/caddy/root/var/www/www.jaredwolff.com`

Lorsque vous obtenez enfin un déploiement réussi, vous pouvez double-vérifier que tout est à la bonne place. Ensuite, une fois que tout semble bon, vous pouvez démarrer votre serveur caddy en utilisant :

```
bastille service caddy caddy start
```

`deploy` fera également quelque chose d'utile ici. Il déployera mon script de sauvegarde `restic` et l'exécutera. Je parlerai de cela plus en détail dans la section sauvegarde.

En fin de compte, voici le Makefile complet :

```Makefile
.POSIX:

HUGO_VERSION := 0.66.0

OPTIMIZED_DIR := optimized
CONTENT_DIR := content
DEST_DIR := public

SERVER := 155.138.230.8
USER := root

# Définir l'endroit où il est déployé.
ifdef PRODUCTION
$(info Construction pour la production. ?)
TARGET := www
else
$(info Construction pour le développement. ?)
BASEURL := --baseURL "https://stage.jaredwolff.com"
TARGET := stage
endif

# Chemin complet
DEPLOY_DIR := /usr/local/bastille/jails/caddy/root/var/www/$(TARGET).jaredwolff.com

IMAGES := \
$(wildcard $(CONTENT_DIR)/*/images/*.jpg) \
$(wildcard $(CONTENT_DIR)/*/images/*.JPG) \
$(wildcard $(CONTENT_DIR)/*/images/*.jpeg) \
$(wildcard $(CONTENT_DIR)/*/images/*.png) \
$(wildcard $(CONTENT_DIR)/*/*/images/*.jpg) \
$(wildcard $(CONTENT_DIR)/*/*/images/*.jpeg) \
$(wildcard $(CONTENT_DIR)/*/*/images/*.png) \
$(wildcard $(CONTENT_DIR)/*/*/images/*.JPG) \

OPTIMIZED_IMAGES := \
$(subst $(CONTENT_DIR)/,$(OPTIMIZED_DIR)/,$(IMAGES))

.PHONY: all
all: build optimize

.PHONY: clean
clean:
rm -rf public/
rm -rf optimized/

.PHONY: serve
serve:
@hugo serve -D

.PHONY: ssh
ssh:
@ssh $(USER)@$(SERVER)

.PHONY: build
build:
@echo "? Génération du site"
hugo --gc --minify -d $(DEST_DIR) $(BASEURL)
rsync -av --del -f"+ */" -f"- *" $(CONTENT_DIR)/ $(OPTIMIZED_DIR)/

.PHONY: optimize
optimize: build $(OPTIMIZED_IMAGES)
@echo "? Optimisation des images"
rsync -r $(OPTIMIZED_DIR)/ $(DEST_DIR)/
du -sh $(CONTENT_DIR)/
du -sh $(DEST_DIR)/

$(OPTIMIZED_IMAGES):
convert -strip -compress JPEG -resize '730>' $(subst $(OPTIMIZED_DIR)/,$(CONTENT_DIR)/,$@) $@

.PHONY: deploy
deploy:
@echo rsync vers $(DEPLOY_DIR)
@rsync -r --del public/ $(USER)@$(SERVER):$(DEPLOY_DIR)/
@echo création d'un instantané restic
@scp scripts/backup.sh $(USER)@$(SERVER):/root/backup.sh
@ssh $(USER)@$(SERVER) sh /root/backup.sh $(DEPLOY_DIR)
@echo "? Le site est déployé !"
```

Il y a quelques autres pépites utiles que vous pourriez vouloir utiliser. `clean`, `serve` et `ssh` ont été très utiles pour les tests et la connexion.

En fin de compte, vous aurez un processus de déploiement en deux étapes. La première génère votre site avec des images optimisées. La seconde consiste à déployer sur un serveur pour l'hébergement statique.

## Sauvegarde incrémentielle

![images/Backup.png](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/images/Backup.png)

Après avoir découvert [Restic](https://restic.net), j'ai été convaincu de son utilité pour toutes mes besoins de sauvegarde incrémentielle. Dans le cas de mon serveur, je l'utilise pour sauvegarder le dossier racine de mon site. Ainsi, si j'ai besoin de revenir en arrière, je peux le faire en quelques étapes.

Voici comment vous pouvez configurer un dépôt `restic` local.

### Configuration

L'initialisation du dépôt est simple. La partie la plus importante est de vous assurer de **ne pas perdre/oublier votre mot de passe !**

```
    # restic init -r /root/backups
    enter password for new repository:
    enter password again:
    created restic repository 32e14c7052 at /root/backups

    Please note that knowledge of your password is required to access
    the repository. Losing your password means that your data is
    irrecoverably lost.
```

Définissez la variable d'environnement `RESTIC_PASSWORD` pour éviter d'entrer votre mot de passe. Pour la rendre permanente, vous devrez placer `export RESTIC_PASSWORD="Votre mot de passe ici !"` dans le fichier `.profile` dans `/root/`.

### Sauvegarde

Invoquer `restic` via SSH est difficile. Donc, notre meilleure option ?

Transférer un script shell (très bref) sur le serveur et l'exécuter après un déploiement. Voici le contenu de ce que j'utilise aujourd'hui :

```sh
#!/bin/sh
export RESTIC_PASSWORD="Votre mot de passe ici !"
restic backup $1 -r /root/backups/
```

***Note de côté :*** Alors que je suis assis ici et que je regarde ce script, pour des raisons de sécurité, vous pouvez remplacer "Votre mot de passe ici !" par $2 qui est le deuxième argument du script. Ainsi, vous n'avez pas besoin de commiter/pousser le mot de passe stocké dans un fichier statique !

Cela définit d'abord votre mot de passe de sauvegarde. Ensuite, il exécute `restic` en utilisant le premier argument de la ligne de commande comme chemin. Donc, pour exécuter une sauvegarde avec ce script, cela ressemblerait à ceci :

```
./backup.sh /path/to/your/public/folder/
```

**Note :** vous devez initialiser votre sauvegarde `restic` *avant* de commencer à sauvegarder. Sinon, cela échouera !

Dans mon cas, je place les sauvegardes incrémentielles dans un dossier différent de ma machine. Ainsi, elles sont facilement accessibles et *rapides*.

### Visualisation de vos sauvegardes

Pour visualiser vos sauvegardes, vous pouvez exécuter la commande suivante :

    # restic snapshots -r /root/backups -g paths -c
    enter password for repository:
    repository e140b5e4 opened successfully, password is correct
    snapshots for (paths [/usr/local/bastille/jails/caddy/root/var/www/www.jaredwolff.com]):
    ID        Time                 Host         Tags
    --------------------------------------------------
    d3328066  2020-03-10 00:30:58  vultr.guest
    f3360819  2020-03-10 04:03:03  vultr.guest
    231dd134  2020-03-10 04:44:00  vultr.guest
    3c1be26a  2020-03-10 04:56:19  vultr.guest
    e96c947c  2020-03-10 05:03:00  vultr.guest
    34c3682a  2020-03-10 14:01:37  vultr.guest
    fbccdb8c  2020-03-10 14:04:26  vultr.guest
    9ce11146  2020-03-10 15:38:49  vultr.guest
    046b3da3  2020-03-10 15:47:06  vultr.guest
    9c28d4bc  2020-03-10 15:48:25  vultr.guest
    469dc228  2020-03-10 15:48:54  vultr.guest
    6f78af72  2020-03-10 17:00:21  vultr.guest
    29ad17b2  2020-03-10 20:18:23  vultr.guest
    ed22ce1f  2020-03-10 20:20:24  vultr.guest
    9c8c1b03  2020-03-11 13:56:40  vultr.guest
    b6cfcfec  2020-03-11 14:08:14  vultr.guest
    e8546005  2020-03-11 14:27:22  vultr.guest
    49a134fe  2020-03-17 00:47:58  vultr.guest
    c0beb283  2020-03-18 20:44:52  vultr.guest
    --------------------------------------------------

Vous pouvez utiliser cette liste pour déterminer si vous devez revenir en arrière sur un déploiement.

### Restauration

La restauration à partir d'une sauvegarde, surtout dans un environnement en direct, doit être rapide. Après avoir visualisé vos sauvegardes, vous pouvez restaurer une sauvegarde spécifique en utilisant son *ID*.

```
restic restore d3328066
```

Cela restaurera les fichiers à la sauvegarde faite le *2020-03-10 00:30:58*. Super. De plus, il ne réécrira pas chaque fichier. Il appliquera uniquement les différences entre l'état actuel et l'état stocké.

## Conclusion

Nous avons couvert beaucoup de terrain dans cet article. Vous avez appris comment :

- Déployer votre propre serveur en utilisant Vultr
- Utiliser Bastille pour créer des jails de type conteneur
- Configurer Caddy pour servir des actifs de fichiers statiques avec TLS
- Déployer les fichiers en utilisant un Makefile assez simple et `rsync`
- Sauvegarder après chaque déploiement en utilisant `restic`

En fin de compte, nous avons une plateforme robuste, sécurisée et simple pour l'hébergement de fichiers et de services statiques.

Restez à l'écoute, car d'autres articles comme celui-ci arriveront bientôt ! En attendant, consultez mes [autres articles](https://www.jaredwolff.com/blog/).

Merci d'avoir lu et à la prochaine ! ?

**Vous pouvez trouver d'autres articles comme celui-ci sur [www.jaredwolff.com](https://www.jaredwolff.com/my-latest-self-hosted-hugo-workflow/).**