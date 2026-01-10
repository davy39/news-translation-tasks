---
title: Comment trouver et modifier un fichier Hosts sous Windows
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-11-18T12:17:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-find-and-edit-a-windows-hosts-file
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fd324f7e6787e098393d3ee.jpg
tags:
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_title: Comment trouver et modifier un fichier Hosts sous Windows
seo_desc: 'While the internet is only about 30 years old, in many ways the hosts file
  is a relic of its (not so ancient) past.

  In most cases you probably won''t need to update your hosts file on Windows. But
  knowing where it is and how it works can be helpful if...'
---

Bien que l'internet n'ait qu'environ 30 ans, le fichier hosts est en quelque sorte un vestige de son passé (pas si ancien).

Dans la plupart des cas, vous n'aurez probablement pas besoin de mettre à jour votre fichier hosts sous Windows. Mais savoir où il se trouve et comment il fonctionne peut être utile si :

* vous avez des problèmes avec le développement local
* vous suspectez qu'un malware a modifié le fichier hosts
* vous voulez une méthode rapide et simple pour bloquer certains sites web
* ou si vous voulez configurer des raccourcis utiles vers des adresses IP internes

Dans cet article, nous allons couvrir [ce qu'est un fichier hosts](#quest-ce-quun-fichier-hosts), [comment l'éditer sous Windows](#comment-editer-un-fichier-hosts-sous-windows), et nous passerons en revue [quelques astuces](#comment-utiliser-le-fichier-hosts-sous-windows-10-pour-bloquer-des-sites-web) que vous pouvez faire avec.

## Qu'est-ce qu'un fichier hosts ?

À l'époque des débuts de l'internet, avant qu'il ne se généralise, les ordinateurs utilisaient un fichier hosts pour mapper les longues adresses IP, difficiles à mémoriser, avec des noms d'hôtes beaucoup plus courts et plus faciles à retenir.

Par exemple, voici une ligne que vous trouverez dans de nombreux fichiers hosts sous Windows, Linux et macOS :

```
127.0.0.1       localhost
```

Ainsi, au lieu de devoir mémoriser une longue adresse IP, il suffisait de visiter localhost.

### Pourquoi les fichiers hosts sont tombés en désuétude

Le système des fichiers hosts fonctionnait bien pour les débuts de l'internet, mais il y avait quelques problèmes majeurs.

Avec la croissance de l'internet, la longueur et la complexité des fichiers hosts ont également augmenté. De plus, chaque fichier hosts ne fonctionnait que pour l'ordinateur sur lequel il se trouvait, et les maintenir synchronisés avec les changements de noms d'hôtes et d'adresses IP est devenu un véritable casse-tête.

Par exemple, imaginez que vous avez deux ordinateurs, A et B. Leurs fichiers hosts contiennent cette mapping pour google.com :

```
172.217.26.46       google.com
```

Mais lorsque Google met à jour ses adresses IP, seul l'ordinateur A met à jour son fichier hosts pour correspondre :

```
172.217.175.78       google.com
```

Ainsi, tout le monde sur l'ordinateur B reste sans Google jusqu'à ce que quelqu'un met à jour le fichier hosts. Lorsque cette personne met à jour le fichier hosts, elle ajoute une autre entrée pour gérer Google avec le sous-domaine www.

```
172.217.175.78       google.com
172.217.175.78       www.google.com
```

Maintenant, tout le monde sur l'ordinateur B est redirigé vers le site web correct, qu'ils visitent google.com ou www.google.com.

Et tout le monde sur l'ordinateur A ne peut visiter que google.com, et non www.google.com, au moins jusqu'à ce que son propre fichier hosts soit mis à jour pour correspondre.

Comme vous pouvez l'imaginer, les fichiers hosts devenaient compliqués, rapidement.

### La solution

Si vous pensez que quelqu'un aurait dû simplement créer un dépôt central pour mapper toutes les adresses IP avec tous les noms d'hôtes, c'est exactement ce qui s'est passé.

Dès le début, un fichier hosts central était maintenu manuellement et partagé par le Stanford Research Institute. Ce système a conduit à l'invention des domaines et des domaines de premier niveau comme .com et .edu, Whois, et il est devenu de plus en plus automatisé.

En fin de compte, le modeste fichier hosts et des innovateurs comme [Elizabeth J. Feinler](https://en.wikipedia.org/wiki/Elizabeth_J._Feinler) ont conduit à l'invention du Domain Name System encore utilisé aujourd'hui.

## Comment éditer un fichier hosts sous Windows

Pour éditer un fichier hosts sous Windows 10, vous devrez l'ouvrir en tant qu'administrateur.

Tout d'abord, ouvrez le Bloc-notes en tant qu'administrateur en appuyant sur la touche Windows, en tapant "bloc-notes", et en cliquant sur "Exécuter en tant qu'administrateur" :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image.png)
_Note : Vous devrez peut-être cliquer sur le bouton flèche pour développer le menu déroulant et voir l'option "Exécuter en tant qu'administrateur"_

Pour ouvrir le fichier hosts dans le Bloc-notes, cliquez sur "Fichier", "Ouvrir", et naviguez jusqu'à `C:\Windows\System32\drivers\etc`.

Vous ne pourrez pas voir de fichiers dans ce répertoire car ils ne sont pas des documents texte. Pour changer le type de fichier, cliquez sur le menu déroulant en bas à droite du menu Ouvrir et cliquez sur "Tous les fichiers" :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-1.png)

