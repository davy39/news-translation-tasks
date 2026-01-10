---
title: Comment générer des images en utilisant React et l'API Dall-E 2 – Tutoriel
  React et API OpenAI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-08T20:22:16.000Z'
originalURL: https://freecodecamp.org/news/generate-images-using-react-and-dall-e-api-react-and-openai-api-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Important-Concepts-and-questions--1-.png
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: image
  slug: image
seo_title: Comment générer des images en utilisant React et l'API Dall-E 2 – Tutoriel
  React et API OpenAI
seo_desc: "By Nishant Kumar\nHey everyone! OpenAI just released its DALL-E API where\
  \ users can generate custom images by just typing in a query. \nSo in this tutorial,\
  \ you'll learn how to integrate the OpenAI DALL-E 2 API with a React app.\nBut First,\
  \ How Does Dal..."
---

Par Nishant Kumar

Salut à tous ! OpenAI vient de publier son API DALL-E où les utilisateurs peuvent générer des images personnalisées en tapant simplement une requête. 

Dans ce tutoriel, vous apprendrez donc à intégrer l'API OpenAI DALL-E 2 avec une application React.

## Mais d'abord, comment fonctionne Dall-E ?

Comme vous le savez déjà, vous devez taper une requête – quelque chose comme **Des ours avec des pinceaux dans la Nuit étoilée, peints par Vincent Van Gogh**. Cela contient de nombreux mots-clés, comme Pinceaux, Nuit étoilée et Vincent Van Gogh.

Ce que Dall-E fera, c'est rechercher ces images qui sont liées aux mots-clés que je viens de mentionner ci-dessus. Ensuite, il utilisera l'intelligence artificielle pour fusionner toutes les images en une seule, puis nous la servira.

Maintenant, apprenons comment vous pouvez intégrer cela dans votre application React pour créer votre propre application avec ces fonctionnalités incroyables.

## Comment créer une application React

Alors, créez une application React. Vous pouvez la créer avec la commande CRA (create-react-app) ou utiliser Vite.

Nous avons besoin d'un champ de texte et d'un bouton comme composants UI. Le champ de texte sera utilisé pour obtenir la requête de l'utilisateur et le bouton pour déclencher la requête API. Créons également un état pour stocker la requête et une fonction qui s'exécutera au clic sur le bouton.

```
import { useState } from "react";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");

  const generateImage = async () => {};

  return (
    <div className="app-main">
      <>
        <h2>Générer une image en utilisant l'API Open AI</h2>

        <textarea
          className="app-input"
          placeholder="Rechercher des ours avec des pinceaux dans la Nuit étoilée, peints par Vincent Van Gogh.."
          onChange={(e) => setPrompt(e.target.value)}
          rows="10"
          cols="40"
        />
        <button onClick={generateImage}>Générer une image</button>
      </>
    </div>
  );
}

export default App;

```

Notre sortie ressemblera à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-05-212826.png)

### Comment intégrer l'API DALL-E 2 avec l'application React

Voyons comment nous pouvons intégrer l'API DALL-E 2 dans notre application.

Tout d'abord, nous devons aller sur le site [OpenAI](https://beta.openai.com). Vous devez vous inscrire pour générer une clé API. Vous recevrez également 18 $ sur votre compte que vous pourrez utiliser.

Choisissez que vous créez une application pendant votre inscription.

Une fois que vous avez créé votre compte, allez dans la section View API Keys, où vous pouvez créer votre clé API unique. Voir l'image ci-dessous pour référence.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-05-213523.png)

Maintenant, dans votre application React, créez un fichier **.env**. Cela sert à stocker la clé API.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-05-213733.png)

Ajoutez votre clé API là. Notez que la méthode pour obtenir la clé à partir des fichiers .env est différente dans CRA et Vite React App. Gardez cela à l'esprit. J'utilise Vite, donc voici comment nous le faisons :

```
VITE_Open_AI_Key = "Votre clé API"
```

Maintenant que la clé API est ajoutée, nous devons importer quelques éléments dans notre fichier App.js ou App.jsx. Cela inclut la **Configuration** et **OpenAIApi** du **SDK openai**. Mais d'abord, nous devons installer le **SDK openai** dans l'application React.

Pour l'installer, tapez simplement la commande ci-dessous :

```
npm install openai
```

Cela peut prendre un certain temps pour s'installer. Ensuite, importez les deux éléments que nous avons mentionnés précédemment comme ceci :

```
import { Configuration, OpenAIApi } from "openai";
```

