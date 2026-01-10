---
title: Comment créer une compétence Alexa qui gère des listes de tâches
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-31T22:03:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-alexa-skill-that-manages-to-do-lists-11c4bab29ea5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ct9YdVEA2z92Z8CGLWz2Zg.jpeg
tags:
- name: Amazon
  slug: amazon
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment créer une compétence Alexa qui gère des listes de tâches
seo_desc: 'By Terren Peterson

  I’m recognized as an Amazon Alexa Champion and have published more than twenty custom
  skills on the platform. I continue to look for new ways to stretch this technology,
  and one recent area I’ve been exploring is using Alexa to hel...'
---

Par Terren Peterson

Je suis reconnu comme un [Alexa Champion](https://developer.amazon.com/alexa/champions/terren-peterson) d'Amazon et j'ai publié plus de vingt compétences personnalisées sur la plateforme. Je continue de chercher de nouvelles façons d'explorer cette technologie, et un domaine récent que j'ai exploré est l'utilisation d'Alexa pour aider à organiser les tâches quotidiennes. L'une des fonctionnalités sous-utilisées sur la plateforme est la capacité de créer des listes personnalisées. [Voici](https://www.amazon.com/gp/help/customer/display.html/ref=cssoc_TW_HP_201549900?nodeId=201549900) un bref aperçu de la manière dont vous pouvez tirer parti de cette fonctionnalité, et n'hésitez pas à tester la [Compétence Planificateur d'Entraînement](https://www.amazon.com/Drawrz-com-Workout-Planner/dp/B07CLY496R/) — c'est gratuit !

![Image](https://cdn-media-1.freecodecamp.org/images/-c8VTjSI7FO9iKgSF0uJGSgM79Z3uAin9Yqp)
_Compétence Planificateur d'Entraînement Alexa_

### Contexte

Les appareils sans les mains comme Alexa ouvrent des possibilités de construire des assistants numériques pratiques. L'une des premières fonctionnalités activées avec l'appareil natif était la capacité de créer des listes de courses. Étant donné l'héritage de vente au détail d'Amazon, il n'est pas surprenant que cela soit arrivé tôt. Dire des phrases comme « ajoute du shampoing à ma liste de courses » l'ajoute au compte Amazon de l'utilisateur. Cela rend également les données sur d'autres applications auxquelles l'utilisateur est connecté.

### Ne pas amener Alexa à la salle de sport, amenez une liste

Après avoir utilisé la fonctionnalité de liste de courses pendant un certain temps, j'ai commencé à penser à d'autres types de listes que je pourrais créer. L'appareil a la capacité de créer des listes personnalisées, et j'ai pensé que cela pourrait être utile pour organiser mes entraînements. Plutôt que d'apporter une liste d'entraînement écrite à la main, je pourrais en créer une en utilisant ma voix.

J'ai écrit une compétence Alexa personnalisée appelée Planificateur d'Entraînement qui posait des questions sur les types d'exercices à faire. Elle créait ensuite une liste pour que je puisse suivre. Voici une capture d'écran de ce que la compétence crée sur mon téléphone.

![Image](https://cdn-media-1.freecodecamp.org/images/vXvBbsfZotdq7rK2QmR4HgQVo5XnN05li9jE)

### Architecture pour utiliser les listes Alexa

La fonctionnalité principale autour des listes est activée via une [API Alexa](https://api.amazonalexa.com/v2/householdlists/) qui gère les entités rendues sur l'application compagnon Alexa.

Dans une architecture typique de compétence Alexa, l'API est invoquée à partir de la fonction Lambda qui contient la fonctionnalité de la compétence. Les données passées dans l'appel d'API indiquent si une nouvelle liste doit être créée, quel élément doit être ajouté, si un élément peut être coché sur la liste, et ainsi de suite. L'application compagnon gère toutes les interactions de l'utilisateur avec les données de la liste, sans effort supplémentaire de la part du développeur de la compétence. L'utilisateur a ensuite la possibilité de gérer cette liste via l'application compagnon, y compris de cocher les éléments comme terminés.

![Image](https://cdn-media-1.freecodecamp.org/images/874aizqiQKmCFc2G1-LqjQRYyBW8YRvVb1TR)

L'interface vocale est la même que pour toute compétence Alexa. La création d'une compétence personnalisée inclut la configuration d'énoncés d'exemple, d'intentions, etc., en fonction de la fonctionnalité fournie à l'utilisateur.

### Activation des permissions pour utiliser les listes

Lors de la création d'une compétence avancée comme celle-ci, la compétence devra demander des permissions supplémentaires. Il existe plusieurs niveaux de permissions et de sécurité, qui doivent tous être en place pour que la compétence fonctionne pleinement.

Tout d'abord, le développeur de la compétence devra reconnaître à la plateforme Alexa que la compétence utilisera les listes. Vous pouvez faire cela dans la configuration de la compétence dans la console du développeur. La capture d'écran ci-dessous provient de l'onglet Permissions dans la console. Les curseurs pour les deux attributs de liste doivent être définis.

![Image](https://cdn-media-1.freecodecamp.org/images/crX24atn1zXmoeXyKHF25te6VHPTqLbPVjBO)
_Identification des permissions supplémentaires nécessaires pour cette compétence personnalisée dans la console du développeur Alexa_

Lorsque la compétence passe par la certification, Amazon valide que les permissions sont requises pour que la compétence fonctionne. Cela aide à gérer l'accès aux données de l'utilisateur qui seront obtenues par le développeur.

Deuxièmement, lorsqu'un utilisateur active la compétence sur son appareil, il devra accorder son consentement pour que la compétence puisse lire et écrire ses données pour son compte. Cela est activé via l'application compagnon, et suit un modèle « opt-in » pour accéder aux privilèges escaladés. Ci-dessous se trouve une capture d'écran des curseurs qui doivent être ajustés dans les paramètres.

![Image](https://cdn-media-1.freecodecamp.org/images/lJTQ0BACYmViOPhC0Vlfn4BpV0LjT9vUYTOG)
_Chaque utilisateur devra accorder des permissions pour accéder à ses données de liste._

Enfin, à l'exécution, un jeton de consentement est créé pour chaque session qui utilise la compétence. Ce jeton doit être enregistré par la fonction Lambda, puis passé dans l'en-tête de l'appel d'API à Alexa.

### Exemple d'appel d'API

Comme mis en évidence dans l'architecture, l'API household contient la fonctionnalité principale requise pour gérer les listes. Il existe plusieurs opérations disponibles dans l'API, et voici la documentation d'Amazon. En utilisant Node.js, voici le code utilisé pour invoquer l'API en utilisant l'opération POST qui crée une nouvelle liste appelée « Suivi d'Entraînement ».

```
var path = "/v2/householdlists/";     var postData = {        "name": "Workout Tracker", //valeur de l'élément, avec une description de chaîne jusqu'à 256 caractères         "state": "active" // statut de l'élément (Enum: "active" uniquement)    };            var consent_token = session.user.permissions.consentToken;
```

```
var options = {        host: api_url,        port: api_port,        path: path,        method: 'POST',        headers: {            'Authorization': 'Bearer ' + consent_token,            'Content-Type': 'application/json'        }    };
```

```
var req = https.request(options, (res) => {    console.log('statusCode:', res.statusCode);    console.log('headers:', res.headers);    var data = "";
```

```
    res.on('data', (d) => {         console.log("données reçues:" + d);         data += d;    });    res.on('error', (e) => {         console.log("erreur reçue");         console.error(e);    });    res.on('end', function() {         console.log("fin de la requête post");        if (res.statusCode === 201) {             var responseMsg = eval('(' + data + ')');             console.log("nouvel identifiant de liste:" + responseMsg.listId);             callback(res.statusCode, responseMsg.listId);        } else {             callback(res.statusCode, 0);        }    });});    req.end(JSON.stringify(postData));
```

L'API retourne un objet JSON qui inclut l'identifiant de liste utilisé dans les appels ultérieurs pour ajouter des éléments à la liste.

### Conclusion

C'est une manière facile de tirer parti de l'interface utilisateur vocale d'Alexa avec l'ubiquité de l'application compagnon Alexa. [Voici un lien](https://github.com/terrenjpeterson/workout-planner) vers le dépôt complet de la compétence, et si vous avez des idées sur la manière de l'améliorer — faites-le moi savoir !