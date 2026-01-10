---
title: Types de données variables expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-07T16:54:47.000Z'
originalURL: https://freecodecamp.org/news/variable-data-types-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/data-types-thumbnail2.jpg
tags:
- name: arrays
  slug: arrays
- name: object
  slug: object
- name: General Programming
  slug: programming
- name: variables
  slug: variables
seo_title: Types de données variables expliqués
seo_desc: "By Deborah Kurata\nWalking into a hardware store, it's not enough to say:\
  \ \"I need a tool\". You need to be specific about the type of tool you need. \n\
  Each tool type has its particular purpose: A hammer to drive a nail into wood, a\
  \ paint brush to paint,..."
---

Par Deborah Kurata

En entrant dans un magasin de bricolage, il ne suffit pas de dire : "J'ai besoin d'un outil". Vous devez être précis sur le type d'outil dont vous avez besoin. 

Chaque type d'outil a son utilisation particulière : un marteau pour enfoncer un clou dans le bois, un pinceau pour peindre, et une clé pour serrer ou desserrer des écrous et des boulons.

Il en va de même pour les variables que nous utilisons pour stocker des données dans notre code. Peu importe le langage de programmation que vous utilisez, lors de la création d'un site web ou d'une application, vous voudrez utiliser le type de variable approprié pour un usage particulier. Nous examinerons les types de base ainsi que des types plus complexes tels que les tableaux (listes) et les objets.

Vous pouvez également regarder la vidéo associée ici qui passe en revue les principaux types de données variables.

