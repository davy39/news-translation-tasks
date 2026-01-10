---
title: Comment authentifier un utilisateur avec la reconnaissance faciale dans React.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-29T13:55:01.000Z'
originalURL: https://freecodecamp.org/news/authenticate-with-face-recognition-reactjs
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/FaceIO-react--1-.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: facial recognition
  slug: facial-recognition
- name: privacy
  slug: privacy
- name: React
  slug: react
- name: Security
  slug: security
seo_title: Comment authentifier un utilisateur avec la reconnaissance faciale dans
  React.js
seo_desc: "By Hrishikesh Pathak\nWith the advent of Web 2.0, authenticating users\
  \ became a crucial task for developers. \nBefore Web 2.0, website visitors could\
  \ only view the content of a web page – there was no interaction. This era of the\
  \ internet was called We..."
---

Par Hrishikesh Pathak

Avec l'avènement du Web 2.0, l'authentification des utilisateurs est devenue une tâche cruciale pour les développeurs. 

Avant le Web 2.0, les visiteurs d'un site web ne pouvaient que consulter le contenu d'une page web – il n'y avait aucune interaction. Cette ère d'Internet était appelée Web 1.0.

Mais après le Web 2.0, les gens ont acquis la capacité de publier leur propre contenu sur un site web. Et alors, la modération de contenu est devenue une tâche sans fin pour les propriétaires de sites web. 

Pour réduire le spam sur ces sites web, les développeurs ont introduit des systèmes d'authentification des utilisateurs. Maintenant, les modérateurs de sites web peuvent facilement connaître la source du spam et peuvent empêcher ces spammers d'accéder davantage au site web.

Si vous souhaitez savoir comment implémenter la modération de contenu sur votre site web, vous pouvez lire mon article sur [Comment détecter et flouter les visages dans vos applications web](https://betterprogramming.pub/detect-and-blur-human-faces-on-your-website-8c4a2d69a538).

Maintenant, voyons ce que nous allons aborder dans ce tutoriel.

## Ce que vous apprendrez dans ce tutoriel

Dans ce tutoriel, nous discuterons des différentes techniques d'authentification que vous pouvez utiliser pour authentifier les utilisateurs. Cela inclut l'authentification par e-mail et mot de passe, l'authentification par téléphone, OAuth, les liens magiques sans mot de passe, et enfin l'authentification faciale. 

Notre principal objectif sera l'authentification via les techniques de reconnaissance faciale dans cet article.

Nous allons également construire un projet qui vous apprend à intégrer l'authentification basée sur la reconnaissance faciale dans votre application web React. 

Dans ce projet, nous utiliserons la plateforme SaaS (logiciel en tant que service) FaceIO pour intégrer l'authentification basée sur la reconnaissance faciale. Assurez-vous donc de configurer un compte [FaceIO](https://faceio.net/getting-started) gratuit pour suivre.

Et enfin, nous examinerons l'aspect de la confidentialité des utilisateurs et discuterons de la manière dont la reconnaissance faciale ne nuit pas à votre confidentialité. Nous parlerons également de savoir si c'est un choix fiable pour les développeurs à l'avenir.

Cet article est rempli d'informations, de projets pratiques et de discussions. Prenez une tasse de café et une part de pizza 🍕 et commençons.

La version finale de ce projet ressemble à ceci. Cela semble intéressant ? Alors, faisons-le.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/faceIO-final.gif)

## Différents types de systèmes d'authentification des utilisateurs

Il existe de nombreux systèmes d'authentification des utilisateurs que vous pouvez choisir d'implémenter sur vos sites web. Il n'y a pas de techniques d'authentification vraiment supérieures ou inférieures. Tous ces systèmes d'authentification dépendent de l'utilisation du bon outil pour le travail.

Par exemple, si vous créez une simple page de destination pour collecter des e-mails auprès des utilisateurs, il n'est pas nécessaire d'utiliser OAuth. Mais si vous construisez une plateforme sociale, alors utiliser OAuth a plus de sens que l'authentification traditionnelle. Vous pouvez récupérer les détails de l'utilisateur et les images de profil directement depuis OAuth.

Si votre application web est construite autour de contenu lié à des investissements ou de services juridiquement contraignants, alors utiliser l'authentification par téléphone a plus de sens. Un utilisateur peut créer des comptes e-mail illimités, mais il aura un nombre limité de numéros de téléphone à utiliser.

