---
title: Apprendre JavaScript pour la manipulation du DOM en espagnol – Cours pour débutants
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2023-06-19T15:12:59.000Z'
originalURL: https://freecodecamp.org/news/learn-javascript-for-dom-manipulation-in-spanish-course-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/course-image.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Apprendre JavaScript pour la manipulation du DOM en espagnol – Cours pour
  débutants
seo_desc: 'Hi! If you speak Spanish and you want to learn JavaScript for DOM manipulation,
  you are in the right place.

  In this article, you will find a brief introduction to JavaScript for DOM manipulation.
  You will learn why this is a very powerful tool for de...'
---

Salut ! Si vous parlez espagnol et que vous souhaitez apprendre JavaScript pour la manipulation du DOM, vous êtes au bon endroit.

Dans cet article, vous trouverez une brève introduction à JavaScript pour la manipulation du DOM. Vous apprendrez pourquoi cet outil est très puissant pour développer des applications web interactives et pourquoi vous devriez l'apprendre si votre objectif est de devenir développeur front-end.

Ensuite, vous trouverez un cours de 5,5 heures sur JavaScript pour la manipulation du DOM sur la chaîne YouTube espagnole de freeCodeCamp, où vous pourrez apprendre les bases en espagnol et construire des projets étape par étape.

Si vous avez des amis hispanophones, vous êtes invité à partager avec eux la **[version espagnole de cet article](https://www.freecodecamp.org/espanol/news/aprende-javascript-para-manipulacion-del-dom-curso-con-proyectos/)**. 

Commençons ! ✨

## ⏺️ **Qu'est-ce que le DOM ?**

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-03-at-2.48.55-PM.png)
_Le DOM représente la structure d'un fichier HTML._

**DOM** est un acronyme qui signifie Document Object Model. Il s'agit d'une interface qui permet aux programmes informatiques d'accéder et de mettre à jour le contenu, la structure et le style d'un document, tel qu'un fichier HTML.

Le DOM permet aux développeurs web d'interagir avec les éléments et les composants de leurs sites web en utilisant des langages de programmation comme JavaScript. 

### Le DOM ressemble à un arbre

Le DOM fonctionne en créant une représentation de tous les éléments d'une page web. Cette représentation ressemble à un arbre inversé avec des nœuds et des connexions qui représentent leur hiérarchie dans le document.

Le premier objet que nous trouvons dans la hiérarchie de haut en bas est l'objet le plus haut dans le document. Pour HTML, il s'agit de l'élément racine `<html>`, qui contient tous les autres objets de la page web. 

En dessous de cet objet, la structure crée des ramifications qui ressemblent à des branches d'arbre.

Chaque objet a une place particulière dans le DOM. La hiérarchie du DOM suit la hiérarchie des objets dans le document. 

**💡 Astuce :** Un titre, un paragraphe, une image ou un lien sont des exemples d'éléments HTML qui sont représentés comme des objets dans le DOM. 

## ⏺️ **Pourquoi le DOM est-il important ?**

Le DOM est la manière dont le navigateur représente la structure d'un document. Grâce au DOM, nous pouvons accéder aux éléments d'une page web en JavaScript et les manipuler dans notre code.

Le DOM dispose également d'un ensemble de méthodes qui permettent aux développeurs d'accéder, de manipuler et même de supprimer des objets de l'arbre. Nous pouvons même modifier dynamiquement ce que l'utilisateur voit. 

Par exemple, nous pourrions changer le texte d'un élément ou ajouter de nouveaux éléments dynamiquement lorsque nous recevons des informations mises à jour pour l'utilisateur.

C'est pourquoi le DOM est super important pour les développeurs. Il nous permet de créer des pages web interactives qui vont au-delà de la simple affichage de contenu et d'informations. 

Avec le DOM, nous pouvons créer des expériences utilisateur interactives. Nous pouvons créer des animations, changer les informations que l'utilisateur voit et réagir aux événements qui se produisent lorsque l'utilisateur interagit avec la page web. 

En gros, le DOM fait du web l'outil incroyable que nous connaissons et aimons aujourd'hui, il est donc très important pour vous en tant que développeur web. Dans ce cours, vous apprendrez comment il fonctionne et comment l'utiliser.

## ⏺️ **Concepts importants du DOM**

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-03-at-2.48.50-PM.png)
_Le DOM ressemble à un arbre (mais inversé)._

