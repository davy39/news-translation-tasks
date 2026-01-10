---
title: Comment utiliser MongoDB + Mongoose avec Node.js – Bonnes pratiques pour les
  développeurs back-end
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-27T00:17:19.000Z'
originalURL: https://freecodecamp.org/news/mongodb-mongoose-node-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/node-mongodb-fundamentals.png
tags:
- name: 'Back end development '
  slug: back-end-development
- name: JavaScript
  slug: javascript
- name: MongoDB
  slug: mongodb
- name: mongoose
  slug: mongoose
- name: node js
  slug: node-js
seo_title: Comment utiliser MongoDB + Mongoose avec Node.js – Bonnes pratiques pour
  les développeurs back-end
seo_desc: "By Mehul Mohan\nMongoDB is undoubtedly one of the most popular NoSQL database\
  \ choices today. And it has a great community and ecosystem. \nIn this article,\
  \ we'll review some of the best practices to follow when you're setting up MongoDB\
  \ and Mongoose wi..."
---

Par Mehul Mohan

MongoDB est sans aucun doute l'un des choix de bases de données NoSQL les plus populaires aujourd'hui. Et il dispose d'une grande communauté et d'un écosystème solide. 

Dans cet article, nous allons passer en revue certaines des meilleures pratiques à suivre lorsque vous configurez MongoDB et Mongoose avec Node.js.

## Prérequis pour cet article

Cet article fait partie du parcours d'apprentissage back-end de codedamn, où nous commençons par les bases du back-end et les couvrons en détail. Par conséquent, je suppose que vous avez déjà une certaine expérience avec JavaScript (et Node.js). 

Actuellement, nous en sommes ici :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2020-10-20-at-9.29.47-PM.png)

