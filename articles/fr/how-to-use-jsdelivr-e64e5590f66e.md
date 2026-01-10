---
title: Comment utiliser JSDelivr
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-04-08T15:54:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-jsdelivr-e64e5590f66e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q1qvRLnBI5meBDrgpZW-BQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment utiliser JSDelivr
seo_desc: 'Easily download JavaScript libraries from npm and GitHub

  The most newbie-friendly way to add a library to a project is to:


  Search for the library

  Look for the source file

  Copy the source file

  Paste what you copied into the project.


  This works, but ...'
---

#### Téléchargez facilement des bibliothèques JavaScript depuis npm et GitHub

La manière la plus simple pour un débutant d'ajouter une bibliothèque à un projet est de :

1. Rechercher la bibliothèque
2. Chercher le fichier source
3. Copier le fichier source
4. Coller ce que vous avez copié dans le projet.

Cela fonctionne, mais c'est un processus fastidieux. C'est plus facile si vous utilisez des CDN comme JSDelivr.

### Qu'est-ce qu'un CDN ?

CDN signifie « content delivery network » (réseau de diffusion de contenu). Son objectif principal est de permettre aux utilisateurs de télécharger des fichiers plus rapidement. Lisez [cet article](https://www.fastly.com/blog/why-you-should-use-content-delivery-network) de Fastly si vous vous demandez si vous devriez utiliser un CDN.

Les CDN permettent aux utilisateurs de télécharger des fichiers plus rapidement en plaçant des centres de données partout dans le monde. Lorsque le navigateur voit un lien CDN, il servira la bibliothèque depuis le centre de données le plus proche de l'utilisateur. C'est ainsi que fonctionnent les CDN.

### Qu'est-ce que JSDelivr ?

JSDelivr est un type spécial de CDN. Il est conçu pour permettre aux utilisateurs de télécharger des bibliothèques JavaScript hébergées sur npm et Github. (Vous pouvez également charger des plugins Wordpress s'ils sont hébergés sur Wordpress.org).

Si vous utilisez JSDelivr (ou tout autre CDN qui sert des bibliothèques JavaScript), vous n'avez pas besoin de copier-coller les fichiers sources dans votre projet. Vous pouvez utiliser un lien comme celui-ci :

```
<script src="https://cdn.jsdelivr.net/npm/package-name"></script>
```

JSDelivr vous permet de spécifier la version de la bibliothèque que vous souhaitez télécharger. Si vous souhaitez spécifier une version, vous ajoutez le numéro de version après un `@`, comme ceci :

```
<script src="https://cdn.jsdelivr.net/npm/[email protected]"></script>
```

### Comment j'utilise JSDelivr

**J'utilise JSDelivr davantage comme un gestionnaire de paquets** puisque JSDelivr vous permet de spécifier la version d'une bibliothèque. Je peux mettre à niveau ou rétrograder la bibliothèque en changeant un numéro. Il n'est pas nécessaire de copier-coller la source originale dans mon projet.

Cependant, **je n'utilise plus beaucoup JSDelivr** parce que j'ai déjà un processus de build qui utilise Webpack. Webpack vous permet d'utiliser `require` pour importer des bibliothèques dans du JavaScript frontal. Il vous permet d'utiliser npm comme gestionnaire de paquets.

**Je n'utilise JSDelivr que pour des projets qui :**

1. Nécessitent une bibliothèque
2. La bibliothèque existe sur JSDelivr (ou d'autres CDN)
3. Le projet n'a pas Webpack (ou des outils similaires installés)

Un exemple de tel projet est les 20 composants dans [Learn JavaScript](https://learnjavascript.today/).

Voici pourquoi.

Les étudiants inscrits à Learn JavaScript essaient d'apprendre JavaScript. Je ne veux pas les distraire en leur faisant apprendre Webpack.

Au lieu de cela, je veux les aider à se concentrer sur ce pour quoi ils sont là — apprendre JavaScript. Je fais cela en supprimant la complexité des projets que nous construisons ensemble. Je réduis tout à du bon vieux HTML, CSS et JavaScript.

Nous avons parlé de ce qu'est JSDelivr, pourquoi l'utiliser et quand l'utiliser. Plongeons maintenant dans les détails de son utilisation.

Pour le reste de l'article, nous utiliserons une bibliothèque appelée [zl-fetch](https://github.com/zellwk/zl-fetch) comme exemple.

### Installation d'une bibliothèque

Pour installer une bibliothèque, vous devez ajouter une balise `<script>` qui pointe vers la bibliothèque sur JSDelivr. Vous pouvez charger la bibliothèque depuis npm ou Github, selon vos préférences.

J'ai tendance à charger les bibliothèques depuis npm.

```
<script src="https://cdn.jsdelivr.net/npm/package-name"></script>
```

Vous devez changer `package-name` par le nom de la bibliothèque que vous installez. Dans ce cas, c'est `zl-fetch`.

```
<script src="https://cdn.jsdelivr.net/npm/zl-fetch"></script>
```

Si vous n'êtes pas sûr du nom de la bibliothèque, vous pouvez rechercher sur [npm](https://www.npmjs.com/), ou directement sur [JSDelivr](https://www.jsdelivr.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/CndXOzCC03uVBwhf73T-AjP5qZxSjOLKzH4F)

### Spécifier une version

Par défaut, JSDelivr télécharge la dernière version d'une bibliothèque.

Je ne recommande pas d'utiliser la dernière version car les auteurs peuvent mettre à jour leur bibliothèque. Si ils mettent à jour leur bibliothèque, votre code peut cesser de fonctionner.

**Vous devez toujours spécifier un numéro de version.** Vous pouvez ajouter un numéro de version en ajoutant `@`, suivi du numéro de version après le nom du paquet, comme ceci :

```
<script src="https://cdn.jsdelivr.net/npm/[email protected]"></script>
```

**Les numéros de version suivent un format [Semver](https://zellwk.com/blog/semantic-versioning/).** Vous pouvez savoir quelles versions sont disponibles en vérifiant les tags disponibles sur Github.

![Image](https://cdn-media-1.freecodecamp.org/images/DvX7KL57jCAeQmDTJLSuhyMjtGTlyabzYuPv)

Dans notre cas, la version actuelle de `zl-fetch` est `2.1.9` :

```
<script src="https://cdn.jsdelivr.net/npm/[email protected]"></script>
```

### Charger un fichier spécifique

JSDelivr s'appuie sur les auteurs pour spécifier un fichier par défaut pour que le format ci-dessus fonctionne. **Si le fichier par défaut n'est pas spécifié, vous devez pointer vers le bon fichier.**

```
<script src="https://cdn.jsdelivr.net/npm/[email protected]/chemin-vers-fichier"></script>
```

Il existe deux façons de savoir quels fichiers sont disponibles.

Premièrement, vous pouvez rechercher le paquet sur JSDelivr. Vous verrez une liste de fichiers et de dossiers vers lesquels vous pouvez pointer :

![Image](https://cdn-media-1.freecodecamp.org/images/mK4mbrhilqZjV1wau0pffsmFst5cQXWIug0n)

Deuxièmement, si vous connaissez npm, vous pouvez utiliser npm pour installer le paquet quelque part sur votre ordinateur. Ensuite, utilisez votre Finder (ou Explorer) pour parcourir les fichiers.

Dans ce cas, disons que le fichier par défaut n'est pas spécifié, et nous voulons le fichier `dist/index.js`. Voici ce que vous écrirez :

```
<script src="https://cdn.jsdelivr.net/npm/[email protected]/dist/index.js"></script>
```

### Charger une version minifiée

Les fichiers minifiés sont généralement plus petits en taille. Les utilisateurs pourront télécharger les fichiers minifiés plus rapidement qu'un fichier non minifié.

JSDelivr minifie les fichiers automatiquement si vous utilisez l'extension `.min.js`.

```
<script src="https://cdn.jsdelivr.net/npm/[email protected]/dist/index.min.js"></script>
```

### Conclusion

J'espère que cet article vous donne un bon aperçu de ce que JSDelivr peut faire.

Merci d'avoir lu. Cet article vous a-t-il aidé ? Si c'est le cas, j'espère que vous envisagerez de [le partager](https://twitter.com/share?text=How%20to%20use%20JSDelivr%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/jsdelivr/). Vous pourriez aider quelqu'un d'autre. Merci beaucoup !

Cet article a été initialement publié sur [_mon blog._](https://zellwk.com/blog/jsdelivr)

Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.