Vous verrez un fichier nommé `hosts`. Double-cliquez sur ce fichier pour l'ouvrir.

Ensuite, vous verrez un fichier hosts similaire à ceci :

```
# Copyright (c) 1993-2009 Microsoft Corp.
#
# Ce fichier HOSTS est un exemple utilisé par Microsoft TCP/IP pour Windows.
#
# Ce fichier contient les mappings des adresses IP aux noms d'hôtes. Chaque
# entrée doit être conservée sur une ligne individuelle. L'adresse IP doit
# être placée dans la première colonne suivie du nom d'hôte correspondant.
# L'adresse IP et le nom d'hôte doivent être séparés par au moins un
# espace.
#
# De plus, des commentaires (comme ceux-ci) peuvent être insérés sur des lignes individuelles
# ou suivant le nom de la machine désigné par un symbole '#'.
#
# Par exemple :
#
#      102.54.94.97     rhino.acme.com          # serveur source
#       38.25.63.10     x.acme.com              # hôte client x

# La résolution du nom localhost est gérée au sein du DNS lui-même.
#	127.0.0.1       localhost
#	::1             localhost
```

Notez que tout est commenté avec des caractères `#`, ce qui signifie que rien n'est réellement lu à partir du fichier hosts. Les versions modernes de Windows incluent un système de type DNS, donc si vous visitez localhost, il vous redirigera automatiquement vers `127.0.0.1`.

Cela étant dit, voici quelques choses que vous pouvez faire avec le fichier hosts.

## Comment mettre à jour le fichier hosts sous Windows 10 si vous avez des problèmes avec localhost

Si vous faites du développement local et que vous avez des problèmes avec localhost, vous pouvez simplement supprimer les commentaires de votre fichier hosts :

```
...
# La résolution du nom localhost est gérée au sein du DNS lui-même.
127.0.0.1       localhost
::1             localhost
```

Après avoir sauvegardé le fichier hosts, fermez le Bloc-notes.

Ensuite, ouvrez PowerShell en appuyant sur la touche Windows, en recherchant "powershell", et en cliquant sur "Exécuter en tant qu'administrateur" :

