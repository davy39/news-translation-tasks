---
title: Comment créer un outil de sélection de couleur en utilisant HTML, CSS et JavaScript
subtitle: ''
author: Fanny Nyayic
co_authors: []
series: null
date: '2024-08-15T11:01:37.761Z'
originalURL: https://freecodecamp.org/news/create-color-picker-using-html-css-and-javascript
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1723709466316/80aae148-6211-4070-ba33-eb4290408912.png
tags:
- name: HTML5
  slug: html5
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: beginner
  slug: beginner
seo_title: Comment créer un outil de sélection de couleur en utilisant HTML, CSS et
  JavaScript
seo_desc: 'Have you ever wanted to create your own interactive tools using just HTML,
  CSS, and JavaScript? In this article, we''ll create a fun and straightforward project:
  a color picker tool.

  This handy little tool will let users select any color they like and...'
---

Avez-vous déjà voulu créer vos propres outils interactifs en utilisant uniquement HTML, CSS et JavaScript ? Dans cet article, nous allons créer un projet amusant et simple : un outil de sélection de couleur.

Cet outil pratique permettra aux utilisateurs de sélectionner n'importe quelle couleur et de voir instantanément ses valeurs HEX et RGB.

Alors, prenez votre éditeur de code préféré, et commençons !

## Étape 1 : Installer votre projet

1. **Créer un nouveau dossier** : Commencez par créer un nouveau dossier sur votre ordinateur pour ce projet. Vous pouvez le nommer **color-picker-tool**.
    
2. **Créer des fichiers** : À l'intérieur du dossier, créez trois fichiers :
    
    * **index.html**
        
    * **styles.css**
        
    * **script.js**
        
    
    ![](https://cdn.hashnode.com/res/hashnode/image/upload/v1723707100431/55c7cc93-7b0d-4d67-abb1-8104dbeda18d.png align="center")
    

## Étape 2 : Construire la structure HTML

1. Ouvrez le fichier **index.html** dans votre éditeur de code.
    
2. **Ajouter la structure HTML de base** : Ajoutez le code suivant dans **index.html** : ou appuyez sur `SHIFT+!` puis sur `Enter` pour définir la structure Emmet, puis changez le titre du document en `"Color Picker Tool"`.
    
3. Liez également vos fichiers **styles.css** et **script.js**.
    
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Color Picker Tool</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
    
        <script src="script.js"></script>
    </body>
    </html>
    ```
    

### Explication :

* `<!DOCTYPE html>` : Cela indique au navigateur que le document est un document HTML5.
    
* `<html lang="en">` : L'élément racine du document HTML, avec la langue définie sur l'anglais.
    
* `<head>` : Contient des méta-informations sur le document, comme le jeu de caractères et le titre.
    
* `<title>` : Définit le titre de la page web, qui apparaît dans l'onglet du navigateur.
    
* `<link rel="stylesheet" href="styles.css">` : Lie le fichier CSS qui style la page.
    
* `<body>` : Contient le contenu de la page web.
    
* `<script src="script.js"></script>` : Lie le fichier JavaScript qui ajoute de l'interactivité à la page.
    

3. **Ajouter le contenu du body :**
    
    ```xml
    <div class="color-picker">
      <input type="color" id="colorInput" value="#ff0000">
        <div class="color-info">
           <p>HEX: <span id="hexValue">#ff0000</span></p>
           <p>RGB: <span id="rgbValue">rgb(255, 0, 0)</span></p>
        </div>
    </div>
    ```
    
    ### Explication :
    

* `<div class="color-picker">` : Un conteneur pour les éléments du sélecteur de couleur.
    
* `<input type="color" id="colorInput" value="#ff0000">` : Un élément d'entrée qui permet aux utilisateurs de choisir une couleur. L'attribut `value` définit la couleur par défaut.
    
* `<div class="color-info">` : Un conteneur pour afficher les informations sur la couleur.
    
* `<p>HEX: <span id="hexValue">#ff0000</span></p>` : Affiche la valeur HEX de la couleur sélectionnée.
    
* `<p>RGB: <span id="rgbValue">rgb(255, 0, 0)</span></p>` : Affiche la valeur RGB de la couleur sélectionnée.
    

Voici ce que nous aurons :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1723708023384/8a3b4b0f-39a3-4cc6-9550-64b593cd5662.png align="center")

## Étape 3 : Styliser avec CSS

1. Ouvrez le fichier **styles.css** dans votre éditeur de code.
    
2. **Ajouter des styles CSS** : Copiez et collez le code suivant dans **styles.css** :
    
    ```css
    body {
        font-family: Arial, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        background-color: #f0f0f0;
    }
    .color-picker {
        background-color: #fff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .color-info {
        margin-top: 20px;
    }
    p {
        margin: 5px 0;
        font-size: 16px;
    }
    ```
    

