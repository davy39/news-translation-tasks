---
title: 'Comment gérer les Snaps Ubuntu : les choses que personne ne vous dit'
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-08-19T13:23:00.000Z'
originalURL: https://freecodecamp.org/news/managing-ubuntu-snaps
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/lego.svg
tags:
- name: Linux
  slug: linux
- name: 'snaps '
  slug: snaps
- name: System administration
  slug: system-administration
- name: Ubuntu
  slug: ubuntu
seo_title: 'Comment gérer les Snaps Ubuntu : les choses que personne ne vous dit'
seo_desc: Canonical’s Snaps are definitely the real deal. The secure and portable
  Linux package management system is more than a geeky tool for showing off your tech
  creds. Just consider the growing list of companies that have already bought in and
  are providi...
---

[Les Snaps de Canonical](https://snapcraft.io/) sont définitivement la vraie affaire. Le système de gestion de paquets Linux sécurisé et portable est bien plus qu'un outil geek pour montrer vos compétences techniques. Il suffit de considérer la [liste croissante](https://snapcraft.io/store) d'entreprises qui ont déjà adopté cette solution et fournissent leur logiciel de bureau via des snaps, notamment Blender, Slack, Spotify, Android Studio et Visual Studio Code de Microsoft (Microsoft !). Et n'oubliez pas que la véritable croissance du système snap se situe dans le monde des appareils IoT et des serveurs plutôt que sur les bureaux.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-138.png)
_Le site snapcraft.io : où les développeurs et utilisateurs de snaps se rencontrent_

Mais à mesure que la popularité des snaps grandit — certaines nouvelles distributions Linux viennent avec le service snapd installé par défaut — vous pourriez être pardonné de vous demander comment vous êtes censé les faire fonctionner. Ne vous méprenez pas : il existe toutes sortes de guides en ligne pour trouver, installer et supprimer des snaps. Et il y a des endroits où les développeurs peuvent obtenir de l'aide pour construire leurs applications en tant que snaps. Mais pour l'instant, je parle de la _configuration_ de leur comportement ou du _dépannage_ lorsque les choses tournent mal.

Pour le record, vous recherchez de nouveaux snaps à installer en utilisant quelque chose comme :

```
snap find aws
```

Lorsque vous trouvez un paquet qui vous plaît, vous l'installez en utilisant :

```
snap install aws-cli
```

Oh, et vous les supprimez avec remove.

```
snap remove aws-cli
```

Voilà. Vous ne pouvez pas dire que je ne vous ai jamais appris quelque chose. Mais ce n'est pas de cela que parle cet article. Ce dont nous allons parler, c'est de la vraie gestion, comme changer les configurations ou dépanner les choses qui ont cassé.

## Comprendre le système de fichiers snap

Comment cela va-t-il être différent de la manière dont vous le feriez normalement sur Linux ? Les fichiers de configuration sont généralement dans _/etc/_, les processus révèlent leurs secrets les plus profonds via _systemctl_, et les logs trouvent leur chemin vers _/var/log/_.

Pas si vite, mon ami. Ce n'est pas toujours ainsi que les choses fonctionnent dans Snapland. Vous voyez, un snap n'est vraiment rien de plus qu'un seul fichier compressé (nommé avec l'extension _.snap_) contenant l'ensemble du système de fichiers nécessaire pour exécuter un paquet. Ces fichiers ne sont jamais réellement décompressés et « installés », mais sont montés dynamiquement au moment de l'exécution et exposés à l'utilisateur comme un environnement virtuel.

Cela signifie que les ressources utilisées par un programme peuvent ne pas exister réellement sur le système hôte. Ainsi, par exemple, le snap Nextcloud crée ses propres versions d'Apache et de MySQL pour son backend. Donc, si vous voulez configurer un nouvel hôte virtuel dans _/etc/apache2/sites-available/_ ou créer un nouvel utilisateur MySQL de manière traditionnelle, vous n'avez pas de chance.

Les avantages de cette approche sont significatifs : l'installation et la configuration seront généralement beaucoup plus fluides et vous aurez beaucoup moins de risques de rencontrer des problèmes de dépendances et de conflits. Mais cela semble aussi signifier que vous avez moins d'accès aux organes vitaux qui alimentent votre logiciel.

Alors, où tout cela se passe-t-il ? Jetez un coup d'œil à votre système de fichiers hôte : vous trouverez probablement plus de répertoires snap que vous ne pouvez en secouer un bâton (si vous en avez envie). Voici les répertoires que le processus d'installation de snap a probablement créés :

/snap/  
/var/snap/  
/var/lib/snapd/  
/home/username/snap/

Autant que ça ? Pour quoi faire ? Passons-les en revue un par un. N'hésitez pas à explorer votre propre machine Linux pour voir tout cela par vous-même.

Les fichiers _.snap_ réels sont conservés dans le répertoire _/var/lib/snapd/snaps/_. Lors de l'exécution, ces fichiers seront montés dans le répertoire racine _/snap/_. En regardant là-bas — dans le sous-répertoire /snap/core/ — vous verrez ce qui ressemble à un système de fichiers Linux régulier. Il s'agit en fait du système de fichiers virtuel utilisé par les snaps actifs.

```
ls /snap/core/current
bin   dev  home  lib64  meta  opt   root  sbin  srv  tmp  var
boot  etc  lib   media  mnt   proc  run   snap  sys  usr  writable
```

Et voici un sous-répertoire contenant des fichiers de configuration (en lecture seule) utilisés par le snap Nextcloud. Cela ne sera là, bien sûr, que si vous avez installé Nextcloud (_snap install nextcloud_).

