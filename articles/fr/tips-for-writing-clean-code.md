---
title: Conseils simples pour vous aider à écrire du code propre
subtitle: ''
author: Nitin Sharma
co_authors: []
series: null
date: '2025-02-04T15:53:47.911Z'
originalURL: https://freecodecamp.org/news/tips-for-writing-clean-code
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738684292390/6e844cd5-28f8-42e9-b9e3-cc6ded9ec72f.png
tags:
- name: programming
  slug: programming-ciovqvfcb008mb253jrczo9ye
- name: clean code
  slug: clean-code
- name: technology
  slug: technology
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
seo_title: Conseils simples pour vous aider à écrire du code propre
seo_desc: 'Being a developer isn’t as straightforward as many people think.

  It’s not just about learning a programming language and typing out code to build
  software. There’s a lot more to it. And one of the most confusing (and often frustrating)
  topics for dev...'
---

Être développeur n'est pas aussi simple que beaucoup de gens le pensent.

Ce n'est pas seulement apprendre un langage de programmation et taper du code pour construire un logiciel. Il y a bien plus que cela. Et l'un des sujets les plus confus (et souvent frustrants) pour les développeurs est le code propre.

Alors, qu'est-ce que le code propre ?

Simplement, il s'agit d'écrire du code si clair et bien organisé que ni vous ni personne d'autre ne serez frustré en essayant de le comprendre six mois plus tard.

Pensez au code propre comme l'équivalent en programmation d'un grand design – il est fonctionnel, beau et facile à utiliser.

Et aujourd'hui, je ne vais pas passer beaucoup de temps à expliquer pourquoi le code propre est important – vous le savez probablement déjà. Au lieu de cela, je vais aller droit au but et partager sept astuces puissantes pour vous aider à écrire du code plus propre et meilleur.

## **Table des matières**

