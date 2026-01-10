---
title: 'Comment utiliser l''API Selection de JavaScript : créer un éditeur de texte
  enrichi et détecter des éléments en temps réel'
subtitle: ''
author: Asfak Ahmed
co_authors: []
series: null
date: '2024-09-16T16:19:02.904Z'
originalURL: https://freecodecamp.org/news/use-the-javascript-selection-api-to-build-a-rich-text-editor
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1726225376443/ae5d57c8-e79e-4dc4-b218-c3a5e34f8293.png
tags:
- name: selection api
  slug: selection-api
- name: element detection
  slug: element-detection
- name: JavaScript
  slug: javascript
- name: '#richtext'
  slug: richtext
- name: ' DOM In JavaScript'
  slug: dom-in-javascript
- name: JavaScript event handling
  slug: javascript-event-handling
seo_title: 'Comment utiliser l''API Selection de JavaScript : créer un éditeur de
  texte enrichi et détecter des éléments en temps réel'
seo_desc: When you interact with web pages, a common task you’ll perform often is
  selecting text. Whether it's highlighting a section of a paragraph to copy, marking
  important parts of a document, or working with interactive features like note-taking
  or text e...
---

Lorsque vous interagissez avec des pages Web, une tâche courante que vous effectuez souvent est la sélection de texte. Qu'il s'agisse de mettre en évidence une section d'un paragraphe pour la copier, de marquer des parties importantes d'un document ou d'utiliser des fonctionnalités interactives comme la prise de notes ou l'édition de texte, les sélections de texte font partie de notre expérience de navigation quotidienne.

L'**API Selection** de JavaScript est ce qui permet d'interagir par programmation avec ces sélections de texte.

Dans ce tutoriel, nous allons plonger au cœur de l'API Selection, explorer ses capacités et démontrer comment vous pouvez l'utiliser pour créer des applications Web interactives basées sur la sélection.

### Dans cet article, nous aborderons :

