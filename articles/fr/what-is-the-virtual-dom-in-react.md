---
title: Qu'est-ce que le Virtual DOM dans React ?
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-06-05T14:51:11.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-virtual-dom-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/Virtual-DOM.png
tags:
- name: DOM
  slug: dom
- name: React
  slug: react
- name: virtual dom
  slug: virtual-dom
seo_title: Qu'est-ce que le Virtual DOM dans React ?
seo_desc: As web applications become more complex, managing updates to the user interface
  becomes a challenging task. This is where the Virtual DOM (Document Object Model)
  comes into play – particularly in React, the leading JavaScript library for building
  use...
---

À mesure que les applications web deviennent plus complexes, la gestion des mises à jour de l'interface utilisateur devient une tâche ardue. C'est là que le Virtual DOM (Document Object Model) entre en jeu – en particulier dans React, la bibliothèque JavaScript de premier plan pour la création d'interfaces utilisateur.

Le Virtual DOM est une copie légère du vrai DOM qui permet à React de gérer les changements plus efficacement en minimisant la manipulation directe requise sur le vrai DOM. Ce processus améliore considérablement les performances des applications web.

Comprendre le Virtual DOM est essentiel pour les développeurs qui veulent tirer le meilleur parti de React. Il joue un rôle clé dans la manière dont React met à jour l'UI, en s'assurant que les changements sont appliqués rapidement sans re-rendus inutiles.


Dans cet article, vous apprendrez :

* Qu'est-ce que le Virtual DOM et comment il fonctionne
* Comment le Virtual DOM se compare au vrai DOM
* Les avantages de l'utilisation du Virtual DOM
* Comment React utilise le Virtual DOM
* Comment le Virtual DOM se compare au Shadow DOM
* Les idées reçues courantes sur le Virtual DOM

## Qu'est-ce que le Virtual DOM et comment fonctionne-t-il ?

Le Virtual DOM est une représentation en mémoire des éléments du vrai DOM. Au lieu d'interagir directement avec le vrai DOM, ce qui peut être lent et coûteux en termes de performance, React crée une représentation virtuelle des composants de l'UI. Cette représentation virtuelle est un objet JavaScript léger qui reflète la structure du vrai DOM.

Voici un processus étape par étape de la manière dont le Virtual DOM fonctionne :

1. **Étape 1 – Rendu initial** : lorsque l'application démarre, l'ensemble de l'UI est représenté sous forme de Virtual DOM. Les éléments React sont créés et rendus dans la structure virtuelle.
2. **Étape 2 – Changements d'état et de props** : à mesure que les états et les props changent dans l'application, React re-rend les composants affectés dans le Virtual DOM. Ces changements n'impactent pas immédiatement le vrai DOM.
3. **Étape 3 – Comparaison à l'aide de l'algorithme de diff** : React utilise ensuite un **algorithme de diff** pour comparer la version actuelle du Virtual DOM avec la version précédente. Ce processus identifie les différences (ou "diffs") entre les deux versions.
4. **Étape 4 – Processus de réconciliation** : en fonction des différences identifiées, React détermine la manière la plus efficace de mettre à jour le vrai DOM. Seules les parties du vrai DOM qui doivent être mises à jour sont modifiées, plutôt que de re-rendre l'ensemble de l'UI. Cette mise à jour sélective est rapide et performante.
5. **Étape 5 – Mise à jour du vrai DOM** : enfin, React applique les changements nécessaires au vrai DOM. Cela peut impliquer l'ajout, la suppression ou la mise à jour d'éléments en fonction des différences détectées à l'étape 3.

Par exemple, supposons que nous avons la fonctionnalité de compteur suivante dans le composant `App` :

```jsx
import React, { useState } from 'react';

function App() {
 const [count, setCount] = useState(0);

 return (
   <div>
     <h1>Compteur : {count}</h1>
     <button onClick={() => setCount(count + 1)}>Incrémenter</button>
   </div>
 );
}

export default App;
```

La représentation du Virtual DOM ressemblera à ceci :