%[https://youtu.be/8cTu_RrkiME]

## **Types de données de base**

Les types de données de base les plus courants disponibles dans la plupart des langages de programmation incluent :

**nombres** : nous utilisons ceci pour toute donnée qui est numérique ou qui doit être traitée comme un nombre pour des opérations d'addition ou d'autres opérations mathématiques. 

Dans certains langages de programmation, il existe plusieurs types de données pour les nombres, selon que le nombre est un entier, un décimal ou une monnaie, par exemple. 

Si nous construisions un jeu de devinettes de nombres, nous stockerions le nombre deviné dans un type de donnée numérique, comme ceci :

```code
usersGuess = 3
```

**chaîne de caractères** : nous utilisons ceci pour toute donnée qui est du texte. Par exemple, un nom, une adresse ou un message. Dans la plupart des langages de programmation, les chaînes de caractères nécessitent des guillemets. Remarquez que le texte à l'intérieur des guillemets peut inclure des espaces et d'autres caractères spéciaux.

```code
usersName = "Jack Harkness"
```

**date** : nous utilisons ceci pour les données qui sont une date ou une heure, comme un anniversaire.

```code
usersBirthday = April 14, 2001
```

**Booléen** : nous utilisons ceci pour les données qui n'ont que la valeur `true` ou `false`. Dans un jeu de devinettes de nombres, la supposition de l'utilisateur était soit correcte, soit incorrecte. Il n'y a pas d'autre valeur.

```code
correctGuess = true
```

Pour les langages de programmation considérés comme "fortement typés", tels que C# et TypeScript, le type de donnée définit le genre de données qui peut être assigné à cette variable. Vous verrez une erreur si vous essayez de mettre le mauvais type de données dans une variable.

```typescript
pageTitle = 'Pet List';	// Variable est une chaîne de caractères.

pageTitle = 42;			// Erreur
						// Impossible de mettre un nombre dans une variable de type chaîne de caractères
```

Avec les langages "dynamiquement typés" tels que JavaScript et Python, le type de donnée définit le genre de données actuellement assigné à cette variable. Ce type peut changer si vous mettez un type de données différent dans cette variable. Ainsi, le type change dynamiquement en fonction de la valeur actuellement assignée.

```javascript
pageTitle = 'Pet List';			// Le type de la variable est une chaîne de caractères

pageTitle = 42;					// Le type de la variable est maintenant un nombre
```

## **Type de donnée Tableau (Liste)**

Un autre type de donnée important en programmation est le tableau, qui dans certains langages de programmation est appelé une liste.

Supposons que nous ajoutons une fonctionnalité à notre site web ou à notre application afin que l'utilisateur puisse fournir le nom de chacun de ses animaux de compagnie. Nous pourrions stocker chaque nom dans une variable séparée comme montré dans la Figure 1.

![Photos de trois chats avec trois variables pour stocker le nom de chaque chat.](https://www.freecodecamp.org/news/content/images/2023/03/array1.jpg)
_Figure 1. Utilisation de variables de chaîne de caractères séparées pour stocker plusieurs éléments._

Mais nous devrions alors limiter le nombre d'animaux de compagnie que nous pourrions permettre en fonction du nombre de variables que nous aurions défini.

Les tableaux résolvent ce problème. Un **tableau** est une collection ou un ensemble d'éléments de données. Vous pouvez penser à un tableau comme une liste d'éléments.

Les éléments de données dans un tableau sont souvent du même type, donc vous pouvez avoir un tableau de nombres, de chaînes de caractères ou de dates.

Dans certains langages de programmation, y compris C#, TypeScript, JavaScript et Python, les tableaux sont définis avec des crochets : [ ] et chaque valeur dans le tableau est séparée par des virgules.

```code
petNames = ["Yoyo", "Vanny", "Cali"]
```

Ici, nous définissons un tableau de chaînes de caractères. Rappelez-vous que les chaînes de caractères doivent être enfermées dans des guillemets. 

![Photos de trois chats avec un seul tableau pour stocker le nom de chaque chat.](https://www.freecodecamp.org/news/content/images/2023/03/array2.jpg)
_Figure 2. Utilisation d'un tableau pour stocker plusieurs éléments._

Avec les tableaux, l'utilisateur peut avoir un nombre presque illimité d'éléments, tels que des noms, car nous pouvons continuer à ajouter au tableau.

```code
petNames = ["Yoyo", "Vanny", "Cali", "Ben", "Maki"]
```

## **Type de donnée Objet (Type de donnée personnalisé)**

Qu'en est-il des données qui représentent des choses dans notre application ? Des choses comme celles montrées dans la Figure 3 :

* Un animal de compagnie
* Un client
* Un produit
* Ou un post, et je veux réellement dire un post sur les réseaux sociaux ici, mais c'est assez proche.

![Quatre icônes représentant un animal de compagnie, un client, un produit et un post](https://www.freecodecamp.org/news/content/images/2023/03/object1.jpg)
_Figure 3. Exemples de types de données personnalisés (objets)._

Nous pouvons stocker des informations détaillées sur une chose, comme un animal de compagnie, un client ou un article de blog, dans un ensemble de variables de chaîne de caractères, de nombre et de date. Mais pour garder cet ensemble de variables pour une chose particulière ensemble comme une seule variable, nous voulons un type de donnée personnalisé qui décrit cette chose. 

Pensez à un objet comme un type de donnée personnalisé qui regroupe un ensemble de variables liées pour une chose particulière.

Passons en revue comment définir un objet comme un type de donnée personnalisé.

### Étape 1 : Identifier les propriétés (caractéristiques)

Pour définir un type de donnée objet, nous identifions d'abord les données que nous voulons stocker pour l'objet. Ce sont souvent des caractéristiques de l'objet, comme le nom, le type et l'âge d'un animal de compagnie. En programmation, nous appelons chacune de ces caractéristiques une **propriété** de l'objet.

Regardons quelques exemples.

![Quatre icônes représentant un animal de compagnie, un client, un produit et un post et leurs caractéristiques](https://www.freecodecamp.org/news/content/images/2023/03/object2.jpg)
_Figure 4. Identifier les données à stocker (ou à conserver) pour chaque objet._

Pour un client, les propriétés pourraient être le nom du client, l'adresse de livraison et le mode de paiement par défaut. 

Un produit peut avoir un nom de produit, une description et une valeur booléenne définissant si le produit est actuellement en stock.

Et pour un article de blog, nous pouvons vouloir stocker le nom de l'utilisateur, le texte de l'article et la date.

Chacune de ces propriétés est une propriété de notre objet.

À ce stade, nous avons la liste des propriétés pour l'objet. Nous voulons stocker des données pour chacune de ces propriétés.

### Étape 2 : Assigner un nom de propriété

Une fois que nous avons défini les propriétés, nous assignons un nom à chaque propriété comme montré dans la Figure 5. 

![Quatre icônes représentant un animal de compagnie, un client, un produit et un post et leurs noms de propriétés](https://www.freecodecamp.org/news/content/images/2023/03/object3.jpg)
_Figure 5. Définir un nom de variable pour chaque propriété d'objet._

Les noms suivent les conventions du langage de programmation que vous utilisez. En général, les noms de propriétés ne peuvent pas avoir d'espaces ou de caractères spéciaux. Ils sont souvent définis en utilisant le camel case, avec la première lettre en minuscule et chaque mot supplémentaire en majuscule.

Chaque propriété a également un type de donnée de base. `petName`, `customerName`, `productName` et `userName` sont des chaînes de caractères. `age` est un nombre, `inStock` est une valeur booléenne (vrai ou faux), et `postDate` est une date.

Nous pourrions suivre des variables séparées pour chacune de ces propriétés d'animal de compagnie et pour chacune de ces propriétés de client et pour chacune de ces propriétés de post. Mais nous finirions avec beaucoup de variables non organisées.

Regroupons plutôt chaque ensemble de propriétés liées dans un objet.

### Étape 3 : Regrouper les propriétés pour l'objet

Nous regroupons les propriétés d'un objet ensemble en utilisant la syntaxe littérale d'objet. Cela garde les données d'un objet ensemble et facilite leur utilisation en tant qu'ensemble.

La syntaxe utilisée pour regrouper les propriétés dépend du langage de programmation que vous utilisez. Dans des langages tels que JavaScript, TypeScript et C#, les propriétés d'objet sont regroupées dans des accolades ({ }).

```code
pet = {
	petName: "Yoyo",
    petType: "cat",
    age: 11
}
```

![Quatre icônes représentant un animal de compagnie, un client, un produit et un post et un exemple d'objet.](https://www.freecodecamp.org/news/content/images/2023/03/object4.jpg)
_Figure 6. Regrouper les propriétés pour chaque objet_

Pour chaque objet, la variable à gauche du signe égal est la variable d'objet et représente un animal de compagnie, un client, un produit ou un post spécifique. À droite du signe égal, à l'intérieur des accolades, nous listons chaque nom de propriété, un deux-points, et les données (souvent appelées une valeur). Nous séparons les propriétés par une virgule.

Pour le dire autrement, vous pouvez penser à un objet comme une collection de paires nom et valeur. Le nom est le nom de la propriété et la valeur est la donnée que vous voulez stocker pour cette propriété. 

Dans la Figure 6, nous avons défini un objet animal de compagnie avec un ensemble spécifique de propriétés, et une valeur pour chaque propriété. Même chose pour le client, et ainsi de suite.

## Essayez par vous-même !

Arrêtons-nous ici un moment et réfléchissons aux objets. Quel est votre passe-temps préféré ? Si vous construisiez un site web ou une application pour soutenir ce passe-temps, quels objets pourriez-vous définir ?

Peut-être aimez-vous cuisiner, donc vous construiriez une application de recettes avec vos recettes préférées. Vous travaillez avec les données de chaque recette en utilisant un objet avec des propriétés telles que les ingrédients, les étapes de la recette, la température de cuisson et le temps.

Ou disons que vous aimez le sport. Vous suivriez les données de chaque joueur en utilisant un objet avec des propriétés telles que le nom, la position et les statistiques. Et vous suivriez les données de chaque jeu en utilisant un autre objet avec des propriétés telles que les équipes et le score.

Quels objets avez-vous définis pour votre passe-temps ?

## **Conclusion**

Une variable a un type de donnée tel que nombre, chaîne de caractères (pour le texte), date et booléen (pour vrai ou faux).

Un tableau stocke un ensemble d'éléments de données, souvent du même type.

Un objet représente quelque chose dans le site web ou l'application, comme un animal de compagnie, un client ou un article de blog. L'objet regroupe les propriétés liées stockant les données pour l'objet.

Maintenant que vous connaissez tout sur les types de données, vous pouvez créer des variables du type approprié pour stocker toute donnée dont vous avez besoin pour votre site web ou votre application.

Si vous êtes autodidacte ou nouveau en programmation et que vous voulez plus d'informations sur les concepts généraux de programmation, consultez ce cours :

%[https://youtu.be/yO4JaMVMerA]