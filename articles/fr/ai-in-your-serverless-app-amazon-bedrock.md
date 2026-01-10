---
title: Comment intégrer l'IA dans votre application Serverless avec Amazon Bedrock
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-10-02T19:23:14.000Z'
originalURL: https://freecodecamp.org/news/ai-in-your-serverless-app-amazon-bedrock
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-02-at-14.19.28.png
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: serverless
  slug: serverless
seo_title: Comment intégrer l'IA dans votre application Serverless avec Amazon Bedrock
seo_desc: "By Sam Williams\nIn today's tech landscape, integrating AI is no longer\
  \ a luxury – it's a necessity. \nAI-driven applications have the potential to transform\
  \ user experiences, automate complex tasks, and unlock new realms of possibilities.\
  \ Understandin..."
---

Par Sam Williams

Dans le paysage technologique actuel, intégrer l'IA n'est plus un luxe, c'est une nécessité.

Les applications alimentées par l'IA ont le potentiel de transformer les expériences utilisateur, d'automatiser des tâches complexes et de débloquer de nouveaux domaines de possibilités. Comprendre et exploiter les API d'IA est une compétence essentielle pour les développeurs souhaitant rester à la pointe de l'innovation.

## Aperçu des API d'IA

Les API d'Intelligence Artificielle sont des outils puissants qui permettent aux développeurs d'utiliser les capacités de modèles de machine learning pré-entraînés. Ces API exposent des fonctionnalités telles que le traitement du langage naturel, la vision par ordinateur, et bien plus encore, permettant aux développeurs d'incorporer facilement des capacités avancées d'IA dans leurs applications.

Vous n'avez plus besoin de comprendre les époques d'entraînement et l'architecture des réseaux de neurones pour utiliser l'IA dans vos projets et construire des fonctionnalités incroyablement puissantes pour vos utilisateurs.

### L'objectif de ce tutoriel :

Le but de ce tutoriel est de vous équiper des connaissances et des compétences pratiques nécessaires pour intégrer de manière transparente les API d'IA dans vos projets.

Je vais vous guider à travers tout le processus, depuis le choix de l'API adaptée à vos besoins spécifiques jusqu'à la mise en œuvre pratique et les meilleures pratiques pour une intégration transparente.

À la fin, vous serez bien équipé pour infuser une intelligence alimentée par l'IA dans vos applications, ouvrant un monde de nouvelles possibilités.

Alors, embarquons ensemble dans ce voyage et découvrons le véritable potentiel des API d'IA.

## Options actuelles d'API d'IA

Il existe de plus en plus de services d'IA disponibles via une simple API. Dans cet article, nous utiliserons [Amazon Bedrock](https://aws.amazon.com/bedrock/), mais il en existe beaucoup d'autres. Même Amazon Bedrock propose 6 modèles disponibles, avec d'autres à venir dans le futur.

### Comparaison des API d'IA disponibles

Pour vous aider à prendre une décision éclairée, comparons certaines des principales API d'IA disponibles sur le marché. Voici un tableau comparatif de quelques options prometteuses :

<table>
<thead>
<tr>
<th>API</th>
<th>Description</th>
<th>Prix</th>
</tr>
</thead>
<tbody>
<tr>
<td>GPT-3.5 (16k)</td>
<td>Modèle de langage de pointe capable de comprendre et de générer du langage naturel ou du code</td>
<td>0,0003 $ / 1000 jetons d'entrée
    0,004 $ / 1000 jetons de sortie</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>GPT-4 (32K)</td>
<td>Le système le plus avancé d'OpenAI, produisant des réponses plus sûres et plus utiles</td>
<td>0,06 $ / 1000 jetons d'entrée
    0,12 $ / 1000 jetons de sortie</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>A2I Jurassic-2 Mid model (Bedrock)</td>
<td>Modèle de taille moyenne, conçu pour trouver le bon équilibre entre qualité exceptionnelle et abordabilité</td>
<td>0,0125 $ / 1000 jetons d'entrée
    0,0125 $ / 1000 jetons de sortie</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>A2I Jurassic-2 Ultra model (Bedrock)</td>