Lorsque nous travaillons avec le DOM, nous trouvons souvent une terminologie utilisée pour décrire la relation entre les nœuds dans la hiérarchie. 

Voici quelques-uns des termes les plus importants que vous devez connaître pour commencer à travailler avec le DOM :

* **Nœud racine :** Le nœud racine est le nœud le plus haut dans l'arbre DOM. C'est le seul nœud dans la hiérarchie qui n'a pas de nœud parent. 
* **Nœud parent :** un nœud qui contient un autre nœud.
* **Nœud enfant :** un nœud qui est directement contenu dans un autre nœud.
* **Nœud descendant :** un nœud qui est à l'intérieur d'un autre nœud (directement ou indirectement).
* **Nœuds frères :** des nœuds qui sont au même niveau dans la hiérarchie DOM et à l'intérieur du même nœud parent. 

Dans cet exemple, nous pourrions représenter le DOM qui sera généré pour ce fichier HTML avec le diagramme que vous pouvez voir ici à droite.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-03-at-12.06.55-PM.png)

**Examinons ce DOM plus en détail :**

* Nous pouvons voir un nœud racine (`**html**`).
* Le nœud racine a deux nœuds enfants (`head` et `body`).
* Le nœud `head` a un nœud enfant (`title`).
* Le nœud `body` a deux nœuds enfants (`h1` et `p`). 
* Les nœuds `h1` et `p` sont frères. Ils sont au même niveau dans la hiérarchie et partagent le même nœud parent.
* Les nœuds en bas n'ont aucun nœud enfant car ils représentent du texte. En plus des éléments HTML, les nœuds peuvent représenter du texte et des commentaires.

💡 **Astuce :** pendant le cours, vous apprendrez la différence entre un nœud et un élément. C'est très important. 

## ⏺️ **Comment sélectionner des éléments du DOM**

Pouvoir sélectionner un élément HTML du DOM est très utile pour avoir accès à la structure du site web. Les éléments sont représentés comme des objets avec des propriétés et des méthodes que nous pouvons utiliser en JavaScript.

Nous avons cinq méthodes pour sélectionner un élément du DOM :

### La méthode `.getElementById()`

Cette méthode est utilisée pour obtenir un élément par son id. Puisque l'id d'un élément doit être unique par page, c'est un moyen parfait de sélectionner un élément spécifique de la hiérarchie DOM, même s'il y a plusieurs éléments similaires ou identiques. 

Voici un exemple :

```javascript
const container = document.getElementById('container');
```

💡 **Astuce :** cela ne retournera qu'un seul élément car les id doivent être uniques.

### La méthode `.getElementsByClassName()`

Cependant, si notre objectif est d'obtenir tous les éléments avec une classe particulière, nous devrions utiliser cette méthode à la place. 

```javascript
const pizzaToppings = document.getElementsByClassName('topping');
```

Cela retourne un objet **HTMLCollection**. Ce type d'objet est un objet de type tableau qui contient une collection d'éléments HTML. 

### La méthode `.getElementsByTagName()`

Parfois, nous pouvons également avoir besoin de sélectionner tous les éléments d'un type particulier, comme tous les **`div`** ou tous les `**p**`. Pour cela, nous avons cette méthode très utile. 

```javascript
const myToppings = document.getElementsByTagName('li');
```

Cette méthode retourne également une **HTMLCollection** car nous pouvons avoir plusieurs éléments avec le même nom de balise.

### La méthode `.querySelect()`

Nous avons également un moyen de sélectionner le premier élément qui correspond à un sélecteur spécifique. Avec cette méthode, nous pouvons écrire des sélecteurs plus complexes similaires à ceux que nous utilisons en CSS pour sélectionner des éléments basés sur des critères plus complexes.

```
const firstNotBrownTopping = document.querySelector('ul li:not(.brown-topping)');
```

💡 **Astuce :** cette méthode ne retourne qu'**un** seul élément – le premier élément qui correspond au sélecteur dans l'ordre où ils apparaissent dans la hiérarchie DOM.

### La méthode `.querySelectAll()`

Et si nous devons sélectionner **tous** les éléments qui correspondent à un sélecteur spécifique, nous devons simplement ajouter All à la fin.

```
const orangeToppings = document.querySelectorAll('.topping.orange-background');
```

