---
title: Comment sécuriser les serveurs Linux avec SE Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2021-10-26T17:33:34.000Z'
originalURL: https://freecodecamp.org/news/securing-linux-servers-with-se-linux
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/Enhance-Linux-server-security-with-SE-Linux--1-.png
tags:
- name: Linux
  slug: linux
- name: Security
  slug: security
- name: servers
  slug: servers
seo_title: Comment sécuriser les serveurs Linux avec SE Linux
seo_desc: "Security is an extremely important aspect of software development, server\
  \ management, and application development these days. \nAnd if you use Linux, you're\
  \ in luck – it comes with an excellent feature called SE Linux that helps you add\
  \ an additional ..."
---

La sécurité est un aspect extrêmement important du développement logiciel, de la gestion des serveurs et du développement d'applications de nos jours. 

Et si vous utilisez Linux, vous avez de la chance – il est livré avec une excellente fonctionnalité appelée SE Linux qui vous aide à ajouter une couche de sécurité supplémentaire.

## Qu'est-ce que SE Linux ?

SE Linux a été développé par la NSA (National Security Agency) pour servir des tâches de sécurité liées au gouvernement.  

SE Linux signifie Security Enhanced Linux. Il donne aux administrateurs système plus de contrôle pour fournir l'accès aux fichiers et aux processus. Avec SE Linux, les administrateurs peuvent définir un contexte et étiqueter des fichiers et les autoriser dans ce contexte.

L'accès et les permissions sont généralement hérités en fonction des groupes d'utilisateurs. Mais il existe certaines sources (comme les serveurs web et les processus) qui ont besoin d'accéder aux ports réseau et aux processus du noyau. Ceux-ci sont généralement générés par l'utilisateur root ou des utilisateurs avec un accès spécial. SE Linux vous aide à limiter qui peut accéder à ces processus spéciaux.

## Comment travailler avec SE Linux

SE Linux est inclus par défaut dans la plupart des distributions Linux. Dans cet article, je vais travailler sur Fedora. 

Gardez simplement à l'esprit que travailler avec SE Linux nécessite un accès `sudo` ou `root`.

Le fichier de configuration de SE Linux se trouve dans le dossier `/etc/sysconfig/selinux`. Regardons son contenu :

### Modes SE Linux

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-69.png)
_Fichier de configuration SE Linux_

Dans le fichier de configuration, nous pouvons changer les modes et choisir l'un des suivants :

1. **Enforced** – Activé par défaut, filtre en fonction des politiques définies.
2. **Permissive** – N'applique pas les politiques définies, mais enregistre toutes les tentatives dans les fichiers de journalisation. Ce mode est utile pour le dépannage.
3. **Disabled** – SE Linux est complètement désactivé. Cela n'est pas recommandé car cela pourrait exposer votre système à des menaces. De plus, revenir à l'application forcée pourrait créer certaines divergences.

Vous pouvez vérifier votre mode SE Linux actuel avec les commandes suivantes :

1. `getenforce`
2. `sestatus`

Si vous devez uniquement changer le mode pour la session actuelle, vous pouvez utiliser les commandes suivantes : 

1. `sudo setenforce 0` – définit le mode permissif pour la session actuelle
2. `sudo setenforce 1` – définit le mode d'application forcée pour la session actuelle

## Politiques SE Linux

Dans SE Linux, les politiques définissent l'accès des utilisateurs. Les utilisateurs définissent l'accès aux rôles et les rôles définissent l'accès aux domaines. Les domaines fournissent ensuite l'accès à certains fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-61.png)
_Politiques SE Linux_

Pour changer et modifier les accès, des 'booleans' sont définis. Nous allons examiner les booleans dans la section suivante.

### Comment gérer les politiques SE Linux avec les booleans

Comme vous le savez maintenant, les politiques SE Linux sont gérées par des booleans.

Voyons un exemple de travail sur la façon de visualiser et de définir un boolean. Dans cet exemple, nous allons définir des booleans spécifiques à `httpd`.

Tout d'abord, listez tous les modules spécifiques à http – `getsebool -a | grep httpd`.

_Ici, **`-a`** liste tous les booleans._

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-80.png)
_Liste des Booleans_

Ensuite, sélectionnons et changeons le boolean surligné en jaune dans le code ci-dessus :

```bash
getsebool httpd_can_connect_ftp
```

Maintenant, définissez la valeur sur `allow`.

```bash
setsebool -P httpd_can_connect_ftp 1
```

Dans la commande ci-dessus,

* Le drapeau P est utilisé pour rendre le changement permanent même après le redémarrage.
* `1` active le boolean.

Maintenant, lorsque vous listez le processus à nouveau, sa valeur sera autorisée.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-81.png)
_Boolean 'on'_

## Architecture SE Linux

Le diagramme ci-dessous explique comment SE Linux valide une tentative à partir de la source :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-62.png)

## Dépannage et journaux SE Linux

SE Linux produit des journaux très détaillés pour chaque tentative. Vous pouvez trouver les journaux et les consulter ici : `/var/log/audit`.

Lors du dépannage, vous devez passer en mode 'permissif' afin que tous les événements puissent être enregistrés dans les journaux. Bien que les politiques ne soient pas appliquées, les tentatives sont enregistrées dans les journaux.

## Comment désactiver et activer SE Linux

Désactiver complètement SE Linux n'est jamais une bonne option. Mais il existe certains scénarios où les politiques peuvent être contournées, comme lors du dépannage. 

Au lieu de désactiver SE Linux si vous rencontrez un petit problème, il est préférable d'investir un peu de temps dans le dépannage. 

Mais si vous devez vraiment désactiver SE Linux, suivez ces étapes : 

1. Changez le mode de 'enforcing' à 'permissive'.
2. Changez le mode de 'permissive' à 'disabled'.

## Conclusion

Apprendre SE Linux vaut votre temps et il existe d'innombrables possibilités que vous pouvez explorer en l'utilisant. 

SE Linux offre aux administrateurs un niveau de contrôle fin. Alors pourquoi ne pas l'apprendre et l'utiliser pour augmenter votre sécurité ?

Merci d'avoir lu jusqu'à la fin. Connectons-nous sur [Twitter](https://twitter.com/hira_zaira).