<td>Le modèle le plus puissant d'AI21, offrant une qualité exceptionnelle</td>
<td>0,0188 $ / 1000 jetons d'entrée
    0,0188 $ / 1000 jetons de sortie</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>Anthropic Claude Instant (Bedrock)</td>
<td>Modèle de langage généraliste de pointe</td>
<td>0,00163 $ / 1000 jetons d'entrée
    0,01102 $ / 1000 jetons de sortie</td>
<td></td>
</tr>
<tr>
<td>Stability AI (Bedrock)</td>
<td>Génération d'images</td>
<td>0,018 $ - 0,072 $ par image
selon la taille et la qualité</td>
</tr>

</tbody>
</table>

### Facteurs clés à considérer lors de la sélection d'une API

Lors du choix d'une API d'IA pour votre projet, il est crucial de considérer plusieurs facteurs clés :

1. **Capacités et fonctionnalités de l'API :** Évaluez les fonctionnalités spécifiques offertes par l'API et assurez-vous qu'elles correspondent aux exigences de votre projet. La qualité du contenu généré peut également varier considérablement entre les modèles, il est donc judicieux de les tester et de voir comment ils performant pour votre cas d'utilisation.
2. **Évolutivité et performance :** Évaluez la capacité de l'API à gérer des charges de travail variables et assurez-vous qu'elle répond à vos attentes en matière de performance, surtout pendant les pics d'utilisation.
3. **Considérations de coût :** Comprenez le modèle de tarification de l'API, y compris les coûts associés à l'utilisation, et déterminez sa compatibilité avec votre budget. 
4. **Confidentialité des données et sécurité :** Assurez-vous que le fournisseur de l'API respecte les réglementations de protection des données et dispose de mesures de sécurité robustes pour protéger les informations sensibles.

En prenant en compte ces facteurs, vous serez mieux équipé pour choisir l'API d'IA qui convient le mieux aux besoins de votre projet.

