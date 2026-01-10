---
title: Comment intégrer ChatGPT avec Google Sheets en utilisant Google Apps Script
subtitle: ''
author: Nibesh Khadka
co_authors: []
series: null
date: '2023-07-20T16:06:35.000Z'
originalURL: https://freecodecamp.org/news/create-chat-gpt-formulas-in-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/GPT-IN-SHeets.png
tags:
- name: chatgpt
  slug: chatgpt
- name: google apps script
  slug: google-apps-script
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: Comment intégrer ChatGPT avec Google Sheets en utilisant Google Apps Script
seo_desc: 'Welcome to this tutorial on how to integrate ChatGPT with Google Spreadsheets
  using the GPT API and Google Apps Script.

  We will create two custom formulas, GPT_SUMMARY and GPT_SIMPLIFY. You can use GPT_SUMMARY
  to summarize a large passage or text int...'
---

Bienvenue dans ce tutoriel sur comment intégrer ChatGPT avec Google Spreadsheets en utilisant l'API GPT et Google Apps Script.

Nous allons créer deux formules personnalisées, GPT_SUMMARY et GPT_SIMPLIFY. Vous pouvez utiliser GPT_SUMMARY pour résumer un grand passage ou texte en quelques points pour une lecture facile. Et vous pouvez utiliser GPT_SIMPLIFY pour simplifier l'anglais en un anglais facile à lire.

Nous allons également créer des menus avec accès à des fonctions qui effectuent les mêmes tâches que les formules. Nous discuterons ensuite des avantages et inconvénients de l'utilisation des formules par rapport aux menus.

À la fin de ce tutoriel, vous comprendrez comment utiliser ChatGPT dans Google Sheets avec Google Apps Script. Vous serez également en mesure de modifier les formules et les menus pour répondre à vos propres besoins, comme la création de CV, de publications sur les réseaux sociaux ou de lettres de motivation.

