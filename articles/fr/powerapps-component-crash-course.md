---
title: Comment étendre Power Apps avec des composants réutilisables
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2025-05-16T17:45:19.456Z'
originalURL: https://freecodecamp.org/news/powerapps-component-crash-course
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1747410099474/8471a651-503f-4ced-a172-7dadac930039.png
tags:
- name: Canvas PowerApps
  slug: canvas-powerapps
- name: Low Code
  slug: low-code
- name: components
  slug: components
seo_title: Comment étendre Power Apps avec des composants réutilisables
seo_desc: If you have experience in traditional software development, low-code tools
  may feel a bit sparse at first. But to many people’s surprise, traditional techniques
  often translate quite well to low-code development. Not always one-for-one – but
  usually ...
---

Si vous avez de l'expérience dans le développement logiciel traditionnel, les outils low-code peuvent sembler un peu limités au premier abord. Mais à la surprise de beaucoup, les techniques traditionnelles se traduisent souvent assez bien dans le développement low-code. Pas toujours de manière identique, mais généralement assez proche.

L'une des tâches les plus fondamentales lors de la construction d'une application est de la décomposer en ses parties principales, ou composants. Les sites web sont construits à partir de blocs plus petits. À quel point sont-ils petits ? Cela dépend de vous, le développeur.

Dans l'exemple ci-dessous, nous pouvons repérer certains éléments évidents : un en-tête, une boîte de recherche, peut-être une barre latérale pour la navigation et une zone de contenu principal. Les applications émergent de nombreuses parties plus petites qui s'assemblent.

