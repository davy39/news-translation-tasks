---
title: Tutoriel sur l'injection SQL - Qu'est-ce que l'injection SQL et comment l'éviter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-01T16:50:56.000Z'
originalURL: https://freecodecamp.org/news/what-is-sql-injection-how-to-prevent-it
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fff3e0c98be260817e495da.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: SQL
  slug: sql
seo_title: Tutoriel sur l'injection SQL - Qu'est-ce que l'injection SQL et comment
  l'éviter
seo_desc: "By Megan Kaczanowski\nSQL injection is when you insert or inject a SQL\
  \ query via input data from the client to the application. \nSuccessful attacks\
  \ allow an attacker to access sensitive data from the database, modify database\
  \ data, potentially shut th..."
---

Par Megan Kaczanowski

L'injection SQL se produit lorsque vous insérez ou injectez une requête SQL via des données d'entrée du client vers l'application. 

Les attaques réussies permettent à un attaquant d'accéder à des données sensibles de la base de données, de modifier les données de la base de données, de potentiellement arrêter la base de données ou d'émettre d'autres commandes d'administration, de récupérer le contenu des fichiers, et parfois d'émettre des commandes au système d'exploitation. 

Ce type d'attaque est relativement facile à détecter et à exploiter, il est donc particulièrement important que tout système vulnérable soit rapidement corrigé.

## Comment fonctionne l'injection SQL ?

L'injection SQL se produit lorsque des données entrent dans un programme à partir d'une source non fiable et que ces données sont utilisées pour construire dynamiquement une requête SQL. 

Parce que SQL ne distingue pas entre le plan de contrôle et le plan de données, l'attaquant peut placer un méta-caractère (un caractère non interprété comme une donnée, tel qu'un trait de soulignement _ qui, en SQL, sera lu comme un caractère générique pour un seul caractère) dans les données d'entrée, puis suivre en entrant des commandes SQL dans le plan de contrôle. 

Par exemple, dans la bande dessinée ci-dessous, si la chaîne `Robert'); DROP TABLE Students;--` était entrée dans une requête qui demandait le nom de l'étudiant, alors la requête deviendrait la suivante :

```
AND studentName = 'Robert';
DROP TABLE Students;
--'
```

La commande drop table est utilisée pour supprimer une table et toutes les lignes de cette table, tandis que la paire de traits d'union indique à la plupart des serveurs de base de données que le reste de l'instruction doit être traité comme un commentaire (permettant au serveur d'ignorer le ' restant de la requête modifiée).

