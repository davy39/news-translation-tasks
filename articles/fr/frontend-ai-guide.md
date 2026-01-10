---
title: Comment créer des applications IA – Un guide pour les développeurs frontend
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-01-23T22:05:41.000Z'
originalURL: https://freecodecamp.org/news/frontend-ai-guide
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Mojito-Cocktail-Recipe-Blog-Banner--1-.png
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Front-end Development
  slug: front-end-development
seo_title: Comment créer des applications IA – Un guide pour les développeurs frontend
seo_desc: 'By Mahmud Adeleye

  Artificial Intelligence: The New Frontier for Frontend Developers

  The demand for AI-powered applications is growing at a fast pace. As a front-end
  developer, you can take advantage of this trend and advance your career by integratin...'
---

Par Mahmud Adeleye

## L'intelligence artificielle : La nouvelle frontière pour les développeurs frontend

La demande d'applications alimentées par l'IA croît à un rythme rapide. En tant que développeur frontend, vous pouvez tirer parti de cette tendance et faire progresser votre carrière en intégrant vos compétences en développement frontend avec les technologies d'IA. 

Cette intégration vous permet de créer des applications intelligentes qui améliorent les expériences utilisateur et fournissent des informations précieuses qui peuvent avoir un impact positif sur les décisions d'un utilisateur.

Pour souligner les opportunités passionnantes qui existent actuellement, considérons ces statistiques :

