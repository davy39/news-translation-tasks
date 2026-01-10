---
title: Création d'une application CRUD avec Express et MongoDB — Partie 2
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-02-03T23:53:43.000Z'
originalURL: https://freecodecamp.org/news/building-a-crud-application-with-express-and-mongodb-part-2-11d421bb0215
coverImage: https://cdn-media-1.freecodecamp.org/images/1*X0yjvqfSbtopiKwuOiUAsw.png
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: learning to code
  slug: learning-to-code
- name: MongoDB
  slug: mongodb
- name: Node.js
  slug: nodejs
seo_title: Création d'une application CRUD avec Express et MongoDB — Partie 2
seo_desc: 'By Zell Liew

  This article is the second part on creating a CRUD application with Express and
  MongoDB. We’re going to venture deep into the last two operations that were not
  covered in the first part — UPDATE and DELETE.

  Without further ado, let’s sta...'
---

Par Zell Liew

Cet article est la deuxième partie sur la création d'une application CRUD avec Express et MongoDB. Nous allons explorer en profondeur les deux dernières opérations qui n'ont pas été couvertes dans la [première partie](http://www.zell-weekeat.com/crud-express-mongodb/) — **MISE À JOUR** et **SUPPRESSION**.

Sans plus attendre, commençons la deuxième partie.

### CRUD — MISE À JOUR

L'opération **MISE À JOUR** est utilisée lorsque vous souhaitez changer quelque chose. Elle ne peut être déclenchée par les navigateurs que par une requête **PUT**. Comme la requête **POST**, la requête **PUT** peut être déclenchée soit par JavaScript, soit par un élément <form>.

Essayons de déclencher une requête **PUT** via JavaScript cette fois, puisque nous avons déjà appris à déclencher une requête via un élément <form> en traitant la requête POST dans l'article précédent.

Pour les besoins de ce tutoriel, nous allons créer un bouton qui, lorsqu'on clique dessus, remplacera la dernière citation écrite par Maître Yoda par une citation écrite par Dark Vador.

Pour ce faire, nous ajoutons d'abord un bouton dans le fichier index.ejs :

```
<div>  <h2>Remplacer la dernière citation écrite par Maître Yoda par une citation écrite par Dark Vador</h2>  <button id="update"> Dark Vador envahit ! </button></div>
```

Nous allons également créer un fichier JavaScript externe pour exécuter la requête **PUT** lorsque le bouton est cliqué. Selon les conventions d'Express, ce fichier est placé dans un dossier appelé public

```
$ mkdir public
$ touch public/main.js
```

Ensuite, nous devons dire à Express de rendre ce dossier public accessible au public en utilisant un middleware intégré appelé express.static

```
app.use(express.static('public'))
```

Une fois cela fait, nous pouvons ajouter le fichier main.js au fichier index.ejs :

```
<!-- ... -->
<script src="main.js"></script>
</body>
```

Ensuite, nous allons envoyer la requête **PUT** lorsque le bouton est cliqué :

```
// main.js
var update = document.getElementById('update')
```

```
update.addEventListener('click', function () {  // Envoyer la requête PUT ici})
```

La manière la plus simple de déclencher une requête **PUT** dans les navigateurs modernes est d'utiliser l'[API Fetch](https://developer.mozilla.org/en/docs/Web/API/Fetch_API). Elle n'est prise en charge que sur [Firefox, Chrome et Opera](http://caniuse.com/#search=fetch), vous pourriez donc vouloir utiliser un [polyfill](https://github.com/github/fetch) si vous souhaitez utiliser Fetch sur un projet réel.

Nous allons envoyer la requête fetch suivante au serveur. Jetez-y un coup d'œil rapide et je vous expliquerai ce que tout cela signifie :

```
fetch('quotes', {  method: 'put',  headers: {'Content-Type': 'application/json'},  body: JSON.stringify({    'name': 'Darth Vader',    'quote': 'I find your lack of faith disturbing.'  })})
```

Prêt à comprendre pourquoi la requête Fetch est écrite de cette manière ? :)

Fetch prend deux paramètres. **Le premier paramètre** est un chemin. Dans ce cas, nous envoyons la requête à /quote, qui sera gérée sur notre serveur.

**Le deuxième paramètre, options,** est un objet optionnel qui vous permet de contrôler un certain nombre de paramètres différents. Ceux que nous avons utilisés ci-dessus sont method, headers et body.

Nous avons défini la méthode sur "put" car nous envoyons une requête PUT.

"Headers" ici fait référence aux [en-têtes HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) que vous souhaitez envoyer au serveur. Il s'agit d'un objet avec plusieurs paires clé-valeur.

"Body" fait référence au contenu que vous envoyez au serveur.

Une chose que vous avez peut-être remarquée est que nous avons défini le Content-Type sur application/json. Nous avons également converti la citation de Dark Vador en JSON dans le body avec JSON.stringify. Nous effectuons ces étapes car nous envoyons la citation de Dark Vador au format JSON (un format standard pour envoyer des informations sur le web) au serveur.

Malheureusement, notre serveur ne lit pas encore les données JSON. Nous pouvons lui apprendre à lire les données JSON en utilisant le middleware bodyparser.json() :

```
app.use(bodyParser.json())
```

Une fois que nous avons fait tout ce qui précède, nous pourrons gérer cette requête **PUT** en utilisant la méthode put :

```
app.put('/quotes', (req, res) => {  // Gérer la requête put })
```

L'étape suivante consiste alors à apprendre à rechercher la dernière citation de Maître Yoda et à la remplacer par une citation de Dark Vador dans MongoDB.

### Mise à jour d'une collection dans MongoDB

Les collections MongoDB disposent d'une méthode appelée findOneAndUpdate qui nous permet de modifier un élément de la base de données. Elle prend quatre paramètres — query, update, options et un callback.

```
db.collections('quotes').findOneAndUpdate(  query,   update,   options,  callback)
```

**Le premier paramètre, query**, nous permet de filtrer la collection à travers des paires clé-valeur qui lui sont données. Nous pouvons filtrer la collection de citations pour les citations de Maître Yoda en définissant le nom sur Yoda.

```
{  name: 'Yoda'}
```

**Le deuxième paramètre, update**, indique à MongoDB quoi faire avec la requête de mise à jour. Il utilise les [opérateurs de mise à jour](https://docs.mongodb.org/manual/reference/operator/update/) de MongoDB comme $set, $inc et $push. Nous utiliserons l'opérateur $set puisque nous changeons les citations de Yoda en citations de Dark Vador :

```
{  $set: {    name: req.body.name,    quote: req.body.quote  }}
```

**Le troisième paramètre, options**, est un paramètre optionnel qui vous permet de définir des éléments supplémentaires. Puisque nous recherchons la dernière citation de Yoda, nous définirons sort dans les options sur {_id: -1}. Cela permet à MongoDB de rechercher dans la base de données, en commençant par l'entrée la plus récente.

```
{  sort: {_id:-1}}
```

Il est possible qu'il n'y ait aucune citation de Maître Yoda dans notre base de données. MongoDB ne fait rien par défaut lorsque cela se produit. Nous pouvons le forcer à créer une nouvelle entrée si nous définissons l'option upsert, qui signifie insert (ou save) si aucune entrée n'est trouvée, sur true :

```
{  sort: {_id: -1},  upsert: true}
```

**Le dernier paramètre est une fonction de callback** qui vous permet de faire quelque chose une fois que MongoDB a remplacé la dernière citation de Yoda par une citation de Dark Vador. Dans ce cas, nous pouvons envoyer les résultats à la requête fetch.

```
(err, result) => {  if (err) return res.send(err)  res.send(result)}
```

Voici la commande findOneAndUpdate complète que nous avons écrite au cours des dernières étapes :

```
app.put('/quotes', (req, res) => {  db.collection('quotes')  .findOneAndUpdate({name: 'Yoda'}, {    $set: {      name: req.body.name,      quote: req.body.quote    }  }, {    sort: {_id: -1},    upsert: true  }, (err, result) => {    if (err) return res.send(err)    res.send(result)  })})
```

Maintenant, chaque fois que quelqu'un clique sur le bouton de mise à jour, le navigateur enverra une requête _PUT_ via Fetch à notre serveur Express. Ensuite, le serveur répond en envoyant la citation modifiée à fetch. Nous pouvons alors gérer la réponse en enchaînant fetch avec une méthode then. Cela est possible car Fetch retourne un objet [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

La manière appropriée de [vérifier si fetch s'est résolu avec succès](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#Checking_that_the_fetch_was_successful) est d'utiliser la méthode ok sur l'objet de réponse. Vous pouvez ensuite retourner res.json() si vous souhaitez lire les données envoyées par le serveur :

```
fetch({ /* request */ }).then(res => {  if (res.ok) return res.json()}).then(data => {  console.log(data)})
```

Si vous travaillez sur une application web sophistiquée, c'est ici que vous utilisez JavaScript pour mettre à jour le DOM afin que les utilisateurs puissent voir les nouvelles modifications immédiatement. La mise à jour du DOM est hors du cadre de cet article, nous allons donc simplement actualiser le navigateur pour voir les modifications.

```
fetch({ /* request */ }).then(res => {  if (res.ok) return res.json()}).then(data => {  console.log(data)  window.location.reload(true)})
```

C'est tout pour l'opération **CREATE** ! Passons à la dernière — **DELETE**.

### CRUD — SUPPRESSION

L'opération **SUPPRESSION** ne peut être déclenchée que par une requête **DELETE**. Elle est similaire à la requête **UPDATE**, donc elle est simple si vous comprenez ce que nous avons fait précédemment.

Pour cette partie, apprenons à supprimer la première citation de Dark Vador. Pour ce faire, nous devons d'abord ajouter un bouton au fichier index.ejs.

```
<div>  <h2>Supprimer la première citation de Dark Vador</h2>  <button id="delete"> Supprimer la première citation de Dark Vador </button></div>
```

Ensuite, nous déclencherons une requête **DELETE** via Fetch chaque fois que le bouton de suppression est cliqué :

```
var del = document.getElementById('delete')
```

```
del.addEventListener('click', function () {  fetch('quotes', {    method: 'delete',    headers: {      'Content-Type': 'application/json'    },    body: JSON.stringify({      'name': 'Darth Vader'    })  })  .then(res => {    if (res.ok) return res.json()  }).  then(data => {    console.log(data)    window.location.reload()  })})
```

Nous pouvons ensuite gérer l'événement côté serveur avec la méthode delete :

```
app.delete('/quotes', (req, res) => {  // Gérer l'événement de suppression ici})
```

### Suppression d'une entrée dans MongoDB

Les collections MongoDB disposent d'une méthode appelée findOneAndDelete qui nous permet de supprimer un élément de la base de données. Elle prend trois paramètres — query, options et un callback. Ces paramètres sont exactement les mêmes que ceux que nous avons utilisés dans findOneAndUpdate lors de la mise à jour d'une entrée dans MongoDB. La seule différence ici est qu'il n'y a pas d'upsert dans les options.

```
db.collections('quotes').findOneAndDelete(  query,   options,  callback)
```

Rappelons que nous essayons de supprimer la première citation de Dark Vador. Pour ce faire, nous filtrons la collection de citations par le nom, « Dark Vador ». Le paramètre query est donc :

```
{  name: req.body.name}
```

Nous pouvons sauter le paramètre options puisque nous n'avons pas à inverser l'ordre de tri. Ensuite, nous pouvons envoyer une réponse à la requête Fetch dans la fonction de callback.

```
(err, result) => {  if (err) return res.send(500, err)  res.send('Une citation de Dark Vador a été supprimée')})
```

Le code complet pour le gestionnaire de suppression est le suivant :

```
app.delete('/quotes', (req, res) => {  db.collection('quotes').findOneAndDelete({name: req.body.name},   (err, result) => {    if (err) return res.send(500, err)    res.send('Une citation de Dark Vador a été supprimée')  })})
```

Maintenant, chaque fois que quelqu'un clique sur le bouton de suppression, le navigateur enverra une requête _DELETE_ via Fetch à notre serveur Express. Ensuite, le serveur répond en envoyant soit une erreur, soit un message.

Comme précédemment, nous pouvons recharger le site web lorsque la requête fetch est terminée avec succès.

```
fetch({ /* request */ }).then(res => {  if (res.ok) return res.json()}).then(data => {  console.log(data)  window.location.reload(true)})
```

C'est tout pour l'opération **DELETE** !

### Conclusion

Vous avez maintenant appris tout ce que vous devez savoir sur la création d'applications simples avec Node et MongoDB. Maintenant, allez de l'avant et créez plus d'applications, jeune padawan. Que la force soit avec vous.