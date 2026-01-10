---
title: Comment créer une fonction d'envoi d'e-mails en utilisant Nodemailer et OAuth2
subtitle: ''
author: Okoro Emmanuel Nzube
co_authors: []
series: null
date: '2025-03-24T23:36:41.467Z'
originalURL: https://freecodecamp.org/news/create-a-send-email-function-using-nodemailer-and-oauth2
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1742859346889/dad1b775-f088-4c24-b252-3d85ec9e0bb7.png
tags:
- name: Node.js
  slug: nodejs
- name: nodemailer
  slug: nodemailer
- name: React
  slug: reactjs
- name: Chakra-ui
  slug: chakra-ui
- name: OAuth2
  slug: oauth2
seo_title: Comment créer une fonction d'envoi d'e-mails en utilisant Nodemailer et
  OAuth2
seo_desc: 'Being able to communicate by sending emails through web applications is
  important these days. It helps businesses stay connected with their potential customers.

  In this article, you’ll learn how to implement the Send Email function in your web
  app us...'
---

Pouvoir communiquer en envoyant des e-mails via des applications web est important de nos jours. Cela aide les entreprises à rester en contact avec leurs clients potentiels.

Dans cet article, vous apprendrez comment implémenter la fonction d'envoi d'e-mails dans votre application web en utilisant Nodemailer.

Commençons sans plus tarder.

## Table des matières