1. En 2023, [plus de 60 % des startups acceptées dans le prestigieux Y Combinator](https://www.theinformation.com/articles/what-we-can-learn-from-ai-startups-in-y-combinators-latest-batch) étaient axées sur l'IA.
2. Malgré un [ralentissement des investissements mondiaux, le financement des startups IA a augmenté et atteint un impressionnant 50 milliards de dollars en 2023.](https://news.crunchbase.com/venture/global-funding-data-analysis-ai-eoy-2023/)

Dans ce guide, nous aborderons les points suivants :

1. Le rôle des développeurs frontend dans l'avancement de l'innovation IA.
2. Les étapes clés à suivre lors de l'intégration des services IA dans votre flux de travail frontend.
3. Comment garantir les performances et la sécurité optimales des applications IA que vous créez.
4. Enfin, nous incorporerons les conseils des points 1-3 pour créer un AI Website Critic capable d'analyser vos sites web et applications de portfolio en utilisant React et le modèle GPT4-Vision d'OpenAI.

## Prérequis

- Connaissance de HTML
- Compréhension de base des hooks React
- Node et npm installés sur votre ordinateur local.

## Le rôle des développeurs frontend dans la création d'expériences pilotées par l'IA

Les développeurs frontend jouent un rôle crucial dans la création d'expériences pilotées par l'IA en tirant parti de leur expertise en conception d'interface utilisateur, en visualisation de données et en implémentation technique. 

Ils sont responsables de la création de l'interface utilisateur, de la conception des flux d'interaction et de l'intégration des fonctionnalités IA de manière transparente dans l'application. 

Les développeurs frontend collaborent également avec les développeurs backend et les scientifiques des données pour garantir le fonctionnement efficace et précis des algorithmes IA.

De plus, les développeurs frontend jouent un rôle critique dans les performances des applications web qui exploitent les derniers modèles d'IA. Ils sont responsables de l'optimisation des performances de l'application, de la garantie de la compatibilité multiplateforme et de la mise en œuvre de conceptions réactives qui s'adaptent à différents appareils et tailles d'écran.

## Comment intégrer les services IA dans votre flux de travail frontend

Pour intégrer les services IA dans votre flux de travail frontend, vous devez suivre une approche systématique qui comprend ces étapes :

1. Identifier la tâche ou le problème que les capacités IA peuvent résoudre ou améliorer.
2. Rechercher et évaluer les entreprises IA qui fournissent des API et des SDK node pour les capacités IA spécifiques requises pour la tâche ou le problème que vous avez identifié. En comprenant les offres de différentes entreprises IA, vous pouvez choisir les services IA les plus adaptés à intégrer dans vos applications. 

Examinons quelques modèles d'IA populaires et leurs tâches principales :

| Modèle d'IA | Tâche |
| --- | --- |
| GPT-4 | Modèle multimodal (capable de texte, image, etc.) |
| Stable Diffusion | Modèle génératif de texte à image |
| Mistral 7B | Modèle multimodal (capable de texte, image, etc.) |
| Voicebox | Modèle génératif de parole |
| DALL·E 3 | Modèle génératif de texte à image |

Vous pouvez explorer davantage de ces modèles sur les pages [Replicate Explore](https://replicate.com/explore) et [Huggingface explore models](https://huggingface.co/models).

3. Intégrer les services IA sélectionnés dans votre application frontend en tirant parti des API et des SDK node fournis. Cela implique de comprendre la documentation et les directives que les entreprises IA offrent pour garantir une intégration transparente et une utilisation appropriée des capacités IA.
4. Tester et valider les services IA intégrés dans votre application frontend pour garantir un fonctionnement précis et efficace. Cette étape est cruciale pour identifier et résoudre les problèmes techniques ou les exigences d'optimisation.

Il est également important de concevoir avec empathie en fournissant des explications et des visualisations claires, donnant aux utilisateurs un sentiment de contrôle et de propriété sur les résultats générés par l'IA. 

### Exemple d'application

Passons en revue un exemple. Supposons que vous souhaitiez créer un générateur de mèmes personnalisé. Dans ce cas, vous devriez rechercher des modèles d'IA spécifiquement entraînés pour travailler avec des images, tels que Stable Diffusion de Stability et DALL·E 3 d'OpenAI.

Après cela, vous pouvez explorer les meilleures API et SDK que vous pouvez utiliser pour tirer parti de ces modèles d'IA et créer un exemple de base. 

Pour illustrer, utilisons le SDK Node Replicate, qui fournit une méthode pratique pour interagir avec le modèle d'IA Stable Diffusion et configurer un programme Node.js de base que nous pourrons ensuite intégrer dans notre application React.

Étape 1. Obtenez votre jeton depuis https://replicate.com/account
Étape 2 : Installez le SDK Node avec la commande npm : `npm install replicate`
Étape 3 : Interrogez le modèle d'IA Stable Diffusion via le SDK replicate.
```
const Replicate = require("replicate");
const replicate = new Replicate({
  
  auth: "", // par défaut process.env.REPLICATE_API_TOKEN
});

async function iLoveCats(){
    const model = "stability-ai/stable-diffusion:27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478";
  const input = {
    prompt: "un chat portant un costume",
  };
  const output = await replicate.run(model, { input });
  console.log(output[0]);
  
}

iLoveCats()
```

Lorsque vous journalisez la sortie, vous obtenez une URL d'image que vous pouvez facilement afficher dans votre application frontend. `https://replicate.delivery/pbxt/ng6Tb0HNdzYwFZXMNv3qmIBxc2GIwU4t7edephtDvuWZ5wNSA/out-0.png`

<figure>
    <img src="https://www.freecodecamp.org/news/content/images/2024/01/catsuit.png"
         alt="Un chat en costume">
    <figcaption>Un chat en costume.</figcaption>
</figure>

## Comment optimiser les performances et la sécurité dans les applications frontend pilotées par l'IA

Optimiser les performances et la sécurité dans les applications frontend pilotées par l'IA est essentiel pour créer une expérience utilisateur fluide et pour la protection des données également. 

Heureusement, les techniques listées ci-dessous sont similaires aux pratiques standard dans le développement frontend traditionnel. Ce chevauchement signifie que les développeurs familiers avec l'optimisation et les pratiques de sécurité frontend conventionnelles peuvent plus facilement s'adapter et appliquer ces compétences aux demandes uniques des applications pilotées par l'IA :

1. Employez des techniques de chargement paresseux et de division de code pour réduire les temps de chargement initiaux et améliorer les performances.
2. Utilisez des techniques de mise en cache et d'optimisation des ressources pour minimiser les appels API inutiles et améliorer la vitesse de récupération des données.
3. Mettez en œuvre des points de terminaison API sécurisés et des mécanismes d'authentification pour garantir un accès autorisé uniquement aux services IA et aux données.

## **Comment créer un AI Website Critic en utilisant React et le modèle GPT4-Vision d'OpenAI**

Dans cette section, nous allons créer une application React qui utilise un modèle de vision pour analyser des images de sites web et fournir des commentaires. Pour ce faire, nous allons suivre le flux de travail en 4 étapes décrit précédemment pour intégrer les services IA dans les applications frontend.   

Puisque nous avons besoin d'un modèle de vision capable d'analyser des images, nous devrions examiner les options disponibles sur le marché, que vous pouvez trouver [ici](https://replicate.com/collections/vision-models) et [ici](https://huggingface.co/models?pipeline_tag=visual-question-answering&sort=downloads). [Après avoir examiné les benchmarks de performance des modèles de vision disponibles](https://encord.com/blog/gpt-vision-vs-llava/), nous allons opter pour le modèle de vision GPT-4 d'OpenAI.  

Le modèle de vision GPT-4 d'OpenAI est un modèle d'IA de pointe sorti fin 2023. Il peut accepter des images en entrée, les analyser et fournir des commentaires détaillés en fonction des prompts. 

Outre les raisons de performance, nous l'utiliserons pour notre application de critique de sites web car il offre des prix relativement moins chers que les autres modèles de vision, et dispose d'un point de terminaison API facile à utiliser intégré à l'interface populaire des développeurs OpenAI.

Il est maintenant temps de l'intégrer dans notre application React.

### Étape 1 : Installer React + Vite

Vous pouvez le faire avec la commande suivante :

```
npm create vite@latest my-website-critic -- --template react
```

### Étape 2 : Installer le package Node OpenAI

Ouvrez le dossier du projet généré dans votre IDE préféré et installez le package Node OpenAI, que vous utiliserez pour interagir avec le modèle GPT4 Vision.

Voici comment l'installer :

```
cd my-website-critic
npm install openai
```

### Étape 3 : Installer le package React markdown 

Cela vous aidera à formater les réponses textuelles du modèle dans un format lisible.

```
npm install react-markdown
```

### Étape 4 : Exécuter npm install

Maintenant, exécutez `npm install` :

```
  npm install
  npm run dev
```

### Étape 5 : Gérer l'état dans React

Dans cette étape, vous utiliserez les hooks **`useState`** et **`useEffect`** de React pour gérer l'état et traiter la requête asynchrone vers l'API d'OpenAI dans `src/App.jsx`.

<figure>
    <img src="https://i.ibb.co/sWM573X/Screenshot-2024-01-18-at-10-34-28-AM.png"
         alt="section héro de freeCodeCamp">
    <figcaption>section héro de freeCodeCamp</figcaption>
</figure>


Pour notre entrée d'image, nous utiliserons une capture d'écran de la section héro de la page d'accueil de freeCodeCamp téléchargée sur une plateforme de stockage d'images comme [IMGBB](https://imgbb.com/). N'hésitez pas à utiliser n'importe quelle URL d'image que vous souhaitez.

Voici le code - je l'expliquerai ci-dessous :

```jsx
import { useState, useEffect } from 'react';
import OpenAI from 'openai';
import ReactMarkdown from 'react-markdown';

const App = () => {
  const [response, setResponse] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const openai = new OpenAI({
      apiKey: "VOTRE_CLE_API_OPENAI",
      dangerouslyAllowBrowser: true,
    });

    const fetchUICriticResponse = async () => {
      setIsLoading(true);
      try {
        const result = await openai.chat.completions.create({
          model: "gpt-4-vision-preview",
          messages: [
            {
              role: "user",
              content: [
                { type: "text", text: "Vous êtes un expert en UI. Que puis-je améliorer sur ce site web ?" },
                {
                  type: "image_url",
                  image_url: {
                    "url": "https://i.ibb.co/sWM573X/Screenshot-2024-01-18-at-10-34-28-AM.png",
                  },
                },
              ],
            },
          ],
          "max_tokens": 1500
        });
        if (result && result.choices && result.choices.length > 0 && result.choices[0].message) {
          console.log(1, result);
          setResponse(result.choices[0].message.content);
        }
      } catch (error) {
        console.error("Erreur lors de la récupération de la réponse IA :", error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchUICriticResponse();
  }, []);

  return (
    <div>
      <h3>Salut ! Expert en UI ici</h3>
      {isLoading ? (
        <p>Chargement...</p>
      ) : response ? (
        <div>
          <h3>Mes commentaires :</h3>
          <ReactMarkdown>{response}</ReactMarkdown>
        </div>
      ) : (
        <p>Aucune réponse reçue.</p>
      )}
    </div>
  );
};

export default App;
```

Dans le composant ci-dessus :

- Le hook **`useEffect`** exécute la fonction `fetchUICriticResponse` lorsque le composant est monté.
- Les hooks **`useState`** gèrent la réponse de l'IA (**`response`**) et l'état de chargement (**`isLoading`**).
- `fetchUICriticResponse` est une fonction asynchrone qui récupère la réponse en utilisant l'API OpenAI.
- Le composant affiche un message de chargement pendant que la réponse est en cours de récupération. Une fois la récupération terminée, il affiche la réponse ou un message de repli en utilisant le package React Markdown que nous avons installé précédemment.

Vous devriez obtenir un résultat similaire à l'image ci-dessous contenant le résultat de l'analyse du modèle GPT4 Vision de l'image fournie et du prompt donné.

<figure>
    <img src="https://i.ibb.co/DCNSHy7/critic.png"
         alt="résultat de l'analyse du modèle GPT4 Vision">
    <figcaption>résultat de l'analyse du modèle GPT4 Vision.</figcaption>
</figure>

Comme vous pouvez le voir, l'analyse passe en revue chaque élément de la page et offre des commentaires – à la fois positifs et plus constructifs – sur des éléments tels que la clarté de la navigation, l'utilisation de l'espace blanc, les fonctions de recherche, et ainsi de suite.


**Remarque :** La gestion des clés API directement dans le frontend n'est pas recommandée pour des raisons de sécurité. L'exemple est uniquement à des fins d'apprentissage. En production, créez un fichier `.env` et placez-y votre `VOTRE_CLE_API_OPENAI`.


## Quelles sont les prochaines étapes ?

Vous pouvez améliorer ces exemples de code en créant un simple champ de saisie pour que les utilisateurs puissent entrer leurs liens d'images. Vous pouvez également configurer un chargeur d'images pour permettre aux utilisateurs de télécharger des images depuis leur appareil local.

Veuillez vous référer à la [documentation officielle](https://platform.openai.com/docs/guides/vision) pour des instructions sur la manière d'y parvenir.

Lors de la décision des applications IA à développer, il est crucial de prendre en compte l'impact prévu, les exigences des utilisateurs et les ressources disponibles. 

D'autres idées potentielles d'applications IA incluent une application de traduction linguistique et un assistant personnel virtuel.

## Conclusion

Si vous êtes intéressé par l'intégration de l'IA dans vos applications frontend, commencez par explorer les modèles d'IA open source et closed source. Vous voudrez également comprendre comment travailler avec les API et les bibliothèques externes. 

Vous devriez également vous concentrer sur la familiarisation avec la gestion des réponses des modèles d'IA et l'interactivité.

Avec ces connaissances, vous pouvez vous positionner pour les nombreuses innovations IA prêtes pour les consommateurs qui émergeront et nécessiteront les services d'un développeur frontend compétent dans la création d'applications alimentées par l'IA.