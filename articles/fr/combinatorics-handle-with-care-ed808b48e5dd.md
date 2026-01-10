---
title: 'Les explosions combinatoires expliquées avec de la glace : comment ajouter
  un peu et obtenir beaucoup'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-04T19:11:00.000Z'
originalURL: https://freecodecamp.org/news/combinatorics-handle-with-care-ed808b48e5dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IwwZN7qurglWUXNLYR35QQ.jpeg
tags:
- name: data structures
  slug: data-structures
- name: JavaScript
  slug: javascript
- name: Mathematics
  slug: mathematics
- name: NoSQL
  slug: nosql
- name: General Programming
  slug: programming
seo_title: 'Les explosions combinatoires expliquées avec de la glace : comment ajouter
  un peu et obtenir beaucoup'
seo_desc: 'By Jeff M Lowery

  Let’s explore the fun, counter-intuitive world of combinatorics.

  Combining values to form sets of distinct combinations can be a tricky thing. Even
  if you ignore order, the number of possible sets grows alarmingly.

  For an array of tw...'
---

Par Jeff M Lowery

Explorons le monde amusant et contre-intuitif de la combinatoire.

Combiner des valeurs pour former des ensembles de combinaisons distinctes peut être une chose délicate. Même si vous ignorez l'ordre, le nombre de jeux possibles augmente de manière alarmante.

Pour un tableau de deux valeurs [1, 2], vous pouvez générer :

* [] (ensemble vide)
* [1]
* [2]
* [1,2] (ou [2,1])

Si les répétitions sont autorisées ([2, 2] par exemple), l'augmentation est encore plus grande. À mesure que le nombre de valeurs d'entrée augmente, le nombre d'ensembles de sortie correspondants [explose](http://www.intmath.com/counting-probability/4-combinations.php) !

