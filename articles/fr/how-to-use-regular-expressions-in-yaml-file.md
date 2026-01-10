---
title: Comment utiliser les expressions régulières dans un fichier YAML – Tutoriel
  RegEx en YAML
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-05-17T14:48:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-regular-expressions-in-yaml-file
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/yamlRe.png
tags:
- name: Regex
  slug: regex
- name: Regular Expressions
  slug: regular-expressions
- name: YAML
  slug: yaml
seo_title: Comment utiliser les expressions régulières dans un fichier YAML – Tutoriel
  RegEx en YAML
seo_desc: 'YAML does not have built-in support for regular expressions. But you can
  still include regex patterns as part of a YAML file''s contents, access those patterns,
  and create a regex out of them.

  You can do this, for example, with the JavaScript RegExp c...'
---

YAML ne prend pas en charge les expressions régulières de manière native. Mais vous pouvez toujours inclure des motifs regex dans le contenu d'un fichier YAML, accéder à ces motifs et créer une regex à partir de ceux-ci.

Vous pouvez le faire, par exemple, avec le constructeur JavaScript `RegExp`.

Ainsi, dans YAML, les expressions régulières sont généralement représentées sous forme de chaînes de caractères, en utilisant une syntaxe spécifique pour définir le motif. Par exemple, une paire clé-valeur YAML qui inclut un motif d'expression régulière pourrait ressembler à ceci :

```bash
exemple :
motif : ^[A-Za-z]+$
```

Dans cet article, je vais vous montrer comment écrire des expressions régulières dans un fichier YAML et accéder à ses entrées dans un fichier JavaScript. Commençons par examiner ce qu'est un fichier YAML.

## Ce que nous allons couvrir

