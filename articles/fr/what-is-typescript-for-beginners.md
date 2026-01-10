---
title: Qu'est-ce que TypeScript ? Un guide pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-21T15:55:07.000Z'
originalURL: https://freecodecamp.org/news/what-is-typescript-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/blog.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Qu'est-ce que TypeScript ? Un guide pour débutants
seo_desc: 'By Emmanuel Ohans

  A few weeks ago, I published an Intermediate TypeScript and React Handbook.

  It received many views and I got several emails. Most were “thank you” emails, but
  then there were others like:


  “… I am new to programming, what is TypeScr...'
---

Par Emmanuel Ohans

Il y a quelques semaines, j'ai publié un [Guide intermédiaire sur TypeScript et React](https://www.freecodecamp.org/news/build-strongly-typed-polymorphic-components-with-react-and-typescript/).

Il a reçu de nombreuses vues et j'ai reçu plusieurs emails. La plupart étaient des emails de "merci", mais il y en avait aussi comme :

> "... Je suis nouveau en programmation, qu'est-ce que TypeScript ?"

Et :

> "Merci pour cet ebook gratuit, mais comment apprendre TypeScript en tant que débutant ?"

J'avais expliqué au début que le guide était destiné aux développeurs intermédiaires qui connaissaient déjà un peu TypeScript — mais quand est-ce que cela a déjà empêché quelqu'un de télécharger une ressource gratuite ! :)

Alors dans ce guide, j'ai décidé de répondre aux questions de ces emails avec l'article que j'aurais aimé avoir lorsque j'ai appris TypeScript.

Maintenant, si vous lisez encore, je vais supposer que vous êtes un débutant en TypeScript.

Attachez votre ceinture. Vous allez vivre une expérience amusante.

## Expliquer TypeScript comme si j'avais 5 ans

Ma méthode d'enseignement est toujours restée la même.

Si vous ne pouvez pas l'expliquer à un enfant de 5 ans, alors peut-être que vous ne connaissez pas assez bien le sujet.

Au lieu de vous submerger avec beaucoup de jargon technique, essayons quelque chose de différent.

Utilisons une analogie que vous n'oubliez jamais.

Quand avez-vous visité le supermarché pour la dernière fois ?

Considérez TypeMart :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-134.png)
_Le supermarché TypeMart_

TypeMart est votre supermarché **grand** typique.

Vous voulez une variété d'articles d'épicerie ramassés après le travail ? Ils vous couvrent.

D'autre part, voici JMart :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-135.png)
_Le supermarché JMart_

JMart est un petit supermarché pour les achats rapides.

À Berlin, où je vis, nous appelons ceux-ci [Spätis](https://allaboutberlin.com/glossary/Sp%C3%A4ti#:~:text=A%20Sp%C3%A4ti%20or%20Sp%C3%A4tkauf%20(pronounced,and%20bodegas%20in%20other%20countries.). Ce sont essentiellement de petites épiceries.

Mais je suis sûr que vous n'êtes pas ici pour une leçon d'allemand.

Ce qui est important pour nous ici, c'est comment fonctionnent les supermarchés, JMart et TypeMart.

### Comment fonctionnent JMart et TypeMart

Avec _JMart_, vous entrez dans le magasin, trouvez l'article d'épicerie dont vous avez besoin et l'apportez à la caissière.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-136.png)
_Aller à la caissière pour payer votre facture_

À ce stade, vous n'êtes pas tout à fait sûr du coût de l'article d'épicerie que vous avez choisi.

Eh bien, c'est pourquoi vous allez à la caissière !

La caissière prend votre article, le scanne et vous dit combien il coûte.

Si elles sont "meilleures" dans leur travail, elles vous diront combien coûte l'article de tête (ou un catalogue manuel qu'elles gardent dans le tiroir).

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-137.png)
_Recevoir la facture de la caissière_

Le processus semble fragile, mais ça marche !

Ces caissières sont intelligentes. Aucun article n'est interdit. Et elles savent ce que coûte chaque article.

Un beau mardi, vous décidez d'essayer _TypeMart_.

Vous réalisez bientôt que les choses sont différentes dans TypeMart.

"Ces grands magasins ennuyeux," pourriez-vous dire.

Contrairement à JMart, ils ont une étiquette de prix pour tout dans le magasin.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-139.png)
_Panier de fruits avec des étiquettes de prix_

Ils vous privent de l'excitation et du regard sur le visage de la caissière lorsqu'elle calcule votre facture.

D'autre part, ce qu'ils vous donnent est une sorte d'assurance.

