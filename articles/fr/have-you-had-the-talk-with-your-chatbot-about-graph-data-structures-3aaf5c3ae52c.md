---
title: Avez-vous eu « La Discussion » avec votre chatbot sur les structures de données
  de graphes ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-19T00:28:53.000Z'
originalURL: https://freecodecamp.org/news/have-you-had-the-talk-with-your-chatbot-about-graph-data-structures-3aaf5c3ae52c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AeUDHuLM_pyfNZ3ZP5znyQ.png
tags:
- name: '#chatbots'
  slug: chatbots
- name: graph database
  slug: graph-database
- name: IBM Watson
  slug: ibm-watson
- name: Recommendation System
  slug: recommendation-system
- name: Web Development
  slug: web-development
seo_title: Avez-vous eu « La Discussion » avec votre chatbot sur les structures de
  données de graphes ?
seo_desc: 'By Mark Watson

  A coming-of-age story for your database model


  _Image credit: [Charlotte Parent](http://www.charlotteparent.com/CLT/Health-Development/More-Than-the-Birds-and-the-Bees-Teaching-Your-Child-About-Healthy-Sexuality/"
  rel="noopener" target...'
---

Par Mark Watson

#### Une histoire de passage à l'âge adulte pour votre modèle de base de données

![Image](https://cdn-media-1.freecodecamp.org/images/1*AeUDHuLM_pyfNZ3ZP5znyQ.png)
_Crédit image : [Charlotte Parent](http://www.charlotteparent.com/CLT/Health-Development/More-Than-the-Birds-and-the-Bees-Teaching-Your-Child-About-Healthy-Sexuality/" rel="noopener" target="_blank" title=")_

Les bases de données de graphes sont un excellent moyen de stocker des données conversationnelles. Un simple [arbre de dialogue](https://en.wikipedia.org/wiki/Dialog_tree) peut ajouter de la profondeur aux interactions de caractères dans un jeu vidéo. Un [graphe de connaissances](http://www.aclweb.org/anthology/N15-1086) peut extraire plus de sens du dialogue pour mieux comprendre comment l'intention de l'utilisateur se rapporte aux données d'une application.

Dans cet article, je vais vous montrer un modèle de graphe de base pour capturer les interactions de chatbot et comment les persister en utilisant le framework [Apache TinkerPop](https://tinkerpop.apache.org/). Je vais également vous montrer quelques requêtes [Gremlin](http://tinkerpop.apache.org/gremlin.html) pour ajouter une fonctionnalité de recommandation au chatbot. Le code source et les instructions d'installation pour mon exemple « Recipe Bot » sont [sur GitHub](https://github.com/ibm-cds-labs/watson-recipe-bot-nodejs-graph).

### Révision : Recipe Bot

Recipe Bot est un [utilisateur bot Slack](https://api.slack.com/bot-users) qui permet aux gens de demander des recettes basées sur des ingrédients ou des cuisines spécifiés. Précédemment, je vous ai montré comment ajouter un support pour que les utilisateurs demandent leurs recettes préférées, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*SjILWmRnPN3sSdr133pHRg.png)

La version graphique du bot a toutes les mêmes fonctionnalités dont j'ai discuté dans mon [article précédent sur la persistance des métadonnées avec JSON](https://medium.com/ibm-watson-data-lab/persisting-data-for-a-smarter-chatbot-be599480f7b2#.jvmry69xz), mais avec la version graphique, vous allez ajouter des recommandations.

### Comment cela fonctionne avec TinkerPop

Voici un diagramme d'architecture de la façon dont le bot fonctionne :

![Image](https://cdn-media-1.freecodecamp.org/images/1*uGXlWtFX65TWPtvpKUkWGg.png)
_Mon Recipe Bot. Hé ! Le diagramme est en fait un [graphe non orienté](https://en.wikipedia.org/wiki/Graph_theory" rel="noopener" target="_blank" title="). Qui l'eût cru ?_

Vous verrez que j'utilise le service Watson Conversation. Watson Conversation me permet de décrire le flux de la conversation à travers l'utilisation de dialogues, et il m'aide à extraire des informations et l'intention de l'utilisateur à partir des messages de chat. Vous pouvez coder votre propre arbre de dialogue et effectuer votre propre analyse de messages, ou vous pouvez utiliser des outils comme Watson Conversation ou Botkit pour vous aider. Voici comment l'arbre de dialogue pour Recipe Bot est modélisé :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qaJL5vQGKkhUCShVpiusGg.png)
_L'interface utilisateur de Watson Conversation. Les graphes sont partout._

Vous pouvez suivre une conversation à travers l'arbre de dialogue de manière similaire à la façon dont vous pouvez suivre les sommets et les arêtes dans un graphe (après tout, [les arbres sont des graphes](https://en.wikipedia.org/wiki/Tree_(graph_theory)) aussi) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fzxYyM3iP9Qc08yu4spt_g.png)
_Ce n'est pas vraiment un arbre, mais je le garde simple, les gars._

Dans le graphe simplifié ci-dessus, Recipe Bot ne se soucie que de la progression entre les principales entités du bot :

1. Personnes
2. Ingrédients
3. Cuisines
4. Recettes

### Modèle de données et motif d'accès

Au fur et à mesure que la conversation progresse, vous stockez les sommets et les arêtes suivants en utilisant l'API TinkerPop :

1. **Sommet Personne :** Pour chaque personne qui interagit avec le bot, stockez cette personne en tant que sommet dans le graphe.

```
{  "label": "person",  "type": "vertex",  "properties": {    "name": "U2JBLUPL2"  }}
```

**2. Sommet Ingrédient ou Cuisine :** Lorsqu'une personne demande un ingrédient ou une cuisine spécifique, vous stockez cet ingrédient ou cette cuisine — ainsi que la liste des recettes récupérées depuis [Spoonacular](https://spoonacular.com/food-api) — en tant que sommet.

```
{  "label": "cuisine",  "type": "vertex",  "properties": {    "name": "chinese",    "detail": "[{\"id\": 573147, \"title\": \"Kale Fried Rice\"..."  }}
```

**3. Arête Sélectionne, personne → (ingrédient | cuisine) :** Vous créez une arête, étiquetée `"selects"`, entre la personne et l'ingrédient ou la cuisine (c'est-à-dire, « personne sélectionne cuisine »). De plus, stockez une propriété `"count"` sur l'arête et incrémentez sa valeur chaque fois que l'utilisateur demande le même ingrédient ou la même cuisine.

```
{  "label": "selects",  "type": "edge",  "inV": 4152,  "outV": 4224,  "properties": {    "count": 3  }}
```

4. **Sommet Recette :** Lorsqu'un utilisateur demande une recette, stockez la recette en tant que sommet.

```
{  "label": "recipe",  "type": "vertex",  "properties": {    "name": "573147",    "detail": "Ok, il faut *45* minutes pour préparer...*",    "title": "Kale Fried Rice"  }}
```

5. **Arête Sélectionne, (ingrédient | cuisine) → recette :** Vous créez une autre arête `"selects"` entre l'ingrédient ou la cuisine et la recette (c'est-à-dire, « cuisine sélectionne recette »). De plus, stockez une propriété `"count"` sur l'arête et incrémentez-la chaque fois que l'ingrédient ou la cuisine sélectionne la même recette.

```
{  "label": "selects",  "type": "edge",  "inV": 4320,  "outV": 4152,  "properties": {    "count": 22  }}
```

**6. Arête Sélectionne, personne → recette :** Vous créez encore une autre arête `"selects"` directement entre la personne et la recette (c'est-à-dire, « personne sélectionne recette »). Stockez une propriété `"count"` sur l'arête et incrémentez-la chaque fois qu'une personne demande la même recette.

```
{  "label": "selects",  "type": "edge",  "inV": 4320,  "outV": 4224,  "properties": {    "count": 4  }}
```

**7. Arête A, recette → (ingrédient | cuisine) :** Enfin, créez une arête, étiquetée `"has"`, entre la recette et l'ingrédient ou la cuisine (c'est-à-dire, « recette a cuisine »). Cette relation vous permet de trouver tous les ingrédients et cuisines qu'une recette utilise. Il n'y a pas de champ count sur cette arête.

```
{  "label": "has",  "type": "edge",  "inV": 4152,  "outV": 4320}
```

Le graphe pour un seul utilisateur ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*h6fvJxvuKB_6EVn-w1itTg.png)
_Ce graphe a tout pour lui. C'est un [graphe (faiblement) connecté](https://en.wikipedia.org/wiki/Connectivity_%28graph_theory%29#Definitions_of_components.2C_cuts_and_connectivity" rel="noopener" target="_blank" title="). Il existe toutes sortes de graphes._

Jusqu'à présent, en utilisant une base de données de graphes, vous obtenez les avantages suivants :

1. Réduisez les appels d'API tiers en mettant en cache les entités.
2. Offrez une expérience plus personnelle aux utilisateurs en exploitant les métadonnées sur leurs interactions.

Une « expérience plus personnelle » pour Recipe Bot signifie permettre aux utilisateurs de demander leurs recettes préférées. Pour trouver les recettes préférées d'un utilisateur, vous utilisez le langage de [parcours de graphe](http://tinkerpop.apache.org/docs/current/reference/#traversal) Gremlin. La requête Gremlin suivante vous donnera les cinq recettes préférées d'un utilisateur, triées par compte :

### Ajout de recommandations

Puisque vous suivez chaque interaction utilisateur avec le bot sous forme de graphe, vous pouvez trouver les ingrédients, cuisines ou recettes populaires demandés par tous les utilisateurs. Vous pouvez utiliser Gremlin pour trouver des recettes populaires basées sur un ingrédient ou une cuisine. Voici comment cela fonctionne :

Supposons qu'un utilisateur cherche des recettes qui utilisent des oignons :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Yf49Io2lbpZeHrsvfyMxLA.png)

Vous pouvez trouver des recettes populaires qui utilisent des oignons en émettant la requête suivante. (Je vais la détailler plus bas — ne vous inquiétez pas !) :

Cette requête dit : « Donnez-moi n'importe qui, à l'exclusion de l'utilisateur appelant, qui a demandé des recettes plus d'une fois qui contiennent des oignons. » Elle se décompose comme suit :

1. Commencez avec `"onions"` :

```
g.V().hasLabel("ingredient").has("name","onions")
```

2. Obtenez les recettes qui contiennent `"onions"`. Cet appel d'API utilise l'arête `"has"` venant du sommet de recette vers le sommet d'ingrédient. L'utilisation de `.in()` saute l'arête et ne retourne que le sommet de recette. (Vous n'avez pas besoin de propriétés de l'objet arête, donc il n'y a aucune raison de le retourner ici.)

```
.in("has")
```

3. Obtenez les utilisateurs qui ont demandé ces recettes plus d'une fois. Cet appel utilise l'arête `"selects"` venant de la personne vers la recette :

```
.inE().has("count",gt(1)).order().by("count", decr)
```

4. Obtenez les utilisateurs, à l'exclusion de l'utilisateur actuel :

```
.outV().hasLabel("person").has("name",neq("CURRENT_USER"))
```

5. Obtenez le chemin complet :

```
.path()
```

Cet appel retourne un tableau de chemins correspondants qui ressemble à ceci :

> ingredient ← recipe ← edge ← person

Vous pouvez accéder à ces recettes recommandées à l'index 1.

Lorsque vous retournez cette liste de recettes à l'utilisateur, l'application place les recettes recommandées en haut et met en évidence le nombre d'utilisateurs qui ont précédemment utilisé chaque recette :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HS0ft98ZPG4AezihLIHnFA.png)

### Qu'est-ce qui suit ?

Essayez un déploiement par vous-même. Le [README du projet](https://github.com/ibm-cds-labs/watson-recipe-bot-nodejs-graph#watson-recipe-bot--ibm-graph) contient des instructions étape par étape pour compléter votre premier déploiement sur IBM Bluemix. Il existe également un [port Java](https://github.com/ibm-cds-labs/watson-recipe-bot-java-graph) de l'application exemple.

Si vous utilisez déjà un arbre de dialogue dans vos applications et que vous souhaitez utiliser une base de données de graphes pour persister les métadonnées sur les interactions, j'espère que le code source dans le dépôt ci-dessus vous donne quelques idées pour offrir des expériences plus personnalisées à vos utilisateurs.

Et si vous avez apprécié cet article, n'hésitez pas à cliquer sur le vieux ♥ afin que d'autres utilisateurs de Medium puissent le trouver et l'apprécier aussi. Bon codage !