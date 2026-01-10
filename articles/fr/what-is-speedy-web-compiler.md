---
title: Qu'est-ce que Speedy Web Compiler ? SWC expliqué avec des exemples
subtitle: ''
author: Preston Mayieka
co_authors: []
series: null
date: '2024-09-05T01:07:47.919Z'
originalURL: https://freecodecamp.org/news/what-is-speedy-web-compiler
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725290113209/260f00cb-5bfe-4260-8e45-0c61a1897cae.png
tags:
- name: Web Development
  slug: web-development
- name: JavaScript
  slug: javascript
- name: Rust
  slug: rust
- name: web performance
  slug: web-performance
seo_title: Qu'est-ce que Speedy Web Compiler ? SWC expliqué avec des exemples
seo_desc: 'In the evolving landscape of JavaScript development, the need for efficient
  and powerful tooling has become increasingly important.

  Developers rely on tools like compilers and bundlers to transform their code, optimize
  performance, and ensure compati...'
---

Dans le paysage en constante évolution du développement JavaScript, le besoin d'outils performants et puissants est devenu de plus en plus crucial.

Les développeurs s'appuient sur des outils tels que les [**compilateurs**](https://en.wikipedia.org/wiki/Compiler) et les [**bundlers**](https://www.codejourney.net/what-is-a-javascript-bundler/) pour transformer leur code, optimiser les performances et assurer la compatibilité entre différents environnements.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1725287352931/41e13dc3-100e-4f75-87df-98342df4beb2.png align="center")

Ces outils sont essentiels pour les applications JavaScript modernes, permettant aux développeurs d'écrire un code propre et maintenable tout en profitant des dernières fonctionnalités du langage.

Cet article vous aidera à comprendre ce qu'est Speedy Web Compiler (SWC) et comment il aide à optimiser les performances de vos applications web.

## Table des matières

