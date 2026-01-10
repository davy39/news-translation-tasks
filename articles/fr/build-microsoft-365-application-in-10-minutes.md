---
title: Comment créer votre première application Microsoft 365 en 10 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-04T17:32:26.000Z'
originalURL: https://freecodecamp.org/news/build-microsoft-365-application-in-10-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/banner.png
tags:
- name: JavaScript
  slug: javascript
- name: Microsoft
  slug: microsoft
- name: ' Single Page Applications '
  slug: single-page-applications
- name: Web Development
  slug: web-development
seo_title: Comment créer votre première application Microsoft 365 en 10 minutes
seo_desc: 'By Waldek Mastykarz

  If you''re a web developer and work with an organization that uses Microsoft 365,
  or you build applications that you sell to customers, I''ve got great news for you:
  you can use your existing skills to build applications that integr...'
---

Par Waldek Mastykarz

Si vous êtes un développeur web et que vous travaillez avec une organisation qui utilise Microsoft 365, ou si vous créez des applications que vous vendez à des clients, j'ai une excellente nouvelle pour vous : vous pouvez utiliser vos compétences existantes pour créer des applications qui s'intègrent à Microsoft 365.

## Qu'est-ce que Microsoft 365 ?

[Microsoft 365](https://www.microsoft.com/microsoft-365) est un ensemble d'applications, comme Microsoft Teams, Outlook, Word ou SharePoint, que les organisations utilisent pour travailler. Chaque jour, des millions de personnes utilisent Microsoft 365 pour discuter, se réunir, envoyer des e-mails, créer des documents, et bien plus encore.

Mais Microsoft 365 n'est pas seulement un ensemble d'applications. C'est aussi une plateforme qui permet aux développeurs, comme vous, de créer des applications. Ces applications peuvent exploiter les données et les insights stockés sur Microsoft 365 et les intégrer dans les flux de travail des utilisateurs.

## Vous pouvez créer votre première application Microsoft 365 en moins de 10 minutes

Voici un court tutoriel qui vous montrera comment créer une application monopage (SPA) simple qui s'intègre à Microsoft 365. L'application permettra aux utilisateurs de se connecter avec leur compte Microsoft 365 et de voir leurs informations de profil.

![Fenêtre de navigateur montrant une page web avec les informations de profil de l'utilisateur](https://www.freecodecamp.org/news/content/images/2022/09/microsoft-365-app-user-profile-information-1.png)
_Application Microsoft 365_

Cela ne semble pas être grand-chose, mais en créant cette application simple, vous apprendrez les bases de la création d'applications Microsoft 365.

### Ce dont vous aurez besoin

* [Node.js LTS](https://nodejs.org) (au moment de la rédaction de cet article, il s'agit de la version 16.17.1)
* Un tenant développeur Microsoft 365. Vous pouvez en obtenir un gratuitement via le [programme développeur Microsoft 365](https://developer.microsoft.com/microsoft-365/dev-program), ce qui vous donnera accès à toutes les API Microsoft 365 nécessaires pour créer vos applications, ainsi qu'à des données de démonstration pour commencer
* 10 minutes de votre temps

Prêt ? C'est parti !

## Enregistrez votre application sur le Microsoft Cloud

Créez un dossier pour votre application, où vous stockerez tous les fichiers de l'application. Ouvrez un terminal et changez le répertoire de travail vers ce dossier.

Dans le terminal, exécutez la commande suivante :

```bash
npx -p @pnp/cli-microsoft365 -- m365 login --authType browser
```

Dans votre navigateur web, connectez-vous avec votre compte développeur Microsoft 365 nouvellement créé :

![Écran de connexion Microsoft 365](https://www.freecodecamp.org/news/content/images/2022/09/Screenshot-2022-09-30-at-12.12.08.png)
_Connectez-vous à votre compte développeur Microsoft 365_

Ensuite, de retour dans le terminal, exécutez la commande suivante :

```bash
appId=$(npx -p @pnp/cli-microsoft365 -- m365 aad app add --name "Hello world" --multitenant --redirectUris "http://localhost,http://localhost/index.html" --platform spa --query "appId" -o text)
```

Avec ces deux commandes, vous avez utilisé la [CLI pour Microsoft 365](https://aka.ms/cli-m365) pour vous connecter à Microsoft 365 et enregistrer votre nouvelle application sur le Microsoft Cloud.

Chaque application qui s'intègre à Microsoft 365 doit être enregistrée et fournir des informations telles que le nom et le type d'application (plateforme). Pour les applications monopages, vous devez également spécifier l'URL de l'application, qui est utilisée pour s'assurer que les utilisateurs se connectent à la bonne application.

Ensuite, écrivez l'ID de l'application nouvellement créée dans un fichier que vous référencerez dans votre application. Dans le terminal, exécutez :

```bash
echo "const appId = '$appId';" > env.js
```

## Créez votre application

Ouvrez le dossier de votre application dans votre éditeur de code. Créez un nouveau fichier nommé `index.html` et collez le code suivant :

```html
<html>
<head>
  // TODO #1 : ajouter les bibliothèques
</head>
<body>
  <h1>Hello Microsoft 365</h1>
  <div id="auth"></div>
  <pre></pre>
  <script>
    // TODO #2 : ajouter le code de l'application
  </script>
</body>
</html>
```

Ce code est une page HTML simple avec deux espaces réservés : l'un pour les bibliothèques que vous utiliserez pour créer votre application, et l'autre pour le code de l'application. Il contient également une `div` où vous afficherez le bouton de connexion/déconnexion et un élément `pre` où vous afficherez les informations de profil de l'utilisateur.

## Ajoutez des bibliothèques

Remplacez le commentaire `TODO #1` par le code suivant :

```html
  <script src="https://alcdn.msauth.net/browser/2.28.3/js/msal-browser.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@microsoft/microsoft-graph-client/lib/graph-js-sdk.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@microsoft/microsoft-graph-client/lib/graph-client-msalBrowserAuthProvider.js"></script>
  <script src="./env.js"></script>
```

Pour créer cette application, vous utiliserez quelques bibliothèques :

* [MSAL.js](https://learn.microsoft.com/azure/active-directory/develop/msal-overview?WT.mc_id=m365-78653-wmastyka) qui vous aide à gérer la connexion des utilisateurs avec leur compte Microsoft 365
* [Microsoft Graph JavaScript SDK](https://learn.microsoft.com/graph/sdks/sdk-installation#install-the-microsoft-graph-javascript-sdk) qui simplifie l'appel à Microsoft Graph – l'API pour accéder aux données et aux insights sur Microsoft 365
* MSAL Browser Auth Provider qui intègre MSAL.js avec le SDK JS Microsoft Graph
* Le fichier `env.js` précédemment créé avec l'ID de votre application

L'utilisation de ces bibliothèques vous aidera à créer votre application plus rapidement, et vous n'aurez pas à vous soucier des détails sur la façon de connecter les utilisateurs, d'obtenir un jeton d'accès ou de gérer correctement les erreurs d'API.

## Connectez les utilisateurs avec leur compte Microsoft 365

Remplacez le commentaire `TODO #2` par le code suivant :

```javascript
    (() => {
      // TODO #3 : créer le client MSAL

      // TODO #5 : gérer la connexion/déconnexion

      // TODO #6 : créer le client Microsoft Graph

      // TODO #7 : obtenir le profil utilisateur Microsoft 365

      function render() {
        // TODO #4 : afficher l'interface utilisateur
      }

      render();
    })();
```

Ce code est une expression de fonction invoquée immédiatement (IIFE) qui encapsule le code de l'application et s'exécute au chargement de l'application. Il contient également plusieurs espaces réservés pour le code que vous écrirez dans les étapes suivantes.

Remplacez le commentaire `TODO #3` par le code suivant :

```javascript
      const msalConfig = {
        auth: {
          clientId: appId
        }
      };
      const msalClient = new msal.PublicClientApplication(msalConfig);
```

Dans ce fragment, vous créez un nouvel objet de configuration pour la bibliothèque MSAL.js qui inclut une référence à l'ID de l'application que vous avez créée précédemment.

Ensuite, vous passez cet objet au constructeur `PublicClientApplication` pour créer une nouvelle instance du client MSAL, que vous utiliserez pour connecter les utilisateurs à votre application avec leur compte Microsoft 365.

Pour l'instant, l'application affiche une page vide. Changeons cela en remplaçant le commentaire `TODO #4` par le code suivant :

```javascript
        msalClient
          .handleRedirectPromise()
          .then(response => {
            const accounts = msalClient.getAllAccounts();

            if (accounts.length === 0) {
              document.querySelector('#auth').innerHTML = '<button>Login</button>';
              document.querySelector('#auth button').addEventListener('click', login);
              document.querySelector('pre').innerHTML = '';
            }
            else {
              document.querySelector('#auth').innerHTML = '<button>Logout</button>';
              document.querySelector('#auth button').addEventListener('click', logout);
              // TODO #8 : afficher le profil utilisateur
            }
          });
```

Lors de la connexion des utilisateurs avec leur compte Microsoft 365, vous les redirigerez vers la page de connexion Microsoft 365. Lorsqu'ils se connecteront, ils seront redirigés vers votre application.

La fonction `handleRedirectPromise` gérera le traitement des informations que Microsoft 365 envoie à votre application. Lorsque les utilisateurs arrivent sur votre application et ne se sont pas encore connectés, la fonction `handleRedirectPromise` se résoudra avec une réponse `null`.

Après avoir géré la redirection, vous vérifiez à l'aide de MSAL si des utilisateurs sont connectés à votre application. S'il n'y en a aucun (`accounts.length === 0`), vous affichez le bouton de connexion. Si des utilisateurs sont connectés, vous affichez le bouton de déconnexion. Plus tard, vous ajouterez le code pour afficher les informations de profil de l'utilisateur.

Les boutons de connexion et de déconnexion n'ont pas encore de gestionnaires de clics, ajoutons-les en remplaçant `TODO #5` par le code suivant :

```javascript
      function login(e) {
        e.preventDefault();
        msalClient.loginRedirect();
      }

      function logout(e) {
        e.preventDefault();
        msalClient.logoutRedirect();
      }
```

Dans les deux cas, vous utilisez MSAL pour connecter et déconnecter les utilisateurs en les redirigeant vers la page de connexion/déconnexion de Microsoft 365.

À ce stade, votre application devrait vous permettre de vous connecter et de vous déconnecter en utilisant votre compte Microsoft 365. Pour vérifier que tout fonctionne comme prévu, enregistrez vos modifications et, dans le terminal, exécutez :

```bash
npx lite-server
```

Dans votre navigateur web, accédez à `http://localhost:3000` et connectez-vous à votre application. Vous devriez voir l'écran suivant :

![Fenêtre de navigateur avec une page web affichant un bouton de connexion](https://www.freecodecamp.org/news/content/images/2022/09/microsoft-365-app-login.png)
_Après vous être connecté à votre application_

Lorsque vous cliquez sur le bouton de connexion, il vous sera demandé de vous connecter avec votre compte Microsoft 365. Ensuite, lorsque vous cliquez sur le bouton de déconnexion, vous serez déconnecté de Microsoft 365 et de l'application.

Ceci conclut la première partie de la création de l'application, et vous êtes prêt à commencer à récupérer des données de Microsoft 365 à l'aide de Microsoft Graph.

## Afficher le profil utilisateur Microsoft 365

Maintenant que votre application prend en charge la connexion et la déconnexion avec les comptes Microsoft 365, l'étape suivante consiste à ajouter le code pour récupérer les informations de profil de l'utilisateur à partir de Microsoft 365.

Remplacez le commentaire `TODO #6` par le code suivant :

```javascript
      function getGraphClient(account) {
        const authProvider = new MSGraphAuthCodeMSALBrowserAuthProvider.AuthCodeMSALBrowserAuthenticationProvider(msalClient, {
          account,
          scopes: ['user.read'],
          interactionType: msal.InteractionType.Redirect,
        });

        return MicrosoftGraph.Client.initWithMiddleware({ authProvider });
      }
```

Cette fonction prend comme argument le compte Microsoft 365 qui a été utilisé pour se connecter à l'application et l'utilise pour créer un client Microsoft Graph que vous utiliserez pour appeler les API Microsoft Graph et obtenir des données de Microsoft 365.

Ensuite, remplaçons le commentaire `TODO #7` par le code suivant :

```javascript
      function loadUserProfile(graphClient) {
        graphClient
          .api('/me')
          .get()
          .then(res => {
            document.querySelector('pre').innerHTML = JSON.stringify(res, null, 2);
          });
      }
```

Cette fonction prend comme argument une instance du client Microsoft Graph telle que retournée par le SDK JavaScript Microsoft Graph et l'utilise pour appeler l'API Microsoft Graph.

Dans ce cas, vous appelez l'API Microsoft Graph `/me` qui renvoie les informations de profil de l'utilisateur actuellement connecté. Les données récupérées sont ensuite affichées dans l'élément `pre` sur la page.

La dernière étape consiste à lier le tout et à appeler les deux fonctions après que l'utilisateur s'est connecté à l'application. Remplacez le commentaire `TODO #8` par le code suivant :

```javascript
              const graphClient = getGraphClient(accounts[0]);
              loadUserProfile(graphClient);
```

C'est tout ! Lorsque vous enregistrez vos modifications et revenez au navigateur, vous verrez qu'il s'est automatiquement actualisé en arrière-plan, et vous êtes invité à accorder à l'application l'accès à vos informations de profil.

![Boîte de dialogue invitant l'utilisateur à accorder à l'application l'accès aux informations de profil de l'utilisateur](https://www.freecodecamp.org/news/content/images/2022/09/microsoft-365-app-profile-permissions-prompt.png)
_Configuration des autorisations sur l'application_

Après avoir accordé l'accès en cliquant sur le bouton **Accepter**, vous verrez les informations de profil affichées dans l'élément `pre` sur la page.

![Fenêtre de navigateur affichant les informations de profil utilisateur de Microsoft 365](https://www.freecodecamp.org/news/content/images/2022/09/microsoft-365-app-user-profile-information-2.png)
_Informations de profil_

Félicitations ! Vous venez de créer votre première application connectée à Microsoft 365.

## Ce n'est que le début

Vous venez de créer votre première application sur Microsoft 365 : une application monopage connectée à Microsoft 365 qui affiche le profil Microsoft 365 de l'utilisateur actuel. Cette application est un exemple simple pour vous montrer comment commencer à créer des applications sur Microsoft 365.

Il y a beaucoup plus de [données et d'insights stockés dans Microsoft 365](https://learn.microsoft.com/graph/api/overview) auxquels vos applications peuvent accéder, et il existe de [nombreux types d'applications](https://learn.microsoft.com/graph/overview) que vous pouvez créer. Le plus beau, c'est que vous pouvez utiliser les mêmes techniques que celles apprises au cours des 10 dernières minutes pour les construire.

Vous venez de créer une application Microsoft 365 en utilisant JavaScript, mais vous pouvez créer des applications sur Microsoft 365 en utilisant n'importe quel langage de programmation. Une chose que toutes les applications Microsoft 365 ont en commun est qu'elles apportent des données et des insights de Microsoft 365 pour aider les gens à travailler ensemble.

Curieux d'en savoir plus ? Découvrez ce que d'autres [développeurs](https://adoption.microsoft.com/sample-solution-gallery/) et [partenaires Microsoft](https://adoption.microsoft.com/partner-solution-gallery/) construisent sur Microsoft 365. Et si vous souhaitez approfondir vos connaissances, consultez le parcours d'apprentissage [Microsoft Graph Fundamentals](https://learn.microsoft.com/training/paths/m365-msgraph-fundamentals/). Et n'hésitez pas à nous contacter si vous avez des questions.