Pour ce tutoriel, nous allons utiliser Amazon Bedrock avec le [modèle A2I Jurassic-2 Mid](https://aws.amazon.com/bedrock/jurassic/).

## Comment demander l'accès au modèle

Étant donné que ce service est tout nouveau, vous devez demander l'accès aux modèles que vous souhaitez utiliser.

Pour ce faire, connectez-vous à votre compte AWS, recherchez "Bedrock" et sélectionnez l'onglet "Base models" à gauche. Passez la souris sur un modèle et il indiquera que vous n'avez pas actuellement accès et de demander l'accès dans "Model Access".

Cela liste tous les modèles. Cliquez sur le bouton d'édition en haut à droite, sélectionnez les modèles auxquels vous souhaitez avoir accès, puis cliquez sur "Save". Pour cela, vous devez sélectionner `Jurassic-2 Ultra` et `Jurassic-2 Mid`.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-09-30-at-18.12.43.png)
_Sélectionnez les modèles pour lesquels vous souhaitez demander l'accès_

Cela ne devrait prendre qu'une minute ou deux pour être approuvé, mais mieux vaut le faire dès que possible.

## Projet : Construire une API de planification de vacances

### Ce que notre API fera

Notre API est conçue pour simplifier la planification de vacances. En fournissant le code de l'état de votre destination et la durée de votre visite, nous générerons un itinéraire personnalisé, suggérant les meilleures activités et lieux à explorer.

### Comment configurer le dépôt

Nous utiliserons le Framework Serverless pour ce projet. Si vous ne l'avez jamais utilisé auparavant, vous pouvez suivre ce tutoriel rapide pour [installer Serverless](https://completecoding.io/how-to-deploy-to-aws-from-the-serverless-framework/) et tout configurer.

Nous allons utiliser JavaScript pour ce projet, alors créez un nouveau dépôt comme ceci :

```
sls create --template aws-nodejs --path aiTourGuide
```

### Créer une Lambda avec des commentaires

Nous devons commencer par créer notre fonction Lambda. J'aime les stocker sous `/src/functions/{functionName}/index.js`. Dans ce cas, mon functionName sera `aiTourGuide`.

Dans le nouveau fichier `index.js`, nous pouvons commencer avec ce code. Il essaie d'obtenir l'état et la durée de la requête, puis retourne une réponse.

```js
exports.handler = async (event) => {
    const { state_code, duration } = JSON.parse(event.body);

    // Le code pour générer l'itinéraire ira ici

    const response = {
        statusCode: 200,
        body: JSON.stringify('Itinéraire généré avec succès !')
    };

    return response;
};


```

### S'inscrire à l'API du National Park Service

Maintenant, nous voulons obtenir des données à transmettre à l'IA. Nous pourrions simplement lui demander de générer un itinéraire pour nous, mais lui donner des données spécifiques à utiliser donne généralement un bien meilleur résultat.

1. Visitez le [site web de l'API du National Park Service](https://www.nps.gov/subjects/developer/get-started.htm) et inscrivez-vous pour obtenir une clé API.
2. Une fois inscrit, vous recevrez une clé API par e-mail pour accéder à leurs services.

### Ajouter l'appel à l'API du National Park Service à la Lambda

```js
const axios = require('axios');
const parksApiKey = process.env.parksApiKey

exports.handler = async (event) => {
    const { state_code, duration } = JSON.parse(event.body);

    // Faire une requête à l'API du National Park Service
    const parksApiUrl = `https://developer.nps.gov/api/v1/parks?stateCode=${state_code}&api_key=${parksApiKey}`
    
    const parksResponse = await axios.get(parksApiUrl);

    // Extraire les données pertinentes de la réponse
    const parks = parksResponse.data.data.map(park => {
        return {
            name: park.fullName,
            description: park.description
        };
    });

    // Le code pour générer l'itinéraire avec les données des parcs ira ici

    const responseBody = parks;
    const response = {
        statusCode: 200,
        body: JSON.stringify(responseBody)
    };

    return response;
};


```

Nous faisons la requête à l'API des parcs en utilisant Axios, puis nous obtenons uniquement le `name` et la `description` de chaque parc à partir de la réponse. Pour l'instant, nous allons simplement retourner ces données dans l'API pour voir ce que nous obtenons.

Une chose que nous faisons est d'obtenir la `parksApiKey` à partir des variables d'environnement au début du fichier. Pour ajouter la `parksApiKey` en tant que variable d'environnement dans un fichier `serverless.yml` du Framework Serverless, vous pouvez suivre ces étapes :

1. Ouvrez votre fichier `serverless.yml` dans un éditeur de texte.
2. Localisez la section `provider`, qui définit les paramètres du fournisseur AWS. Sous celle-ci, ajoutez un bloc `environment` s'il n'existe pas déjà.
3. Dans le bloc `environment`, définissez votre variable d'environnement comme ceci :

```yaml
provider:
  name: aws
  runtime: nodejs18.x
  environment:
    parksApiKey: "VOTRE CLÉ API"

```

### Configurer le fichier serverless.yml

Pour déployer réellement une API et notre code, nous devons dire à Serverless quoi déployer. Nous faisons cela en modifiant la section `functions` de la configuration.

```yaml
functions:
  aiTourGuide:
    handler: src/functions/aiTourGuide/index.handler
    events:
      - httpApi:
          path: /tourguide
          method: post

```

Cela signifie que nous allons déployer une fonction lambda `aiTourGuide` avec un endpoint API post pointant vers `/tourguide`. Assurez-vous simplement que la section handler est le chemin correct pour votre dépôt et votre structure de dossiers.

Si vous avez [configuré vos identifiants AWS pour un profil spécifique](https://completecoding.io/aws-credentials-setup/), vous devez ajouter cela à votre section provider, sinon il utilisera vos identifiants AWS par défaut.

```jsx
provider:
  name: aws
  runtime: nodejs18.x
  profile: "Votre Profil" // optionnel

```

### Déployer et tester

Maintenant que nous avons créé notre fonction Lambda et intégré l'API du National Park Service, il est temps de déployer et de tester notre API de planification de vacances.

1. **Déploiement :** Tout ce que nous avons à faire est d'exécuter `sls deploy` à nouveau et nos changements seront déployés.
2. **Test :** Utilisez un outil comme Postman pour envoyer une requête POST à votre API avec les paramètres requis, tels que `state_code` et `duration`. Vous devriez obtenir une réponse comme celle-ci.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-09-30-at-15.56.11.png)
_Image montrant la réponse_

Vous pouvez voir que nous avons un tableau d'objets, avec le nom du parc et la description. Exactement ce que nous voulions.

### Comment préparer notre prompt d'IA

Ensuite, nous allons préparer une requête à une API d'IA pour améliorer nos recommandations de planification de vacances. Nous allons utiliser le modèle A2I Jurassic-2 Mid via Amazon Bedrock pour générer des descriptions engageantes pour les activités recommandées.

J'ai tendance à commencer relativement simplement et à affiner le prompt au fur et à mesure que je vois comment il fonctionne. J'encapsule également la génération de mon prompt dans une fonction. Cela peut devenir assez grand et complexe plus tard, donc il est préférable de ne pas l'avoir dans le gestionnaire principal. Je l'ai souvent dans son propre fichier !

Commençons par quelque chose comme ceci :

```js
const generatePrompt = ({parks,duration}) => {

	const stringListOfParks = parks.map(({name, description}) => {
		return `Nom du parc : ${name}:
	description : ${description}`}).join(`
	
	`)
	
	const prompt = `Vous êtes un guide touristique expert aux États-Unis qui se concentre sur la conception d'itinéraires de vacances pour passer du temps dans les parcs nationaux. 
	Je vais vous donner des descriptions de plusieurs parcs dans la région ainsi que la durée du voyage. 
	Créez un itinéraire pour ce voyage, en détaillant les activités qui peuvent être faites chaque jour.
	
	Durée du voyage = ${duration} jours
	
	Parcs nationaux locaux:
	${stringListOfParks}
	`;
	return prompt
}

```

La fonction `stringListOfParks` transforme le tableau d'objets en une longue chaîne. Cela peut ne pas être nécessaire, mais nous devons attendre pour voir.

Ensuite, nous créons le prompt d'IA. Nous disons à l'IA qui elle est censée être, quelles informations nous allons lui donner et ce que nous voulons qu'elle fasse. Pour commencer, cela est bien, mais avec le temps, nous pouvons tester différents changements à notre prompt pour voir ce qui génère les meilleurs résultats.

### Comment appeler l'API d'IA

Maintenant que nous avons un prompt, nous pouvons le transmettre à Amazon Bedrock pour traiter notre prompt. Nous devons commencer par importer le SDK AWS et créer le `bedrockruntime`.

Vous devrez également installer le SDK AWS pour Bedrock car il n'est actuellement inclus dans aucune des versions lambda :

```jsx
npm i -S @aws-sdk/client-bedrock-runtime

```

Et nous ajoutons ce code en haut de notre fichier Lambda.

```js
import { BedrockRuntime } from "@aws-sdk/client-bedrock-runtime";
import axios from "axios";

const bedrockruntime = new BedrockRuntime()
```

Nous utilisons également des imports maintenant, ce qui signifie que nous devons changer notre fichier `index.js` en `index.mjs`. Si vous l'avez fait en utilisant TypeScript, vous n'auriez pas à renommer votre fichier.

Nous devons appeler la commande `invokeModel` et lui passer un ensemble de paramètres. Je trouve qu'il est plus propre de créer un objet séparé pour les paramètres plutôt que de tout faire en un seul endroit.

Actuellement, il n'existe pas de version asynchrone de la commande `invokeModel`, donc nous allons l'encapsuler dans une promesse.

```js
const aiPrompt = generatePrompt({parks,duration});

const aiModelId = 'ai21.j2-mid-v1'; // nous utilisons le modèle A2I Jurassic-2 Mid

const invokeModelParams = {
    body: JSON.stringify({
        prompt: aiPrompt,
        maxTokens: 200,
        temperature: 0.5,
        topP: 0.5, // optionnel
    }),
    modelId: aiModelId,
    accept: 'application/json',
    contentType: 'application/json'
};

const aiResponse = await new Promise((resolve, reject) => {
    bedrockruntime.invokeModel(invokeModelParams, function(err, data) {
        if (err) {
            reject(err); // une erreur s'est produite
        } else {
            resolve(data); // réponse réussie
        }
    });
});

// Extraire le texte généré par l'IA de la réponse
const aiResponseJson = JSON.parse(
    new TextDecoder().decode(aiResponse.body)
);
const aiItinerary =  aiResponseJson.completions[0].data.text;

const responseBody = aiItinerary;
const response = {
    statusCode: 200,
    body: responseBody,
};
return response;

```

Vous avez peut-être remarqué que nous transmettons plus que simplement notre prompt dans le corps. C'est parce que nous pouvons changer quelques autres choses pour obtenir une sortie différente.

Les LLM fonctionnent en choisissant le mot suivant dans la phrase. `temperature` et `topP` contrôlent si le modèle choisit des mots inhabituels ou s'en tient au mot le plus probable.

* Température : Plus proche de 1 signifie que des mots plus inhabituels seront choisis, plus proche de 0 choisit des mots plus probables.
* topP : Lors du choix du mot suivant, limitez le nombre d'options dont l'IA dispose pour choisir en additionnant les probabilités. Les nombres plus proches de 1 signifient que plus de mots improbables sont inclus.

Dans notre cas, nous voulons une réponse relativement créative mais aussi que les choses soient correctes, donc 0,5 est un bon paramètre de départ pour les deux. Si nous lui demandions de décrire une scène de science-fiction, nous voudrions opter pour temp=0,7 topP=0,8, ou si nous lui demandions d'écrire du code de traitement de données, nous le réduirions à 0,2 car nous voulons une réponse plus susceptible d'être correcte.

Ce sont deux choses que vous pouvez changer et tester pour voir quelles valeurs donnent les meilleurs résultats. Les paramètres que vous transmettez dépendent également [du modèle](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).

### Comment ajouter des permissions IAM pour appeler Bedrock

Si votre fonction Lambda doit accéder à des ressources ou services AWS comme Amazon Bedrock, nous devons nous assurer de configurer les permissions IAM appropriées.

Dans votre fichier serverless.yml, vous devez ajouter ceci à votre section provider. Cela indique que cette Lambda a la permission d'utiliser `bedrock:InvokeModel`.

```jsx
provider:
  name: aws
  runtime: nodejs18.x
  environment:
    parksApiKey: VOTRE CLÉ API
  iam:
    role:
      statements:
        - Effect: "Allow"
          Action:
            - "bedrock:InvokeModel"
          Resource: "*"

```

### Déployer et tester (à nouveau)

Après avoir intégré l'API d'IA et assuré les permissions IAM appropriées, redéployez votre fonction Lambda en exécutant `sls deploy`. Ensuite, nous pouvons la tester une fois de plus pour nous assurer que l'itinéraire de vacances généré par l'IA fonctionne correctement.

En utilisant la même requête que la dernière fois, voici la réponse que j'ai obtenue, et vous devriez obtenir quelque chose de similaire.

_Jour 1 :_

* _Arriver à Jackson, Mississippi et s'enregistrer à l'hôtel_
* _Visiter le Medgar and Myrlie Evers Home National Monument_
* _Nuit à Jackson_

_Jour 2 :_

* _Conduire à Natchez, Mississippi et s'enregistrer à l'hôtel_
* _Visiter le Natchez National Historical Park_
* _Nuit à Natchez_

_Jour 3 :_

* _Conduire à Vicksburg, Mississippi et s'enregistrer à l'hôtel_
* _Visiter le Vicksburg National Military Park_
* _Nuit à Vicksburg_

_Jour 4 :_

* _Conduire à Tupelo, Mississippi et s'enregistrer à l'hôtel_
* _Visiter le Tupelo National Battlefield_
* _Nuit à Tupelo_

_Jour 5 :_

* _Conduire à Corinth, Mississippi et s'enregistrer à l'hôtel_
* _Visiter le Shiloh National Military Park_
* _Nuit à Corinth_

_Jour 6 :_

* _Conduire à Jackson, Mississippi et s'enregistrer à l'hôtel_
* _Visiter le Brices Cross Roads National Battlefield Site_
* _Nuit à Jackson_

_Jour 7 :_

* _Conduire à Gulf Islands National Seashore et s'enregistrer à l'hôtel_

## Corrections du code

Il y a quelques petits problèmes :

* Il s'arrête à la moitié du jour 7 alors que nous avons dit 8 jours.
* Les descriptions ne sont pas très intéressantes.

### Comment étendre la limite de jetons

La raison pour laquelle la réponse a été coupée est que nous avons initialement passé un `maxTokens: 200` dans notre commande AI. Cela devrait être une correction simple en augmentant ce nombre.

Nous pourrions le régler à un nombre très élevé comme 10 000, mais nous devons toujours payer pour tous les jetons générés. Le régler à 10 000 ne rendra pas chaque réponse longue de 10 000 jetons, mais avoir une limite plus raisonnable nous protège d'avoir une facture AWS inattendue.

Je règle le mien à 1000. Si vous voulez être sophistiqué, vous pourriez changer cela en fonction du nombre de jours qu'ils voyagent.

### Comment améliorer l'itinéraire

Cela est un peu plus difficile. Les problèmes sont qu'il est très fade et qu'il répète beaucoup de "conduire ici et s'enregistrer à l'hôtel", "Nuit à Y".

Nous pouvons essayer d'améliorer notre prompt pour obtenir un meilleur résultat. Tout d'abord, disons explicitement qu'il n'a pas besoin de nous parler de la conduite ou de l'enregistrement à l'hôtel.

```jsx
// Nouveau contenu
Ne pas écrire sur la conduite. Ne pas écrire sur l'enregistrement à l'hôtel. Ne pas écrire sur où passer la nuit.
```

Nous pouvons également demander un résultat plus descriptif. J'ai ajouté une autre ligne au prompt :

```jsx
Donnez une description des choses qu'ils verront et ce qu'il y a à faire dans chaque parc.

```

Un truc pour redéployer lorsque vous n'avez changé que le code est les déploiements de fonction. Vous pouvez exécuter `sls deploy function -f {nom de la fonction}` qui dans notre cas est `sls deploy function -f aiTourGuide`. Cela est beaucoup plus rapide que de redéployer toute l'application, vous permettant de tester plus tôt et donc d'itérer plus rapidement.

### Échec de l'amélioration

Ayant apporté cette modification, j'espérais que le résultat s'améliorerait, mais ce ne fut pas le cas. J'ai essayé environ 15 prompts différents et ils ont tous gardé la même structure et ignoré mes instructions de ne pas parler des hôtels, de la conduite ou de passer la nuit.

### Option 2 – changer d'autres paramètres

Avec l'IA donnant toujours une réponse très similaire et ennuyeuse, vous pouvez commencer à changer d'autres choses. Pour augmenter la créativité de l'IA, augmentez la température. Je suis passé à 0,8.

Cela devrait amener l'IA à sélectionner des mots plus inhabituels et à créer une réponse moins structurée et plus aléatoire.

Malheureusement, la réponse était presque identique.

### Option 3 – changer de modèle

L'une des choses géniales à propos de l'utilisation de Bedrock est qu'il existe plusieurs modèles à utiliser, et le passage de l'un à l'autre peut être très facile.

Nous avons utilisé le modèle `Jurassic-2 Mid` jusqu'à présent, mais il n'est pas à la hauteur de cette tâche. Peut-être qu'il est bon avec des prompts beaucoup plus petits ou des tâches plus simples. Pour l'instant, nous pouvons passer à l'utilisation de `Jurassic-2 Ultra`. La chose incroyable est que ce n'est qu'une ligne de code :

```jsx
const aiModelId = "ai21.j2-ultra-v1"; // utilisé pour être ai21.j2-mid-v1

```

Parce qu'ils proviennent de la même entreprise, ils ont des paramètres identiques. Si vous vouliez passer à l'un des autres modèles, vous devriez peut-être changer quelques autres options dans le corps de `invokeModelParams`.

Une chose que je conseille avec ce modèle plus grand est d'augmenter le délai d'expiration de Lambda. Par défaut, il est à 6s, mais parfois ce n'est pas suffisant.

```jsx
functions:
  aiTourGuide:
    handler: src/functions/aiTourGuide/index.handler
    timeout: 26  # < nouvelle ligne de config
    events:
      - httpApi:
          path: /tourguide
          method: post

```

## Les Résultats

Avec notre prompt mis à jour et notre nouveau modèle, nous obtenons un bien meilleur résultat :

_Jour 1 : 
Commencez votre voyage en explorant le Brices Cross Roads National Battlefield Site. Découvrez comment la victoire confédérée à Brices Cross Roads fut une victoire significative pour le Major Général Nathan Bedford Forrest, mais son effet à long terme sur la guerre s'avéra coûteux pour les Confédérés. Brices Cross Roads est un excellent exemple de victoire à la bataille, mais de défaite à la guerre._

_Jour 2 : 
Aujourd'hui, visitez l'Emmett Till and Mamie Till-Mobley National Monument. En 1955, Emmett Till, âgé de 14 ans, s'est rendu à Money, Mississippi, pour rendre visite à des parents. Il a été kidnappé, torturé et assassiné après avoir prétendument sifflé une femme blanche. Sa mère, Mamie Till-Mobley, a insisté pour des funérailles à cercueil ouvert près de leur ville natale de Chicago. Sa décision courageuse a permis au monde de voir la violence raciste infligée à son fils et a mis en mouvement le Mouvement des Droits Civiques._

_Jour 3 : 
Le Gulf Islands National Seashore est l'endroit idéal à visiter aujourd'hui. Des millions de visiteurs sont attirés par le Golfe du Mexique pour les eaux côtières émeraude du Gulf Islands National Seashore, ses magnifiques plages de sable blanc, ses marais fertiles et ses paysages historiques. Venez explorer avec nous aujourd'hui !_

_Jour 4 : 
Le Medgar and Myrlie Evers Home National Monument est le prochain sur la liste. Medgar et Myrlie Evers étaient des partenaires dans la lutte pour les droits civiques. L'assassinat de Medgar Evers dans le carport de leur maison le 12 juin 1963 fut le premier meurtre d'un leader nationalement significatif du Mouvement des Droits Civiques Américains, et il devint un catalyseur pour le passage de la loi sur les droits civiques de 1964. Myrlie Evers a continué à promouvoir les questions d'égalité raciale et de justice sociale._

_Jour 5 : 
Le Natchez National Historical Park est un excellent endroit à visiter aujourd'hui. Découvrez l'histoire de tous les peuples de Natchez, Mississippi, de la colonisation européenne, de l'esclavage africain, de l'économie cotonnière américaine, à la lutte pour les droits civiques sur le bas Mississippi._

_Jour 6 : 
Aujourd'hui, explorez le Natchez Trace National Scenic Trail. Le Natchez Trace National Scenic Trail est composé de cinq sections de sentiers de randonnée courant à peu près parallèlement à la route panoramique de 444 miles de long, le Natchez Trace Parkway. Les sentiers pédestres totalisent plus de 60 miles et offrent des opportunités d'explorer les zones humides, les marais, les forêts de feuillus, et l'histoire de la région. Pour savoir ce qui est ouvert et ce qui est fermé, visitez www.nps.gov/natr/planyourvisit/what-is-open-what-is-closed.htm_

_Jour 7 : 
Le Natchez Trace Parkway est l'endroit idéal à visiter aujourd'hui. Le Natchez Trace Parkway est une route récréative et panoramique de 444 miles à travers trois États. Il suit à peu près l'« Old Natchez Trace », un corridor de voyage historique utilisé par les Amérindiens, les « Kaintucks », les colons européens, les marchands d'esclaves, les soldats et les futurs présidents. Aujourd'hui, les gens peuvent profiter non seulement d'une route panoramique, mais aussi de randonnée, de vélo, d'équitation et de camping le long du Parkway._

_Jour 8 : 
Terminez votre voyage en explorant le Shiloh National Military Park. Visitez les sites de la lutte la plus épique dans le Théâtre Occidental de la Guerre Civile. Près de 110 000 troupes américaines se sont affrontées dans un combat sanglant qui a résulté en 23 746 victimes ; plus de victimes que dans toutes les guerres précédentes de l'Amérique combinées. Explorez les champs de bataille de Shiloh et de Corinth pour découvrir l'impact de cette lutte sur les soldats et sur la nation._

J'ai ensuite décidé de l'essayer avec les modèles Claude Instant pour voir comment il s'en sortait. Pour ce faire, vous devez changer les [paramètres du modèle passés](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html#model-parameters-claude), mais ce n'est pas très différent.

Comme vous pouvez le voir, ce modèle s'en sort aussi bien que le modèle `Jurassic-2 Ultra`, mais en regardant le tableau des prix, il est 10 fois moins cher pour les jetons d'entrée et 60 % du prix pour les jetons de sortie.

_Basé sur les descriptions fournies, voici un itinéraire de 8 jours axé sur les activités dans les parcs nationaux :_

_Jour 1 : Passez la matinée au Brices Cross Roads National Battlefield Site pour en apprendre davantage sur la victoire confédérée qui s'y est déroulée à travers des expositions et un court film. L'après-midi, visitez l'Emmett Till and Mamie Till-Mobley National Monument pour en apprendre davantage sur leur histoire et son impact sur le mouvement des droits civiques._

_Jour 2 : Consacrez la journée entière à explorer le Gulf Islands National Seashore. Faites de la randonnée ou du vélo le long des magnifiques sentiers côtiers, ramassez des coquillages sur la plage et observez la faune le long du rivage et dans les marais._

_Jour 3 : Passez la matinée à visiter le Medgar and Myrlie Evers Home National Monument et en apprendre davantage sur leur activisme pour les droits civiques. L'après-midi, visitez le Natchez National Historical Park pour découvrir l'histoire diverse de la région de Natchez à travers des bâtiments historiques, des sentiers de randonnée et des expositions._

_Jour 4 : Profitez d'une route panoramique le long du Natchez Trace Parkway, en vous arrêtant à divers points de vue pour des opportunités de photos. Envisagez de faire de la randonnée ou du vélo sur des portions du Natchez Trace National Scenic Trail adjacent pour une exploration plus active._

_Jour 5 : Plongez-vous dans l'histoire épique de la guerre civile du Shiloh National Military Park en visitant les sites de bataille et en apprenant sur la bataille sanglante de deux jours qui s'y est déroulée._

_Jour 6 : Passez la matinée au Tupelo National Battlefield pour en apprendre davantage sur la bataille de 1864 qui s'y est déroulée. L'après-midi, continuez vers le Vicksburg National Military Park pour un film d'introduction et une visite des vastes champs de bataille et fortifications._

_Jour 7 : Consacrez une autre journée entière à explorer davantage le Vicksburg NMP, comme faire une visite guidée par un ranger ou randonner sur des sentiers supplémentaires pour découvrir les nuances du long siège qui s'y est déroulé._

_Jour 8 : Avant de partir, envisagez de retourner dans un parc préféré de la semaine précédente pour une exploration supplémentaire ou pour voir ce que vous avez peut-être manqué initialement._

J'ai également testé le Claude v2, qui est plus avancé mais coûte également à peu près le même prix que le modèle Jurassic-2 Ultra. Cela n'a pas produit de réponse notablement meilleure, donc pour ce cas d'utilisation, je resterais définitivement avec le modèle Anthropic Claude Instant.

## Comment passer au niveau supérieur

C'est un très bon début pour un prompt aussi simple. Vous pourriez itérer dessus, l'améliorer et tester différents styles et formulations. Vous pourriez essayer de trouver d'autres sources d'informations à transmettre à votre prompt, car lui donner des informations utiles à utiliser dans la réponse est souvent le meilleur moyen d'améliorer les résultats de ces modèles.

## Comment utiliser ce processus dans d'autres applications

À travers ce processus, vous avez appris à construire une application qui exploite la puissance de l'IA. Vous pouvez maintenant suivre ce même processus pour ajouter de la puissance d'IA à vos propres applications AWS.

* Trouvez un cas d'utilisation où l'IA pourrait générer du contenu pour vous
* Rassemblez des données qui aideront l'IA à créer une meilleure réponse.
* Générez le prompt
* Appelez la fonction `InvokeModel` dans Bedrock
* Déployez et testez votre fonction d'IA
* Changez le prompt et les paramètres pour voir quels résultats donnent les meilleures réponses

## Comment en apprendre davantage sur le Serverless

Maintenant que vous savez comment intégrer l'IA dans vos applications, vous avez probablement plein d'idées d'applications.

Si vous voulez apprendre à construire le reste de cette idée, consultez mon [guide ultime du Serverless](https://completecoding.io/the-ultimate-guide-to-backend-serverless-development/) ou mon cours qui vous aide à [Maîtriser le Serverless en construisant 7 projets réels](https://serverlessmasterclass.com/7-serverless-projects?utm_source=freecodecamp&utm_medium=text).