* [Qu'est-ce qu'un fichier YAML ?](#heading-quest-ce-quun-fichier-yaml)

* [Comment écrire des expressions régulières dans un fichier YAML](#heading-comment-ecrire-des-expressions-regulieres-dans-un-fichier-yaml)

* [Comment importer un fichier YAML en JavaScript et l'utiliser](#heading-comment-importer-un-fichier-yaml-en-javascript-et-lutiliser)

* [Conclusion](#heading-conclusion)

## Qu'est-ce qu'un fichier YAML ?

YAML signifie YAML n'est pas un langage de balisage. C'est un format de fichier de sérialisation de données lisible par les humains et les machines. Il est souvent utilisé comme fichiers de configuration, pour l'échange de données et pour représenter des données structurées en ingénierie DevOps.

Les fichiers YAML utilisent l'indentation et une syntaxe concise pour définir des structures de données telles que des listes, des dictionnaires (paires clé-valeur) et des scalaires (chaînes de caractères, nombres, booléens).

Chaque entrée dans un fichier YAML peut être une chaîne de caractères, un nombre ou un booléen, et d'autres types de données spécifiques à YAML comme les scalaires et les listes. Voici un fichier YAML contenant ces types de données :

```bash
# Exemple de types de données YAML
# -----------------------------

# Scalaires
null_exemple : null           # Scalaire Null
bool_exemple : true           # Scalaire Booléen
int_exemple : 42              # Scalaire Entier
float_exemple : 3.14          # Scalaire Flottant
str_exemple : "Bonjour, YAML !"  # Scalaire Chaîne de caractères

# Séquences (Tableaux)
seq_exemple :                 # Séquence (Tableau)
  - Pomme
  - Orange
  - Banane

# Mappages (Dictionnaires)
map_exemple :                 # Mappage (Dictionnaire)
  clé1 : valeur1
  clé2 : valeur2
  clé3 : valeur3

# Liste (Séquence de Mappages)
list_exemple :                # Liste de Mappages (Séquence de Dictionnaires)
  - nom : John
    âge : 30
  - nom : Jane
    âge : 28
  - nom : Bob
    âge : 35
```

Vous pouvez également mettre des expressions régulières directement dans un fichier YAML. Et c'est ce que nous allons examiner ensuite.

## Comment écrire des expressions régulières dans un fichier YAML

Vous pouvez représenter des valeurs spécifiques dans un fichier YAML sous forme d'expressions régulières. Voici quelques motifs regex de validation :

```bash
# fichier validator.yaml
mot_de_passe :
  motif : ^(?!.*[\s])(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$
  description : |
    - Au moins 8 caractères
    - Au moins une lettre majuscule
    - Au moins une lettre minuscule
    - Au moins un chiffre
    - Caractères spéciaux autorisés : @$!%*#?&

numeroTelephoneNigerian :
  motif : ^(\+?234|0)[789]\d{9}$
  description : |
    - Format de numéro de téléphone nigérian
    - Commence par +234 ou 0
    - Suivi de 7, 8 ou 9
    - Total de 11 chiffres

email :
  motif : ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
  description : |
    - Format d'adresse email valide
    - Exemple : exemple@exemple.com

nom_utilisateur :
  motif : ^[a-zA-Z0-9_-]{3,16}$
  description : |
    - Caractères autorisés : lettres (majuscules et minuscules), chiffres, souligné (_) et trait d'union (-)
    - Longueur minimale : 3 caractères
    - Longueur maximale : 16 caractères
```

Vous pouvez ensuite importer le fichier YAML dans votre fichier JavaScript et faire ce que vous voulez avec – par exemple, créer des expressions régulières à partir de ces motifs et les utiliser.

Mais ce processus n'est pas simple. C'est donc la prochaine chose que vous allez apprendre dans cet article.

## Comment importer un fichier YAML en JavaScript et l'utiliser

Si vous essayez d'importer un fichier YAML dans un fichier JavaScript avec la syntaxe `import`, comme `import abc from file.yaml`, vous obtiendrez ce type d'erreur :

![reYamlErr](https://www.freecodecamp.org/news/content/images/2023/05/reYamlErr.png align="left")

Au lieu de faire cela, vous devriez créer un `package.json` dans votre répertoire de projet en exécutant `npm init -y` et installer le package `js-yaml` en exécutant `npm install js-yaml`.

Après cela, importez le module `fs` de Node.js et le package `js-yaml` de cette manière :

```js
const fs = require('fs');
const yaml = require('js-yaml');
```

La prochaine chose à faire est de lire le fichier `validator.yaml` avec la méthode `readFileSync` du module `fs` et de parser le fichier YAML avec la méthode `load()` :

```js
const yamlData = fs.readFileSync('validator.yaml', 'utf8');
const parsedData = yaml.load(yamlData);
```

Il ne reste plus qu'à accéder à l'un des motifs, créer une RegEx à partir de celui-ci et l'utiliser. Voici comment j'ai utilisé le motif de mot de passe :

```js
const passwordPattern = parsedData.password.pattern;
const pwordValidator = new RegExp(passwordPattern);

const myPassword = 'reallyStrongPassword21!';
console.log(pwordValidator.test(myPassword)); //true
```

Voici comment j'ai utilisé le motif de validation de numéro de téléphone nigérian :

```js
const phonePattern = parsedData.nigerianPhoneNumber.pattern;

phoneValidator = new RegExp(phonePattern);

const myPhoneNum = '08133333333';
console.log(phoneValidator.test(myPhoneNum)); //true;
```

Voici le code complet :

```js
// importer le module fs pour pouvoir accéder au fichier YAML
const fs = require('fs');

// importer le package YAML
const yaml = require('js-yaml');

// Lire le fichier validator.yaml avec le module FS
const yamlData = fs.readFileSync('test.yaml', 'utf8');

// parser le fichier YAML
const parsedData = yaml.load(yamlData);

// Accéder au motif de validation du mot de passe depuis le fichier YAML
const passwordPattern = parsedData.password.pattern;

// Créer une regex à partir du motif de mot de passe
const pwordValidator = new RegExp(passwordPattern);

const myPassword = 'reallyStrongPassword21!';
console.log(pwordValidator.test(myPassword)); //true

// Accéder au motif de validation du numéro de téléphone nigérian depuis le fichier YAML
const phonePattern = parsedData.nigerianPhoneNumber.pattern;

// Créer une regex à partir du motif de téléphone
phoneValidator = new RegExp(phonePattern);

const myPhoneNum = '08133333333';
console.log(phoneValidator.test(myPhoneNum)); //true;

// Accéder au motif de validation de l'email depuis le fichier YAML
const emailPattern = parsedData.email.pattern;

// Créer une regex à partir du motif de téléphone
emailValidator = new RegExp(emailPattern);

const emailAddress = 'chris@gmail.com';
console.log(emailValidator.test(emailAddress)); //false;

// Accéder au motif de validation du nom d'utilisateur depuis le fichier YAML
const usernamePattern = parsedData.username.pattern;

// Créer une regex à partir du motif de téléphone
usernameValidator = new RegExp(usernamePattern);

const username = 'ksound22';
console.log(usernameValidator.test(username)); //false;
```

## Conclusion

Cet article vous a montré comment mettre des expressions régulières dans un fichier YAML, l'importer dans un fichier JavaScript avec le package `js-yaml` et accéder à l'une des valeurs qu'il contient.

Nous avons également examiné comment vous pouvez créer des expressions régulières à partir des motifs dans le fichier YAML et les tester avec certaines chaînes de caractères.

Merci d'avoir lu. Si vous trouvez l'article utile, veuillez le partager avec vos amis et votre famille.