Il n'y a pas de surprises !

Vous savez exactement combien coûte chaque article que vous avez choisi.

C'est bénéfique pour les jours où votre portefeuille est maigre.

Chaque centime compte.

### Pourquoi cette analogie est-elle importante ?

Votre intuition était correcte.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-140.png)
_JMart représente JavaScript. TypeMart, TypeScript._

Dans l'analogie, JMart représente JavaScript et TypeMart, TypeScript.

Lorsque vous allez dans un supermarché, il y a un contrat non écrit : ils promettent d'avoir ce dont vous avez besoin à un prix équitable.

Et vous promettez de payer ce que vous achetez (sauf si vous faites du vol à l'étalage. Ne faites pas cela.)

C'est la même chose pour le code.

C'est un contrat non écrit, mais clair et brutal.

Votre contrat est avec l'utilisateur de votre application. Et vous promettez que votre application fonctionne.

Considérez un exemple avec une application de conférence comme Google Meet.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-141.png)
_L'interface web de Google Meet. Source : https://shrtm.nu/L0yk_

La promesse avec Google Meet est que vous pourrez toujours passer des appels vidéo. Ils promettent également que vous pouvez couper le son pendant que vous discutez avec votre partenaire ou regardez un TikTok rapide.

Heureusement qu'ils ne peuvent pas vous entendre !

Ou du moins, c'est ce que vous pensez ?

Imaginez si le bouton de coupure de son ne faisait pas ce qu'il promet.

Là vont vos secrets. Et avec eux, votre confiance en Google Meet.

C'est la même chose pour les applications que vous écrivez.

Vous promettez une application fonctionnelle, et vos utilisateurs font confiance à cela — en supposant que vous avez gagné leur confiance.

Ramenons cela à la maison.

Dans JMart et TypeMart, les marchandises sont de l'argent. Avec les logiciels, les marchandises sont des données.

Supposons que vous aviez une application de compteur basique.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-142.png)
_Interface utilisateur d'une application de compteur basique_

Votre utilisateur voit une interface utilisateur élégante, mais sous le capot, ce qui fait vraiment la magie est la _variable_ de compteur que vous augmentez ou diminuez.

Avec JMart (analogue à JavaScript), les marchandises ne sont pas étiquetées (avec des étiquettes de prix). Vous ne savez pas combien coûte quoi que ce soit. Vous allez à la caissière pour connaître votre sort.

C'est similaire à la façon dont JavaScript fonctionne.

Vous définissez et manipulez toutes sortes de variables, mais il n'y a pas d'étiquette explicite pour ce que sont les variables.

Vous faites confiance à ce que vous avez écrit et le passez au compilateur JavaScript pour connaître votre sort.

Considérez le code JavaScript trivial suivant :

```js
const JMart = {
    bananes: true,
    pommes: true,
    mangues: true
}
```

Dans une application JavaScript standard, vous pourriez écrire ce qui suit :

```js
const maCommande = JMart.voitures.prix

```

Même si `voitures` n'existe pas sur l'objet `JMArt`, il n'y a pas d'étiquette explicite qui définit cela.

Ainsi, lorsque vous écrivez votre code, vous ne savez peut-être pas que cette ligne de code est défectueuse... Jusqu'à ce que vous alliez à la caissière pour connaître votre sort.

La caissière ici est l'interpréteur JavaScript. Typiquement, cela se produit lorsque vous exécutez le code dans un navigateur.

Si vous le faites, vous obtenez alors une erreur qui dit `ne peut pas lire le prix de undefined`.

Si vous avez envoyé ce code (par erreur) en production, vos utilisateurs seront également confrontés à cette erreur laide.

Vous venez de compromettre leur confiance dans votre application.

Avec TypeScript, les choses sont différentes. Chaque morceau de données est "étiqueté" tout comme dans TypeMart.

Avant d'aller à la caissière (c'est-à-dire le navigateur) pour exécuter le code, vous pouvez savoir si votre application fonctionne comme elle le devrait !

Le compilateur TypeScript lancera une erreur vous indiquant que vous avez fait une erreur en accédant à une valeur incorrecte.

Cela se produit dans votre éditeur de code, avant d'ouvrir l'application dans un navigateur.

Comme ramasser un article d'épicerie que vous ne pouvez pas vous permettre dans TypeMart, vous voyez l'étiquette de prix.

Vous savez ce qu'il y a dans votre portefeuille. Il est juste de dire que vous avez été averti.

