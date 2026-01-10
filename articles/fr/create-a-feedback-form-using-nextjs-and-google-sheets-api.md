---
title: Comment créer un formulaire de feedback en utilisant l'API Google Sheets
subtitle: ''
author: Georgey V B
co_authors: []
series: null
date: '2021-09-21T17:44:05.000Z'
originalURL: https://freecodecamp.org/news/create-a-feedback-form-using-nextjs-and-google-sheets-api
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/Build-a-feedback-form-using-Google-Sheets-API.png
tags:
- name: api
  slug: api
- name: forms
  slug: forms
- name: google sheets
  slug: google-sheets
seo_title: Comment créer un formulaire de feedback en utilisant l'API Google Sheets
seo_desc: 'Google Sheets provide a simple way to create online forms and gather data
  from users. In this tutorial we will use Google Sheets and Next.js to build a simple
  form.

  We''ll use Next.js as our front end, and we''ll use Google Sheets as the back end
  to se...'
---

Google Sheets offre une manière simple de créer des formulaires en ligne et de collecter des données auprès des utilisateurs. Dans ce tutoriel, nous allons utiliser Google Sheets et Next.js pour construire un formulaire simple.

Nous utiliserons Next.js comme front-end et Google Sheets comme back-end pour envoyer les données que nous recevons via un formulaire. Ainsi, nous pouvons apprendre à utiliser Next.js et Google Sheets pour construire un formulaire simple.

Voici ce que nous allons couvrir dans ce tutoriel :

1. Comment configurer un nouveau projet dans Google Cloud Console
2. Comment connecter le nouveau projet à une feuille Google Sheets
3. Comment créer un formulaire front-end dans une application Next.js
4. Comment connecter le formulaire à la feuille Google Sheets

> Pour vous aider à suivre, j'ai créé un [dépôt GitHub](https://github.com/GeoBrodas/nextjs-form-using-google-sheets-api). Si vous vous perdez, n'hésitez pas à y jeter un coup d'œil.

# Comment configurer un nouveau projet dans Google Cloud Console

Pour accéder à l'API Google Sheets, nous devons d'abord configurer un nouveau projet sur Google Cloud Console. Rendez-vous sur le [site](https://cloud.google.com), allez dans la [console](https://console.cloud.google.com) et créez un nouveau projet.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/cloud-new.png)

Après la création du nouveau projet, allez dans **APIs et Services** et cliquez sur **Activer les APIs et Services**.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/cloud-enable.png)

Recherchez Google Sheets dans la bibliothèque et activez-le.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/enable-sheets-api.png)

Maintenant, allez dans APIs et Services, puis **Identifiants** et cliquez sur **Nouvel identifiant**. Créez un nouveau compte de service.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/create-cred.png)

Donnez-lui un nom approprié et remplissez tous les détails. Après avoir généré le compte de service, copiez l'adresse e-mail quelque part. Nous devrons l'ajouter à notre feuille Google Sheets par la suite. Nous venons de créer un compte Bot pour gérer les différentes requêtes qui seront envoyées depuis le front-end.

Ensuite, cliquez sur le compte de service dans **Identifiants** puis allez dans **Clés**. Cliquez sur **Ajouter une clé**. Assurez-vous de la définir au format JSON.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/google_key.png)

Un fichier sera téléchargé lors de la création de la nouvelle clé. Il contient toutes les variables d'environnement dont nous avons besoin pour connecter notre application front-end à Google Sheets.

# Comment connecter le nouveau projet à une feuille Google Sheets