Vous pouvez trouver le code source de ce projet dans [ce](https://github.com/nibukdk/GPT_Google_Sheets_Integration) dépôt GitHub.

Si vous souhaitez suivre une version vidéo de cet article, la voici :

%[https://www.youtube.com/watch?v=DlcJv97TZhE]

### Prérequis

Ce tutoriel n'est pas destiné aux débutants en Apps Script ou JavaScript. Je n'expliquerai pas chaque méthode ou classe utilisée dans le code. Ce n'est pas non plus un tutoriel sur comment utiliser et optimiser ChatGPT – nous nous concentrerons plutôt sur comment intégrer GPT dans Google Sheets.

#### À qui s'adresse ce tutoriel ?

Ce tutoriel s'adresse aux utilisateurs intermédiaires à avancés qui ont une compréhension de base d'Apps Script et de JavaScript. Si vous êtes nouveau dans l'un ou l'autre de ces domaines, je vous recommande de commencer par un tutoriel pour débutants avant d'essayer celui-ci.

## Étape 1 – Obtenir la clé API de ChatGPT

![Obtenir les clés API ChatGpt](https://cdn.hashnode.com/res/hashnode/image/upload/v1689645559540/943d9a3e-d326-4cd9-ab45-0866898110d2.png)
_Obtenir la clé API ChatGpt_

Tout d'abord, si vous n'avez pas déjà de compte avec OpenAI, vous devrez en [créer](https://auth0.openai.com/u/signup/identifier?state=hKFo2SBWU2Y5U0ZjYXlDWG5LU0xhdmxhd1pCVW1wQ2ppUUp3eKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIERpalA1aER5X3hGdEl0TzlRdnlud3FJQ2NlcDduNm4zo2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q) un. Une fois que vous avez un compte, vous pouvez créer une nouvelle clé API en allant dans la section des clés API sous l'onglet Utilisateur.

Cliquez sur le bouton Créer une nouvelle clé secrète et copiez la clé après qu'elle ait été créée. _Vous ne pourrez plus voir cette clé API_, alors assurez-vous de la copier quelque part en sécurité.

## Étape 2 – Récupérer les données de l'API ChatGpt avec Apps Script

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1689558938459/8586ac7a-9b41-41ef-9dcd-c4297436912d.png)
_Exemple de feuille de calcul_

J'ai nommé ma feuille de calcul GPT_Integration avec trois colonnes : Passage, Passage Simplifié et Texte Résumé.

![Comment ouvrir l'éditeur de code Apps Script depuis la feuille de calcul](https://cdn.hashnode.com/res/hashnode/image/upload/v1689559154810/de6ba3ed-a5af-4a23-ab45-e64bd39a48e6.png)

Ouvrons le script d'application pour cette feuille de calcul, renommons-le en GPT_integration, et renommons également le fichier existant en utils.gs. Nous allons créer une fonction appelée `fetchData` ici.

```javascript
const CHAT_GPT_API_KEY = "collez votre clé API ici";
const BASE_URL = "https://api.openai.com/v1/chat/completions";


function fetchData(systemContent, userContent) {
  try {
    const headers = {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${CHAT_GPT_API_KEY}`
    };

    const options = {
      headers,
      method: "GET",
      muteHttpExceptions: true,
      payload: JSON.stringify({
        "model": "gpt-3.5-turbo",
        "messages": [{
          "role": "system",
          "content": systemContent,
        },
        {
          "role": "user",
          "content": userContent
        },
        ],
        "temperature": 0.7
      })
    };

    const response = JSON.parse(UrlFetchApp.fetch(BASE_URL, options));
    //console.log(response);
    //console.log(response.choices[0].message.content)
    return response.choices[0].message.content;
  } catch (e) {
    console.log(e)
    SpreadsheetApp.getActiveSpreadsheet().toast("Une erreur est survenue. Veuillez vérifier votre formule ou réessayer plus tard.");
    return "Une erreur est survenue. Veuillez vérifier votre formule ou réessayer plus tard.";
  }
}
```

Voici quelques points clés à remarquer dans le code ci-dessus :

1. Collez la clé API que vous avez créée précédemment à l'intérieur des guillemets.
2. Nous allons utiliser l'API Chat Completions. Vous pouvez trouver plus de détails à ce sujet [ici](https://platform.openai.com/docs/api-reference/chat/create).
3. Les modèles ChatGPT ont différents rôles, tels que system, user et assistant.
4. Le paramètre systemContent est l'endroit où vous fournissez le rôle pour le système GPT. Par exemple, vous pourriez dire "Vous êtes un professeur expert en algèbre" ou "Vous êtes un rédacteur expert de CV".
5. Le paramètre userContent est l'endroit où vous fournissez des tâches à effectuer pour le modèle. Dans notre cas, nous fournirons de longs passages de la feuille de calcul à résumer et simplifier.
6. Nous allons utiliser le [modèle GPT 3.5 turbo](https://platform.openai.com/docs/models/gpt-3-5).
7. Nous désactivons les HTTPExceptions afin de pouvoir utiliser notre propre message d'erreur dans le bloc catch.
8. La chaîne d'erreur est utile lorsque nous rencontrons des erreurs telles que [Rate Limit Exceed](https://platform.openai.com/docs/guides/rate-limits/what-are-the-rate-limits-for-our-api).

Nous retournons le contenu de l'objet de réponse de GPT qui sera ensuite traité par nos formules.

L'objet de réponse de ChatGPT a la structure suivante :

```json
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "\n\nBonjour, comment puis-je vous aider aujourd'hui ?",
    },
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21
  }
}
```

Lisez plus sur comment utiliser UrlFetchApp depuis [ici](https://developers.google.com/apps-script/reference/url-fetch/url-fetch-app).

## Étape 3 – Intégrer ChatGpt en tant que formule de feuille de calcul

### Formule GPT SIMPLIFY

Encore une fois, pour la formule personnalisée, nous allons créer un nouveau fichier nommé formula et ensuite nous créerons une fonction nommée GPT_SIMPLIFY.

```javascript
/**
 * Simplifie le paragraphe donné en termes simples.
 * @param {String} input La valeur à simplifier.
 * @return Texte simplifié.
 * @customfunction
 */