Examinons quelques systèmes d'authentification populaires afin de voir leurs avantages et inconvénients.

### Authentification basée sur l'e-mail et le mot de passe

L'authentification basée sur l'e-mail et le mot de passe est la technique la plus ancienne pour vérifier un utilisateur. L'implémentation est également très simple et facile à utiliser. 

L'avantage de ce système est que vous n'avez pas besoin d'avoir un compte tiers pour vous connecter. Si vous avez un e-mail, qu'il soit auto-hébergé ou provenant d'un service (comme Gmail, Outlook, etc.), vous êtes prêt à partir. 

Le principal inconvénient de ce système est que vous devez vous souvenir de tous vos mots de passe. Comme le nombre de sites web ne cesse de croître et que nous devons nous connecter à la plupart des sites pour accéder à nos profils, se souvenir des mots de passe pour chaque site devient une tâche ardue pour nous, humains. 

Trouver un mot de passe unique et fort est également une tâche énorme. Nos cerveaux ne sont généralement pas capables de mémoriser de nombreuses chaînes aléatoires de lettres et de chiffres. C'est le plus grand inconvénient des systèmes d'authentification basés sur l'e-mail et le mot de passe.

### Authentification par téléphone

L'authentification par téléphone est généralement une technique d'authentification très fiable pour vérifier l'identité d'un utilisateur. Comme un utilisateur n'a généralement pas plus d'un numéro de téléphone, cela peut être mieux adapté pour les sites web liés aux actifs où l'identité de l'utilisateur est très importante. 

Mais l'inconvénient de ce système est que les gens ne veulent pas révéler leurs numéros de téléphone s'ils ne vous font pas confiance. Un numéro de téléphone est beaucoup plus personnel qu'un e-mail. 

Un autre facteur important de l'authentification par téléphone est son coût. Le coût de l'envoi d'un message texte à un utilisateur avec un OTP est élevé par rapport à l'e-mail. Les propriétaires de sites web et les développeurs préfèrent donc souvent rester avec l'authentification par e-mail.

### Authentification basée sur OAuth 

OAuth est une technique relativement nouvelle par rapport aux deux précédentes. Dans cette technique, les fournisseurs OAuth authentifient les utilisateurs et fournissent des informations utiles au nom de l'utilisateur. 

Par exemple, si l'utilisateur a un compte avec Google (par exemple), il peut se connecter à d'autres sites directement en utilisant son compte Google. Le site web obtient les détails de l'utilisateur directement depuis Google. Cela signifie qu'il n'est pas nécessaire de créer plusieurs comptes et de se souvenir de chaque mot de passe pour ces comptes. 

Le principal inconvénient de ce système est que vous, en tant que développeur, devez faire confiance aux fournisseurs OAuth et de nombreuses personnes ne veulent pas lier tous leurs comptes pour des raisons de confidentialité. Vous verrez donc souvent un champ e-mail-mot de passe en plus de OAuth sur la plupart des sites web.

### Authentification par lien magique

Les liens magiques résolvent la plupart des problèmes auxquels vous êtes confronté dans l'authentification par e-mail et mot de passe. Ici, vous devez fournir uniquement votre mot de passe et vous recevrez un e-mail avec un lien d'authentification. Ensuite, vous devez ouvrir ce lien dans votre navigateur et c'est tout. Pas besoin de se souvenir de mots de passe. 

Ce type d'authentification a gagné en popularité ces jours-ci. Il fait gagner beaucoup de temps à l'utilisateur, et il est également très économique. Et vous n'avez pas à faire confiance à un tiers comme dans le cas de OAuth.

### Authentification par reconnaissance faciale

La reconnaissance faciale est l'une des dernières techniques d'authentification, et de nombreux développeurs l'adoptent ces jours-ci. La reconnaissance faciale réduit la difficulté de saisir votre e-mail-mot de passe ou toute autre information d'identification de l'utilisateur pour se connecter à une application web. 

Le plus important est que ce système d'authentification est rapide et ne nécessite aucun matériel spécial. Vous avez juste besoin d'une webcam, que presque tous les appareils ont de nos jours. 

La technologie de reconnaissance faciale utilise l'intelligence artificielle pour cartographier les détails faciaux uniques d'un utilisateur et les stocker sous forme de hachage (certains nombres et texte aléatoires sans signification) pour réduire les problèmes liés à la confidentialité. 