✨ **Super.** Ce sont les principales méthodes JavaScript que nous pouvons utiliser pour sélectionner des éléments du DOM. Maintenant, voyons comment vous pouvez ajouter et supprimer des éléments.

## ⏺️ **Comment manipuler le DOM**

Un autre aspect clé de la puissance du DOM est qu'il nous permet de manipuler la hiérarchie initiale du document pour ajouter, supprimer et modifier des éléments. 

Tout d'abord, nous pouvons **créer** un élément. 

Par exemple :

```javascript
const newTopping = document.createElement('li');
```

Et une fois que nous avons le nouvel élément, nous pouvons l'ajouter à notre hiérarchie DOM existante. 

Si nous avons une référence à l'élément parent où nous voulons l'ajouter, `**toppingsList**`, nous pouvons l'ajouter en appelant la méthode `**.append()**`, comme ceci :

```javascript
toppingsList.append(newTopping);
```

Nous pouvons également **supprimer** un élément avec la méthode `**.remove()**` :

```javascript
newTopping.remove();
```

Et nous pouvons **modifier** le contenu d'un élément, comme son HTML interne ou son texte interne :

```
newTopping.innerText = 'Extra Cheese';
```

```
newTopping.innerText = '<div class="new-topping">Extra Cheese</div>';
```

## ⏺️ **Comment attribuer des styles**

Nous pouvons également utiliser la notation par points pour accéder et modifier le style d'un élément. Nous pouvons même ajouter et supprimer les classes des éléments.

```javascript
newTopping.classList.add('topping', 'brown-background');
```

```javascript
newTopping.style.backgroundColor = 'blue';
newTopping.style.color = '#6dff00';
newTopping.style.textTransform = 'uppercase';
```

C'est très puissant, et vous apprendrez comment faire cela pendant le cours lorsque nous construirons les projets. 

💡 **Astuce :** nous pouvons également détecter et gérer les **événements DOM** en JavaScript. Les événements peuvent être déclenchés par des interactions utilisateur, comme le clic sur un bouton de souris, ou par le navigateur, comme lorsque le chargement d'une image est terminé.

## **⏺️ Contenu du cours**

Super. Maintenant que vous en savez plus sur le DOM et pourquoi les développeurs web devraient apprendre à manipuler le DOM en JavaScript, voyons un aperçu de ce que vous apprendrez pendant le cours.

💡 **Astuce :** le cours suppose une connaissance de base de HTML, CSS et JavaScript. Nous travaillerons sur les exemples et les projets étape par étape, mais il est recommandé d'avoir des connaissances préalables sur les bases de JavaScript.

### Introduction au DOM

* Qu'est-ce que le DOM ?
* À quoi sert le DOM ?
* Hiérarchie de base du DOM.
* Concepts importants.
* Relations entre les nœuds.
* Nœud vs. élément dans le DOM.

### Outils de développement Chrome et le DOM

* Introduction aux outils de développement Chrome.
* L'onglet Éléments.
* Comment inspecter une page web.
* Comment utiliser la console.
* Visualisation et compréhension du DOM.
* Manipulation du DOM dans l'aperçu.

**💡 Astuce :** pendant le cours, nous travaillerons avec Visual Studio Code et nous installerons l'extension Live Server pour voir nos changements automatiquement. 

### Sélection d'un élément du DOM

* `**.getElementById()**`
* `**.getElementsByClassName()**`
* `**.getElementsByTagName()**`
* `**.querySelect()**`
* `**.querySelectAll()**`

### Attribution de style avec JavaScript

* La propriété `**style**`.
* Personnalisation des propriétés CSS avec JavaScript.
* Obtenir la valeur d'une propriété CSS.

### Définition du contenu d'un élément

* La propriété `**.innerText**`.
* La propriété `**.innerHTML**`.
* La propriété `**.textContent**`.
* Leurs différences et comment les obtenir.

### Modification et parcours du DOM

* Comment créer un élément.
* Comment ajouter un élément.
* Comment supprimer un élément.
* Parcourir le DOM pour accéder au nœud parent, aux nœuds enfants et aux nœuds frères.

### Événements DOM

* Qu'est-ce qu'un événement ?
* Déclencheurs d'événements
* Types d'événements DOM
* Concepts importants
* Écouteurs d'événements
* Comment gérer les événements