function GPT_SIMPLIFY(input) {
  console.log(input)
  const systemContent = "Simplifiez le texte donné en termes simples. Souvenez-vous que le lecteur n'est pas un expert en anglais.";
  return Array.isArray(input) ?
    input.flat().map(text => fetchData(systemContent, text)) :
    fetchData(systemContent, input);

}
```

1. La formule `GPT_SIMPLIFY` simplifie tout texte fourni en entrée. L'entrée de cette fonction est la donnée provenant de la feuille de calcul. Lorsque vous sélectionnez une plage, une cellule ou plusieurs cellules, les données de la plage seront automatiquement fournies par la feuille de calcul à cette formule.
2. Le `systemContent` est défini pour être passé en tant que premier paramètre à la fonction `fetchData(systemContent,userContent)`.
3. Nous vérifions si l'entrée est un tableau car les données passées à cette fonction peuvent être soit un tableau imbriqué, soit simplement une chaîne si nous sélectionnons plusieurs cellules ou une seule cellule, respectivement, dans la feuille de calcul.

Vous pouvez lire plus sur les fonctions personnalisées sur cette [page](https://developers.google.com/apps-script/guides/sheets/functions).

Allez-y et appliquez cette formule dans votre feuille de calcul. J'ai copié du texte d'un livre que je lis dans la première colonne et appliqué la formule dans la deuxième colonne nommée "Simplify Passage", comme ceci `=GPT_SIMPLIFY(A2)` pour la deuxième cellule.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/gpt_simplify_formula.png)
_Application de la formule GPT_SIMPLIFY_

Note : Assurez-vous d'actualiser la feuille de calcul avant d'appliquer la formule pour synchroniser avec les dernières modifications du script.

### GPT SUMMARIZE

Pour résumer la formule, nous allons simplement copier la fonction de simplification et quelques autres choses, comme vous pouvez le voir dans le code ci-dessous.

```javascript
/**
 * Résume le paragraphe donné. Il fournit de 3 à 5 points.
 *
 * @param {String} input La valeur à résumer.
 * @return Texte résumé.
 * @customfunction
 */
function GPT_SUMMARY(input) {
  console.log(input)
  const systemContent = "Résumé du texte donné. Fournissez au moins 3 et au plus 5 points.";
  return Array.isArray(input) ?
    input.flat().map(text => fetchData(systemContent, text)) :
    fetchData(systemContent, input);

}
```

La chose principale à remarquer ici est le contenu du système différent.

Note : Puisque ce n'est pas un tutoriel sur comment utiliser ChatGpt de manière optimale, j'ai fourni des instructions en tant que contenu du système au lieu de jouer un rôle, puis j'ai simplement fourni des données dans le contenu de l'utilisateur. Vous pouvez improviser cela en fournissant des rôles dans le contenu du système, et des tâches ainsi que des données en tant que deux rôles d'utilisateur différents dans notre fonction `FetchData()`.

### Erreur de limite de taux GPT

Pour les utilisateurs gratuits, la limite de taux pour utiliser l'API est de **3/minute**. Ainsi, lorsque vous appliquez ces formules dans plus de trois cellules, vous rencontrerez l'erreur. Heureusement, l'exécution ne s'arrêtera pas car nous retournons une chaîne d'erreur depuis fetch data qui sera enregistrée dans ces cellules.

![Erreur de limite de taux GPT](https://cdn.hashnode.com/res/hashnode/image/upload/v1689574131023/70e326ac-33bd-4d75-96db-208fc27b5859.png)
_Erreur de limite de taux de l'API_

### Actualisation automatique et erreur

De plus, la fonction d'actualisation automatique de la formule peut forcer la réapplication de la formule sur les cellules qui ont déjà des valeurs satisfaisantes chaque fois que les cellules sources sont mises à jour, dans notre cas les cellules de la colonne "A".

Lorsque nous ajoutons une limite de taux par-dessus l'actualisation automatique, cela peut causer un dilemme. Vous pouvez techniquement apporter des modifications aux fonctions personnalisées pour accommoder de telles circonstances, mais j'aime garder les formules légères et efficaces. Donc, je recommande de créer plutôt des menus personnalisés et d'appliquer ces fonctions manuellement.

## Étape 4 – Intégrer l'API Chat GPT dans les fonctions de menu de la feuille de calcul

### Menu GPT Simplify

Tout d'abord, créons un autre fichier nommé `menu`. Ensuite, nous créerons la fonction `gptSimplifyMenu` qui sera une alternative à la formule GPT_SIMPLIFY.

```javascript