### Explication :

* `body` : Style le corps de la page. Il centre le contenu à la fois verticalement et horizontalement et définit un fond gris clair.
    
* `font-family: Arial, sans-serif;` : Définit la police pour le texte sur la page.
    
* `display: flex;` : Utilise Flexbox pour la mise en page.
    
* `justify-content: center;` et `align-items: center;` : Centre le contenu.
    
* `height: 100vh;` : Définit la hauteur à 100 % de la hauteur de la fenêtre.
    
* `margin: 0;` : Supprime la marge par défaut.
    
* `background-color: #f0f0f0;` : Définit la couleur de fond de la page.
    
* `.color-picker` : Style le conteneur du sélecteur de couleur avec un fond blanc, un remplissage, des coins arrondis et une ombre pour une apparence de carte.
    
* `.color-info` : Ajoute une marge en haut pour le séparer de l'entrée de couleur.
    
* `p` : Style les paragraphes dans les informations de couleur, définissant la marge et la taille de la police.
    

Voici ce que nous aurons :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1723708068790/0b16e350-d292-4076-b5ee-29016970f762.png align="center")

À ce stade, nous pouvons choisir une couleur, mais les codes de couleur ne seront pas affichés. Pour afficher les codes de couleur, nous devrons ajouter un peu de JavaScript.

## Étape 4 : Ajouter la fonctionnalité JavaScript

1. Ouvrez le fichier `script.js` dans votre éditeur de code.
    
2. **Ajouter le code JavaScript** : Ajoutez le code suivant dans `script.js` :
    
    ```javascript
    document.getElementById('colorInput').addEventListener('input', function() {
        const color = this.value;
        document.getElementById('hexValue').textContent = color;
        document.getElementById('rgbValue').textContent = hexToRgb(color);
    });
    function hexToRgb(hex) {
        const r = parseInt(hex.slice(1, 3), 16);
        const g = parseInt(hex.slice(3, 5), 16);
        const b = parseInt(hex.slice(5, 7), 16);
        return `rgb(${r}, ${g}, ${b})`;
    }
    ```
    
    ### Explication :
    
    * `document.getElementById('colorInput')` : Sélectionne l'élément d'entrée de couleur par son `ID`.
        
    * `.addEventListener('input', function() {...})` : Ajoute un écouteur d'événement qui se déclenche chaque fois que l'utilisateur sélectionne une nouvelle couleur.
        
    * `const color = this.value;` : Obtient la valeur actuelle de l'entrée de couleur, qui est au format HEX.
        
    * `document.getElementById('hexValue').textContent = color;` : Met à jour le contenu texte de l'affichage de la valeur HEX avec la couleur sélectionnée.
        
    * `document.getElementById('rgbValue').textContent = hexToRgb(color);` : Convertit la couleur HEX en RGB et met à jour l'affichage de la valeur RGB.
        
    * `function hexToRgb(hex) {...}` : Une fonction qui convertit une chaîne de couleur HEX en une chaîne RGB.
        
        * `parseInt(hex.slice(1, 3), 16)` : Convertit les deux premiers caractères de la couleur HEX (après le `#`) en un nombre décimal, représentant la composante rouge.
            
        * `parseInt(hex.slice(3, 5), 16)` : Convertit les deux caractères suivants en la composante verte.
            
        * `parseInt(hex.slice(5, 7), 16)` : Convertit les deux derniers caractères en la composante bleue.
            
        * `return` rgb(${r}, ${g}, ${b})`;` : Retourne la couleur RGB sous forme de chaîne.
            

## Étape 5 : Tester votre outil de sélection de couleur

1. **Ouvrir le projet dans un navigateur** : Ouvrez le fichier **index.html** dans un navigateur web pour voir votre outil de sélection de couleur.
    
2. **Interagir avec l'outil** : Utilisez l'entrée de couleur pour sélectionner différentes couleurs. Les valeurs HEX et RGB doivent se mettre à jour automatiquement lorsque vous sélectionnez de nouvelles couleurs.
    

### Réflexions finales

Félicitations ! Vous avez réussi à créer un outil de sélection de couleur en utilisant HTML, CSS et JavaScript.

Ce projet est un excellent moyen de pratiquer le travail avec les entrées utilisateur et la manipulation du DOM. Vous pouvez améliorer cet outil en ajoutant des fonctionnalités comme la copie des valeurs de couleur dans le presse-papiers ou l'enregistrement des couleurs favorites.

Amusez-vous à expérimenter et à apprendre !