Cela semble génial, n'est-ce pas ? Vous apprendrez tout cela et bien plus pendant le cours.

## ⏺️ **Projets du cours**

Pendant le cours, nous créerons cinq projets interactifs étape par étape. Voyons ce que vous apprendrez dans chacun d'eux en détail.

### Générateur de couleurs hexadécimales aléatoires

Notre premier projet sera un générateur de couleurs hexadécimales aléatoires. Nous générerons une couleur hexadécimale aléatoire et nous l'assignerons comme couleur de fond de l'élément `**body**`. 

💡 **Astuce :** vous pratiquerez comment attacher un écouteur d'événement, comment gérer un événement et comment mettre à jour le texte interne et le style d'un élément.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Random-Hex-Color.png)
_Projet 1 : Générateur de couleurs hexadécimales aléatoires_

### Sélecteur de couleurs RVB avec curseurs

Notre deuxième projet mettra également en vedette des couleurs, mais cette fois la couleur ne sera pas aléatoire. Ce sera une couleur RVB et vous pourrez choisir les valeurs de rouge, vert et bleu pour générer une nouvelle couleur et mettre à jour le fond.

**💡 Astuce :** vous pratiquerez comment gérer un nouveau type d'événement et comment obtenir les valeurs des curseurs chaque fois que l'événement est déclenché.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/RGB-Slider-1.png)
_Projet 2 : Sélecteur de couleurs RVB avec curseurs_

### Générateur de citations aléatoires

Notre troisième projet affichera une citation aléatoire et son auteur. L'utilisateur pourra cliquer sur le bouton bleu pour changer la citation actuelle. 

💡 **Astuce :** vous pratiquerez le travail avec des nombres aléatoires en JavaScript, la mise à jour du texte d'un élément et la gestion des événements DOM.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Citas-Motivacionales.png)
_Projet 3 : Générateur de citations aléatoires_

### Chronomètre

Notre quatrième projet sera un chronomètre. Les utilisateurs pourront démarrer, mettre en pause et arrêter le chronomètre et mettre à jour le temps et les icônes de manière appropriée. 

💡 **Astuce :** vous apprendrez comment mettre à jour le contenu d'un élément en continu à un intervalle de temps fixe, comment réinitialiser l'intervalle de temps et comment mettre à jour le HTML interne d'un élément dans le DOM. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Stopwatch.png)
_Projet 4 : Chronomètre_

### Application de liste de tâches

Enfin, notre cinquième projet sera une application de liste de tâches. L'utilisateur pourra écrire une tâche dans le champ de saisie de texte et cliquer sur le bouton ou appuyer sur Entrée au clavier pour ajouter la nouvelle tâche. Les tâches auront le texte, un bouton pour les marquer comme complètes et un bouton pour les supprimer de la liste. Chaque action mettra à jour son style.

**💡 Astuce :** vous apprendrez comment gérer les événements du clavier et vous pratiquerez comment créer un élément, attribuer et supprimer des classes, et supprimer des éléments du DOM.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Todo-list-app.png)
_Projet 5 : Application de liste de tâches_

💡 **Astuce :** pendant les projets, nous travaillerons également avec les icônes Bootstrap, Flexbox et Google Fonts. 

## 📌 Cours JavaScript pour la manipulation du DOM sur YouTube

Super. Maintenant que vous en savez plus sur JavaScript pour la manipulation du DOM et ce que vous apprendrez pendant le cours, vous pouvez commencer à suivre le cours :

%[https://www.youtube.com/watch?v=koiPxFFiqJ4]

✍️ Cours créé par **Estefania Cassingena Navone** (Twitter : [@EstefaniaCassN](https://twitter.com/EstefaniaCassN), YouTube : [Coding with Estefania](https://youtube.com/codingwithestefania)).

J'espère vraiment que vous aimerez le cours et que vous le trouverez utile pour plonger plus profondément dans le monde du développement web front-end.

Vous êtes également invité à continuer à apprendre avec nos autres cours en **espagnol** :

%[https://www.youtube.com/watch?v=XqFR2lqBYPs]

%[https://www.youtube.com/watch?v=ivdTnPl1ND0]

%[https://www.youtube.com/watch?v=DLikpfc64cA]

%[https://www.youtube.com/watch?v=6Jfk8ic3KVk]