* [Introduction à Speedy Web Compiler](#heading-quest-ce-que-speedy-web-compiler)
    
* [Contexte de SWC](#heading-contexte-de-swc)
    
* [Comment fonctionne Speedy Web Compiler](#heading-comment-fonctionne-speedy-web-compiler)
    
* [Avantages de l'utilisation de Speedy Web Compiler](#heading-avantages-de-lutilisation-de-speedy-web-compiler)
    
* [Comment configurer Speedy Web Compiler dans votre projet](#heading-comment-configurer-speedy-web-compiler)
    
* [Intégration de SWC dans les Frameworks populaires](#heading-integration-de-swc-dans-les-frameworks-populaires)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que Speedy Web Compiler ?

Tout d'abord, laissez-moi vous expliquer.

SWC signifie Speedy Web Compiler, et lorsqu'on le décompose :

**Speedy** - Cela signifie que c'est rapide ! SWC traite et transforme le code JavaScript, ce qui le rend efficace pour une utilisation dans de grands projets.

**Web** - Tout est question de développement web. Il se concentre sur l'amélioration de la gestion du JavaScript (le langage du web).

**Compiler** - Il prend du code écrit dans une forme et le transforme dans une autre forme qui peut être mieux comprise ou utilisée par les ordinateurs.

## Contexte de SWC

[kdy1](https://github.com/kdy1), un développeur sud-coréen et contributeur de [Next.js](https://nextjs.org/), a créé SWC comme un outil plus rapide pour gérer le code JavaScript.

La motivation était le besoin de rapidité et d'efficacité, car les projets web deviennent de plus en plus volumineux et complexes.

Avec de nombreux sites web et applications dépendant de JavaScript, SWC aide les développeurs à gagner du temps et à travailler plus efficacement.

## Comment fonctionne Speedy Web Compiler

SWC utilise [Rust](https://www.rust-lang.org/), un langage de programmation réputé pour sa rapidité et sa sécurité.

SWC fonctionne en prenant votre code JavaScript ou TypeScript et en le transformant en une version capable de s'exécuter efficacement dans divers environnements.

Comprendre comment SWC y parvient implique d'examiner ses étapes fondamentales : l'analyse syntaxique (parsing), la transformation et la génération de code.

### Comment SWC analyse-t-il le code ?

La première étape du processus de compilation est l'analyse syntaxique (parsing).

Elle commence par la **lecture** et l'analyse du code pour comprendre sa structure.

C'est un peu comme prendre une phrase complexe et la décomposer en ses composants grammaticaux : sujet, verbe, complément, etc.

![Illustration de l'analyse de code formant un arbre de syntaxe abstraite](https://cdn.hashnode.com/res/hashnode/image/upload/v1725287153049/b7ec431c-24db-4c7a-9fb0-ef3ce0d92921.png align="center")

En termes techniques, SWC convertit votre code en un [**Arbre de Syntaxe Abstraite (AST)**.](https://en.wikipedia.org/wiki/Abstract_syntax_tree)

L'AST est une représentation sous forme d'arbre du code source, où chaque nœud de l'arbre correspond à une construction présente dans le code, telle que des expressions, des instructions et des fonctions.

Cette structure arborescente permet à SWC de traiter et de comprendre la logique du code d'une manière à la fois efficace et évolutive.

### Comment SWC transforme-t-il le code ?

Après avoir créé l'AST, SWC passe à la phase de transformation.

C'est là que la magie opère : SWC applique diverses optimisations et modifications au code en fonction de l'environnement cible.

Par exemple, si vous ciblez des navigateurs anciens qui ne supportent pas les fonctionnalités modernes de JavaScript, SWC transformera votre code ES6+ en une version rétrocompatible.

![Engrenage jaune avec deux flèches circulaires l'entourant, accompagné du texte "Transformation de l'AST" sur un fond sombre.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725287185279/371d2ac2-e919-4f25-8caf-01d4157fd290.png align="center")

Pendant cette phase, SWC gère également les transformations TypeScript. Il supprime la syntaxe spécifique à TypeScript, comme les types et les interfaces, convertissant le code en JavaScript pur qui sera exécuté par n'importe quel moteur JavaScript.

SWC peut appliquer des transformations personnalisées basées sur des plugins ou des configurations spécifiques, ce qui le rend très polyvalent.

### Comment SWC génère-t-il un code optimisé ?

Une fois les transformations terminées, SWC passe à l'étape finale : la génération de code.

Lors de cette étape, SWC prend l'AST transformé et le convertit à nouveau en code exécutable.

En revanche, ce processus n'est pas seulement l'inverse de l'analyse syntaxique.

SWC prend un soin particulier à générer un code qui est à la fois fonctionnellement correct et optimisé pour la performance.

![Dessin au trait jaune d'une fenêtre de code avec une icône de clé et d'engrenage, au-dessus d'un texte indiquant "Génération de code optimisé" sur un fond noir.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725287212996/af724e34-6473-4104-8244-e35c1be6a3c0.png align="center")

Par exemple, SWC peut supprimer le code mort (code qui ne sera jamais exécuté) ou mettre en ligne (inline) certaines fonctions pour réduire la surcharge.

L'objectif est de produire un code aussi propre et efficace que possible, garantissant qu'il s'exécute rapidement et de manière fiable dans les environnements de production.

## Avantages de l'utilisation de Speedy Web Compiler

### Performance

L'un des avantages majeurs de l'utilisation de SWC est sa vitesse exceptionnelle. SWC atteint cette rapidité hors pair grâce à l'utilisation de Rust.

Les développeurs peuvent s'attendre à une amélioration significative des performances lors de la compilation de leur code pour de grands projets ou des bases de code importantes.

![Illustration d'un chronomètre à l'intérieur d'une fenêtre de navigateur web, avec des lignes de mouvement indiquant la vitesse. Le texte ci-dessous indique "Temps de chargement plus rapides".](https://cdn.hashnode.com/res/hashnode/image/upload/v1725287254910/9c4827d9-81db-488d-bdb8-6b0806ddfd67.png align="center")

Cette vitesse réduit considérablement les temps de build, améliorant l'efficacité et la réactivité du processus de développement. C'est tellement rapide qu'on pourrait croire qu'il est en retard pour une réunion !

### Sortie optimisée

SWC compile votre code et garantit que la sortie est hautement optimisée pour les performances en environnement de production en supprimant le code mort, en mettant les fonctions en ligne et en réduisant la taille du résultat.

Cela rend l'utilisation de SWC rentable, vous épargnant des dépenses supplémentaires pendant la production.

Le résultat est un code plus léger, plus rapide et plus efficace qui peut améliorer les temps de chargement et les performances des applications web.

### Compatibilité

SWC est entièrement compatible avec les bibliothèques et Frameworks JavaScript modernes.

Vous n'avez pas à vous soucier de l'utilisation d'ES6+ ou de TypeScript. Cela fait de SWC un choix polyvalent pour vos projets.

## Comment configurer Speedy Web Compiler

### Installation

Pour installer SWC dans votre projet JavaScript ou TypeScript, suivez ces étapes :

1. **Initialisez votre projet :** Si ce n'est pas déjà fait, commencez par initialiser un nouveau projet. Dans votre terminal, lancez :
    

```bash
npm init -y
```

2. **Installez SWC avec npm :** Exécutez la commande suivante pour télécharger les binaires pré-construits :
    

```bash
npm install -D @swc/cli @swc/core
```

3. **Créez un fichier JavaScript :** Créez un fichier `src/index.js` avec du code :
    

```javascript
const greet = (name) => {
  return `Hello, ${name}!`;
};

console.log(greet("World"));
```

4. **Compilez avec SWC :** Lancez SWC depuis la ligne de commande pour compiler votre fichier JavaScript :
    

```bash
npx swc src/index.js -o dist/index.js
```

5. **Code résultant :** Le code JavaScript résultant dans `dist/index.js` ressemblera à ceci :
    

```javascript
"use strict";
var greet = function(name) {
    return "Hello, " + name + "!";
};
console.log(greet("World"));
```

Il s'agit du code ES5 transpilé produit par SWC, adapté aux environnements qui nécessitent une rétrocompatibilité avec les anciennes versions de JavaScript.

## Intégration de SWC dans les Frameworks populaires

Si vous utilisez Next.js, Deno, Vite, Remix, Parcel ou Turbopack, SWC est déjà intégré.

![Logos de divers frameworks et outils de développement web sur fond noir, incluant : Deno, Vite, Next.js, Remix, Turbopack, et une boîte en carton ouverte.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725287305286/e0a1e681-4531-402c-ae41-1f8c5f1318c8.png align="center")

> Des améliorations notables ont été apportées à Next.js, un framework React populaire, depuis la version 12 (Source : [Next.js 12: The SDK for the Web](https://nextjs.org/blog/next-12))

## Conclusion

Dans le domaine en constante mutation du développement JavaScript, posséder les bons outils peut faire une différence significative.

SWC, le [Speedy Web Compiler](http://swc.rs), se distingue comme une solution robuste pour convertir et optimiser le code JavaScript et TypeScript.

Sa vitesse impressionnante, due à son implémentation basée sur Rust, ainsi que sa gestion efficace des transformations et optimisations de code, en font un outil puissant pour le développement web moderne.

Si vous souhaitez rester en contact :

[Connectez-vous avec moi sur LinkedIn](https://www.linkedin.com/in/preston-mayieka/)

[Suivez-moi sur X](https://mobile.x.com/Preston_Mayieka)