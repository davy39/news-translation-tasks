---
title: Top 10 des vulnérabilités OWASP – Un guide pour les testeurs d'intrusion et
  les chasseurs de primes aux bugs
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2023-02-13T23:44:49.000Z'
originalURL: https://freecodecamp.org/news/owasp-top-10-vulnerabilities
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/image-39-1.png
tags:
- name: bug bounty
  slug: bug-bounty
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: penetration testing
  slug: penetration-testing
seo_title: Top 10 des vulnérabilités OWASP – Un guide pour les testeurs d'intrusion
  et les chasseurs de primes aux bugs
seo_desc: 'In this article, we will look at OWASP and the top 10 web application vulnerabilities
  they''ve identified. This is a useful topic for both web app pen-testers and bug
  bounty hunters.

  What do web app pen-testers and bug bounty hunters have in common? T...'
---

Dans cet article, nous allons examiner l'OWASP et les 10 principales vulnérabilités des applications web qu'ils ont identifiées. Il s'agit d'un sujet utile pour les testeurs d'intrusion d'applications web et les chasseurs de primes aux bugs.

Qu'ont en commun les testeurs d'intrusion d'applications web et les chasseurs de primes aux bugs ? Ils chassent tous deux les bugs, mais ces derniers gagnent plus d'argent ;)

La sécurité des applications web est un sujet vaste. Il existe de nombreuses façons d'exploiter une application web. Cela peut représenter un défi pour les ingénieurs en sécurité, surtout s'ils commencent leur carrière.

