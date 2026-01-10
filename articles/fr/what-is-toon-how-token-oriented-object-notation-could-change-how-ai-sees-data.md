---
title: Qu'est-ce que TOON ? Comment la Token-Oriented Object Notation pourrait changer
  la façon dont l'IA perçoit les données
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2025-11-13T15:23:51.254Z'
originalURL: https://freecodecamp.org/news/what-is-toon-how-token-oriented-object-notation-could-change-how-ai-sees-data
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1762978794293/e75f145b-a418-458e-8a41-12fe3add0107.png
tags:
- name: llm
  slug: llm
- name: AI
  slug: ai
- name: json
  slug: json
seo_title: Qu'est-ce que TOON ? Comment la Token-Oriented Object Notation pourrait
  changer la façon dont l'IA perçoit les données
seo_desc: 'JSON, or JavaScript Object Notation, was popularized by Douglas Crockford
  in early 2000. Since then, there’s been no looking back. JSON has become the standardized
  data exchange format between client and server technologies.

  JSON was built for humans...'
---


`JSON`, ou JavaScript Object Notation, a été popularisé par Douglas Crockford au début des années 2000. Depuis, il n'y a pas eu de retour en arrière. Le JSON est devenu le format d'échange de données standardisé entre les technologies client et serveur.

Le JSON a été conçu pour les humains. Il est lisible, accessible et universel pour que les API consomment des données ou renvoient des réponses. Mais à l'ère moderne de l'IA, un inconvénient du JSON est apparu au grand jour : il est assez verbeux.

Chaque accolade, chaque guillemet et chaque clé répétée consomme des tokens. Si vous passez du temps à créer des applications qui communiquent avec des grands modèles de langage (LLMs), vous savez probablement que les tokens sont la monnaie d'échange des interactions avec les LLM. Plus il y a de tokens, plus votre solution d'IA sera coûteuse.

Désormais, il y a un nouveau venu appelé `TOON` (Token-Oriented Object Notation). Il promet de permettre aux LLMs de communiquer avec des données structurées de manière plus efficace, intelligente et rentable.

Cet article est le résultat de ma curiosité lors de l'exploration de TOON. Je voulais comprendre pourquoi il est tendance, comment il fonctionne et comment vous pouvez l'utiliser aujourd'hui dans vos projets JavaScript/TypeScript et Python. J'espère que vous trouverez cela aussi passionnant que moi.

