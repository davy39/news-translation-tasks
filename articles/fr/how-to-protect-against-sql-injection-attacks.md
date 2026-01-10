---
title: Attaques par injection SQL – Comment utiliser SQLMap pour trouver les vulnérabilités
  des bases de données
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2022-12-13T00:40:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-protect-against-sql-injection-attacks
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/Stealth-Security
seo_title: Attaques par injection SQL – Comment utiliser SQLMap pour trouver les vulnérabilités
  des bases de données
---

Blog-Banner--27-.png
étiquettes:
- nom: cybersécurité
  slug: cybersecurite
- nom: base de données
  slug: base-de-donnees
- nom: sécurité de l'information
  slug: securite-de-linformation
- nom: '#infosec'
  slug: infosec
- nom: test d'intrusion
  slug: test-dintrusion
- nom: SQL
  slug: sql
seo_title: null
seo_desc: 'Les bases de données sont l'épine dorsale de toute application. Elles nous offrent un moyen de stocker et d'organiser de grandes quantités de données de manière à ce que nous puissions y accéder, les gérer et les mettre à jour facilement.

Des petites entreprises aux grandes entreprises, les bases de données jouent un rôle critique dans le maintien des systèmes en fonctionnement. Les acteurs malveillants cherchent toujours à prendre le contrôle des bases de données lors des cyberattaques.

Dans cet article, vous apprendrez comment les attaquants peuvent prendre le contrôle des bases de données et ce que vous pouvez faire à ce sujet. 

**Notez que cet article est à des fins éducatives uniquement**. Si vous faites quelque chose d'illégal et que vous avez des ennuis, je ne suis pas responsable. Obtenez toujours la permission du propriétaire du site/système avant de scanner / forcer brutalement / exploiter un système. 

## Qu'est-ce que l'injection SQL ?

L'injection SQL est un type de cyberattaque dans lequel un attaquant insère du code malveillant dans une instruction SQL. Si elle réussit, elle aidera l'attaquant à accéder à des données sensibles dans une base de données. 

Une fois que l'attaquant prend le contrôle de la base de données, il peut voler, modifier ou même supprimer les données.

Voici quelques scénarios d'injection SQL.

* Un attaquant pourrait insérer un morceau de code malveillant dans un formulaire de connexion. Par exemple, si le formulaire de connexion attend que l'utilisateur entre son nom d'utilisateur et son mot de passe, l'attaquant pourrait entrer un nom d'utilisateur comme admin’ OR ‘1’=‘1. Cela évaluera toujours à vrai et permettra à l'attaquant de se connecter sans connaître le mot de passe réel.
* Un attaquant pourrait insérer un morceau de code malveillant dans un formulaire de recherche. Par exemple, si le formulaire de recherche attend que l'utilisateur entre un mot-clé, l'attaquant peut entrer un mot-clé comme ’ OR ‘1’=‘1. Cela retournera tous les enregistrements de la base de données, plutôt que ceux qui correspondent au mot-clé.
* Un attaquant peut insérer un morceau de code malveillant dans un formulaire qui permet aux utilisateurs de mettre à jour leurs informations. Par exemple, si le formulaire attend que l'utilisateur entre son numéro de téléphone, l'attaquant pourrait entrer un numéro de téléphone comme ’; DROP TABLE users; --,. Cela supprimera la table entière des utilisateurs de la base de données.

Ce ne sont que quelques exemples d'attaques par injection SQL. Il existe de nombreuses autres façons dont les attaquants peuvent utiliser ces techniques pour accéder à une base de données. Les bases de données qui ne sont pas mises à jour/maintenues régulièrement seront souvent vulnérables aux attaques par injection SQL.

## Qu'est-ce que SQL Map ?