Si vous avez très peu d'expérience avec Node.js/JavaScript ou le back-end en général, [c'est probablement un bon point de départ](https://codedamn.com/learning-paths/backend). Vous pouvez également trouver [un cours gratuit sur Mongoose + MongoDB + Node.js ici](https://codedamn.com/learn/node-mongodb-fundamentals). Plongeons dans le sujet.

## Pourquoi avez-vous besoin de Mongoose ?

Pour comprendre pourquoi nous avons besoin de Mongoose, comprenons comment MongoDB (et une base de données) fonctionne au niveau architectural.

* Vous avez un serveur de base de données (par exemple, le serveur communautaire MongoDB)
* Vous avez un script Node.js en cours d'exécution (en tant que processus)

Le serveur MongoDB écoute sur une socket TCP (généralement), et votre processus Node.js peut s'y connecter en utilisant une connexion TCP. 

Mais au-dessus de TCP, MongoDB a également son propre protocole pour comprendre ce que le client (notre processus Node.js) veut que la base de données fasse.

Pour cette communication, au lieu d'apprendre les messages que nous devons envoyer sur la couche TCP, nous abstraisons cela à l'aide d'un logiciel "pilote", appelé pilote MongoDB dans ce cas. Le pilote MongoDB est disponible en tant que [package npm ici](https://www.npmjs.com/package/mongodb).

Maintenant, rappelez-vous, le pilote MongoDB est responsable de la connexion et de l'abstraction des requêtes/responses de communication de bas niveau pour vous – mais cela ne vous mène que jusqu'à un certain point en tant que développeur. 

Parce que MongoDB est une base de données sans schéma, elle vous donne beaucoup plus de pouvoir que ce dont vous avez besoin en tant que débutant. Plus de pouvoir signifie plus de surface pour faire des erreurs. Vous devez réduire votre surface de bugs et d'erreurs que vous pouvez faire dans votre code. Vous avez besoin de quelque chose de plus.

Rencontrez Mongoose. Mongoose est une abstraction sur le pilote natif MongoDB (le package npm que j'ai mentionné ci-dessus). 

La règle générale avec les abstractions (telle que je la comprends) est que avec chaque abstraction, vous perdez un certain pouvoir d'opération de bas niveau. Mais cela ne signifie pas nécessairement que c'est mauvais. Parfois, cela booste la productivité de 1000x+ parce que vous n'avez jamais vraiment besoin d'avoir un accès complet à l'API sous-jacente de toute façon.

Une bonne façon d'y penser est que vous pouvez techniquement créer une application de chat en temps réel à la fois en C et en Python. 

L'exemple Python serait beaucoup plus facile et plus rapide pour vous en tant que développeur à implémenter avec une productivité plus élevée. 

C _peut_ être plus efficace, mais cela viendra à un coût énorme en termes de productivité/vitesse de développement/bogs/plantages. De plus, pour la plupart, vous n'avez pas besoin d'avoir le pouvoir que C vous donne pour implémenter des websockets.

De même, avec Mongoose, vous pouvez limiter votre surface d'accès à l'API de bas niveau, mais débloquer beaucoup de gains potentiels et une bonne DX.

## Comment connecter Mongoose + MongoDB

Tout d'abord, voyons rapidement comment vous devriez vous connecter à votre base de données MongoDB en 2020 avec Mongoose :

```js
mongoose.connect(DB_CONNECTION_STRING, {
	useNewUrlParser: true,
	useUnifiedTopology: true,
	useCreateIndex: true,
	useFindAndModify: false
})
```

Ce format de connexion garantit que vous utilisez le nouveau parseur d'URL de Mongoose et que vous n'utilisez aucune pratique obsolète. Vous pouvez lire en profondeur tous ces messages de dépréciation [ici](https://mongoosejs.com/docs/deprecations.html) si vous le souhaitez.

## Comment effectuer des opérations Mongoose

Passons maintenant à la discussion des opérations avec Mongoose et comment vous devriez les effectuer.

Mongoose vous offre des options pour deux choses :

1. Requêtes basées sur curseur
2. Requête de récupération complète

### Requêtes basées sur curseur

Les requêtes basées sur curseur signifient que vous travaillez avec un seul enregistrement à la fois tout en récupérant un seul ou un lot de documents à la fois depuis la base de données. C'est une manière efficace de travailler avec de grandes quantités de données dans un environnement de mémoire limitée. 

Imaginez que vous devez analyser des documents d'une taille totale de 10 Go sur un serveur cloud de 1 Go/1 cœur. Vous ne pouvez pas récupérer toute la collection car cela ne tiendra pas sur votre système. Le curseur est une bonne (et la seule ?) option ici.

### Requête de récupération complète

Il s'agit du type de requête où vous obtenez la réponse complète de votre requête en une seule fois. Pour la plupart, c'est ce que vous utiliserez. Par conséquent, nous nous concentrerons principalement sur cette méthode ici.

## Comment utiliser les modèles Mongoose

Les modèles sont le superpouvoir de Mongoose. Ils vous aident à appliquer les règles de "schéma" et fournissent une intégration transparente de votre code Node dans les appels de base de données. 

La toute première étape consiste à définir un bon modèle :

```
import mongoose from 'mongoose'

const CompletedSchema = new mongoose.Schema(
	{
		type: { type: String, enum: ['course', 'classroom'], required: true },
		parentslug: { type: String, required: true },
		slug: { type: String, required: true },
		userid: { type: String, required: true }
	},
	{ collection: 'completed' }
)

CompletedSchema.index({ slug: 1, userid: 1 }, { unique: true })

const model = mongoose.model('Completed', CompletedSchema)
export default model

```

Voici un exemple réduit directement depuis la base de code de codedamn. Quelques points intéressants à noter ici :

1. Essayez de garder `required: true` sur tous les champs qui sont requis. Cela peut vous éviter beaucoup de problèmes si vous n'utilisez pas un système de vérification de type statique comme TypeScript pour vous aider avec les noms de propriétés corrects lors de la création d'un objet. De plus, la validation gratuite est super cool aussi.
2. Définissez des index et des champs uniques. La propriété `unique` peut également être ajoutée dans un schéma. Les index sont un sujet vaste, donc je ne vais pas entrer dans les détails ici. Mais à grande échelle, ils peuvent vraiment vous aider à accélérer vos requêtes.
3. Définissez explicitement un nom de collection. Bien que Mongoose puisse automatiquement donner un nom de collection basé sur le nom du modèle (`Completed` ici, par exemple), c'est beaucoup trop d'abstraction à mon avis. Vous devriez au moins connaître les noms de vos bases de données et collections dans votre base de code.
4. Restreignez les valeurs si vous le pouvez, en utilisant des énumérations.

## Comment effectuer des opérations CRUD

CRUD signifie **C**réer, **L**ire, **M**ettre à jour et **D**étruire. Ce sont les quatre options fondamentales avec lesquelles vous pouvez effectuer toute sorte de manipulation de données dans une base de données. Passons rapidement en revue quelques exemples de ces opérations.

### L'opération de création

Cela signifie simplement créer un nouvel enregistrement dans une base de données. Utilisons le modèle que nous avons défini ci-dessus pour créer un enregistrement :

```js
try {
    const res = await CompletedSchema.create(record)
} catch(error) {
	console.error(error)
    // gérer l'erreur
}
```

Encore quelques conseils ici :

1. Utilisez async-await au lieu de callbacks (plus agréable à l'œil, pas d'avantage de performance révolutionnaire en tant que tel)
2. Utilisez des blocs try-catch autour des requêtes car votre requête _peut_ échouer pour un certain nombre de raisons (enregistrement en double, valeur incorrecte, etc.)

### L'opération de lecture

Cela signifie lire les valeurs existantes depuis la base de données. C'est simple comme cela en a l'air, mais il y a quelques pièges que vous devriez connaître avec Mongoose :

```
const res = await CompletedSchema.find(info).lean()
```

1. Pouvez-vous voir l'appel de la fonction `lean()` là ? Il est super utile pour la performance. Par défaut, Mongoose traite le(s) document(s) retourné(s) depuis la base de données et ajoute ses méthodes _magiques_ dessus (par exemple `.save`)
2. Lorsque vous utilisez `.lean()`, Mongoose retourne des objets JSON simples au lieu de documents lourds en mémoire et en ressources. Rend les requêtes plus rapides et moins coûteuses pour votre CPU aussi.
3. Cependant, vous pouvez omettre `.lean()` si vous pensez réellement à mettre à jour les données (nous verrons cela ensuite)

### L'opération de mise à jour

Si vous avez déjà un document Mongoose avec vous (sans utiliser `.lean()`), vous pouvez simplement modifier la propriété de l'objet et l'enregistrer en utilisant `object.save()` :

```
const doc = await CompletedSchema.findOne(info)
doc.slug = 'something-else'
await doc.save()
```

Rappelez-vous qu'ici, deux appels à la base de données sont effectués. Le premier est sur `findOne` et le second est sur `doc.save`. 

Si vous le pouvez, vous devriez toujours réduire le nombre de requêtes frappant la base de données (car si vous comparez la mémoire, le réseau et le disque, le réseau est presque toujours le plus lent).

Dans l'autre cas, vous pouvez utiliser une requête comme celle-ci :

```
const res = await CompletedSchema.updateOne(<condition>, <query>).lean()
```

et il ne fera qu'un seul appel à la base de données.

### L'opération de suppression

La suppression est également simple avec Mongoose. Voyons comment vous pouvez supprimer un seul document :

```js
const res = await CompletedSchema.deleteOne(<condition>)
```

Tout comme `updateOne`, `deleteOne` accepte également le premier argument comme condition de correspondance pour le document. 

Il existe également une autre méthode appelée `deleteMany` qui ne doit être utilisée que lorsque vous savez que vous voulez supprimer plusieurs documents. 

Dans tout autre cas, utilisez toujours `deleteOne` pour éviter les suppressions multiples accidentelles, surtout lorsque vous essayez d'exécuter des requêtes vous-même. 

## Conclusion

Cet article était une simple introduction au monde de Mongoose et MongoDB pour les développeurs Node.js. 

Si vous avez aimé cet article, vous pouvez améliorer vos compétences en tant que développeur en suivant le [parcours d'apprentissage back-end de codedamn](https://codedamn.com/learning-paths/backend). N'hésitez pas à me contacter sur [Twitter](https://twitter.com/mehulmpt) pour tout retour !