![Capture d'écran montrant comment ouvrir PowerShell en tant qu'administrateur](https://www.freecodecamp.org/news/content/images/2020/12/powershell-run-as-administrator-1.jpg)

Dans la fenêtre PowerShell, entrez `ipconfig /flushdns` pour vider le DNS intégré de Windows :

![Capture d'écran montrant comment vider le DNS Windows avec PowerShell](https://www.freecodecamp.org/news/content/images/2020/12/image-85.png)

Après cela, vous devriez pouvoir visiter localhost dans votre navigateur et voir ce sur quoi vous travaillez. Si vous avez toujours des problèmes, essayez de fermer complètement votre navigateur, puis ouvrez une nouvelle fenêtre de navigateur et réessayez.

## Comment mettre à jour votre fichier hosts sous Windows 10 si vous pensez qu'il a été modifié

Même si les fichiers hosts sont tombés en désuétude avec des systèmes plus récents comme le DNS, ils fonctionnent toujours pour des raisons de compatibilité. Et les pirates ont définitivement tiré parti de cela dans le passé.

Ce qu'ils faisaient, c'était pointer un site web courant comme google.com vers une adresse IP non sécurisée. Cette adresse IP pouvait servir un site qui ressemble exactement à celui de Google, mais qui essaie en réalité de voler vos informations sensibles.

Bien que cela ait été un problème dans le passé, la plupart des logiciels de sécurité comme la Suite de Sécurité Windows peuvent reconnaître et corriger les problèmes avec le fichier hosts automatiquement.

Cela dit, si vous ouvrez votre fichier hosts et que vous voyez beaucoup d'entrées étranges, vous voudrez peut-être revenir au fichier hosts par défaut de Windows.

Il suffit de copier et coller le fichier hosts par défaut de plus tôt dans l'article dans votre fichier hosts et de sauvegarder. Ensuite, ouvrez PowerShell et utilisez la commande `ipconfig /flushdns` pour vider le DNS Windows.

Notez que certains logiciels de sécurité tiers utilisent le fichier hosts pour bloquer les sites web dangereux. Si c'est le cas, pas de souci – votre logiciel de sécurité devrait ajouter toutes ces entrées à votre fichier hosts. Nous verrons comment cela fonctionne dans la section suivante.

## Comment utiliser le fichier hosts sous Windows 10 pour bloquer des sites web

Vous ne voulez pas que vos amis ou votre famille visitent certains sites web sur votre ordinateur ? Ou êtes-vous comme moi et vous laissez distraire par toutes les photos de chats sur l'internet ?

Si c'est le cas, vous pouvez utiliser le fichier hosts pour bloquer complètement les sites web.

Par exemple, si vous voulez bloquer Reddit, ajoutez simplement ceci au bas de votre fichier hosts :

```
127.0.0.1     reddit.com
127.0.0.1     www.reddit.com
```

Ensuite, ouvrez PowerShell et exécutez `ipconfig /flushdns` pour vider le DNS Windows 10. De plus, fermez les fenêtres du navigateur qui sont ouvertes et rouvrez-les.

Après cela, chaque fois que vous essayez de visiter Reddit, ou que vous cliquez sur une URL Reddit comme [https://www.reddit.com/r/FreeCodeCamp/](https://www.reddit.com/r/FreeCodeCamp/), votre navigateur sera redirigé vers `127.0.0.1`, ou localhost.

Comme il n'y a pas de site web là-bas, votre navigateur affichera un message d'erreur :

![Capture d'écran du message d'erreur après avoir bloqué reddit.com dans le fichier hosts et l'avoir visité dans le navigateur](https://www.freecodecamp.org/news/content/images/2020/12/image-86.png)

Le seul inconvénient est que cela ne fonctionne que sur un seul appareil – vous pourriez simplement prendre votre téléphone et naviguer sur Reddit dessus. Néanmoins, c'est une méthode astucieuse pour créer une certaine friction sur votre ordinateur de travail.

Cela nous amène à la dernière astuce, qui consiste à utiliser le fichier hosts pour faciliter un peu votre vie.

## Comment utiliser le fichier hosts sous Windows 10 pour configurer des raccourcis utiles

Si vous passez beaucoup de temps à ajuster les paramètres de votre routeur, ou si vous avez un projet sympa en cours sur un [Raspberry Pi](https://www.freecodecamp.org/news/build-a-personal-dev-server-on-a-5-dollar-raspberry-pi/), vous savez que taper une longue adresse IP est fastidieux.

Au lieu de cela, vous pouvez utiliser le fichier hosts pour rendre la connexion à d'autres appareils sur votre réseau local beaucoup plus rapide.

Par exemple, si votre routeur est à `192.168.0.1`, vous pouvez ajouter ce qui suit à votre fichier hosts :

```
192.168.0.1       my.router
```

Ensuite, videz votre DNS Windows 10 avec `ipconfig /flushdns` et redémarrez votre navigateur.

Et ensuite, chaque fois que vous visitez my.router, vous devriez être redirigé vers `192.168.0.1`.

Notez simplement que vous devrez peut-être visiter http://my.router, au moins la première fois. Sinon, votre navigateur pourrait ne pas reconnaître .router comme un domaine de premier niveau (TLD) valide, et essaiera de rechercher le terme my.router à la place.

Pour contourner cela, vous pourriez utiliser un nom d'hôte comme ceci :

```
192.168.0.1       router.my
```

Cela devrait fonctionner immédiatement car .my est le TLD pour les personnes et les entreprises en Malaisie.

Heureusement, il existe aujourd'hui de nombreux TLD valides. Voici une liste de certains des TLD les plus courants : [https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains](https://en.wikipedia.org/wiki/List_of_Internet_top-level_domains)

Encore une fois, le seul inconvénient de cette méthode est qu'elle ne fonctionne que sur un seul appareil. Vous devriez mettre à jour les fichiers hosts sur vos autres appareils pour activer les mêmes raccourcis.

Et cela devrait être à peu près tout ce que vous devez savoir sur le fichier hosts sous Windows 10. Et beaucoup de ces connaissances devraient s'appliquer à Linux et macOS.

Alors, sortez et personnalisez votre fichier hosts comme le faisaient les pionniers de l'internet.

Avez-vous trouvé cela utile ? Connaissez-vous d'autres astuces pour le fichier hosts ? Faites-le moi savoir sur [Twitter](https://twitter.com/kriskoishigawa).

Restez en sécurité et bon édit du fichier hosts !