Construire et déployer un modèle de reconnaissance faciale basé sur l'intelligence artificielle à partir de zéro n'est pas facile et peut être très coûteux pour les développeurs indépendants et les petites startups. Vous pouvez donc utiliser des plateformes SaaS pour effectuer tout ce travail lourd pour vous. FaceIO et AWS Recognition sont des exemples de ces types de services que vous pouvez utiliser dans vos projets.

Dans ce projet pratique, nous allons utiliser les API FaceIO pour authentifier un utilisateur via la reconnaissance faciale dans une application web React. FaceIO vous offre un moyen facile d'intégrer le système d'authentification avec leur bibliothèque JavaScript `fio.js`.

## Installation du projet

Avant de commencer, assurez-vous de créer un compte FaceIO et de créer un nouveau projet. Enregistrez l'ID public de votre projet FaceIO. Nous avons besoin de cet ID plus tard dans notre projet.

Pour créer un projet React.js, nous utiliserons Vite. Pour démarrer un projet Vite, naviguez vers votre dossier souhaité et exécutez la commande suivante :

```bash
npm create vite@latest

```

Suivez ensuite les instructions et créez une application React en utilisant Vite. Naviguez à l'intérieur du dossier et exécutez `npm install` pour installer toutes les dépendances de votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-from-2022-07-27-10-46-05.png)

Après avoir suivi toutes ces étapes, la structure de votre projet devrait ressembler à ceci :

```bash
.
├── index.html
├── package.json
├── package-lock.json
├── public
│   └── vite.svg
├── src
│   ├── App.css
│   ├── App.jsx
│   ├── assets
│   │   └── react.svg
│   └── main.jsx
└── vite.config.js

```

## Comment intégrer FaceIO dans notre projet React

Pour intégrer FaceIO dans notre projet, nous devons ajouter leur CDN dans le fichier `index.html`. Ouvrez le fichier `index.html` et ajoutez le CDN FaceIO avant le composant `root`. Pour en savoir plus, consultez le [guide d'intégration de FaceIO](https://faceio.net/integration-guide).

```html
<body>    
    <script src="https://cdn.faceio.net/fio.js"></script>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
</body>

```

Maintenant, supprimez tout le code du fichier `App.jsx` pour commencer à partir de zéro. J'ai gardé ce tutoriel aussi minimal que possible. J'ai donc seulement ajouté un titre et deux boutons dans l'interface utilisateur pour démontrer comment fonctionne le processus d'authentification faciale de FaceIO. 

Ici, un bouton fonctionne comme un bouton d'inscription, et l'autre comme un bouton de connexion.

Le code à l'intérieur du fichier `App.jsx` ressemble à ceci :

```jsx
import "./App.css";
function App() {
  return (
    <section>
      <h1>Authentification faciale par FaceIO</h1>
      <button>S'inscrire</button>
      <button>Se connecter</button>
    </section>
  );
}

export default App;

```

### Comment enregistrer le visage d'un utilisateur en utilisant FaceIO

Travailler avec FaceIO est très rapide et facile. Comme nous utilisons la bibliothèque `fio.js`, nous devons exécuter une seule fonction d'assistance pour authentifier un utilisateur. Cette bibliothèque `fio.js` fera la plupart du travail pour nous.

Pour enregistrer un utilisateur, nous initialisons notre objet FaceIO à l'intérieur d'un hook `useEffect`. Sinon, chaque fois qu'un état change, il réexécute les composants et réinitialise l'objet `faceIO`.

```js
let faceio;
useEffect(() => {
    faceio = new faceIO("Votre ID public ici");
}, []);

```

Votre ID public FaceIO se trouve sur votre console FaceIO. Copiez l'ID public et collez-le ici pour initialiser votre objet FaceIO.

Maintenant, définissez une fonction nommée `handleSignIn()`. Cette fonction contient notre logique d'enregistrement de l'utilisateur. 

À l'intérieur de la fonction, appelez la méthode `enroll` de l'objet `faceIO`. Cette méthode `enroll` est équivalente à la fonction d'inscription dans un système d'enregistrement standard basé sur un mot de passe et accepte un argument `payload`. Vous pouvez ajouter toute information spécifique à l'utilisateur (par exemple, son nom ou son adresse e-mail) à ce payload. 

Ces informations de payload seront stockées avec les données d'authentification faciale pour référence future. Pour en savoir plus sur les autres arguments optionnels, consultez leur [documentation API](https://faceio.net/integration-guide#enroll).

Dans notre bouton `S'inscrire`, lors du clic de l'utilisateur, nous invoquons cette fonction `handleSignIn()`. Les extraits de code pour l'inscription de l'utilisateur ressemblent à ceci :

```js
const handleSignIn = async () => {
    try {
      let response = await faceio.enroll({
        locale: "auto",
        payload: {
          email: "example@gmail.com",
          pin: "12345",
        },
      });

      console.log(` Identifiant facial unique : ${response.facialId}
      Date d'enregistrement : ${response.timestamp}
      Genre : ${response.details.gender}
      Approximation de l'âge : ${response.details.age}`);
    } catch (error) {
      console.log(error);
    }
  };

