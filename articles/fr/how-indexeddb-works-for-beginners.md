---
title: Comment utiliser IndexedDB – Guide de base de données pour débutants
subtitle: ''
author: Victor Yakubu
co_authors: []
series: null
date: '2022-09-08T16:23:00.000Z'
originalURL: https://freecodecamp.org/news/how-indexeddb-works-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Colorful-Minimalist-Shapes-Internal-Pitch-Deck-Talking-Presentation-1.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: database
  slug: database
seo_title: Comment utiliser IndexedDB – Guide de base de données pour débutants
seo_desc: "The modern browser has given us a number of options when it comes to storing\
  \ data on the client-side. Aside from storing data, browser databases allow us to\
  \ retrieve that data. \nBased on your application's needs, you can choose from the\
  \ different bro..."
---

Le navigateur moderne nous a donné un certain nombre d'options pour stocker des données côté client. En plus de stocker des données, les bases de données du navigateur nous permettent de récupérer ces données. 

En fonction des besoins de votre application, vous pouvez choisir parmi les différentes options de stockage du navigateur disponibles pour améliorer l'expérience de vos utilisateurs lorsqu'ils utilisent vos applications. 

L'une de ces options de stockage du navigateur est IndexedDB. J'ai utilisé IndexedDB pour la première fois il y a quelques mois. Avant de l'utiliser, j'ai parcouru des articles et des vidéos sur diverses implémentations. J'ai donc pensé qu'il serait intéressant d'en parler en fonction de ma compréhension de son fonctionnement. 

Donc, dans cet article, je vais parler de ce qu'est IndexedDB, de ses avantages et de son fonctionnement.

## Qu'est-ce qu'une base de données ?

De nos jours, les données sont partout. Les données peuvent être n'importe quelle information telle que votre âge, votre localisation, ce que vous avez récemment acheté sur un site en ligne, et ainsi de suite. Les données peuvent être sous forme de vidéos, d'images, de fichiers ou même de texte.  

Les entreprises doivent pouvoir stocker et traiter ces données efficacement, et elles utilisent des bases de données à cette fin.

Maintenant, une base de données est simplement l'endroit où vous stockez des données – c'est aussi simple que cela. Donc, si vous ouvrez une feuille Excel, par exemple, et que vous la remplissez avec des données, cela est considéré comme une base de données. 

Le but de stocker des données dans une base de données est de faciliter l'accès à celles-ci. Cela vous permet de les modifier, de les protéger et également de les analyser pour obtenir autant d'informations que possible.

## Types de bases de données

Il existe principalement deux types de bases de données. Selon vos besoins, vous voudrez essayer les deux au cours de votre parcours :

### Bases de données relationnelles

Dans une base de données relationnelle, les données sont stockées dans une collection de tables. Ces tables sont connectées les unes aux autres. 

Les exemples de bases de données relationnelles incluent Oracle, PostgreSQL, MySQL, Microsoft SQL Server, et ainsi de suite.

### Bases de données non relationnelles

Dans une base de données non relationnelle, les données sont stockées dans des collections. Il n'y a pas de tables, de colonnes ou de lignes et les données ne sont pas connectées les unes aux autres. 

Parmi les bases de données non relationnelles, il existe différentes catégories : bases de données clé-valeur, bases de données de documents, bases de données de graphes, bases de données à colonnes larges, bases de données de moteurs de recherche, et plus encore.

Les exemples de bases de données non relationnelles incluent Redis, MongoDB, Neo4j, Cassandra, et d'autres. Notre propre IndexedDB est également une base de données non relationnelle.

Dans cet article, nous ne couvrirons pas en profondeur les bases de données elles-mêmes, car ce n'est pas le but principal. Mais [Dionysia Lemonaki](https://www.freecodecamp.org/news/author/dionysia/) a un article plus détaillé sur les bases de données relationnelles et non relationnelles que vous pouvez consulter [ici](https://www.freecodecamp.org/news/relational-vs-nonrelational-databases-difference-between-sql-db-and-nosql-db/) pour en savoir plus.