![Image des composants d'un site web](https://www.scriptedbytes.com/content/images/2025/05/components.png align="left")

Les composants nous permettent d'isoler les responsabilités et de gérer la complexité pour des parties spécifiques d'une application. Dans le développement traditionnel et low-code, ils jouent un rôle vital dans la création de produits maintenables, réutilisables et testables.

Dans cet article, vous apprendrez ce qu'est un composant. Ensuite, nous construirons un composant de champ de texte personnalisé dans une application Canvas.

### Prérequis

Ce tutoriel suppose une compréhension de base de Microsoft Power Apps. Bien que ce ne soit pas nécessaire pour comprendre l'article, pour suivre activement, vous aurez besoin d'un accès à un environnement Power Platform avec le rôle de sécurité App Maker.

### Table des matières

* [Le concept de composant](#heading-le-concept-de-composant)
  
* [Comment construire votre propre composant](#heading-comment-construire-votre-propre-composant)
  
* [Conclusion](#heading-conclusion)
  

## Le concept de composant

L'idée des composants n'est pas nouvelle et n'est pas exclusive au logiciel.

Pensons à une voiture un instant. Une voiture est composée de nombreuses parties plus petites : des roues, un moteur, des sièges, un volant, etc. Mais c'est le concept de la voiture, et spécifiquement sa capacité à nous transporter, qui apporte de la valeur. Ce concept émerge de la manière dont les parties individuelles fonctionnent ensemble.

Imaginez maintenant que vous avez un pneu crevé. Pas une bonne journée. Mais grâce à la manière dont les voitures sont conçues, vous n'avez pas besoin d'une nouvelle voiture entière, peut-être même pas d'un nouveau pneu. Vous réparez le problème et vous êtes de nouveau sur la route en quelques heures. Décomposer les choses en parties plus petites aide à rendre l'ensemble du système plus résilient. Appliquer ce même principe au développement d'applications est une approche intelligente et pérenne.

### Deux grands types de composants

Dans une application, les composants peuvent varier en complexité et en responsabilité. Certains sont simples, comme une étiquette de texte. D'autres sont plus complexes, comme une boîte de dialogue contextuelle. Quelle que soit leur complexité (encore une fois, votre choix de conception), les composants tombent généralement dans l'une des deux catégories :

* **Composants de présentation ("Dumb")**
  
* **Composants conteneurs ("Smart")**
  

La différence réside dans le but. Un composant conteneur peut interagir avec des sources externes et mutent généralement l'état. Un composant de présentation, en revanche, est généralement responsable uniquement de l'apparence des choses et de la communication légère avec l'application.

Les composants conteneurs sont souvent plus complexes et plus difficiles à tester. Les composants de présentation sont généralement plus simples et plus prévisibles.

Cela ne signifie pas que vous devez éviter les composants conteneurs. Ce n'est pas réaliste. À un moment donné, votre application devra communiquer avec le monde extérieur.

### À part : Fonctions pures

Le concept de **fonctions pures** est utile ici.

Une fonction est considérée comme *pure* si elle retourne toujours la même sortie pour la même entrée et n'interagit pas avec un état externe.

```JavaScript
// Exemple 1 (pur)
function add(x, y) {
  return x + y;
}

console.log(add(2, 3)); // Toujours 5

// Exemple 2 (non pur)
function subtract(x) {
  const y = Math.floor(Math.random() * 100) + 1; // Nombre aléatoire entre 1 - 100
  console.log(y);
  return x + y;
}

console.log(subtract(5)); // Imprévisible
```

Tout comme `add()` est pure et `subtract()` ne l'est pas, un composant de présentation se comporte comme une fonction pure : même entrée, même sortie. La sortie peut être l'apparence de l'interface utilisateur ou un événement avec des données associées.

### Plus sur les entrées et les sorties

Si vous avez déjà construit une application Canvas, vous avez déjà utilisé des composants, même si vous ne vous en êtes pas rendu compte. La plupart des contrôles dans une application Canvas sont des composants de présentation.

Prenons le contrôle **Label**. Il reçoit une entrée (`Text`) et rend une sortie (le texte à l'écran).

![Image du label de l'application Canvas](https://www.scriptedbytes.com/content/images/2025/05/Snag_37f5d6fa.png align="left")

Les événements sont un autre type de sortie. Par exemple, le contrôle **Button** émet un événement lorsqu'il est cliqué, géré via la propriété `OnSelect`. Cette propriété permet à l'application de répondre au clic et d'exécuter une logique.

![Image du bouton de l'application Canvas](https://www.scriptedbytes.com/content/images/2025/05/Snag_37fa1150.png align="left")

📢 Lorsqu'un composant envoie un message à l'application, on dit que le composant a *émis un événement*.

Examinons maintenant le contrôle **Text Input**.

Comme les autres, il a des entrées (comme `Placeholder`). Mais il émet également un événement `Change` via `OnChange`. Mieux encore, il passe des données à l'application via sa propriété `Value`. À mesure que l'utilisateur tape, la valeur est mise à jour. Cette valeur est la manière dont nous accédons à ce qu'il a tapé.

![Image de l'entrée de texte de l'application Canvas](https://www.scriptedbytes.com/content/images/2025/05/Snag_38070a2d.png align="left")

## Comment construire votre propre composant

Construisons un composant d'entrée personnalisé et simple. Il comprendra :

* Une étiquette au-dessus de l'entrée
  
* Une validation "requis" optionnelle
  
* Une détection de changement et une sortie de données
  

Voici à quoi il ressemblera :

![Image du champ de texte personnalisé à construire](https://www.scriptedbytes.com/content/images/2025/05/image.png align="center")

### Partie 1 : Créer le composant

1. Accédez à la section **Composants** de votre application Canvas.
  
2. Ajoutez un nouveau composant et nommez-le `cmp_baseInput`.
  
3. Redimensionnez-le à 340 (l) x 100 (h).
  
![Image de la création d'un composant](https://www.scriptedbytes.com/content/images/2025/05/Snag_3819d94d.png align="left")

### Partie 2 : Ajouter des contrôles

1. Ajoutez un contrôle **Text Input**, centré.
  
2. Ajoutez deux **Labels**, l'un au-dessus, l'autre en dessous de l'entrée.
  
3. Renommez-les :
  
    * `lbl_label`
      
    * `lbl_hint`
      
    * `txt_textField`
      
![Image des contrôles appropriés ajoutés au composant](https://www.scriptedbytes.com/content/images/2025/05/Snag_381d4ce8.png align="left")

### Partie 3 : Ajouter des propriétés personnalisées

Ajoutez quatre propriétés au composant. Nous nous intéressons principalement au type de propriété, à la définition de la propriété et aux propriétés de type de données.

* `IsRequired` (Data, Input, Boolean)
  
* `Label` (Data, Input, Text)
  
* `Value` (Data, Output, Text)
  
* `OnChange` (Event)
  
![Image des propriétés personnalisées ajoutées au composant](https://www.scriptedbytes.com/content/images/2025/05/Snag_38262956.png align="left")

### Partie 4 : Connecter les propriétés

Définissez les propriétés du contrôle comme suit.

```plaintext
lbl_label.Text = cmp_baseInput.Label

lbl_hint.Text = "Ce champ est requis."
lbl_hint.Visible = cmp_baseInput.IsRequired And Len(txt_textField.Value) < 1

txt_textField.OnChange = cmp_baseInput.OnChange()

cmp_baseInput.Value = txt_textField.Value
cmp_baseInput.Label = "Libellé de l'espace réservé"
```

### Partie 5 : Le styliser

```plaintext
lbl_label.Size = 12
lbl_label.Height = 24
lbl_label.FontColor = RGBA(122, 138, 143, 1)

lbl_hint.Size = 10
lbl_hint.Height = 24
lbl_hint.FontColor = RGBA(215, 58, 60, 1)
lbl_hint.FontWeight = 'TextCanvas.Weight'.Semibold
```

### Partie 6 : L'ajouter à l'application

1. Retournez à l'écran de l'application.
  
2. Insérez le composant et nommez-le `cmp_userName`.
  
3. Ajoutez une étiquette à proximité et définissez son texte sur :
  `"Le nom d'utilisateur est : " & cmp_userName.Value`
  
![Image de l'insertion du composant dans l'application](https://www.scriptedbytes.com/content/images/2025/05/Snag_3835242d.png align="left")

![Image du composant inséré dans l'application](https://www.scriptedbytes.com/content/images/2025/05/Snag_383a4039.png align="left")

### Partie 7 : Le tester

* Tapez dans le composant et cliquez à l'extérieur  l'étiquette près du composant se met à jour et l'indice disparaît.
  
* Effacez le texte  l'indice réapparaît
  
* Définissez `IsRequired` sur false  l'indice disparaît
  
* Définissez `OnChange` sur `Notify("Un changement s'est produit !")` et tapez dans l'entrée  un message toast apparaît avec votre notification.
  

## Conclusion

Vous venez de créer un composant de présentation fonctionnel. Il gère les étiquettes, la validation, la sortie des valeurs et même les événements, le tout dans un seul package.

C'est la véritable puissance des composants : l'abstraction, la clarté et la réutilisabilité. Que vous soyez dans un environnement traditionnel ou low-code, penser en composants vous aide à décomposer la complexité en parties gérables.

À mesure que vos applications grandissent, cette mentalité portera ses fruits. Vous passerez moins de temps à réécrire la logique et plus de temps à construire de la valeur, une partie bien définie à la fois.

*Avez-vous aimé cet article ?* J'écris régulièrement sur le low-code, les modèles de développement et les sujets technologiques pratiques sur [scriptedbytes.com](https://www.scriptedbytes.com)

*Restez curieux et continuez à construire.*