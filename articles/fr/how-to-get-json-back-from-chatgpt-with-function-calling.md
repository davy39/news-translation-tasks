---
title: Comment structurer les réponses JSON dans ChatGPT avec l'appel de fonction
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-10-25T18:09:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-json-back-from-chatgpt-with-function-calling
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/chatgpt-ui-circled-1.png
tags:
- name: chatgpt
  slug: chatgpt
- name: json
  slug: json
seo_title: Comment structurer les réponses JSON dans ChatGPT avec l'appel de fonction
seo_desc: 'By James Charlesworth

  ChatGPT''s Problem With JSON

  Open up the ChatGPT UI and ask it for some JSON. Chances are you will get a response
  like you can see in the cover photo above: a JSON object presented to you in markdown
  format, with some text to eit...'
---

Par James Charlesworth

## Le problème de ChatGPT avec le JSON

Ouvrez l'[interface utilisateur de ChatGPT](https://chat.openai.com/) et demandez-lui du JSON. Il y a de fortes chances que vous obteniez une réponse comme celle que vous pouvez voir dans la photo de couverture ci-dessus : un objet JSON présenté en format markdown, avec du texte de chaque côté expliquant ce que le JSON montre.  

Si vous essayez cette même invite dans le [OpenAI Playground](https://platform.openai.com/playground), vous pouvez voir que le JSON est encadré par trois backticks (syntaxe markdown).

![Interface Open AI Playground montrant une invite utilisateur demandant du JSON](https://www.freecodecamp.org/news/content/images/2023/10/openai-playground-1-1.png)
_https://platform.openai.com/playground_

C'est bien. ChatGPT a fait un effort supplémentaire en expliquant la réponse en termes faciles à comprendre – faciles à comprendre, c'est-à-dire... pour un humain. Pas pour une machine. Les machines ont besoin de données dans un format qui respecte un schéma fiable, cohérent et prévisible.

Idéalement, vous aimeriez analyser la réponse de ChatGPT dans votre code et en faire quelque chose d'utile, comme ceci :

```ts
// Utiliser le package openai depuis npm pour appeler ChatGPT
import OpenAI from "openai";

// Créer une nouvelle instance du client openai avec notre clé API
const openai = new OpenAI({ apiKey: process.env.OPENAI_KEY });

// Appeler le point de terminaison des complétions de ChatGPT et demander du JSON
const gptResponse = await openai.chat.completions.create({
    model: "gpt-3.5-turbo",
    temperature: 1,
    messages: [
        {
            role: "user",
            content: "Donnez-moi le JSON pour un objet qui représente un chat."
        }
    ],
});

// Essayer de lire la réponse en tant que JSON,
// Cela échouera probablement avec une SyntaxError...
const json = JSON.parse(gptResponse.choices[0].message.content);
```

Mais cela ne fonctionnera que si `gptResponse.choices[0].message.content` est un JSON valide à chaque fois.  

Il serait également agréable d'avoir un JSON retourné qui respecte de manière fiable un schéma :

```ts
type Cat = {
    name: string,
    colour: "brown" | "grey" | "black",
    age: number
}

// Lire le JSON de réponse et le typer selon notre schéma d'objet Cat
const json = <Cat>JSON.parse(gptResponse.choices[0].message.content);
```

Ne pas pouvoir compter sur ChatGPT pour retourner un JSON valide dans un format prévisible peut introduire des bugs dans votre application, en particulier lorsque la cohérence est essentielle. Cela devient un vrai problème lorsque vous écrivez du code qui dépend des réponses en temps réel de ChatGPT pour déclencher des actions ou des mises à jour spécifiques, nous devons donc trouver une solution. Il existe plusieurs façons d'aborder ce problème...

## Comment l'ingénierie des invites peut aider

Une approche pour résoudre ce problème est l'ingénierie des invites.

![Image Open AI Playground montrant une invite système contrôlant le format de la réponse](https://www.freecodecamp.org/news/content/images/2023/10/asking-specifically-2.png)
_https://platform.openai.com/playground_

Ici, nous avons ajouté des instructions à la fois à l'invite utilisateur et au [message système](https://platform.openai.com/docs/guides/gpt/chat-completions-api). Les instructions tentent de forcer le modèle à retourner uniquement le JSON que nous voulons, avec le format que nous voulons.  

Et pour de nombreux cas d'utilisation, cela fonctionne de manière acceptable. Vous pouvez voir sur la capture d'écran ci-dessus que la réponse de l'"Assistant" n'est rien d'autre que du JSON, et que le JSON respecte le schéma que nous avons décrit pour lui.

Mais cela ne fonctionne pas 100 % du temps.

Voici la _même_ paire d'invites avec la température du modèle réglée au-dessus de 1. Remarquez comment le champ `colour` dans le JSON retourné ne respecte plus l'une des valeurs autorisées que nous avons spécifiées dans l'invite utilisateur :

![Interface Open AI Playground montrant le paramètre de température provoquant des réponses invalides à des valeurs plus élevées](https://www.freecodecamp.org/news/content/images/2023/10/higher-temperature-1.png)

## L'appel de fonction à la rescousse

L'[appel de fonction](https://platform.openai.com/docs/guides/gpt/function-calling) est une nouvelle façon d'utiliser l'API ChatGPT. Au lieu de recevoir un message du modèle de langage, vous recevez une demande pour appeler une fonction.  

Si vous avez déjà utilisé des plugins dans l'interface utilisateur de ChatGPT, l'_appel de fonction_ est la fonctionnalité derrière les scènes qui permet l'intégration des plugins avec les réponses du LLM.

Les plugins définissent les fonctions disponibles pour le modèle et lui permettent d'appeler ces fonctions en réponse aux invites des utilisateurs.  

Lorsque vous utilisez l'API dans votre propre code, vous pouvez également tirer parti de l'appel de fonction pour mieux contrôler les données que vous recevez du modèle, y compris le forcer à retourner des données JSON dans un format prévisible.

Voici une requête de base qui utilise l'appel de fonction pour retourner un objet `message.function_call` dans la réponse au lieu d'une chaîne `message.content`.  

Ici, nous demandons simplement à ChatGPT d'appeler une fonction ("getName") et une description de la fonction à l'intérieur du tableau `functions: []`. Nous instruisons également ChatGPT que nous nous attendons à ce qu'il appelle cette fonction dans la réponse en définissant la valeur de `function_call` sur le nom de notre fonction.

```ts
const gptResponse = await openai.chat.completions.create({
    model: "gpt-3.5-turbo-0613",
    messages: [
        {
            role: "user",
            content: "Appelle la fonction 'getName' et dis-moi le résultat."
        }
    ],
    functions: [
        {
            name: "getName",
            parameters: {
                type: "object",
                properties: {}
            }
        }
    ],
    function_call: { name: "getName" }
});

// Affichera "getName"...
console.log(gptResponse.choices[0].message.function_call.name);
```

Il est important de noter ici que la fonction `getName()` n'a pas besoin d'exister réellement quelque part dans notre base de code. Tout ce que nous faisons, c'est dire à ChatGPT qu'elle existe et qu'elle est disponible pour être appelée.

### Comment ajouter des arguments de fonction

L'appel de fonction est génial car il rend la réponse de ChatGPT prévisible et structurée.  

Dans l'exemple ci-dessus, nous obtiendrons un objet dans `gptResponse.choices[0].message.function_call` qui contiendra des détails sur la manière dont ChatGPT souhaite exécuter notre fonction (imaginaire). 

Cet objet ressemble à ce qui suit, avec le nom de la fonction et une version [stringifiée](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) de tout argument de fonction avec lequel elle doit être appelée :

```json
{
  name: "functionName",
  arguments: "{ \"arg1\": \"value\" }",
}
```

Nous pouvons tirer parti de cette deuxième valeur `arguments` en décrivant la forme des arguments de la fonction et en faisant en sorte que ChatGPT remplisse cette valeur avec un JSON qui respecte notre forme.

Voici l'exemple original sous forme d'appel de fonction. Remarquez comment nous avons décrit le schéma de l'objet `Cat` à ChatGPT à l'intérieur de la définition d'une fonction `createCatObject` :

```ts
    type Cat = {
        name: string,
        colour: "brown" | "grey" | "black",
        age: number
    }

    const openai = new OpenAI({ apiKey: process.env.OPENAI_KEY });

    const gptResponse = await openai.chat.completions.create({
        model: "gpt-3.5-turbo-0613",
        messages: [
            {
                role: "user",
                content: "Crée un nouvel objet Cat."
            }
        ],
        functions: [
            {
                name: "createCatObject",
                parameters: {
                    type: "object",
                    properties: {
                        name: {
                            type: "string"
                        },
                        colour: {
                            type: "string",
                            enum: ["brown", "grey", "black"]
                        },
                        age: {
                            type: "integer"
                        }
                    },
                    required: ["name", "colour", "age"]
                }
            }
        ],
        function_call: { name: "createCatObject" }
    });

    const functionCall = gptResponse.choices[0].message.function_call;
    const json = <Cat>JSON.parse(functionCall.arguments);
```

Cette requête de complétion instruira ChatGPT de créer un nouvel objet chat et de l'envoyer à la fonction `createCatObject()` dans un format spécifique. La dernière ligne :

```ts
const json = <Cat>JSON.parse(functionCall.arguments);
```

analyse les arguments de ChatGPT dans notre type `Cat`, qui reflète la description que nous avons donnée au modèle de la forme de notre objet attendu.

## Conclusion

L'appel de fonction avec ChatGPT apporte non seulement de la clarté et de la prévisibilité aux résultats, mais introduit également un changement de paradigme dans la manière dont vous pouvez interfacer avec les modèles d'apprentissage automatique. 

Cette approche structurée garantit que les réponses de ChatGPT sont évolutives, permettant une intégration plus facile dans diverses applications, qu'il s'agisse de simples applications web ou de pipelines d'apprentissage automatique plus complexes.