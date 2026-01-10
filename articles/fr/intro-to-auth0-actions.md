---
title: Comment étendre votre flux de connexion avec les Actions Auth0
subtitle: ''
author: Rohit Jacob Mathew
co_authors: []
series: null
date: '2021-12-22T15:46:00.000Z'
originalURL: https://freecodecamp.org/news/intro-to-auth0-actions
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/rohit-code-idk-2400-x-1260.jpg
tags:
- name: Auth0
  slug: auth0
- name: authentication
  slug: authentication
seo_title: Comment étendre votre flux de connexion avec les Actions Auth0
seo_desc: "I recently attended a training session with the Auth0 Dev Rel team to learn\
  \ about a cool new feature called Auth0 Actions. \nIn this article, I am going to\
  \ explain what Auth0 Actions are, why you'd want to use them, and how to set one\
  \ up.\nWhat are Aut..."
---

J'ai récemment participé à une session de formation avec l'équipe Dev Rel d'Auth0 pour en savoir plus sur une nouvelle fonctionnalité appelée Auth0 Actions. 

Dans cet article, je vais expliquer ce que sont les Actions Auth0, pourquoi vous voudriez les utiliser et comment en configurer une.

## Qu'est-ce que les Actions Auth0 ?

Les Actions sont des fonctions sécurisées, spécifiques au locataire, versionnées et écrites en Node.js qui s'exécutent à certains points pendant l'exécution d'Auth0. Les Actions sont utilisées pour personnaliser et étendre les capacités d'Auth0 avec une logique personnalisée.