<button onClick={handleSignIn}>S'inscrire</button>

```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/faceIO-1.png)
_Écran FaceIO_

### Comment se connecter en utilisant la reconnaissance faciale

Après avoir enregistré l'utilisateur, vous devrez ensuite l'amener dans le flux d'authentification ou de connexion. L'utilisation de la bibliothèque `fio.js` facilite également la configuration d'un flux de connexion utilisant l'authentification faciale. 

Nous devons invoquer la méthode `authenticate` de l'objet `faceIO`, qui est équivalente à la fonction de connexion dans un système d'enregistrement standard basé sur un mot de passe, et tout le travail critique sera effectué par le package `fio.js`.

Tout d'abord, définissez une nouvelle fonction nommée `handleLogIn()` pour gérer toute la logique de connexion dans notre application React. À l'intérieur de cette fonction, nous invoquons la méthode `authenticate` de l'objet `faceIO` comme je l'ai mentionné précédemment.

Cette méthode accepte un argument `locale`. Il s'agit de la langue par défaut de l'interaction des utilisateurs avec les widgets FaceIO. Si vous n'êtes pas sûr, vous pouvez attribuer `auto` à ce champ. 

La méthode `authenticate` accepte également d'autres arguments optionnels comme `permissionTimeout`, `idleTimeout`, `replyTimeout`, etc. Vous pouvez consulter leur documentation API pour en savoir plus sur les arguments optionnels.

Nous invoquons cette fonction `handleLogIn()` lorsque quelqu'un clique sur le bouton `Se connecter` :

```js
const handleLogIn = async () => {
    try {
      let response = await faceio.authenticate({
        locale: "auto",
      });

      console.log(` Identifiant facial unique : ${response.facialId}
          Payload : ${response.payload}
          `);
    } catch (error) {
      console.log(error);
    }
  };

<button onClick={handleLogIn}>Se connecter</button>

```

Notre projet d'authentification des utilisateurs utilisant FaceIO et React est maintenant complet ! Vous avez appris comment enregistrer et connecter un utilisateur. Vous pouvez voir que le processus est assez simple par rapport à l'implémentation d'une méthode d'authentification basée sur `e-mail-mot de passe` ou une autre méthode d'authentification que nous avons discutée plus tôt dans cet article.

Maintenant, vous pouvez styliser tous les éléments `jsx` en utilisant CSS. Je n'ai pas ajouté de CSS ici pour réduire la complexité de ce projet. Si vous êtes curieux, vous pouvez consulter mon [Gist GitHub](https://gist.github.com/hrishiksh/bf76c98e05f6e85eb46d7e736bae351d).

Si vous souhaitez héberger ce projet React FaceIO gratuitement, vous pouvez consulter cet article sur [comment déployer votre projet React et Nextjs dans Cloudflare pages](https://hrishikeshpathak.com/blog/deploy-nextjs-cloudflare-pages).

## Comment utiliser l'API REST de FaceIO

En plus de fournir des widgets via la bibliothèque `fio.js`, FaceIO propose également des [API REST](https://faceio.net/rest-api) pour rationaliser le processus d'authentification. 

Chaque application dans la console FaceIO a une clé API. Vous pouvez utiliser cette clé API pour accéder aux points de terminaison de l'API REST de FaceIO. L'URL de base pour l'API REST est `https://api.faceio.net/`.