![Image](https://megankaczanowski.com/content/images/2020/12/Screen-Shot-2020-12-30-at-6.23.14-PM.png)
_https://xkcd.com/327/_

De nombreux serveurs de base de données permettent l'exécution de plusieurs requêtes à la fois, tant qu'elles sont séparées par des points-virgules. Si c'est le cas, ce type d'attaque permet à l'attaquant d'exécuter plusieurs commandes contre une base de données (plusieurs serveurs de base de données, y compris Oracle, ne permettent pas ce type d'exécution).

Prévenir l'injection SQL est en fait assez simple - soit ne pas permettre les requêtes dynamiques, soit empêcher l'entrée fournie par l'utilisateur qui contient du SQL malveillant d'affecter la logique de la requête.

## Autres types d'injection SQL

Il existe quelques autres types d'injection SQL à surveiller :

### Injection SQL basée sur les erreurs

L'attaquant s'appuie sur des messages d'erreur détaillés de la base de données pour en apprendre davantage sur la structure de la base de données. Pour prévenir cela, seuls des messages d'erreur génériques doivent être affichés.

### Injection SQL aveugle

Se produit lorsque l'application est vulnérable à l'injection SQL, mais n'affiche que des messages d'erreur génériques (plutôt que des messages d'erreur détaillés ou les résultats de la requête). 

Une façon d'accéder à l'information est d'utiliser des requêtes vrai/faux et d'extraire l'information une question à la fois. Une autre option est d'envoyer une commande qui demande à la base de données d'attendre un certain temps avant de retourner une réponse. 

En fonction du temps que la base de données met à répondre avec un message d'erreur, l'attaquant peut déduire si la commande a retourné vrai ou faux.

### Injection SQL UNION

Utilise l'opérateur UNION pour récupérer des données de plusieurs tables dans la base de données.

### Injection SQL hors bande

Relativement rare, mais se produit lorsque l'attaquant ne peut pas recevoir de réponse à sa commande dans le même canal qu'il l'a soumise. 

Au lieu de cela, elle repose sur la capacité d'un serveur à utiliser un autre protocole (comme HTTP ou DNS) pour livrer les réponses à une requête de l'attaquant.

## Comment prévenir les attaques par injection SQL

### Instructions préparées (avec requêtes paramétrées)

Les requêtes paramétrées obligent les développeurs à définir tout le code SQL et à passer chaque paramètre à la requête plus tard. Ensuite, la base de données peut distinguer entre le code et les données, indépendamment de l'entrée de l'utilisateur. 

Par exemple, si un attaquant entrait le nom `Robert'); DROP TABLE Students;--` la requête paramétrée ne serait plus vulnérable et chercherait plutôt un nom qui correspond littéralement à toute la chaîne `Robert'); DROP TABLE Students;--`. 

L'avantage des instructions préparées est que le code SQL reste dans l'application, le rendant (pour la plupart) indépendant de la base de données.

Cela peut nuire aux performances, dans de rares cas. Si c'est le cas, le développeur devra valider fortement toutes les données ou échapper à toutes les entrées fournies par l'utilisateur en utilisant une routine d'échappement spécifique à la base de données. 

### Procédures stockées

Les procédures stockées sont des instructions SQL pré-créées avec des paramètres qui n'incluent aucune génération dynamique de SQL (cela peut être fait, mais ne devrait pas l'être). Pour configurer des procédures stockées, les développeurs doivent construire des instructions SQL avec des paramètres pour toutes les entrées nécessaires.

La différence entre les procédures stockées et les instructions préparées est que les procédures stockées sont définies et stockées dans la base de données, mais appelées depuis l'application. 

De plus, comme les procédures stockées nécessitent des droits d'exécution dans certains SGBD (qui ne sont pas disponibles par défaut), il est important de créer un compte séparé avec le moins de privilèges possible plutôt que de donner un accès propriétaire.

### Validation des entrées par liste blanche

La validation des entrées par liste blanche vérifie les entrées externes par rapport à un ensemble d'entrées connues et approuvées, échouant pour toute entrée qui ne correspond pas. Cela ne doit être utilisé que dans les cas où les variables de liaison ne sont pas autorisées (les espaces réservés pour les valeurs réelles dans les instructions SQL).

La validation des entrées par liste blanche peut également être une option de secours pour détecter les entrées avant qu'elles ne soient passées à la requête.

### Échappement de toutes les entrées fournies par l'utilisateur

Vous ne devriez utiliser cette méthode que si les options précédentes ne sont pas possibles, car elle ne peut pas prévenir toutes les injections SQL. Ne l'utilisez que pour le code hérité qui ne peut pas être réécrit pour utiliser l'une des recommandations précédentes. Malheureusement, cela est une implémentation très spécifique à la base de données. 

Chaque SGBD prend en charge un schéma d'échappement de caractères. Si toutes les entrées de l'utilisateur sont échappées en utilisant le schéma correct, le SGBD pourra différencier entre l'entrée et le code SQL écrit par les développeurs.

### Moindres privilèges

Le principe des moindres privilèges n'est pas une défense contre l'injection SQL, mais une façon de limiter les dégâts qu'une attaque peut causer. 

S'assurer que les comptes d'application n'ont que les permissions dont ils ont besoin et pas plus peut être frustrant (il est définitivement plus facile de leur donner des droits DBA ou admin, mais cela offre une surface d'attaque significativement plus grande). 

Plutôt que de retirer l'accès des comptes, commencez à partir de zéro, en accordant exactement l'accès nécessaire. 

Par exemple, si un compte a besoin d'un accès en lecture seule, assurez-vous qu'il a un accès en lecture seule uniquement aux tables dont il a besoin (ou même à des portions d'une table). Si possible, évitez d'accorder un accès de création ou de suppression aux comptes de base de données. Chaque utilisateur/application devrait avoir un compte séparé.

De plus, examinez les privilèges du compte du système d'exploitation sous lequel le système de gestion de base de données (SGBD) s'exécute. Par défaut, beaucoup s'exécutent sous des comptes très puissants - changez cela pour un privilège plus approprié. 

### Sources/Lectures complémentaires :

* [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
* [PortSwigger SQL Injection](https://portswigger.net/web-security/sql-injection)
* [Netsparker SQL Injection](https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/)