* [1. Écrivez du code comme si vous l'expliquiez à un enfant de 5 ans](#heading-1-ecrivez-du-code-comme-si-vous-lexpliquiez-a-un-enfant-de-5-ans)

* [2. Utilisez des outils d'IA (ou un réviseur de code IA)](#heading-2-utilisez-des-outils-dia-ou-un-reviseur-de-code-ia)

* [3. Supprimez les commentaires inutiles](#heading-3-supprimez-les-commentaires-inutiles)

* [4. Suivez le principe DRY](#heading-4-suivez-le-principe-dry)

* [5. Corrigiez la mise en forme de votre code et suivez un style cohérent](#heading-5-corrigiez-la-mise-en-forme-de-votre-code-et-suivez-un-style-coherent)

* [6. Ne laissez pas vos fonctions faire trop de choses](#heading-6-ne-laissez-pas-vos-fonctions-faire-trop-de-choses)

* [7. Organisez correctement vos fichiers et dossiers](#heading-7-organisez-correctement-vos-fichiers-et-dossiers)

* [Conclusion](#heading-conclusion)

## **1. Écrivez du code comme si vous l'expliquiez à un enfant de 5 ans**

Soyons honnêtes – si vous écrivez du code excessivement astucieux que vos coéquipiers ou quelqu'un d'autre ne peut pas facilement lire, cela ne sera utile à personne.

Vous devez écrire du code si simple que n'importe qui, y compris quelqu'un qui ouvre le fichier pour la première fois, peut facilement le parcourir.

Par exemple, si vos noms de variables ressemblent à ceci :

```plaintext
let x = y + z;
```

Ce n'est pas utile. Personne ne saura ce que x, y et z signifient – pas même vous, trois semaines plus tard.

Les variables doivent décrire ce qu'elles contiennent. Pensez à elles comme des commentaires auto-documentés. Voici un meilleur exemple :

```plaintext
let totalPrice = productPrice + shippingCost;
```

Cette simple bonne pratique peut être appliquée même lors de l'écriture de fonctions, de commentaires, etc.

Voici un exemple de code difficile à comprendre :

```plaintext
function calc(itm) {
 let t = 0;
 for (let i = 0; i < itm.length; i++) {
 t += itm[i].p;
 }
 return t;
}
```

Vous voyez, cela ne vous donne pas une idée claire de la fonction autre que la logique.

Au lieu de cela, essayez de l'écrire comme ceci :

```plaintext
function calculateTotalPrice(cartItems) {
    let totalPrice = 0;
    for (let i = 0; i < cartItems.length; i++) {
        totalPrice += cartItems[i].price;
    }
    return totalPrice;
}
```

Maintenant, il est clair, juste en regardant le code, ce qui se passe.

## 2. Utilisez des outils d'IA (ou un réviseur de code IA)

L'IA évolue rapidement et est utilisée dans presque toutes les industries.

Eh bien, en tant que développeur, vous pouvez utiliser l'IA pour vous aider à écrire du code propre et lisible – grâce à des outils d'IA comme [ChatGPT](https://chatgpt.com/), [Claude](https://claude.ai/), et [GitHub Copilot](https://github.com/features/copilot).

Pour commencer, vous pouvez copier et coller votre code dans un LLM et lui demander de le réviser.

Voici un exemple de demande que j'ai faite à ChatGPT :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1738673389541/558c64b6-f92e-4ede-bd00-8fe9c98623c0.png align="center")

Et voici ce que ChatGPT a recommandé :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1738673434670/badadf50-2e1f-46f9-9f3b-c9b189dfaeeb.png align="center")

Il m'a même fourni une version améliorée du code. La voici :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1738673489244/3cf70568-a418-460b-9aa6-768a544965c2.png align="center")

En plus de cela, vous pouvez également utiliser des réviseurs de code alimentés par l'IA comme [CodeRabbit AI](https://www.coderabbit.ai/), qui s'intègre à vos demandes de tirage pour offrir des revues de code automatisées, des visites guidées, et plus encore.

En termes simples, lorsque vous installez CodeRabbit AI, ajoutez-le à votre demande de tirage, puis créez une demande de tirage, CodeRabbit AI vous fournit des résumés, des revues de code, des visites guidées, et plus encore.

Voici un exemple d'un dépôt open-source « [minefield](https://github.com/bitbomdev/minefield/pull/158) » d'un résumé généré par CodeRabbit AI :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1738675580325/ef823a77-6969-4e8a-a141-640468d0169d.png align="center")

Dans les exemples ci-dessus, CodeRabbit AI parcourt simplement le code et fournit un excellent résumé mettant en évidence les nouvelles fonctionnalités, les corrections de bugs et les tests unitaires ajoutés via une demande de tirage.

Si vous souhaitez en savoir plus, voici un [guide de démarrage rapide](https://docs.coderabbit.ai/getting-started/quickstart/) qui fournit plus d'informations sur la façon de commencer et d'utiliser CodeRabbit AI.

Notez que les outils d'IA peuvent être d'une grande aide pour améliorer votre code, mais ils ne doivent jamais remplacer votre propre réflexion.

Lorsque l'IA suggère des modifications, demandez-vous toujours : Cela a-t-il vraiment du sens ?

Après tout, l'IA n'est pas parfaite – elle peut générer du code incorrect. Elle peut également manquer des détails importants qu'un humain peut seul comprendre pleinement.

Au lieu d'accepter aveuglément les suggestions de l'IA, prenez un moment pour comprendre pourquoi elles ont été faites.

Rappelez-vous, le but est d'utiliser l'IA pour accélérer votre flux de travail, attraper des erreurs, et plus encore – tout en gardant le contrôle total sur votre code.

## 3. Supprimez les commentaires inutiles

Écrire de bons commentaires de code peut aider les autres à comprendre pourquoi votre code fait ce qu'il fait.

Mais je vois des développeurs écrire trop de commentaires, même là où il n'y en a pas besoin.

Je crois que, chaque fois que possible, le bon code doit se documenter lui-même.

Voici un exemple de commentaire pas très utile :

```plaintext
// Ajout de 10 au résultat 
total = total + 10;
```

Vous voyez, ici le commentaire n'a pas de sens, et il n'ajoute vraiment rien au code (ou à notre compréhension de celui-ci).

Il est préférable d'écrire des commentaires uniquement s'ils sont importants pour aider un réviseur à comprendre pourquoi vous avez fait quelque chose en particulier ou s'il y a une ambiguïté qui nécessite une explication.

Voici un exemple :

```plaintext
// Ajout de 10 car le client exige une marge de 10 % pour les calculs 
total = total + 10;
```

Maintenant, vous pouvez voir que le commentaire donne une idée claire de pourquoi le programmeur a ajouté 10 au total.

## 4. Suivez le principe DRY

J'ai vu beaucoup de programmeurs répéter la même logique ou ajouter la même fonctionnalité dans différents fichiers.

Eh bien, vous n'avez pas besoin de répéter le même code partout car cela rend le processus beaucoup plus complexe. Gardez votre code DRY (Don't Repeat Yourself).

Au lieu de cela, abstraire cette logique dans une seule fonction réutilisable.

Par exemple, au lieu d'écrire la même logique dans différents fichiers :

```plaintext
if (user.age > 18 && user.age < 65) { 
 // Faire quelque chose 
}

if (user.age > 18 && user.age < 65) { 
 // Faire autre chose 
}
```

Vous pouvez créer une fonction réutilisable afin de pouvoir utiliser la logique partout, comme montré ci-dessous :

```plaintext
function isWorkingAge(age) { 
 return age > 18 && age < 65; 
}

if (isWorkingAge(user.age)) { 
 // Faire quelque chose 
}
```

En bref – écrivez une fois, et utilisez partout.

## 5. Corrigiez la mise en forme de votre code et suivez un style cohérent

C'est une autre astuce simple, mais beaucoup de développeurs n'y pensent même pas.

Tout d'abord, vous devez formater votre code avec une indentation appropriée.

Vous pouvez simplement installer une extension VS Code/linters comme [Prettier](https://prettier.io/), [ESLint](https://eslint.org/), ou [Flake8](https://pypi.org/project/flake8/), selon le langage de programmation que vous utilisez. Configurez quelques paramètres, et vous êtes prêt à partir.

Ces linters peuvent vous aider à écrire un meilleur code en trouvant des erreurs, en vous aidant à suivre les règles de codage, et en gardant votre code cohérent. Ils peuvent également attraper des erreurs, rendre votre code plus facile à lire, et économiser du temps sur la correction de bugs et les revues.

Mais corriger votre mise en forme ne signifie pas seulement que c'est du code propre – c'est bien plus que cela.

Au-delà de la mise en forme, vous devez vous en tenir à un guide de style cohérent pour des choses comme les noms de fonctions ou les noms de variables.

Par exemple, voici du code qui a un style incohérent :

```plaintext
let total_price;  
let UserData;  
function getuser() {}
```

Mais certains d'entre vous peuvent demander, pourquoi le code est-il incohérent ?

Eh bien, il utilise plusieurs conventions de nommage différentes – comme `total_price` utilise snake_case, `UserData` utilise PascalCase, et `getuser()` est en minuscules au lieu de camelCase.

Cela rend votre code plus difficile à lire et plus confus. Au lieu de cela, vous pouvez suivre un style cohérent. Voici comment :

```plaintext
let userData; 
let totalPrice; 
function getUser() {}
```

Et juste pour vous le dire, JavaScript suit généralement camelCase pour les variables et les fonctions, donc des noms comme `getUser(), userData, et totalPrice` seraient plus cohérents.

Peu importe que vous travailliez en équipe ou seul, vous en tenir à un style est une bonne idée. Cela rend le code propre, et le réviseur peut facilement le parcourir.

## 6. Ne laissez pas vos fonctions faire trop de choses

En tant que programmeur, je sais que parfois vous devez écrire une logique complexe à l'intérieur d'une fonction.

Mais le plus souvent, les programmeurs incluent trop de logique dans une seule fonction, ce qui la fait faire plus d'une chose à la fois. Ces fonctions deviennent trop complexes, ce qui les rend difficiles à lire ou à comprendre.

Il est préférable de créer plusieurs fonctions plus petites, chaque fonction gérant une seule responsabilité.

Voici un exemple de fonction légèrement trop complexe :

```plaintext
function calculateCart(items) {
 let total = 0;
 for (let i = 0; i < items.length; i++) {
 total += items[i].price * items[i].quantity;
 }
 return total > 100 ? total * 0.9 : total;
}
```

Vous voyez, cette seule fonction fait trop de choses – elle applique des remises si applicable, et calcule le prix total en fonction de la quantité, ce qui la rend difficile à réutiliser pour des cas d'utilisation spécifiques.

Une meilleure façon est de la diviser en trois fonctions :

* Une pour appliquer la remise (si applicable).

* Une pour calculer le prix total en fonction de la quantité.

* Une pour obtenir le total et appliquer la remise si nécessaire.

Cela rend le code plus propre et plus facile à gérer. Voici une version améliorée :

```plaintext
function calculateCart(items) {
 const total = getCartTotal(items);
 return applyDiscount(total);
}

function getCartTotal(items) {
 return items.reduce((sum, item) => sum + item.price * item.quantity, 0);
}

function applyDiscount(total) {
 return total > 100 ? total * 0.9 : total;
}
```

Vous voyez, au lieu d'écrire tout en un long bloc, la logique est divisée en fonctions plus petites et plus claires.

Et c'est ce qui la rend plus facile à comprendre pour vous (et tout le monde).

## 7. Organisez correctement vos fichiers et dossiers

Maintenant vient la partie la plus importante.

Lorsque vous travaillez sur un grand projet, il n'a pas de sens de mettre tout votre code dans un seul dossier avec un tas de fichiers aléatoires. Cela devient un cauchemar pour quiconque essaie de réviser le code ou de trouver un fichier spécifique.

Réfléchissez-y – parcourir 50 fichiers juste pour corriger un bug. Personne ne veut cela.

Au lieu de cela, essayez d'organiser votre projet en plusieurs dossiers basés sur des pages ou des fonctionnalités.

Et ne vous arrêtez pas là – divisez les grands fichiers en modules plus petits et spécifiques basés sur la fonctionnalité. De cette façon, tout est bien rangé, facile à trouver, et a du sens au premier coup d'œil.

Voici un mauvais exemple de structure de projet :

```plaintext
project-folder/  
├── index.html  
├── app.js  
├── helpers.js  
├── data.js  
├── user.js  
├── product.js
```

C'est désordonné, n'est-ce pas ? Maintenant, voici comment vous pouvez l'améliorer :

```plaintext
project-folder/  
├── pages/  
│   ├── home/  
│   │   ├── HomePage.js  
│   │   ├── HomePage.css  
│   │   └── HomePage.test.js  
│   ├── user/  
│   │   ├── UserPage.js  
│   │   ├── UserPage.css  
│   │   └── UserPage.test.js  
│   └── product/  
│       ├── ProductPage.js  
│       ├── ProductPage.css  
│       └── ProductPage.test.js  
├── components/  
│   ├── Header.js  
│   ├── Footer.js  
│   └── Button.js  
├── utils/  
│   └── api.js  
└── index.js
```

Vous voyez comme c'est simple ?

Vous avez des dossiers séparés pour les pages, les composants et les utilitaires. À l'intérieur de chaque dossier, les fichiers sont organisés par objectif et ont des noms clairs.

Par exemple, si vous avez besoin de quelque chose pour la page produit, vous saurez exactement où le trouver.

## Conclusion

Dans cet article, vous avez appris les bases nécessaires pour commencer à écrire du code propre, efficace et maintenable.

Nous avons discuté de la façon d'écrire du code propre, d'utiliser des outils d'IA, d'appliquer des techniques de mise en forme de code appropriées, de structurer des fonctions efficacement, et de suivre d'autres bonnes pratiques.

Si vous appliquez ces conseils de manière cohérente, vous améliorerez considérablement vos compétences en codage et écriverez du code plus propre.

J'espère que vous avez aimé cela.

Vous pouvez me contacter sur [Substack](https://substack.com/@nitinfab), et [Twitter](https://x.com/Nitinfab).

De plus, si vous êtes intéressé à en apprendre davantage sur l'IA, vous pouvez vous abonner à ma newsletter, [AI Made Simple](https://aimadesimple0.substack.com/), où je plonge plus profondément dans les stratégies pratiques d'IA pour les gens du quotidien.