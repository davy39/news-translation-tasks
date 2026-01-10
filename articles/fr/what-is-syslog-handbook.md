---
title: Le manuel Syslog – Comment collecter et rediriger les logs vers un serveur
  distant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-02-29T19:40:35.000Z'
originalURL: https://freecodecamp.org/news/what-is-syslog-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/The-Syslog-Handbook-Cover.png
tags:
- name: Linux
  slug: linux
- name: logging
  slug: logging
seo_title: Le manuel Syslog – Comment collecter et rediriger les logs vers un serveur
  distant
seo_desc: 'By Serhii Orlivskyi

  If you''re in information technology, you''ll likely agree that logging is important.
  It helps you monitor a system, troubleshoot issues, and generally provides useful
  feedback about the system’s state. But it’s important to do logg...'
---

Par Serhii Orlivskyi

Si vous travaillez dans le domaine des technologies de l'information, vous serez probablement d'accord pour dire que la journalisation est importante. Elle vous aide à surveiller un système, à résoudre les problèmes et fournit généralement des commentaires utiles sur l'état du système. Mais il est important de bien faire la journalisation.

Dans ce manuel, je vais expliquer ce qu'est le protocole syslog et comment il fonctionne. Vous apprendrez les formats de messages syslog, comment configurer rsyslog pour rediriger les messages vers un serveur distant centralisé en utilisant TLS et via un réseau local, comment rediriger les données des applications vers syslog, comment utiliser Docker avec syslog, et bien plus encore.

## Table des matières