```json
{
 "type": "div",
 "props": {},
 "children": [
   {
     "type": "h1",
     "props": {},
     "children": [
       {
         "type": "TEXT_ELEMENT",
         "props": {
           "nodeValue": "Compteur : 0"
         }
       }
     ]
   },
   {
     "type": "button",
     "props": {
       "onClick": "setCount(count + 1)"
     },
     "children": [
       {
         "type": "TEXT_ELEMENT",
         "props": {
           "nodeValue": "Incrémenter"
         }
       }
     ]
   }
 ]
}

```

Lorsque le bouton `Incrémenter` est cliqué une fois, seul l'élément `h1` est modifié :

```json
{
 "type": "h1",
 "props": {},
 "children": [
   {
     "type": "TEXT_ELEMENT",
     "props": {
       "nodeValue": "Compteur : 1"
     }
   }
 ]
}

```

## Comparaison du Virtual DOM avec le vrai DOM

Pour voir les avantages du Virtual DOM, il est important de comprendre comment il diffère du vrai DOM. Le vrai DOM et le Virtual DOM servent des objectifs similaires mais opèrent de manière distincte avec des implications significatives pour la performance et l'efficacité.

Le vrai DOM est une interface standard intégrée dans les navigateurs qui représente et interagit avec les éléments HTML, de la déclaration `Doctype` et de l'élément racine `html` à tous les autres éléments qu'il contient.

Ce vrai DOM représente l'ensemble du document HTML sous forme de structure arborescente et permet à JavaScript de manipuler et de modifier les documents HTML. Parfois, lorsque ces changements se produisent, l'ensemble du document peut être re-rendu.

Cela contraste avec le Virtual DOM, qui utilise un **algorithme de diff** pour comparer les versions actuelle et précédente des mises à jour du DOM. Il ne re-rend que les parties de l'UI qui ont changé, au lieu de tout re-rendre.

## Avantages de l'utilisation du Virtual DOM dans le développement web

### Développement simplifié

Le Virtual DOM vous permet d'écrire du code dans un style plus déclaratif. Cela signifie que, au lieu d'écrire des instructions détaillées sur la manière de mettre à jour l'UI, vous pouvez simplement décrire à quoi l'UI devrait ressembler, et React s'occupe du reste. Cela est rendu possible par la syntaxe déclarative de React et son architecture basée sur les composants.

### Performance améliorée

L'un des principaux avantages de l'utilisation du Virtual DOM est l'amélioration significative des performances qu'il offre. La manipulation directe du vrai DOM est lente et peut entraîner des problèmes de performance, en particulier dans les applications complexes.

### Expérience utilisateur améliorée

Le Virtual DOM contribue à une meilleure UX en garantissant que les mises à jour de l'UI sont fluides, réactives et sans rafraîchissement complet de la page. Les utilisateurs sont moins susceptibles de rencontrer des retards ou des saccades, ce qui entraîne une interaction plus fluide avec l'application.

### Développement multiplateforme

Les principes du Virtual DOM ne sont pas limités au développement web uniquement. React Native – une version de React pour la création d'applications mobiles multiplateformes – utilise une approche similaire. Cela augmente la productivité et réduit le temps de développement car vous pouvez réutiliser du code sur les plateformes web et mobiles.

## Idées reçues courantes sur le Virtual DOM

Il existe quelques idées reçues sur le Virtual DOM. Examinons cinq de ces idées reçues et les réalités de chacune d'elles.

### Le Virtual DOM est une fonctionnalité du navigateur

**Réalité** : le Virtual DOM est une abstraction implémentée par React, et non une fonctionnalité du navigateur. Les navigateurs ont le vrai DOM, qui est la manière standard de représenter et d'interagir avec les documents HTML. Le Virtual DOM existe uniquement en mémoire au sein de React et est utilisé pour optimiser les mises à jour du vrai DOM.

### Le Virtual DOM remplace le vrai DOM

