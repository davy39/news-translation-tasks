---
title: Comment j'ai construit une application qui met en avant les premières et dernières
  phrases de grands romans
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-10T19:49:35.000Z'
originalURL: https://freecodecamp.org/news/write-better-sentences-and-do-javascript-crud-with-mean-while-mostly-avoiding-acronyms-fe17905bcec5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DAg4N0DRKpVri7bwj42WyA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: 'tech '
  slug: tech
- name: writing
  slug: writing
- name: writing tips
  slug: writing-tips
seo_title: Comment j'ai construit une application qui met en avant les premières et
  dernières phrases de grands romans
seo_desc: 'By Roger Collier

  I know sentences. In my decade as a print journalist, I’ve written hundreds of articles
  for dozens of publications. I’ve dished out more sentences than Judge Judy. But
  I didn’t study writing or journalism, at least not formally.

  My d...'
---

Par Roger Collier

Je connais les phrases. En tant que journaliste de presse écrite depuis une décennie, j'ai écrit des centaines d'articles pour des dizaines de publications. J'ai produit plus de phrases que le juge Judy. Mais je n'ai pas étudié l'écriture ou le journalisme, du moins pas formellement.

Mon diplôme est en génie électrique. J'ai appris à écrire en étudiant et en imitant les phrases des écrivains professionnels. Et les écrivains sont généralement à leur meilleur dans leurs premières et dernières phrases.

> « La phrase la plus importante dans tout article est la première. 

> Vous devriez accorder autant d'attention au choix de votre dernière phrase qu'à votre première. »

> — *On Writing Well*, William Zinsser