1. [Prérequis](#heading-prerequisites)  
2. [Introduction](#heading-introduction)
3. [Qu'est-ce que syslog ?](#heading-quest-ce-que-syslog)
    * [Protocole Syslog](#heading-protocole-syslog)
    * [Démons Syslog](#heading-demons-syslog)
    * [Formats de messages Syslog](#heading-formats-de-messages-syslog)
        * [Format RFC3164](#heading-format-rfc3164)
        * [Format RFC5424](#heading-format-rfc5424)
    * [Niveaux de journalisation Syslog](#heading-niveaux-de-journalisation-syslog)
    * [Facilités Syslog](#heading-facilites-syslog)
4. [Comment configurer rsyslog pour rediriger les messages vers un serveur distant centralisé en utilisant TLS](#heading-comment-configurer-rsyslog-pour-rediriger-les-messages-vers-un-serveur-distant-centralise-en-utilisant-tls)
    * [Mettre à jour rsyslog](#heading-mettre-a-jour-rsyslog)
    * [Installer les dépendances](#heading-installer-les-dependances)
    * [Configurer le serveur rsyslog exportateur](#heading-configurer-le-serveur-rsyslog-exportateur)
    * [Ne transférer que les logs générés par certains programmes](#heading-ne-transférer-que-les-logs-generes-par-certains-programmes)
    * [Spécifier les noms de domaine et les chemins de certificats corrects dans votre configuration](#heading-specifier-les-noms-de-domaine-et-les-chemins-de-certificats-corrects-dans-votre-configuration)
    * [Installer les certificats certbot](#heading-installer-les-certificats-certbot)
    * [Donner accès aux certificats à rsyslog](#heading-donner-acces-aux-certificats-a-rsyslog)
    * [Configurer le serveur rsyslog acceptant](#heading-configurer-le-serveur-rsyslog-acceptant)
    * [S'assurer que le pare-feu ne bloque pas votre trafic](#heading-sassurer-que-le-pare-feu-ne-bloque-pas-votre-trafic)
    * [Redémarrer rsyslog](#heading-redemarrer-rsyslog)
    * [Tester la configuration](#heading-tester-la-configuration)
    * [Comment stocker les logs distants dans un fichier séparé](#heading-comment-stocker-les-logs-distants-dans-un-fichier-separe)
    * [Considérations de performance](#heading-considerations-de-performance)
5. [Comment configurer rsyslog pour rediriger les messages vers un serveur distant centralisé via un réseau local](#heading-comment-configurer-rsyslog-pour-rediriger-les-messages-vers-un-serveur-distant-centralise-via-un-reseau-local)
    * [Exporter la configuration du serveur](#heading-exporter-la-configuration-du-serveur)
    * [Accepter la configuration du serveur](#heading-accepter-la-configuration-du-serveur)
    * [Redémarrer rsyslog et tester](#heading-redemarrer-rsyslog-et-tester)
6. [Autres possibilités de transfert de logs](#heading-autres-possibilites-de-transfert-de-logs)
7. [Comment rediriger les données des applications vers syslog](#heading-comment-rediriger-les-donnees-des-applications-vers-syslog)
    * [Application autonome de l'hôte et syslog](#heading-application-autonome-de-lhote-et-syslog)
        * [Redirection des logs vers syslog lors de l'exécution en avant-plan](#heading-redirection-des-logs-vers-syslog-lors-de-lexecution-en-avant-plan)
        * [Redirection des logs vers syslog lors de l'exécution en arrière-plan avec systemctl](#heading-redirection-des-logs-vers-syslog-lors-de-lexecution-en-arriere-plan-avec-systemctl)
        * [Redirection des logs à partir de fichiers de log existants](#heading-redirection-des-logs-a-partir-de-fichiers-de-log-existants)
    * [Docker et syslog](#heading-docker-et-syslog)
        * [Configuration d'un seul conteneur Docker](#heading-configuration-dun-seul-conteneur-docker)
        * [Configuration d'un service Docker via un fichier docker-compose](#heading-configuration-dun-service-docker-via-un-fichier-docker-compose)
        * [Configuration d'une valeur par défaut pour chaque conteneur via le démon Docker](#heading-configuration-dune-valeur-par-defaut-pour-chaque-conteneur-via-le-demon-docker)
        * [Activation des applications à l'intérieur de Docker pour journaliser directement vers syslog](#heading-activation-des-applications-a-linterieur-de-docker-pour-journaliser-directement-vers-syslog)
    * [Comment utiliser les bibliothèques de journalisation pour votre langage de programmation pour journaliser vers syslog](#heading-comment-utiliser-les-bibliotheques-de-journalisation-pour-votre-langage-de-programmation-pour-journaliser-vers-syslog)
        * [Client Node.js](#heading-client-nodejs)
        * [Client Python](#heading-client-python)
8. [Conclusion](#heading-conclusion)






## Prérequis

Dans ce guide, nous allons discuter de syslog et de ses concepts associés. Bien que j'expliquerai la plupart des sujets que nous aborderons, vous devriez avoir une connaissance de base des éléments suivants :

* Utilisation du terminal Linux (comme la navigation dans l'arborescence des répertoires, la création et l'édition de fichiers, le changement des permissions de fichiers, etc.)
* Une compréhension de base des réseaux (nom de domaine, hôte, adresse IP, TLS/SSL, certificat TLS, clé privée/publique, etc.).

## Introduction

Chaque système/application peut fournir ses logs dans différents formats. Si vous devez travailler avec de nombreux systèmes et les maintenir, il est important de gérer les logs de manière centralisée, gérable et évolutive.

Tout d'abord, il est utile de collecter tous les logs des applications sur votre machine en un seul endroit pour un traitement ultérieur.

Après avoir collecté tous les logs en un seul endroit, vous pouvez maintenant passer au traitement. Mais que faire si votre machine n'est qu'un seul nœud parmi un groupe de serveurs ? Dans ce cas, le traitement local des logs vous donne des informations sur ce nœud unique mais certainement pas sur tous les autres.

Vous pouvez très bien vouloir transférer tous les logs collectés vers un serveur central qui analyse tous les enregistrements, découvre les problèmes et les incohérences, déclenche des alertes et stocke enfin les logs pour une analyse forensique future.

Notez la commodité d'avoir un point d'accès central à tous vos logs. Vous n'avez pas à courir d'une machine à l'autre, à la recherche d'informations appropriées et à superposer manuellement différents fichiers de log.

Ainsi, pour atteindre l'objectif ci-dessus, vous pouvez exploiter le protocole syslog et utiliser un démon syslog très populaire appelé rsyslog pour collecter tous les logs et les transférer vers un serveur distant pour un traitement ultérieur de manière sécurisée et fiable.

Et c'est exactement l'exemple que je veux présenter dans ce tutoriel pour illustrer un cas d'utilisation courant et important de syslog. Je donnerai à ceux qui ne sont pas familiers avec lui un premier aperçu des problèmes qu'il peut résoudre.

Nous explorerons donc ce scénario, avec des exemples de redirection de logs à partir d'applications hôtes, de conteneurs Docker, et de clients Node.js et Python, dans cet article.

Mais d'abord, vous devez comprendre la terminologie autour de syslog, car elle est souvent entourée de mythes, de mystère et remplie de confusion. Eh bien, peut-être que j'exagère un peu ici, mais vous voyez mon point : la terminologie est importante.

## Qu'est-ce que syslog ?

De nos jours, il y a beaucoup d'incertitude quant à ce que le mot syslog désigne réellement, alors clarifions cela :

### Protocole Syslog

Syslog est un protocole de journalisation système qui est une norme pour la journalisation des messages. Il définit un format de message commun pour permettre aux systèmes d'envoyer des messages à un serveur de journalisation, qu'il soit configuré localement ou sur le réseau. Le serveur de journalisation gérera ensuite le traitement ou le transport ultérieur des messages.

Tant que le format de vos messages est conforme à ce protocole, vous devez simplement les transmettre à un serveur de journalisation (ou, en d'autres termes, un démon de journalisation dont nous parlerons bientôt) et les oublier.

Le transport des messages, la rotation, le traitement et l'enrichissement seront, à partir de ce moment, gérés par le serveur de journalisation et l'infrastructure à laquelle il est connecté. Votre application n'a pas besoin de connaître ou de gérer tout cela. Ainsi, nous obtenons une architecture découplée (la gestion des logs est séparée de l'application).

Mais le principal point du protocole syslog est, bien sûr, la standardisation. Tout d'abord, il est beaucoup plus facile d'analyser les logs lorsque toutes les applications adhèrent à une norme commune qui génère les logs dans le même format (ou plus ou moins le même, mais ne brûlons pas les étapes).

Si vos logs ont un format commun, il est tout d'abord facile de filtrer les enregistrements par une fenêtre de temps particulière ou par les niveaux de log respectifs (également appelés niveaux de gravité. Par exemple : info, warning, error, etc.).

Deuxièmement, vous pouvez avoir beaucoup d'applications différentes qui implémentent un transport de log elles-mêmes. Dans ce cas, vous devriez passer beaucoup de temps à parcourir la documentation, à comprendre comment configurer la journalisation des fichiers, la rotation des logs ou la transmission des logs pour chaque application au lieu de simplement le configurer une fois dans votre serveur syslog et d'attendre que toutes vos applications soumettent simplement leurs logs à celui-ci.

### Démons Syslog

Maintenant que vous comprenez que syslog est un protocole qui spécifie le format commun des messages de log produits par les applications, nous pouvons parler un peu des démons syslog. Ils sont essentiellement des serveurs de journalisation ou des expéditeurs de logs conçus pour recevoir des enregistrements de log, les convertir au format syslog (s'ils ne sont pas déjà convertis), et gérer les transformations de données, l'enrichissement et le transport vers diverses destinations.

L'une des premières implémentations de démon syslog pour Linux était simplement appelée **syslog** (ce qui a causé beaucoup de confusion) ou **sysklogd**. Plus tard, des implémentations plus modernes et couramment utilisées telles que **rsyslog** ou **syslog-ng** ont émergé. Celles-ci ont également été conçues spécifiquement pour Linux.

Mais si vous êtes intéressé par un démon syslog multiplateforme, qui peut également être utilisé sur MacOS, Android, ou même Windows, vous pouvez jeter un œil à **nxlog**.

Dans les sections suivantes de ce manuel, nous verrons plusieurs exemples pratiques de travail avec syslog. Pour cela, nous utiliserons rsyslog, qui est un démon syslog léger et très performant avec une large gamme de fonctionnalités. Il est généralement préinstallé sur de nombreuses distributions Linux (à la fois basées sur Debian et RedHat).

Rsyslog, comme de nombreux autres démons syslog, écoute par défaut un socket unix `/dev/log`. Il transmet les données entrantes à un fichier `/var/log/syslog` sur les distributions basées sur Debian ou à `/var/log/messages` sur les systèmes basés sur RedHat.

Certains messages de log spécifiques sont également stockés dans d'autres fichiers dans `/var/log`, mais le point principal est que tout cela peut, bien sûr, être configuré pour répondre à vos besoins.

Maintenant, vous connaissez la véritable signification de syslog et des démons syslog. Mais il y a un point important à noter. Dans de nombreux cas (et au cours de ce guide également), dire syslog de manière informelle fait référence au démon syslog ainsi qu'à l'infrastructure qui l'entoure (sockets Unix, fichiers dans `/var/log`, ainsi que d'autres démons si les messages sont transférés sur le réseau). Donc, dire « publier un message vers syslog » signifie envoyer un message au socket Unix `/dev/log` où il sera intercepté et traité par un démon syslog selon ses paramètres.

### Formats de messages Syslog

Syslog définit un certain format (structure) des enregistrements de log. Les applications travaillant avec syslog doivent adhérer à ce format lors de la journalisation vers `/dev/log`. À partir de là, les démons syslog récupéreront les messages, et les analyseront et les traiteront selon leur configuration.

Il existe deux types de formats syslog : l'ancien format BSD original qui provenait des premières versions des systèmes Unix BSD et est devenu une norme avec la spécification RFC3164, ainsi qu'un nouveau format de la RFC5424.

#### Format RFC3164

Ce format se compose des 3 parties suivantes : PRI, HEADER (TIMESTAMP, HOSTNAME), MSG (TAG, CONTENT). Voici un exemple plus concret (tiré directement de la RFC3164, d'ailleurs) :

```
<34>Oct 11 22:14:15 mymachine su: 'su root' failed for lonvick on /dev/pts/8
```

Voyons ce qui se passe ici :

* `<34>` (PRI) – priorité de l'enregistrement de log qui se compose du niveau de facilité multiplié par 8 plus le niveau de gravité. Nous parlerons des facilités et des niveaux de gravité bientôt, mais dans l'exemple ci-dessus nous obtenons : un numéro de facilité 4 (34 // 8 = 4) et un niveau de gravité critique (34 % 8 = 2).
* `Oct 11 22:14:15` (TIMESTAMP) – horodatage en heure locale sans l'année et une milliseconde ou une partie de fuseau horaire. Il suit une chaîne de format « Mmm dd hh:mm:ss »
* `mymachine` (HOSTNAME) – nom d'hôte, adresse IPv4 ou IPv6 de la machine d'où provient le message.
* `su` (TAG) – Nom du programme ou du processus qui a généré le message. Tout caractère non alphanumérique termine le champ TAG et est supposé être une partie de départ du champ suivant (CONTENT). Dans notre cas, il s'agit d'un caractère deux-points (« : »). Mais il aurait également pu s'agir d'un simple espace, ou même de crochets avec le PID (identifiant de processus) à l'intérieur, tel que « [123] ».
* `: 'su root' failed for lonvick on /dev/pts/8` (CONTENT) – Un message réel de l'enregistrement de log.

Comme vous pouvez le voir, la RFC3164 ne fournit pas beaucoup d'informations structurelles et présente certaines limitations et inconvénients tels qu'un horodatage restreint ou une certaine variabilité et incertitude (par exemple, dans les délimiteurs après le champ TAG). De plus, le format RFC3164 stipule que seul l'encodage ASCII est pris en charge.

Tout ce qui précède est en fait le résultat de la RFC3164 n'étant pas une norme stricte gravée dans le marbre, mais plutôt une généralisation de bon effort de certaines implémentations syslog qui existaient déjà à l'époque.

#### Format RFC5424

La RFC5424 présente un format mis à jour et plus structuré qui traite certains des problèmes rencontrés dans la RFC3164.

Il se compose des parties suivantes : HEADER (PRI, VERSION, TIMESTAMP, HOSTNAME, APP-NAME, PROCID, MSGID), STRUCTURED DATA (SD-ELEMENTS (SD-ID, SD-PARAM)), MSG. Voici un exemple :

```
<34>1 2003-10-11T22:14:15.003Z mymachine.example.com su - ID47 - BOM'su root' failed for lonvick on /dev/pts/8

```

* `<34>` (PRI) – priorité de l'enregistrement de log. Combinaison de gravité et de facilité. Même chose que pour la RFC3164.
* `1` (VERSION) – version de la spécification du protocole syslog. Ce nombre est censé être incrémenté pour toute spécification future qui apporte des modifications à la partie HEADER.
* `2003-10-11T22:14:15.003Z` (TIMESTAMP) – un horodatage avec l'année, les informations de sous-seconde et les parties de fuseau horaire. Il suit le format standard ISO 8601 tel que décrit dans la RFC3339 avec quelques restrictions mineures, comme ne pas utiliser les secondes intercalaires, nécessitant toujours le délimiteur « T » et mettant en majuscule chaque caractère dans l'horodatage. NILVALUE (« - ») sera utilisé si l'application syslog ne peut pas obtenir l'heure système (c'est-à-dire qu'elle n'a pas accès à l'heure sur le serveur).
* `https://mymachine.example.com/` (HOSTNAME) – FQDN, nom d'hôte ou l'adresse IP de l'origine du log. NILVALUE peut également être utilisé lorsque l'application syslog ne connaît pas le nom d'hôte d'origine.
* `su` (APP-NAME) – appareil ou application qui a produit le message. NILVALUE peut être utilisé lorsque l'application syslog n'est pas consciente du nom de l'application du producteur de log.
* `-` (PROCID) – valeur dépendante de l'implémentation souvent utilisée pour fournir un nom de processus ou un ID de processus de l'application qui a généré le message. Une NILVALUE doit être utilisée lorsque ce champ n'est pas fourni.
* `ID47` (MSGID) – champ utilisé pour identifier le type de message. Doit contenir NILVALUE lorsqu'il n'est pas utilisé.
* `-` (STRUCTURED DATA) – fournit des sections avec des paires clé-valeur transmettant des métadonnées supplémentaires sur le message. NILVALUE doit être utilisé lorsque les données structurées ne sont pas fournies. Exemples : « [exampleSection@32473 iut="3" eventSource="Application" eventID="1011"][exampleSection2@32473 class="high"] ». En pratique, la partie STRUCTURED DATA était rarement utilisée et les informations de métadonnées étaient généralement mises dans la partie MSG que de nombreuses applications structurent sous forme de JSON.
* `BOM'su root' failed for lonvick on /dev/pts/8` (MSG) – message réel de l'enregistrement de log. Le « BOM » au début est un caractère non imprimable qui signifie que le reste de la charge utile est encodé en UTF8. Si ce caractère n'est pas présent, alors d'autres encodages comme ASCII peuvent être supposés par les démons syslog.

La RFC5424 a un format plus pratique utilisé pour un horodatage et beaucoup plus de parties structurelles que vous pouvez utiliser pour spécifier toutes sortes de métadonnées pour les messages de log.

De plus, la spécification a été conçue pour être extensible avec le champ VERSION. Même si je ne suis pas au courant de certaines extensions de spécification syslog qui utilisent ce dernier et incrémentent la version, la possibilité est toujours là.

Enfin, le nouveau format prend en charge l'encodage UTF8 et pas seulement l'ASCII.

Notez que si un message dirigé vers `/dev/log` ne suit pas l'un des formats syslog décrits, il sera toujours traité par des démons tels que rsyslog. Rsyslog essaiera d'analyser ces enregistrements selon soit ses valeurs par défaut, soit des modèles personnalisés.

Les modèles sont un sujet séparé qui nécessite son propre article, donc nous ne nous concentrerons pas sur eux maintenant.

Par défaut, rsyslog traitera ces messages comme des données non structurées et les traitera telles quelles. Il essaiera de combler les lacunes comme un champ d'horodatage, un niveau de gravité, etc., du mieux qu'il peut et conformément à ses paramètres par défaut (par exemple, l'horodatage deviendra l'heure actuelle, le niveau de log sera « user » et le niveau de gravité sera « info »).

Lorsque vous inspectez les enregistrements de log dans `/var/log/messages` ou `/var/log/syslog` (selon le système), vous verrez probablement un format différent de ceux décrits ci-dessus. Pour rsyslog, cela ressemble à ceci :

```
Feb 19 10:01:43 mymachine systemd[1]: systemd-hostnamed.service: Deactivated successfully.

```

Ceci est simplement le format que rsyslog utilise pour afficher les messages ingérés qu'il a sauvegardés sur le disque et non un format syslog standard. Vous pouvez trouver ce format dans le fichier rsyslog.conf ou dans la documentation officielle sous le nom `RSYSLOG_TraditionalFileFormat`. Mais vous pouvez toujours configurer comment rsyslog sort ses messages vous-même en utilisant des modèles.

Un aspect important à comprendre est que rsyslog traite les messages au fur et à mesure qu'ils arrivent. Il les reçoit et les transmet immédiatement aux destinations spécifiées ou les sauvegarde localement dans des fichiers, tels que `/var/log/messages`. Une fois les messages entièrement traités, rsyslog ne conserve aucune métadonnée à leur sujet, à part ce qu'il a stocké dans les fichiers de log.

Cela signifie que si les enregistrements dans `/var/log/messages` sont stockés dans le format traditionnel rsyslog présenté ci-dessus, ils ne conserveront pas, par exemple, leur valeur PRI initiale. Bien que PRI et d'autres données soient accessibles à rsyslog en interne lors du traitement et du routage des messages, toutes ces informations ne sont pas par défaut stockées dans les fichiers de log.

### Niveaux de journalisation Syslog

Syslog prend en charge les niveaux de log suivants, appelés niveaux de gravité selon la terminologie de syslog :

<table style="border:none;border-collapse:collapse;"><colgroup><col width="108"><col width="308"><col width="208"></colgroup><tbody><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;background-color:#cccccc;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-left: 36pt;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Code</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;background-color:#cccccc;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-left: 36pt;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Niveau de log&nbsp;</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;background-color:#cccccc;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-left: 36pt;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Mot clé</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">0</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Urgence&nbsp;</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Consolas,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">emerg</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">1</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Alerte&nbsp;</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Consolas,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">alert</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">2</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Critique&nbsp;</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Consolas,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">crit</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">3</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Erreur&nbsp;</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Consolas,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">err</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">4</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Avertissement&nbsp;</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Consolas,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">warning</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">5</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Remarque&nbsp;</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Consolas,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">notice</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">6</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Informationnel&nbsp;</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Consolas,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">info</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">7</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Débogage&nbsp;</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Consolas,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">debug</span></p></td></tr></tbody></table>

Ces niveaux vous permettent de catégoriser les messages par critères de gravité (importance), l'urgence étant le niveau le plus élevé.

### Facilités Syslog

Les facilités Syslog représentent l'origine d'un message. Vous pouvez souvent les utiliser pour filtrer et catégoriser les enregistrements de log par le système qui les a générés.

Notez que les facilités syslog (ainsi que les niveaux de gravité, en fait) ne sont pas strictement normatives, donc différentes facilités et niveaux peuvent être utilisés par différents systèmes d'exploitation et distributions. De nombreux détails ici sont historiquement enracinés et pas toujours basés sur l'utilité.

<table style="border:none;border-collapse:collapse;"><colgroup><col width="82"><col width="123"><col width="420"></colgroup><tbody><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;background-color:#cccccc;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;text-align: center;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Code</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;background-color:#cccccc;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;text-align: center;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Mot-clé</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;background-color:#cccccc;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;text-align: center;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:700;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Description</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">0</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">kern</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Messages du noyau</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">1</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">user</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Messages de niveau utilisateur général. Cette facilité est typiquement utilisée par défaut si aucune autre n'est spécifiée</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">2</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">mail</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Messages du système de messagerie. Générés par les serveurs et clients de messagerie en cours d'exécution, le cas échéant.</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">3</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">daemon</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Message du démon système non lié au noyau mais à d'autres services en arrière-plan</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">4</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">auth</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Messages de sécurité/généraux d'authentification (générés par des outils comme su, login, ftpd etc. qui demandent les identifiants de l'utilisateur)</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">5</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">syslog</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Messages générés par le démon syslog lui-même</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">6</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">lpr</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Messages du sous-système de l'imprimante en ligne générés par les services d'impression</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">7</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">news</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Messages du sous-système des nouvelles du réseau (peut être utilisé lorsque les appareils réseau génèrent des messages syslog)</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">8</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">uucp</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Messages du sous-système UUCP (Unix-to-Unix Copy Protocol)</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">9</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">cron</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Messages du démon Cron liés aux tâches planifiées (erreurs, résultats des tâches planifiées, etc.)</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">10</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">authpriv</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Messages privés de sécurité/authentification. Les messages avec ce niveau sont acheminés vers un fichier séparé avec des permissions plus restreintes</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">11</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">ftp</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Messages du sous-système du protocole de transfert de fichiers</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">12</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">ntp</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Messages du sous-système du protocole de temps réseau</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">13</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">security/log audit</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Messages générés par les systèmes (sous-)d'audit. La facilité est également utilisée par divers outils de sécurité/autorisation</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">14</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">console/log alert</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Messages d'alerte nécessitant une attention particulière ; générés par les systèmes d'alerte. Peut également être utilisé par divers outils de sécurité/autorisation ou toute autre application ayant besoin de relayer un message d'alerte important</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">15</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">solaris-cron/clock</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Messages vers le démon de l'horloge comme cron. Presque la même chose que la facilité 9. La différence est historique plutôt que fonctionnelle.&nbsp;</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">16-22</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">local0-local7</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:12pt;font-family:Arial,sans-serif;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Local0-local7 : Facilités locales réservées pour un usage personnalisé par des processus qui ne rentrent pas dans les catégories définies ci-dessus</span></p></td></tr></tbody></table>

Notez que la spécification du protocole syslog définit uniquement les codes pour les facilités. Les mots-clés peuvent être utilisés par les démons syslog pour la lisibilité.

Maintenant que nous avons vu la liste de toutes les facilités existantes, portez une attention particulière à celles telles que « sécurité », « authpriv », « audit de log » ou « alerte de log ». Il est possible pour une application de journaliser vers différentes facilités en fonction de la nature du message.

Par exemple, une application pourrait généralement journaliser vers la facilité « utilisateur », mais une fois qu'elle reçoit une alerte importante, elle pourrait journaliser vers la facilité 14 (alerte de log). Ou en cas de notice d'authentification/autorisation, elle pourrait la diriger vers la facilité « auth », et ainsi de suite.

Si vous avez une application personnalisée et que vous vous demandez quelle facilité serait la mieux adaptée, vous pouvez utiliser la facilité « utilisateur » (code 1) ou des facilités locales personnalisées (codes 16-22).

La différence ultime entre les facilités utilisateur et locales est que la première est plus générale, ce qui agrège les logs de différentes applications utilisateur. Mais soyez conscient que d'autres logiciels pourraient tout aussi bien utiliser l'une des facilités locales sur votre machine.

## Comment configurer `rsyslog` pour rediriger les messages vers un serveur distant centralisé en utilisant TLS

Examinons maintenant un exemple pratique dont j'ai parlé au début. Cela peut ne pas sembler être le cas d'utilisation le plus basique – surtout pour ceux qui ne sont pas familiers avec les démons syslog – mais c'est un scénario assez courant. J'espère que cela vous aidera à apprendre beaucoup de choses utiles en cours de route.

Je vais maintenant vous guider à travers les étapes que vous devrez suivre pour transférer les données syslog d'un serveur à un autre qui jouera le rôle d'agrégateur de logs centralisé. Dans cet exemple, nous enverrons les logs au fur et à mesure qu'ils arrivent, en utilisant le protocole TCP avec des certificats pour le chiffrement et la vérification d'identité.

Dans les exemples suivants, je suppose que vous avez un serveur centralisé pour accepter les données syslog et un ou plusieurs serveurs exportateurs qui transfèrent leurs messages syslog vers ce nœud central acceptant. Je supposerai également que tous les serveurs sont découvrables par leurs noms de domaine respectifs et exécutent des distributions Linux basées sur Debian ou RedHat.

Alors, plongeons-nous et commençons.

### Mettre à jour rsyslog

Comme rsyslog est généralement préinstallé sur la plupart des distributions Linux courantes, je ne couvrirai pas le processus d'installation ici. Assurez-vous simplement que votre rsylogd est suffisamment à jour pour tirer parti de sa large gamme de fonctionnalités.

Exécutez la commande suivante sur tous vos serveurs :

```
rsyslogd -v
```

Et assurez-vous que la version dans la sortie est 6 ou supérieure.

Si ce n'est pas le cas, exécutez les commandes suivantes pour mettre à jour votre démon :

Pour les distributions basées sur Debian :

```
sudo apt-get update
sudo apt-get install --only-upgrade rsyslog
sudo systemctl restart rsyslog

```

Pour les distributions basées sur RedHat :

```
sudo yum update rsyslog
sudo systemctl restart rsyslog

```

Ou utilisez `dnf` au lieu de `yum` pour CentOS8/RHEL8 :

### Installer les dépendances

Pour gérer le transfert sécurisé des messages sur le réseau en utilisant TLS, nous devrons installer le module `rsyslog-gnutls`. Si vous préférez compiler rsyslog à partir de la source, vous devrez spécifier un drapeau respectif lors de la compilation. Mais si vous utilisez des gestionnaires de paquets, vous pouvez simplement exécuter ce qui suit pour chaque serveur :

Pour les distributions basées sur Debian :

```
sudo apt-get update
sudo apt-get install rsyslog-gnutls
sudo systemctl restart rsyslog

```

Pour les distributions basées sur RedHat :

```
sudo yum install epel-release
sudo yum install rsyslog-gnutls
sudo systemctl restart rsyslog

```

### Configurer le serveur rsyslog exportateur

Maintenant, nous allons créer un fichier de configuration rsyslog pour les nœuds qui vont exporter leurs logs vers le serveur central. Pour ce faire, créez le fichier de configuration dans le répertoire de configuration de rsyslog :

```
sudo touch /etc/rsyslog.d/export-syslog.conf
```

Assurez-vous que le fichier est lisible par l'utilisateur `syslog` sur les distributions basées sur Debian (`chown syslog:adm /etc/rsyslog.d/export-syslog.conf` ou `chmod 644 /etc/rsyslog.d/export-syslog.conf`). Notez que sur les distributions basées sur RedHat comme CentOS, rsyslog s'exécute sous root, donc il ne devrait pas y avoir de problèmes de permissions.

Ouvrez maintenant le fichier créé et ajoutez la configuration suivante :

```
# Définir les fichiers de certificat
global(
  DefaultNetstreamDriverCAFile="<path_to_your_ca.pem>"
  DefaultNetstreamDriverCertFile="<path_to_your_cert.pem>"
  DefaultNetstreamDriverKeyFile="<path_to_your_private_key.pem>"
)

# Configurer l'action de transfert pour tous les messages
*.* action(
  type="omfwd"
  StreamDriver="gtls"
  StreamDriverMode="1"
  StreamDriverPermittedPeers="<domain_name_of_your_accepting_central_server>"
  StreamDriverAuthMode="x509/name"
  target="<domain_name_or_ip_of_your_accepting_central_server>" port="514" protocol="tcp"
  action.resumeRetryCount="100" # vous pouvez modifier les paramètres de file d'attente et de nouvelle tentative comme vous le souhaitez
  queue.type="linkedList" queue.size="10000"
)

```

La configuration ci-dessus transférera tous les messages qui sont digérés par rsyslog vers votre serveur distant. Si vous souhaitez obtenir un contrôle plus fin, reportez-vous à la sous-section ci-dessous.

### Ne transférer que les logs générés par certains programmes

Si vous souhaitez transférer des messages pour un certain programme uniquement, vous pouvez spécifier la condition suivante au lieu de `*.*` avant `action` dans la configuration ci-dessus :

```
if $programname == '<your_program_name>' then
# ...ici va votre action et tout le reste

```

Si vous souhaitez spécifier plus d'un nom de programme, ajoutez plusieurs conditions en utilisant `or` :

```
if ($programname == '<your_program_name1>' or $programname == '<your_program_name2>' $programname == '<your_program_name3>') then
# ...ici va votre action et tout le reste
```

Pour plus d'informations, reportez-vous à la documentation RainerScript pour rsyslog [ici](https://www.rsyslog.com/doc/rainerscript/control_structures.html#if-else-if-else).

### Spécifier les noms de domaine et les chemins de certificats corrects dans votre configuration

Maintenant, revenons à notre fichier de configuration. Il utilisera TLS (comme vous pouvez le voir dans `StreamDriverMode="1"`) et transférera toutes les données vers `target` sur le port 514, qui est un port par défaut pour syslog.

Pour rendre cette configuration valide, vous devrez remplacer `<domain_name_of_your_accepting_central_server>` et `<domain_name_or_ip_of_your_accepting_central_server>` par le nom de domaine respectif de votre serveur central acceptant (par exemple : `my-central-server.company.com`) ainsi que spécifier les chemins corrects vers les certificats dans la section `global`.

Notez que, puisque sur les distributions de type Debian, rsyslog s'exécute généralement sous l'utilisateur `syslog`, vous devrez vous assurer que les certificats eux-mêmes et tous les répertoires dans leur chemin sont lisibles et accessibles par cet utilisateur (pour les répertoires, cela signifie que les bits de permission « r » et « x » doivent être définis).

Sur les systèmes basés sur RedHat, en revanche, rsyslog s'exécute souvent en tant que root, donc il n'est pas nécessaire de modifier les permissions des fichiers.

Pour vérifier sous quel utilisateur votre rsyslog s'exécute, exécutez ce qui suit :

```
sudo ps -aux | grep rsyslog

```

Et regardez du côté gauche le nom d'utilisateur exécutant rsyslogd.

Si vous n'avez pas encore de certificats SSL, lisez les deux sous-sections suivantes sur l'installation des certificats avec Let's Encrypt et l'octroi d'accès à rsyslog. Si vous avez déjà tous les certificats nécessaires et les permissions, vous pouvez sauter ces étapes en toute sécurité.

### Installer les certificats certbot

Tout d'abord, vous devrez installer certbot. Pour les systèmes basés sur Debian, exécutez ce qui suit :

```
sudo apt-get install certbot

```

Si vous obtenez une erreur indiquant que le paquet n'est pas trouvé, exécutez `sudo apt-get update` et réessayez.

Pour les systèmes basés sur RedHat :

```
sudo yum install epel-release
sudo yum install certbot

```

Assurez-vous qu'aucun serveur n'est en cours d'exécution sur le port 80, puis exécutez certbot en mode autonome, en spécifiant votre nom de domaine avec le drapeau `-d` pour obtenir vos certificats SSL :

```js
sudo certbot certonly --standalone -d <your_domain_name>
# Par exemple : sudo certbot certonly --standalone -d my-sever1.mycompany.com
```

Suivez les instructions de certbot, et à la fin, vous recevrez vos certificats SSL qui seront stockés dans `/etc/letsencrypt/live/<your_domain_name>/`.

Confirmez qu'il n'y a pas de problèmes lors du processus de renouvellement du certificat comme ceci :

```
sudo certbot renew --dry-run
```

Les certificats seront automatiquement renouvelés par certbot, donc vous n'avez pas à vous soucier de les mettre à jour manuellement chaque fois. Si vous avez installé certbot comme décrit ci-dessus, il utilisera un minuteur systemd ou créera une tâche cron pour gérer les renouvellements.

### Donner accès aux certificats à rsyslog

Si vous exécutez un système basé sur Debian, alors, comme mentionné ci-dessus, vous devez accorder à l'utilisateur `syslog` les privilèges nécessaires pour accéder aux certificats et clés de certbot. Cela est dû au fait que le répertoire `/etc/letsencrypt/live` avec les fichiers générés par certbot est restreint à l'utilisateur root uniquement.

Nous allons donc copier les certificats et clés dans les emplacements standard des certificats et clés. Pour les distributions basées sur Debian, il s'agit respectivement de `/etc/ssl/certs` et `/etc/ssl/private`. Ensuite, nous modifierons les permissions de ces fichiers.

Tout d'abord, créez un groupe qui aura accès aux certificats SSL :

```
sudo groupadd sslcerts

```

Ajoutez l'utilisateur `syslog` à ce groupe :

```
sudo usermod -a -G sslcerts syslog
```

Ajoutez les permissions et la propriété pour le répertoire `/etc/ssl/private` au groupe créé :

```
sudo chown root:sslcerts /etc/ssl/private
sudo chmod 750 /etc/ssl/private

```

Maintenant, nous allons créer un script qui déplacera les fichiers de certificat du répertoire live de Let's Encrypt vers `/etc/ssl`. Exécutez ce qui suit :

```
sudo touch /etc/letsencrypt/renewal-hooks/deploy/move-ssl-certs.sh
sudo chmod +x /etc/letsencrypt/renewal-hooks/deploy/move-ssl-certs.sh

```

Notez qu'en créant le script dans le répertoire `/etc/letsencrypt/renewal-hooks/deploy`, il s'exécutera automatiquement après chaque renouvellement de certificat. De cette façon, vous n'aurez pas à vous soucier de déplacer manuellement les certificats et d'accorder des permissions chaque fois qu'ils expirent.

Ouvrez le fichier créé et ajoutez le contenu suivant, en remplaçant `<your-domain-name>` par le domaine de votre machine qui correspond au répertoire créé par certbot dans `/etc/letsencrypt/live` :

```
#!/bin/bash

# Définir les répertoires source et de destination
DOMAIN_NAME=<your-domain-name>
LE_LIVE_PATH="/etc/letsencrypt/live/$DOMAIN_NAME"
SSL_CERTS_PATH="/etc/ssl/certs"
SSL_PRIVATE_PATH="/etc/ssl/private"

# Copier la chaîne complète et la clé privée dans les répertoires respectifs
cp "$LE_LIVE_PATH/fullchain.pem" "$SSL_CERTS_PATH/$DOMAIN_NAME-letsencrypt-fullchain.pem"
cp "$LE_LIVE_PATH/cert.pem" "$SSL_CERTS_PATH/$DOMAIN_NAME-letsencrypt-cert.pem"
cp "$LE_LIVE_PATH/privkey.pem" "$SSL_PRIVATE_PATH/$DOMAIN_NAME-letsencrypt-privkey.pem"

# Définir la propriété et les permissions
chown root:sslcerts "$SSL_CERTS_PATH/$DOMAIN_NAME-letsencrypt-fullchain.pem"
chown root:sslcerts "$SSL_CERTS_PATH/$DOMAIN_NAME-letsencrypt-cert.pem"
chown root:sslcerts "$SSL_PRIVATE_PATH/$DOMAIN_NAME-letsencrypt-privkey.pem"

chmod 644 "$SSL_CERTS_PATH/$DOMAIN_NAME-letsencrypt-fullchain.pem"
chmod 644 "$SSL_CERTS_PATH/$DOMAIN_NAME-letsencrypt-cert.pem"
chmod 640 "$SSL_PRIVATE_PATH/$DOMAIN_NAME-letsencrypt-privkey.pem"
```

Maintenant, exécutez le script créé pour déplacer effectivement les certificats vers /etc/ssl et donner les permissions à l'utilisateur `syslog` :

```
sudo /etc/letsencrypt/renewal-hooks/deploy/move-ssl-certs.sh

```

Enfin, allez dans le fichier de configuration rsyslog `/etc/rsyslog.d/export-syslog.conf` et changez les chemins des certificats en conséquence :

```
# Définir les fichiers de certificat
global(
DefaultNetstreamDriverCAFile="/etc/ssl/certs/<your_domain_name>-letsencrypt-fullchain.pem"
  DefaultNetstreamDriverCertFile="/etc/ssl/certs/<your_domain_name>-letsencrypt-cert.pem"
  DefaultNetstreamDriverKeyFile="/etc/ssl/private/<your_domain_name>-letsencrypt-privkey.pem"
)

```

Notez que même si rsyslog s'exécute généralement en tant que root sur les distributions basées sur RedHat, vous pouvez constater que ce n'est pas le cas pour votre système.

Si ce n'est pas le cas, vous pouvez effectuer les mêmes manipulations de permissions que nous avons faites ci-dessus. Mais l'emplacement recommandé par défaut pour les certificats et clés SSL peut différer. Pour CentOS, il s'agit de `/etc/pki/tls/certs` et `/etc/pki/tls/private`. Mais vous pouvez également toujours choisir des emplacements complètement différents si nécessaire.

### Configurer le serveur rsyslog acceptant

Configurons maintenant un serveur central qui acceptera les logs du reste des machines.

Si vous n'avez pas encore acquis de certificats SSL pour votre serveur, reportez-vous à la section sur l'installation des certificats certbot.

Si votre serveur est basé sur Debian, reportez-vous à la section sur l'octroi d'accès aux certificats à rsyslog.

Maintenant, de manière similaire à la configuration du serveur exportateur, créez un fichier de configuration rsyslog :

```
sudo touch /etc/rsyslog.d/import-syslog.conf
```

Ouvrez le fichier et ajoutez ce qui suit :

```
# Définir les fichiers de certificat
global(  DefaultNetstreamDriverCAFile="/etc/ssl/certs/<your_domain_name>-letsencrypt-fullchain.pem"
  DefaultNetstreamDriverCertFile="/etc/ssl/certs/<your_domain_name>-letsencrypt-cert.pem"
  DefaultNetstreamDriverKeyFile="/etc/ssl/private/<your_domain_name>-letsencrypt-privkey.pem"
)

# Écouteur TCP
module(
  load="imtcp"
  PermittedPeer=["<your_peer1>","<your_peer2>","<your_peer3>"]
  StreamDriver.AuthMode="x509/name"
  StreamDriver.Mode="1"
  StreamDriver.Name="gtls"
)

# Démarrer l'écouteur sur le port 514
input(
  type="imtcp"
  port="514"
)

```

Notez que vous devez remplacer `PermittedPeer=["<your_peer1>","<your_peer2>","<your_peer3>"]` par un tableau des noms de domaine de vos serveurs exportateurs, par exemple : `PermittedPeer=["export-server1.company.com","export-server2.company.com","export-server3.company.com"]`.

N'oubliez pas non plus de vérifier et de changer vos chemins de certificats dans la section `global` si nécessaire. Encore une fois, si vous êtes sur un système basé sur RedHat, vous pouvez simplement référencer les certificats dans le répertoire live de Let's Encrypt en raison des permissions root.

### S'assurer que le pare-feu ne bloque pas votre trafic

Assurez-vous que le pare-feu sur votre serveur central ne bloque pas le trafic entrant sur le port 514. Par exemple, si vous utilisez `iptables` :

Pour vérifier si la règle existe déjà :

```
sudo iptables -C INPUT -p tcp --dport 514 -j ACCEPT
```

Si la commande précédente se termine par une erreur, vous pouvez définir une règle d'acceptation avec :

```
sudo iptables -A INPUT -p tcp --dport 514 -j ACCEPT # les règles s'appliqueront immédiatement
iptables-save > /etc/iptables/rules.v4 # ou utilisez `iptables-save > /etc/sysconfig/iptables` pour les distributions basées sur RedHat

```

### Redémarrer rsyslog

Maintenant, après avoir ajouté les configurations appropriées à tous vos serveurs, vous devez redémarrer rsyslog sur tous ceux-ci, en commençant par votre nœud central acceptant :

```
sudo systemctl restart rsyslog
```

Vous pouvez vérifier s'il y a des erreurs après le redémarrage de rsyslog en exécutant ce qui suit :

```js
sudo systemctl status rsyslog
sudo journalctl -u rsyslog | tail -100

```

La première commande ci-dessus affichera le statut de rsyslog, et la deuxième affichera les 100 dernières lignes des logs de rsyslog. Si vous avez mal configuré quelque chose et que votre configuration n'a pas fonctionné, vous devriez trouver des informations utiles là.

### Tester la configuration

Pour tester si votre redirection syslog a fonctionné, émettez la commande suivante sur le nœud central pour commencer à surveiller les nouvelles données arrivant dans syslog :

Pour les systèmes basés sur Debian :

```
tail -f /var/log/syslog
```

Pour les systèmes basés sur RedHat :

```
tail -f /var/log/messages
```

Après cela, allez sur chacun de vos nœuds exportateurs et exécutez :

```
logger "Hello, world!"
```

Vous devriez voir un message « Hello, world! » de chaque serveur exportateur apparaître dans le syslog de votre machine acceptante.

Si tout a fonctionné, alors félicitations ! Vous avez maintenant configuré et vérifié avec succès la redirection syslog sur le réseau.

Note : appuyez sur Ctrl+C pour quitter la commande `tail -f` exécutée sur le nœud central.

Dans une section ultérieure, nous considérerons le même scénario mais sans certificats au cas où tous vos serveurs sont situés dans un réseau local de confiance. Après cela, nous explorerons enfin comment rediriger les données réelles de différentes applications vers syslog.

### Comment stocker les logs distants dans un fichier séparé

Mais attendez une seconde – avant de continuer, considérons une petite modification utile à notre configuration.

Supposons que vous souhaitiez configurer votre rsyslog central de manière à ce qu'il redirige le trafic distant vers un fichier séparé au lieu du typique `/var/log/syslog` ou `/var/log/messages`.

Pour ce faire, apportez les modifications suivantes à votre fichier `/etc/rsyslog.d/import-syslog.conf` :

Ajoutez une propriété de jeu de règles à l'objet `input` :

```
input(
  type="imtcp"
  port="514"
  ruleset="remote"
)

```

Ensuite, ajoutez la ligne suivante en bas du fichier :

```
ruleset(name="remote") {
  if $hostname == '<your_remote_hostname>' then {
    action(type="omfile" file="/var/log/remote-logs.log")
    stop
  }
}

```

Changez `<your_remote_hostname>` en conséquence. Vous pouvez également définir plusieurs noms d'hôte avec un `or` comme nous l'avons vu précédemment. N'hésitez pas également à changer le chemin vers le fichier de sortie (c'est-à-dire `/var/log/remote-logs.log`) pour répondre à vos besoins.

Après cela, redémarrez rsyslog.

### Considérations de performance

Rsyslog est un outil très léger et performant pour gérer et transférer vos logs sur le réseau. Cependant, effectuer un protocole TCP et une poignée de main TLS pour valider les certificats pour chaque message de log (ou un lot de messages) a un coût.

Dans la section suivante, vous apprendrez à effectuer le transfert TCP et UDP sans certificats TLS. Cela sera généralement une méthode plus performante, mais vous ne devez l'utiliser que dans un réseau local de confiance.

En ce qui concerne UDP, même s'il est plus performant que TCP, vous ne devez l'utiliser que si les pertes de données potentielles sont acceptables.

Si vous n'avez pas besoin d'une livraison de logs en temps quasi réel, il peut être préférable de stocker tous vos logs dans un seul fichier (vous pouvez le faire avec rsyslog ou en employant d'autres outils ou techniques). Ensuite, vous pouvez planifier un script séparé, qui transférera ce fichier vers un serveur central lorsqu'il atteindra une certaine taille ou lorsque certains intervalles de temps se seront écoulés.

Dans tous les cas, avant d'employer une solution particulière, assurez-vous de faire un benchmark en vous concentrant sur le test de charge de votre système pour découvrir quelle approche fonctionne le mieux pour vous.

## Comment configurer `rsyslog` pour rediriger les messages vers un serveur distant centralisé via un réseau local

Si votre scénario n'implique pas de communications sur un réseau non fiable, vous pouvez décider de ne pas utiliser de certificats pour transférer vos enregistrements syslog. Je veux dire, les poignées de main TLS sont coûteuses après tout !

De plus, la configuration dans ce cas, que nous allons discuter maintenant, sera assez simplifiée. Elle impliquera moins d'étapes, car notre principale préoccupation lors de la configuration du transfert syslog avec TLS était les certificats SSL et leurs permissions de fichiers.

### Exporter la configuration du serveur

Pour configurer votre serveur exportateur afin de transférer les données syslog en utilisant TCP sans chiffrement, connectez-vous à chaque serveur exportateur et créez un fichier de configuration rsyslog :

```
sudo touch /etc/rsyslog.d/export-syslog.conf
```

Ouvrez ce fichier et ajoutez la configuration suivante, en remplaçant `<your_remote_server_hostname_or_ip>` par le nom d'hôte ou l'IP de votre nœud central, qui doit être découvrable sur votre réseau :

```
*.* action(
  type="omfwd"
  target="<your_remote_server_hostname_or_ip>"
  port="514"
  protocol="tcp"
  action.resumeRetryCount="100"
  queue.type="linkedList"
  queue.size="10000"
)

```

Si vous souhaitez utiliser le protocole UDP, vous pouvez simplement changer `protocol="tcp"` en `protocol="udp"`.

Au cas où vous vous demanderiez maintenant si nous pourrions utiliser UDP pour transférer le trafic dans notre exemple précédent avec des certificats, alors la réponse est non. Cela est dû au fait qu'une poignée de main TLS fonctionne sur TCP mais pas sur UDP. Au moins, c'est ainsi qu'il a été conçu à l'origine, et même s'il peut exister certaines variations et modifications de protocole dans la nature, elles sont très délicates et définitivement hors du cadre de ce manuel.

Notez qu'il existe une syntaxe alternative plus simple mais moins flexible pour écrire la configuration ci-dessus.

Pour le transfert via TCP :

```
*.* @@<your_remote_server_hostname>:514
```

Pour le transfert via UDP :

```
*.* @<your_remote_server_hostname>:514
```

Je vous montre ces variations de syntaxe car vous pouvez les rencontrer dans d'autres articles. Ces variations reproduisent la syntaxe du démon sysklogd (oui, l'une des premières implémentations de démon syslog dont rsyslog est un fork compatible à rebours).

### Accepter la configuration du serveur

Créez un fichier de configuration rsyslog sur votre serveur acceptant :

```
sudo touch /etc/rsyslog.d/import-syslog.conf
```

Ouvrez le fichier et ajoutez le contenu suivant :

* Pour recevoir le trafic TCP :

```
module(load="imtcp") # Charger le module imtcp
input(type="imtcp" port="514") # Écouter sur le port TCP 514

```

* Pour recevoir UDP :

```
module(load="imudp") # Charger le module imudp pour UDP
input(type="imudp" port="514") # Écouter sur le port UDP 514
```

Les alternatives de syntaxe héritée du fichier de configuration pour le serveur de réception seraient les suivantes :

Pour TCP :

```
$ModLoad imtcp # Charger le module imtcp pour TCP
$InputTCPServerRun 514 # Écouter sur le port TCP 514

```

Pour UDP :

```
$ModLoad imudp # Charger le module imudp pour UDP
$UDPServerRun 514 # Écouter sur le port UDP 514

```

Notez, cependant, que même si vous pourriez parfois rencontrer l'ancienne syntaxe rsyslog de réception de messages, elle n'est pas compatible avec sysklogd.

Pour configurer un écouteur dans rsyslogkd, vous devriez avoir à définir une variable spéciale différente dans le fichier de configuration comme décrit [ici](https://wiki.gentoo.org/wiki/Sysklogd#Remote_logging). Mais entrer dans les détails de syslogkd est hors du cadre de cet article.

De plus, je ne recommande pas d'utiliser l'ancienne syntaxe (ni l'auteur de rsyslog). Elle est présentée purement à des fins éducatives, afin que vous sachiez ce que c'est au cas où vous la rencontreriez.

Vous pouvez lire plus sur les formats de configuration de rsyslog [ici](https://www.rsyslog.com/doc/configuration/conf_formats.html).

Au cas où vous utilisez un pare-feu, vérifiez que ses paramètres autorisent les connexions UDP ou TCP entrantes sur le port 514.

### Redémarrer rsyslog et tester

Allez sur chaque machine en commençant par le serveur acceptant et redémarrez rsyslog. Ensuite, vérifiez qu'il n'y a pas d'erreurs dans ses logs :

```
sudo systemctl restart rsyslog
sudo journalctl -u rsyslog | tail -100

```

## Autres possibilités de transfert de logs

Rsyslog est un outil très puissant avec beaucoup plus de fonctionnalités que nous n'en avons couvert jusqu'à présent. Par exemple, il prend en charge le transfert direct des logs vers Elasticsearch, qui est un système de stockage de logs très performant. Mais c'est un sujet séparé qui mérite son propre article.

Pour l'instant, je vais simplement vous donner un aperçu de ce à quoi pourrait ressembler une configuration rsyslog-to-elasticsearch :

```
# Notez que vous devrez installer "rsyslog-elasticsearch" en utilisant votre gestionnaire de paquets comme apt ou yum
module(load="omelasticsearch") # Charger le module de sortie Elasticsearch

# Définir un modèle pour construire un message JSON pour chaque enregistrement rsyslog, puisque Elasticsearch fonctionne avec JSON
template(name="plain-syslog"
         type="list") {
           constant(value="{")
             constant(value="\"@timestamp\":\"")      property(name="timereported" dateFormat="rfc3339")
             constant(value="\",\"host\":\"")         property(name="hostname")
             constant(value="\",\"severity\":\"")     property(name="syslogseverity-text")
             constant(value="\",\"facility\":\"")     property(name="syslogfacility-text")
             constant(value="\",\"syslogtag\":\"")    property(name="syslogtag")
             constant(value="\",\"message\":\"")      property(name="msg" format="json")
           constant(value="\"}\n")
         }

# Rediriger tous les logs vers l'index syslog d'Elasticsearch qui écoute sur localhost:9200
*.* action(type="omelasticsearch"
       server="localhost:9200"
       searchIndex="syslog-index"
       template="plain-syslog")
```

Pour plus d'informations, reportez-vous à la [documentation](https://www.rsyslog.com/doc/configuration/modules/omelasticsearch.html).

## Comment rediriger les données des applications vers `syslog`

Jusqu'à présent, nous avons couvert la configuration d'un démon syslog. Mais comment poussons-nous réellement les logs des applications réelles vers un syslog ?

Idéalement, il serait préférable que votre application dispose déjà d'une intégration syslog et puisse être configurée pour envoyer les logs à syslog directement.

Mais que faire si ce n'est pas le cas ? Eh bien, c'est certainement dommage, car la redirection manuelle de `stdout` et `stderr` vers syslog peut présenter ses défis et inconvénients. Mais ne vous inquiétez pas, ce n'est pas si compliqué ! Au moins, en quelque sorte.

Examinons différents scénarios :

### Application autonome de l'hôte et syslog

Tout d'abord, considérons que vous avez déjà une application s'exécutant localement sur votre machine hôte (sans conteneurisation). Il existe plusieurs façons de rediriger ses logs dans ce cas.

Au lieu d'utiliser des commandes d'exemple générales et de répéter constamment « changer <you_app_blah_blah> dans la commande ci-dessus en conséquence » (ce dont je suis assez fatigué à ce stade), je vais installer une véritable application et montrer la redirection avec des exemples concrets.

L'application choisie sera le courtier Mosquitto, car je suis très amateur de MQTT, mais vous pouvez utiliser ce que vous voulez, car ce n'est qu'un exemple.

Oh, et au fait, Mosquitto fournit une intégration directe avec syslog. Il suffit d'un petit changement (`log_dest syslog`) dans son fichier de configuration. Mais nous n'allons pas nous pencher sur cela, puisque notre hypothèse est que nous travaillons avec une application incapable d'interfacer directement avec syslog.

Voici comment installer le courtier sur les systèmes basés sur Debian :

```
sudo apt-get update
sudo apt-get install mosquitto
```

Et voici l'installation basée sur RedHat :

```
sudo yum install epel-release
sudo yum install mosquitto
```

Après l'installation, Mosquitto pourrait être automatiquement exécuté en arrière-plan, donc je l'arrête avec `sudo systemctl stop mosquitto`.

#### Redirection des logs vers syslog lors de l'exécution en avant-plan

Vous pouvez exécuter Mosquitto en avant-plan et rediriger tous ses logs vers syslog en utilisant le niveau « info » et la facilité local0 :

```
sudo mosquitto -c /etc/mosquitto/mosquitto.conf -v 2>&1 | sudo logger -t mosquitto -p local0.info

```

* L'option `-c` spécifie un fichier de configuration Mosquitto non par défaut et peut être omise.
* `-v` spécifie un mode verbeux qui produit plus de sortie.
* Le drapeau `-t` fourni à la commande « logger » est un TAG représentant le nom du programme.

Notez que la facilité par défaut de l'outil logger est `user` et le niveau de gravité par défaut est `notice`.

Transférer toute la sortie dans syslog avec un niveau de gravité commun est bien et tout, mais il serait plus logique de pouvoir distinguer au moins entre les messages d'information et d'erreur.

Pour pouvoir distinguer ceux-ci, vous devrez écrire un script bash personnalisé. Ci-dessous, vous pouvez voir un exemple. Notez que la partie étrange « > >(...) » est une fonctionnalité de substitution Bash.

```
#!/bin/bash

# Définir votre commande d'application ici
command="/usr/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf -v"
programname="mosquitto"

# Utiliser la substitution de processus pour gérer stdout et stderr séparément
{
    $command 2> >(while read line; do logger -p local0.error -t "$programname" "$line"; done) \
                             > >(while read line; do logger -p local0.info -t "$programname" "$line"; done)
} 

```

Pour exécuter le script ci-dessus, sauvegardez-le simplement dans un fichier, donnez-lui des permissions d'exécution avec `sudo chmod +x /path/to/your_script.sh`, et exécutez-le avec `sudo ./your_script.sh`.

Une chose à savoir est que démarrer Mosquitto n'est pas la commande la plus adaptée pour l'exemple ci-dessus, car il redirige toute sa sortie de journalisation vers stderr par défaut. Vous ne verrez donc que des messages avec un niveau de gravité « erreur » dans les fichiers de log syslog.

Voici maintenant un exemple de script bash si vous souhaitez déterminer le niveau de gravité en analysant chaque enregistrement de log de l'application à partir de stdout ou stderr et baser un niveau de gravité sur certaines sous-chaînes spécifiques dans chaque enregistrement (par exemple, « ERROR », « WARN », « INFO », etc.) :

```
#!/bin/bash

# Définir votre commande d'application ici
command="/usr/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf -v"
programname="mosquitto"

# Exécuter la commande et canaliser sa sortie stdout et stderr vers une boucle while
$command 2>&1 | while read line; do
    # Déterminer le niveau de gravité en fonction du contenu de la ligne
    if [[ "$line" == *"Error:"* ]]; then
        logger -t "$programname" -p user.err "$line" # Transférer les messages d'erreur en tant qu'erreurs
    elif [[ "$line" == *"Warning"* ]]; then
        logger -t "$programname" -p user.warning "$line" # Transférer les messages d'avertissement en tant qu'avertissements
    else
        logger -t "$programname" -p user.info "$line" # Transférer tous les autres messages en tant qu'informations
    fi
done

```

#### Redirection des logs vers syslog lors de l'exécution en arrière-plan avec systemctl

De nombreuses applications s'exécutent en tant que démons (en arrière-plan). Souvent, elles peuvent être démarrées et gérées à l'aide de l'outil de gestion de processus `systemctl` ou similaire.

Si vous souhaitez rediriger les logs d'une application qui s'exécute en tant que démon systemctl vers syslog, suivez l'exemple ci-dessous.

Voici les étapes que vous devrez effectuer lors de l'exécution du courtier Mosquitto en arrière-plan :

Étape 1 : créer un script sh personnalisé :

```
sudo touch /usr/local/bin/mosquitto_with_logger.sh

```

Étape 2 : ouvrez le fichier et ajoutez le contenu suivant :

```
#!/bin/bash
/usr/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf -v 2>&1 | logger -t mosquitto

```

Étape 3 : ajoutez les permissions d'exécution au script :

```
sudo chmod +x /usr/local/bin/mosquitto_with_logger.sh

```

Étape 4 : créez un fichier d'unité systemd :

```
sudo touch /etc/systemd/system/mosquitto_syslog.service 

```

Étape 5 : ouvrez le fichier et ajoutez ce qui suit :

```
[Unit]
Description=Mosquitto MQTT Broker avec journalisation personnalisée
After=network.target

[Service]
ExecStart=/usr/local/bin/mosquitto_with_logger.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target

```

Étape 6 : rechargez systemd, activez le service personnalisé pour qu'il s'exécute au démarrage du système, et enfin démarrez-le :

```
sudo systemctl daemon-reload
sudo systemctl enable mosquitto_syslog.service
sudo systemctl start mosquitto_syslog.service

```

#### Redirection des logs à partir de fichiers de log existants

Au cas où votre application ne journalise que dans un fichier et que vous souhaitez rediriger ces logs vers syslog, consultez le fichier de configuration rsyslog suivant que vous pouvez placer dans `/etc/rsyslog.d/` avec une extension de fichier `.conf` :

```
module(load="imfile" PollingInterval="10") # Charger le module imfile

# Pour les logs d'information
input(type="imfile"
      File="/path/to/your/app-info.log"
      Tag="myapp"
      Severity="info"
      Facility="local0")

# Pour les logs d'erreur
input(type="imfile"
      File="/path/to/your/app-error.log"
      Tag="myapp"
      Severity="error"
      Facility="local0")

# vous pouvez mettre vos actions qui transféreront les données ici
# ou vous fier aux actions du fichier rsyslog.conf original qui importe ce fichier

```

La configuration ci-dessus suppose que vous avez des fichiers séparés pour les logs d'information et d'erreur.

En principe, vous pourriez également transférer tout le contenu d'un seul fichier en attribuant une gravité commune ou en essayant d'analyser chaque nouvelle ligne dans le fichier et de deviner son niveau de log prévu. Cela nécessiterait que nous utilisions les jeux de règles de rsyslog similaires à ce qui suit :

```
module(load="imfile" PollingInterval="10") # Charger le module d'entrée imfile

# Modèle pour formater les messages avec la gravité et la facilité d'origine
template(name="CustomFormat" type="string" string="<%PRI%>%TIMESTAMP% %HOSTNAME% %msg%\n")

# Surveiller un fichier de log spécifique
input(type="imfile"
      File="/path/to/your/logfile.log"
      Tag="myApp"
      Ruleset="guessSeverity")

# Jeu de règles pour analyser les entrées de log et deviner la gravité
ruleset(name="guessSeverity") {
    # Utiliser des filtres basés sur les propriétés pour vérifier le contenu du message et le router en conséquence
    if ($msg contains "Error:") then {
        action(type="omfile"
               File="/var/log/errors.log" # Spécifier le fichier de log pour les messages d'erreur
               Template="CustomFormat"
              )
    } else if ($msg contains "Warning:") then {
        action(type="omfile"
               File="/var/log/warnings.log" # Spécifier le fichier de log pour les messages d'avertissement
               Template="CustomFormat"
              )
    } else {
        action(type="omfile"
               File="/var/log/info.log" # Spécifier le fichier de log par défaut pour les autres messages
               Template="CustomFormat"
              )
    }
}

```

Vous devez vous assurer que `/path/to/your/logfile.log` existe avant d'appliquer la configuration ci-dessus.

Nous avons utilisé des jeux de règles ci-dessus, ce qui est une autre fonctionnalité intéressante de rsyslog. Vous pouvez en lire plus à ce sujet dans la [documentation officielle](https://www.rsyslog.com/doc/concepts/multi_ruleset.html).

Cependant, la configuration ci-dessus définit explicitement la destination des messages traités en les dirigeant vers différents fichiers en fonction de leur gravité. Si vous souhaitez transférer les messages vers le `/var/log/messages` ou `/var/log/syslog` standard, vous devrez le spécifier explicitement (et modifier/ajouter plus de modèles pour refléter les niveaux de gravité appropriés).

Mais que faire si vous avez de nombreuses autres règles dans votre fichier de configuration principal rsyslog ? Vous ne voulez pas les répéter dans le jeu de règles ci-dessus et vous voulez simplement analyser le niveau de gravité et passer l'enregistrement à la configuration principale de rsyslog pour gérer le reste ?

Malheureusement, je n'ai pas trouvé de moyen élégant de faire cela. Il n'y a qu'une approche astucieuse pour resoumettre votre enregistrement à rsyslog en utilisant l'utilitaire `logger` et le module `omprog`. Je vais montrer cette approche de toute façon pour être complet, et puisque c'est un bon moyen de voir plus de fonctionnalités de rsyslog. Mais soyez conscient que cela implique un certain surcoût, puisque vous invoquerez essentiellement rsyslog deux fois pour chaque enregistrement.

Pour resoumettre un enregistrement à rsyslog, incluez le module `omprog` :

```
module(load="omprog")
```

Et changez les actions à l'intérieur de l'arbre if-else en ce qui suit :

```
action(type="omprog"
        Template="CustomFormat" # Propriété facultative pour formater le message
        binary="/usr/bin/logger -t myApp -p local0.error"
      )

```

Au fait, n'oubliez pas de vous assurer que les fichiers de log sont accessibles à l'utilisateur sous lequel rsyslog s'exécute.

Je recommande de garder toute la logique d'analyse et de redirection de log dans les fichiers de configuration rsyslog. Mais si vous ne voulez pas le faire, et que vous préférez créer une configuration rsyslog séparée dans votre cas d'utilisation spécifique, ci-dessous vous pouvez trouver un script bash pour faire ce que nous avons fait ci-dessus.

Le script suit un fichier de log, analyse chaque enregistrement pour attribuer un niveau de gravité approprié, et transfère ces enregistrements vers syslog :

```
#! /bin/bash

tail -F /path/to/log-file.log | while read line; do
  if [[ "$line" == *"Error:"* ]]; then
    logger -p local0.err "$line" # Transférer les messages d'erreur en tant qu'erreurs
  else
    logger -p local0.info "$line" # Transférer les autres messages en tant qu'informations
  fi
done

```

Si vous souhaitez tester si le script ci-dessus fonctionne, créez simplement un `log-file.log`, exécutez le script, puis émettez `echo "Error: this is a test error message" >> log-file.log` dans un terminal séparé. Après cela, vous devriez voir le message d'erreur dans le fichier de log rsyslog `/var/log/messages` ou `/var/log/syslog`.

L'exécution directe du script ci-dessus bloquera votre terminal et attendra sa compilation. Donc pour des scénarios pratiques, vous voudrez le lancer en arrière-plan en utilisant, par exemple, `setsid` ou d'autres outils.

Une chose importante avant de continuer est que lors du test des scripts et configurations ci-dessus, soyez conscient que votre rsyslog peut avoir une fonctionnalité de déduplication activée. Si c'est le cas, les messages en double peuvent ne pas être traités. Il s'agit d'une fonctionnalité héritée, mais il y a des chances qu'elle soit toujours dans votre configuration (principalement sur les systèmes basés sur Debian). Lisez plus d'informations [ici](https://www.rsyslog.com/doc/configuration/action/rsconf1_repeatedmsgreduction.html).

De plus, vous pouvez supprimer [les messages indésirables](https://www.rsyslog.com/discarding-unwanted-messages/).

### Docker et syslog

Les logs par défaut générés vers stdout/stderr par les applications s'exécutant dans des conteneurs Docker sont stockés dans des fichiers sous /var/lib/docker/containers (le chemin exact peut dépendre de votre système).

Pour accéder aux logs d'un conteneur particulier, vous pouvez utiliser `docker logs <container name or container id>`. Mais que faire si vous souhaitez rediriger stdout et stderr de vos applications conteneurisées directement vers syslog ? Alors il existe à nouveau plusieurs options. Ci-dessous, j'utiliserai un conteneur Mosquitto broker comme exemple.

#### Configuration d'un seul conteneur Docker

Si vous démarrez un conteneur en utilisant une commande `docker run`, reportez-vous à l'exemple ci-dessous :

```
docker run -it -d -p 1883:1883 -v /etc/mosquitto/mosquitto.conf:/mosquitto/config/mosquitto.conf --log-driver=syslog --log-opt syslog-address=udp://192.168.0.1:514 --log-opt tag="docker/{{.Name}}/{{.ID}}" eclipse-mosquitto:2

```

Dans cet exemple :

* `--log-driver=syslog` spécifie que le pilote syslog doit être utilisé.
* `--log-opt syslog-address=udp://192.168.0.1:514` spécifie le protocole, l'adresse et le port de votre serveur syslog. Si vous avez un serveur syslog s'exécutant localement et que vous souhaitez simplement que vos logs apparaissent sous `/var/log` sur votre machine locale, vous pouvez omettre cette option.
* `--log-opt tag="docker-{{.Name}}-{{.ID}}"` définit un champ TAG personnalisé pour les logs de ce conteneur. `{{.Name}}` se résoudra en nom du conteneur, tandis que `{{.ID}}` en ID du conteneur. Notez que vous ne devez pas utiliser de barres obliques (« / ») ici car rsyslog ne les analysera pas et tronquera les parties TAG qui suivent. Mais cela fonctionnera avec des tirets (« - »). Cela implique également que rsyslog fait de son mieux pour analyser tous les formats de messages possibles et qu'il ne fait pas toujours ce que vous attendez. Vous pouvez en lire plus [ici](https://www.rsyslog.com/doc/whitepapers/syslog_parsing.html).
* Le reste des drapeaux comme `-it -d` ou `-p` et `-v` sont des drapeaux spécifiques au conteneur qui spécifient le mode du conteneur, les ports mappés, les volumes, etc. Vous pouvez en lire plus en détail dans [cet article](https://cedalo.com/blog/mosquitto-docker-configuration-ultimate-guide/).

#### Configuration d'un service Docker via un fichier docker-compose

Si vous utilisez docker-compose au lieu d'exécuter directement `docker run`, voici un exemple de fichier `docker-compose.yml` :

```
version: '3'
services:
  mosquitto:
    image: eclipse-mosquitto:2
    logging:
      driver: syslog
      options:
        syslog-address: "udp://192.168.0.1:514"
        tag: "docker/{{.Name}}/{{.ID}}"
   ports:
     - 1883:1883
     - 8883:8883
     - 9001:9001
   volumes:
     - ./mosquitto/config:/mosquitto/config

```

Portez une attention particulière aux directives `driver`, `syslog-address` et `tag`, qui sont similaires à l'exemple docker-run.

#### Configuration d'une valeur par défaut pour chaque conteneur via le démon Docker

Si vous ne souhaitez pas spécifier les options du pilote de log dans chaque fichier docker-compose ou chaque fois que vous utilisez une commande « docker run », vous pouvez définir la configuration suivante dans `/etc/docker/daemon.json` qui l'appliquera globalement.

```
{
  "log-driver": "syslog",
  "log-opts": {
    "syslog-address": "udp://192.168.0.1:514",
    "tag": "docker/{{.Name}}/{{.ID}}"
  }
}

```

Après cela, redémarrez docker avec `sudo systemctl restart docker` ou `sudo service docker restart`.

#### Activation des applications à l'intérieur de Docker pour journaliser directement vers syslog

Si vous avez une application capable de transférer ses logs directement vers syslog (comme Mosquitto) et que vous souhaitez l'utiliser dans un conteneur, vous devrez mapper le `/dev/log` local vers `/dev/log` à l'intérieur du conteneur.

Pour cela, vous pouvez utiliser la section `volumes` de `docker-compose.yml` ou le drapeau `-v` de la commande `docker run`.

### Comment utiliser les bibliothèques de journalisation pour votre langage de programmation pour journaliser vers syslog

Maintenant, que faire si vous développez une application ou devez créer un script d'agrégation personnalisé qui transfère des messages de certaines applications ou appareils vers syslog ?

Pour donner un exemple concret, vous pourriez vouloir construire une console de contrôle pour vos appareils IoT.

Supposons que vous avez un ensemble d'appareils qui se connectent à un courtier MQTT. Chaque fois que ces appareils génèrent des messages de log, ils les publient sur un certain sujet MQTT.

Dans ce cas, vous pourriez vouloir créer un script personnalisé qui s'abonne à ce sujet, reçoit des messages et les transfère à syslog pour un stockage et un traitement ultérieurs. De cette manière, vous rassemblerez tous vos logs en un seul endroit avec la possibilité de les visualiser et de les gérer avec des outils tels que Splunk, Elastic stack, etc., ou d'exécuter des statistiques ou des rapports sur eux.

Ci-dessous, je vais vous montrer comment envoyer des messages depuis votre application Node.js ou Python vers syslog. Cela vous permettra d'implémenter vos applications personnalisées qui fonctionnent avec syslog.

Notez que le scénario d'exemple ci-dessus a donné un cas d'utilisation pratique pour ce que nous allons voir dans cette section. Mais nous n'explorerons pas davantage ce sujet, car cela nécessiterait un peu plus de temps et d'efforts et pourrait nous éloigner du point principal de ce guide.

Mais si vous êtes intéressé par la gestion de quelque chose comme cela, vous pouvez facilement étendre les scripts que je montre ci-dessous en utilisant la bibliothèque MqttJS et en vous connectant au courtier avec Node.js comme décrit [ici](https://cedalo.com/blog/nodejs-mqtt-usage-with-mosquitto-example/) ou en utilisant le client Paho MQTT Python comme montré dans ce [tutoriel](https://cedalo.com/blog/configuring-paho-mqtt-python-client-with-examples/).

#### Client Node.js

Malheureusement, il n'existe pas beaucoup de bibliothèques populaires, maintenables et éprouvées pour la journalisation syslog avec Node.js. Mais une bonne option que vous pouvez utiliser est une bibliothèque polyvalente pour la journalisation appelée winston. Elle est assez utilisable dans les petits et grands projets.

Lors de l'installation de winston, vous devrez également installer un transport personnalisé appelé `winston-syslog` :

```
npm install winston winston-syslog
```

Voici un exemple d'utilisation :

```js
const winston = require('winston');
require('winston-syslog').Syslog;

const logger = winston.createLogger({
  levels: winston.config.syslog.levels,
  format: winston.format.printf((info) => {
    return `${info.message}`;
  }),
  transports: [
    new winston.transports.Syslog({
      app_name: 'MyNodeApp',
      facility: 'local0',
      type: 'RFC5424',
      protocol: 'unix', // Utiliser le socket Unix
      path: '/dev/log', // Chemin vers le socket Unix pour syslog
    })
  ]
});

// Messages de journalisation de différents niveaux de gravité
// Lorsque vous utilisez le niveau emerg, vous pourriez obtenir des avertissements dans votre terminal
// Mais ne paniquez pas - c'est attendu, puisque c'est le niveau le plus sévère
logger.emerg('Ceci est un message d\'urgence.');
logger.alert('Ceci est un message d\'alerte.');
logger.crit('Ceci est un message critique.');
logger.error('Ceci est un message d\'erreur.');
logger.warning('Ceci est un message d\'avertissement.');
logger.notice('Ceci est un message de notification.');
logger.info('Ceci est un message d\'information.');
logger.debug('Ceci est un message de débogage.');


logger.end();

```

Notez que si vous supprimez la propriété `format` de l'objet passé à `createLogger`, vous verrez une charge utile JSON composée d'un message et d'un niveau de gravité pour les messages dans syslog. C'est le format par défaut des enregistrements analysés par `winston-syslog`.

#### Client Python

Dans le cas de Python, vous n'avez même pas besoin d'installer de dépendances tierces, car Python est déjà livré avec deux bibliothèques assez capables : syslog et logging. Vous pouvez utiliser l'une ou l'autre.

La première est conçue pour travailler spécifiquement avec syslog, tandis que la seconde peut également gérer d'autres transports de log (stdout, fichier, etc.). Elle peut également souvent être étendue de manière transparente pour fonctionner avec syslog pour les projets existants.

Voici un exemple d'utilisation de la bibliothèque « syslog » :

```python
import syslog

# Journaliser un seul message d'information
# Déclenche un appel implicite à openlog() sans paramètres
syslog.syslog(syslog.LOG_INFO, "Message an info message.")

# Vous pouvez également définir la facilité
syslog.openlog(ident="MyPythonApp", facility=syslog.LOG_LOCAL0)

# messages avec différents niveaux de gravité et la facilité LOG_LOCAL0
syslog.syslog(syslog.LOG_EMERG, "Ceci est un message d'urgence.")
syslog.syslog(syslog.LOG_ALERT, "Ceci est un message d'alerte.")
syslog.syslog(syslog.LOG_CRIT, "Ceci est un message critique.")
syslog.syslog(syslog.LOG_ERR, "Ceci est un message d'erreur.")
syslog.syslog(syslog.LOG_WARNING, "Ceci est un message d'avertissement.")
syslog.syslog(syslog.LOG_NOTICE, "Ceci est un message de notification.")
syslog.syslog(syslog.LOG_INFO, "Ceci est un message d'information.")
syslog.syslog(syslog.LOG_DEBUG, "Ceci est un message de débogage.")

# Fermer le log si nécessaire (généralement géré automatiquement à la sortie du programme)
syslog.closelog()

```

Et voici un exemple d'utilisation de la bibliothèque « logging ». Notez que « logging » a un ensemble prédéfini de niveaux de log qui ne s'aligne pas complètement avec les niveaux de gravité syslog (par exemple, certains niveaux comme « crit », « emerg » et « notice » sont manquants par défaut). Vous pouvez cependant l'étendre si nécessaire, mais nous allons garder cela simple ici. Pour plus d'informations, reportez-vous [ici](https://docs.python.org/3/library/logging.handlers.html#:~:text=LOG_LOCAL7-,mapPriority,-(levelname)) :

```python
import logging
import logging.handlers

# Créer un logger
logger = logging.getLogger('MyPythonApp') # Définir le nom de l'application
logger.setLevel(logging.INFO) # Définir le niveau de log par défaut

# Créer un SysLogHandler
syslog_handler = logging.handlers.SysLogHandler(address='/dev/log', facility=logging.handlers.SysLogHandler.LOG_LOCAL0)

# Optionnel : formater le message de log
# Définir un format qui peut être analysé par rsyslog.
# Celui présenté ci-dessous est une simplification de RFC3164
# Notez que la valeur PRI sera préfixée automatiquement au début
formatter = logging.Formatter("%(name)s: %(message)s") 
syslog_handler.setFormatter(formatter)

# Ajouter le SysLogHandler au logger
logger.addHandler(syslog_handler)

# Journaliser des messages avec des niveaux de log standard
logger.debug('Ceci est un message de débogage.')
logger.info('Ceci est un message d\'information.')
logger.warning('Ceci est un message d\'avertissement.')
logger.error('Ceci est un message d\'erreur.')
logger.critical('Ceci est un message critique.')
```

Alternativement, vous pouvez utiliser une bibliothèque non standard « loguru » ou une autre. Les bibliothèques intégrées sont assez puissantes et suffisantes pour la plupart des cas d'utilisation. Mais si vous utilisez déjà une bibliothèque comme loguru dans votre projet, vous pouvez l'étendre pour qu'elle fonctionne avec syslog :

```python
from loguru import logger
import logging
import logging.handlers

class SyslogHandler:
    def __init__(self, appname, address='/dev/log', facility=logging.handlers.SysLogHandler.LOG_USER):
        self.appname = appname
        self.handler = logging.handlers.SysLogHandler(address=address, facility=facility)
        self.loglevel_map = {
            "TRACE": logging.DEBUG,
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "SUCCESS": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }

    def write(self, message):
        # Extraire le niveau de log, le texte du message et autres informations nécessaires.
        loglevel = self.loglevel_map.get(message.record["level"].name, logging.INFO)
        logmsg = f"{self.appname}: {message.record['message']}"
        
        # Créer un enregistrement de log que le système de journalisation standard peut comprendre.
        record = logging.LogRecord(name=self.appname, level=loglevel, pathname="", lineno=0, msg=logmsg, args=(), exc_info=None)
        self.handler.emit(record)

    def flush(self):
        pass

# Configurer Loguru pour utiliser le SyslogHandler défini ci-dessus
appname = "MyPythonApp"
logger.add(SyslogHandler(appname), format="{message}")

# Maintenant, vous pouvez journaliser des messages et ils seront dirigés vers syslog
logger.info("Ceci est un message d'information envoyé à syslog.")
```

## Conclusion

Dans ce manuel, vous avez tout appris sur syslog. Nous avons clarifié la terminologie confuse, exploré ses cas d'utilisation et vu de nombreux exemples d'utilisation.

Les points principaux à retenir sont :

* Syslog est un protocole décrivant le format commun d'échange de messages entre les applications et les démons syslog. Ces derniers prennent en charge l'analyse des messages, les enrichissements, le transport et le stockage.
* Les gens font communément référence de manière informelle à l'infrastructure des démons syslog, leur configuration, les fichiers de stockage des logs et les sockets d'acceptation comme « syslog ». « Rediriger les logs vers syslog » signifie rediriger les logs vers le socket `/dev/log` où ils seront récupérés par un démon syslog, traités et sauvegardés selon sa configuration.
* Il existe deux formats syslog standard : l'obsolète RFC3164 et un plus récent RFC5424.
* Certains démons syslog bien connus incluent : sysklogd (Linux), rsyslog (Linux), syslog-ng (Linux) et nxlog (multiplateforme).
* Rsyslog et autres démons de log peuvent transférer les logs d'un serveur à un autre. Vous pouvez utiliser cela pour créer une infrastructure de collecte de logs avec un serveur central traitant tous les logs provenant du reste des nœuds.
* Bien que cela entraîne un certain surcoût, il est important de transférer les logs en utilisant le protocole TLS au cas où ils sont transportés sur un réseau non fiable.
* Le démon rsyslog est un outil léger et puissant avec de nombreuses fonctionnalités. Il peut collecter des messages de différentes sources, y compris des fichiers et le réseau. Il peut traiter ces données en utilisant des modèles et des jeux de règles personnalisables, puis soit les sauvegarder sur le disque, soit les transférer ailleurs. Rsyslog peut également s'intégrer directement avec Elasticsearch, entre autres capacités.
* Il est possible de transférer les logs d'une application vers syslog même si elle ne fournit pas d'intégration native. Vous pouvez le faire pour les applications autonomes de l'hôte, les systèmes conteneurisés ou via un script d'agrégation écrit dans un langage de programmation de votre choix.
* La sortie des applications autonomes (stdout et stderr) peut être capturée et redirigée vers l'outil utilitaire Linux `logger`. Docker fournit un pilote syslog séparé pour la journalisation, tandis que de nombreux langages de programmation disposent de bibliothèques de journalisation dédiées.

Merci d'avoir lu, et bon logging !