**Réalité** : le Virtual DOM agit comme un intermédiaire entre React et le navigateur, et non comme un remplacement du vrai DOM. Le vrai DOM est toujours ce que le navigateur utilise pour rendre l'UI, mais les mises à jour de celui-ci sont gérées via le Virtual DOM.

### React est la seule bibliothèque et le seul framework qui utilise le Virtual DOM

**Réalité** : React a seulement popularisé le concept du Virtual DOM, mais ce n'est pas la seule bibliothèque ou framework qui l'utilise. D'autres frameworks comme VueJS et SolidJS utilisent également le Virtual DOM pour mettre à jour l'UI.

### Le Virtual DOM résout tous les problèmes de performance

**Réalité** : le Virtual DOM peut améliorer considérablement les performances, mais ce n'est pas une solution magique à tous les problèmes. De mauvaises pratiques de codage, des rendus inutiles et de grands arbres de composants peuvent encore entraîner des problèmes de performance.

### Le Virtual DOM et le Shadow DOM sont identiques

**Réalité** : le Virtual DOM et le Shadow DOM ne sont pas la même chose. Le Virtual DOM est une copie légère du vrai DOM avec laquelle React optimise les mises à jour de l'UI. En revanche, le Shadow DOM est une technologie de navigateur utilisée pour encapsuler les styles et la structure des composants web.

## Vrai DOM vs Virtual DOM vs Shadow DOM

Maintenant que nous avons établi que le Virtual DOM, le Shadow DOM et le vrai DOM ne sont pas identiques, examinons les différences entre les trois.

|  **Aspect** | **Vrai DOM**  | **Virtual DOM**   | **Shadow DOM**  
|---|---|---|---|---|
| **Définition**  | API standard du navigateur pour représenter et interagir avec les documents HTML  |  Représentation en mémoire du vrai DOM | Une technologie de navigateur qui encapsule et isole le DOM et le style des composants web  
|**Flexibilité**| Manipulé directement via JavaScript ou les API DOM | Abstrait et optimisé par le framework | Limité aux frontières des composants
|  **Implémentation** |  Fournie par le navigateur | Implémentée par des frameworks comme React et Vue  | Fait partie de la norme des Web Components, fournie par le navigateur 
|  **Performance** | La manipulation directe peut être lente et causer des problèmes de performance  | Déjà optimisée pour des mises à jour efficaces  | Fournit une encapsulation, réduisant les conflits de style 
|**Utilisation**|Pour le rendu et l'interaction avec les documents web|Pour des mises à jour efficaces de l'UI par les frameworks| Pour créer des composants web isolés et réutilisables
|**Mises à jour**| Mises à jour immédiates de l'UI | Les mises à jour sont regroupées et optimisées | Les mises à jour sont limitées au composant, n'affectant pas le DOM global
| **Repaints** | Les mises à jour fréquentes peuvent causer des repaints coûteux | Minimise les repaints en regroupant les mises à jour | Limité au composant, réduisant les repaints globaux
|**Cas d'utilisation**| Développement web général et manipulation de documents | Mises à jour efficaces de l'UI dans des frameworks comme React et Vue | Encapsulation des styles et de la structure dans les composants web


## Conclusion

Comme vous l'avez lu dans cet article, le Virtual DOM est une fonctionnalité clé de React qui améliore les performances et les mises à jour efficaces de l'UI. Avec cela, React peut regrouper les mises à jour, minimiser les reflows et les repaints, et appliquer les changements efficacement. Cela rend les mises à jour de l'UI rapides et fluides, offrant une meilleure expérience utilisateur dans le processus.

Comprendre le Virtual DOM et son fonctionnement peut vous aider à créer des applications React performantes.

## Apprendre React et Next JS

Vous voulez découvrir d'autres fonctionnalités cool de React comme le Virtual DOM ? Inscrivez-vous à mon cours React 18 sur Udemy ! Je vous guiderai à travers le monde de React en créant un super jeu 2048 avec des animations à partir de zéro.

[![Next.js crash course on Udemy](https://assets.mateu.sh/assets/fcc-universal)](https://assets.mateu.sh/r/fcc-universal)