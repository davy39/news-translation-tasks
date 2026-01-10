---
title: Comment utiliser les linters et les formateurs de code dans vos projets
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-04-10T22:02:17.000Z'
originalURL: https://freecodecamp.org/news/using-prettier-and-jslint
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/alysa-bajenaru-88IV5AtWjB8-unsplash.jpg
tags:
- name: clean code
  slug: clean-code
- name: eslint
  slug: eslint
- name: Prettier
  slug: prettier
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les linters et les formateurs de code dans vos projets
seo_desc: 'Hi everyone! In this article we''re going to take a look at two very useful
  tools we can use to make our lives easier when writing code: linting tools and code
  formatters.

  We''re going to talk about what these tools are, how they work, why are they use...'
---

Bonjour à tous ! Dans cet article, nous allons examiner deux outils très utiles qui peuvent faciliter notre vie lors de l'écriture de code : les outils de linting et les formateurs de code.

Nous allons parler de ce que sont ces outils, de leur fonctionnement, de leur utilité, et enfin voir comment les implémenter dans un projet React de base.

C'est parti !

# Table des matières

* [À propos des outils de linting](#heading-a-propos-des-outils-de-linting)
    
    * [Qu'est-ce que les outils de linting ?](#heading-quest-ce-que-les-outils-de-linting)
        
    * [Pourquoi les outils de linting sont-ils utiles ?](#heading-pourquoi-les-outils-de-linting-sont-ils-utiles)
        
    * [Principaux outils de linting sur le marché](#heading-principaux-outils-de-linting-sur-le-marché)
        
* [À propos des formateurs de code](#heading-a-propos-des-formateurs-de-code)
    
    * [Qu'est-ce que les formateurs de code ?](#heading-quest-ce-que-les-formateurs-de-code)
        
    * [Pourquoi les formateurs de code sont-ils utiles ?](#heading-pourquoi-les-formateurs-de-code-sont-ils-utiles)
        
    * [Principaux formateurs de code disponibles](#heading-principaux-formateurs-de-code-disponibles)
        
* [Comment implémenter ESLint et Prettier](#heading-comment-implementer-eslint-et-prettier)
    
    * [Comment installer ESLint](#heading-comment-installer-eslint)
        
    * [Comment installer Prettier](#heading-comment-installer-prettier)
        
* [Conclusion](#heading-conclusion)
    

# À propos des outils de linting

Dans le monde du développement web, les outils de linting sont devenus une partie essentielle de la boîte à outils du développeur.

Les outils de linting sont utilisés pour analyser le code source afin de détecter les erreurs potentielles ou les problèmes de style, ce qui facilite le maintien de la qualité et de la cohérence du code dans un projet.

## Qu'est-ce que les outils de linting ?

Les outils de linting sont des outils automatisés qui analysent le code source pour détecter les erreurs potentielles, les vulnérabilités de sécurité ou les problèmes de style de codage.

Ils sont conçus pour aider les développeurs à attraper les erreurs avant qu'elles ne deviennent un problème, et pour promouvoir les meilleures pratiques en matière de codage.

Le terme "lint" provient du nom du premier outil de lint, qui a été développé au début des années 1970 par une équipe de chercheurs des Bell Labs dirigée par Stephen C. Johnson.

Le premier outil de lint était conçu pour analyser le code source C afin de détecter les erreurs potentielles et les problèmes de style.

Depuis lors, les outils de linting ont évolué pour fonctionner avec une variété de langages de programmation, y compris JavaScript, Python et Ruby.

## Pourquoi les outils de linting sont-ils utiles ?

Les outils de linting sont utiles pour plusieurs raisons. Tout d'abord, ils aident à détecter les erreurs tôt dans le processus de développement, lorsqu'elles sont plus faciles et moins coûteuses à corriger.

Ensuite, ils peuvent aider à promouvoir les normes de codage et les meilleures pratiques au sein d'une équipe de développement, garantissant que le code est cohérent et maintenable.

Enfin, ils peuvent aider à identifier les vulnérabilités de sécurité potentielles dans votre code, réduisant ainsi le risque de faille.

## Principaux outils de linting sur le marché

Il existe plusieurs outils de linting disponibles sur le marché aujourd'hui. Voici quelques-uns des plus populaires :

1. **ESLint** : [ESLint](https://eslint.org/) est un linter largement utilisé et hautement configurable pour JavaScript et TypeScript. Il peut être étendu à l'aide de plugins et prend en charge divers ensembles de règles, ce qui en fait un outil flexible pour imposer des normes de codage et prévenir les erreurs.
    
2. **JSHint** : [JSHint](https://jshint.com/) est un linter populaire qui existe depuis 2010. Il offre une configuration simple et une large gamme de règles intégrées pour aider les développeurs à éviter les pièges courants et à améliorer la qualité du code.
    
3. **JSLint** : [JSLint](https://www.jslint.com/) était l'un des premiers linters développés pour JavaScript, et il est encore utilisé aujourd'hui. Il est connu pour sa rigueur et pour imposer un style de code particulier, ce qui peut être utile pour maintenir la cohérence au sein d'une équipe.
    
4. **StandardJS** : [StandardJS](https://standardjs.com/) est un linter populaire qui vise à fournir une approche "tout compris" pour le linting JavaScript. Il a une configuration minimale et inclut un ensemble de règles opinées conçues pour promouvoir un code propre et lisible.
    

Et nous devons également parler de **TypeScript**. Lorsque vous utilisez [TypeScript](https://www.typescriptlang.org/), le compilateur TypeScript lui-même agit comme un linter. Il vérifie la syntaxe du code TypeScript et fournit des avertissements et des erreurs en cas de problèmes. Ce linter intégré peut attraper des erreurs courantes et des problèmes tels que des noms de variables mal orthographiés, des appels de méthodes invalides et des erreurs de syntaxe.

Le compilateur TypeScript peut être exécuté en utilisant la commande `tsc` dans un terminal. Lorsque le drapeau `--noEmit` est utilisé, le compilateur TypeScript effectuera uniquement une vérification de syntaxe sans compiler le code en JavaScript. Cela permet au compilateur d'agir comme un linter et de fournir des commentaires sur la qualité du code sans générer de sortie.

Vous pouvez également configurer le compilateur TypeScript en utilisant un fichier `tsconfig.json` pour spécifier diverses options, y compris la rigueur de la vérification. Cela peut aider à détecter encore plus de problèmes potentiels et à garantir que le code suit les meilleures pratiques.

Si vous n'êtes pas familier avec TypeScript, je vous recommande [cet article que j'ai écrit il y a quelque temps](https://www.freecodecamp.org/news/an-introduction-to-typescript/).

# À propos des formateurs de code

Dans le développement web moderne, les formateurs de code sont devenus un outil essentiel pour les développeurs. Ces outils automatisent le processus de formatage du code, facilitant ainsi l'écriture et la lecture du code.

## Qu'est-ce que les formateurs de code ?

Les formateurs de code sont des outils automatisés qui aident à formater automatiquement le code source. Le principal objectif des formateurs de code est de standardiser le formatage du code dans un projet ou une équipe, facilitant ainsi la lecture et la compréhension du code.

Avec les formateurs de code, les développeurs n'ont plus besoin de passer du temps à formater manuellement le code, ce qui peut faire gagner beaucoup de temps et d'efforts.

Les outils de formatage de code existent depuis des décennies. L'un des premiers outils était le programme "indent", qui était utilisé pour formater le code C au début des années 1970. Mais ces premiers outils étaient limités et n'avaient pas le même niveau de fonctionnalité que les formateurs de code modernes.

Dans les années 2000, des outils comme "astyle" et "uncrustify" ont été développés, introduisant des capacités de formatage plus avancées.

## Pourquoi les formateurs de code sont-ils utiles ?

Les formateurs de code sont utiles pour diverses raisons. Tout d'abord, ils aident à standardiser le formatage du code, ce qui facilite la lecture et la compréhension du code. Cela est particulièrement important lors du travail sur de grands projets avec plusieurs développeurs, où chacun doit pouvoir lire et comprendre le code des autres.

Les formateurs de code aident également à garantir que le code est cohérent dans un projet ou une équipe, ce qui peut aider à prévenir les erreurs et à améliorer la qualité du code. Ils facilitent également la maintenance du code au fil du temps, car le code est formaté de manière cohérente et est plus facile à lire et à comprendre.

## Principaux formateurs de code disponibles

Il existe plusieurs outils de formatage de code disponibles sur le marché aujourd'hui. Voici quelques-uns des plus populaires :

1. **Prettier** : [Prettier](https://prettier.io/) est un formateur de code populaire pour JavaScript, TypeScript et CSS. Il est hautement configurable et peut être utilisé dans une variété d'environnements différents, y compris des éditeurs, des outils de construction et des vérificateurs de qualité de code.
    
2. **ESLint** : Bien que principalement connu comme un outil de linting, [ESLint](https://eslint.org/) peut également être utilisé comme un formateur de code. Il dispose d'un drapeau `--fix` qui peut automatiquement formater votre code en fonction des règles que vous définissez.
    
3. **Beautify** : Beautify est un formateur de code pour JavaScript, HTML et CSS qui peut être utilisé dans une variété d'éditeurs et d'IDE. Il permet de personnaliser vos options de formatage et prend en charge une large gamme de langages.
    

# Comment implémenter ESLint et Prettier

Bien, voyons maintenant un linter et un formateur de code en action ! Nous allons implémenter les deux outils les plus populaires (ESLint et Prettier) dans un projet React simple pour avoir une idée de leur fonctionnement.

Commençons par créer notre projet en exécutant cette commande dans notre ligne de commande : `npm create vite@latest linternsAndFormatters --template react`

Ensuite, accédez à votre projet avec `cd` et exécutez `npm install` pour installer nos dépendances.

Maintenant que notre projet est opérationnel, nous allons commencer par installer **ESLint**.

## Comment installer ESLint

Pour installer ESLint, nous pouvons simplement exécuter `npm init @eslint/config` dans notre console. Cela lancera une série de prompts demandant comment nous voulons utiliser ESLint dans notre projet et construira la configuration correspondante. Votre console pourrait ressembler à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-72.png align="left")

*Installation de ESLint*

Après tout cela, nous verrons un nouveau fichier appelé `.eslintrc.cjs` à la racine de notre projet. C'est ici que réside la configuration de ESLint et où nous pouvons personnaliser le linter selon nos préférences. La configuration initiale donnée les options que j'ai sélectionnées est la suivante :

```javascript
module.exports = {
    "env": {
        "browser": true,
        "es2021": true
    },
    "extends": [
        "eslint:recommended",
        "plugin:react/recommended"
    ],
    "overrides": [
    ],
    "parserOptions": {
        "ecmaVersion": "latest",
        "sourceType": "module"
    },
    "plugins": [
        "react"
    ],
    "rules": {
    }
}
```

Pour voir notre linter en action, ajoutons le script suivant dans notre fichier `package.json` :

```javascript
"lint": "eslint --fix . --ext .js,.jsx"
```

Ce script exécute la commande `eslint` avec l'option `--fix` pour corriger automatiquement les erreurs et avertissements de linting. La commande est exécutée sur tous les fichiers avec l'extension `.js` ou `.jsx` situés dans le répertoire racine du projet, comme spécifié par l'argument `.`.

Modifions maintenant notre fichier `app.jsx` pour avoir le code suivant :

```javascript
import React from 'react'
import './App.css'

function App() {

  const emptyVariable = ''

  return (
    <div className="App">
      <h1>Vite + React</h1>
    </div>
  )
}

export default App
```

Ensuite, exécutez `npm run lint` et voilà ! Votre linter hurle avec du texte surligné en rouge que vous avez une variable inutilisée dans votre code ! =D

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-73.png align="left")

## Comment installer Prettier

Bien, passons maintenant à notre formateur de code.

Nous allons l'installer en exécutant `npm install --save-dev --save-exact prettier`.

Ensuite, nous allons créer un fichier de configuration vide en exécutant `echo {}> .prettierrc.json`.

Puisque nous sommes ici, ajoutez les options suivantes à votre fichier de configuration nouvellement créé :

```javascript
{
  "singleQuote": true,
  "jsxSingleQuote": true,
  "semi": false
}
```

Ce que cela fait, c'est s'assurer que des guillemets simples sont utilisés chaque fois que possible et que les points-virgules sont introuvables (parce que, bon sang, qui aime les points-virgules...).

Comme nous l'avons fait avec notre linter, ajoutons le script suivant dans notre fichier `package.json` :

```javascript
    "format": "prettier --write ."
```

Le script exécute le formateur de code Prettier sur tous les fichiers du répertoire du projet et de ses sous-répertoires. Lorsqu'il est exécuté avec l'option `--write`, il modifie les fichiers en place, les changeant pour qu'ils se conforment aux règles de Prettier pour l'indentation, la longueur des lignes et autres options de formatage. L'argument `.` spécifie que tous les fichiers du répertoire du projet et de ses sous-répertoires doivent être formatés.

Enfin, "enlaidissons" la première ligne de notre fichier `app.jsx` comme ceci :

```javascript
import React from "react";
```

Exécutez `npm run format` et vous devriez voir la correction se faire sous vos yeux :

```javascript
import React from 'react'
```

Vous pouvez maintenant respirer facilement, ces vilains points-virgules ne reviendront pas vous hanter. ;)

Comme nous l'avons vu, la configuration de ces deux outils n'est pas si complexe, et ils aident vraiment à faciliter notre travail quotidien. ESLint nous aidera à attraper les bugs et le code inutile/redondant, et Prettier nous aidera à standardiser le format du code dans toute notre base de code.

Un autre conseil est que si vous avez un pipeline CI/CD en place, il est bon d'implémenter les scripts de linting et de formatage dans votre workflow. Cela vous aidera à garantir que chaque déploiement est à la fois automatiquement linté et formaté.

Si vous n'êtes pas familier avec le CI/CD ou la configuration d'un pipeline, j'ai récemment écrit [un article à ce sujet](https://www.freecodecamp.org/news/what-is-ci-cd/). ;)

# Conclusion

Les linters et les formateurs de code sont des outils puissants qui peuvent grandement bénéficier aux développeurs web.

Les linters aident à détecter les bugs et les problèmes potentiels avant qu'ils ne deviennent des problèmes sérieux, et encouragent à écrire un code plus maintenable et lisible.

Les formateurs de code aident à imposer un style et un format de code cohérents, économisant du temps et réduisant les chances d'erreurs humaines.

En utilisant ces outils dans votre workflow de développement web, vous pouvez améliorer votre productivité et la qualité de votre code.

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau.

Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman). À la prochaine !

![Image](https://www.freecodecamp.org/news/content/images/2023/04/4M2n.gif align="left")