1. [Prérequis](#heading-prerequisites)
    
2. [Outils que nous allons utiliser](#heading-outils-que-nous-allons-utiliser)
    
3. [Configuration du Frontend](#heading-configuration-du-frontend)
    
    * [Installer Node.js](#heading-installer-nodejs)
        
    * [Configuration du formulaire de contact](#heading-configuration-du-formulaire-de-contact)
        
4. [Configuration du Backend](#heading-configuration-du-backend)
    
    * [Configuration des bibliothèques Backend](#heading-configuration-des-bibliothèques-backend)
        
    * [Configuration OAuth2](#heading-configuration-oauth2)
        
    * [Configuration de Nodemailer](#heading-configuration-nodemailer)
        
5. [Conclusion](#heading-conclusion)
    

## **Prérequis**

Pour tirer le meilleur parti de ce projet, il est important d'avoir quelques connaissances de base sur les éléments suivants :

* JavaScript : Avoir une bonne compréhension fondamentale de comment JS fonctionne vous aidera à suivre le projet.
    
* React.js et Chakra UI : Vous devez avoir une bonne compréhension de comment `usestate` fonctionne et comment vous pouvez l'appliquer dans un projet. Il est également important que vous soyez familier avec Chakra UI et que vous sachiez comment l'utiliser pour styliser votre application web.
    
* Une petite connaissance de [Nodemailer](https://www.nodemailer.com/about/) serait également utile.
    

## **Outils que nous allons utiliser**

Dans l'un de mes projets récents, j'ai créé une fonction d'envoi d'e-mails en Node.js en utilisant Nodemailer. Cette fonction garantissait que les e-mails des utilisateurs seraient livrés efficacement. Et maintenant que je sais comment cela fonctionne, je voulais le partager avec vous tous.

### Nodemailer et SMTP

Alors, qu'est-ce que Nodemailer ?

Nodemailer est un module populaire de Node.js qui vous permet d'envoyer des e-mails efficacement en utilisant différentes méthodes telles que SMTP (Simple Mail Transfer Protocol), OAuth2, et ainsi de suite.

SMTP agit comme un service postal – ou plutôt, c'est un service postal qui trie vos e-mails et achemine vos messages sur différents serveurs de messagerie jusqu'à ce qu'ils atteignent leur destination finale. Cela aide à garantir que vos messages atteignent la bonne boîte de réception à chaque fois.

Mais il est important de noter que SMTP ne gère que **l'envoi d'e-mails**, ce qui signifie qu'il ne gère pas la récupération des e-mails déjà envoyés. Mais des protocoles comme IMAP (Internet Message Access Protocol) et POP3 (Post Office Protocol version 3) vous permettent de récupérer des e-mails. Nous n'utiliserons pas ces outils ici, mais je voulais simplement que vous en soyez conscient au cas où vous souhaiteriez implémenter une fonctionnalité de récupération dans vos propres projets.

### OAuth2

OAuth2, abréviation de Open Authorization, simplifie le processus d'authentification et d'autorisation. Avec OAuth2, les utilisateurs n'ont pas à subir le tracas de se connecter ou de se logger à plusieurs reprises. Au lieu de cela, les applications web peuvent accéder en toute sécurité aux données privées des utilisateurs sur d'autres sites web – uniquement avec la permission de l'utilisateur.

Mais ne vous inquiétez pas, OAuth2 n'accorde aux applications demandeuses qu'un accès limité, généralement juste assez pour créer un profil de base. Il est probable que vous ayez déjà utilisé OAuth2 sans même réaliser ce qui se passe en arrière-plan. Plutôt cool, n'est-ce pas ?

Maintenant que vous en savez un peu plus sur les outils que nous allons utiliser, passons à la suite.

## Configuration du Frontend

Tout d'abord, vous devez configurer votre environnement. Lors de la configuration de mon environnement, j'ai utilisé React.js et Chakra UI (pour le style).

### Installer Node.js

Avant de commencer ce processus, assurez-vous que Node est installé sur votre ordinateur. Si ce n'est pas le cas, rendez-vous sur leur [site web](https://nodejs.org/en) pour le télécharger et l'installer.

Vous pouvez également utiliser votre ligne de commande pour installer Node en exécutant la commande `nvm install --lts`.

Ou vous pourriez utiliser la nouvelle méthode recommandée sur le site web de Node.js, qui consiste simplement à exécuter `fnm`.

Voici comment procéder : sur votre ligne de commande, exécutez les commandes suivantes :

```javascript
winget install Schniz.fnm // cette commande télécharge et installe fnm dans votre système d'exploitation.

fnm install 22 // cela télécharge et installe node.js.

node -v // cela affiche la version de node.js actuellement installée dans votre système d'exploitation.

npm --v // cela vérifie la version de npm actuellement installée.

```

Ensuite, configurons votre interface frontend.

### Configuration du formulaire de contact

Comme je l'ai mentionné ci-dessus, j'utilise React pour mon frontend et Chakra UI pour le style. Je ne vais pas expliquer comment installer React ici, mais si vous avez besoin d'aide pour cela pour votre projet, [consultez mon article à ce sujet](https://www.freecodecamp.org/news/how-to-install-react-a-step-by-step-guide).

Ensuite, assurez-vous d'avoir Chakra UI configuré. Vous pouvez le faire en suivant les étapes sur le [site officiel de Chakra Ui](https://chakra-ui.com/docs/get-started/frameworks/vite).

Remarque : L'application web est une application web complète, qui se compose de diverses pages comme Accueil, Services, Tarifs, Contact, et ainsi de suite. Mais pour les besoins de cet article, nous nous concentrerons uniquement sur la page de contact.

Voici à quoi ressemblera la page de contact :

![Interface de conception frontend du formulaire de contact](https://cdn.hashnode.com/res/hashnode/image/upload/v1742477133862/421baf80-c55a-443a-9e68-c2b2e2a9b1a2.png align="center")

La première étape pour construire ce formulaire de contact est de créer votre entrée de formulaire. Voici comment vous pouvez le faire :

```javascript
import { Box, Button, Flex, Image, Input, Text, Textarea } from '@chakra-ui/react';
 return (
    <Flex
      flexDir={{ lg: 'row', md: 'row', sm: 'column', base: 'column' }}
      pt="10%"
      w={{ lg: '80%' }}
      gap={10}
      justify="center"
      align="center"
      m="auto"
    >
      <Box w="100%">
        <Image src="Images/Contact_Bg.png" alt="Contact Background" />
      </Box>

      <Box w="80%">
        <Text
          as="h1"
          fontSize={{ base: '2xl', md: '3xl', sm: '3xl' }}
          fontWeight="bold"
          mb={3}
        >
          Contactez-nous
        </Text>
        <Text
          as="p"
          w={{ base: '100%', md: '80%' }}
          mt={5}
          fontSize={{ base: 'sm', md: 'md', lg: 'lg' }}
          mb={6}
        >
          Veuillez utiliser le formulaire ci-dessous pour nous contacter, et notre équipe vous répondra dès que possible. Si vous préférez nous contacter par téléphone, vous pouvez trouver nos coordonnées ci-dessous.
        </Text>

        <Box w={{ base: '100%', md: '90%' }}>
          <Input
            required
            value={name}
            placeholder="Nom"
            mb={4}
            aria-label="Nom"
          />
          <Input
            required
            value={email}
            placeholder="Entrez votre Email"
            mb={4}
            aria-label="Email"
          />
          <Input
            required
            value={subject}
            placeholder="Sujet"
            mb={4}
            aria-label="Sujet"
          />
          <Textarea
            value={message}
            placeholder="Message"
            mb={4}
            aria-label="Message"
            resize="none"
          />
        </Box>

        <Button
          mb={4}
          isLoading={isLoading}
          isDisabled={isLoading}
          onClick={handleSubmit}
          colorScheme="teal"
        >
          Envoyer
        </Button>
      </Box>
    </Flex>
  );
}
```

Dans le code ci-dessus, nous importons les divers composants UI de la bibliothèque Chakra UI que nous allons utiliser pour construire l'entrée du formulaire.

Maintenant que nous avons créé les entrées du formulaire, concentrons-nous sur l'aspect logique : rendre l'entrée du formulaire fonctionnelle. Voici comment vous pouvez le faire :

```javascript
import { useState } from 'react';
```

Vous importez le hook `useState` (qui est un hook React) qui vous permet de déclarer/ajouter des états et de gérer les états dans un composant fonctionnel.

Le hook `useState` déclarant des états et gérant des états peut sembler un peu étrange pour vous – mais j'ai un article qui vous aidera à comprendre comment le hook `useState` fonctionne : [Voici](https://www.freecodecamp.org/news/how-to-use-the-usestate-and-useeffect-hooks-in-your-project).

Ensuite, vous devrez déclarer vos variables d'état. Voici comment vous pouvez le faire :

```javascript
const [name, setName] = useState('');
const [email, setEmail] = useState('');
const [subject, setSubject] = useState('');
const [message, setMessage] = useState('');
const [isLoading, setIsLoading] = useState(false);
const [error, setError] = useState('');
```

Dans le code ci-dessus, la variable d'état inclut des éléments comme `name`, `email`, `subject`, `message`, et ainsi de suite que nous utilisons pour stocker les entrées de l'utilisateur à partir du formulaire de contact. Ensuite, nous utilisons `setName`, `setEmail`, `setSubject`, `setMessage` et ainsi de suite pour gérer et mettre à jour l'état au cas où la valeur initiale changerait à un moment donné.

Ensuite, créez une fonction pour gérer la soumission du formulaire :

```javascript
const handleSubmit = async (e) => {
  e.preventDefault();
  setIsLoading(true);
  setError('');
```

Ici, `e.preventDefault()` aide à empêcher la page de se recharger lorsque le formulaire est soumis. `SetIsLoading(true)` montre que la soumission du formulaire est en cours. Et `setError(' ')` efface tout message d'erreur précédent qui aurait pu se produire lors de la soumission.

Ensuite, créez une fonction de validation de formulaire pour valider les formulaires d'entrée et rechercher toute erreur avant que le formulaire ne soit finalement soumis.

```javascript
if (!name || !email || !subject || !message) {
  setError('Tous les champs sont obligatoires.');
  setIsLoading(false);
  return;
}

if (!/\S+@\S+\.\S+/.test(email)) {
  setError('Format d\'email invalide.');
  setIsLoading(false);
  return;
}
```

Avant que le formulaire ne soit finalement soumis, le code ci-dessus vérifie d'abord si tous les champs d'entrée sont remplis. Si un champ est trouvé vide, il affiche une erreur et la soumission du formulaire est immédiatement arrêtée. Il en va de même pour l'email. Les emails sont organisés et tapés selon une syntaxe spécifique, et si le champ email ne suit pas cette syntaxe, une erreur est également affichée.

Ensuite, créez un objet qui stocke les informations fournies par l'utilisateur lorsqu'il remplit le formulaire. Ces informations seront envoyées au backend.

```javascript
const formData = { name, email, subject, message };
```

Maintenant, créez une fonction qui envoie vos données au backend :

```javascript
try {
  const response = await fetch("VOTRE LIEN API ICI", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(formData),
  });

  const result = await response.json();
```

La réponse `fetch` envoie les données à l'API backend. Elle utilise la méthode `post`. Lorsque les données sont envoyées au backend, elles sont envoyées sous forme de fichier `JSON`. Ensuite, les données à l'intérieur du fichier `JSON` sont toutes converties en une chaîne.

Voici à quoi cela ressemble lorsqu'il est envoyé :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1742477266973/7c1a1da7-c7f7-40bc-89f2-a26cb1f444e4.png align="center")

À ce stade, travaillons sur la gestion de la réponse de l'API ainsi que sur la gestion des erreurs :

```javascript
if (response.ok) {
      alert(result.message || 'Email envoyé avec succès !');
      setName('');
      setEmail('');
      setSubject('');
      setMessage('');
    } else {
      setError(result.error || 'Échec de l\'envoi de l\'email.');
    }
  } catch (error) {
    setError('Une erreur inattendue est survenue. Veuillez réessayer plus tard.');
  } finally {
    setIsLoading(false);
  }
```

Dans le code ci-dessus, après que l'utilisateur a correctement saisi ses informations et les a soumises, si le message est envoyé avec succès, une alerte sera affichée avec le message `Email envoyé avec succès`. Mais si le message n'a pas été envoyé avec succès – peut-être en raison de la manière dont l'utilisateur a saisi ses informations ou en raison d'une demande échouée – une alerte sera également affichée avec un message d'erreur `Échec de l'envoi de l'email`.

Pour gérer les erreurs de serveur qui pourraient survenir en raison de problèmes de réseau ou en raison de l'indisponibilité de l'API, un message d'erreur sera affiché `Une erreur inattendue est survenue. Veuillez réessayer plus tard`.

À ce stade, nous avons réussi à construire l'aspect frontend du formulaire. Nous pouvons donc maintenant nous plonger pleinement dans le backend. Continuons.

## Configuration du Backend

Pour le backend, nous allons utiliser `Node.js`, `Dotenv`, `CORS`, `Nodemailer`, et `oAuth2`.

### Configuration des bibliothèques Backend

Commençons par configurer votre serveur Node.js. Pour ce faire, vous voudrez créer un fichier dans votre dossier backend avec le nom `send-email.js`. Ensuite, dans votre dossier backend, vous créerez un fichier package.json et installerez toutes les dépendances dont vous aurez besoin.

Commencez par exécuter `npm init -y` dans votre terminal. Cela crée le fichier Package.json qui gère votre projet et stocke toutes les dépendances.

Ensuite, installons les bibliothèques que vous allez utiliser :

* `Nodemailer` permet l'envoi d'e-mails, comme vous le savez maintenant.
    
* `dotenv` charge un environnement où vous stockerez votre fichier `.env`.
    
* `cors` permet les requêtes entre le frontend et le backend.
    
* `googleapis` fournit un support d'authentification OAuth2 pour envoyer des e-mails en toute sécurité.
    

Vous pouvez les installer un par un en exécutant les commandes `npm install nodemailer`, `npm install dotenv`, `npm install cors`, et `npm install googleapis`. Ou vous pouvez les installer tous en une fois avec :

```bash
npm install nodemailer dotenv cors googleapis
```

Notez que `cors` joue un rôle important dans l'assurance d'une communication efficace entre votre serveur frontend et le backend. [Vous pouvez en apprendre plus sur CORS ici](https://www.freecodecamp.org/news/access-control-allow-origin-header-explained).

### Configuration OAuth2

Maintenant, avant de terminer la configuration de la fonction d'envoi d'e-mails, vous devez d'abord configurer `OAuth2` pour obtenir l'accès aux jetons et clés que vous utilisez, tels que `CLIENT_ID`, `CLIENT_SECRET`, `REFRESH_TOKEN`, et ainsi de suite.

Pour configurer OAuth2, [allez ici](https://console.cloud.google.com/projectselector2/home) pour visiter votre tableau de bord Google Cloud. Une fois ouvert, il devrait ressembler à ceci :

![Tableau de bord Google Cloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1742477897924/e6879a15-6835-42e8-a869-8e49b725101a.png align="center")

Sur l'écran, cliquez sur "créer un projet" et il vous emmènera à un endroit où vous pourrez créer votre projet. Cela devrait ressembler à ceci :

![Création de projet Google Cloud](https://cdn.hashnode.com/res/hashnode/image/upload/v1742477974830/bd51345f-0af8-4ad0-a912-0a59db8e3fee.png align="center")

Après avoir créé votre projet, il vous emmènera à votre tableau de bord avec le nom de votre projet affiché en haut à gauche de l'écran. Cela montre que vous avez créé votre projet avec succès.


![Tableau de bord Google Cloud après la création du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1742478101790/7fa5e621-69c2-4144-ae9c-a3bd9b59a038.png align="center")

Après avoir créé le compte, cliquez sur le bouton bascule en haut à gauche de votre écran. Lorsqu'il s'ouvre, cliquez sur le bouton APIs & Services. Un menu déroulant devrait alors s'afficher. Ensuite, cliquez sur l'écran de consentement OAuth.


![Processus Google Cloud API et Services](https://cdn.hashnode.com/res/hashnode/image/upload/v1742478459190/1af14c8f-7cff-4efa-804c-88ba19f0c47c.png align="center")

Après cela, il devrait vous diriger vers une nouvelle page où vous pourrez alors configurer votre projet.

Le processus de configuration comporte quatre étapes, que nous allons parcourir maintenant.

#### Étape 1 : Ajouter les informations de l'application

Tout d'abord, vous devrez ajouter les informations de votre application, qui incluent le nom de votre application et l'email de support utilisateur. Pour le nom de l'application, allez-y et ajoutez le nom de votre projet. Pour l'email de support, ajoutez votre adresse email et cliquez sur le bouton "Suivant". Cela devrait ressembler à ceci :

![Étape 1 de la configuration du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1742478695772/587bef4a-e1e1-4ae8-94e0-f620f4b81c79.png align="center")

#### Étape 2 : Configurer la section du public

Ensuite, vous devrez configurer la section du public. Dans cette section, choisissez l'option "Externe", ce qui signifie que d'autres personnes (pas seulement celles de l'organisation) peuvent envoyer des messages avec l'application web.


![Étape 2 de la configuration du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1742478724025/59dde0dd-e1f7-445c-9155-64926f71d746.png align="center")

#### Étape 3 : Ajouter les informations de contact

Maintenant, vous arriverez à la section des informations de contact, où vous devrez ajouter votre adresse email.

#### Étape 4 : Accepter les services Google API

Enfin, vous devrez accepter les services Google API. Après cela, vous pouvez terminer la configuration de votre projet en cliquant sur le bouton "créer".

![Étape 3 de la configuration du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1742478750231/742f0104-0631-4442-8a69-1266b433a1d1.png align="center")

Après avoir complètement configuré votre projet, il vous emmènera à une page où vous pourrez créer votre ID client. Pour le créer, cliquez sur le bouton "Créer un client OAuth" sur l'écran.

![Section Créer un client OAuth](https://cdn.hashnode.com/res/hashnode/image/upload/v1742478869578/b12e0437-ef27-4127-80fb-d8e36a2714c1.png align="center")

Cela vous emmène à un endroit où vous ajouterez les informations sur votre projet. Pour le "type de projet/application", choisissez Application web, puis faites défiler vers le bas et cliquez sur le bouton Créer.

Après cela, votre `Client ID` et votre `Client Secret` devraient enfin être générés. Voici à quoi cela ressemble :

![Génération réussie du Client ID et du Client Secret](https://cdn.hashnode.com/res/hashnode/image/upload/v1742479023599/004465be-cce9-4b20-aa32-5a4f676f4d03.png align="center")

Ensuite, rendez-vous sur le [OAuth Playground](https://developers.google.com/oauthplayground/) où vous terminerez la configuration finale. Une fois là-bas, cliquez sur le bouton d'engrenage en haut à droite de l'écran. Là, ajoutez simplement votre `client ID` et `Client Secret` que vous avez générés précédemment.

![Étape 1 du processus de génération du token de rafraîchissement](https://cdn.hashnode.com/res/hashnode/image/upload/v1742479184829/7885b38b-de54-46fb-9c0d-a0739110dd98.png align="center")

Ensuite, à gauche, faites défiler jusqu'à "Gmail API v1", cliquez dessus, et sélectionnez la première option du menu déroulant qui était "[https://mail.google.com/](https://mail.google.com/)". Ensuite, cliquez sur "Autoriser les APIs".

![Étape 2 du processus de génération du token de rafraîchissement](https://cdn.hashnode.com/res/hashnode/image/upload/v1742479467364/2f04e0ac-3514-4bc4-b16f-cf163770a5c5.png align="center")

Cela vous emmènera à une page de connexion avec Google, où vous pourrez choisir votre compte email et continuer.

![Étape 3 du processus de génération du token de rafraîchissement](https://cdn.hashnode.com/res/hashnode/image/upload/v1742479538105/c3470cfa-5867-40a2-a2bc-122334efa752.png align="center")

Ensuite, vous serez redirigé vers le tableau de bord OAuth Playground. À ce stade, votre code d'autorisation a été généré pour vous, mais ce dont vous avez vraiment besoin est le `Refresh token`. Donc pour l'obtenir, cliquez sur `Exchange authorization code for tokens`. Après cela, votre `refresh token` devrait être généré.

![Étape finale du processus de génération du token de rafraîchissement](https://cdn.hashnode.com/res/hashnode/image/upload/v1742479669946/76b6b4a3-1929-4354-abb2-a7f514e04c20.png align="center")

À ce stade, votre configuration OAuth2 est terminée ! Maintenant, il ne reste plus qu'à stocker tous les jetons que vous avez générés dans un fichier `.env` que vous avez créé. Vous devrez également configurer votre fonction d'envoi d'e-mails en utilisant `NodeMailer`.

### Configuration de `Nodemailer`

Maintenant que vous avez obtenu tous les jetons nécessaires pour créer votre fonction d'envoi d'e-mails, il ne reste plus qu'à commencer à assembler votre code backend.

Tout d'abord, commencez par charger votre fichier `.env` dans `process.env` afin de pouvoir accéder facilement à tous les jetons que vous avez générés. Importez également les bibliothèques que vous avez initialement installées.

```javascript
require("dotenv").config();
const nodemailer = require("nodemailer");
const cors = require("cors");
const { google } = require("googleapis");
```

Ensuite, vous devrez configurer OAuth2. Ici, le `client ID` et le `client Secret` que vous avez initialement générés seront utilisés pour authentifier l'application et demander et créer des jetons d'accès de manière sécurisée. Ceux-ci seront utilisés pour envoyer des e-mails de manière transparente via les API Google.

Vous devrez également configurer le jeton de rafraîchissement qui permet à l'application d'obtenir de nouveaux jetons d'accès automatiquement sans nécessiter d'interaction de l'utilisateur.

```javascript
const oAuth2Client = new google.auth.OAuth2(
  process.env.CLIENT_ID,
  process.env.CLIENT_SECRET,
  process.env.REDIRECT_URI
);

//configuration du jeton de rafraîchissement.
oAuth2Client.setCredentials({
  refresh_token: process.env.OAUTH_REFRESH_TOKEN,
});
```

Puisque nous voulons que le frontend interagisse correctement avec le backend, vous voudrez configurer un `CORS Middleware`. Cela permet les requêtes de n'importe quelle origine (`\*`) ainsi que les requêtes POST de cette origine. Voici comment vous pouvez le faire :

```javascript
const corsMiddleware = cors({ origin: "*", methods: ["POST"] });
```

Ensuite, créez une fonction pour gérer `CORS` et la méthode de requête. Cette fonction applique le `CORS` middleware à la requête de telle sorte que si la méthode de requête est `OPTIONS`, elle répond avec un `200 status (preflight OK)`. Cela signifie que votre requête a été approuvée/autorisée par le serveur car elle a respecté les règles définies par le serveur. Si la méthode de requête n'est pas `POST`, une réponse de `405 status (Method not allowed)` sera affichée, indiquant que votre requête ne respecte pas la règle définie par le serveur.

Voici comment cela se fait :

```javascript
corsMiddleware(req, res, async () => {
  if (req.method === "OPTIONS") {
    return res.status(200).send("Preflight OK");
  }

  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }
```

Ensuite, créez une fonction qui extrait et valide la requête d'entrée. Cette requête contient le `name`, `email`, `subject`, et `message` de l'expéditeur. Cette fonction garantit que tous les champs d'entrée doivent être remplis et que l'email doit également être écrit correctement. Sinon, elle répond avec une erreur `400 status`.

```javascript
const { name, email, subject, message } = req.body;

// Valider l'entrée
if (!name || !email || !subject || !message) {
  return res.status(400).json({ error: "Tous les champs sont obligatoires." });
}

if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
  return res.status(400).json({ error: "Adresse email invalide." });
}
```

Ensuite, vous créerez une fonction qui aide à récupérer de nouveaux jetons d'accès. Vous créerez également une fonction de transporteur Nodemailer. Ce transporteur a été configuré pour utiliser le service SMTP de Gmail avec l'authentification OAuth2.

Cela signifie que chaque fois qu'un utilisateur envoie un email, la fonction de transporteur vérifie d'abord si le service SMTP de Gmail est prêt. Si c'est le cas, l'email sera d'abord vérifié avec OAuth2, et si la vérification d'authentification est réussie, l'email sera livré avec succès.

```javascript
//Fonction pour récupérer un nouveau jeton d'accès
const accessToken = await oAuth2Client.getAccessToken();
if (!accessToken || !accessToken.token) {
  throw new Error("Échec de la récupération du jeton d'accès.");
}
console.log("Jeton d'accès récupéré avec succès.");

/// Création de la fonction de transporteur Nodemailer
const transporter = nodemailer.createTransport({
  service: "gmail",
  auth: {
    type: "OAuth2",
    user: process.env.EMAIL_HOST,
    clientId: process.env.CLIENT_ID,
    clientSecret: process.env.CLIENT_SECRET,
    refreshToken: process.env.OAUTH_REFRESH_TOKEN,
    accessToken: accessToken.token,
  },
  debug: true,
  logger: true,
});

///La fonction vérifiant si le serveur SMTP est prêt
await transporter.verify();
console.log("Le serveur SMTP est prêt à envoyer des emails.");
```

Enfin, vous voudrez structurer votre email dans le format dans lequel il doit être affiché dans la boîte de réception du destinataire. Vous créerez également une fonction de gestion des erreurs qui s'affiche chaque fois qu'un email est envoyé avec succès ou chaque fois qu'une erreur se produit.

```javascript
const mailOptions = {
        from: `"${name}" <${email}>`, 
        to: process.env.EMAIL_RECEIVE,
        replyTo: email,
        subject,
        html: `
          <h1>Nom : ${name}</h1>
          <p>Email : ${email}</p>
          <p>Sujet : ${subject}</p>
          <p>Message : ${message}</p>
          <p><i>Message du site web Exesenergy</i></p>
        `,
      };
      console.log("Options de mail :", mailOptions);

      // Envoyer l'email
      await transporter.sendMail(mailOptions);
      console.log("Email envoyé avec succès.");

      return res
        .status(200)
        .json({ status: "success", message: "Email envoyé avec succès." });
    } catch (error) {
      console.error("Détails de l'erreur :", error);
      return res
        .status(500)
        .json({ error: "Erreur interne du serveur", details: error.message });
    }
```

À ce stade, vous avez configuré avec succès vos applications frontend et backend. Maintenant, vous pourriez vouloir les héberger. J'ai décidé d'héberger les deux applications en utilisant Vercel et de lier leurs URLs ensemble.

Voici le code source pour accéder au [frontend](https://github.com/Derekvibe/ExesEnergyFrontend) et au [backend](https://github.com/Derekvibe/ExesEnergyBackend/blob/main/api/send-email.js).

Voici le résultat final :

![Représentation vidéo de comment la fonction d'envoi de mail fonctionne](https://cdn.hashnode.com/res/hashnode/image/upload/v1742476641876/69f5123a-570f-4e1a-bbed-6278b54fed7a.gif align="center")

## **Conclusion**

Nodemailer est un module populaire de Node.js qui permet à ses utilisateurs d'envoyer des e-mails efficacement en utilisant différentes méthodes comme SMTP et OAuth2.

Si vous êtes arrivé jusqu'ici, j'espère avoir réussi à vous montrer l'importance de Nodemailer et comment vous pouvez l'utiliser pour envoyer des messages électroniques directement depuis votre site web.

Merci d'avoir lu !