[SQLmap](https://sqlmap.org/) est un outil open-source qui trouve et exploite automatiquement les vulnérabilités d'injection SQL. Nous pouvons l'utiliser pour tester les applications web pour les vulnérabilités d'injection SQL et accéder à une base de données vulnérable.

SQLmap est un outil préféré parmi les testeurs d'intrusion pour sa facilité d'utilisation et sa flexibilité. Il est écrit en Python et fonctionne sur Windows, Linux et MacOS.

Nous pouvons utiliser SQLmap pour effectuer une large gamme d'attaques. Cela inclut l'identification des bases de données, l'extraction de données et même la prise de contrôle d'une base de données entière. Nous pouvons également l'utiliser pour contourner les formulaires de connexion et exécuter des commandes arbitraires sur le système d'exploitation sous-jacent.

## Comment installer SQLMap

SQLMap est préinstallé dans Kali Linux et Parrot OS. Pour installer SQLMap dans les systèmes basés sur Ubuntu / Debian, utilisez le gestionnaire de paquets apt.

```
apt install sqlmap
```

Pour installer SQLMap sur Mac, nous pouvons utiliser [Homebrew](https://brew.sh/).

```
brew install sqlmap
```

Si vous utilisez d'autres plateformes, vous pouvez [trouver les instructions d'installation ici](https://sqlmap.org/).

Une fois l'installation terminée, nous pouvons vérifier le menu d'aide en utilisant la commande `-h`. Cela sera également une référence pratique lors de l'utilisation de SQLMap.

```
sqlmap -h
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-28.png)
_Menu d'aide de SQLMap_

SQLMap fournit également un menu d'aide détaillé. Nous pouvons y accéder en utilisant la commande `-hh`.

```
sqlmap -hh
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-29.png)
_Menu d'aide avancé de SQLMap_

Maintenant que nous avons installé SQLMap, voyons comment travailler avec lui.

## **Comment utiliser SQL Map**

SQLMap est un outil utilisé pour l'exploitation automatisée des vulnérabilités d'injection SQL. Nous pouvons utiliser SQLMap pour tester les sites web et les bases de données pour les vulnérabilités et exploiter ces vulnérabilités pour prendre le contrôle de la base de données.

Pour utiliser SQLMap, nous devons d'abord identifier un site web ou une base de données vulnérable à l'injection SQL. Nous pouvons le faire manuellement ou utiliser SQLMap pour scanner le site web. Une fois que nous avons identifié un site web ou une base de données vulnérable, nous pouvons utiliser SQLMap pour l'exploiter.

Voici la commande de base de SQLMap :

```
$ sqlmap -u [URL] -p [paramètre] --dbs
```

Cette commande indiquera à SQLMap de scanner l'URL et le paramètre spécifiés pour les vulnérabilités. Cela inclut l'exposition de données, la mise à jour de données, ou même le vidage de la base de données entière.

Le moyen le plus simple de vérifier si un site web est vulnérable à l'injection SQL est via les paramètres de requête. Supposons qu'un site web liste les informations des utilisateurs en utilisant un paramètre id – par exemple, testsite.com/page.php?id=1.

Cela peut être passé en entrée à SQLMap et SQLMap scannera automatiquement le site pour voir si la base de données est vulnérable. Voici la commande :

```
sqlmap -u http://testsite.com/page.php?id=1 --dbs
```

Le drapeau `-u` est utilisé pour spécifier une URL et la commande `--dbs` indique à SQLMap d'essayer d'énumérer la base de données.

Si l'attaque réussit, SQLMap listera la base de données utilisée ainsi que la liste des tables.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-30.png)
_Sortie de SQLMap_

Une fois que nous avons obtenu un premier point d'appui, nous pouvons maintenant travailler avec la base de données. Voici la commande pour lister les tables dans une base de données.

```
sqlmap -u https://testsite.com/page.php?id=1 -D <nom_bd> --tables
```

Pour lister les colonnes dans une table, nous pouvons utiliser cette commande :

```
sqlmap -u https://testsite.com/page.php?id=7 -D <nom_base_de_donnees> -T <nom_table> --columns
```

Pour vider une base de données entière, voici la commande :

```
sqlmap -u https://testsite.com/page.php?id=7 -D <nom_base_de_donnees> --dump-all
```

SQLMap fournit de nombreuses autres commandes utiles comme la définition de cookies, le cyclage des agents utilisateurs, et bien d'autres. Pour plus d'informations et une liste complète des options, vous pouvez [vous référer à la documentation de SQLMap](https://github.com/sqlmapproject/sqlmap/wiki/Introduction).

## Comment se défendre contre les attaques par injection SQL

Pour prévenir les attaques par injection SQL, nous devons suivre ces étapes :

### Utiliser des requêtes paramétrées

Utilisez toujours des requêtes paramétrées lors de l'interaction avec une base de données. Cela signifie que nous devons utiliser des espaces réservés dans nos instructions SQL pour toute entrée utilisateur. Nous pouvons ensuite fournir l'entrée en tant que paramètre séparé lorsque la requête est exécutée. 

Cela empêchera un attaquant d'être en mesure d'injecter du SQL arbitraire dans nos instructions SQL.

### Ne jamais faire confiance à l'entrée utilisateur

Nous devons toujours vérifier et assainir toute entrée utilisateur pour nous assurer qu'elle est sûre. Nous devons nous assurer que l'entrée ne contient aucun caractère dangereux ou code malveillant. 

Cela aidera à prévenir un attaquant d'être en mesure d'injecter des requêtes SQL même s'il est en mesure de trouver un moyen de contourner notre utilisation de requêtes paramétrées.

### Utiliser des instructions préparées

Si la base de données prend en charge les instructions préparées, nous devons les utiliser au lieu des requêtes paramétrées. 

Les instructions préparées sont des instructions SQL pré-compilées. Nous pouvons exécuter ces instructions plusieurs fois avec différents paramètres. 

Cela rendra plus difficile pour un attaquant d'injecter du code malveillant puisque les instructions préparées sont pré-compilées.

### Authentification et contrôles d'accès

Nous devons avoir une authentification forte et des contrôles d'accès à notre base de données. Cela garantira que seuls les utilisateurs autorisés sont en mesure d'accéder à notre base de données et la protège des acteurs malveillants.

### Surveillance et alertes

Surveillez toujours votre base de données pour les activités suspectes et définissez des alertes. Cela inclut les tentatives de connexion échouées ou un grand nombre de requêtes SQL. 

Cela peut nous aider à détecter une attaque par injection SQL dès le début, et à prendre des mesures appropriées pour l'arrêter.

## Résumé

Les bases de données sont l'épine dorsale de chaque entreprise. La mise à jour, la maintenance et la sécurisation des bases de données sont essentielles pour les protéger des acteurs malveillants. 

SQLmap est un outil puissant qui nous aide à auditer les vulnérabilités des bases de données. Il est important pour les développeurs et les professionnels de la sécurité de se familiariser avec SQLMap pour se défendre contre les attaques par injection SQL.

_Aimé cet article ? Rejoignez Stealth Security_ [_Newsletter Hebdomadaire_](https://stealthsecurity.io/) _et recevez des articles livrés dans votre boîte de réception chaque vendredi. Vous pouvez également_ [_me contacter_](https://www.linkedin.com/in/manishmshiva/) _sur Linkedin._