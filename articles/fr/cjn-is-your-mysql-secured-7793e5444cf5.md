---
title: Comment s'assurer que votre base de données MySQL est sécurisée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-28T20:36:56.000Z'
originalURL: https://freecodecamp.org/news/cjn-is-your-mysql-secured-7793e5444cf5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zhBThkATGUKWNUibHxFybg.png
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: Comment s'assurer que votre base de données MySQL est sécurisée
seo_desc: 'By Clark Jason Ngo

  Some basic information before we get started:

  Source: Center for Internet Security’s (CIS) Oracle MySQL Community Server 5.7

  Operating system: Windows 10

  Where to execute: command line

  mysql -u USERNAME -p

  Target application: Oracl...'
---

Par Clark Jason Ngo

#### Quelques informations de base avant de commencer :

Source : [Center for Internet Security’s (CIS) Oracle MySQL Community Server 5.7](http://www.itsecure.hu/library/image/CIS_Oracle_MySQL_Community_Server_5.7_Benchmark_v1.0.0.pdf)

**Système d'exploitation :** Windows 10

**Où exécuter :** ligne de commande

```
mysql -u NOM_UTILISATEUR -p
```

**Application cible :** Oracle MySQL Community Server 5.7

### **Audit et journalisation pour les systèmes d'information**

Les journaux jouent un rôle crucial pour la sécurité en cas de cyberattaque suspectée. Une révision manuelle des journaux est fastidieuse pour le personnel de sécurité, et ils doivent utiliser des outils de révision de journaux pour extraire des informations et les analyser. Les journaux doivent utiliser une technologie de stockage WORM (write once read many) et le chiffrement pour éviter la corruption et la perte de données de journal. De plus, les journaux doivent avoir un format standardisé pour faciliter la maintenance, l'accès et la comparaison.

#### **Assurez-vous que « log_error » n'est pas vide**

**commande :**

```sql
SHOW variables LIKE 'log_error';
```

![Image](https://cdn-media-1.freecodecamp.org/images/l3RqZv9978n6JjOZ46JpcdAjzpkwCOMZBZRZ)
_journalisation des erreurs_

Les journaux d'erreurs contiennent des données sur les événements lorsque mysqld démarre ou s'arrête. Ils montrent également lorsqu'une table doit être évaluée ou réparée. Ils doivent générer une « valeur ». La raison d'activer la journalisation des erreurs est qu'elle aide à augmenter la capacité de détecter les tentatives malveillantes contre MySQL et d'autres messages vitaux.

#### **Assurez-vous que les fichiers de journal sont stockés sur une partition non système**

**commande :**

```
SELECT @@global.log_bin_basename;
```

Les fichiers de journal de MySQL peuvent être stockés n'importe où dans le système de fichiers et définis en utilisant la configuration MySQL. De plus, il est une bonne pratique de s'assurer que les journaux dans le système de fichiers ne sont pas encombrés avec d'autres journaux tels que les journaux d'application. Vous devez vous assurer que la valeur retournée n'indique pas qu'elle se trouve dans la racine « ('/') », « /var », ou « /usr ». La raison en est que le partitionnement diminuera la probabilité de déni de service si l'espace disque disponible pour le système d'exploitation est épuisé.

![Image](https://cdn-media-1.freecodecamp.org/images/nhcvpYZlHHOOhdfs6yvaV5HcG-FDxgJpVqBK)
_**Fichiers de journal dans une partition non système**_

#### **Assurez-vous que « log_error_verbosity » n'est pas défini sur « 1 »**

**commande :**

```sql
SHOW GLOBAL VARIABLES LIKE 'log_error_verbosity';
```

Cette vérification fournit des informations supplémentaires sur les fonctionnalités que le journal MySQL a ou a activées sur les messages d'erreur. Une valeur de 1 active la journalisation des messages d'erreur. Une valeur de 2 active à la fois la journalisation des messages d'erreur et d'avertissement. Une valeur de 3 active la journalisation des messages d'erreur, d'avertissement et de note. Cela aide à détecter les comportements malveillants en journalisant les erreurs de communication et les connexions interrompues.

![Image](https://cdn-media-1.freecodecamp.org/images/iRTm8K9NxMBl1IB7NHFBauh0rrJ-u9oCgY0k)
_**Verbosité des erreurs de journal**_

#### **Assurez-vous que la journalisation d'audit est activée**

L'activation de la journalisation d'audit est cruciale pour un environnement de production pour les sessions utilisateur interactives et les sessions d'application. Avec la journalisation d'audit, elle aide à identifier qui a changé quoi et quand. Elle peut également aider à identifier ce qu'un attaquant a fait et peut même être utilisée comme preuve dans les enquêtes.

commande :

```sql
SELECT NAME FROM performance_schema.setup_instruments WHERE NAME LIKE '%/alog/%';
```

![Image](https://cdn-media-1.freecodecamp.org/images/Liy1Sl4SLwpwWpLu-NvjVreSc5MRwp3zNiP7)
_**Journal d'audit 1**_

![Image](https://cdn-media-1.freecodecamp.org/images/iG5c9r9fh9S-vrpBk37okSv21nTa33qqaKZZ)
_**Journal d'audit 2**_

![Image](https://cdn-media-1.freecodecamp.org/images/9vNTODm1dLPjcAcWykuXDrygS2i86JGSwPvC)
_**Aucun plugin de journal d'audit**_

**commande :**

```
SET GLOBAL general_log = 'ON';
```

![Image](https://cdn-media-1.freecodecamp.org/images/LL5kVryy-QDopuKWWMneeagTdkJRwO2l-mtF)
_**Requête de journal général**_

**commande :** CREATE USER 'user1'@'localhost' IDENTIFIED BY PASSWORD 'not-so-secret';

Le chemin du journal dans Windows 10 peut être trouvé en utilisant l'application Services, en vérifiant si MySQL est en cours d'exécution, et en cliquant droit sur propriétés.

Le journal dans le système de l'auteur était situé dans : C:\ProgramData\MySQL\MySQL Server 5.7\Data\DJ-JASON-CLARK.log

![Image](https://cdn-media-1.freecodecamp.org/images/cGkM1MPU2GPoQ8ja7mFWjQKY--j15UJBUezO)
_**Journal général dans le système**_

![Image](https://cdn-media-1.freecodecamp.org/images/acgtKwuMOxUL42WJQTUe5kwNawpnkS0Npf-P)
_**Processus d'audit MySQL Enterprise**_

### **Authentification pour le système d'information**

L'authentification garantit que les identifiants fournis par l'utilisateur ou la machine correspondent à la base de données des utilisateurs autorisés dans un système d'exploitation local ou dans un serveur d'authentification. L'authentification est suivie par l'autorisation, qui est accordée par un administrateur aux utilisateurs ou aux machines. Une authentification couramment utilisée dans les réseaux privés et publics est l'authentification basée sur un mot de passe.

#### **Assurez-vous que les mots de passe ne sont pas stockés dans la configuration globale**

La section [client] d'un fichier de configuration MySQL permet la création d'un utilisateur et la définition d'un mot de passe. La vérification est importante car permettre un utilisateur et un mot de passe dans le fichier de configuration impacte négativement la confidentialité du mot de passe de l'utilisateur.

Pour auditer, ouvrez le fichier de configuration MySQL et examinez la section [client] — elle ne doit pas avoir de mot de passe stocké. Aucun mot de passe n'a été défini dans le système de l'auteur (voir figure ci-dessous). Si un mot de passe a été défini dans le fichier de configuration, utilisez mysql_config_editor pour stocker les mots de passe sous forme chiffrée dans .mylogin.cnf.

![Image](https://cdn-media-1.freecodecamp.org/images/Q88ION6J2v8yvZZhOHi6W92WEeEEPYxlrSRL)
_**Section [client] du fichier de configuration MySQL**_

#### **Assurez-vous que « sql_mode » contient « NO_AUTO_CREATE_USER »**

L'option « no_auto_create_user » permet d'empêcher la création automatique d'un utilisateur lorsque les informations d'authentification ne sont pas fournies.

**commande :**

```
SELECT @@global.sql_mode;
```

![Image](https://cdn-media-1.freecodecamp.org/images/04EKee02Rr3Irs1pSUzonmRF-NtDcpX8Samq)
_**Pas de création automatique d'utilisateur dans global**_

**commande :**

```sql
SELECT @@session.sql_mode;
```

![Image](https://cdn-media-1.freecodecamp.org/images/joKBhVTvSWObegwcx4rysRngCVzRu12-PacM)
_**Pas de création automatique d'utilisateur dans session**_

#### **Assurez-vous que des mots de passe sont définis pour tous les comptes MySQL**

Un utilisateur peut créer un mot de passe vide. Avoir un mot de passe vide est risqué car n'importe qui peut simplement usurper l'identité de l'utilisateur, entrer l'ID de connexion de l'utilisateur et se connecter au serveur. Cela contourne l'authentification, ce qui est mauvais.

**commande :**

```sql
SELECT User,host FROM mysql.user WHERE authentication_string='';
```

![Image](https://cdn-media-1.freecodecamp.org/images/ZpvRueSkB-NE2pSDpDhJe0ypEFwGCxofYfg1)
_**Utilisateurs avec des mots de passe vides**_

#### **Assurez-vous que « default_password_lifetime » est inférieur ou égal à « 90 »**

Changer la durée de vie du mot de passe à 90 jours diminue le temps disponible pour un attaquant pour compromettre le mot de passe, et ainsi diminue la probabilité de se faire attaquer.

**commande :**

```sql
SHOW VARIABLES LIKE 'default_password_lifetime';
```

![Image](https://cdn-media-1.freecodecamp.org/images/CJO2VduUgpaCDsqUwf4-J7BhVeNJERQhrFLu)
_**Durée de vie du mot de passe par défaut avec une valeur de 0**_

**commande :**

```
SET GLOBAL default_password_lifetime=90;
```

![Image](https://cdn-media-1.freecodecamp.org/images/OnRfHJLsHIqyo9FVYPtYH-8tLowjEeBhaiko)
_**Définir la durée de vie du mot de passe par défaut à 90**_

#### **Assurez-vous que la complexité du mot de passe est en place**

La complexité du mot de passe ajoute une force de sécurité aux authentifications et inclut l'ajout ou l'augmentation de la longueur, de la casse, des nombres et des caractères spéciaux. Plus le mot de passe est complexe, plus il est difficile pour les attaquants d'utiliser la force brute pour obtenir le mot de passe. Les mots de passe faibles sont facilement obtenus dans un dictionnaire de mots de passe.

**commande :**

```
SHOW VARIABLES LIKE 'validate_password%';
```

![Image](https://cdn-media-1.freecodecamp.org/images/x25sxKvZfaRQPK4ZmcfroMLHSRwIr4MqEV9J)
_**Vérifier la complexité du mot de passe**_

![Image](https://cdn-media-1.freecodecamp.org/images/YRlXHe0O0kFZDla6r0lCPv0krGHw8OIg5fKi)
_**Implémenter la complexité du mot de passe**_

#### **Assurez-vous qu'aucun utilisateur n'a de noms d'hôte génériques**

Les utilisateurs avec des noms d'hôte génériques (%) se voient accorder la permission à n'importe quel emplacement. Il est préférable d'éviter de créer des noms d'hôte génériques. Au lieu de cela, créez des utilisateurs et donnez-leur des emplacements spécifiques à partir desquels un utilisateur donné peut se connecter et interagir avec la base de données.

**commande :**

```
SELECT user, host FROM mysql.user WHERE host = '%';
```

![Image](https://cdn-media-1.freecodecamp.org/images/vPYOo8ZvwxKBGIxAI3ghiCSv7taKUF9wtRng)
_**Nom d'hôte générique**_

![Image](https://cdn-media-1.freecodecamp.org/images/VYixR1Z4ccQn3mhyIojKjVFPi5PF-fHvb8Ka)
_**Changer le nom d'hôte générique**_

#### **Assurez-vous qu'aucun compte anonyme n'existe**

Les utilisateurs peuvent avoir un nom d'utilisateur anonyme (vide ou blanc). Ces noms d'utilisateur anonymes n'ont pas de mots de passe et n'importe quel autre utilisateur peut utiliser ce nom d'utilisateur anonyme pour se connecter au serveur MySQL. La suppression de ces comptes anonymes garantit que seuls les utilisateurs identifiés et de confiance peuvent accéder au serveur MySQL.

**commande :**

```
SELECT user,host FROM mysql.user WHERE user = '';
```

![Image](https://cdn-media-1.freecodecamp.org/images/yCiBhUnSoYw8hiTde0V7fSimGjVyjMjetWLW)
_**Aucun compte anonyme**_

### **Connexion réseau au serveur MySQL**

La connexion réseau joue un rôle important pour la communication entre l'utilisateur et le serveur MySQL. Les connexions réseau non sécurisées sont très vulnérables aux attaques. Voici les vérifications pour la sécurité des connexions réseau.

#### **Assurez-vous que « have_ssl » est défini sur « YES »**

Pour éviter que des attaquants malveillants ne regardent à l'intérieur de votre système, il est préférable d'utiliser SSL/TLS pour tout le trafic réseau lors de l'utilisation de réseaux non fiables.

**commande :**

```
WHERE variable_name = 'have_ssl';
```

![Image](https://cdn-media-1.freecodecamp.org/images/ut3VeJpXP6eYKjT2al0QaVZYurNRXqhBSgbE)
_**Pas de SSL**_

#### **Assurez-vous que « ssl_type » est défini sur « ANY », « X509 », ou « SPECIFIED » pour tous les utilisateurs distants**

SSL/TLS doit être configuré par utilisateur. Cela empêche davantage l'écoute indiscrète des attaquants malveillants.

**commande :**

```sql
SELECT user, host, ssl_type FROM mysql.user WHERE NOT HOST IN ('::1', '127.0.0.1', 'localhost');
```

![Image](https://cdn-media-1.freecodecamp.org/images/4lluCsRhf5Kgz4AUpGPWiDb7pZYv6Tnt5W3i)
_**Pas de ssl_type**_

### **Réplication**

La vérification de l'état de la réplication vous permet de surveiller les performances et les vulnérabilités de sécurité. Microsoft SQL Server Management Studio dispose des outils suivants pour surveiller la réplication :

1. voir l'état de l'agent de capture instantanée,
2. voir l'état de l'agent de lecture de journal, et
3. voir l'état de synchronisation.

#### **Assurez-vous que le trafic de réplication est sécurisé**

Le trafic de réplication entre les serveurs doit être sécurisé. Lors des transferts de réplication, des mots de passe pourraient fuir.

Pour auditer, vérifiez s'ils utilisent : un réseau privé, un VPN, SSL/TLS ou un tunnel SSH. Espérons que le système de l'auteur utilise un réseau privé. Corrigé si ce n'est pas le cas, et sécurisé en utilisant le réseau privé, un VPN, SSL/TLS ou un tunnel SSH.

![Image](https://cdn-media-1.freecodecamp.org/images/0RM3gzfomxLEWKzwnf1C-KynDJNAqhfXPaKX)
_**Réseau privé**_

#### **Assurez-vous que « MASTER_SSL_VERIFY_SERVER_CERT » est défini sur « YES » ou « 1 »**

« MASTER_SSL_VERIFY_SERVER_CERT » vérifie si la réplique doit vérifier le certificat du primaire ou non. La réplique doit vérifier le certificat du primaire pour authentifier le primaire avant de continuer la connexion.

**commande :**

```sql
SELECT ssl_verify_server_cert FROM mysql.slave_master_info;
```

![Image](https://cdn-media-1.freecodecamp.org/images/4WAxSQDlSx-jC43Z5nFCbnYLkfaxyH-6hkcm)
_**Pas de SSL pour la vérification réplique-primaire**_

#### **Assurez-vous que « master_info_repository » est défini sur « TABLE »**

« master_info_repository » détermine où la réplique journalise l'état du primaire et les informations de connexion. Le mot de passe est stocké dans le référentiel d'informations du primaire qui est un fichier texte en clair. Stocker le mot de passe dans la TABLE master_info est plus sûr.

**commande :**

```
SHOW GLOBAL VARIABLES LIKE 'master_info_repository';
```

![Image](https://cdn-media-1.freecodecamp.org/images/n-74-mT9wp5NnY6ROI-oij9BJ05F5ElPOLPR)
_**Valeur du référentiel d'informations du primaire**_

#### **Assurez-vous que « super_priv » n'est pas défini sur « Y » pour les utilisateurs de réplication**

Le privilège « SUPER » (« super_priv ») situé dans la table « mysql.user » a des fonctions comme « CHANGE », « MASTER TO », « KILL », « mysqladmin kill », « PURGE BINARY LOGS », « SET GLOBAL », « mysqladmin debug », et d'autres contrôles de journalisation. Donner à un utilisateur le privilège « SUPER » permet à l'utilisateur de voir et de terminer les instructions SQL en cours d'exécution, même pour la gestion des mots de passe. Si l'attaquant exploite et obtient le privilège « SUPER », il peut désactiver, modifier ou détruire les données de journalisation.

**commande :**

```sql
SELECT user, host FROM mysql.user WHERE user='repl' and Super_priv = 'Y';
```

![Image](https://cdn-media-1.freecodecamp.org/images/vy8xJdaYwOOAzIWyvrVaRm27JL4h9KqPIuzM)
_**Vérification de la réplication pour les utilisateurs avec le privilège SUPER**_

#### **Assurez-vous qu'aucun utilisateur de réplication n'a de noms d'hôte génériques**

MySQL vous permet d'accorder des permissions à des noms d'hôte génériques. Les noms d'hôte génériques doivent être évités, et vous devez créer ou modifier des utilisateurs et leur donner des emplacements spécifiques à partir desquels un utilisateur donné peut se connecter et interagir avec la base de données.

![Image](https://cdn-media-1.freecodecamp.org/images/7XVbzJBQYHEr8pVq41eL0QmJZvM-27aQfSXe)
_**Vérification de la réplication pour les noms d'hôte génériques**_

### **Conclusion**

Les vérifications suivantes sont effectuées pour un environnement de travail unique utilisant MySQL comme système d'information à la fois du côté application et du côté utilisateur.

L'évaluation est impérative pour vérifier la journalisation standard de MySQL et activer des fonctions de journalisation supplémentaires (cela permet également de vérifier les vulnérabilités d'authentification). Les vérifications réseau sont importantes pour empêcher d'autres utilisateurs avec des intentions malveillantes de regarder dans votre réseau. Implémentez toujours SSL/TLS pour chiffrer. Sécuriser le transfert unidirectionnel est nécessaire. Sécuriser le trafic de réplication ajoute une couche défensive.

Le résultat de l'évaluation peut vous informer si le système est capable de fonctionner à un niveau de confiance.

Merci d'avoir lu mon blog ! Vous avez maintenant commencé le chemin pour sécuriser votre base de données MySQL. 😊