!["Exemple de flux d'Actions"](https://cdn.hashnode.com/res/hashnode/image/upload/v1639214635781/VFyOmuqRg.png)

Ci-dessus, vous pouvez voir un exemple de flux. Dans celui-ci, une fois que l'utilisateur se connecte au système, vous ajoutez un déclencheur pour vérifier l'identité de l'utilisateur en utilisant Onfido, puis vous confirmez le consentement en utilisant OneTrust avant de terminer le flux de connexion et d'émettre le jeton.

En bref, une action est un moyen programmatique d'ajouter une logique métier personnalisée à votre flux de connexion.

## Pourquoi utiliser les Actions Auth0 ? 💡

**Extensibilité** – elles sont conçues pour donner aux développeurs plus d'outils et une meilleure expérience dans leurs flux de travail de connexion.

**Fonctionnalité Glisser-Déposer** – L'éditeur de flux vous permet de construire visuellement des flux de travail personnalisés avec des blocs d'Actions glisser-déposer pour un contrôle complet.

**Éditeur de Code Monaco** – Conçu pour les développeurs, vous pouvez facilement écrire des fonctions JavaScript avec validation, complétion intelligente du code et définitions de types avec support TypeScript.

**Environnement Serverless** – Auth0 héberge vos fonctions d'Action personnalisées et les traite lorsque vous le souhaitez. Les fonctions sont stockées et exécutées sur leur infrastructure.

**Contrôle de Version** – Vous avez la possibilité de stocker un historique des modifications individuelles des Actions et la possibilité de revenir à des versions précédentes si nécessaire.

**Tests Pré-Production** – Vos Actions personnelles peuvent être rédigées, examinées et testées avant d'être déployées en production.

## Comment Configurer les Actions Auth0

Pour les besoins de cette démonstration, nous allons créer une action pour imposer l'Authentification Multi-Facteurs (MFA) pour un rôle spécifique. Je vais vous guider à travers le processus de :

1. Création d'un rôle
2. Ajout d'utilisateurs
3. Configuration d'une application de démonstration
4. Création d'une Action pour imposer la MFA
5. Test du code

Commençons :

### 1) Connectez-vous à Votre Compte Auth0

La première étape pour sécuriser votre application est d'accéder au tableau de bord Auth0 afin de créer votre application Auth0. 

Si vous n'avez pas encore créé de compte Auth0, vous pouvez [vous inscrire pour un compte gratuit maintenant](https://a0.to/signup-for-auth0).

### 2) Créez une Application

Une fois dans le tableau de bord, allez dans l'onglet Applications dans la barre latérale de gauche.

![Page Application](https://cdn.hashnode.com/res/hashnode/image/upload/v1639214927748/WpImjm7mg.png)

Cliquez sur Créer une Application.

Donnez un nom convivial à votre application (comme Test Actions App) et choisissez Applications Web à Page Unique comme type d'application.

![Page de Création d'Application](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215005392/uhXHjQpPZ.png)

Dans l'onglet démarrage rapide, choisissez React. Téléchargez l'application exemple. Cela aura déjà en place la plupart des détails nécessaires.

![Exemple de Démarrage Rapide](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215038833/KmbmIA1nt.png)

Nous devons également configurer quelques paramètres pour cette application. Choisissez l'onglet Paramètres (à côté de démarrage rapide). Ajoutez votre URL localhost aux endroits suivants :

1. URLs de Rappel Autorisées
2. URLs de Déconnexion Autorisées
3. Origines Web Autorisées

![Mettre à Jour les Paramètres de l'Application](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215091880/cwD9fJnFd.png)

### 3) Configuration de l'Application

Décompressez le code que nous avons téléchargé à un endroit de votre choix. Ensuite, ouvrez-le dans l'éditeur de code de votre choix.

Vérifiez que les détails de votre application sont correctement configurés dans `src/auth_config.json`.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-16-at-7.56.39-PM.png)

Nous allons exécuter ce code localement, alors installez les dépendances et exécutez-le en mode dev (pour avoir le rechargement à chaud activé). Pour ce faire, `npm install & npm run dev`.

Une fois l'application démarrée, vous devriez voir une SPA comme ci-dessous. Si vous cliquez sur Se Connecter, vous serez redirigé vers votre boîte de connexion.

![Application Exemple](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215261508/-E672eefw.png)

### 4) Configuration des Utilisateurs et des Rôles

Cliquez sur l'onglet Gestion des Utilisateurs dans la barre latérale de gauche.

Allez dans l'onglet Utilisateurs et cliquez sur le bouton Créer un Utilisateur. Nous devons créer 2 utilisateurs :

1. Utilisateur Admin
2. Utilisateur Test

Rappelez-vous ces identifiants car ce sont les utilisateurs de test que nous utiliserons pour cette démonstration.

![Création d'Utilisateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215392817/I51zfr-Ov.png)

Allez dans l'onglet Rôles et cliquez sur le bouton Créer un Rôle. Appelez le rôle `Admin` et, une fois créé, allez dans l'onglet utilisateur et attribuez-le à votre utilisateur Admin.

Une fois cela fait, retournez à votre SPA en cours d'exécution localement et essayez de vous connecter avec un identifiant. Vous devriez pouvoir accéder à un portail utilisateur comme ci-dessous :

![Connexion Initiale](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215500834/SgGX7vE_5.png)

### 5) Configuration des Actions

Cliquez sur l'onglet Actions dans la barre latérale de gauche. Ensuite, allez dans la catégorie Flux.

Sélectionnez le Flux de Connexion. Cela exécutera le flux d'une action une fois le processus de connexion dans votre boîte de connexion terminé.

![Flux de Connexion](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215815525/N-h2y-tlI.png)

Cliquez sur le bouton `+` dans Ajouter une Action et sélectionnez Construire une Action Personnalisée.

Nommez-la MFA pour Rôle et laissez le reste tel quel.

![Flux de Création d'Action](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215793963/Rj2rC2T6f.png)

Une fois créée, vous arriverez à un écran comme suit :

![Éditeur de Code d'Action](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215844044/VrPsqFVBz.png)

Ajoutez le code suivant dans la fonction `onExecutePostLogin` :

```
  if (event.authorization != undefined && event.authorization.roles.includes("Admin")) {
      api.multifactor.enable("any");
  };

```

![Code d'Action](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215869129/2ELHfGy5s.png)

Sur le côté gauche, vous pouvez voir un bouton de lecture. Il s'agit de votre environnement de test à l'intérieur de l'éditeur d'actions. Vous trouverez l'objet [event](https://auth0.com/docs/actions/triggers/post-login/event-object) dans lequel vous pouvez tester le flux d'actions en ajoutant `Admin` au tableau `authorization.roles`.  
  
Lorsque vous ajoutez le rôle `Admin`, vous devriez voir une réponse avec MFA comme ci-dessous. Lorsqu'il n'est pas présent, vous devriez obtenir un tableau vide.

![Cas de Test d'Action](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215931493/zai-96biU.png)

Cliquez sur sauvegarder le brouillon et déployer. 

Allez maintenant dans le flux et cliquez sur l'onglet actions personnalisées à droite et vous devriez pouvoir glisser-déposer l'action `MFA pour Rôles` dans le flux. Cliquez sur Appliquer pour que ce nouveau flux fonctionne avec votre boîte de connexion.

![Flux d'Action](https://cdn.hashnode.com/res/hashnode/image/upload/v1639215949399/nK49n1ZHZ.png)

Vous devrez également activer la MFA sur le tableau de bord Auth0. 

Ouvrez l'onglet Sécurité et choisissez l'authentification multifactorielle. Dans l'écran suivant, activez le Mot de Passe à Usage Unique. Cela permettra aux utilisateurs d'utiliser une application comme Google Authenticator pour un mot de passe à usage unique. 

Il existe d'autres facteurs que vous pouvez imposer, comme l'OTP basé sur SMS ou Email, mais pour cette démonstration, nous utiliserons uniquement le mot de passe à usage unique.  
  
Dans la section politiques, laissez tout tel quel et sauvegardez vos modifications.

![Écran MFA](https://cdn.hashnode.com/res/hashnode/image/upload/v1639216209703/f54daE0Jo.png)

### 6) Test avec Votre Application

Maintenant, lorsque vous allez vous connecter sur l'application en cours d'exécution localement, vous devriez être invité à faire une MFA pour l'utilisateur admin. Alors testons cela.

Cliquez sur connexion et redirigez vers votre boîte de connexion. Si vous êtes déjà connecté, déconnectez-vous puis faites de même.

Entrez les identifiants de votre utilisateur admin :

![Connexion Admin](https://cdn.hashnode.com/res/hashnode/image/upload/v1639216252587/jyNxUdkU9.png)

Une fois la connexion effectuée, vous serez invité à vous authentifier avec votre application d'authentification préférée. J'ai utilisé Google Authenticator et j'ai entré mon OTP.

![MFA Admin](https://cdn.hashnode.com/res/hashnode/image/upload/v1639216272416/9BGhY_91S.png)

Vous serez ensuite invité à consentir à partager vos données utilisateur avec l'application.

![Consentement MFA](https://cdn.hashnode.com/res/hashnode/image/upload/v1639216291893/v2IITRcrF.png)

Une fois que vous acceptez ce qui précède, vous devriez être connecté.

![Admin Connecté](https://cdn.hashnode.com/res/hashnode/image/upload/v1639216404160/YnZZikEzZ.png)

Si vous essayez le même flux avec l'utilisateur de test, vous remarquerez que vous êtes directement connecté après la page de consentement et qu'aucune demande de MFA n'a été déclenchée. 

C'est parce que dans notre code d'actions, comme montré ci-dessous, vous pouvez voir que nous vérifions si les rôles de l'utilisateur ont le rôle Admin. Si c'est le cas, alors nous demandons à Auth0 de déclencher un flux de travail MFA avec l'un des cas d'utilisation MFA activés du locataire.

```
  if (event.authorization != undefined && event.authorization.roles.includes("Admin")) {
      api.multifactor.enable("any");
  };

```

## Conclusion

Félicitations ! Vous venez de créer un flux d'Actions Auth0 personnalisé et de le tester. Il s'agissait d'un exemple simple pour vous aider à comprendre ce que sont les Actions Auth0, et comment elles peuvent être construites et utilisées dans vos flux de travail. 

Il existe de nombreux flux plus complexes que vous pouvez construire, et vous pouvez trouver quelques exemples fournis par Auth0 ci-dessous. Il suffit de cliquer sur le déclencheur et vous trouverez des exemples spécifiques.

[Code d'Actions Exemple](https://auth0.com/docs/actions/triggers/)

Merci d'avoir lu ! J'espère vraiment que vous trouverez cet article utile. Si c'est le cas, veuillez le partager pour que d'autres puissent le voir.

Merci d'avoir lu ! :)

P.S N'hésitez pas à me contacter sur [LinkedIn](https://www.linkedin.com/in/rohitjmathew) ou [Twitter](https://twitter.com/iamrohitjmathew)

## Annexe

Les sources suivantes ont été très utiles pour la rédaction de cet article :

* [Présentation des Actions Auth0 - Auth0](https://auth0.com/blog/introducing-auth0-actions/)
* [Actions Auth0 - Documentation Auth0](https://auth0.com/docs/actions)