Il est passionnant de savoir qu'IndexedDB, dont nous allons parler ici, est une base de données disponible sur tous les navigateurs modernes. Mais IndexedDB n'est pas la seule option de stockage du navigateur disponible. Il y a aussi le [stockage local](https://www.freecodecamp.org/news/how-leverage-local-storage-to-build-lightning-fast-apps-4e8218134e0c/), le [stockage de session](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage), les [cookies](https://www.freecodecamp.org/news/everything-you-need-to-know-about-cookies-for-web-development/), [Web SQL](https://www.w3.org/TR/webdatabase/), et le [stockage en cache](https://www.freecodecamp.org/news/web-caching-explained-by-buying-milk-at-the-supermarket-2ba6133ca4ed/). 

Vous êtes peut-être déjà familier avec ces options, mais si ce n'est pas le cas, je vous encourage à en lire davantage à leur sujet. 

## Qu'est-ce que le stockage du navigateur ? En quoi est-il différent du stockage serveur ?

Le stockage du navigateur est également appelé stockage côté client. Il s'agit simplement d'un stockage situé sur le navigateur d'un utilisateur.

Tout comme le stockage côté serveur (qui vous permet de stocker des données dans une base de données appelée backend) où vous pouvez communiquer avec la base de données en utilisant des lignes de code, le stockage côté client utilise le même principe. 

Mais gardez à l'esprit que le stockage côté client n'est pas un substitut au stockage côté serveur. Le stockage côté client est principalement utilisé pour améliorer l'expérience de l'utilisateur. 

Un exemple simple est lorsque vous vous connectez à une plateforme pour la première fois. Le stockage côté serveur gère l'authentification et les autorisations nécessaires, et le stockage côté client permet de visiter cette plateforme après quelques heures et de continuer à partir de l'état précédent sans avoir à envoyer une requête au backend.

Ensuite, chaque fois que vous devez vous connecter après un certain temps, le stockage côté client sauvegarde vos identifiants de connexion et les remplit automatiquement. Tout ce qui vous sera demandé est de cliquer sur le bouton de connexion.

Le côté serveur peut être écrit et accessible en utilisant n'importe quel nombre de langages de programmation selon votre préférence – comme Python, Ruby, C#, PHP et JavaScript (NodeJS). Pour le côté client, vous utiliserez principalement JavaScript pour accéder et communiquer avec le stockage du navigateur.

D'accord, maintenant apprenons à connaître IndexedDB.

## Qu'est-ce qu'IndexedDB ?

Ci-dessus, nous avons parlé des bases de données non relationnelles et de leurs différents types. Nous avons également mentionné les bases de données clé-valeur comme l'un de ces types, n'est-ce pas ? Eh bien, IndexedDB est un exemple de base de données clé-valeur.

### Qu'est-ce qu'une base de données clé-valeur ?

Une base de données clé-valeur signifie que toutes les données stockées doivent être assignées à une clé. C'est l'une des bases de données non relationnelles les moins compliquées, du moins à mon avis. 

Une base de données clé-valeur associe une clé à une valeur. La clé sert d'identifiant unique pour cette valeur, ce qui signifie que vous pouvez suivre cette valeur en utilisant la clé.

Si votre application doit récupérer des données constamment, les bases de données clé-valeur utilisent des structures d'index très efficaces et compactes pour localiser rapidement et de manière fiable les valeurs par leurs clés. En utilisant la clé, vous êtes en mesure non seulement de récupérer la valeur stockée, mais aussi de la supprimer, de la mettre à jour et de la remplacer.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/key-value.png)
_[base de données clé-valeur](https://mdn.github.io/learning-area/javascript/apis/client-side-storage/indexeddb/notes/)_

D'accord, je crois que vous comprenez maintenant ce qu'est une base de données clé-valeur ? Continuons à parler d'IndexedDB. 

### **Avantages d'IndexedDB**

Nous avons toutes ces options de stockage du navigateur disponibles pour nous, ce qui est une bonne chose car nous pouvons en choisir une en fonction de nos besoins. Et chaque option a des capacités différentes. 

Il est donc important de savoir comment chacune fonctionne et quelles sont leurs capacités afin de pouvoir choisir la bonne pour votre cas d'utilisation.

Cela dit, IndexedDB présente les avantages suivants :

1. IndexedDB est asynchrone, ce qui signifie qu'il n'empêche pas l'interface utilisateur de se rendre pendant le chargement des données.
2. Il vous permet de catégoriser vos données en utilisant des magasins d'objets.
3. Il vous permet de stocker de grandes quantités de données.
4. Il supporte des objets comme des vidéos, des images, et ainsi de suite – tout objet qui supporte un algorithme de clonage structuré.
5. Il supporte les transactions de base de données et la gestion des versions.
6. Il a de grandes performances.
7. La base de données est privée à une origine.
8. Il est supporté sur tous les navigateurs modernes.

### Cas d'utilisation d'IndexedDB 

En plus de savoir comment IndexedDB fonctionne, il est également important de savoir quand l'utiliser.

* **Pour stocker du contenu généré par l'utilisateur :** Un exemple de contenu généré par l'utilisateur est le remplissage d'un formulaire de demande. Pendant le processus de remplissage du formulaire, un utilisateur peut le quitter et revenir plus tard pour le compléter sans perdre ses entrées de données initiales.
* **Pour stocker l'état de l'application :** Lorsque l'utilisateur charge pour la première fois un site web ou une application, vous pouvez utiliser IndexedDB pour stocker ces états initiaux. Cela peut être des authentifications de connexion, des requêtes API, ou tout autre état nécessaire avant que l'UI ne soit rendue. Ainsi, lorsque l'utilisateur visite à nouveau le site, la vitesse de chargement augmente car l'application a déjà un état stocké. Cela signifie qu'elle rend l'UI plus rapidement.
* **Pour une application qui fonctionne hors ligne :** Les utilisateurs peuvent éditer et ajouter des données pendant que l'application est hors ligne. IndexedDB traitera et videra ces opérations dans une file de synchronisation lorsque l'application sera en ligne.

## Comment fonctionne IndexedDB

Maintenant, la partie principale de cet article : apprendre comment fonctionne IndexedDB. Nous allons utiliser le diagramme ci-dessous, et nous allons passer en revue les différents événements et chemins un après l'autre et le code JavaScript associé pour les expliquer correctement.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Untitled-Diagram-Page-1.drawio--1-.png)
_Diagramme des événements IndexedDB_

### Chemin 1 : Que faire si la base de données n'existe pas

Lorsque vous créez une nouvelle base de données dans IndexedDB, c'est le chemin qu'elle suivra. Ce chemin est assez simple :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Untitled-Diagram-Page-2.drawio.png)

Une chose importante à noter est que, lors de la création d'une base de données, vous devrez donner un nom et une version à la base de données (vous déterminez la version à donner à la base de données). 

De plus, lorsque vous créez une base de données pour la première fois, la **version 1** lui est automatiquement assignée même si vous n'avez pas indiqué de version.

Maintenant, expliquons le diagramme ci-dessus. Lorsque vous créez une base de données, elle vérifie si une base de données avec ce nom (dbname) existe déjà. 

Si elle n'existe pas, elle procédera à l'appel de l'événement **upgrade**. Lorsque l'événement upgrade est appelé, vous pouvez alors mettre à niveau la structure de la base de données. Lorsque le bloc de l'événement upgrade s'exécute avec succès, il appelle ensuite l'événement **success**.

```
        const request = indexedDB.open('myDatabase', 1);

        //upgrade event
        request.onupgradeneeded = () => {
            alert("upgrade needed")
        }

        //on success
        request.onsuccess = () => {
            alert("success is called")
        }
```

### Chemin 2 : Que faire si la base de données existe mais a une nouvelle version supérieure à la version précédente

Maintenant, nous allons examiner le deuxième chemin. Lorsqu'une nouvelle base de données est créée, elle vérifie d'abord si la base de données existe déjà. 

Si une base de données avec le même nom existe, elle vérifie ensuite la version pour voir si la version est supérieure à la version précédente. Si c'est le cas, elle appelle ensuite l'événement **upgrade** où vous pouvez modifier la structure de la base de données. Et après cela, elle appelle l'événement **success**.



![Image](https://www.freecodecamp.org/news/content/images/2022/08/Untitled-Diagram-Page-3.drawio.png)

Suivant l'explication ci-dessus, regardons maintenant le code ci-dessous.

Supposons que nous avions déjà créé une base de données avec le nom "myDatabase". Puisque le nom de la base de données est le même que celui que nous avons créé précédemment, il passe ensuite à la vérification de la version. La version précédente était "version 1". Puisque nous avons changé la version en "version 2" et puisque la version 2 > version 1, elle exécutera alors la modification à l'intérieur de la fonction **onupgradeneeded**.

```
    const request = indexedDB.open('myDatabase', 2);

        //upgrade event
        request.onupgradeneeded = () => {
            alert("upgrade needed")
        }

        //on success
        request.onsuccess = () => {
            alert("success is called")
        }
```

### Chemin 3 : Que faire si la base de données existe, mais que la version est inférieure à la version actuelle

Suivant le diagramme ci-dessous, si la base de données existe déjà et que la version est inférieure à la version actuelle, elle passe ensuite à la vérification si la version est la même que la version actuelle. 

Il y a deux résultats possibles ici : premièrement, si la version est la même que la version actuelle, elle appelle l'événement **success**, c'est-à-dire qu'aucune mise à jour ne sera effectuée, la base de données reste la même, aucune erreur n'est générée. Deuxièmement, si la version est inférieure à la version actuelle, elle échoue et génère une erreur.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Untitled-Diagram-Page-4.drawio--3-.png)

### Comment créer un magasin d'objets et une transaction dans IndexedDB

* [**Magasin d'objets**](https://developer.mozilla.org/en-US/docs/Web/API/IDBObjectStore) : Il s'agit d'une collection d'objets à l'intérieur d'une base de données. Une base de données peut avoir différents magasins d'objets. En considérant le code ci-dessous, myDatabase est la base de données créée, tandis que myDatabaseStore est le magasin d'objets créé à l'intérieur de la base de données. Le magasin d'objets peut être utilisé pour stocker toute forme de données. J'ai utilisé le code ci-dessous pour expliquer comment créer un magasin d'objets.

```
let db;

const openRequest = indexedDB.open('myDatabase', 1);

openRequest.onupgradeneeded = function (e) {
    db = e.target.result;
    console.log('running onupgradeneeded');
    const storeOS = db.createObjectStore('myDatabaseStore',  {keyPath: "name"});
                
};
openRequest.onsuccess = function (e) {
    console.log('running onsuccess');
    db = e.target.result;
};
openRequest.onerror = function (e) {
    console.log('onerror! doesnt work');
};

```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/key-value-1.png)
_Création d'un magasin d'objets_

* [**Transaction**](https://developer.mozilla.org/en-US/docs/Web/API/IDBTransaction) : Une transaction est une séquence de tâches regroupées ensemble. Pour qu'une transaction soit réussie, toutes les tâches regroupées doivent réussir ; si une échoue, aucune ne réussira. Si cela se produit, aucune mise à jour ne sera effectuée dans la base de données. Les transactions ont des méthodes, des propriétés et des événements que vous pouvez explorer. Dans le code ci-dessous, j'ai pu ajouter un élément au magasin d'objets en l'enveloppant dans une transaction.

```
let db;

const openRequest = indexedDB.open('myDatabase', 2);

openRequest.onupgradeneeded = function (e) {
    db = e.target.result;
    console.log('running onupgradeneeded');
    const storeOS = db.createObjectStore('myDatabaseStore',  {keyPath: "name"});
                
};
openRequest.onsuccess = function (e) {
    console.log('running onsuccess');
    db = e.target.result;
    addItem();
};
openRequest.onerror = function (e) {
    console.log('onerror! doesnt work');
    console.dir(e);
};

function addItem() {
    const item = {
        name: 'banana',
        price: '$2.99',
        description: 'It is a purple banana!',
        created: new Date().getTime(),
    };
    const tx = db.transaction("myDatabaseStore", "readwrite");
    const store = tx.objectStore('myDatabaseStore');
    store.add(item);
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/09/key-value-2.png)
_Ajout d'un élément au magasin_

## Conclusion

IndexedDB est une option de stockage côté client très puissante que les développeurs peuvent utiliser pour offrir une meilleure expérience utilisateur pour leurs sites web ou applications. Il vous aide à réduire le temps nécessaire pour charger des données à partir d'un site web ou d'une application que vos utilisateurs visitent fréquemment.

Si vous n'avez pas encore construit quelque chose avec IndexedDB, je vous encourage à essayer. Cet article n'a pas couvert comment faire cela, mais il existe des ressources en ligne qui vous guideront. Construire des choses vous aidera à apprécier IndexedDB davantage.

J'espère que vous avez apprécié la lecture autant que j'ai apprécié l'écrire.

**Documentation pertinente sur IndexedDB :**

* [www.w3.org/IndexedDB](https://www.w3.org/TR/IndexedDB/#introduction)
* [developer.mozilla.org/IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)