* [Explorez l'API Selection de JavaScript, un outil puissant pour interagir avec et manipuler le texte sélectionné par l'utilisateur sur une page Web.](#heading-quest-ce-que-lapi-selection)
    
* [Présentation de document.execCommand(), une méthode facile à utiliser pour ajouter du formatage au texte sélectionné, notamment le gras, l'italique et le souligné.](#heading-la-fonction-documentexeccommand)
    
* [Démonstration de la construction d'un éditeur de texte enrichi simple avec des fonctionnalités de formatage de base en utilisant à la fois l'API Selection et execCommand().](#heading-exemple-dutilisation-comment-creer-un-editeur-de-texte-enrichi-avec-lapi-selection-javascript)
    
* [Détecter les éléments cliqués et leurs positions en temps réel.](#heading-comment-obtenir-lelement-clique-et-sa-position-en-temps-reel)
    

## Qu'est-ce que l'API Selection ?

L'**API Selection** est une API Web fournie par les navigateurs modernes qui permet aux développeurs de travailler avec les sélections de texte des utilisateurs sur une page Web. Elle vous permet de :

1. Obtenir des détails sur le texte actuellement sélectionné.
    
2. Modifier ou manipuler les sélections par programmation.
    
3. Détecter quand les utilisateurs effectuent une sélection.
    
4. Stocker, remplacer ou supprimer des sélections de texte.
    

Cette API est couramment utilisée pour les éditeurs de texte enrichi, les fonctionnalités de copier/coller, les infobulles personnalisées, la mise en évidence, les annotations, et bien plus encore.

## Que pouvez-vous faire avec l'API Selection ?

L'API Selection vous donne le pouvoir d'interagir avec le texte sélectionné par l'utilisateur de diverses manières. Voici quelques capacités clés :

1. **Obtenir le texte actuellement sélectionné** : Extraire le texte mis en évidence que l'utilisateur sélectionne dans le document.
    
2. **Modifier la sélection** : Définir ou modifier une sélection par programmation, soit en définissant de nouveaux points de début et de fin, soit en la réduisant entièrement.
    
3. **Supprimer la sélection** : Effacer une sélection une fois que vous avez fini de l'utiliser.
    
4. **Extraire des informations de position** : Savoir où la sélection commence et se termine, à la fois dans le document et sur l'écran (utile pour les infobulles personnalisées ou les annotations).
    
5. **Appliquer un style personnalisé** : Vous pouvez styliser le texte sélectionné, ajouter des mises en évidence ou déclencher des événements lorsqu'un utilisateur effectue une sélection.
    

## Composants clés de l'API Selection

Pour utiliser efficacement l'API Selection, il est important de comprendre certains de ses concepts fondamentaux. Voici les objets et méthodes clés :

### **1\.** L'objet `Selection` 

L'objet `Selection` représente la sélection actuelle de texte sur une page Web. Il est accessible via la méthode `window.getSelection()` et constitue l'objet principal avec lequel vous interagirez.

```typescript
const selection = window.getSelection();
console.log(selection);
```

L'objet `Selection` fournit de multiples propriétés et méthodes pour récupérer, modifier et manipuler le texte sélectionné par l'utilisateur.

### **2\.** L'objet `Range` 

L'objet `Range` représente un fragment d'un document. Il contient des informations sur les points de début et de fin d'une sélection et vous permet de manipuler des portions du document.

Par exemple, vous pouvez créer une plage (range) pour mettre en évidence ou manipuler des nœuds de texte spécifiques ou récupérer le contenu textuel à l'intérieur d'une certaine plage.

```typescript
const selection = window.getSelection();
const range = selection.getRangeAt(0); // Récupérer la première plage de la sélection
console.log(range);
```

## Méthodes et propriétés clés de l'API Selection

Voici une décomposition des méthodes et propriétés les plus couramment utilisées de l'**API Selection** et de l'**API Range** :

### **Méthodes de l'API Selection :**

#### 1\. `window.getSelection()` :

La méthode `window.getSelection()` est utilisée pour récupérer la sélection de texte actuelle sur la page Web. Elle renvoie un objet `Selection`, qui représente la plage de texte sélectionnée par l'utilisateur, ou la position actuelle du curseur (si aucun texte n'est sélectionné).

**Détails sur** `window.getSelection()` **:**

L'objet `Selection` contient des détails sur le texte actuellement sélectionné (le cas échéant), y compris les nœuds de début et de fin, les décalages (offsets) et les méthodes pour manipuler la sélection.

Si aucun texte n'est sélectionné, l'objet `Selection` reflétera la position actuelle du curseur sans aucune plage sélectionnée.

**Exemple de code :**

```typescript
const selection = window.getSelection();
console.log(selection);  // Affiche l'objet Selection dans la console
```

**Exemple d'utilisation :**

Vérifier si du texte est sélectionné :

```typescript
const selection = window.getSelection();
if (selection.rangeCount > 0) {
    console.log('Du texte est sélectionné');
} else {
    console.log('Aucun texte sélectionné');
}
```

Ceci vérifie si du texte est sélectionné en vérifiant si `rangeCount` (le nombre de plages de texte) est supérieur à zéro.

#### 2\. `Selection.anchorNode` **et** `Selection.focusNode` **:**

`anchorNode` représente le nœud où l'utilisateur a commencé la sélection. C'est le point de départ de la sélection, bien que visuellement il puisse se trouver à la fin selon la direction du glissement de l'utilisateur.

`focusNode` représente le nœud où l'utilisateur a terminé la sélection. C'est le point final de la sélection, mais encore une fois, cela pourrait visuellement apparaître comme le début de la sélection si l'utilisateur a sélectionné vers l'arrière.

**Détails importants :**

* **Direction de la sélection** : Si la sélection est faite de gauche à droite (glissement vers l'avant), cet `anchorNode` sera la partie antérieure de la sélection. Si la sélection est faite de droite à gauche (glissement vers l'arrière), l'`anchorNode` sera à la partie postérieure de la sélection, mais le focus apparaîtra en premier.
    
* **Types de nœuds** : `anchorNode` et `focusNode` renvoient tous deux des nœuds DOM. Cela signifie qu'il peut s'agir de nœuds de texte, de nœuds d'élément ou de tout autre type de nœud dans le document.
    
* **Offsets** : En plus de ces propriétés, `Selection.anchorOffset` et `Selection.focusOffset` vous donnent le décalage exact des caractères à l'intérieur des nœuds où la sélection commence et se termine.
    

#### 3\. `Selection.toString()` :

Pour utiliser la méthode `Selection.toString()`, il vous suffit de l'appeler sur la sélection actuelle. Cette méthode renvoie la valeur de chaîne du texte actuellement sélectionné dans le document.

```typescript
const selectedText = selection.toString();
console.log(selectedText);  // Sortie : Le texte sélectionné
```

**Comment ça marche :**

1. `window.getSelection()` : Récupère l'objet `Selection` actuel représentant le texte sélectionné par l'utilisateur.
    
2. `.toString()` : Convertit la plage sélectionnée en une chaîne de texte brut.
    
3. Le résultat est ensuite affiché dans la console.
    

#### 4\. `Selection.removeAllRanges()` :

La méthode `Selection.removeAllRanges()` est utilisée pour effacer ou supprimer toute sélection de texte actuelle sur une page Web. Lorsqu'elle est appelée, elle désélectionne tout texte que l'utilisateur a pu sélectionner, laissant la sélection vide.

```typescript
selection.removeAllRanges();
```

**Comment ça marche :**

* `window.getSelection()` : Récupère l'objet `Selection` actuel.
    
* `.removeAllRanges()` : Efface la sélection, désélectionnant efficacement tout texte mis en évidence sur la page.
    

#### 5\. `Selection.addRange(range)` :

La méthode `Selection.addRange(range)` est utilisée pour ajouter un objet `Range` spécifique à la sélection actuelle dans le document. Cela vous permet de sélectionner par programmation une plage de texte ou d'éléments.

```typescript
// Créer un objet range
const range = document.createRange();

// Sélectionner un élément spécifique ou une partie du document
const element = document.getElementById('myElement');

// Définir la plage pour qu'elle commence au début de l'élément et se termine à la fin
range.selectNodeContents(element);

// Effacer toute sélection existante et ajouter la nouvelle plage
const selection = window.getSelection();
selection.removeAllRanges();  // Supprimer les sélections existantes
selection.addRange(range);  // Ajouter la nouvelle plage
```

**Comment ça marche :**

1. `document.createRange()` : Crée un nouvel objet `Range`.
    
2. `range.selectNodeContents()` : Définit la plage pour couvrir le contenu d'un élément DOM spécifique (dans ce cas, l'élément avec l'ID `myElement`).
    
3. `selection.removeAllRanges()` : Efface tout texte ou élément précédemment sélectionné.
    
4. `selection.addRange(range)` : Ajoute la `Range` définie à la sélection, en faisant d'elle le texte ou le contenu actuellement sélectionné.
    

**Cas d'utilisation :**

* **Sélectionner du texte par programmation** : Si vous souhaitez mettre en évidence des parties spécifiques du document par programmation, vous pouvez utiliser cette méthode pour les sélectionner.
    
* **Logique de sélection personnalisée** : Dans les applications Web qui nécessitent des sélections spécifiques de texte ou d'éléments, comme les éditeurs ou les outils d'interface utilisateur personnalisés, cela peut être utilisé pour gérer les sélections des utilisateurs.
    

### **Méthodes de l'API Range :**

#### 1\. `range.setStart(node, offset)` :

La méthode `Range.setStart(node, offset)` est utilisée pour définir le point de départ d'un objet `Range`. Vous spécifiez le `node` où la plage doit commencer et l' `offset` (position à l'intérieur du nœud) pour le point de départ.

**Paramètres :**

* `node` : Le nœud DOM où la plage doit commencer. Il peut s'agir d'un nœud d'élément ou d'un nœud de texte.
    
* `offset` : La position à l'intérieur du nœud où la plage commence. Pour les nœuds d'élément, il s'agit de l'index des nœuds enfants. Pour les nœuds de texte, il s'agit de la position du caractère dans le texte.
    

```typescript
// Créer un objet range
const range = document.createRange();

// Sélectionner le nœud de texte où la plage doit commencer
const textNode = document.getElementById('myElement').firstChild;

// Définir le début de la plage au 5ème caractère dans le nœud de texte
range.setStart(textNode, 5);
```

**Explication du code :**

1. `document.createRange()` : Crée un nouvel objet `Range`.
    
2. `textNode` : Cela fait référence au premier enfant de l'élément avec l'ID `myElement`, qui est censé être un nœud de texte.
    
3. `range.setStart(textNode, 5)` : Définit le début de la plage au 5ème caractère dans le nœud de texte.
    

**Notes importantes :**

* Dans les **nœuds de texte**, l'`offset` fait référence à la position d'un caractère dans le texte. Par exemple, `offset = 5` signifie que la plage commence après le 5ème caractère.
    
* Dans les **nœuds d'élément**, l'`offset` fait référence à l'index des nœuds enfants. Par exemple, `offset = 0` commencerait avant le premier élément enfant, tandis que `offset = 1` commencerait après le premier enfant.
    

**Exemple de cas d'utilisation :**

Vous pourriez utiliser `setStart` dans un scénario où vous souhaitez mettre en évidence ou extraire une partie d'un texte, en commençant à un point spécifique :

```typescript
const range = document.createRange();
const textNode = document.getElementById('myText').firstChild;
range.setStart(textNode, 3); // Commencer au 4ème caractère
range.setEnd(textNode, 8);   // Terminer au 9ème caractère

const selection = window.getSelection();
selection.removeAllRanges(); // Effacer les sélections précédentes
selection.addRange(range);   // Mettre en évidence le texte sélectionné
```

Dans cet exemple, il sélectionne le texte commençant du 4ème caractère et se terminant au 9ème caractère, mettant ainsi en évidence cette partie du texte.

#### 2\. `range.cloneContents()` :

La méthode `Range.cloneContents()` est utilisée pour créer une copie du contenu à l'intérieur de la plage spécifiée. Elle renvoie un `DocumentFragment` contenant les nœuds et le contenu de la plage, mais ne modifie pas le document original.

**Détails clés :**

* **Renvoie** : Un `DocumentFragment` qui contient les nœuds et éléments clonés à l'intérieur de la plage.
    
* **Non destructif** : Cette méthode n'altère ni ne supprime le contenu du document original – elle crée simplement une copie.
    

**Exemple de code :**

```typescript
// Créer un objet range
const range = document.createRange();

// Sélectionner le contenu d'un élément spécifique
const element = document.getElementById('myElement');
range.selectNodeContents(element);

// Cloner le contenu de la plage
const clonedContent = range.cloneContents();

// Ajouter le contenu cloné quelque part dans le document
document.body.appendChild(clonedContent);
```

**Comment ça marche :**

1. `document.createRange()` : Crée un nouvel objet `Range`.
    
2. `range.selectNodeContents(element)` : Sélectionne tout le contenu à l'intérieur de l'élément spécifié.
    
3. `range.cloneContents()` : Crée un `DocumentFragment` qui contient une copie des contenus sélectionnés.
    
4. `document.body.appendChild(clonedContent)` : Ajoute le contenu cloné quelque part dans le document (dans ce cas, à la fin du body).
    

**Cas d'utilisation :**

1. **Duplication de contenu** : Utilisez cette méthode lorsque vous devez créer une copie du contenu sélectionné sans modifier l'original.
    
2. **Manipulation des données copiées** : Après avoir cloné le contenu, vous pouvez modifier ou traiter le fragment cloné (par exemple, pour des fonctionnalités de glisser-déposer, des infobulles personnalisées ou la sauvegarde d'une partie du contenu).
    

**Scénario d'exemple :**

Si vous souhaitez copier une partie du contenu d'une page Web et l'afficher ailleurs :

```typescript
const range = document.createRange();
const element = document.querySelector('#textElement');
range.setStart(element.firstChild, 0);  // Définir le début de la plage
range.setEnd(element.firstChild, 10);   // Définir la fin de la plage (10 premiers caractères)

// Cloner le contenu et l'ajouter à un autre élément
const clonedContent = range.cloneContents();
document.querySelector('#targetElement').appendChild(clonedContent);
```

Dans cet exemple, les 10 premiers caractères de `#textElement` sont clonés et insérés dans `#targetElement`. Cela n'affecte pas le contenu original dans `#textElement`.

### Cas d'utilisation de l'API Selection

#### 1\. Mise en évidence de texte

En utilisant l'API Selection, vous pouvez mettre en évidence du texte dynamiquement en fonction de l'entrée de l'utilisateur. Par exemple, vous pouvez envelopper le texte sélectionné dans une balise `<mark>` pour le mettre en évidence.

```xml
<p id="text">Ceci est un texte sélectionnable.</p>
<button onclick="highlightSelection()">Mettre en évidence</button>

<script>
function highlightSelection() {
    const selection = window.getSelection();
    if (selection.rangeCount > 0) {
        const range = selection.getRangeAt(0);
        const highlight = document.createElement('mark');
        range.surroundContents(highlight);
    }
}
</script>
```

Ce script permet aux utilisateurs de mettre en évidence le texte sélectionné d'un simple clic.

#### 2\. Copier le texte sélectionné

Vous pouvez facilement extraire et manipuler le texte sélectionné avec la méthode `Selection.toString()`. Voici un exemple de copie du texte sélectionné dans le presse-papiers :

```xml
<p id="text">Sélectionnez n'importe quelle partie de ce texte et copiez-la dans le presse-papiers.</p>
<button onclick="copySelection()">Copier</button>

<script>
function copySelection() {
    const selection = window.getSelection();
    const text = selection.toString();
    
    navigator.clipboard.writeText(text).then(() => {
        alert("Copié dans le presse-papiers : " + text);
    });
}
</script>
```

Cet extrait permet aux utilisateurs de copier n'importe quel texte sélectionné et de le coller ailleurs.

#### 3\. Annotation de texte

Vous pouvez combiner l'API Selection avec des annotations personnalisées. Vous pouvez afficher une infobulle flottante ou une boîte d'annotation en détectant la position de la sélection sur la page.

```xml
<p>Sélectionnez du texte pour voir la boîte d'annotation.</p>

<script>
document.addEventListener("mouseup", () => {
    const selection = window.getSelection();
    const selectedText = selection.toString();
    
    if (selectedText.length > 0) {
        const range = selection.getRangeAt(0);
        const rect = range.getBoundingClientRect();
        
        const annotationBox = document.createElement("div");
        annotationBox.style.position = "absolute";
        annotationBox.style.left = `${rect.left}px`;
        annotationBox.style.top = `${rect.top - 30}px`;
        annotationBox.textContent = "Annotez ceci !";
        document.body.appendChild(annotationBox);
    }
});
</script>
```

Ce script crée une boîte d'annotation juste au-dessus du texte sélectionné.

### Fonctionnalités avancées de l'API Selection

1. **Plages multiples** : Certains navigateurs prennent en charge plusieurs sélections de texte sur une seule page, où vous pouvez sélectionner plusieurs plages de texte et les manipuler simultanément.
    
2. **Détection des changements de sélection** : Vous pouvez écouter les événements `selectionchange` sur le document, ce qui vous permet de détecter quand l'utilisateur modifie sa sélection.
    
    ```typescript
    document.addEventListener("selectionchange", () => {
        const selection = window.getSelection();
        console.log("Sélection modifiée :", selection.toString());
    });
    ```
    
3. **Travailler avec les formulaires** : Les sélections peuvent être utiles dans les formulaires, vous permettant d'auto-compléter, de copier ou de valider la saisie de l'utilisateur en fonction du texte sélectionné.
    

L'**API Selection de JavaScript** est un outil puissant pour créer des applications Web dynamiques et interactives. Que vous souhaitiez implémenter une fonctionnalité personnalisée de copier/coller, activer des annotations ou créer des éditeurs de texte avancés, l'API Selection fournit le contrôle et la flexibilité dont vous avez besoin pour gérer les sélections des utilisateurs.

Grâce à ses méthodes et propriétés faciles à utiliser, vous pouvez améliorer les expériences utilisateur et créer des fonctionnalités intuitives basées sur la sélection.

## Exemple d'utilisation : comment créer un éditeur de texte enrichi avec l'API Selection JavaScript

L'API Selection permet non seulement d'interagir avec les sélections de texte, mais ouvre également la porte à une manipulation de texte plus avancée, comme la création d'un **éditeur de texte enrichi**. Un éditeur de texte enrichi (Rich Text Editor - RTE) permet aux utilisateurs de formater le texte sélectionné avec des fonctionnalités telles que le gras, l'italique et le souligné.

Dans cette section, nous allons voir comment construire un éditeur de texte enrichi de base en utilisant l'API Selection et fournir un exemple avec les principales fonctionnalités de formatage.

### Comment l'API Selection aide-t-elle à construire un éditeur de texte enrichi ?

L'API Selection vous permet de :

* Détecter le texte sélectionné par l'utilisateur.
    
* Modifier par programmation le contenu sélectionné, par exemple, en appliquant un style gras, italique ou souligné.
    
* Permettre aux utilisateurs d'effectuer des modifications sur place avec des commandes d'interface utilisateur simples (comme des boutons ou des raccourcis clavier).
    

En utilisant `window.getSelection()` et l'API Range, vous pouvez manipuler le texte en fonction des actions de l'utilisateur (comme cliquer sur un bouton "Gras"). Vous pouvez ensuite envelopper le texte sélectionné dans les balises HTML appropriées (`<b>`, `<i>`, `<u>`) ou appliquer des styles en ligne.

### Fonctionnalités de base d'un éditeur de texte enrichi

Pour notre exemple, nous allons implémenter trois fonctionnalités de formatage de base :

1. **Gras** : Mettre le texte sélectionné en gras.
    
2. **Italique** : Mettre le texte sélectionné en italique.
    
3. **Souligné** : Souligner le texte sélectionné.
    

#### Structure HTML

Voici une mise en page simple pour l'éditeur avec des boutons pour le Gras, l'Italique et le Souligné :

```xml
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Éditeur de texte enrichi simple</title>
  <style>
    #editor {
      border: 1px solid #ccc;
      min-height: 150px;
      padding: 10px;
      margin-top: 10px;
    }
    .toolbar {
      margin-bottom: 5px;
    }
    .toolbar button {
      margin-right: 5px;
    }
  </style>
</head>
<body>
  <div class="toolbar">
    <button onclick="formatText('bold')"><b>Gras</b></button>
    <button onclick="formatText('italic')"><i>Italique</i></button>
    <button onclick="formatText('underline')"><u>Souligné</u></button>
  </div>

  <!-- Div contenteditable pour l'éditeur -->
  <div id="editor" contenteditable="true">
    Tapez votre texte ici...
  </div>

  <script src="editor.js"></script>
</body>
</html>
```

#### JavaScript : Gérer le formatage avec l'API Selection

Maintenant que nous avons la structure de base, ajoutons du JavaScript pour gérer le formatage du texte. Nous utiliserons l'**API Selection** et `document.execCommand()`, une méthode héritée toujours prise en charge par la plupart des navigateurs, pour appliquer le formatage.

Voici le JavaScript pour rendre les boutons fonctionnels :

```typescript
// Fonction pour formater le texte en fonction de la commande
function formatText(command) {
  document.execCommand(command, false, null);
}
```

La méthode `execCommand` vous permet d'exécuter des commandes sur le contenu à l'intérieur d'un élément qui possède l'attribut `contenteditable`. Dans notre cas, les commandes seront `'bold'`, `'italic'` et `'underline'`.

### La fonction `document.execCommand()`

La fonction `document.execCommand()` est une méthode héritée fournie par les navigateurs qui permet aux développeurs d'effectuer diverses opérations d'édition de documents directement sur le contenu d'un élément `contenteditable`. Cette méthode a été largement utilisée pour construire des éditeurs de texte enrichi pour les applications Web en raison de sa simplicité et de sa prise en charge par les navigateurs.

Bien qu'elle soit toujours fonctionnelle dans la plupart des navigateurs modernes, il est important de noter que `execCommand` a été dépréciée et pourrait ne plus être prise en charge dans les futures versions des navigateurs. Mais elle constitue toujours un bon point de départ pour les éditeurs de texte enrichi de base.

Si vous recherchez une solution à long terme, des API plus récentes comme l'API Selection combinée à l'API Range ou des bibliothèques tierces (comme Quill.js et Draft.js) sont recommandées pour des besoins d'édition complexes.

### Qu'est-ce que `document.execCommand()` ?

La méthode `document.execCommand()` exécute une commande spécifiée pour manipuler ou formater le texte dans un élément **contenteditable** (comme une div, un textarea ou un champ d'entrée). Elle peut effectuer des commandes telles que l'application de styles, la modification de l'alignement du texte, la création de liens, et bien plus encore.

#### Syntaxe de `execCommand()` :

```typescript
document.execCommand(command, showUI, value);
```

* `command` : Une chaîne de caractères qui représente la commande à exécuter (par exemple, `'bold'`, `'italic'`, `'underline'`, `'createLink'`).
    
* `showUI` : Une valeur booléenne indiquant si l'interface utilisateur par défaut pour la commande doit être affichée (presque toujours `false`, car les interfaces utilisateur des navigateurs sont souvent incohérentes).
    
* `value` : Optionnel. Une chaîne représentant la valeur à passer pour certaines commandes (par exemple, l'URL pour créer un lien).
    

#### Valeur de retour

`execCommand()` renvoie `true` si la commande est exécutée avec succès ou `false` sinon.

### Comment améliorer l'éditeur de texte enrichi

Bien que l'exemple ci-dessus vous donne un éditeur de texte enrichi de base, vous pouvez étendre ses fonctionnalités en ajoutant plus de contrôles et en gérant d'autres commandes :

* **Couleur du texte** : Changer la couleur du texte sélectionné en utilisant `execCommand('foreColor', false, 'red')`.
    
* **Alignement du texte** : Aligner le texte à gauche, au centre ou à droite en utilisant des commandes comme `execCommand('justifyCenter')`.
    
* **Annuler/Rétablir** : Implémenter les fonctionnalités d'annulation et de rétablissement en utilisant `execCommand('undo')` et `execCommand('redo')`.
    
* **Ajout de liens** : Permettre aux utilisateurs d'ajouter des liens avec `execCommand('createLink', false, '`[`http://example.com`](http://example.com)`')`.
    

En utilisant l'API Selection combinée à `document.execCommand()`, nous avons construit un éditeur de texte enrichi simple mais fonctionnel avec des fonctionnalités de gras, d'italique et de souligné. Cet éditeur de base peut être encore amélioré avec des fonctionnalités supplémentaires telles que la taille de la police, la couleur et l'alignement pour créer un éditeur de texte enrichi complet pour vos applications Web.

### **Comment obtenir l'élément cliqué et sa position en temps réel**

Le moyen le plus simple de détecter l'élément cliqué dans une page Web est d'utiliser l'écouteur d'événement `click` en JavaScript.

Voici comment vous pouvez faire :

```typescript
document.addEventListener('click', (event) => {
    const clickedElement = event.target;
    console.log('Vous avez cliqué sur :', clickedElement.tagName);
});
```

#### Explication du code :

* `document.addEventListener('click', ...)` : Cela attache un écouteur d'événement à l'ensemble du document.
    
* [`event.target`](http://event.target) : Cette propriété renvoie l'élément spécifique qui a été cliqué.
    
* `clickedElement.tagName` : Cela fournit le nom de la balise de l'élément cliqué (comme `DIV`, `SPAN`, `BUTTON`, etc.).
    

Cela affichera le nom de la balise de l'élément dans la console lorsque vous cliquerez n'importe où sur le document.

### **Comment obtenir la position en temps réel de l'élément**

Une fois que vous avez l'élément cliqué, vous pouvez trouver sa position sur l'écran en utilisant l'API DOM de JavaScript. Plus précisément, `getBoundingClientRect()` nous donne la position de l'élément par rapport à la fenêtre d'affichage (viewport).

```typescript
document.addEventListener('click', (event) => {
    const clickedElement = event.target;
    const position = clickedElement.getBoundingClientRect();

    console.log(`Élément : ${clickedElement.tagName}`);
    console.log(`Position : Haut - ${position.top}px, Gauche - ${position.left}px`);
});
```

#### Explication du code :

* `getBoundingClientRect()` : Cette méthode renvoie la taille d'un élément et sa position par rapport à la fenêtre d'affichage. Elle vous donne plusieurs propriétés utiles :
    
    * `top` : Distance par rapport au haut de la fenêtre d'affichage.
        
    * `left` : Distance par rapport à la gauche de la fenêtre d'affichage.
        
    * `right` : Distance du bord gauche au bord droit de l'élément.
        
    * `bottom` : Distance du bord supérieur au bord inférieur de l'élément.
        

Les valeurs `top` et `left` sont généralement les plus utiles, car elles vous indiquent où l'élément est positionné.

### **Exemple complet avec code**

Méttons tout cela ensemble. Nous allons créer un exemple interactif où le fait de cliquer sur n'importe quel élément affiche son nom de balise et sa position à la manière d'une infobulle.

Voici le code complet :

```xml
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Détecter l'élément cliqué et sa position</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .tooltip {
            position: absolute;
            background-color: #333;
            color: #fff;
            padding: 5px;
            border-radius: 5px;
            font-size: 12px;
            display: none;
        }
    </style>
</head>
<body>

<div class="tooltip" id="tooltip"></div>

<h1>Cliquez sur les éléments pour voir leur balise et leur position</h1>
<p>Ceci est un paragraphe. Cliquez dessus !</p>
<button>Cliquez-moi</button>
<div style="width: 100px; height: 100px; background-color: lightblue;">Cliquez sur cette boîte</div>

<script>
    const tooltip = document.getElementById('tooltip');

    document.addEventListener('click', (event) => {
        const clickedElement = event.target;
        const position = clickedElement.getBoundingClientRect();
        
        // Obtenir le nom de la balise de l'élément cliqué
        const elementTag = clickedElement.tagName;

        // Obtenir la position actuelle de l'élément
        const top = position.top + window.scrollY; // Tenir compte du défilement de la page
        const left = position.left + window.scrollX;

        // Afficher l'infobulle près de l'élément cliqué
        tooltip.innerHTML = `Balise : ${elementTag}<br>Position : Haut - ${Math.round(top)}px, Gauche - ${Math.round(left)}px`;
        tooltip.style.display = 'block';
        tooltip.style.top = `${top + 20}px`; // Décalage pour positionner sous l'élément
        tooltip.style.left = `${left + 20}px`; // Décalage pour positionner à droite de l'élément
    });

    document.addEventListener('scroll', () => {
        tooltip.style.display = 'none'; // Masquer l'infobulle lorsque l'utilisateur fait défiler la page
    });
</script>

</body>
</html>
```

#### Explication du code :

1. **Structure HTML** :
    
    * La div `tooltip` est initialement masquée mais sera affichée dynamiquement lorsqu'un utilisateur cliquera sur un élément.
        
    * Nous avons inclus quelques éléments cliquables (`h1`, `p`, `button`, `div`) à des fins de démonstration.
        
2. **JavaScript** :
    
    * Lorsqu'un élément est cliqué, nous calculons son nom de balise et sa position en utilisant [`event.target`](http://event.target) et `getBoundingClientRect()`.
        
    * Nous mettons à jour le contenu de `tooltip` et le déplaçons dynamiquement en fonction de la position de l'élément.
        
    * `window.scrollY` et `window.scrollX` sont ajoutés pour tenir compte de tout défilement survenu sur la page.
        
3. **CSS** :
    
    * L'infobulle est stylisée comme une petite boîte avec un fond sombre et du texte blanc. Elle est initialement masquée (`display: none`).
        
    * Lorsqu'un élément est cliqué, l'infobulle est positionnée près de l'élément cliqué en ajustant ses styles `top` et `left`.
        

### Exemple en direct :

Cliquez n'importe où sur la page Web et vous verrez le nom de la balise et la position de l'élément cliqué s'afficher dans une infobulle. Cette méthode est bénéfique pour créer des interactions personnalisées, déboguer ou gérer des mises en page complexes dans les applications Web modernes.

## Conclusion

Dans ce tutoriel, nous avons exploré comment utiliser l'**API Selection de JavaScript** pour interagir avec le texte que l'utilisateur sélectionne et le manipuler par programmation. Nous avons également découvert la fonction `document.execCommand()` qui, bien que dépréciée, nous permet d'appliquer un formatage de texte de base comme le gras, l'italique et le souligné au contenu sélectionné.

Nous avons démontré comment construire un éditeur de texte enrichi simple avec des fonctionnalités de base en utilisant ces outils. Nous avons également abordé comment détecter quel élément HTML a été cliqué en utilisant l'événement `click` et en accédant à la propriété [`event.target`](http://event.target).

Ces techniques constituent la base de la création d'éditeurs de texte Web dynamiques et interactifs.