Une façon de se faire une idée de la construction de bonnes phrases est de taper le texte des écrivains que vous admirez tout en le lisant à voix haute. Hunter S. Thompson [a copié des romans entiers](http://menwithpens.ca/hunter-thompson/), tapant *The Great Gatsby* et *A Farewell to Arms* sur sa machine à écrire pour intégrer Fitzgerald et Hemingway dans ses doigts.

Je n'ai rien fait d'aussi extrême, mais depuis de nombreuses années, je tape les premières et dernières phrases de chaque livre que je lis, ce qui a abouti à une [liste toujours croissante](http://rogercollier.com/firstlast/) et, je l'espère, à des améliorations dans mon propre écriture.

Mais je ne peux lire qu'un nombre limité de livres et enregistrer qu'un nombre limité de phrases dans les quelques heures que j'ai chaque jour entre gagner ma vie et dormir. Des enfants à élever, des tapis à passer l'aspirateur, *Stranger Things* à regarder en binge — vous savez, la vie.

Ne serait-ce pas génial, me suis-je souvent dit, s'il existait un endroit en ligne où chacun pourrait contribuer avec les premières et dernières phrases des livres qu'il lit. Nous pourrions, ensemble, construire un trésor de phrases. Ce serait une excellente ressource pour les personnes qui, comme moi, aiment apprendre par imitation.

Eh bien, il se trouve que ma dernière obsession est d'apprendre à programmer en JavaScript. J'ai donc commencé, avec mes connaissances limitées, à créer cet endroit moi-même, en utilisant les frameworks JavaScript MongoDB, Express, Angular 2 et Node.js — connus collectivement sous le nom de MEAN stack. J'ai appelé cette application web (très simple) [First and Last](http://www.first-and-last.com/).

> « Certains apprécient les belles œuvres d'art ; d'autres apprécient les bons vins. Moi, j'apprécie les belles phrases. »

> — *How to Write a Sentence and How to Read One*, Stanley Fish

Le reste de cet article alternera entre des sections décrivant mes réflexions sur la manière d'écrire de meilleures phrases et des sections expliquant certaines des choses que j'ai apprises sur la programmation en travaillant sur First and Last.

Si vous êtes uniquement intéressé par l'écriture, n'hésitez pas à sauter les sections sur la programmation. Si vous êtes uniquement intéressé par la programmation, vous pouvez faire défiler les parties sur l'écriture. Si vous êtes uniquement intéressé par le repassage de vos sous-vêtements en faisant du parachutisme ou de l'escalade, veuillez aller [ici](https://en.wikipedia.org/wiki/Extreme_ironing) à la place.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
*Dernière phrase de *Where the Wild Things Are* de Maurice Sendak (crédit image : [geraldbrazel](https://www.flickr.com/photos/geraldbrazell/6389453857" rel="noopener" target="_blank" title="))*

### Lire de tout

Si vous aspirez à être une star littéraire — le prochain Jonathan Franzen ou Zadie Smith — alors tenez-vous en à la lecture de littérature de haut niveau. Apprenez des maîtres. Mais la plupart des gens qui veulent améliorer leur écriture ont des objectifs plus modestes.

> « Chaque livre que vous prenez a sa propre leçon ou leçons, et souvent les mauvais livres ont plus à enseigner que les bons. »

> — *On Writing*, Stephen King

Peut-être voulez-vous commencer un blog ou écrire un [article Medium pour Free Code Camp](https://medium.freecodecamp.com/how-to-get-published-in-the-freecodecamp-medium-publication-9b342a22400e). Peut-être voulez-vous impressionner votre patron en écrivant de meilleurs rapports.

Dans ma ville — Ottawa, Ontario — environ 150 000 personnes travaillent pour le gouvernement fédéral canadien. Des milliers d'autres sont employés par la ville. Les pièces d'écriture les plus fréquemment produites ici, je suppose, sont les documents gouvernementaux : mémos, notes d'information, règlements, communiqués de presse, politiques, avis publics, directives, etc.

La plupart de ces documents sont-ils bien écrits ? Disons simplement qu'il y a [place à l'amélioration](http://rogercollier.com/portfolio/gobbledygook/). Beaucoup de place. Une place de la taille du Canada.

![Image](https://cdn-media-1.freecodecamp.org/images/1BhI8MKJPFyLB8bY4lBfjmOZVTptxrq-CzqC)
*Je range mes livres par couleur. Joli. Mais mauvais pour la chasse aux livres. Hmm, je pense que Dune a une couverture beige…*

Les personnes qui veulent simplement écrire plus clairement et de manière plus concise peuvent trouver un plus grand bénéfice à étudier des phrases en dehors du domaine de la fiction littéraire. Lisez des non-fictions populaires. Lisez des livres pour enfants. Allez, lisez des boîtes de céréales.

Un bon endroit pour trouver des phrases solides et fonctionnelles est dans le travail des romanciers de genre, les auteurs qui traitent de détectives endurcis, d'amants éconduits, d'avocats astucieux et de vampires rêveurs.

Oui, ces livres sont souvent remplis de clichés. Mais ils ne sont jamais confus. Des auteurs comme James Patterson, Linwood Barclay et Harlan Coben sont des experts pour rendre les phrases faciles à lire. J'ai beaucoup appris en étudiant leur écriture — je ne suis pas un snob de livres — et vous trouverez certaines de leurs phrases dans First and Last.

> « Si cela ressemble à de l'écriture, je le réécris. »

> — *10 règles d'écriture*, Elmore Leonard

Les phrases dans la fiction commerciale sont sobres et directes. Elles contiennent peu de fioritures, pas de [hooptedoodle](http://www.nytimes.com/2001/07/16/arts/writers-writing-easy-adverbs-exclamation-points-especially-hooptedoodle.html). Les gens emmènent ces livres en vacances à la plage pour une raison. Vous pouvez les lire à moitié ivre et ne rien manquer.

En revanche, il est déconseillé de s'attaquer à Ulysses après votre cinquième Bahama Mama.

### Pas assez d'informations

Mon objectif technique principal en créant First and Last était simple : récupérer des données du navigateur, les stocker dans une base de données, puis les renvoyer au navigateur pour les afficher. C'est à peu près tout. Je voulais apprendre comment les informations circulent entre le front-end (Angular) et le back-end (Node et MongoDB).

En d'autres termes, je voulais créer une application qui effectue les quatre opérations de base de la base de données — créer, lire, mettre à jour et supprimer (CRUD). Je ne suis pas fan des acronymes, mais je dois admettre que j'aime CRUD et MEAN. Ce sont des mots doux pour ce pessimiste bourru.

#### Étape 1 : Obtenir l'entrée de l'utilisateur

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

#### Étape 2 : Stocker dans MongoDB

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

#### Étape 3 : Récupérer de la base de données et afficher dans le navigateur

![Image](https://cdn-media-1.freecodecamp.org/images/U5TYVnKb9emCiCSQL04LIKX3Asi3BzmyfPoy)

Comme je l'ai dit, simple. Pas d'algorithmes sophistiqués. Pas de visualisation de données. Juste le déplacement d'informations, principalement du texte, dans les deux sens. Pourtant, j'ai fait une supposition stupide qui m'a causé quelques ennuis.

Pour afficher mes phrases stockées dans le navigateur, je devais d'abord les récupérer de la base de données. Lorsque j'ai demandé à MongoDB trois entrées aléatoires, il a retourné un tableau avec trois objets. Dans Angular, j'ai assigné les données récupérées à un tableau local appelé « sentences », que j'ai déclaré comme contenant des objets.

```js
export class DisplayallComponent implements OnInit {  
  sentences: [Object]; 
  
```

Cela a bien fonctionné. Plus tard, j'ai décidé de permettre aux utilisateurs de « aimer » et de commenter les phrases. J'ai donc dû mettre à jour, dans le back-end, le schéma de données qui indiquait à MongoDB quel type d'informations stocker. J'ai déclaré un compteur de likes comme un nombre et un tableau de chaînes appelé « likedBy », où j'ai mis les noms d'utilisateur des utilisateurs qui avaient aimé une paire particulière de phrases.

```js
const SentenceSchema = mongoose.Schema({  
  likes: {  
    type: Number, default: 0 
  }, 
  likedBy: {  
    type: [String] 
  }
```

Encore une fois, aucun problème. Enfin, j'ai ajouté des commentaires. Chaque objet de commentaire contiendrait un nom d'utilisateur et le corps du commentaire. J'ai ajouté un tableau d'objets à mon schéma de données, le déclarant de la même manière que j'avais fait pour mon tableau « sentences » dans Angular.

```js
const SentenceSchema = mongoose.Schema({  
  likes: {  
    type: Number, default: 0 
  }, 
  likedBy: {  
    type: [String] 
  },
  comments: {
    type: [Object]
  } 
```

Lorsque j'ai testé les commentaires, cependant, cela n'a pas fonctionné. Il n'y avait aucune erreur évidente sur le front-end, aucun texte rouge hurlant dans la console de Chrome DevTools. Lorsque j'ai jeté un coup d'œil dans la base de données, cependant, les commentaires que j'avais soumis dans le navigateur étaient introuvables.

Après quelques essais et quelques jurons silencieux en pleine nuit, j'ai compris le problème. MongoDB, il s'est avéré, voulait que je sois plus spécifique qu'Angular. Je devais lui dire les types de données de chaque élément dans un objet de commentaire dans mon tableau « comments ». Se contenter de dire que le tableau contenait des objets n'était pas suffisant.

```js
comments: [{
       username: String,
       body: String
 }],
```

Les programmeurs, il semble, ont au moins une chose en commun avec l'auteur de *Cinquante nuances de Grey*. Parfois, il est payant d'être plus explicite.

### Gardez-le court (enfin, pas trop long)

![Image](https://cdn-media-1.freecodecamp.org/images/phWtplJkEFYCu24Y8xqHZfPvz7EI0Rf77IFs)
*Dernière phrase de *1984* de George Orwell (crédit image : [m.a.r.c.](https://www.flickr.com/photos/mabi/307544850" rel="noopener" target="_blank" title="))*

J'adore une bonne longue phrase, vraiment. Garrison Keillor, de la renommée de *A Prairie Home Companion*, écrit de belles phrases drôles et interminables qui ne se terminent que lorsque l'encre est épuisée. Le romancier E.L. Doctorow commence *Billy Bathgate* avec une phrase de 131 mots et se termine par un [monstre de 277 mots](http://www.first-and-last.com/search/billy%20bathgate). Dans *A Writer’s Life*, la légende de la non-fiction Gay Talese a une phrase qui fait **QUATRE CENT DIX-NEUF** mots de long.

![Image](https://cdn-media-1.freecodecamp.org/images/n0tB-a0UX4ZvZ5aiCJgahhpy457cXLMhfM0X)
*Une phrase looooooooongue. À ne pas essayer à la maison.*

Mais ne vous y trompez pas — ces écrivains se montrent. Ils sont bons dans ce qu'ils font et veulent que vous le sachiez. Et cela me va. Parce que dans les mains d'un grand écrivain, toute phrase, même une plus longue que le reçu Burger King de Shaquille O'Neal, sera sous contrôle.

Je ne suis pas Gay Talese. Vous non plus. Si vous allez trop loin, vous allez vous tromper. Faites-moi confiance. Je corrige l'écriture de journalistes pigistes et d'universitaires, et lorsque les clauses commencent à s'accumuler, les problèmes aussi. Modificateurs pendants. Pronoms mal assortis. Répétitions inelegantes. Mots inutiles. Conjonctions bizarres.

En bref, [blerg](https://www.youtube.com/watch?v=4DuKPHXRLjA).

Il est préférable de varier la longueur de vos phrases — c'est plus agréable à l'oreille — mais de les garder sous contrôle. Un mélange de phrases courtes et de longueur moyenne est votre meilleur pari.

![Image](https://cdn-media-1.freecodecamp.org/images/8eGzteXvd1M7dPH1IIN6UWEoZs4atbOUjT6e)
*Première phrase de *Neuromancer* de William Gibson (crédit image : [Frédéric Poirot](https://www.flickr.com/photos/fredarmitage/1057613629" rel="noopener" target="_blank" title="))*

### Trop d'informations

Je m'apprête à partager plus de code, et les choses vont devenir laides. Désolé, je suis nouveau dans ce domaine. Si vous voulez vous moquer de moi dans les commentaires, n'hésitez pas.

Les journalistes ont la peau dure. Nous en avons besoin. Plus tôt cette semaine, par exemple, j'ai reçu le courriel suivant — d'un certain type qui loue des appartements de luxe à Budapest — à propos d'un [article sur le jeûne intermittent](http://www.cmaj.ca/content/185/8/E321) que j'ai écrit en 2013.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
*Je m'excuse. Qu'est-ce que l'autophagie ?*

En tout cas, voici la fonction appelée dans Angular lorsqu'un utilisateur cliquait sur l'icône de pouce levé sous une entrée dans First and Last, telle que je l'avais écrite à l'origine.

```js
if(this.authService.loggedIn()) {
  const isInArray = sentence.likedBy.includes(this.username); 
  if(!isInArray) {
    sentence.likedBy.push(this.username); 
    this.authService.incrementLikes(sentence).subscribe(data => {
      this.sentences[index] = data;
```

Les utilisateurs pouvaient « aimer » une paire de phrases uniquement s'ils étaient connectés et n'avaient pas déjà « aimé » cette entrée. Lorsque ces conditions étaient remplies, un tableau local des utilisateurs qui avaient aimé cette paire de phrases était mis à jour.

Ensuite, un appel était fait pour mettre à jour le compteur de likes et le tableau « likedBy » dans la base de données. L'objet phrase entier était envoyé au back-end et, lorsque l'objet phrase mis à jour était retourné, le compteur de likes affiché dans le navigateur augmentait de un.

Dans mon modèle de données dans le back-end, j'avais ceci, malheureusement.

```js
module.exports.incrementLikes = function(sentence, callback) {
  const query = {_id:sentence._id};
  sentence.likes++;
  const likesPlus = sentence.likes;
  const likesUserArray = sentence.likedBy;
  const newLikeUser = likesUserArray[likesUserArray.length - 1];
  Sentences.findOneAndUpdate(query, 
    {likes: likesPlus, $push:{likedBy: newLikeUser}}, 
    {new: true}, callback
  );
}
```

Cette fonction incrémentait le compteur passé en paramètre et l'assignait à une variable locale, qui remplaçait le compteur de likes dans la base de données.

Si cela n'était pas assez détourné, j'ai copié l'ensemble du tableau « likedBy » de l'objet phrase passé à la fonction, puis j'ai créé UNE AUTRE variable locale pour contenir le dernier nom d'utilisateur de ce tableau avant, enfin, de pousser ce nom d'utilisateur dans le tableau « likedBy » de la base de données.

Cela fonctionnait, mais quand même. Ridicule.

Les seules informations dont MongoDB avait besoin d'Angular étaient l'ID unique de l'objet phrase à mettre à jour et le nom d'utilisateur de l'utilisateur qui a cliqué sur l'icône de pouce levé. Pas l'objet phrase entier.

Alors, à la place, j'ai créé un nouvel objet avec seulement ces deux éléments dans Angular pour le passer au back-end.

```js
onLikeClick(sentence, index) {
  if(this.authService.loggedIn()) {
    const isInArray = sentence.likedBy.includes(this.username); 
    if(!isInArray) {
      const updateLikes = {
        likeID: sentence._id,
        likeUsername: this.username
      }
      this.authService.incrementLikes(updateLikes).subscribe(data =>
          this.sentences[index] = data;
```

Ensuite, j'ai simplement incrémenté le compteur de likes à l'intérieur de la base de données (plutôt que d'incrémenter à l'extérieur et d'écraser la valeur de la base de données) et j'ai poussé le nom d'utilisateur passé à la fonction dans le tableau « likedBy » de la base de données.

```js
module.exports.incrementLikes = function(updateLikes, callback) {
  const query = {_id:updateLikes.likeID};
  const newLikeUser = updateLikes.likeUsername;
  Sentences.findOneAndUpdate(query, 
    {$inc: {likes: 1}, $push: {likedBy: newLikeUser}}, 
    {new: true}, callback
  );
}
```

Lorsque vous êtes un débutant en programmation, la joie de faire fonctionner quelque chose peut obscurcir le jugement. Il est tentant de laisser du code laid tranquille parce qu'après tout, il fait ce que je veux qu'il fasse. Mais si je valorise la concision lorsque j'écris en prose, pourquoi devrait-ce être différent lorsque j'écris du code ? Le désordre est du désordre.

Pas la peine de transmettre des informations qui ne sont pas nécessaires.

Lorsque un agent de police vous demande votre permis de conduire, vous ne lui donnez pas aussi votre carte de bibliothèque, votre certificat de naissance et votre mot de passe Ashley Madison.

### Gardez-le simple

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
*Quelques-uns de mes livres sur l'écriture. Et quelques-uns de mes orteils (sur le tapis).*

Je suis un grand fan de la lisibilité. Je pense que lorsque vous jetez un coup d'œil à un paragraphe dense de longues phrases — truffé d'acronymes ou de statistiques ou de symboles ou de titres de postes pompeux ou de longs mots affreux se terminant par « -isation » — votre cerveau soupire.

« Oh, comme c'est merveilleux », gémit-il avec sa petite bouche de cerveau. « Cela va être super amusant. »

Beaucoup de gens qui écrivent occasionnellement dans le cadre de leur travail, en particulier les universitaires et les experts en la matière, sont si préoccupés par le contenu qu'ils oublient souvent de considérer la présentation. Ils veulent être exhaustifs, faire tous leurs points — du point A au point Z — et entasser autant d'informations que possible dans chaque phrase.

Mais si le résultat final est illisible et peu susceptible d'être retenu, peut-être n'y a-t-il aucun intérêt. Je préfère que les lecteurs se souviennent de quelques idées présentées clairement plutôt qu'ils oublient instantanément une douzaine d'idées surchargées présentées de manière désordonnée.

> « Pauvre Faulkner. Pense-t-il vraiment que les grandes émotions viennent des grands mots ? Il pense que je ne connais pas les mots de dix dollars. Je les connais tous. Mais il y a des mots plus anciens, plus simples et meilleurs, et ce sont ceux que j'utilise. »

> — Ernest Hemingway

Il y aura toujours du désordre disgracié dans certaines formes d'écriture — c'est inévitable. Les articles sur la programmation et la technologie auront des acronymes. L'écriture commerciale aura des mots à la mode. Les résumés de recherches médicales peuvent contenir des ratios de taux ajustés de 0,86, IC à 96 % 0,4–0,56.

Néanmoins, nous pouvons essayer de faire mieux. Nous pouvons présenter uniquement les informations dont le lecteur a besoin, rien de plus. Nous pouvons résister à l'envie d'impressionner, de montrer nos vocabulaires améliorés par Google. Nous pouvons tailler les adjectifs décoratifs, éviter le jargon, éviter « whom » à tout prix. Nous pouvons faire plus que simplement déverser des mots sur une page.

Écrire bien est difficile. Mais c'est l'écrivain qui devrait souffrir. Pas le lecteur.