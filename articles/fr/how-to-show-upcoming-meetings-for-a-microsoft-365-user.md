---
title: Comment afficher les réunions à venir pour un utilisateur Microsoft 365
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-17T17:08:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-show-upcoming-meetings-for-a-microsoft-365-user
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-17-at-14.47.26.png
tags:
- name: JavaScript
  slug: javascript
- name: Microsoft
  slug: microsoft
- name: Productivity
  slug: productivity
- name: Web Development
  slug: web-development
seo_title: Comment afficher les réunions à venir pour un utilisateur Microsoft 365
seo_desc: 'By Waldek Mastykarz

  If you''re a web developer and you work with an organization that uses Microsoft
  365, you probably use it to manage your meetings.

  In this tutorial, you''ll learn how you can build a simple personal assistant in
  under 10 minutes tha...'
---

Par Waldek Mastykarz

Si vous êtes un développeur web et que vous travaillez avec une organisation qui utilise Microsoft 365, vous l'utilisez probablement pour gérer vos réunions.

Dans ce tutoriel, vous apprendrez comment construire un assistant personnel simple en moins de 10 minutes qui affichera à un utilisateur Microsoft 365 les réunions qu'il lui reste pour la journée.

## Comment construire des applications pour Microsoft 365

[Précédemment](https://www.freecodecamp.org/news/build-microsoft-365-application-in-10-minutes/), je vous ai montré comment utiliser vos compétences existantes en développement web pour exploiter les données et les insights stockés sur Microsoft 365 et construire des applications pour votre organisation.

En seulement 10 minutes, vous pouvez construire une application simple qui affiche le profil de l'utilisateur connecté à votre application avec son compte Microsoft 365.

![Fenêtre de navigateur montrant une page web avec des informations de profil utilisateur](https://www.freecodecamp.org/news/content/images/2022/09/microsoft-365-app-user-profile-information-1.png)
_Application Microsoft 365 simple montrant le profil de l'utilisateur actuel_

Cette fois, je veux vous montrer comment construire – en seulement 10 minutes – un assistant personnel simple qui affiche les réunions à venir pour l'utilisateur actuellement connecté.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-88.png)
_Application personnalisée pour Microsoft 365 montrant la liste des réunions à venir_

## Ce dont vous aurez besoin

* [Node.js LTS](https://nodejs.org/) (au moment de la rédaction de cet article, c'est la version 16.18.0)
* un locataire développeur Microsoft 365. Vous pouvez en obtenir un gratuitement depuis le [programme développeur Microsoft 365](https://developer.microsoft.com/microsoft-365/dev-program), et il vous donnera accès à toutes les API Microsoft 365 dont vous avez besoin pour construire vos applications, ainsi qu'à des données de démonstration pour commencer
* 10 minutes de votre temps

## Comment enregistrer votre application sur le cloud Microsoft

Créez un dossier pour votre application, où vous stockerez tous les fichiers de l'application. Ouvrez un terminal et changez le répertoire de travail pour ce dossier.

Dans le terminal, exécutez la commande suivante :

```bash
npx -p @pnp/cli-microsoft365 -- m365 login --authType browser
```

Dans votre navigateur web, connectez-vous avec votre nouveau compte développeur Microsoft 365 :

![Écran de connexion Microsoft 365](https://www.freecodecamp.org/news/content/images/2022/09/Screenshot-2022-09-30-at-12.12.08.png)
_Connectez-vous à votre compte développeur Microsoft 365_

Ensuite, retournez dans le terminal et exécutez la commande suivante :

```bash
appId=$(npx -p @pnp/cli-microsoft365 -- m365 aad app add --name "Upcoming Meetings" --multitenant --redirectUris "http://localhost,http://localhost/index.html" --platform spa  --query "appId" -o text)
```

Avec ces deux commandes, vous avez utilisé le [CLI pour Microsoft 365](https://aka.ms/cli-m365) pour vous connecter à Microsoft 365 et enregistrer votre nouvelle application sur le cloud Microsoft.

Toute application qui s'intègre à Microsoft 365 doit être enregistrée et fournir des informations telles que le nom et le type de l'application (plateforme). Pour les applications monopages, vous devez également spécifier l'URL de l'application, qui est utilisée pour garantir que les utilisateurs se connectent à la bonne application.

Ensuite, écrivez l'ID de la nouvelle application créée dans un fichier que vous référencerez dans votre application. Dans le terminal, exécutez :

```bash
echo "const appId = '$appId';" > env.js
```

## Comment créer votre application

Ouvrez le dossier de votre application dans votre éditeur de code. Créez un nouveau fichier nommé `index.html` et collez le code suivant :

```html
<html>
<head>
  <title>Upcoming meetings</title>
  <!-- TODO #1: ajouter les bibliothèques -->
</head>
<body>
  <h1>Upcoming meetings</h1>
  <div id="auth"></div>
  <div id="upcomingMeetings"></div>
  <script>
    // TODO #2: ajouter le code de l'application
  </script>
</body>
</html>
```

Ce code est une simple page HTML avec deux espaces réservés : un pour les bibliothèques que vous utiliserez pour construire votre application, et un autre pour le code de l'application. Il contient également une `div` où vous afficherez le bouton de connexion/déconnexion et une autre `div` où vous afficherez la liste des réunions à venir pour aujourd'hui.

## Comment ajouter les bibliothèques

Remplacez le commentaire `TODO #1` par le code suivant :

```html
  <script src="https://alcdn.msauth.net/browser/2.28.3/js/msal-browser.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@microsoft/microsoft-graph-client/lib/graph-js-sdk.js"></script>
  <script
    src="https://cdn.jsdelivr.net/npm/@microsoft/microsoft-graph-client/lib/graph-client-msalBrowserAuthProvider.js"></script>
  <script src="./env.js"></script>
```

Pour construire cette application, vous utiliserez quelques bibliothèques :

* [MSAL.js](https://learn.microsoft.com/azure/active-directory/develop/msal-overview?WT.mc_id=m365-79476-wmastyka) qui vous aide à gérer la connexion des utilisateurs avec leur compte Microsoft 365
* [Microsoft Graph JavaScript SDK](https://learn.microsoft.com/graph/sdks/sdk-installation#install-the-microsoft-graph-javascript-sdk) qui simplifie l'appel à Microsoft Graph – l'API pour accéder aux données et insights sur Microsoft 365
* MSAL Browser Auth Provider qui intègre MSAL.js avec le Microsoft Graph JS SDK
* le fichier `env.js` précédemment créé avec l'ID de votre application

L'utilisation de ces bibliothèques vous aidera à construire votre application plus rapidement, et vous n'aurez pas à vous soucier des détails de la connexion des utilisateurs, de l'obtention d'un jeton d'accès, ou de la gestion correcte des erreurs d'API.

## **Comment connecter les utilisateurs avec leur compte Microsoft 365**

Remplacez le commentaire `TODO #2` par le code suivant :

```javascript
    (() => {
      // TODO #3: créer le client MSAL

      // TODO #5: gérer la connexion/déconnexion

      // TODO #6: créer le client Microsoft Graph

      // TODO #7: obtenir les réunions à venir depuis le calendrier de l'utilisateur Microsoft 365

      function render() {
        // TODO #4: rendre l'UI
      }

      render();
    })();
```

Ce code est une expression de fonction immédiatement invoquée (IIFE) qui encapsule le code de l'application et s'exécute lorsque l'application se charge. Il contient également plusieurs espaces réservés pour le code que vous écrirez dans les prochaines étapes.

Remplacez le commentaire `TODO #3` par le code suivant :

```javascript
      const scopes = ['Calendars.Read'];
      const msalConfig = {
        auth: {
          clientId: appId
        }
      };
      const msalClient = new msal.PublicClientApplication(msalConfig);
```

Dans ce fragment, vous créez un nouvel objet de configuration pour la bibliothèque MSAL.js qui inclut une référence à l'ID de l'application que vous avez créée précédemment. Vous définissez également une liste de permissions (également connues sous le nom de scopes) que votre application devra demander pour pouvoir accéder aux informations du calendrier de l'utilisateur actuellement connecté.

Ensuite, vous passez cet objet au constructeur `PublicClientApplication` pour créer une nouvelle instance du client MSAL. Vous l'utiliserez pour connecter les utilisateurs à votre application avec leur compte Microsoft 365.

Pour l'instant, l'application affiche une page vide. Changeons cela en remplaçant le commentaire `TODO #4` par le code suivant :

```javascript
        msalClient
          .handleRedirectPromise()
          .then(response => {
            const accounts = msalClient.getAllAccounts();

            if (accounts.length === 0) {
              document.querySelector('#auth').innerHTML = '<button>Login</button>';
              document.querySelector('#auth button').addEventListener('click', login);
              document.querySelector('#upcomingMeetings').innerHTML = '';
            }
            else {
              document.querySelector('#auth').innerHTML = '<button>Logout</button>';
              document.querySelector('#auth button').addEventListener('click', logout);
              // TODO #8: charger les réunions à venir
            }
          });
```

Lorsque vous connectez les utilisateurs avec leur compte Microsoft 365, vous les redirigez vers la page de connexion Microsoft 365. Lorsqu'ils se connectent, ils sont redirigés vers votre application.

La fonction `handleRedirectPromise` gérera le traitement des informations que Microsoft 365 envoie à votre application. Lorsque les utilisateurs arrivent sur votre application et ne sont pas encore connectés, la fonction `handleRedirectPromise` se résoudra avec une réponse `null`.

Après avoir traité la redirection, vous vérifiez à l'aide de MSAL s'il y a des utilisateurs connectés à votre application. S'il n'y en a aucun (`accounts.length === 0`), vous affichez le bouton de connexion. S'il y a des utilisateurs connectés, vous affichez le bouton de déconnexion. Plus tard, vous ajouterez le code pour afficher les réunions à venir depuis le calendrier de l'utilisateur.

Les boutons de connexion et de déconnexion manquent de leurs gestionnaires de clics, alors ajoutons-les en remplaçant `TODO #5` par le code suivant :

```javascript
      function login(e) {
        e.preventDefault();
        msalClient.loginRedirect({
          scopes
        });
      }

      function logout(e) {
        e.preventDefault();
        msalClient.logoutRedirect();
      }
```

Dans les deux cas, vous utilisez MSAL pour connecter et déconnecter les utilisateurs en les redirigeant vers la page de connexion/déconnexion Microsoft 365. Dans la fonction de connexion, vous passez également le même ensemble de permissions afin que les utilisateurs ne soient invités qu'une seule fois à approuver le même ensemble de permissions lors de la connexion à l'application et du chargement de ses données.

À ce stade, votre application devrait vous permettre de vous connecter et de vous déconnecter en utilisant votre compte Microsoft 365. Pour vérifier que tout fonctionne comme prévu, sauvegardez vos modifications et, dans le terminal, exécutez :

```bash
npx lite-server
```

Dans votre navigateur web, accédez à `http://localhost:3000` et connectez-vous à votre application. Vous devriez voir l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-90.png)
_Après vous être connecté à votre application_

Lorsque vous cliquez sur le bouton de connexion, vous serez invité à vous connecter avec votre compte Microsoft 365. Ensuite, lorsque vous cliquez sur le bouton de déconnexion, vous serez déconnecté de Microsoft 365 et de l'application.

Cela conclut la première partie de la construction de l'application, et vous êtes prêt à commencer à récupérer des données depuis Microsoft 365 en utilisant Microsoft Graph.

## Comment afficher les réunions à venir depuis Microsoft 365

Maintenant que votre application prend en charge la connexion et la déconnexion avec les comptes Microsoft 365, l'étape suivante consiste à ajouter le code pour récupérer les informations sur les réunions à venir depuis le calendrier de l'utilisateur connecté.

### Comment obtenir un client Microsoft Graph

Remplacez le commentaire `TODO #6` par le code suivant :

```js
      function getGraphClient(account) {
        const authProvider = new MSGraphAuthCodeMSALBrowserAuthProvider.AuthCodeMSALBrowserAuthenticationProvider(msalClient, {
          account,
          scopes,
          interactionType: msal.InteractionType.Redirect,
        });

        return MicrosoftGraph.Client.initWithMiddleware({ authProvider });
      }
```

Cette fonction prend en argument le compte Microsoft 365 qui a été utilisé pour se connecter à l'application. Elle l'utilise pour créer un client Microsoft Graph que vous utiliserez pour appeler les API Microsoft Graph et obtenir des données depuis Microsoft 365.

Notez également que vous passez la même liste de permissions d'API (scopes) que vous avez définie précédemment. Cela permettra au `graphClient` d'obtenir un jeton d'accès pour l'API Microsoft Graph avec accès aux informations du calendrier.

### Comment charger les informations sur les réunions à venir

Ensuite, remplaçons le commentaire `TODO #7` par le code suivant :

```js
      function getTimeString(dateFromGraph) {
        const date = new Date(dateFromGraph + 'Z');
        const minutes = date.getMinutes();
        return `${date.getHours()}:${minutes < 10 ? '0' : ''}${minutes}`;
      }

      function loadUpcomingMeetings(graphClient) {
        // configurer la requête Microsoft Graph pour récupérer les réunions à venir pour aujourd'hui
        const now = new Date();
        const midnight = new Date();
        midnight.setDate(midnight.getDate() + 1);
        midnight.setHours(0);
        midnight.setMinutes(0);
        midnight.setSeconds(0);
        midnight.setMilliseconds(0);

        graphClient
          .api(`/me/calendarview?startdatetime=${now.toISOString()}&enddatetime=${midnight.toISOString()}&$orderby=start/dateTime`)
          .get()
          .then(res => {
            if (res.value.length === 0) {
              document.querySelector('#upcomingMeetings').innerHTML = 'No more meetings for today';
            }
            else {
              const meetingsHtml = res.value.map(meeting => {
                return `<dt>
                  ${getTimeString(meeting.start.dateTime)}-${getTimeString(meeting.end.dateTime)} ${meeting.subject}
                </dt>
                <dd>
                  ${meeting.location.displayName} with ${meeting.attendees.map(attendee => attendee.emailAddress.name).join(', ')}
                </dd>`;
              });
              document.querySelector('#upcomingMeetings').innerHTML = `<dl>${meetingsHtml.join('')}</dl>`;
            }
          });
      }
```

La fonction `loadUpcomingMeetings` prend en argument une instance du client Microsoft Graph telle que retournée par le SDK JavaScript Microsoft Graph et l'utilise pour appeler l'API Microsoft Graph.

### Comment appeler l'API Microsoft Graph

Pour obtenir la liste des réunions à venir pour aujourd'hui, vous appelez l'API Microsoft Graph `/me/calendarview`. Ce point de terminaison prend en arguments les dates et heures de début et de fin et retourne une vue du calendrier.

L'utilisation de ce point de terminaison vous permet d'inclure les occurrences de réunions récurrentes que les utilisateurs pourraient avoir dans leurs calendriers. Pour récupérer les réunions à venir pour aujourd'hui, vous prenez l'heure actuelle comme date/heure de début, et le minuit à venir comme date/heure de fin.

### Comment traiter la réponse de l'API Microsoft Graph

Après avoir appelé l'API, vous obtenez un tableau avec des objets qui représentent les réunions à venir pour l'utilisateur actuel. Chaque réunion contient des informations telles que le sujet de la réunion, l'heure de début et de fin, le lieu et les participants.

Si le tableau retourné est vide, cela signifie qu'il n'y a pas de réunions à venir. S'il contient un ou plusieurs éléments, vous utilisez la fonction `map` pour transformer les éléments de réunion en une chaîne HTML avec `dt` et `dd`, montrant le sujet de la réunion, l'heure de début et de fin dans un format lisible, le lieu de la réunion et qui sont les participants.

### Comment formater l'heure de début et de fin des événements

Pour formater la date, vous utilisez la fonction `getTimeString`. Elle prend en argument la date retournée par Microsoft Graph.

La chose importante à garder à l'esprit ici est que par défaut, l'API Microsoft Graph retourne les heures et les dates dans le fuseau horaire UTC. Comme les informations de fuseau horaire sont stockées séparément, avant de parser la date, vous devez ajouter le dénominateur de fuseau horaire UTC `Z` à la chaîne de date.

La dernière pièce est de tout rassembler et d'appeler les deux fonctions après que l'utilisateur se connecte à l'application. Remplacez le commentaire `TODO #8` par le code suivant :

```js
              const graphClient = getGraphClient(accounts[0]);
              loadUpcomingMeetings(graphClient);
```

C'est tout ! Lorsque vous sauvegardez vos modifications et retournez dans le navigateur, vous verrez qu'il s'est automatiquement actualisé en arrière-plan, et vous êtes invité à accorder à l'application l'accès à vos informations de calendrier.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-91.png)
_Défini les permissions sur l'application_

Après avoir accordé l'accès, en cliquant sur le bouton **Accepter**, vous verrez les informations sur vos réunions à venir affichées sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-92.png)
_Informations sur les réunions à venir récupérées depuis le calendrier Microsoft 365_

## Résumé

Dans cet article, vous avez appris comment utiliser le SDK Microsoft Graph pour vous connecter à l'API Microsoft Graph et récupérer des informations sur les réunions à venir depuis le calendrier de l'utilisateur actuel.

Ce n'est qu'un des nombreux scénarios et [types d'applications](https://learn.microsoft.com/graph/overview) que vous pouvez implémenter sur Microsoft 365. Pour plus d'informations sur le type de données et d'insights stockés sur Microsoft 365 auxquels vous pouvez accéder, consultez la [documentation de l'API Microsoft Graph](https://learn.microsoft.com/graph/api/overview).