/**
 * Simplifie le paragraphe donné en termes simples.
 * @customfunction
 */
function gptSimplifyMenu() {
  try {
    // obtenir les feuilles et les données
    const ss = SpreadsheetApp.getActiveSheet();
    const data = ss.getDataRange().getValues();
    const lastRow = data.length;
    const lastCol = data[0].length;

    // définir le rôle de gpt
    const systemContent = "Simplifiez le texte donné en termes simples. Souvenez-vous que le lecteur n'est pas un expert en anglais.";


    for (let i = 1; i < data.length; i++) {
      // ne simplifier que si ce n'est pas déjà simplifié ou si une erreur s'est produite précédemment
      if (data[i][1] === "" || data[i][1] === "Une erreur est survenue. Veuillez vérifier votre formule ou réessayer plus tard.") {
        data[i][1] = fetchData(systemContent, data[i][0]);
        console.log(data[i][1]);

      }
    }

    ss.getRange(1, 1, lastRow, lastCol).setValues(data);
  } catch (e) {
    console.log(e)
    SpreadsheetApp.getActiveSpreadsheet().toast("Une erreur est survenue. Veuillez vérifier votre formule ou réessayer plus tard.");

  }
}
```

Points clés qui sont différents à comprendre dans ce code sont :

1. Nous codons en dur les sources de données, comme data[i][1], qui fait référence à la deuxième colonne (c'est-à-dire "Passage Simplifié") comme montré dans l'image de la feuille de calcul ci-dessus. Cela signifie que si vous utilisez d'autres colonnes pour sauvegarder les données de ChatGPT, vous devrez apporter des modifications en conséquence.
2. Nous ne récupérons les données que lorsque la cellule cible est vide ou contient un message d'erreur. Cela aide à éviter les appels API inutiles.

### Ajouter une fonction personnalisée en tant que menu de feuille de calcul

La fonction est prête à être testée, mais elle n'apparaîtra toujours pas dans la feuille de calcul. Pour ce faire, nous devons fournir les instructions suivantes.

```javascript

/**
 * Le menu crée une interface de menu dans la feuille de calcul.
 */
function createCustomMenu() {
   // définir l'interface de menu 
  let menu = SpreadsheetApp.getUi().createMenu("Fonctions GPT");
   // ajouter une fonction au menu
   menu.addItem("GPT SIMPLIFY", "gptSimplifyMenu");
   // ajouter le menu à l'interface de la feuille de calcul
  menu.addToUi();
}

/**
 * Déclencheur OnOpen qui crée le menu
 * @param {Dictionary} e
 */
function onOpen(e) {
  createCustomMenu();
}
```

Dans `createCustomMenu()` :

1. Nous définissons le menu avec [`SpreadsheetApp.getUi().createMenu("Fonctions GPT")`](https://developers.google.com/apps-script/reference/base/ui#createmenucaption) comme Fonctions GPT, le titre apparaissant dans l'onglet de la feuille de calcul.
2. Nous ajoutons une fonction au menu avec `menu.addItem("GPT SIMPLIFY", "gptSimplifyMenu")`, où le premier paramètre est le titre pour l'affichage et le second est la fonction à appeler lorsqu'on appuie dessus.
3. Ajoutez le menu à l'interface utilisateur avec `menu.addToUi()`.

Le déclencheur [onOpen](https://developers.google.com/apps-script/guides/triggers#onopene) s'exécute automatiquement chaque fois que le document auquel le script est attaché se recharge et ajoute ainsi un menu à la feuille de calcul comme montré dans l'image ci-dessous.

![Menu des fonctions GPT](https://cdn.hashnode.com/res/hashnode/image/upload/v1689573996102/660acf86-567e-4261-96db-2a8ed1c2182c.png)

Allez-y et essayez la formule – elle ne sera appliquée que si la cellule est soit vide, soit préremplie avec un message d'erreur.

### Menu GPT Summarize

Nous allons apporter quelques modifications mineures après avoir copié la fonction de simplification comme montré ci-dessous :

```javascript
/**
 * Résume le paragraphe donné. Il fournit de 3 à 5 points.
 * @customfunction
 */
