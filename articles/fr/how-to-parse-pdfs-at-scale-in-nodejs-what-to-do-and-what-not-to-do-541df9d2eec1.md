---
title: 'Comment analyser des PDF à grande échelle dans NodeJS : ce qu''il faut faire
  et ne pas faire'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-08T17:50:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-parse-pdfs-at-scale-in-nodejs-what-to-do-and-what-not-to-do-541df9d2eec1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2oJSHV1UGmLtCxPM81xheA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: software architecture
  slug: software-architecture
- name: technology
  slug: technology
seo_title: 'Comment analyser des PDF à grande échelle dans NodeJS : ce qu''il faut
  faire et ne pas faire'
seo_desc: 'By Tom

  Take a step into program architecture, and learn how to make a practical solution
  for a real business problem with NodeJS Streams with this article.


  Your stakeholder, after you save them countless hours poring over PDF files to get
  their data...'
---

Par Tom

Plongez dans l'architecture de programme et apprenez à créer une solution pratique pour un problème commercial réel avec les flux NodeJS grâce à cet article.

![Image](https://cdn-media-1.freecodecamp.org/images/-9GHNBViusI3UYW3wSxo1aLTOjNXbY-4la2O)
_Votre partie prenante, après que vous lui avez économisé d'innombrables heures à examiner des fichiers PDF pour obtenir leurs données. (Source : GIPHY)_

### Un détour : la mécanique des fluides

L'une des plus grandes forces du logiciel est que nous pouvons développer des abstractions qui nous permettent de raisonner sur le code et de manipuler les données de manière compréhensible. Les _flux_ sont une telle classe d'abstraction.

En mécanique des fluides simple, le concept de [ligne de courant](https://en.wikipedia.org/wiki/Streamlines,_streaklines,_and_pathlines#Streamlines) est utile pour raisonner sur la manière dont les particules de fluide se déplaceront et les contraintes qui leur sont appliquées à divers points d'un système.

Par exemple, supposons que vous avez de l'eau qui s'écoule uniformément dans un tuyau. À mi-chemin du tuyau, il se divise. Généralement, le débit d'eau se divise également dans chaque branche. Les ingénieurs utilisent le concept abstrait d'une ligne de courant pour raisonner sur les propriétés de l'eau, telles que son débit, pour un nombre quelconque de branches ou de configurations de pipeline complexes. Si vous demandiez à un ingénieur ce qu'il suppose être le débit à travers chaque branche, il répondrait intuitivement par "la moitié". Cela s'étend mathématiquement à un nombre arbitraire de lignes de courant.

Les flux, conceptuellement, sont pour le code ce que les lignes de courant sont pour la mécanique des fluides. Nous pouvons raisonner sur les données à un point donné en les considérant comme faisant partie d'un flux, plutôt que de nous soucier des détails d'implémentation entre la manière dont elles sont stockées. On pourrait arguer que vous pourriez généraliser cela à un concept universel de pipeline que nous pouvons utiliser entre les disciplines. Un entonnoir de vente vient à l'esprit, mais c'est tangentiel et nous le couvrirons plus tard. Le meilleur exemple de flux, et celui que vous devez _absolument_ connaître si vous ne l'avez pas déjà fait, sont les pipes UNIX :

```
cat server.log | grep 400 | less
```

Nous appelons affectueusement le caractère `|` un pipe. Basé sur sa fonction, nous transmettons la sortie d'un programme comme entrée d'un autre programme. En établissant effectivement un pipeline.

(Aussi, cela ressemble à un pipe.)

Si vous êtes comme moi et que vous vous demandez à ce stade pourquoi cela est nécessaire, demandez-vous pourquoi nous utilisons des [pipelines](https://en.wikipedia.org/wiki/Pipeline_transport) dans la vie réelle. Fondamentalement, c'est une structure qui élimine le stockage entre les points de traitement. Nous n'avons pas besoin de nous soucier de stocker des barils de pétrole s'il est pompé.

Devinez cela dans le logiciel. Les développeurs et ingénieurs intelligents qui ont écrit le code pour le transfert de données l'ont configuré de telle sorte qu'il n'occupe jamais trop de mémoire sur une machine. Peu importe la taille du fichier journal ci-dessus, il ne bloquera pas le terminal. L'ensemble du programme est un processus traitant des points de données infinitésimaux dans un flux, plutôt que des conteneurs de ces points. Le fichier journal n'est jamais chargé en mémoire en une seule fois, mais plutôt en parties gérables.

Je ne veux pas réinventer la roue ici. Maintenant que j'ai couvert une métaphore pour les flux et la raison de les utiliser, Flavio Copes a un excellent [article de blog](https://flaviocopes.com/nodejs-streams/#streams-powered-node-apis) couvrant leur implémentation dans Node. Prenez le temps nécessaire pour couvrir les bases là-bas, et lorsque vous serez prêt, revenez et nous passerons en revue un cas d'utilisation.

### La situation

Maintenant que vous avez cet outil dans votre ceinture à outils, imaginez ceci :

Vous êtes au travail et votre manager / service juridique / RH / votre client / (insérez ici la partie prenante) vous a approché avec un problème. Ils passent beaucoup trop de temps à examiner des PDF structurés. Bien sûr, normalement les gens ne vous diront pas une telle chose. Vous entendrez : « Je passe 4 heures à faire de la saisie de données. » Ou « Je regarde des tableaux de prix. » Ou encore : « Je remplis les bons formulaires pour que nous recevions nos crayons estampillés au nom de l'entreprise chaque trimestre. »

Quoi qu'il en soit, si leur travail implique à la fois (a) la lecture de documents PDF structurés et (b) l'utilisation massive de ces informations structurées, alors vous pouvez intervenir et dire : « Hé, nous pourrions peut-être automatiser cela et libérer votre temps pour travailler sur d'autres choses. »

![Image](https://cdn-media-1.freecodecamp.org/images/3uzuMbFWvG3sXqNVrCYRJQaaUlwk2roHoqxW)
_Vitesse sans effort. Votre code est un parfum, maintenant dites bonjour à votre publicité télévisée. (Source : [Chris Peeters](https://www.pexels.com/@krizz59" rel="noopener" target="_blank" title="))_

Alors, pour les besoins de cet article, imaginons une entreprise fictive. D'où je viens, le terme « dummy » fait référence soit à un idiot, soit à une tétine de bébé. Alors imaginons cette fausse entreprise qui fabrique des tétines. Et tant qu'à faire, sautons le requin et disons qu'elles sont imprimées en 3D. L'entreprise fonctionne comme un fournisseur éthique de tétines pour les nécessiteux qui ne peuvent pas se permettre les produits premium eux-mêmes.

(Je sais à quel point cela semble stupide, suspendez votre incrédulité, s'il vous plaît.)

Todd se procure les matériaux d'impression qui entrent dans les produits de DummEth, et doit s'assurer qu'ils répondent à trois critères clés :

* ils sont en plastique de qualité alimentaire, pour préserver la santé des bébés,
* ils sont bon marché, pour une production économique, et
* ils sont approvisionnés aussi près que possible, pour soutenir la copie marketing de l'entreprise affirmant que leur chaîne d'approvisionnement est également éthique et pollue aussi peu que possible.

### Le projet

Pour faciliter le suivi, j'ai mis en place un [dépôt GitLab](https://gitlab.com/fourzerofour/pdf-parser-nodejs) que vous pouvez cloner et utiliser. Assurez-vous également que vos installations de Node et NPM sont à jour.

#### Architecture de base : contraintes

Maintenant, que cherchons-nous à faire ? Supposons que Todd travaille bien avec les tableurs, comme beaucoup de travailleurs de bureau. Pour que Todd trie le bon grain de l'ivraie en matière d'impression 3D, il est plus facile pour lui d'évaluer les matériaux par leur qualité alimentaire, leur prix par kilogramme et leur lieu d'origine. Il est temps de définir quelques contraintes de projet.

Supposons que la qualité alimentaire d'un matériau est notée sur une échelle de zéro à trois. Zéro signifiant des plastiques riches en BPA interdits en Californie. Trois signifiant des matériaux non contaminants couramment utilisés, comme le polyéthylène basse densité. Cela est purement pour simplifier notre code. En réalité, nous devrions somehow mapper les descriptions textuelles de ces matériaux (par exemple : « LDPE ») à une qualité alimentaire.

Le prix par kilogramme peut être supposé être une propriété du matériau donnée par son fabricant.

L'emplacement, nous allons simplifier et supposer qu'il s'agit d'une simple distance relative, à vol d'oiseau. À l'autre extrémité du spectre, il y a la solution suringénierisée : utiliser une API (par exemple : Google Maps) pour discerner la distance de voyage approximative qu'un matériau donné parcourrait pour atteindre le ou les centres de distribution de Todd. Dans tous les cas, disons que nous l'avons comme valeur (kilomètres jusqu'à Todd) dans les PDF de Todd.

De plus, considérons le contexte dans lequel nous travaillons. Todd fonctionne effectivement comme un collecteur d'informations sur un marché dynamique. Les produits entrent et sortent, et leurs détails peuvent changer. Cela signifie que nous avons un nombre arbitraire de PDF qui peuvent changer — ou plus précisément, être mis à jour — à tout moment.

Ainsi, sur la base de ces contraintes, nous pouvons enfin déterminer ce que nous voulons que notre code accomplisse. Si vous souhaitez tester votre capacité de conception, faites une pause ici et réfléchissez à la manière dont vous structureriez votre solution. Cela peut ne pas ressembler à ce que je m'apprête à décrire. Ce n'est pas grave, tant que vous fournissez une solution de travail saine pour Todd, et quelque chose que vous ne regretterez pas plus tard en essayant de maintenir.

#### Architecture de base : solutions

Nous avons donc un nombre arbitraire de PDF, et quelques règles pour les analyser. Voici comment nous pouvons procéder :

1. Configurer un objet Stream capable de lire à partir d'une entrée. Comme un client HTTP demandant des téléchargements de PDF. Ou un module que nous avons écrit qui lit des fichiers PDF à partir d'un répertoire dans le système de fichiers.
2. Configurer un [Buffer](https://nodejs.org/api/buffer.html) intermédiaire. C'est comme le serveur dans un restaurant livrant un plat terminé à son client prévu. Chaque fois qu'un PDF complet est passé dans le flux, nous vidons ces morceaux dans le buffer afin qu'il puisse être transporté.
3. Le serveur (Buffer) livre la nourriture (données PDF) au client (notre fonction d'analyse). Le client en fait ce qu'il veut (convertir en un format de feuille de calcul) avec.
4. Lorsque le client (Analyseur) a terminé, laissez le serveur (Buffer) savoir qu'il est libre et peut travailler sur de nouvelles commandes (PDF).

Vous remarquerez qu'il n'y a pas de fin claire à ce processus. En tant que restaurant, notre combo Stream-Buffer-Analyseur ne se termine jamais, jusqu'à ce qu'il n'y ait plus de données — plus de commandes — qui arrivent.

Maintenant, je sais qu'il n'y a pas encore une seule ligne de code. C'est crucial. Il est important de pouvoir raisonner sur nos systèmes avant de les écrire. Maintenant, nous n'aurons pas tout correct du premier coup même avec un raisonnement a priori. Les choses se cassent toujours dans la nature. Les bugs doivent être corrigés.

Cela dit, c'est un exercice puissant de retenue et de prévoyance que de planifier votre code avant de l'écrire. Si vous pouvez simplifier des systèmes de complexité croissante en parties gérables et en analogies, vous pourrez augmenter votre productivité de manière exponentielle, à mesure que le stress cognitif de ces complexités s'estompe dans des abstractions bien conçues.

Donc, dans le grand schéma des choses, cela ressemble à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/fDA8RRi33-g0BupQgDe-rkAoKWijWPzzQVVi)
_Le concept initial de notre programme. Cela ne ressemblera pas à cela une fois terminé, mais le processus de résolution de problèmes est tout aussi important que le résultat. Encerclé en vert : ce que nous allons faire ensuite._

### Introduction des dépendances

Maintenant, en guise d'avertissement, je devrais ajouter qu'il existe tout un monde de réflexion autour de l'introduction de dépendances dans votre code. J'adorerais couvrir ce concept dans un autre article. En attendant, laissez-moi simplement dire que l'un des conflits fondamentaux en jeu est celui entre notre désir d'accomplir notre travail rapidement (c'est-à-dire éviter le [syndrome NIH](https://en.wikipedia.org/wiki/Not_invented_here)) et notre désir d'éviter le [risque tiers](https://global.theiia.org/knowledge/Public%20Documents/TaT_April_2014.pdf).

En appliquant cela à notre projet, j'ai choisi de déléguer la majeure partie de notre traitement de PDF au module [_pdfreader_](https://www.npmjs.com/package/pdfreader). Voici quelques raisons pour lesquelles :

* Il a été publié récemment, ce qui est un bon signe que le dépôt est à jour.
* Il a une dépendance — c'est-à-dire qu'il s'agit simplement d'une abstraction sur un autre module — qui est régulièrement maintenu sur GitHub. Cela seul est un excellent signe. De plus, la dépendance, un module appelé _pdf2json_, a des centaines d'étoiles, 22 contributeurs, et de nombreux yeux qui le surveillent de près.
* Le mainteneur, [Adrian Joly](https://github.com/adrienjoly), fait une bonne tenue des livres dans le suivi des problèmes de GitHub et répond activement aux questions des utilisateurs et des développeurs.
* Lors de l'audit via NPM (6.4.1), aucune vulnérabilité n'est trouvée.

Donc, dans l'ensemble, cela semble être une dépendance sûre à inclure.

Maintenant, le module fonctionne de manière assez simple, bien que son README ne décrive pas explicitement la structure de sa sortie. Les notes de bas de page :

1. Il expose la classe `PdfReader` à instancier
2. Cette instance a deux méthodes pour analyser un PDF. Elles retournent la même sortie et ne diffèrent que par l'entrée : `PdfReader.parseFileItems` pour un nom de fichier, et `PdfReader.parseBuffer` à partir de données que nous ne voulons pas référencer depuis le système de fichiers.
3. Les méthodes demandent un callback, qui est appelé chaque fois que le `PdfReader` trouve ce qu'il désigne comme un élément PDF. Il y en a trois types. D'abord, les métadonnées du fichier, qui est toujours le premier élément. Ensuite, les métadonnées de la page. Cela agit comme un retour chariot pour les coordonnées des éléments de texte à traiter. Enfin, les éléments de texte que nous pouvons considérer comme des objets / structs simples avec une propriété de texte, et des coordonnées 2D en virgule flottante [AABB](https://stackoverflow.com/a/22512393) sur la page.
4. C'est à notre callback de traiter ces éléments dans une structure de données de notre choix et également de gérer les erreurs qui lui sont lancées.

Voici un extrait de code à titre d'exemple :

```
const { PdfReader } = require('pdfreader');
```

```
// Initialiser le lecteur
const reader = new PdfReader();
```

```
// Lire un buffer défini arbitrairement
reader.parseBuffer(buffer, (err, item) =>; {
```

```
  if (err)    console.error(err);
```

```
  else if (!item)    /* pdfreader met en file d'attente les éléments dans le PDF et les passe à     * la fonction de rappel. Lorsqu'aucun élément n'est passé, cela indique que     * nous avons terminé la lecture du PDF. */    console.log('Terminé.');
```

```
  else if (item.file)    // Les éléments de fichier ne référencent que le chemin du fichier PDF.    console.log(`Analyse de ${item.file && item.file.path || 'un buffer'}`)
```

```
  else if (item.page)    // Les éléments de page contiennent simplement leur numéro de page.    console.log(`Page ${item.page} atteinte`);
```

```
  else if (item.text) {
```

```
    // Les éléments de texte ont quelques propriétés supplémentaires :    const itemAsString = [      item.text,      'x: ' + item.x,      'y: ' + item.y,      'w: ' + item.width,      'h: ' + item.height,    ].join('\n\t');
```

```
    console.log('Élément de texte : ', itemAsString);
```

```
  }
```

```
});
```

### Les PDF de Todd

Revenons à la situation de Todd, juste pour fournir un peu de contexte. Nous voulons stocker les données des tétines basées sur trois critères clés :

* leur qualité alimentaire, pour préserver la santé des bébés,
* leur coût, pour une production économique, et
* leur distance par rapport à Todd, pour soutenir la copie marketing de l'entreprise affirmant que leur chaîne d'approvisionnement est également éthique et pollue aussi peu que possible.

J'ai codé en dur un script simple qui randomise certains produits fictifs, et vous pouvez le trouver dans le répertoire [/data](https://gitlab.com/fourzerofour/pdf-parser-nodejs/tree/master/data) du dépôt compagnon pour ce projet. Ce script écrit ces données randomisées dans des fichiers JSON.

Il y a aussi un document modèle là-dedans. Si vous êtes familier avec les moteurs de templating comme [Handlebars](https://handlebarsjs.com/), alors vous comprendrez cela. Il existe des services en ligne — ou si vous vous sentez aventureux, vous pouvez créer le vôtre — qui prennent des données JSON et remplissent le modèle, et vous le retournent sous forme de PDF. Peut-être, pour des raisons de complétude, nous pourrions essayer cela dans un autre projet. En tout cas : j'ai utilisé un tel service pour générer les PDF fictifs que nous allons analyser.

Voici à quoi cela ressemble (l'espace blanc supplémentaire a été rogné) :

![Image](https://cdn-media-1.freecodecamp.org/images/e1AdMEuwERY-EpPrEmJtG3cUAdWLRHid1r2U)

Nous aimerions obtenir de ce PDF un JSON qui nous donne :

* l'ID et la date de la réquisition, à des fins de comptabilité,
* le SKU de la tétine, pour une identification unique, et
* les propriétés de la tétine (nom, qualité alimentaire, prix unitaire et distance), afin que Todd puisse les utiliser dans son travail.

Comment faisons-nous cela ?

### Lecture des données

Tout d'abord, mettons en place la fonction pour lire les données d'un de ces PDF et extraire les éléments PDF de _pdfreader_ dans une structure de données utilisable. Pour l'instant, ayons un tableau représentant le document. Chaque élément du tableau est un objet représentant une collection de tous les éléments de texte sur la page à l'index de cet objet. Chaque propriété de l'objet de page a une valeur y pour sa clé, et un tableau des éléments de texte trouvés à cette valeur y pour sa valeur. Voici le diagramme, pour que ce soit plus simple à comprendre :

![Image](https://cdn-media-1.freecodecamp.org/images/2RfKHC6ekLDAC3XjdOttspI4FOheum8o28Xc)

La fonction `readPDFPages` dans [/parser/index.js](https://gitlab.com/fourzerofour/pdf-parser-nodejs/blob/master/parser/index.js) gère cela, de manière similaire au code d'exemple écrit ci-dessus :

```
/* Accepte un buffer (par exemple : de fs.readFile), et l'analyse * en tant que PDF, en donnant une structure de données utilisable pour * l'analyse de second niveau spécifique à l'application. */
function readPDFPages (buffer) {
  const reader = new PdfReader();
```

```
  // Nous retournons une Promesse ici, car l'opération de lecture du PDF est asynchrone.
  return new Promise((resolve, reject) =>; {
```

```
    // Chaque élément de ce tableau représente une page dans le PDF
    let pages = [];
```

```
    reader.parseBuffer(buffer, (err, item) =>; {
```

```
      if (err)
        // Si nous avons un problème, éjectons !
        reject(err)
```

```
      else if (!item)
        // Si nous n'avons plus d'éléments, résolvons avec la structure de données
        resolve(pages);
```

```
      else if (item.page)
        // Si l'analyseur a atteint une nouvelle page, il est temps de
        // travailler sur le prochain objet de page dans notre tableau de pages.
        pages.push({});
```

```
      else if (item.text) {
```

```
        // Si nous n'avons PAS un nouvel élément de page, alors nous devons
        // soit récupérer, soit créer un nouveau tableau "row"
        // pour représenter la collection d'éléments de texte à notre
        // position Y actuelle, qui sera la position Y de cet élément.
```

```
        // Donc, cette ligne se lit comme,
        // "Soit récupérer le tableau de lignes pour notre page actuelle,
        //  à notre position Y actuelle, soit en créer un nouveau"
        const row = pages[pages.length-1][item.y] || [];
```

```
        // Ajouter l'élément au conteneur de référence (c'est-à-dire : la ligne)
        row.push(item.text);
```

```
        // Inclure le conteneur dans la page actuelle
        pages[pages.length-1][item.y] = row;
```

```
      }
```

```
    });
  });
```

```
}
```

Ainsi, en passant un buffer PDF dans cette fonction, nous obtiendrons des données organisées. Voici ce que j'ai obtenu d'un test, et en l'imprimant en JSON :

```
[ {
  '3.473': [ 'DÉTAILS DU PRODUIT RÉQUISITION' ],
  '4.329': [ 'Date : 23/05/2019' ],
  '5.185': [ 'ID de réquisition : 298831' ],
  '6.898': [ 'Pacifier Tech', 'Todd Lerr' ],
  '7.754': [ '123 Example Blvd', 'DummEth Pty. Ltd.' ],
  '8.61': [ 'Timbuktu', '1337 Leet St' ],
  '12.235': [ 'SKU', '6308005' ],
  '13.466': [ 'Nom du produit', 'Tétine en quartz citron carré' ],
  '14.698': [ 'Qualité alimentaire', '3' ],
  '15.928999999999998': [ '$ / kg', '1.29' ],
  '17.16': [ 'Emplacement', '55' ]
} ]
```

Si vous regardez attentivement, vous remarquerez qu'il y a une erreur d'orthographe dans le PDF original. « Réquisition » est mal orthographié « Requsition ». La beauté de notre analyseur est que nous ne nous soucions pas particulièrement des erreurs comme celles-ci dans nos documents d'entrée. Tant qu'ils sont structurés correctement, nous pouvons extraire des données de manière précise.

Maintenant, nous devons simplement organiser cela en quelque chose de plus utilisable (comme si nous l'exposions via une API). La structure que nous recherchons est quelque chose comme ceci :

```
{
  reqID: '000000',
  date: 'DD/MM/YYYY', // Ou autre chose basé sur la géographie
  sku: '000000',
  name: 'Une chaîne que nous avons rognée',
  foodGrade: 'X',
  unitPrice: 'D.CC',
  // D pour Dollars, C pour Cents
  location: 'XX',
}
```

#### Une parenthèse : l'intégrité des données

Pourquoi incluons-nous les nombres sous forme de chaînes ? Cela est basé sur le risque d'analyse. Disons simplement que nous avons forcé tous nos nombres en chaînes :

Le prix unitaire et l'emplacement seraient corrects — ils sont censés être des nombres comptables après tout.

La qualité alimentaire, pour ce projet très limité, est _techniquement_ sûre. Aucune donnée n'est perdue lorsque nous la forçons — mais si elle est effectivement un classificateur, comme une énumération, il est préférable de la conserver sous forme de chaîne.

L'ID de réquisition et le SKU, cependant, s'ils sont forcés en chaînes, pourraient perdre des données importantes. Si l'ID pour une réquisition donnée commence par trois zéros et que nous forçons cela en un nombre, eh bien, nous venons de perdre ces zéros et nous avons corrompu les données.

Ainsi, parce que nous voulons l'intégrité des données lors de la lecture des PDF, nous laissons tout sous forme de chaîne. Si le code d'application souhaite convertir certains champs en nombres pour les rendre utilisables pour des opérations arithmétiques ou statistiques, alors nous laisserons la coercition se produire à ce niveau. Ici, nous voulons simplement quelque chose qui analyse les PDF de manière cohérente et précise.

### Restructuration des données

Maintenant que nous avons les informations de Todd, nous devons simplement les organiser de manière utilisable. Nous pouvons utiliser une variété de fonctions de manipulation de tableaux et d'objets, et ici [MDN](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference) est votre ami.

C'est l'étape où chacun a ses propres préférences. Certains préfèrent la méthode qui fait simplement le travail et minimise le temps de développement. D'autres préfèrent rechercher le meilleur algorithme pour le travail (par exemple : réduire le temps d'itération). C'est un bon exercice de voir si vous pouvez trouver un moyen de faire cela et de le comparer à ce que j'ai obtenu. J'adorerais voir des moyens meilleurs, plus simples, plus rapides, ou même simplement différents d'accomplir le même objectif.

En tout cas, voici comment je l'ai fait : la fonction `parseToddPDF` dans [/parser/index.js](https://gitlab.com/fourzerofour/pdf-parser-nodejs/blob/master/parser/index.js).

```
function parseToddPDF (pages) {
```

```
  const page = pages[0]; // Nous savons qu'il n'y aura qu'une seule page
```

```
  // Carte déclarative des données PDF que nous attendons, basée sur la structure de Todd
  const fields = {
    // "Nous nous attendons à ce que le champ reqID soit sur la ligne à 5.185, et le
    //  premier élément de ce tableau"
    reqID: { row: '5.185', index: 0 },
    date: { row: '4.329', index: 0 },
    sku: { row: '12.235', index: 1 },
    name: { row: '13.466', index: 1 },
    foodGrade: { row: '14.698', index: 1 },
    unitPrice: { row: '15.928999999999998', index: 1 },
    location: { row: '17.16', index: 1 },
  };
```

```
  const data = {};
```

```
  // Assigner les données de la page à un objet que nous pouvons retourner, selon
  // notre spécification des champs
  Object.keys(fields)
    .forEach((key) =>; {
```

```
      const field = fields[key];
      const val = page[field.row][field.index];
```

```
      // Nous ne voulons pas perdre les zéros de tête ici, et pouvons faire confiance
      // à toute application / gestion de données pour s'en soucier. C'est
      // pourquoi nous ne forçons pas à Number.
      data[key] = val;
```

```
    });
```

```
  // Correction manuelle de certains champs de texte pour qu'ils soient utilisables
  data.reqID = data.reqID.slice('ID de réquisition : '.length);
  data.date = data.date.slice('Date : '.length);
```

```
  return data;
```

```
}
```

Le cœur du problème ici est dans la boucle `forEach`, et comment nous l'utilisons. Après avoir récupéré les positions Y de chaque élément de texte précédemment, il est simple de spécifier chaque champ que nous voulons comme une position dans notre objet de pages. En fournissant effectivement une carte à suivre.

Tout ce que nous avons à faire ensuite est de déclarer un objet de données à sortir, itérer sur chaque champ que nous avons spécifié, suivre le chemin selon notre spécification, et assigner la valeur que nous trouvons à la fin à notre objet de données.

Après quelques lignes pour nettoyer certains champs de chaîne, nous pouvons retourner l'objet de données et nous sommes prêts à partir. Voici à quoi cela ressemble :

```
{
  reqID: '298831',
  date: '23/05/2019',
  sku: '6308005',
  name: 'Tétine en quartz citron carré',
  foodGrade: '3',
  unitPrice: '1.29',
  location: '55'
}
```

### Mettre le tout ensemble

![Image](https://cdn-media-1.freecodecamp.org/images/qL-zRXELF5AwM6TlzS9dMuN3cXFwZQjJuWTI)

Maintenant, nous allons passer à la construction de la concurrency pour ce module d'analyse afin que nous puissions fonctionner à grande échelle, et reconnaître quelques barrières importantes à le faire. Le diagramme ci-dessus est excellent pour comprendre le contexte de la logique d'analyse. Il ne fait pas grand-chose pour comprendre comment nous allons le paralléliser. Nous pouvons faire mieux :

![Image](https://cdn-media-1.freecodecamp.org/images/S4MbRGGBTBKqHBOWEZTNpKdMRQMMwpvAxusN)

Trivial, je sais, et peut-être trop généralisé pour que nous puissions l'utiliser pratiquement, mais c'est un concept fondamental à formaliser.

Maintenant, avant tout, nous devons réfléchir à la manière dont nous allons gérer l'entrée et la sortie de notre programme, qui enveloppera essentiellement la logique d'analyse et la distribuera ensuite parmi les processus de travail de l'analyseur. Il y a de nombreuses questions que nous pouvons poser ici et de nombreuses solutions :

* Sera-ce une application en ligne de commande ?
* Sera-ce un serveur cohérent, avec un ensemble de points de terminaison API ? Cela soulève sa propre série de questions — REST ou GraphQL, par exemple ?
* Peut-être n'est-ce qu'un module squelette dans une base de code plus large — par exemple, que se passe-t-il si nous généralisions notre analyse à travers une suite de documents binaires et que nous voulions séparer le modèle de concurrency du type de fichier source particulier et de l'implémentation de l'analyse ?

Pour des raisons de simplicité, je vais envelopper la logique d'analyse dans un utilitaire en ligne de commande. Cela signifie qu'il est temps de faire un tas d'hypothèses :

* Attend-il des chemins de fichiers en entrée, et sont-ils relatifs ou absolus ?
* Ou bien, attend-il des données PDF concaténées, à être transmises ?
* Va-t-il sortir des données vers un fichier ? Parce que si c'est le cas, alors nous allons devoir fournir cette option comme argument pour que l'utilisateur spécifie...

### Gestion de l'entrée de la ligne de commande

Encore une fois, en gardant les choses aussi simples que possible : j'ai opté pour que le programme attende une liste de chemins de fichiers, soit comme arguments individuels de la ligne de commande :

```
node index file-1.pdf file-2.pdf … file-n.pdf
```

Ou transmis à l'entrée standard sous forme de liste de chemins de fichiers séparés par des sauts de ligne :

```
# lire les lignes d'un fichier texte avec tous nos chemins
cat files-to-parse.txt | node index
# ou peut-être simplement les lister à partir d'un répertoire
find ./data -name "*.pdf" | node index
```

Cela permet au processus Node de manipuler l'ordre de ces chemins de la manière qu'il juge appropriée, ce qui nous permet de mettre à l'échelle le code de traitement plus tard. Pour ce faire, nous allons lire la liste des chemins de fichiers, quelle que soit la manière dont ils ont été fournis, et les diviser par un nombre arbitraire en sous-listes. Voici le code, la méthode `getTerminalInput` dans [./input/index.js](https://gitlab.com/fourzerofour/pdf-parser-nodejs/blob/master/input/index.js) :

```
function getTerminalInput (subArrays) {
```

```
  return new Promise((resolve, reject) =>; {
```

```
    const output = [];
    if (process.stdin.isTTY) {
```

```
      const input = process.argv.slice(2);
```

```
      const len = Math.min(subArrays, Math.ceil(input.length / subArrays));
```

```
      while (input.length) {
        output.push(input.splice(0, len));
      }
```

```
      resolve(output);
```

```
    } else {
      let input = '';
      process.stdin.setEncoding('utf-8');
```

```
      process.stdin.on('readable', () =>; {
        let chunk;
        while (chunk = process.stdin.read())
          input += chunk;
      });
```

```
      process.stdin.on('end', () =>; {
        input = input.trim().split('\n');
```

```
        const len = Math.min(input.length, Math.ceil(input.length / subArrays));
```

```
        while (input.length) {
          output.push(input.splice(0, len));
        }
```

```
        resolve(output);
      })
    }
  });
```

```
}
```

Pourquoi diviser la liste ? Supposons que vous avez un CPU à 8 cœurs sur du matériel grand public, et 500 PDF à analyser.

Malheureusement pour Node, même s'il gère le code asynchrone de manière fantastique grâce à sa boucle d'événements, il ne s'exécute que sur un seul thread. Pour traiter ces 500 PDF, si vous n'exécutez pas de code multithread (c'est-à-dire : plusieurs processus), vous n'utilisez qu'un huitième de votre capacité de traitement. En supposant que l'efficacité de la mémoire ne soit pas un problème, vous pourriez traiter les données jusqu'à huit fois plus rapidement en tirant parti des modules de parallélisme intégrés de Node.

Diviser notre entrée en morceaux nous permet de faire cela.

En passant, cela est essentiellement un équilibreur de charge primitif et suppose clairement que les charges de travail présentées par l'analyse de chaque PDF sont interchangeables. C'est-à-dire que les PDF sont de la même taille et ont la même structure.

C'est évidemment un cas trivial, surtout puisque nous ne prenons pas en compte la gestion des erreurs dans les processus de travail et quel travailleur est actuellement disponible pour gérer de nouvelles charges. Dans le cas où nous aurions mis en place un serveur API pour gérer les demandes d'analyse entrantes, nous devrions considérer ces besoins supplémentaires.

### Regroupement de notre code

Maintenant que nous avons notre entrée divisée en charges de travail gérables, admettons de manière un peu artificielle — j'adorerais refactoriser cela plus tard — passons en revue comment nous pouvons la regrouper. Il s'avère que Node dispose de deux modules séparés pour configurer le code parallèle.

Celui que nous allons utiliser, le module [cluster](https://nodejs.org/api/cluster.html), permet essentiellement à un processus Node de créer des copies de lui-même et d'équilibrer le traitement entre eux comme il le juge approprié.

Cela est construit sur le module [child_process](https://nodejs.org/api/child_process.html), qui est moins étroitement couplé avec la parallélisation des programmes Node eux-mêmes et vous permet de créer d'autres processus, comme des programmes shell ou un autre binaire exécutable, et d'interfacer avec eux en utilisant l'entrée standard, la sortie, etc.

Je vous _recommande vivement_ de lire la documentation de l'API pour chaque module, car elles sont fantastiquement bien écrites, et même si vous êtes comme moi et trouvez la lecture de manuels sans but ennuyeuse et totalement fastidieuse, au moins familiarisez-vous avec les introductions de chaque module, cela vous aidera à vous ancrer dans le sujet et à élargir vos connaissances de l'écosystème Node.

Alors, parcourons le code. Le voici en vrac :

```
const cluster = require('cluster');
const numCPUs = require('os').cpus().length;
```

```
const { getTerminalInput } = require('./input');
```

```
(async function main () {
```

```
  if (cluster.isMaster) {
```

```
    const workerData = await getTerminalInput(numCPUs);
```

```
    for (let i = 0; i < workerData.length; i++) {
```

```
      const worker = cluster.fork();
      const params = { filenames: workerData[i] };
```

```
      worker.send(params);
```

```
    }
```

```
  } else {
```

```
    require('./worker');
```

```
  }
```

```
})();
```

Nos dépendances sont assez simples. D'abord, il y a le module cluster comme décrit ci-dessus. Ensuite, nous nécessitons le module [os](https://nodejs.org/api/os.html) dans le but expresse de déterminer combien de cœurs de CPU il y a sur notre machine — ce qui est un paramètre fondamental pour diviser notre charge de travail. Enfin, il y a notre fonction de gestion des entrées que j'ai externalisée dans un autre fichier pour des raisons de complétude.

Maintenant, la méthode principale est en fait assez simple. En fait, nous pourrions la décomposer en étapes :

1. Si nous sommes le processus principal, divisons l'entrée qui nous est envoyée de manière égale selon le nombre de cœurs de CPU de cette machine
2. Pour chaque charge de travail à venir, générez un travailleur par `cluster.fork` et configurez un objet que nous pouvons lui envoyer par le canal de messages RPC inter-processus du module [cluster], et envoyez-lui cette chose.
3. Si nous ne sommes pas en fait le module principal, alors nous devons être un travailleur — exécutez simplement le code dans notre fichier de travailleur et appelez cela une journée.

Rien de fou ne se passe ici, et cela nous permet de nous concentrer sur le vrai travail, qui consiste à déterminer comment le travailleur va utiliser la liste de noms de fichiers que nous lui donnons.

### Messagerie, Async et Streams, tous les éléments d'un régime alimentaire nutritif

Tout d'abord, comme ci-dessus, laissez-moi vous donner le code à consulter. Faites-moi confiance, le parcourir d'abord vous permettra de sauter toute explication que vous considéreriez comme triviale.

```
const Bufferer = require('../bufferer');
const Parser = require('../parser');
const { createReadStream } = require('fs');
```

```
process.on('message', async (options) =>; {
```

```
  const { filenames } = options;
  const parser = new Parser();
```

```
  const parseAndLog = async (buf) => console.log(await parser.parse(buf) + ',');
```

```
  const parsingQueue = filenames.reduce(async (result, filename) =>; {
```

```
    await result;
```

```
    return new Promise((resolve, reject) =>; {
```

```
      const reader = createReadStream(filename);
      const bufferer = new Bufferer({ onEnd: parseAndLog });
```

```
      reader
        .pipe(bufferer)
        .once('finish', resolve)
        .once('error', reject)
        });
    }, true);
```

```
  try {
    await parsingQueue;
    process.exit(0);
  } catch (err) {
    console.error(err);
    process.exit(1);
  }
```

```
});
```

Maintenant, il y a quelques hacks sales ici, alors soyez prudent si vous êtes l'un des non-initiés (je plaisante seulement). Regardons ce qui se passe en premier :

La première étape consiste à exiger tous les ingrédients nécessaires. Notez bien, cela est basé sur ce que le code lui-même fait. Alors laissez-moi simplement dire que nous allons utiliser un flux Writable personnalisé que j'ai affectueusement nommé Bufferer, un wrapper pour notre logique d'analyse de la dernière fois, également nommé de manière intrigante, Parser, et le bon vieux createReadStream fiable du module [fs](https://nodejs.org/api/fs.html).

Maintenant, voici où la magie opère. Vous remarquerez que rien n'est réellement enveloppé dans une fonction. L'ensemble du code du travailleur attend simplement qu'un message arrive au processus — le message de son maître avec le travail qu'il doit faire pour la journée. Excusez le langage médiéval.

Nous pouvons donc voir en premier lieu qu'il est asynchrone. Tout d'abord, nous extrayons les noms de fichiers du message lui-même — si c'était du code de production, je les validerais ici. En fait, bon sang, je les validerais dans notre code de traitement d'entrée plus tôt. Ensuite, nous instancions notre objet d'analyse — un seul pour l'ensemble du processus — c'est pour que nous puissions analyser plusieurs buffers avec un seul ensemble de méthodes. Une préoccupation que j'ai est qu'il gère la mémoire en interne, et en réflexion, c'est une bonne chose à réviser plus tard.

Ensuite, il y a un simple wrapper, `parseAndLog`, autour de l'analyse qui journalise le buffer PDF JSON-ifié avec une virgule ajoutée à la fin, juste pour faciliter la vie lors de la concaténation des résultats de l'analyse de plusieurs PDF.

![Image](https://cdn-media-1.freecodecamp.org/images/Tax7YoQWvdD11C5YgXFvCzLE7B6-rIS9WUYE)
_Votre travailleur, prêt et prêt pour un rendez-vous avec le destin._

Enfin, le cœur du sujet, la file d'attente asynchrone. Laissez-moi expliquer :

Ce travailleur a reçu sa liste de noms de fichiers. Pour chaque nom de fichier (ou chemin, en réalité), nous devons ouvrir un flux lisible à travers le système de fichiers afin que nous puissions obtenir les données PDF. Ensuite, nous devons générer notre Bufferer, (notre serveur, en suivant l'analogie du restaurant précédente), afin que nous puissions transporter les données vers notre Parser.

Le Bufferer est personnalisé. Tout ce qu'il fait vraiment, c'est accepter une fonction à appeler lorsqu'il a reçu toutes les données dont il a besoin — ici, nous lui demandons simplement d'analyser et de journaliser ces données.

Donc, maintenant que nous avons toutes les pièces, nous les connectons simplement :

1. Le flux lisible — le fichier PDF, se connecte au Bufferer
2. Le Bufferer termine et appelle notre méthode `parseAndLog` à l'échelle du travailleur

L'ensemble de ce processus est enveloppé dans une Promesse, qui elle-même est retournée à la fonction reduce dans laquelle elle se trouve. Lorsqu'elle est résolue, l'opération reduce continue.

Cette file d'attente asynchrone est en fait un modèle très utile, donc je le couvrirai plus en détail dans mon prochain article, qui sera probablement plus concis que les précédents.

En tout cas, le reste du code termine simplement le processus en fonction de la gestion des erreurs. Encore une fois, si c'était du code de production, vous pouvez parier qu'il y aurait une journalisation et une gestion des erreurs plus robustes ici, mais en tant que preuve de concept, cela semble correct.

### Donc ça marche, mais est-ce utile ?

Donc, voilà. Ce fut un peu un voyage, et cela fonctionne certainement, mais comme tout code, il est important de passer en revue ses forces et ses faiblesses. À première vue :

* Les flux doivent être empilés dans des buffers. Cela, malheureusement, défait le but d'utiliser des flux, et l'efficacité de la mémoire en souffre en conséquence. C'est un ajustement nécessaire avec du ruban adhésif pour travailler avec le module _pdfreader_. J'adorerais voir s'il existe un moyen de diffuser des données PDF et de les analyser à un niveau plus fin. Surtout si une logique d'analyse modulaire et fonctionnelle peut encore être appliquée.
* À ce stade embryonnaire, la logique d'analyse est également ennuyeusement fragile. Imaginez simplement, que se passe-t-il si j'ai un document plus long qu'une page ? Un tas d'hypothèses s'envolent et rendent le besoin de données PDF en streaming encore plus fort.
* Enfin, ce serait génial de voir comment nous pourrions développer cette fonctionnalité avec la journalisation et les points de terminaison API pour la fournir au public — pour un prix, ou pro bono, selon les contextes dans lesquels elle est utilisée.

Si vous avez des critiques ou des préoccupations spécifiques, j'adorerais les entendre aussi, puisque repérer les faiblesses du code est la première étape pour les corriger. Et, si vous connaissez une meilleure méthode pour diffuser et analyser des PDF de manière concurrente, faites-le moi savoir afin que je puisse le laisser ici pour toute personne lisant cet article pour une réponse. Dans tous les cas — ou pour tout autre but — envoyez-moi un [email](mailto:tom@fourzerofour.pw) ou contactez-moi sur [Reddit](https://www.reddit.com/u/_fourzerofour).