![Image](https://cdn-media-1.freecodecamp.org/images/1*7DsXxogHWKpaynmwaTfE7Q.jpeg)
_[Explosion combinatoire](http://www.torbair.com/blog/2015/12/26/4mvxoio4tc8j28reqsbz449tlab4ss" rel="noopener" target="_blank" title="), en effet_

Appelons les valeurs d'entrée **articles** et chaque combinaison de ces valeurs un **choix**. De plus, permettons plusieurs articles, chacun avec des choix distincts. Un bon exemple serait un menu. Nous allons simuler le menu de **Ye Olde Ice Cream Shoppe**, qui propose à ses clients des combinaisons de glaces, de garnitures et de sirops.

Les parfums de glace sont : **CHOCOLAT, FRAISE, VANILLE**

Garnitures : **ananas, fraise, copeaux de noix de coco, noix de pécan**

Sirops : **chocolat, guimauve, caramel, érable**

Il y a certaines contraintes sur les choix : les clients peuvent choisir **deux** glaces, **deux** garnitures et **un** sirop. Les choix de glace et de garniture sont exclusifs, ce qui signifie que je ne peux pas choisir ananas + ananas, par exemple. Le client peut choisir de ne pas avoir de garnitures et de sirop, mais doit choisir au moins une glace. Avec ces contraintes, le taux d'augmentation est exponentiel, de l'ordre de 2 à la puissance n, ce qui est considérablement moins que si l'ordre était significatif et les doublons autorisés.

#### Palatabilité

**Ye Olde Ice Cream Shoppe** est en réalité assez moderne dans son approche des affaires et développe un système expert d'intelligence artificielle pour juger quelles combinaisons de glace, de garniture et de sirop sont savoureuses. Les serveurs verront un avertissement sur leurs registres lorsque qu'un client choisira une sélection désagréable. Les serveurs sont alors invités à vérifier avec le client que leur commande est correcte.

### Étape 1 : Construction des données

Le code pour cet article peut être trouvé [ici](https://github.com/JeffML/Combinatorics). Je vais supposer que vous êtes familier avec JavaScript et Node.js. Une connaissance pratique de Lodash (ou Underscore) est utile. Le code utilise une base de données map/reduce pour le stockage.

La première étape sera de créer une base de données de toutes les combinaisons de glaces, de garnitures et de sirops. Les entrées seront les suivantes :

```js
var menu = {
  iceCream: {min: 1, max: 2, values: ["CHOCOLATE", "STRAWBERRY", "VANILLA"]},
  topping: {min: 0, max: 2, values: ["pineapple", "strawberry", "coconut flakes", "pecans"]},
  syrup: {min:0, max: 1, values: ["chocolate", "marshmallow", "butterscotch", "maple"]}
}
```

Avec ces données, je peux écrire une fonction [Combinator](https://github.com/JeffML/Combinatorics/blob/master/Combinator.js) qui prend chaque élément du menu et génère toutes les combinaisons possibles autorisées. Chaque combinaison est stockée sous forme de tableau. Par exemple, les combinaisons de glaces ressembleraient à ceci :

```js
[ [ 'CHOCOLATE', 'STRAWBERRY' ],
 [ 'CHOCOLATE', 'VANILLA' ],
 [ 'CHOCOLATE' ],
 [ 'STRAWBERRY', 'VANILLA' ],
 [ 'STRAWBERRY' ],
 [ 'VANILLA' ] ]
```

Une fois les combinaisons de glaces, de garnitures et de sirops déterminées, il ne reste plus qu'à itérer chaque combinaison d'articles avec les autres :

```js
var allChoices = [];

_.each(iceCreamChoices, function(ic) {
  _.each(toppingChoices, function(tp) {
    _.each(syrupChoices, function(sy) {
      allChoices.push([ic,tp,sy]);
    })
  })
})
```

Cela donne une combinaison de glace(s), de garniture(s) et de sirop, comme :

```js
[ [ 'VANILLA' ], [ 'coconut flakes', 'pecans' ], [] ],
  [ [ 'VANILLA' ], [ 'coconut flakes' ], [ 'chocolate' ] ],
  [ [ 'VANILLA' ], [ 'coconut flakes' ], [ 'marshmallow' ] ],...
```

Les choix présentés se traduisent par :

* Glace à la vanille avec des copeaux de noix de coco et des noix de pécan, sans sirop
* Glace à la vanille avec des copeaux de noix de coco et du sirop de chocolat
* Glace à la vanille avec des copeaux de noix de coco et du sirop de guimauve

Même avec seulement quelques éléments de menu restreints, le nombre de choix autorisés est de 330 !

### Étape 2 : Stockage des données

Maintenant que toutes les combinaisons d'articles commandables sont déterminées, d'autres travaux peuvent être effectués. Le système d'IA pour déterminer les combinaisons de choix savoureux s'avère complexe et ne sera pas intégré dans le système d'exploitation des registres. Au lieu de cela, une requête AJAX sera faite à un serveur hébergeant le programme d'IA. Les entrées seront les choix de menu du client, et la sortie évaluera la palatabilité de ces choix comme l'un des suivants : **[beurk, bof, savoureux, sublime].** Une note de palatabilité de **beurk** déclenche l'avertissement mentionné précédemment.

Nous avons besoin d'une réponse rapide à la requête, donc les notes de palatabilité seront mises en cache dans une base de données. Étant donné la nature de l'augmentation exponentielle, cela pourrait évoluer vers un problème de Big Data si davantage de choix d'articles sont ajoutés au menu à l'avenir.

Disons qu'il est décidé de stocker les combinaisons de choix et les notes dans une base de données NoSQL. En utilisant [PouchDB,](https://pouchdb.com/guides/) chaque choix et valeur de palatabilité sont stockés sous forme de documents JSON. Un [_index secondaire_](https://pouchdb.com/guides/queries.html) (alias _vue_) avec chaque choix comme clé nous permettra de rechercher rapidement la note de palatabilité. Au lieu de pousser les données dans un tableau **allChoices** comme montré ci-dessus dans [buildChoices.js](https://gist.github.com/JeffML/c0f9c7c02272da7c57604bd685910cd2), je peux pousser des documents JSON vers la base de données pour le stockage.

En procédant naïvement, je peux apporter quelques modifications dans Step1.js pour arriver à Step2.js : tout d'abord, je dois installer PouchDB via npm, puis l'importer. Ensuite, je crée une base de données NoSQL appelée **choices**.

```js
var PouchDB = require('pouchdb');
var db = new PouchDB('choices');
```

Maintenant, chaque choix est posté dans la base de données des choix :

```js
var count = 0;

_.each(iceCreamChoices, function(ic) {
  _.each(toppingChoices, function(tp) {
    _.each(syrupChoices, function(sy) {
      //allChoices.push([ic,tp,sy]);
      db.post({choice: [ic,tp,sy]}, function(err, doc){
        if (err) console.error(err);
        else console.log(`stored ${++count}`);
      });
    })
  })
});

console.log('done??');
```

Cela fonctionne ! En quelque sorte. Comme on peut le déduire du paramètre de rappel de **db.post**, cette opération est asynchrone. Ce que nous voyons dans le journal est :

```bash
>node Step2.js
done??
stored 1
stored 2
stored 3
...
```

Donc le code dit qu'il a terminé avant même que le premier enregistrement n'ait été stocké. Cela posera un problème si j'ai d'autres traitements à faire contre la base de données et que tous les enregistrements ne sont pas encore là.

### Étape 3 : Correction et amélioration

Il y a aussi un problème plus subtil : l'épuisement potentiel des ressources. Si la base de données limite le nombre de connexions simultanées, un grand nombre de requêtes de publication simultanées peut entraîner des délais de connexion.

Pour [Step3.js](https://github.com/JeffML/Combinatorics/blob/master/Step3.js), j'ai fait un peu de correction de bugs, de reformattage et de refactorisation de ce qui avait été écrit dans Step2.js. Un bug était que chaque exécution ajoutait de plus en plus d'enregistrements à la base de données, dupliquant ce qui était là avant. La solution était de détruire la base de données existante, de la recréer, puis d'exécuter le programme principal :

```js
// remove old
db.destroy(null, function () {
    db = new PouchDB('choices');
    run();
});
```

Ensuite, j'ai ajouté un compteur en cours d'exécution des documents stockés et des requêtes de publication en cours afin que le programme : 1) sache quand le dernier document est stocké ; 2) permette seulement cinq publications à la fois. La méthode run() ressemble maintenant à ceci (avec quelques omissions) :

```js
function run() {
    var menu = { //...
    }

    var iceCreamChoices = new Combinator({ //...
    });
    var toppingChoices = new Combinator({ //...
    });
    var syrupChoices = new Combinator({ //...
    });

    var count = 0;
    var total = iceCreamChoices.length * toppingChoices.length * syrupChoices.length;
    var postCount = 0;
    var postCountMax = 5;

    _.each(iceCreamChoices, function (ic) {
        _.each(toppingChoices, function (tp) {
            _.each(syrupChoices, function (sy) {
                var si = setInterval(() => {
                    if (postCount < postCountMax) {
                        clearInterval(si);
                        postChoice(ic, tp, sy);
                    }
                }, 10);
            })
        })
    });

    function postChoice(ic, tp, sy) {
        ++postCount;
        db.post({
            choice: [ic, tp, sy]
        }, function (err, doc) {
            --postCount;
            done(err);
        });
    }

    function done(err) {
        if (err) {
            console.error(err);
            process.exit(1);
        }

        console.log(`stored ${++count}`);
        if (count === total) {
            console.log('done');
        }
    }
}
```

Les principaux changements à noter sont que :

1. Un **postCount** suit le nombre de publications en cours
2. Un minuteur d'intervalle vérifie le **postCount** et publiera et quittera lorsque des emplacements de publication seront disponibles
3. Un gestionnaire **done()** est appelé lorsque tous les choix sont stockés

### Étape 4 : Ajout de la palatabilité

Avec tous les choix de menu possibles en place, nous pouvons maintenant faire en sorte que l'IA détermine la palatabilité de chacun. L'IA n'est qu'une maquette pour le moment, qui attribue des valeurs aléatoires à chaque enregistrement de document dans PouchDB. Ces valeurs seront stockées dans la base de données en mettant à jour chaque document avec une note de goût.

```js
var _ = require('lodash');

var PouchDB = require('pouchdb');
var db = new PouchDB('choices');

db.allDocs({
        include_docs: true
    })
    .then(docs => {
        _.each(docs.rows, r => {
            r.doc.taste = palatability();
            db.put(r.doc);
        });
    });

function palatability() {
    var scale = Math.round(Math.random() * 10);

    var taste;

    switch (true) {
    // this switch is a horrible hack;  don't ever do this ;-P
    case (scale < 2):
        taste = "ugh";
        break;
    case (scale < 5):
        taste = "meh";
        break;
    case (scale < 8):
        taste = "tasty";
        break;
    default:
        taste = "sublime";
        break;
    }

    return taste;
}
```

Juste pour vérifier que nous avons stocké les choses correctement, nous pouvons vider les documents de la base de données vers la console :

```js
db.allDocs({
        include_docs: true
    })
    .then(docs => {
        _.each(docs.rows, r => {
            console.log(r.doc.choice, r.doc.taste)
        });
    });
//output looks like:
/*
[ [ 'STRAWBERRY' ], [ 'coconut flakes' ], [ 'maple' ] ] 'sublime'
[ [ 'CHOCOLATE' ], [ 'pecans' ], [ 'chocolate' ] ] 'tasty'
[ [ 'CHOCOLATE', 'STRAWBERRY' ], [], [ 'chocolate' ] ] 'sublime'
[ [ 'VANILLA' ], [], [ 'marshmallow' ] ] 'meh'
[ [ 'CHOCOLATE', 'STRAWBERRY' ],
  [ 'pineapple' ],
  [ 'marshmallow' ] ] 'meh'
*/
```

### Étape 5 : Recherche de la palatabilité

Les documents sont dans la base de données, mais il faut maintenant un moyen de déterminer la palatabilité des choix d'un client. Cela se fait en définissant une vue, qui est une fonction qui retourne une clé pour chaque document, ainsi qu'une valeur. Quelle doit être la clé ?

Je pourrais utiliser r.doc.choice comme clé, mais les tableaux ont un ordre et cet ordre pourrait changer si les éléments de menu définis dans l'étape 1 étaient réorganisés plus tard. La clé est simplement un identifiant de la sélection de choix et ne porte pas de signification sémantique propre. Ce qui devrait fonctionner, c'est de :

* aplatir chaque tableau r.doc.choice,
* ordonner les éléments par ordre alphabétique, puis
* les concaténer ensemble
* le résultat est une clé

Si davantage de choix sont ajoutés à l'avenir, la longueur de la clé pourrait dépasser la limite autorisée par la base de données. Au lieu d'utiliser la clé telle que construite, un hachage de la clé pourrait être utilisé comme véritable clé. Un hachage SHA256 en hexadécimal fait 64 caractères de long, et la probabilité d'une collision de hachage, même pour un quadrillion de choix, est pratiquement nulle. L'écriture de la fonction de hachage pour les choix est facile, en utilisant le module **crypto** de Node.js et une chaîne Lodash :

```js
const crypto = require('crypto');
const _ = require('lodash')

function hash(choice) {
    var str = _.chain(choice)
        .flatten()
        .sortBy()
        .join('|')
        .value();

    return crypto.createHmac('sha256', 'old ice cream')
        .update(str)
        .digest('hex');
}

module.exports = hash;
```

L'ajout du hachage à nos documents existants est une simple question d'itération à travers chaque document de la base de données, de calcul de son hachage et de mise à jour du document avec une valeur de clé :

```js
const _ = require('lodash');
const hash = require('./hash');

const PouchDB = require('pouchdb');
const db = new PouchDB('choices');

db.allDocs({
        include_docs: true
    })
    .then(docs => {
        _.each(docs.rows, r => {
            r.doc.key = hash(r.doc.choice);
            db.put(r.doc);
        });
    })
    .catch(e => {
        console.error(e)
    });
```

Ensuite, une vue de base de données est construite en utilisant le champ de clé de document comme index ; je l'appellerai **choice**.

```js
const PouchDB = require('pouchdb');
const db = new PouchDB('choices');

// doc that defines the view
var ddoc = {
    _id: '_design/choice',
    views: {
        by_key: {
            map: function (doc) {
                emit(doc.key, doc.taste);
            }.toString()
        }
    }
};

// remove any existing view, then add new one:
db.get(ddoc._id)
    .then(doc => {
        return db.remove(doc);
    })
    .then(() => {
        db.put(ddoc)
            .catch(function (err) {
                console.error(err);
            });
    });
```

Pour toute clé de document (hachage du tableau de choix), je peux trouver son goût via la vue **choice**. Maintenant, tout est en place pour déterminer si le choix d'un client est **beurk, bof, savoureux,** ou **sublime**. Pour tester cela, nous faisons quelques choix aléatoires et voyons si nous pouvons trouver le goût :

```js
    const choices = [
        [['VANILLA'], ['coconut flakes', 'pecans'], ['marshmallow']],
        [['CHOCOLATE'], ['pecans'], ['chocolate']],
        [['STRAWBERRY', 'VANILLA'], ['pineapple', 'coconut flakes'], ['marshmallow']],
        [['STRAWBERRY'], ['pecans'], ['maple']],
        [['VANILLA'], ['coconut flakes', 'pineapple'], ['chocolate']],
        [['CHOCOLATE, STRAWBERRY'], ['pineapple', 'pecans'], ['butterscotch']],
    ];

    const keys = _.map(choices, c => {
        return hash(c);
    });

    db.query('choice/by_key', {
        keys: keys,
        include_docs: false,
    }, function (err, result) {
        if (err) {
            return console.error(err);
        }
        _.each(result.rows, (r, i) => {
            console.log(`${choices[i]} tastes ${r.value}`);
        })
    });
```

Les résultats sont :

```bash
=> node test
VANILLA,coconut flakes,pecans,marshmallow tastes ugh
CHOCOLATE,pecans,chocolate tastes sublime
STRAWBERRY,VANILLA,pineapple,coconut flakes,marshmallow tastes tasty
STRAWBERRY,pecans,maple tastes meh
VANILLA,coconut flakes,pineapple,chocolate tastes sublime
```

C'est tout ! Il ne reste plus qu'à écrire un logiciel client qui soumet des choix via AJAX et obtient une valeur de goût (palatabilité) en retour. Si c'est **beurk**, alors un avertissement apparaît sur la caisse.

_Dans un article ultérieur, j'affine l'algorithme utilisé ci-dessus. [Découvrez-le](https://medium.com/@jefflowery/recursive-generator-f8bc30e5e412#.wa7sl6bt7)!_

### Références

[**La croissance exponentielle n'est pas cool. L'explosion combinatoire l'est.**](http://www.torbair.com/blog/2015/12/26/4mvxoio4tc8j28reqsbz449tlab4ss)  
[_Une grande partie de l'industrie technologique est obsédée par la croissance exponentielle. Tout ce qui est linéaire est en train de mourir, ou est mort depuis des années..._](http://www.torbair.com/blog/2015/12/26/4mvxoio4tc8j28reqsbz449tlab4ss)  
[www.torbair.com](http://www.torbair.com/blog/2015/12/26/4mvxoio4tc8j28reqsbz449tlab4ss)  


[**Calculatrice de combinaisons et permutations**](https://www.mathsisfun.com/combinatorics/combinations-permutations-calculator.html)  
[_Découvrez combien de façons différentes vous pouvez choisir des articles. Pour une explication approfondie des formules, veuillez visiter..._](https://www.mathsisfun.com/combinatorics/combinations-permutations-calculator.html)  
[www.mathsisfun.com](https://www.mathsisfun.com/combinatorics/combinations-permutations-calculator.html)