Vous pouvez trouver tout le code source utilisé dans cet article dans [ce dépôt GitHub](https://github.com/tapascript/toon-and-json).

## **Table des matières**

1. [Qu'est-ce que Toon ?](#heading-qu-est-ce-que-toon)
    
2. [Pourquoi TOON est-il important maintenant ?](#heading-pourquoi-toon-est-il-important-maintenant)
    
3. [JSON vs TOON - Apprendre par l'exemple](#heading-json-vs-toon-apprendre-par-l-exemple)
    
4. [Comment utiliser TOON avec JavaScript / TypeScript](#heading-comment-utiliser-toon-avec-javascript-typescript)
    
5. [Comment utiliser Toon avec Python ?](#heading-comment-utiliser-toon-avec-python)
    
6. [Attendez, JSON pourrait encore être préférable (dans de nombreux cas)](#heading-attendez-json-pourrait-encore-etre-preferable-dans-de-nombreux-cas)
    
7. [L'avenir de TOON](#heading-l-avenir-de-toon)
    
8. [Avant de terminer…](#heading-avant-de-terminer)
    

## Qu'est-ce que Toon ?

<a id="heading-qu-est-ce-que-toon"></a>
TOON est un nouveau format de sérialisation de données conçu avec un objectif de code :

> Réduire le nombre de tokens lors de l'échange de données structurées avec des modèles de langage.

Alors que le JSON utilise une syntaxe verbeuse avec des accolades, des guillemets et des virgules, TOON s'appuie sur un style tabulaire efficace en tokens, qui est beaucoup plus proche de la façon dont les LLMs comprennent naturellement les données structurées.

Faisons une comparaison rapide entre JSON et TOON :

Voici du JSON avec un tableau `users` qui contient des informations sur deux utilisateurs (deux objets) :

```json
{
  "users": [
    { "id": 1, "name": "Alice", "role": "admin" },
    { "id": 2, "name": "Bob", "role": "user" }
  ]
}
```

Si vous vouliez représenter les mêmes données en TOON, cela ressemblerait à ceci :

```json
users[2]{id,name,role}:
  1,Alice,admin
  2,Bob,user
```

Avez-vous remarqué les différences ?

* Pas de guillemets, d'accolades ou de deux-points dans TOON.
    
* Le `users[2]{id,name,role}:` déclare un tableau de deux objets avec les champs id, name et role.
    
* Les lignes ci-dessous sont simplement les lignes de données.
    

Vous pouvez voir que TOON a visiblement réduit l'utilisation des tokens de 30 à 50 %, selon la forme des données.

## Pourquoi TOON est-il important maintenant ?

<a id="heading-pourquoi-toon-est-il-important-maintenant"></a>
Les LLMs comme GPT, Gemini et Claude sont des systèmes basés sur les tokens. Chaque mot, symbole ou bloc coûte des tokens en entrée et en sortie. Ainsi, si vous préparez un LLM avec une entrée/sortie de données structurées comme ceci :

```json
{ "products": [ ... 300, "items" ... ] }
```

Vous pourriez gaspiller des milliers de tokens en guillemets, accolades, deux-points et clés répétées. TOON résout cela en se concentrant sur une représentation compacte mais structurée.

Certains des principaux avantages de TOON sont :

* 30 à 50 % de tokens en moins pour les ensembles de données uniformes.
    
* Il présente moins d'encombrement syntaxique, ce qui facilite le raisonnement des LLMs.
    
* Il peut être imbriqué comme nous le faisons avec JSON.
    
* Fonctionne bien avec des langages comme Python, Go, Rust et JavaScript.
    

TOON est un excellent complément au JSON, en particulier pour les projets d'IA, les LLMs et les prompts riches en données. Il ne remplacera peut-être pas entièrement le JSON, mais il convient aux cas d'utilisation où le JSON est considéré comme trop lourd pour l'échange de données.

## JSON vs TOON – Apprendre par l'exemple

<a id="heading-json-vs-toon-apprendre-par-l-exemple"></a>
Maintenant que vous avez une idée de base de ce que fait TOON et pourquoi il est utile, examinons certaines des structures JSON les plus utilisées et leur représentation équivalente en TOON.

### 1\. Un objet simple

Voici comment vous représenteriez un objet avec JSON :

```json
{ "name": "Alice", "age": 30, "city": "Bengaluru" }
```

Et voici comment cela fonctionne avec TOON :

```json
name: Alice
age: 30
city: Bengaluru
```

### 2\. Tableau de valeurs

Avec JSON :

```json
{ "colors": ["red", "green", "blue"] }
```

Avec TOON :

```json
colors[3]: red,green,blue
```

### 3\. Tableau d'objets

Avec JSON :

```json
{
  "users": [
    { "id": 1, "name": "Alice" },
    { "id": 2, "name": "Bob" }
  ]
}
```

Avec TOON :

```json
users[2]{id,name}:
  1,Alice
  2,Bob
```

Ici, `users[2]{id,name}` représente le schéma, et les lignes qui le suivent contiennent les lignes de données réelles.

![Schéma TOON](https://cdn.hashnode.com/res/hashnode/image/upload/v1762968459600/03584141-37ae-429d-a999-99ffb93acdcc.png align="center")

### 4\. Objets imbriqués

Avec JSON :

```json
{
  "user": {
    "id": 1,
    "name": "Alice",
    "profile": { "age": 30, "city": "Bengaluru" }
  }
}
```

Avec TOON :

```json
user:
  id: 1
  name: Alice
  profile:
    age: 30
    city: Bengaluru
```

L'indentation représente l'imbrication. C'est presque comme du YAML, mais c'est toujours structuré.

### 5\. Tableau d'objets avec champs imbriqués

Avec JSON :

```json
{
  "teams": [
    {
      "name": "Team Alpha",
      "members": [
        { "id": 1, "name": "Alice" },
        { "id": 2, "name": "Bob" }
      ]
    }
  ]
}
```

Avec TOON :

```json
teams[1]:
  - name: Team Alpha
    members[2]{id,name}:
      1,Alice
      2,Bob
```

C'est toujours parfaitement compréhensible et beaucoup plus petit que le format JSON.

Maintenant que vous en savez un peu plus sur la syntaxe TOON, voyons comment l'utiliser avec différents langages de programmation.

## Comment utiliser TOON avec JavaScript / TypeScript

<a id="heading-comment-utiliser-toon-avec-javascript-typescript"></a>
Dans la plupart des cas, TOON n'est pas destiné à être écrit à la main. La plupart des données TOON seront générées automatiquement par un logiciel, ou vous devrez encoder des données existantes (par exemple, des données JSON) au format TOON.

Et il y a une bonne nouvelle – [TOON](https://github.com/toon-format) possède déjà un package NPM officiel que vous pouvez utiliser dans votre projet JavaScript/TypeScript pour convertir vos données JSON en TOON et vice versa.

Installez-le à l'aide de la commande suivante :

```bash
npm install @toon-format/toon # Ou yarn add, pnpm install, etc
```

Le moyen le plus simple de créer du code TOON est de convertir du JSON en TOON. Vous pouvez utiliser la méthode `encode()` du package NPM mentionné ci-dessus :

```javascript
import { encode } from "@toon-format/toon";

const data = {
  users: [
    { id: 1, name: "Alice", role: "admin" },
    { id: 2, name: "Bob", role: "user" },
  ],
};

const toonString = encode(data);
console.log(toonString);
```

Sortie :

```json
users[2]{id,name,role}:
  1,Alice,admin
  2,Bob,user
```

Pour faire l'inverse (TOON => JSON), vous devez utiliser la méthode `decode()` :

```javascript
import { decode } from "@toon-format/toon";

const toonString = `
users[2]{id,name,role}:
  1,Alice,admin
  2,Bob,user
`;

const jsonObject = decode(toonString);
console.log(jsonObject);
```

Sortie :

```json
{
  "users": [
    { "id": 1, "name": "Alice", "role": "admin" },
    { "id": 2, "name": "Bob", "role": "user" }
  ]
}
```

Vous pouvez consulter [ce bac à sable](https://codesandbox.io/p/sandbox/javascript-forked-n4zsww) et essayer quelques exemples d'encodage et de décodage.

## Comment utiliser Toon avec Python ?

<a id="heading-comment-utiliser-toon-avec-python"></a>
L'utilisation de TOON dans les projets Python est aussi simple qu'avec JavaScript/TypeScript. Il existe des packages Python qui peuvent encoder des données JSON en TOON et les décoder en JSON. Le package `python-toon` est le plus célèbre ces derniers temps.

Tout d'abord, ouvrez votre terminal et installez le package `python-toon` :

```bash
pip install python-toon
```

Notez que si vous êtes dans un environnement virtuel, vous devrez d'abord l'activer :

```bash
python -m venv venv
source venv/bin/activate
pip install python-toon
```

C'est tout ! Vous êtes maintenant prêt à utiliser les méthodes pour encoder et décoder vos données vers et depuis TOON. Tout d'abord, encodons des données JSON en TOON en utilisant Python :

```python
from toon import encode

# Un objet channel
channel = {"name": "tapaScript", "age": 2, "type": "education"}
toon_output = encode(channel)
print(toon_output)
```

Sortie :

```json
name: tapaScript
age: 2
type: education
```

De même, nous pouvons décoder TOON en JSON :

```python
from toon import decode

toon_string = """
name: tapaScript
age: 2
type: education
"""

python_struct = decode(toon_string)
print(python_struct)
```

Sortie :

```json
{"name": "tapaScript", "age": 2, "type": "education"}
```

## Attendez, JSON pourrait encore être préférable (dans de nombreux cas)

<a id="heading-attendez-json-pourrait-encore-etre-preferable-dans-de-nombreux-cas"></a>
Soyons clairs : TOON n'est PAS un remplacement universel du JSON. En fait, vous devriez toujours préférer le JSON dans de nombreux cas, par exemple lorsque :

* Vos données sont profondément imbriquées.
    
* Vos données sont irrégulières (par exemple, des formes d'objets variables).
    
* Votre application nécessite des validations de schéma strictes ou l'application de types.
    
* Cas d'utilisation non liés à l'IA où le JSON se démarque toujours et fait parfaitement son travail.
    

Une approche hybride peut même mieux fonctionner. Conservez le JSON pour le format d'échange de données de votre application avec les API, mais convertissez-le en TOON lorsqu'il s'agit d'envoyer des données aux LLMs.

## L'avenir de TOON

<a id="heading-l-avenir-de-toon"></a>
TOON, bien qu'à ses débuts, attire beaucoup l'attention de la communauté des développeurs. Sa traction précoce rend impossible de ne pas en parler.

TOON a déjà été exploré pour :

* Moins de surcharge de tokens pour les données d'entraînement structurées afin de fine-tuner les LLMs.
    
* Échange de données compact dans les Frameworks d'agents.
    
* Sérialisation et désérialisation plus rapides des données entre le MCP et les moteurs de workflow d'IA.
    
* Avec les API d'IA Serverless, où le coût et la vitesse comptent beaucoup.
    

Tout comme le JSON a été un standard pour l'échange de données sur le Web, TOON pourrait bientôt être standardisé pour l'échange de données d'IA. Alors la prochaine fois que vous rédigerez un prompt ou que vous transmettrez des données structurées à un modèle d'IA, essayez le format TOON. Vous remarquerez peut-être que le modèle devient plus rapide et moins cher.

## Avant de terminer…

<a id="heading-avant-de-terminer"></a>
C'est tout ! J'espère que vous avez trouvé cet article instructif.

Restons connectés :

* Abonnez-vous à ma [chaîne YouTube](https://www.youtube.com/tapasadhikary?sub_confirmation=1).
    
* Découvrez mes cours GRATUITS, [40 Days of JavaScript](https://www.tapascript.io/courses/40-days-javascript) et [15 Days of React Design Patterns](https://www.tapascript.io/courses/react-design-patterns).
    
* Suivez-moi sur [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) si vous ne voulez pas manquer la dose quotidienne de conseils de montée en compétences.
    
* Rejoignez mon [serveur Discord](https://discord.gg/zHHXx4vc2H), et apprenons ensemble.
    

À bientôt pour mon prochain article. D'ici là, prenez soin de vous et continuez à apprendre.