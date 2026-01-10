---
title: 'Firestore : Comment rester dans les limites de la nouvelle offre gratuite
  de la base de données Firebase'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-11T21:48:00.000Z'
originalURL: https://freecodecamp.org/news/firestoreliving
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ec5740569d1a4ca3ef8.jpg
tags:
- name: Cloud Services
  slug: cloud-services
- name: database
  slug: database
- name: Firebase
  slug: firebase
- name: Free Software
  slug: free-software
seo_title: 'Firestore : Comment rester dans les limites de la nouvelle offre gratuite
  de la base de données Firebase'
seo_desc: "By Jeff M Lowery\nI recently started a personal project where I wanted\
  \ to use a database in the cloud. There are quite a few to choose from. My main\
  \ criteria was that it be something low or no cost. \nEventually I decided on Firestore,\
  \ using the Spark ..."
---

Par Jeff M Lowery

[J'ai récemment commencé un projet personnel](https://www.freecodecamp.org/news/netlify-functions-firebase-and-graphql-working-together-at-last/) où je voulais utiliser une base de données dans le cloud. Il y en a plusieurs parmi lesquelles choisir. Mon critère principal était que ce soit quelque chose de peu coûteux ou gratuit. 

J'ai finalement opté pour [Firestore](https://firebase.google.com/docs/firestore), en utilisant le [Spark Plan](https://firebase.google.com/pricing). Ce plan m'offre 5 Go de stockage, avec 50 000 lectures et 20 000 écritures par jour gratuitement, ce qui, à l'époque, semblait suffisant. J'ai rapidement appris qu'un peu d'imprudence peut rapidement dépasser ces limites de transactions.

Firestore est une base de données de stockage de documents NoSQL. Chaque base de données NoSQL est différente et ma courbe d'apprentissage a été plus raide que prévu. Comme vous le savez, le meilleur professeur est l'adversité, et j'ai fait ma part d'erreurs dès le début. Une de trop, cependant, et j'avais atteint la limite de lecture ou d'écriture du plan, ce qui pouvait parfois arriver en une heure ou deux. Ensuite, il était temps de mettre fin à la journée.

Les choses sont meilleures maintenant, alors je vous offre ces leçons apprises :

### *Faites* commencer par le plan gratuit

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-198.png)
_Photo par [Unsplash](https://unsplash.com/@frankiefoto?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">frank mckenna</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Oui, il est facile de dépasser les limites du plan, mais ces occurrences vous forceront à apprendre à être efficace avec vos lectures et écritures. Vous deviendrez plus conscient des coûts en séquencant plusieurs opérations de base de données de manière efficace.

### Commencez par un petit ensemble de données

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-199.png)
_Photo par [Unsplash](https://unsplash.com/@rayhennessy?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Ray Hennessy</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Cela peut sembler évident, mais par **petit**, je veux dire moins de 100 documents au total. Dans mon projet, j'ai d'abord créé une collection avec 10 000 documents. J'ai ensuite réalisé que j'avais fait une erreur dans les données que j'avais chargées, j'ai corrigé cela, j'en ai trouvé une autre, je suis allé la corriger, mais... TRANSACTION_RESOURCE_LIMIT_EXCEEDED. Eh bien, c'est fini pour la journée.

### Prenez le temps de concevoir votre modèle de données

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-200.png)
_Photo par [Unsplash](https://unsplash.com/@kellysikkema?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Kelly Sikkema</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Comme l'axiome du charpentier : « Mesurez deux fois, coupez une fois », vous ne voulez pas ajuster vos champs et la structure de vos documents JSON de manière fragmentée. Oh, vous le ferez bien sûr, mais vous vous épargnerez quelques transactions en pratiquant un peu de prévoyance. Écrivez d'abord un schéma des documents, de leurs champs et de leurs relations. [La visualisation est la clé du bonheur.](https://www.freecodecamp.org/news/inserting-uml-in-markdown-using-vscode/)

### Testez et vérifiez vos scripts de chargement de données

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-201.png)
_Photo par [Unsplash](https://unsplash.com/@nasa?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">NASA</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Vous aurez besoin de scripts pour peupler la base de données à partir d'une autre source. C'est le moment de :

* vérifier que ce que vous avez chargé est ce que vous attendiez
* gérer correctement le cas de données manquantes pour les champs

J'ai fait des erreurs dans les deux cas. D'abord, lorsque j'ai chargé des données de chaîne dans un champ de document, je n'avais pas immédiatement remarqué que ces chaînes avaient déjà des guillemets, donc les chaînes stockées avaient des guillemets intégrés. Cela ne semblait pas être un problème sérieux, mais cela est devenu un casse-tête plus tard lors de l'écriture et des tests de recherches sur ce champ. Comme il y avait beaucoup de documents, j'ai passé une partie importante de mon quota d'écriture quotidien à nettoyer cela.

Dans le second cas, j'ai découvert que Firestore n'a aucun mécanisme pour déterminer [l'existence d'une propriété dans un document](https://stackoverflow.com/questions/46806860/how-to-query-cloud-firestore-for-non-existing-keys-of-documents) (il n'y a pas de vérification _undefined_). Il existe un [test **exists** pour les documents](https://firebase.google.com/docs/firestore/query-data/get-data#get_a_document), mais pas pour les champs de document. La meilleure pratique est de peupler les champs de données manquants avec **null**, puis de faire des tests d'équivalence null dans une clause where pour trouver des documents avec des propriétés « manquantes ».

### Ce qu'un petit ensemble de données ne vous apprendra pas

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-202.png)
_Photo par [Unsplash](https://unsplash.com/@goodfreephoto_com?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Good Free Photos</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Une fois que vous avez résolu les problèmes sur le petit ensemble de données, il est temps de passer à un ensemble plus grand. Avec plus de documents à traiter, des choses comme l'efficacité des requêtes, la pagination et les requêtes par lots deviennent importantes.

### Lisez par morceaux, écrivez par morceaux

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-203.png)
_Photo par [Unsplash](https://unsplash.com/@picoftasty?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Mae Mu</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Les [opérations par lots](https://firebase.google.com/docs/firestore/manage-data/transactions) permettent plusieurs lectures/écritures sur la base de données dans une seule transaction. Cela signifie que si une opération d'écriture échoue, toutes les écritures échouent, et les données de la base de données conservent leur état d'origine. Chaque opération dans un lot compte vers les quotas totaux de lecture/écriture, donc cela n'aide pas les quotas d'utilisation. De plus, lors de l'écriture via des opérations par lots, soyez conscient qu'il y a une limite de 500 opérations par lot.

Soyez prudent lorsque vous corrélez deux documents (c'est-à-dire, pour chaque document A, il y a une association par référence à un document B). Ne récupérez pas tous les documents du premier, puis parcourez les autres. C'est un bon moyen de consommer le quota de transactions lors du débogage.

Il est préférable de récupérer un sous-ensemble de la première collection, puis de le parcourir document par document. Associez ces documents avec les documents de la deuxième collection en récupérant **un** qui correspond aux critères. Continuez à faire cela jusqu'à ce que toute la première collection ait été récupérée. Lors du débogage, vous pouvez vérifier que tout semble fonctionner correctement et, si ce n'est pas le cas, arrêter le processus avant qu'un grand nombre de transactions ne soient exécutées.

### Comment limiter les résultats des requêtes

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-204.png)
_Photo par [Unsplash](https://unsplash.com/@will0629?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Will Porada</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Le langage de requête de Firestore n'est pas aussi richement expressif que SQL, mais il existe encore plusieurs façons de restreindre vos requêtes afin de ne pas surcharger les données. Bien que techniquement il n'y ait pas de limite de taille pour un corps de réponse POST, en pratique, il y en a une.

Certains mécanismes pour limiter les résultats des requêtes :

**where et compound where**

Vous pouvez enchaîner plusieurs clauses where ensemble, similaires à l'ajout d'expressions conditionnelles à une seule clause where en SQL.

```
citiesRef.where('state', '==', 'CO').where('name', '==', 'Denver');
```

**limit et ranges**

Vous pouvez limiter le nombre de documents retournés par une requête en utilisant une clause limit à la fin de l'objet de requête.

```
let biggest = citiesRef.where('population', '>', 2500000)  .orderBy('population').limit(2);
```

Vous pouvez également spécifier une plage d'enregistrements à récupérer via des contraintes startAt/endAt ou startBefore/endBefore, ce qui vous permet de faire de la pagination basée sur un curseur.

```
let docRef = db.collection('cities').doc('SF');
```

```
return docRef.get().then(snapshot => {  let startAtSnapshot = db.collection('cities')    .orderBy('population')    .startAt(snapshot);  return startAtSnapshot.limit(10).get();});
```

**in array query**

Vous pouvez rechercher des correspondances spécifiques dans un tableau. Cela est bon pour les valeurs énumérées.

```
const usaOrJapan = citiesRef.where('country', 'in', ['USA', 'Japan']);
```

Comme démontré, il est possible de travailler dans les limites du Spark Plan tout en apprenant Firestore. C'est gratuit, ce qui est toujours un bon point de départ.