[OWASP](https://owasp.org/), abréviation de Open Web Application Security Project, est une organisation dédiée à l'amélioration de la sécurité des logiciels. OWASP fournit des outils et des ressources pour aider les ingénieurs en sécurité à rendre leurs applications plus sûres.

La contribution la plus importante de l'OWASP à la cybersécurité est la liste des 10 principales vulnérabilités OWASP. Cette liste contient les 10 risques de sécurité les plus critiques pour les applications web qui doivent être surveillés et prévenus.

Connaître ces 10 risques de sécurité vous aidera à réduire le risque d'attaques contre les actifs web de votre entreprise. Cela aide également les chasseurs de primes aux bugs à se faire une idée de ce qu'il faut rechercher lors de l'audit d'applications web.

Examinons chaque vulnérabilité OWASP en détail.

## Attaques par injection

![Image](https://miro.medium.com/max/1050/0*a35--5rW6hbDhqL0.png)
_Crédits : One.com_

Une injection est un type de vulnérabilité dans lequel un attaquant injecte du code malveillant dans une application web. Les injections peuvent entraîner un accès non autorisé à des données sensibles, une perte de données, ou même une compromise complète du système.

Un exemple d'attaque par injection est l'injection SQL. Cela se produit lorsqu'un attaquant injecte du code SQL malveillant dans une requête SQL d'une application web. Cela est effectué lorsque les entrées dans l'application web ne sont pas correctement vérifiées. Si l'attaque réussit, le code malveillant est exécuté par le serveur de base de données.

Un autre exemple est l'injection de commandes. Ici, un attaquant injecte des commandes shell malveillantes dans une application web. Cela peut entraîner des conséquences dévastatrices, y compris une prise de contrôle complète du système.

Pour prévenir les attaques par injection, vérifiez et nettoyez toutes les entrées utilisateur. Le nettoyage consiste à supprimer les données nuisibles ou malveillantes entrées dans la boîte d'entrée. 

Par exemple, si un utilisateur entre des caractères autres qu'une chaîne alphanumérique, vous pouvez les supprimer avant de les envoyer au backend et les vérifier à nouveau dans le backend. Cela aide à éliminer le contenu nuisible ou malveillant et protège contre les menaces de sécurité.

De plus, utilisez toujours des requêtes SQL prêtes à l'emploi dans le backend au lieu de générer des requêtes SQL à la volée. De plus, gardez tous les logiciels et bibliothèques à jour avec les derniers correctifs de sécurité.

## Surveillance et journalisation insuffisantes

![Image](https://miro.medium.com/max/1050/0*egLRXhlTvg1kMip1.png)
_Crédits : Scalyr_

La surveillance et la journalisation insuffisantes font référence à l'absence de surveillance et de journalisation appropriées pour un serveur web ou une base de données. Cela rend la détection et la réponse aux incidents de sécurité difficiles.

Par exemple, si un système ne dispose pas d'une journalisation appropriée, il sera difficile de détecter lorsqu'un attaquant tente de compromettre le système. Sans surveillance en temps réel, il sera difficile de détecter les incidents de sécurité à temps.

Pour remédier à la surveillance et à la journalisation insuffisantes, vous devez mettre en place des systèmes de surveillance robustes qui capturent un large éventail d'événements. Cela inclut la journalisation de l'accès aux données sensibles, du trafic réseau et des journaux système.

Incluez également la surveillance des appareils réseau en utilisant des services comme [Snort](https://www.snort.org/). Snort est un système gratuit et open source de détection et de prévention des intrusions réseau. De plus, examinez et analysez périodiquement les données de journalisation pour identifier les tendances et les incidents de sécurité potentiels.

## Authentification défaillante

![Image](https://miro.medium.com/max/1050/0*BpaGMLQRVcYEOlKZ.jpg)
_Crédits : SSL2BUY_

L'authentification défaillante fait référence aux faiblesses dans le processus d'authentification. Cela inclut des problèmes tels que des mots de passe faibles ou facilement devinables, l'absence de gestion appropriée des mots de passe et l'utilisation de mécanismes d'authentification vulnérables.

Par exemple, un attaquant peut exploiter un système qui permet des mots de passe faibles en devinant des mots de passe courants à partir d'une liste comme [rockyou.txt](https://github.com/praetorian-inc/Hob0Rules/blob/master/wordlists/rockyou.txt.gz). Ils peuvent également utiliser des outils de force brute comme Hydra et d'autres outils de craquage de mots de passe pour briser le chiffrement si un algorithme faible est utilisé.

Un autre exemple est l'utilisation de questions de sécurité facilement devinables, telles que « Quel est le nom de jeune fille de votre mère ? ». Un attaquant qui a fait des recherches de base sur la cible peut facilement répondre à ces questions.

Pour prévenir l'authentification défaillante, activez des mécanismes d'authentification forts, tels que l'authentification multifacteur (MFA). Appliquez des politiques de recyclage des mots de passe qui obligent les utilisateurs à changer de mots de passe périodiquement.

## Exposition de données sensibles

![Image](https://miro.medium.com/max/1050/0*JFK9HgJ9pVq6OuCn.jpg)
_Crédits : Spaceclick_

L'exposition de données sensibles fait référence au stockage et à la transmission d'informations sensibles sans sécurité appropriée. Cela inclut les mots de passe, les numéros de carte de crédit et les informations personnellement identifiables (PII).

La raison la plus courante de cela est l'absence de chiffrement. Le chiffrement est le processus de codage des informations. Ce processus convertit le texte original, connu sous le nom de texte en clair, en une forme alternative connue sous le nom de texte chiffré. Idéalement, seules les parties autorisées peuvent déchiffrer un texte chiffré en texte en clair et accéder aux informations originales.

Par exemple, si vous avez une base de données où vous stockez des mots de passe, vous devez utiliser un type de chiffrement pour protéger les mots de passe de vos clients. Si vous les stockez en texte en clair, vous mettrez vos clients en danger si vous exposez leurs mots de passe. 

Sans méthodes de protection telles que le chiffrement, l'exposition de données sensibles peut entraîner l'interception, le vol ou la manipulation des données par un attaquant. Pour atténuer ce risque, chiffrez toujours les informations sensibles lorsqu'elles sont stockées et transmises.

Stockez toujours les mots de passe chiffrés au lieu des mots de passe en texte en clair. Activez les contrôles d'accès pour garantir que seules les personnes autorisées peuvent accéder aux données sensibles.

## Entités externes XML

![Image](https://miro.medium.com/max/1050/0*2d-SrGkL8Jp3X0Uw.png)
_Crédits : Cobalt.io_

Les entités externes XML sont une vulnérabilité qui affecte les processeurs XML. Cela se produit lorsqu'ils analysent l'entrée XML d'un utilisateur sans validation appropriée.

Cette vulnérabilité permet à un attaquant d'injecter du code XML malveillant dans un document XML. Cela peut entraîner l'exposition d'informations sensibles, un déni de service, et même l'exécution de code à distance.

Pour prévenir les attaques XXE, les applications doivent valider et nettoyer l'entrée XML. Désactivez le traitement des entités externes XML et DTD par défaut.

Lorsque cela est possible, utilisez un format de données moins complexe, tel que JSON. La plupart des API sont maintenant basées sur JSON, donc ce serait un gain mutuel de passer de XML à JSON.

## **Contrôle d'accès défaillant**

![Image](https://miro.medium.com/max/1028/0*l-JKIns3xdMmDsuk.png)
_Crédits : JavatPoint_

Alors que l'authentification nous indique si un utilisateur peut accéder à un système, le contrôle d'accès nous indique qui peut accéder à une ressource spécifique dans un système.

Le contrôle d'accès défaillant se produit lorsqu'une application ne restreint pas l'accès aux ressources sensibles. Cela inclut les fichiers, les enregistrements de base de données, ou même les fonctionnalités de produit qui devraient être limitées à certains utilisateurs.

Un contrôle d'accès défaillant peut permettre à des utilisateurs non autorisés de visualiser, modifier ou supprimer des données sensibles. Pour réduire ce risque, activez des politiques de contrôle d'accès solides comme l'accès basé sur les rôles pour les utilisateurs, les administrateurs et autres.

Attribuez les droits d'accès en fonction du principe du moindre privilège. Cela signifie que les utilisateurs ne doivent avoir que le moindre accès nécessaire pour effectuer leur travail. Des audits et évaluations de sécurité réguliers aideront à identifier ces vulnérabilités de contrôle d'accès.

## Mauvaise configuration de la sécurité

![Image](https://miro.medium.com/max/1008/0*ulgvx9jVahT5CFsb.png)
_Crédits : MyF5_

La mauvaise configuration de la sécurité survient lorsqu'une application n'est pas configurée correctement. Cela entraînera l'exposition d'informations critiques, telles que les messages d'erreur ou les détails du système.

Par exemple, si vous ne changez pas les paramètres par défaut de votre backend, cela peut exposer le message d'erreur à l'utilisateur au lieu de le gérer élégamment. Vous pouvez souvent voir cela sur les sites PHP qui impriment une erreur dans le navigateur au lieu d'un message 500.

Pour réduire ce risque, masquez tous les messages de débogage et d'erreur de votre application de production. Appliquez les contrôles de sécurité et les correctifs appropriés selon les besoins, à temps. Enfin, effectuez des analyses et évaluations de sécurité régulières pour vous assurer qu'il n'y a pas de mauvaise configuration dans vos applications.

## Cross-Site Scripting (XSS)

![Image](https://miro.medium.com/max/1050/0*lV00-0_ua_8xQlUf.png)
_Crédits : Imperva_

Le Cross-Site Scripting (XSS) est un problème de sécurité courant sur les sites web. Si ce problème n'est pas traité, un attaquant peut injecter des scripts malveillants dans une page web. Ce script est ensuite exécuté par le navigateur web de la victime.

Considérez un site web qui permet aux utilisateurs de poster des commentaires. Un attaquant pourrait créer un commentaire contenant du code JavaScript malveillant et l'ajouter en tant que commentaire. Si l'entrée n'est pas nettoyée par le site web, ce code s'exécutera pour chaque utilisateur qui ouvre la page des commentaires.

Les attaques XSS peuvent voler des données telles que les détails de connexion, effectuer des actions non autorisées au nom de la victime, ou même rediriger la victime vers un site web malveillant. Pour prévenir les attaques XSS, nettoyez toujours le contenu généré par les utilisateurs et vérifiez les données d'entrée côté serveur.

## Désérialisation non sécurisée

![Image](https://miro.medium.com/max/1050/0*iJT40E_ArbQzB7qo.jpg)
_Crédits : Portswigger_

La désérialisation est le processus de conversion d'un flux d'octets en une structure de données qu'un programme peut ensuite utiliser. La désérialisation non sécurisée se produit lorsqu'une application web désérialise des données non fiables.

Par exemple, une application web peut permettre aux utilisateurs de télécharger un fichier contenant des objets Java sérialisés en tant qu'entrée. L'application web désérialise ensuite les objets et les traite.

Un attaquant peut créer un fichier malveillant qui, une fois désérialisé, exécutera un logiciel malveillant. Cela permettra à un attaquant d'effectuer divers types d'attaques, telles que l'exécution de code à distance et l'élévation de privilèges.

Pour prévenir les attaques de désérialisation non sécurisée, vérifiez toutes les entrées de l'utilisateur. Limitez la quantité de code qui s'exécute avec des privilèges élevés et assurez-vous de chiffrer toutes les données sensibles.

## Utilisation de composants avec des vulnérabilités connues

![Image](https://miro.medium.com/max/926/0*woyu85N8xKXrC6YK.png)
_Crédits : Wildnet_

Lorsque vous prévoyez d'utiliser un logiciel, vérifiez les vulnérabilités connues. Il existe de nombreuses bases de données publiques comme [exploitdb](https://www.exploit-db.com/) qui vous aideront à rechercher des problèmes avec les logiciels tiers.

Ces bases de données contiennent des vulnérabilités publiquement divulguées pour divers logiciels et applications. Ne pas le faire laissera votre application ouverte aux attaques. Un attaquant fera les recherches pour vous et utilisera ces vulnérabilités pour accéder à votre système.

Par exemple, votre application peut utiliser une bibliothèque tierce pour gérer les téléchargements de fichiers, mais cette bibliothèque peut avoir une vulnérabilité connue. Cela laissera l'application ouverte aux attaques, même si le reste de l'application est sécurisé.

Assurez-vous de faire vos recherches avant d'utiliser un logiciel tiers pour votre entreprise.

## Résumé

En résumé, le top 10 des vulnérabilités de l'OWASP est une checklist vitale. Elle nous aide à garder nos applications web et nos logiciels sécurisés. 

En tant que testeur d'intrusion ou chasseur de primes aux bugs, vous devez être conscient de ces vulnérabilités pour rester en avance sur les attaquants.

Nettoyez toujours les entrées utilisateur, employez la journalisation et faites vos recherches avant d'utiliser un logiciel tiers.

---

J'espère que vous avez trouvé cet article instructif. Vous pouvez trouver plus d'articles/vidéos sur l'IA et la cybersécurité [sur mon site web](https://www.manishmshiva.com/).