Le schéma d'URL accepte les paramètres d'URL comme ceci `https://api.faceio.net/cmd?param=val&param2=val2`. Ici, `cmd` est un point de terminaison API et `param` est un paramètre de point de terminaison s'il en accepte.

En utilisant les points de terminaison de l'API REST, vous pouvez automatiser diverses tâches dans votre backend.

1. Vous pouvez supprimer un identifiant facial à la demande d'un utilisateur.
2. Vous pouvez attacher un payload à un identifiant facial.
3. Vous pouvez changer le code PIN associé à un identifiant facial.

Cette API REST est destinée à être utilisée uniquement côté serveur. Assurez-vous de ne pas l'exposer aux clients. Il est important que vous lisiez les sections suivantes sur la confidentialité et la sécurité pour en savoir plus à ce sujet.

## Comment utiliser les WebHooks de FaceIO

Les Webhooks sont des systèmes de communication pilotés par des événements entre serveurs. Vous pouvez utiliser cette [fonctionnalité de webhook de FaceIO](https://faceio.net/webhooks) pour mettre à jour et synchroniser votre backend avec les nouveaux événements se produisant dans votre application web front-end. 

L'événement de ce webhook se déclenche lors de l'enregistrement d'un nouvel utilisateur, du succès de l'authentification faciale, de la suppression d'un identifiant facial, etc.

Vous pouvez configurer les webhooks FaceIO dans votre console de projet. Un appel typique de webhook de FaceIO dure 6 secondes. Cela contient toutes les informations sur un événement spécifique au format JSON et ressemble à ceci :

```json
{
  "eventName":"String - Nom de l'événement",
  "facialId": "String - Identifiant facial unique de l'utilisateur cible",
  "appId":    "String - ID public de l'application",
  "clientIp": "String - Adresse IP publique",
  "details": {
     "timestamp": "String optionnelle - Horodatage de l'événement",
     "gender":    "String optionnelle - Genre de l'utilisateur inscrit",
     "age":       "String optionnelle - Âge de l'utilisateur inscrit"
   }
}

```

## Confidentialité et FaceIO

La confidentialité est la chose la plus importante pour un utilisateur de nos jours. Comme les grandes entreprises utilisent vos données pour leur propre bénéfice, des questions se posent sur la validité et la légitimité de la confidentialité de ces techniques de reconnaissance faciale.

FaceIO, en tant que service, suit toutes les directives de confidentialité et obtient le consentement de l'utilisateur avant de demander l'accès à leur caméra. Même si le développeur le souhaitait, FaceIO ne scanne pas les visages sans obtenir le consentement. Les utilisateurs peuvent facilement se désinscrire du système et peuvent supprimer leurs données faciales du serveur.

FaceIO est conforme au CCP et au GDPR. En tant que développeur, vous pouvez publier ce système d'authentification faciale n'importe où dans le monde sans rencontrer de problèmes de confidentialité. Vous pouvez lire cet article pour en savoir plus sur les [meilleures pratiques de confidentialité de FaceIO](https://faceio.net/apps-best-practice).

## Sécurité de FaceIO

La sécurité d'une application web est un sujet important à discuter et à considérer. En tant que développeur, vous êtes responsable de la sécurité des utilisateurs d'un site ou d'une application.

FaceIO suit certaines directives de sécurité importantes et sérieuses pour la protection des données des utilisateurs. FaceIO hache toutes les données faciales uniques de l'utilisateur ainsi que le payload que nous avons spécifié précédemment. Ainsi, les informations stockées ne sont rien d'autre que des chaînes aléatoires qui ne peuvent pas être rétro-conçues.

FaceIO décrit certaines directives de sécurité très importantes pour les développeurs. Leur guide de sécurité se concentre sur l'ajout d'un code PIN fort pour protéger les données des utilisateurs. FaceIO rejette également les visages couverts afin que personne ne puisse usurper l'identité de quelqu'un d'autre.

## Conclusion

Si vous avez lu jusqu'ici, merci pour votre temps et vos efforts. Assurez-vous de suivre le tutoriel pratique afin de bien comprendre le sujet. 

Le projet devrait être accessible si vous suivez toutes les étapes. Si vous en faites quelque chose, montrez-le-moi sur [Twitter](https://twitter.com/hrishikshpathak). Si vous avez des questions, n'hésitez pas à demander. Je serai heureux de vous aider. En attendant, passez une bonne journée.