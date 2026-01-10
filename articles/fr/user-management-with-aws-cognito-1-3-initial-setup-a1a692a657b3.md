---
title: Gestion des utilisateurs avec AWS Cognito — (1/3) Installation initiale
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-02T18:29:34.000Z'
originalURL: https://freecodecamp.org/news/user-management-with-aws-cognito-1-3-initial-setup-a1a692a657b3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ubdzj9K3MrbMb0Ep0UV3IA.png
tags:
- name: AWS
  slug: aws
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Gestion des utilisateurs avec AWS Cognito — (1/3) Installation initiale
seo_desc: 'By Kangze Huang

  The Complete AWS Web Boilerplate — Tutorial 1A



  Main Table of Contents Click Here

  Part A: Initial Setup

  Part B: The Core Functionality

  Part C: Last Steps to Full Fledged


  Download the Github here.

  Introduction

  Setting up user authent...'
---

Par Kangze Huang

#### Le modèle AWS Web complet — Tutoriel 1A

![Image](https://cdn-media-1.freecodecamp.org/images/e1CBg1j1AJmx1aoLC5kX0KWTfCpBhk2evIa9)

> [**Table des matières principale Cliquez ici**](https://medium.com/@kangzeroo/the-complete-aws-web-boilerplate-d0ca89d1691f#.uw0npcszi)

> **Partie A :** [Installation initiale](https://medium.com/@kangzeroo/user-management-with-aws-cognito-1-3-initial-setup-a1a692a657b3#.pgxyg8q8o)

> **Partie B :** [Fonctionnalités principales](https://medium.com/@kangzeroo/user-management-with-aws-cognito-2-3-the-core-functionality-ec15849618a4)

> **Partie C :** [Dernières étapes pour une solution complète](https://medium.com/@kangzeroo/user-management-with-aws-cognito-3-3-last-steps-to-full-fledged-73f4a3a9f05e#.v3mg316u5)

Téléchargez le Github [ici](https://github.com/kangzeroo/Kangzeroos-AWS-Cognito-Boilerplate).

### Introduction

La configuration de l'authentification des utilisateurs peut prendre des âges, mais c'est une pierre angulaire essentielle de toute application de production. Il existe des options telles que AuthO et PassportJS, mais elles ont soit des courbes d'apprentissage difficiles, nécessitent une maintenance continue, ou sont vulnérables aux erreurs de programmation car elles nécessitent une configuration manuelle. Si seulement il existait un service de gestion des utilisateurs personnalisable, sécurisé et hautement évolutif sur le cloud.

Présentation d'Amazon Cognito et des identités fédérées. Cognito est la solution AWS pour gérer les profils utilisateurs, et les identités fédérées aident à suivre vos utilisateurs sur plusieurs connexions. Intégrés à l'écosystème AWS, AWS Cognito ouvre un monde de possibilités pour le développement avancé de l'interface utilisateur, car Cognito + les rôles IAM vous donnent un accès sécurisé sélectif à d'autres services AWS. Vous voulez permettre l'accès au bucket S3 uniquement à des utilisateurs spécifiques connectés ? Il suffit de connecter une connexion Cognito avec un rôle IAM autorisé à accéder au bucket, et maintenant votre bucket est sécurisé ! Le meilleur de tout, le niveau gratuit vous donne 50 000 utilisateurs actifs mensuels, vous n'aurez donc pas à vous soucier de payer plus jusqu'à ce que vous soyez prêt à exploser.

Ce modèle est une application web React-Redux qui intègre toutes les fonctionnalités d'AWS Cognito et des identités fédérées. Utilisez ce modèle si vous avez une application que vous souhaitez développer avec un service d'authentification prêt pour la production dès le début. En effet, c'est une rampe de lancement puissante pour votre prochaine grande idée.

Allez sur AWS Cognito dans la console AWS pour commencer !

![Image](https://cdn-media-1.freecodecamp.org/images/L-eUlNJZNfWnJdq5Fpiv6KZ1GXgyJrl871Zd)

### Installation initiale — Cognito

![Image](https://cdn-media-1.freecodecamp.org/images/tkMhJH8RcXnUWHfhkoJdvMzJxm4Y2JKsPUaQ)

Nous allons configurer AWS Cognito, qui est un pool de connexion personnalisé (comme la connexion avec un email). Cognito N'EST PAS un gestionnaire de connexion pour tout type de connexion (comme Facebook et Gmail), uniquement pour les connexions personnalisées.

Commençons par créer un pool d'utilisateurs en cliquant sur « Gérer vos pools d'utilisateurs ». Un pool d'utilisateurs est un groupe d'utilisateurs qui remplissent la même désignation. Si vous créiez un clone d'Uber, vous créeriez 2 pools d'utilisateurs — un pour les conducteurs et un pour les passagers. Pour l'instant, créons simplement 1 nouveau pool d'utilisateurs appelé « App_Users ». L'écran de configuration devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/SfXQUIUYNXLW0RUY8iwP4ZBic6Jrb6yIz24s)
_Nom du pool d'utilisateurs_

Nous allons passer par ce processus étape par étape, alors entrez le nom du pool « App_Users » et cliquez sur « Parcourir les paramètres ». L'étape suivante est « Attributs », où nous définissons les attributs que nos « App_Users » auront.

![Image](https://cdn-media-1.freecodecamp.org/images/O7QhmNjg9m9RpNwLUz2hjfbzv9sxolLuP7n4)
_Attributs des utilisateurs_

Maintenant, nous voulons seulement avoir un email, un mot de passe et un « agentName ». L'email est notre identifiant unique pour un utilisateur et le mot de passe est un champ obligatoire (c'est pourquoi vous ne le voyez pas dans la liste des attributs standard). Nous voulons que les utilisateurs puissent avoir un pseudonyme, alors configurons « agentName » comme un attribut personnalisé. Nous utilisons seulement « agentName » pour montrer comment ajouter des attributs personnalisés. Faites défiler vers le bas et vous verrez l'option pour ajouter des attributs personnalisés.

![Image](https://cdn-media-1.freecodecamp.org/images/Scp0n-wf0VsNHQQ03J1xo0tXPwRDJ8CwFu6a)
_Attributs personnalisés_

À la date de rédaction de ce tutoriel, vous ne pouvez pas revenir en arrière et changer les attributs personnalisés (même si AWS semble pouvoir le faire), alors assurez-vous de bien faire cela du premier coup ! Si vous devez changer des attributs, vous devrez créer un nouveau pool d'utilisateurs. Espérons qu'AWS corrige ce problème bientôt. En tout cas, passons aux politiques de compte !

![Image](https://cdn-media-1.freecodecamp.org/images/EzZmDaVOQKLsGxqQb-TF6KfNNG43y7GeDtPo)
_Politiques de compte_

Nous pouvons voir ici que nos mots de passe peuvent être renforcés pour nécessiter certains caractères. Évidemment, exiger un mélange de divers types de caractères serait plus sécurisé, mais les utilisateurs n'aiment souvent pas cela. Pour un compromis, exigeons simplement que le mot de passe soit de 8+ caractères de long, et inclue au moins 1 nombre. Nous voulons également que les utilisateurs puissent s'inscrire eux-mêmes. Les autres parties ne sont pas si importantes, alors passons à l'étape suivante : vérifications.

![Image](https://cdn-media-1.freecodecamp.org/images/ZSesvPppQzQtylalxAt8kYO3ptalae1VCJa1)
_Vérifications de compte_

Cette partie est cool, nous pouvons facilement intégrer l'authentification multifacteur (MFA). Cela signifie que les utilisateurs doivent s'inscrire avec un email ainsi qu'une autre forme d'authentification comme un numéro de téléphone. Un code PIN serait envoyé à ce numéro de téléphone et l'utilisateur l'utiliserait pour vérifier son compte. Nous n'utiliserons pas la MFA dans ce tutoriel, seulement la vérification par email. Réglez la MFA sur « off » et cochez seulement « Email » comme méthode de vérification. Nous pouvons laisser le « AppUsers-SMS-Role » (rôle IAM) qui a été rempli, car nous ne l'utiliserons pas mais pourrions l'utiliser à l'avenir. Cognito utilise ce rôle IAM pour être autorisé à envoyer des messages SMS utilisés dans la MFA. Puisque nous n'utilisons pas la MFA, nous pouvons passer à : Personnalisations de messages.

![Image](https://cdn-media-1.freecodecamp.org/images/7GSg9dIVav372e4QPuRJ9bXcTfmIGruwibQz)
_Messages de compte personnalisés_

Lorsque les utilisateurs reçoivent leurs emails de vérification de compte, nous pouvons spécifier ce qui va dans cet email. Ici, nous avons créé un email personnalisé et placé programmatiquement le code PIN de vérification représenté par `{####}`. Malheureusement, nous ne pouvons pas passer d'autres variables comme un lien de vérification. Pour y parvenir, nous devrions utiliser une combinaison de AWS Lambda et AWS SES.

![Image](https://cdn-media-1.freecodecamp.org/images/z-bUgpq6-KqndouSQACi5OpsRb8EpV3KSFcD)
_Messages de compte personnalisés_

Faites défiler la page dans l'étape de personnalisation des messages et nous pouvons ajouter nos propres adresses FROM et REPLY-TO par défaut. Pour ce faire, nous devons vérifier un email dans AWS SES, ce qui est facile et super rapide à configurer. Dans un nouvel onglet, allez à la page d'accueil de la console AWS en cliquant sur le cube orange en haut à gauche. Dans la page d'accueil de la console, recherchez SES (Simple Email Service). Cliquez pour aller à la page SES, puis cliquez sur le lien Adresses email dans le menu de gauche.

![Image](https://cdn-media-1.freecodecamp.org/images/A5RdmoIRfu75F4pAlnHf0uykAvpwE3wkpSk0)

Ensuite, cliquez sur « Vérifier une nouvelle adresse », et entrez l'email que vous souhaitez vérifier.

![Image](https://cdn-media-1.freecodecamp.org/images/QDUaZrmT73RnSATgkl8onbn8ln21LJWvLe3j)

Maintenant, connectez-vous à votre email et ouvrez l'email d'AWS. Cliquez sur le lien dans l'email pour vérifier, et vous serez redirigé vers la page AWS SES à nouveau. Vous avez vérifié un email avec succès ! C'était facile.

Maintenant que c'est fait, retournons à AWS Cognito et passons à : Tags.

![Image](https://cdn-media-1.freecodecamp.org/images/3--4yXNLjHuDWWdAP5ELZwePidQoZeloH4Hq)
_Tags du pool d'utilisateurs_

Il n'est pas obligatoire d'ajouter des tags à un pool d'utilisateurs, mais c'est définitivement utile pour gérer de nombreux services AWS. Ajoutons simplement un tag pour 'AppName' et définissons-le à une valeur de 'MyApp'. Nous pouvons maintenant passer à : Appareils.

![Image](https://cdn-media-1.freecodecamp.org/images/wJYvzItugAwEyXSY9cXI9NAhKcDfut4rPEK1)
_Appareils_

Nous pouvons choisir de mémoriser les appareils de nos utilisateurs. Je sélectionne généralement « Toujours » car mémoriser les appareils des utilisateurs est à la fois gratuit et ne nécessite aucun codage de notre part. Les informations sont utiles aussi, alors pourquoi pas ? Étape suivante : Apps.

![Image](https://cdn-media-1.freecodecamp.org/images/2UfKm3CYYbsQa6QdKvGPwPILUvk4j1h7io0a)
_Apps_

Nous voulons que certaines applications aient accès à notre pool d'utilisateurs. Ces applications ne sont présentes nulle part ailleurs dans l'écosystème AWS, ce qui signifie que lorsque nous créons une « app », c'est un identifiant Cognito uniquement. Les applications sont utiles car nous pouvons avoir plusieurs applications accédant au même pool d'utilisateurs (imaginez une application clone d'Uber, et une application complémentaire de pratique de test de conduite). Nous allons définir le jeton de rafraîchissement à 30 jours, ce qui signifie que chaque tentative de connexion retournera un jeton de rafraîchissement que nous pouvons utiliser pour l'authentification au lieu de nous connecter à chaque fois. Nous décochons « Générer le secret client » car nous avons l'intention de nous connecter à notre pool d'utilisateurs depuis le front-end au lieu du back-end (donc, nous ne pouvons pas garder de secrets sur le front-end car ce n'est pas sécurisé). Cliquez sur « Créer une application » puis sur « Étape suivante » pour passer à : Déclencheurs.

![Image](https://cdn-media-1.freecodecamp.org/images/3Z8IPzD9uRGcLI3aATFoAqgCoSHK3lY4hQiT)
_Déclencheurs_

Nous pouvons déclencher diverses actions dans le flux d'authentification et de configuration des utilisateurs. Vous vous souvenez comment nous avons dit que nous pouvons créer des emails de vérification de compte plus complexes en utilisant AWS Lambda et AWS SES ? C'est ici que nous le configurerions. Pour le cadre de ce tutoriel, nous n'utiliserons aucun déclencheur AWS Lambda. Passons à l'étape finale : Révision.

![Image](https://cdn-media-1.freecodecamp.org/images/jlPgyxBt0tMrpuc0jldofVdeSypisGWCocDI)
_Révision_

Ici, nous passons en revue toutes les configurations de configuration que nous avons faites. Si vous êtes sûr de ces informations, cliquez sur « Créer le pool » et notre pool d'utilisateurs Cognito sera généré !

Prenez note de l'ID du pool `us-east-1_6i5p2Fwao` dans l'onglet Détails du pool.

![Image](https://cdn-media-1.freecodecamp.org/images/QqbMbVl7GvHh083UvY39YXbkeTYqv0D0biOp)
_Remarquez l'ID du pool_

Et l'ID du client de l'application `5jr0qvudipsikhk2n1ltcq684b` dans l'onglet Apps. Nous aurons besoin de ces deux éléments dans notre application côté client.

![Image](https://cdn-media-1.freecodecamp.org/images/-8p3fPT8mAl-wVuEFRAjztUKA18j6QPe0mrv)
_Remarquez l'ID du client de l'application_

Maintenant que Cognito est configuré, nous pouvons configurer les identités fédérées pour plusieurs fournisseurs de connexion. Dans ce tutoriel, nous ne couvrons pas les spécificités de la connexion FB car cela ne fait pas partie du cadre de cette série de tutoriels. Cependant, l'intégration de la connexion FB est super facile et nous montrerons comment cela se fait dans la section ci-dessous.

### Installation initiale — Identités fédérées

![Image](https://cdn-media-1.freecodecamp.org/images/90IsJWecVCVPebDqABxVaAxqJ81CbSN80qwd)

Ensuite, nous voulons configurer les « Identités fédérées ». Si nous avons une application qui permet à plusieurs fournisseurs de connexion (Amazon Cognito, Facebook, Gmail, etc.) pour le même utilisateur, nous utiliserions les identités fédérées pour centraliser toutes ces connexions. Dans ce tutoriel, nous utiliserons à la fois notre connexion Amazon Cognito, ainsi qu'une potentielle connexion Facebook. Allez à Identités fédérées et commencez le processus pour créer un nouveau pool d'identités. Donnez-lui un nom approprié.

![Image](https://cdn-media-1.freecodecamp.org/images/Z4DaYZSFEvuzVONWBSu7zNIJrEcvFY3hjFFJ)

Maintenant, développez la section « Fournisseurs d'authentification » et vous verrez l'écran ci-dessous. Sous Cognito, nous allons ajouter le pool d'utilisateurs Cognito que nous venons de créer. Copiez et collez l'ID du pool d'utilisateurs et l'ID du client de l'application que nous avons notés précédemment.

![Image](https://cdn-media-1.freecodecamp.org/images/2aWx2T6c3Ek3SdCLvsUqiNhkusJSTUJGu0hc)

Et si nous voulions la connexion Facebook pour le même pool d'identités utilisateur, nous pouvons aller à l'onglet Facebook et simplement entrer notre ID d'application Facebook. C'est tout ce qu'il y a à faire sur la console AWS !

![Image](https://cdn-media-1.freecodecamp.org/images/SspjVsav0UYlQCQEwAh0Y7vWbJQrGIET4Rm8)

Enregistrez le pool d'identités et vous serez redirigé vers l'écran ci-dessous où les rôles IAM sont créés pour représenter le pool d'identités fédérées. Le rôle IAM non authentifié est pour les utilisateurs non connectés, et la version authentifiée est pour les utilisateurs connectés. Nous pouvons accorder à ces rôles IAM la permission d'accéder à d'autres ressources AWS comme les buckets S3 et autres. C'est ainsi que nous obtenons une sécurité accrue en intégrant notre application dans tout l'écosystème AWS. Continuez à terminer la création de ce pool d'identités.

![Image](https://cdn-media-1.freecodecamp.org/images/QF9nJpmbHzNiblaOlNxJ7N6FxJqvI0EeInIS)

Vous devriez maintenant voir l'écran ci-dessous après avoir créé avec succès le pool d'identités. Vous n'avez besoin de noter qu'une seule chose, qui est l'ID du pool d'identités (par exemple, `us-east-1:65bd1e7d-546c-4f8c-b1bc-9e3e571cfaa7`) que nous utiliserons plus tard dans notre code. Super !

![Image](https://cdn-media-1.freecodecamp.org/images/2ZmhE7019DoVa-o4efQtPW7UeGeLVuWQZ2SI)

Quittez tout et retournez à l'écran principal d'AWS Cognito. Si nous entrons dans la section Cognito ou la section Identités fédérées, nous voyons que nous avons les 2 pools nécessaires configurés. AWS Cognito et AWS Federated Identities sont prêts à l'emploi !

![Image](https://cdn-media-1.freecodecamp.org/images/FI4-abtFRmp4r9eszvErYlUSlAgFZyTBuPBy)
_AWS Cognito_

![Image](https://cdn-media-1.freecodecamp.org/images/9OogLw3GvEXUarO55p4KaILnCl27aF52fYMw)
_AWS Identités fédérées_

C'est tout pour la configuration ! Avec ces 2 pools, nous pouvons intégrer le reste de notre code dans le service d'authentification complet d'Amazon et atteindre une gestion des utilisateurs de premier ordre. C'était bien plus facile que le OAuth personnalisé + Passport.js ! Si vous aimez ce que vous avez vu jusqu'à présent, continuez à lire ! N'oubliez pas qu'une fois que vous aurez appris cela, ce sera super facile à l'avenir, donc cela vaut définitivement l'investissement en temps. À la prochaine section !

> [**Table des matières principale Cliquez ici**](https://medium.com/@kangzeroo/the-complete-aws-web-boilerplate-d0ca89d1691f#.uw0npcszi)

> **Partie A :** [Installation initiale](https://medium.com/@kangzeroo/user-management-with-aws-cognito-1-3-initial-setup-a1a692a657b3#.pgxyg8q8o)

> **Partie B :** [Fonctionnalités principales](https://medium.com/@kangzeroo/user-management-with-aws-cognito-2-3-the-core-functionality-ec15849618a4)

> **Partie C :** [Dernières étapes pour une solution complète](https://medium.com/@kangzeroo/user-management-with-aws-cognito-3-3-last-steps-to-full-fledged-73f4a3a9f05e#.v3mg316u5)

> Ces méthodes ont été partiellement utilisées dans le déploiement de [renthero.ca](http://renthero.ca)