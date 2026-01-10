---
title: Comment fonctionnent les règles de lint JavaScript (et pourquoi les arbres
  de syntaxe abstraite sont importants)
subtitle: ''
author: Tilda Udufo
co_authors: []
series: null
date: '2025-05-21T15:21:33.755Z'
originalURL: https://freecodecamp.org/news/how-javascript-lint-rules-work-and-why-abstract-syntax-trees-matter
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1747835156597/f30994d4-f4da-4100-af25-9f858c015aa8.png
tags:
- name: JavaScript
  slug: javascript
- name: Linter
  slug: linter
- name: ast
  slug: ast
- name: React
  slug: reactjs
seo_title: Comment fonctionnent les règles de lint JavaScript (et pourquoi les arbres
  de syntaxe abstraite sont importants)
seo_desc: Before I started to contribute to eslint-plugin-react, I didn’t think too
  deeply about the linters I used every day while writing code. Like many developers,
  I installed them at the start of a project, appreciated the red underlines or auto-fixes,
  an...
---

Avant de commencer à contribuer à [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react/), je ne réfléchissais pas trop profondément aux linters que j'utilisais tous les jours en écrivant du code. Comme beaucoup de développeurs, je les installais au début d'un projet, j'appréciais les soulignements rouges ou les corrections automatiques, et je passais à autre chose.

Mais derrière ces messages utiles se cache un système puissant de règles et de structure que la plupart d'entre nous explorent rarement.

Les linters sont partout - à travers les langages, les frameworks et les flux de travail. Ils aident à attraper les erreurs, à imposer un formatage cohérent et à promouvoir les meilleures pratiques. Ils font partie des premiers outils que nous installons dans un nouveau projet, et pourtant, ils sont aussi parmi les plus sous-estimés et les moins compris.

Dans cet article, je vais vous emmener sous le capot. Nous allons voir comment fonctionnent les règles de lint JavaScript, pourquoi les AST (Abstract Syntax Trees) sont si importants, et comment vous pouvez utiliser cette compréhension pour écrire ou contribuer à un linter vous-même.

## 📚 Table des matières