Nous devons créer une variable de configuration, qui prendra la clé API du fichier .env.

```
const configuration = new Configuration({
	apiKey: import.meta.env.VITE_Open_AI_Key,
});
```

Maintenant, nous devons passer cette instance de configuration à OpenAIApi, et créer une nouvelle instance pour OpenAIApi.

```
const openai = new OpenAIApi(configuration);
```

Voici le code complet jusqu'à présent :

```
import { Configuration, OpenAIApi } from "openai";

import { useState } from "react";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const configuration = new Configuration({
    apiKey: import.meta.env.VITE_Open_AI_Key,
  });

  const openai = new OpenAIApi(configuration);
  

  return (
    <div className="app-main">
      <>
        <h2>Générer une image en utilisant l'API Open AI</h2>

        <textarea
          className="app-input"
          placeholder="Rechercher des ours avec des pinceaux dans la Nuit étoilée, peints par Vincent Van Gogh.."
          onChange={(e) => setPrompt(e.target.value)}
          rows="10"
          cols="40"
        />
        <button onClick={generateImage}>Générer une image</button>
      </>
    </div>
  );
}

export default App;

```

Maintenant, dans la fonction **generateImage**, nous devons appeler l'instance OpenAIApi que nous avons créée précédemment. N'oubliez pas que la fonction doit être asynchrone.

```
const generateImage = async () => {
    await openai.createImage({
      prompt: prompt,
      n: 1,
      size: "512x512",
    });
  };
```

Comme vous pouvez le voir, nous utilisons **openai.createImage**. Cette API est utilisée pour créer une image en utilisant une requête utilisateur. Elle prend également **n**, qui est le nombre d'images que nous voulons que l'API retourne, et la **taille de l'image**. 

Il existe trois tailles d'images différentes avec des prix différents, qui sont listés ci-dessous. Si vous utilisez la taille 1024x1024, cela vous coûtera 0,020 $ par image.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-05-215314.png)

Maintenant, cette fonction **openai.createImage** retourne une réponse que nous pouvons stocker dans une variable. Nous pouvons ensuite obtenir le lien de l'image générée à partir de la variable de réponse.

```
const generateImage = async () => {
    const res = await openai.createImage({
      prompt: prompt,
      n: 1,
      size: "512x512",
    });

    console.log(res.data.data[0].url);
  };
```

Mais ne faisons pas cela. Créons un état supplémentaire pour stocker ce lien d'image afin que nous puissions voir l'image dans l'UI elle-même.

```
const [result, setResult] = useState("");

const generateImage = async () => {
    const res = await openai.createImage({
      prompt: prompt,
      n: 1,
      size: "512x512",
    });

    setResult(res.data.data[0].url);
  };
```

Maintenant, le lien de l'image sera stocké dans l'état **result**. Affichons également l'image dans l'UI. Mais comme le résultat est initialement vide, nous pouvons créer une vérification. Nous ne verrons la balise image que s'il y a un lien dans l'état.

```
{result.length > 0 ? (
          <img className="result-image" src={result} alt="result" />
        ) : (
          <></>
        )}
```

Et voici aussi le style :

```
.result-image {
  margin-top: 20px;
  width: 350px;
}
```

L'UI ressemblera maintenant à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-05-220108.png)

Tapons quelque chose et voyons le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-05-220222.png)

Dans l'exemple ci-dessus, j'ai tapé **Un cheval sur la plage avec des sables rouges.** Et voici le résultat.

Essayons quelque chose de plus complexe, comme **Des ours avec des pinceaux dans la Nuit étoilée, peints par Vincent Van Gogh.** 

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-05-220423.png)

C'est ainsi que vous le faites. Vous pouvez taper n'importe quelle requête et elle générera cette image grâce à l'intelligence artificielle. 

## Conclusion

Et c'est tout, les amis. Maintenant, vous savez comment créer votre propre application React avec l'API DALL-E 2 pour générer des images en utilisant l'IA. Il y a beaucoup plus de fonctionnalités que vous pouvez ajouter. Alors, allez-y et expérimentez un peu.

Si vous voulez voir la version vidéo de ceci, consultez ma vidéo sur [Générer des images en utilisant React et l'API Dall-E - Tutoriel React et API OpenAI](https://youtu.be/oacBV4tnuYQ) sur ma chaîne YouTube [Cybernatico](https://www.youtube.com/c/CybernaticoByNishant).

Consultez le code sur [GitHub](https://github.com/nishant-666/Dall-E-API-with-React) pour référence.

> Bon apprentissage.