function gptSummaryMenu() {
  try {
    // obtenir les feuilles et les données
    const ss = SpreadsheetApp.getActiveSheet();
    const data = ss.getDataRange().getValues();
    const lastRow = data.length;
    const lastCol = data[0].length;

    // définir le rôle de gpt
    const systemContent = "Résumé du texte donné. Fournissez au moins 3 et au plus 5 points.";


    for (let i = 0; i < data.length; i++) {
      console.log(`Inside gptSummaryMenu() for loop`)

      if (i == 0) continue;
      // ne résumer que si ce n'est pas déjà résumé ou si une erreur s'est produite précédemment
      if (data[i][2] === "" || data[i][2] === "Une erreur est survenue. Veuillez vérifier votre formule ou réessayer plus tard.") {
        data[i][2] = fetchData(systemContent, data[i][0]);
        console.log(data[i][2]);
      }
    }

    ss.getRange(1, 1, lastRow, lastCol).setValues(data);
  } catch (e) {
    console.log(e)
    SpreadsheetApp.getActiveSpreadsheet().toast("Une erreur est survenue. Veuillez vérifier votre formule ou réessayer plus tard.");
  }
}
```

1. Le rôle du système a été modifié pour traiter l'instruction de résumé.
2. La colonne cible pour sauvegarder les données est maintenant la troisième colonne.
3. La chaîne de documentation a également été ajustée.

Quant à l'ajout de cette fonction au menu, je vous laisse le faire.

## Conseils pour modifier le code

Tout ce dont vous avez besoin pour créer votre propre formule comme =GPT_COVER_LETTER_CREATOR() sont les modifications suivantes :

### Pour FetchData

Vous pouvez changer la description du contenu du système pour répondre à vos besoins, comme "Vous écrivez une lettre de motivation experte pour les développeurs de logiciels".

Ajoutez une autre instruction dans le tableau des messages :

```json
// de ceci 
[{
          "role": "system",
          "content": systemContent,
        },
        {
          "role": "user",
          "content": userContent
        },
        ], 

// à ceci 
[{
          "role": "system",
          "content": "Vous écrivez une lettre de motivation experte pour les développeurs de logiciels",
        },
        {
          "role": "user",
          "content": "Écrivez-moi une lettre de motivation pour cette annonce d'emploi donnée"
        },
        {
          "role": "user",
          "content": userContent // ceci est l'annonce d'emploi de la feuille de calcul
        },
        ],
```

Vous pouvez également ajouter un autre élément de liste pour inclure vos compétences et expériences.

### Autres fonctions

Assurez-vous simplement que vos cellules/colonnes sources et cellules/colonnes cibles sont correctement indexées (par exemple, si vous n'utilisez pas la première colonne comme cellule source et la deuxième pour sauvegarder les données).

## Résumé

Dans ce tutoriel, vous avez appris comment utiliser Google Apps Script pour récupérer les réponses de ChatGPT depuis l'API et les sauvegarder dans des feuilles de calcul en utilisant des formules personnalisées et des menus personnalisés.

Nous avons commencé par créer un nouveau projet Google Apps Script et ajouter l'API ChatGPT. Ensuite, nous avons écrit un script qui récupérerait une réponse ChatGPT pour une invite donnée. Nous avons sauvegardé la réponse en utilisant une formule personnalisée dans une cellule de la feuille de calcul.

Nous avons également créé un élément de menu personnalisé qui nous permettrait de récupérer une réponse ChatGPT depuis n'importe quelle cellule de la feuille de calcul. Cet élément de menu ouvrirait un bouton pour récupérer la réponse.

La dernière étape consistait à partager la feuille de calcul avec d'autres afin qu'ils puissent utiliser les formules et menus personnalisés pour récupérer les réponses de ChatGPT.

J'espère que vous avez apprécié cet article et que vous l'avez trouvé utile. Si vous avez des questions, n'hésitez pas à me le faire savoir.

Je suis **Nibesh Khadka**, freelance spécialisé dans l'automatisation des produits Google avec Apps Script. Contactez-moi si vous avez besoin de mes services à me@nibeshkhadka.com.