C'est là la différence initiale majeure entre TypeScript et JavaScript que vous devez connaître.

> TypeScript est JavaScript avec une syntaxe pour les types.

Où les types sont des étiquettes qui pendent autour de votre article d'épicerie (données), vous disant exactement ce que chaque morceau de code représente.

Considérez l'exemple trivial suivant en JavaScript :

```js

const maFonction = (a, b) => {
   return a * b
}

```

En TypeScript, ce code pourrait ressembler à ceci :

```ts
const maFonction = (a: string, b: string) => {
	return a * b
}
```

Remarquez comment cela ressemble presque à l'identique au code JavaScript.

Mais il a une différence majeure : les données `a` et `b` sont "étiquetées".

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-143.png)
_Les annotations de type des paramètres de la fonction_

Ce code précise spécifiquement que `a` et `b` attendus dans `maFonction` sont des chaînes de caractères.

Avec cette information (appelée annotation de type), TypeScript peut maintenant vous montrer des erreurs lorsque vous écrivez votre code.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-144.png)
_Voir ce code dans le terrain de jeu TypeScript : https://shrtm.nu/FlC0_

Ces erreurs s'afficheront généralement sous la forme de lignes rouges ondulées. Similaires aux erreurs dans des applications comme Microsoft Word.

Vous pouvez ensuite survoler ces lignes pour voir les détails de l'erreur.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-145.png)
_Les détails de l'erreur TypeScript_

Dans cet exemple simple, le cœur de l'erreur est que l'opération de multiplication ne doit pas être exécutée sur des chaînes de caractères.

### Erreurs non exceptionnelles

Si vous êtes un développeur JavaScript plus expérimenté, vous pouvez déjà remarquer que l'exemple de code ci-dessus ne lance pas d'erreur en JavaScript standard.

```js
const maFonction = (a, b) => {
    return a * b
}

```

Si vous calculez "1" * "6" en JavaScript, vous obtiendrez 6.

En interne, JavaScript force les chaînes de caractères en nombres et effectue l'opération de multiplication.

Ces types d'erreurs qui ne échouent pas en JavaScript, mais qui génèrent des erreurs en TypeScript, sont appelées erreurs non exceptionnelles.

Celles-ci sont censées vous aider à prévenir des bugs désagréables dans votre application.

Vous ne devez pas nécessairement vous en soucier à ce stade de votre parcours TypeScript, mais cela vaut la peine d'être mentionné.

Comme vous pouvez le voir, TypeScript va loin pour vous aider à attraper des comportements indésirables dans votre code.

Une façon simple de corriger cela serait de typer les paramètres explicitement, c'est-à-dire, `a` et `b` comme des nombres :

```ts
const maFonction = (a: number, b: number) => {
   return a * b
}
```

Et l'erreur disparaît !

Ne soyez pas fâché contre TypeScript pour avoir attiré votre attention sur ces erreurs non exceptionnelles.

Elles sont des sources potentielles de bugs dans votre application.

TypeScript à la rescousse 🚨🏽

## Conclusion

Demandez-vous, est-ce que je sais maintenant ce qu'est TypeScript ?

Oui, vous le savez — conceptuellement.

TypeScript est à JavaScript ce que TypeMart est à JMart.

TypeScript vous donne une manière organisée de "étiqueter" les données au sein de votre application pour prévenir des erreurs inconnues.

Ces erreurs seront attrapées et portées à votre attention avant d'aller à la caissière — c'est-à-dire, avant d'exécuter votre application.

Prenez un moment pour digérer cette information. Elle sera cruciale lorsque vous [apprendrez plus sur TypeScript](https://www.freecodecamp.org/news/an-introduction-to-typescript/).

Donnez-vous une tape dans le dos et allez écrire votre première application TypeScript.



### Ressources supplémentaires

* [Guide intermédiaire sur TypeScript et React](https://www.freecodecamp.org/news/build-strongly-typed-polymorphic-components-with-react-and-typescript/) : Apprenez TypeScript intermédiaire avec React en construisant un composant polymorphe fortement typé.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/image-148.png)
_[Guide intermédiaire sur TypeScript et React](https://www.freecodecamp.org/news/build-strongly-typed-polymorphic-components-with-react-and-typescript/)_



* Enviez-vous un exercice rapide sur TypeScript ? Repérez et corrigez l'erreur dans l'exemple décrit précédemment. Utilisez l'éditeur en ligne officiel appelé le terrain de jeu TypeScript ici : [[https://shrtm.nu/FlC0](https://shrtm.nu/FlC0)]