```
ls /snap/nextcloud/current/conf/
httpd.conf  mime.types  ssl.conf
```

Ok. Maintenant, qu'en est-il de _/var/snap/_ ? Très similaire aux habitants traditionnels de _/var/_, les fichiers dans _/var/snap/_ contiennent diverses formes de données utilisateur et de fichiers de log — le genre de données générées et consommées par les applications pendant les opérations. Cet exemple montre des répertoires pour les données utilisées par certains snaps liés au bureau, y compris l'AWS CLI et l'outil de communication d'équipe Slack. (OK, techniquement parlant, l'AWS CLI n'est pas un outil de bureau.)

```
ls /var/snap
aws-cli  core18           gnome-system-monitor  gnome-calculator
brave    gnome-3-26-1604  gnome-characters      gtk-common-themes
core     gnome-3-28-1804  gnome-logs            slack
```

Plongez profondément dans les sous-répertoires de _/var/snap/_ sur votre machine et voyez ce que vous pouvez découvrir.

Il reste le répertoire _~/snap_ qui existe dans le répertoire personnel d'un utilisateur sur au moins certains systèmes de fichiers Linux. Il contiendra des répertoires utilisant certains des noms que vous verrez dans /var/snap. Que se passe-t-il là-dedans ?

```
ls ~/snap
aws-cli  brave  gnome-calculator  slack
```

Pour autant que je sache, ces répertoires sont destinés à stocker des données versionnées liées aux paramètres utilisés par votre compte utilisateur.

## Outils d'administration des snaps

Jusqu'à présent, je vous ai montré comment trouver diverses classes de données conservées dans les fichiers de configuration (dans _/var/snap/_), les systèmes de fichiers virtuels (_/snap/_) et les collections de paramètres utilisateur (_~/snap_). Je vous ai également montré où _ne pas_ chercher — _/var/lib/snapd/_ — où les fichiers .snap eux-mêmes résident ; rien à voir ici, continuez.

Maintenant, qu'en est-il de l'administration réelle ? C'est un peu plus compliqué. Certains snaps — comme Nextcloud — exposent une interface d'administration complète. J'en parle dans [mon article sur l'administration de Nextcloud en tant que Snap](https://www.freecodecamp.org/news/snapd-nextcloud/). Mais il semble que la simplicité des snaps signifie parfois qu'il n'y a tout simplement pas beaucoup de configuration manuelle possible.

Cependant, ce n'est pas toujours le cas. Mais d'abord, vous devrez connaître les _services snap_. Certaines applications plus complexes nécessitent des piles logicielles multi-couches. Nextcloud, par exemple, crée et gère ses propres versions d'Apache, MySQL, PHP et Redis. Chacune de ces « couches » est, en termes de snap, appelée un service.

Si des snaps installés sur votre machine ont leurs propres services, vous pourrez les lister avec leur statut en utilisant cette commande snapd :

```
snap services
Service                    Startup  Current   Notes
nextcloud.apache           enabled  active    -
nextcloud.mdns-publisher   enabled  active    -
nextcloud.mysql            enabled  active    -
nextcloud.nextcloud-cron   enabled  active    -
nextcloud.nextcloud-fixer  enabled  inactive  -
nextcloud.php-fpm          enabled  active    -
nextcloud.redis-server     enabled  active    -
nextcloud.renew-certs      enabled  active    -
```

Vous pouvez également contrôler l'état d'exécution et de démarrage d'un service. Cet exemple arrêtera le service Apache de Nextcloud et s'assurera qu'il ne se lance pas lorsque le système redémarre (bien que, rappelez-vous simplement que cela désactivera Nextcloud — vous ne voulez probablement pas faire cela) :

```
snap stop --disable nextcloud.apache
```

Vous pouvez également utiliser systemctl pour gérer les processus de service snap :

```
systemctl status snap.nextcloud.apache
```

Si votre snap inclut au moins un service, vous pouvez afficher ses logs en utilisant snapd :

```
snap logs nextcloud
```

Vous pouvez également spécifier un service particulier :

```
snap logs nextcloud.mysql
```

Pour certains snaps (comme Nextcloud), snapd rend les configurations utiles disponibles depuis la ligne de commande. Vous pouvez afficher les paramètres disponibles en utilisant _snap get_ :

```
snap get nextcloud
Key        Value
mode       production
nextcloud  {...}
php        {...}
ports      {...}
private    {...}
```

Descendez d'un niveau en ajoutant le nom d'un paramètre spécifique. Cet exemple nous montre que Nextcloud écoute actuellement uniquement sur les ports 80 (HTTP) et 443 (HTTPS).

```
snap get nextcloud ports
Key          Value
ports.http   80
ports.https  443
```

Vous pourriez changer un paramètre en utilisant la commande _set_. Celui-ci indiquerait à Nextcloud d'écouter sur le port 8080 pour les requêtes HTTP non sécurisées au lieu de 80.

```
snap set nextcloud ports.http=8080
```

Snapd offre également quelques paramètres de configuration système qui sont [décrits ici](https://docs.snapcraft.io/system-options/87), la documentation des [variables d'environnement est maintenue ici](https://docs.snapcraft.io/environment-variables/7983), et des informations sur [la mise à jour de vos snaps peuvent être trouvées ici](https://docs.snapcraft.io/keeping-snaps-up-to-date/7022).

Tout cela vous permettra de commencer lorsque les choses ont besoin d'être réparées. Alors, mettez-vous au travail.

_Vous cherchez plus ? Vous pourriez apprécier mes [livres et cours Pluralsight](https://bootstrap-it.com/) sur les sujets liés à Linux, AWS et Docker._