Maintenant, connectons le projet nouvellement créé sur Google Cloud Console à une feuille Google Sheets. Rendez-vous sur [Google Sheets](http://sheets.google.com/) et créez une nouvelle feuille de calcul.

Avant de continuer, n'hésitez pas à ajouter quelques données brutes afin d'avoir quelque chose à récupérer lors de l'appel des requêtes dans la section suivante.

Une fois cela fait, cliquez sur Partager et ajoutez l'e-mail du compte de service que nous venons de créer. Assurez-vous de lui donner un **accès Éditeur** et décochez **Notifier les personnes**.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/share.png)

Maintenant, passons à la partie amusante. Allons dans l'éditeur de code et créons le front-end pour notre formulaire.

# Comment créer le formulaire front-end

Pour construire le front-end, nous utiliserons Next.js et la fonctionnalité API-routes pour envoyer une requête POST à notre feuille Google Sheets.

Installez Next en utilisant cette commande :

```bash
npx create-next-app
```

Pour construire le formulaire et accélérer le processus de développement, nous utiliserons quelques packages tiers. Alors, allez-y et installez les suivants :

```bash
npm i @chakra-ui/react @emotion/react@^11 @emotion/styled@^11 framer-motion@^4 react-hook-form
```

* Chakra-UI : un framework accessible qui m'a personnellement aidé à accélérer la conception front-end de la plupart de mes applications.
* React-Hook-Form : vous aide à construire des formulaires efficaces avec une validation côté client à la volée.

Dans ce tutoriel, je me concentrerai davantage sur l'exécution de la fonctionnalité du formulaire plutôt que sur la construction de la validation côté client. [Voici](https://react-hook-form.com/get-started#Applyvalidation) un guide complet sur l'ajout de la validation côté client en utilisant [React-Hook-Form](https://react-hook-form.com/). Bien sûr, n'hésitez pas à consulter la [documentation de Chakra-UI](https://chakra-ui.com/docs/getting-started) également.

Après avoir installé tous les packages, ouvrez-le avec n'importe quel éditeur de code. Dans Next.js, chaque fichier que vous créez dans le dossier `/pages` est une route individuelle. Vous pouvez en créer une nouvelle, mais ici j'utiliserai le fichier racine lui-même, c'est-à-dire `/pages/index.js`.

Effacez toutes les lignes de code pré-générées. Maintenant, créons une structure de base pour le formulaire.

```js
import { VStack, Text, Input } from "@chakra-ui/react"

function Home () {
    function submitHandler () {
     // Requête POST
    }
    
    return (
        <VStack>
          <Text fontSize="2xl" fontWeight="bold">
            Votre réponse compte !
          </Text>
          
          <form onSubmit={submitHandler}>
              <Input placeholder="Entrez votre nom" />
              <Button>Soumettre !</Button>
          </form>
        </VStack>
    )
}
```

VStack enveloppe tous les éléments verticalement. C'est un raccourci facile pour `flex-direction: column`. Le reste du code devrait être assez explicite.

La beauté de Chakra-UI est que chacun de ses composants ressemble étroitement aux éléments HTML réels, réduisant ainsi la courbe d'apprentissage.

Vous pouvez ajouter d'autres champs de saisie de votre choix. Voici le résultat final :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/form.png)

Maintenant, gérons la réponse du formulaire lorsque l'utilisateur le soumet. Pour cela, nous utiliserons `react-hook-form`.

Pour obtenir la réponse du formulaire, nous devons importer le hook `useForm`, comme ceci :

```js
import { useForm } from 'react-hook-form';
```

À partir du hook, déstructurez ce qui suit :

```js
const {
    register,
    handleSubmit
  } = useForm();
```

Enveloppez le `submitHandler` que nous avons créé précédemment avec `handleSubmit` :

```js
<form onSubmit={handleSubmit(submitHandler)}>
   {/* Champs de saisie ici */}               
</form>
```

Maintenant, ajoutez `register` à tous les champs de saisie comme suit :

```js
<Input placeholder="Entrez votre message" {...register('name') />
```

Maintenant, lorsque le bouton est cliqué, nous devrions pouvoir voir les données saisies. Pour l'instant, enregistrez simplement les données dans la console comme suit :

```js
function submitHandler (data) {
	console.log(data);
}
```

Cela fait, créons maintenant une nouvelle route API pour la requête POST à envoyer depuis le formulaire.

# Comment connecter le formulaire à la feuille Google Sheets

Créez un nouveau fichier dans la route `./pages/api/`. Chaque fichier que vous créez dans cette route est une route API, qui donne accès à toutes les fonctionnalités de Node.js.

Allez-y et créez un nouveau fichier dans la route, disons `./pages/api/sheet.js`. Structurez une requête GET de base pour voir si tout fonctionne bien :

```js
function handler (req, res) {
	res.json({message: "Ça marche !"});
}

export default handler;
```

Pour vérifier si la requête API fonctionne à ce stade, allez sur `http://localhost:3000/api/sheet`.

Cela fait, configurons d'abord la requête POST à envoyer depuis le front-end en utilisant la méthode native `Fetch`.

```js
async function submitHandler (data) {
	const response = await fetch("/api/sheet", {
    		method: "POST",
        	body: JSON.stringify(data),
        	headers: {
        		'Content-Type': 'application/json',
      		},
    	})
}
```

Avant de faire autre chose, nous devons télécharger un autre package :

```bash
npm install googleapis
```

Dans la route API (`/pages/api/sheet`), déstructurez les données que nous recevons du front-end.

```js
import {google} from "googleapis"

async function handler (req, res) {
    if (req.method === "POST"){
    		const {name, message} = req.body;
		res.json({message: "Ça marche !"});
    }
}

export default handler;
```

Note : Les routes API écouteront par défaut une requête GET. Nous devons donc vérifier explicitement si la méthode est une requête POST.

Avant de continuer, il y a une dernière chose à configurer, et ce sont les variables d'environnement. Ouvrez le fichier JSON contenant toutes les informations d'identification lorsque nous avons créé la nouvelle clé.

Créez un nouveau fichier `.env.local` à la racine. Allez-y et entrez les variables suivantes.

```env
CLIENT_EMAIL=votreclientemail
CLIENT_ID=votreclientid
PRIVATE_KEY=votreprivatekey
SPREADSHEET_ID=votreidfeuillecalc
```

Cela fait, nous avons presque terminé la configuration de la route API pour gérer la requête que nous allons envoyer à notre feuille Google Sheets. Tout d'abord, créons un jeton d'authentification :

```js
const auth = new google.auth.GoogleAuth({
    credentials: {
      client_email: process.env.CLIENT_EMAIL,
      client_id: process.env.CLIENT_ID,
      private_key: process.env.PRIVATE_KEY.replace(/\\n/g, '\n'),
    },
    scopes: [
      'https://www.googleapis.com/auth/drive',
      'https://www.googleapis.com/auth/drive.file',
      'https://www.googleapis.com/auth/spreadsheets',
    ],
  });
```

Pour accéder à la feuille Google Sheets, notre application doit d'abord fournir quelques portées – généralement des accès en lecture et en écriture.

Vous pouvez en savoir plus sur les portées dans la [documentation officielle de Google Sheets](https://developers.google.com/sheets/api/guides/authorizing).

Vous vous demandez peut-être pourquoi j'ai utilisé la méthode `replace` dans la troisième variable d'environnement. Cela était dû à une erreur typique que je rencontrais auparavant. Après avoir parcouru Stack Overflow, j'ai finalement trouvé la solution. Il semble que la `PRIVATE_KEY` doive être correctement analysée en supprimant les barres obliques de la clé originale. Cela peut être facilement résolu en utilisant la méthode `replace`.

Vous pouvez trouver plus d'informations sur cette erreur dans cette [demande de tirage](https://github.com/leerob/leerob.io/pull/342) que j'ai ouverte.

Ensuite, passez le jeton d'authentification et spécifiez la version de l'API. La dernière est la v4.

```js
const sheets = google.sheets({
    auth,
    version: 'v4',
  });
```

Ensuite, nous appelons la méthode `spreadsheets.value.append` pour ajouter l'entrée de l'utilisateur dans les cellules de la feuille de calcul.

```js
const response = await sheets.spreadsheets.values.append({
      spreadsheetId: process.env.DATABASE_ID,
      range: 'Sheet1!A2:C',
      valueInputOption: 'USER_ENTERED',
      requestBody: {
        values: [[name, message]],
      },
    });
```

Vous pouvez trouver l'ID de la feuille de calcul dans l'URL elle-même :

```url
https://docs.google.com/spreadsheets/d/{spreadsheetID}/edit#gid=0
```

La plage détermine quelles lignes et colonnes l'application doit lire ou écrire. Si vous êtes confus sur la façon de trouver la plage, vous pouvez la déterminer en utilisant Google Sheets lui-même via l'interface utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/select_range.png)

La troisième propriété, `valueInputOption`, détermine comment la valeur saisie par l'utilisateur doit être analysée dans la feuille de calcul.

Par exemple, si l'utilisateur a saisi un nombre, la feuille de calcul le lira également comme un nombre.

La quatrième propriété contient les données à ajouter dans une cellule particulière. Pour ajouter plusieurs valeurs, vous pouvez tout mettre dans un tableau, comme dans ce cas – nom et message.

Pour terminer la route API, envoyez enfin une réponse au front-end :

```js
res.status(201).json({response, result: "Feedback posté dans la feuille de calcul !"})
```

Si tout se passe bien, vous devriez pouvoir faire une requête POST et ajouter avec succès une nouvelle valeur de cellule dans la feuille de calcul.

# Conclusion

Félicitations ! Vous êtes prêt à commencer à collecter des feedbacks. Vous pourriez créer votre propre formulaire de feedback sur votre site web. Ou vous pourriez vous intégrer à un service existant comme Typeform.

Mais vous voulez garder votre formulaire de feedback sur votre site, sur votre page. C'est là que l'intégration avec l'API Google Sheets est utile.

L'API Google Sheets est assez basique – elle peut lire et écrire dans des feuilles de calcul. De plus, elle est complètement gratuite, bien qu'il y ait une limitation sur les requêtes API que vous pouvez faire dans un laps de temps particulier.

Ainsi, l'API Google Sheets serait idéale pour les applications et plateformes à petite échelle avec un public plus restreint. Si vous avez des questions, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/BrodasGeo).