* [Qu'est-ce qu'un Linter ?](#heading-quest-ce-quun-linter)

* [Du Code à l'Arbre : Entrée de l'AST](#heading-du-code-a-larbre-entree-de-last)

* [Pourquoi les AST sont Importants pour le Linting](#heading-pourquoi-les-ast-sont-importants-pour-le-linting)

* [Comment ESLint Utilise les AST Sous le Capot](#heading-comment-eslint-utilise-les-ast-sous-le-capot)

* [Anatomie d'une Règle de Lint](#heading-anatomie-dune-regle-de-lint)

* [Outils Utiles pour Explorer les AST](#heading-outils-utiles-pour-explorer-les-ast)

* [Conclusion : Pourquoi Vous Devriez Comprendre Cela](#heading-conclusion-pourquoi-vous-devriez-comprendre-cela)

## 🧹 Qu'est-ce qu'un Linter ?

Un linter est un outil qui analyse automatiquement votre code pour signaler les erreurs, imposer des règles de style et attraper les bugs potentiels. Pensez-y comme le Grammarly du monde du codage - il vous aide à écrire un code plus propre et plus cohérent en pointant les problèmes tôt.

Un exemple populaire est [ESLint](https://eslint.org/), un linter open-source pour JavaScript et TypeScript qui vérifie le code pour les problèmes et peut même corriger automatiquement certains d'entre eux.

Les linters sont souvent :

* Intégrés dans votre éditeur de texte ou IDE

* Exécutés dans le cadre d'un pipeline CI ou d'un hook pre-commit

* Utilisés avec des formatteurs comme Prettier pour une cohérence encore plus stricte

Mais comment décident-ils ce qu'il faut signaler comme un problème ? C'est là que les **règles de lint** entrent en jeu.

### 🧱 Règles de Lint : Le Cerveau Derrière le Linter

Les règles de lint sont les éléments de base de tout linter. Chaque règle définit :

1. **Ce qu'il faut chercher** : un motif spécifique dans votre code.

2. **Ce qu'il faut faire à ce sujet** : un avertissement, une erreur ou une correction automatique.

Il existe de nombreux types de règles, souvent regroupés en catégories comme :

* **Prévention des erreurs** : Attraper les bugs, comme l'utilisation de variables non déclarées.

* **Style de code** : Imposer un formatage et des conventions de nommage cohérents.

* **Meilleures pratiques** : Encourager des motifs de codage plus sûrs ou plus lisibles.

* **Sécurité** : Signaler le code risqué, comme les appels directs à `eval()` ou les regex non sécurisées.

Si vous avez déjà vu un message ESLint comme celui-ci :

```bash
Unexpected console.log

Missing semicolon

'myVar' is assigned a value but never used
```

... vous avez vu des règles de lint en action.

Ils ne sont pas juste des "policiers de style". Les linters aident à réduire la charge mentale en attrapant les petits problèmes tôt, afin que vous puissiez vous concentrer sur le tableau d'ensemble de ce que votre code essaie de faire.

## 🌳 Du Code à l'Arbre : Entrée de l'AST

Pour comprendre comment fonctionnent les règles de lint sous le capot, nous devons parler de l'**Abstract Syntax Tree (AST)** - la structure de données au cœur de chaque linter.

Un AST est une représentation structurée et arborescente de votre code. Au lieu de lire votre code comme du texte brut, un linter le convertit en un arbre où chaque partie de votre code (une variable, une chaîne, une fonction, etc.) devient un **nœud** dans l'arbre.

Voici un exemple.

Collez ce code dans [AST Explorer](https://astexplorer.net/), un outil qui vous permet de visualiser l'AST pour le code en temps réel :

```javascript
const name = "Tilda";
```

Définissez le langage sur **JavaScript**, et choisissez l'un des parseurs ESLint comme **Espree**. Vous verrez quelque chose comme ceci dans le panneau de droite :

![AST (Abstract Syntax Tree) montrant un nœud VariableDeclaration pour une déclaration de constante. À l'intérieur se trouve un VariableDeclarator qui assigne un nœud Literal avec la valeur de chaîne 'Tilda' à un Identifier nommé 'name'.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747767760645/7929c578-7558-4a1b-8aa6-ed30399b090b.png align="center")

Dans l'image ci-dessus de AST Explorer, vous pouvez voir comment l'arbre est structuré :

* **Programme :**

  * Le nœud racine de l'AST. Il enveloppe l'ensemble du code.

  * Contient un `body`, qui est un tableau de déclarations.

* **VariableDeclaration**

  * Type : `"VariableDeclaration"`

  * Représente une déclaration utilisant le mot-clé `const`.

  * A un `kind` de `"const"` et une liste de `declarations`.

* **VariableDeclarator**

  * Type : `"VariableDeclarator"`

  * Représente une seule variable en cours de déclaration.

  * Contient deux parties clés :

    * **Identifier**

      * Type : `"Identifier"`

      * Nom : `"name"`

      * Il s'agit de la variable en cours de déclaration.

    * **Literal**

      * Type : `"Literal"`

      * Valeur : `"Tilda"`

      * Il s'agit de la chaîne assignée à la variable.

Cette imbrication est ce qui rend la structure **"arborescente"**. Chaque nœud est un parent pour des morceaux plus petits (ses enfants), ce qui aide les linters à naviguer dans le code de manière fiable.

Ainsi, tandis que vos yeux voient une courte ligne de JavaScript, le linter voit une carte détaillée de ce que cette ligne *signifie* structurellement. Cette hiérarchie permet à des outils comme ESLint de pointer exactement quel type de code est utilisé - et où - afin que les règles puissent cibler des motifs comme :

* "Signaler toutes les variables `const`"

* "Avertir lorsqu'une variable est nommée `name`"

* "Interdire les chaînes codées en dur comme `Tilda`"

## 🤖 Pourquoi les AST sont Importants pour le Linting

Maintenant, voici l'idée clé : les règles de lint ne fonctionnent pas en lisant votre code comme du texte. Elles fonctionnent en faisant correspondre des motifs de nœuds spécifiques dans l'AST.

Cela compte beaucoup car il existe des dizaines de façons d'écrire la même logique en JavaScript. Prenons deux versions de la même logique : l'une écrite comme une **déclaration de fonction**, et l'autre comme une **fonction fléchée**.

```javascript
function greet() {
  return "hello";
}

const greet = () => "hello";
```

À première vue, elles semblent différentes. Mais lorsque nous examinons leurs AST, nous voyons que les deux suivent des motifs structurels similaires. C'est ce qui permet à un linter de reconnaître ce que votre code fait, peu importe comment il est écrit.

### 🌳 L'Arbre Derrière la Déclaration de Fonction

![Abstract Syntax Tree (AST) montrant un nœud FunctionDeclaration avec un Identifier pour le nom de la fonction. La fonction contient un BlockStatement avec un nœud ReturnStatement. À l'intérieur du ReturnStatement se trouve un nœud Literal retournant la chaîne 'hello'](https://cdn.hashnode.com/res/hashnode/image/upload/v1747766773571/dfe619ca-d3a4-43a6-9018-c31e4abc6ed8.png align="center")

Voici ce que ESLint voit dans l'arbre AST lorsque vous écrivez une déclaration de fonction :

* Il commence par un nœud `FunctionDeclaration`.

* Ce nœud contient :

  * Un `Identifier` (le nom de la fonction : `greet`)

  * Un `BlockStatement` représentant le corps de la fonction

  * À l'intérieur du `BlockStatement`, il y a un `ReturnStatement`

  * Le `ReturnStatement` retourne un `Literal` — la chaîne `"hello"`

### 🌳 L'Arbre Derrière la Fonction Fléchée

![Abstract Syntax Tree (AST) montrant un nœud VariableDeclaration pour une fonction fléchée const. À l'intérieur se trouve un VariableDeclarator assignant une ArrowFunctionExpression à un identifier. L'ArrowFunctionExpression contient un body avec un nœud Literal retournant la chaîne 'hello'.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747766822908/4723a1e9-c616-4b0d-bdde-ccf1f1cd6b0d.png align="center")

Voici ce que ESLint voit lorsque vous écrivez la même logique en utilisant une fonction fléchée :

* Un `VariableDeclaration` avec `kind: "const"`

  * À l'intérieur, un `VariableDeclarator`, qui assigne une valeur à la variable `greet`

  * La valeur est une `ArrowFunctionExpression`

  * Le corps de la fonction fléchée est un `Literal` — la chaîne `"hello"`

Même si la syntaxe est différente, les deux chemins mènent finalement à un **nœud Literal** contenant `"hello"` — ce qui est tout ce que votre linter doit prendre en compte.

### 💡 Ramenez-le à la maison avec un exemple

Imaginez que votre équipe a une règle : les fonctions ne devraient pas retourner de chaînes codées en dur comme `"hello"`. Vous voulez un linter qui signale cela.

Avec les AST, vous pouvez écrire **une règle de lint** qui correspond à un `ReturnStatement` ou à une `ArrowFunctionExpression` dont le corps est un `Literal`.

Voici l'idée de base :

```javascript
ReturnStatement(node) {
  if (node.argument?.type === "Literal" && node.argument.value === "hello") {
    context.report({ node, message: "Évitez de retourner des chaînes statiques 'hello'." });
  }
}
```

Et pour les fonctions fléchées avec des corps d'expression :

```javascript
ArrowFunctionExpression(node) {
  if (node.body?.type === "Literal" && node.body.value === "hello") {
    context.report({ node, message: "Évitez de retourner des chaînes statiques 'hello'." });
  }
}
```

Même si les styles de code sont différents, la **structure de l'AST est suffisamment similaire** pour que les deux fonctions déclenchent la règle, car le linter ne regarde pas comment le code est écrit, seulement ce que la structure de l'AST est réellement.

C'est ce qui rend les AST si utiles : ils permettent aux linters d'ignorer les différences de surface et de se concentrer sur la signification et la structure réelles de votre code. En conséquence, vous pouvez écrire des règles plus intelligentes et plus flexibles qui attrapent des motifs à travers différents styles, peu importe comment quelqu'un a écrit son JavaScript.

## 🔨 Comment ESLint utilise les AST sous le capot

ESLint s'appuie sur un format standardisé appelé [ESTree (ECMAScript Tree)](https://github.com/estree/estree) pour représenter le code JavaScript sous forme d'Arbre de Syntaxe Abstraite (AST). ESTree n'est pas un parseur en soi - c'est une spécification qui définit comment le code JavaScript doit être représenté sous forme d'arbre. Cela permet à ESLint (et à des outils similaires) de comprendre le code de manière cohérente et structurée.

Lorsque vous exécutez ESLint sur votre code, voici ce qui se passe sous le capot :

### **1. Votre Code est Parsé en un AST**

ESLint convertit votre code en un AST qui suit le format ESTree. Cet arbre est composé de nœuds, chacun représentant une partie de votre code (comme une variable, une fonction ou une expression). La structure résultante est ce que chaque règle de lint analysera.

### **2. Les Règles de Lint "S'abonnent" à des Types de Nœuds Spécifiques**

Chaque règle de lint indique à ESLint quels **types de nœuds** elle souhaite écouter. Par exemple, une règle peut se soucier de :

* `Identifier`

* `CallExpression`

* `VariableDeclaration`

Ces types de nœuds correspondent à la structure que vous verriez dans des outils comme AST Explorer.

### **3. ESLint Parcourt l'Arbre et Déclenche les Règles**

ESLint parcourt l'AST, visitant un nœud à la fois. Lorsqu'il atteint un type de nœud auquel une règle s'est abonnée, il déclenche la fonction correspondante dans cette règle.

Ce processus est efficace et déclaratif, vous n'avez pas à vous soucier de scanner manuellement chaque ligne de code. ESLint fait le parcours, votre règle se contente d'écouter.

### **4. Les Règles Inspectent les Nœuds et Signalent les Problèmes**

À l'intérieur de chaque règle, vous recevez le nœud que ESLint a passé. Vous pouvez examiner ses propriétés - comme le nom, la valeur ou la structure environnante - et décider s'il viole le motif que vous avez prévu.

Si c'est le cas, vous utilisez `context.report()` pour dire à ESLint de le signaler comme un problème. ESLint peut également corriger le problème automatiquement si vous fournissez une fonction `fix()` à l'intérieur de `context.report()`.

```javascript
context.report({
 a0 a0 a0 a0node: node,
 a0 a0 a0 a0message: "Point-virgule manquant".
 a0 a0 a0 a0fix: function(fixer) {
 a0 a0 a0 a0    return fixer.insertTextAfter(node, ";");
 a0 a0 a0 a0}
});
```

## 🥻 Anatomie d'une Règle de Lint

Examinons une règle ESLint personnalisée très simple. Celle-ci signale toute variable nommée `any` :

```javascript
module.exports = {
 a0 a0meta: {
 a0 a0 a0 a0type: "problem",
 a0 a0 a0 a0docs: {
 a0 a0 a0 a0 a0 a0description: "Interdire les variables nommées 'any'",
 a0 a0 a0 a0},
 a0 a0},

 a0 a0create(context) {
 a0 a0 a0 a0return {
 a0 a0 a0 a0 a0 a0Identifier(node) {
 a0 a0 a0 a0 a0 a0 a0 a0if (node.name === 'any') {
 a0 a0 a0 a0 a0 a0 a0 a0 a0 a0context.report({
 a0 a0 a0 a0 a0 a0 a0 a0 a0 a0 a0 a0node,
 a0 a0 a0 a0 a0 a0 a0 a0 a0 a0 a0 a0message: "N'utilisez pas 'any' comme nom de variable."
 a0 a0 a0 a0 a0 a0 a0 a0 a0 a0});
 a0 a0 a0 a0 a0 a0 a0 a0}
 a0 a0 a0 a0 a0 a0}
 a0 a0 a0 a0};
 a0 a0}
};
```

🔎 **Ce qui se passe ici :**

* La section meta fournit des informations sur la règle (utilisées dans la documentation et les outils ESLint).

* La fonction `create()` définit les types de nœuds que la règle écoute.

* `Identifier(node)` est déclenchée chaque fois qu'un identifiant est trouvé dans le code.

* Si le nom de l'identifiant est `any`, la règle appelle `context.report()` pour lever un avertissement.

## **🛠 Outils Utiles pour Explorer les AST**

Comprendre les AST peut sembler abstrait au début, mais certains outils rendent la courbe d'apprentissage beaucoup plus douce. Ceux-ci sont particulièrement utiles lorsque vous essayez de visualiser comment votre code se traduit en structures arborescentes, ou lorsque vous déboguez une règle personnalisée.

### **1.** [**AST Explorer**](https://astexplorer.net/)

C'est l'outil le plus convivial pour les débutants et le plus puissant pour travailler avec les AST. Vous pouvez :

* Coller n'importe quel code JavaScript

* Choisir un parseur compatible ESLint (comme Espree)

* Voir instantanément la structure AST du côté droit

* Survoler les nœuds de l'arbre et voir comment ils correspondent à des parties spécifiques de votre code

Si vous écrivez une règle personnalisée, AST Explorer deviendra probablement votre meilleur ami. Il vous aide à déterminer exactement quel type de nœud vous devez cibler et quelles propriétés sont disponibles sur ce nœud.

### **2. Exemples de Règles et Tests ESLint**

Parfois, la meilleure façon d'apprendre est de lire du code réel. Les règles de base d'ESLint (ou les règles de plugins populaires comme [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react/)) incluent :

* Définitions de règles

* Fichiers de test montrant le code qui **devrait** et **ne devrait pas** déclencher la règle

* Exemples de corrections (si la règle est corrigible automatiquement)

Parcourir ceux-ci vous aide à comprendre comment les règles du monde réel sont structurées et comment la configuration des tests fonctionne.

Conseil : Regardez dans les dossiers `tests/lib/rules/` ou `lib/rules/` des dépôts ESLint ou des plugins.

### **3. Documentation d'ESLint**

ESLint dispose d'une documentation complète sur le travail avec les règles :

* [ESLint : Travailler avec les Règles](https://archive.eslint.org/docs/2.0.0/developer-guide/working-with-rules)

* [ESLint : Règles Personnalisées](https://eslint.org/docs/latest/extend/custom-rules)

## ** 2705 Conclusion : Pourquoi Vous Devriez Comprendre Cela**

Comprendre comment fonctionnent les AST vous donne des superpouvoirs lorsqu'il s'agit de personnaliser et de contribuer aux outils de linting. Que vous essayiez d'imposer un motif spécifique dans la base de code de votre équipe ou que vous souhaitiez contribuer à un plugin comme [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react/), cette connaissance vous aidera à :

* 🔧 **Contribuer aux règles existantes** en comprenant ce qu'elles vérifient et comment

* 🐛 **Déboguer les comportements de linter déroutants** lorsque les règles se déclenchent de manière inattendue (ou pas du tout)

* 🛠 **Écrire vos propres règles personnalisées** pour imposer des normes de codage spécifiques, des conventions de projet ou des meilleures pratiques

Vous n'avez pas besoin d'être un expert en compilateurs ou de comprendre pleinement chaque type de nœud dans la spécification. Vous devez simplement reconnaître les motifs, explorer les arbres et vous familiariser avec l'identification des nœuds dont votre règle se soucie.