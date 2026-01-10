---
title: Qu'est-ce que YAML ? Le format de fichier YML
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-11-11T16:20:17.000Z'
originalURL: https://freecodecamp.org/news/what-is-yaml-the-yml-file-format
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-christina-morillo-1181675.jpg
tags:
- name: markup
  slug: markup
- name: Web Development
  slug: web-development
- name: YAML
  slug: yaml
seo_title: Qu'est-ce que YAML ? Le format de fichier YML
seo_desc: 'YAML is one of the most popular languages for writing configuration files.

  In this article, you will learn how YAML compares to XML and JSON - two languages
  also used for creating configuration files.

  You will also learn some of the rules and feature...'
---

YAML est l'un des langages les plus populaires pour écrire des fichiers de configuration.

Dans cet article, vous apprendrez comment YAML se compare à XML et JSON - deux langages également utilisés pour créer des fichiers de configuration.

Vous apprendrez également certaines des règles et fonctionnalités du langage, ainsi que sa syntaxe de base.

Voici ce que nous allons couvrir :

1. [Qu'est-ce que YAML ?](#questcequeyaml)
2. [XML VS JSON VS YAML - Quelles sont les différences ?](#differences)
    1. [XML](#xml)
    2. [JSON](#json)
    3. [YAML](#yaml)
3. [Fonctionnalités et règles de base de YAML](#fonctionnalitesetregles)
    1. [Comment créer un fichier YAML](#creerfichier)
    2. [Support multi-documents dans YAML](#multidocument)
    3. [Indentation dans YAML](#indentation)
    4. [Tabulations dans YAML](#tabulations)
    5. [Espaces blancs dans YAML](#espacesblancs)
    6. [Types de données explicites dans YAML](#typesdedonneesexplicites)
4. [Introduction à la syntaxe YAML](#syntaxe)
    1. [Scalaires](#scalaires)
    2. [Collections](#collections)

## Qu'est-ce que YAML ? <a name="questcequeyaml"></a>

YAML signifie **YAML** **A**in't **M**arkup **L**anguage, mais à l'origine, cela signifiait **Y**et **A**nother **M**arkup **L**anguage.

YAML est un langage de sérialisation de données lisible par l'homme, tout comme XML et JSON.

La sérialisation est un processus où une application ou un service qui a des structures de données différentes et est écrit dans un ensemble de technologies différentes peut transférer des données à une autre application en utilisant un format standard.

En d'autres termes, la sérialisation consiste à traduire, convertir et envelopper une structure de données dans un autre format.

Les données dans le nouveau format peuvent être stockées dans un fichier ou transmises à une autre application ou service via un réseau.

YAML est un format largement utilisé pour écrire des fichiers de configuration pour différents outils DevOps, programmes et applications en raison de sa syntaxe lisible par l'homme et intuitive.

## XML VS JSON VS YAML - Quelles sont les différences ? <a name="differences"></a>

XML, JSON et YAML sont tous utilisés pour créer des fichiers de configuration et transférer des données entre applications.

Chaque langage a ses avantages et ses inconvénients.

Maintenant, voyons quelques-unes des caractéristiques des trois langages. Vous verrez également un exemple de la façon dont le même code est écrit dans chaque langage pour démontrer les différences de haut niveau dans leur syntaxe.

### XML <a name="xml"></a>

XML, qui signifie Extensible Markup Language, a été introduit pour la première fois en 1996 et a été conçu pour une utilisation générale.

XML est un langage de balisage généralisé. Il offre une syntaxe structurée mais flexible et un schéma de document défini. Cela en fait un bon choix lorsque vous travaillez avec des configurations complexes qui nécessitent un format structuré et un contrôle plus fin de la validation du schéma pour garantir que les configurations ont toujours le format correct.

Cela dit, la syntaxe de XML peut être verbeuse, redondante et plus difficile à lire en comparaison avec d'autres langages de sérialisation.

```xml
<Employees>
    <Employee> 
        <name> John Doe </name>
        <department> Engineering </department>
        <country> USA </country>
    </Employee>
     <Employee> 
        <name> Kate Kateson </name>
        <department> IT Support </department>
        <country> United Kingdom </country>
    </Employee>
</Employees>
```

### JSON <a name="json"></a>

JSON signifie JavaScript Object Notation et existe depuis le début des années 2000.

JSON a été initialement inspiré par le langage de programmation JavaScript, mais il n'est pas lié à un seul langage. Au lieu de cela, il s'agit d'un format indépendant du langage.

La plupart des langages de programmation modernes disposent de bibliothèques pour analyser et générer des données JSON.

JSON offre une syntaxe beaucoup plus lisible, conviviale, compacte et simple par rapport à XML. Il constitue un excellent format pour stocker et transférer des informations entre des applications web et des serveurs via un réseau.

Cela dit, il peut ne pas offrir le meilleur support pour les configurations complexes.

```json
{
	"Employees": [
    {
			"name": "John Doe",
			"department": "Engineering",
			"country": "USA"
		},

		{
			"name": "Kate Kateson",
			"department": "IT support",
			"country": "United Kingdom"
		}
	]
}
```

### YAML <a name="yaml"></a>

YAML, initialement connu sous le nom de Yet Another Markup Language, a été créé en 2001 mais signifie maintenant YAML Ain't Markup Language.

YAML est un sur-ensemble strict officiel de JSON malgré son apparence très différente de JSON.

YAML peut faire tout ce que JSON peut faire et plus encore. Un fichier YAML valide peut contenir du JSON, et JSON peut se transformer en YAML.

YAML possède la syntaxe la plus lisible par l'homme, intuitive et compacte pour définir des configurations par rapport à XML et JSON.

YAML utilise l'indentation pour définir la structure dans le fichier, ce qui est utile si vous êtes habitué à écrire du code Python et que vous êtes familier avec le style d'indentation utilisé par le langage.

Cela dit, si vous ne respectez pas l'indentation et le format, cela peut entraîner des erreurs de validation, ce qui le rend moins convivial pour les débutants.

```yaml
Employees:
- name: John Doe
  department: Engineering
  country: USA
- name: Kate Kateson
  department: IT support
  country: United Kingdom
```

## Fonctionnalités et règles de base de YAML <a name="fonctionnalitesetregles"></a>

Maintenant, passons en revue certaines des règles et fonctionnalités de base du langage.

### Comment créer un fichier YAML <a name="creerfichier"></a>

Pour créer un fichier YAML, utilisez soit l'extension de fichier `.yaml` ou `.yml`.

### Support multi-documents dans YAML <a name="multidocument"></a>

Avant d'écrire du code YAML, vous pouvez ajouter trois tirets (`---`) au début du fichier :

```yaml
---
Employees:
- name: John Doe
  department: Engineering
  country: USA
- name: Kate Kateson
  department: IT support
  country: United Kingdom
```

YAML vous permet d'avoir plusieurs documents YAML dans un seul fichier YAML, ce qui facilite grandement l'organisation des fichiers.

Séparez chaque document avec trois tirets (`---`) :

```yaml
---
Employees:
- name: John Doe
  department: Engineering
  country: USA
- name: Kate Kateson
  department: IT support
  country: United Kingdom
---
Fruit:
 - Oranges
 - Pears
 - Apples
```

Vous pouvez également utiliser trois points (`...`) pour marquer la fin du document :

```yaml
---
Employees:
- name: John Doe
  department: Engineering
  country: USA
- name: Kate Kateson
  department: IT support
  country: United Kingdom
...
```

### Indentation dans YAML <a name="indentation"></a>

Dans YAML, l'accent est mis sur l'indentation et la séparation des lignes pour désigner les niveaux et la structure des données. Le système d'indentation est assez similaire à celui utilisé par Python.

YAML n'utilise pas de symboles tels que des accolades, des crochets ou des balises d'ouverture ou de fermeture - juste l'indentation.

### Tabulations dans YAML <a name="tabulations"></a>

YAML ne vous permet pas d'utiliser des tabulations lors de la création d'indentations - utilisez des espaces à la place.

### Espaces blancs dans YAML <a name="espacesblancs"></a>

Les espaces blancs n'ont pas d'importance tant que les éléments enfants sont indentés à l'intérieur de l'élément parent.

### Comment écrire un commentaire dans YAML <a name="commentaire"></a>

Pour ajouter un commentaire afin de commenter une ligne de code, utilisez le caractère `#` :

```yaml
---
# Employees in my company
Employees:
- name: John Doe
  department: Engineering
  country: USA
- name: Kate Kateson
  department: IT support
  country: United Kingdom
```

### Types de données explicites dans YAML <a name="typesdedonneesexplicites"></a>

Bien que YAML détecte automatiquement les types de données dans un fichier, vous pouvez spécifier le type de données que vous souhaitez utiliser.

Pour spécifier explicitement le type de données, utilisez le symbole `!!` et le nom du type de données avant la valeur :

```yaml
# parse this value as a string
date: !!str 2022-11-11

## parse this value as a float (it will be 1.0 instead of 1)
fave_number: !!float 1
```

## Introduction à la syntaxe YAML <a name="syntaxe"></a>

### Scalaires <a name="scalaires"></a>

Les scalaires dans YAML sont les données sur la page - chaînes de caractères, nombres, booléens et nuls.

Voyons quelques exemples de la façon d'utiliser chacun d'eux.

Dans YAML, les chaînes de caractères peuvent dans certains cas être laissées sans guillemets, mais vous pouvez également les entourer de guillemets simples (`' '`) ou doubles (`" "`) :

```yaml
A string in YAML!

'A string in YAML!'

"A string in YAML!"
```

Si vous souhaitez écrire une chaîne de caractères qui s'étend sur plusieurs lignes et que vous souhaitez conserver les sauts de ligne, utilisez le symbole pipe (`|`) :

```yaml
|
 I am message that spans multiple lines
 I go on and on across lines
 and lines
 and more lines
```

Assurez-vous que le message est indenté !

Alternativement, si vous avez une chaîne de caractères dans un fichier YAML qui s'étend sur plusieurs lignes pour une meilleure lisibilité, mais que vous souhaitez que l'analyseur l'interprète comme une chaîne de caractères sur une seule ligne, vous pouvez utiliser le caractère `>`, qui remplacera chaque saut de ligne par un espace :

```yaml
>
 I am message that spans
 multiple lines
 but I will be parsed
 on one line
```

Encore une fois, assurez-vous de ne pas oublier d'indenter le message !

Les nombres expriment des données numériques, et dans YAML, ceux-ci incluent les entiers (nombres entiers), les flottants (nombres avec un point décimal), les exponentielles, les octaux et les hexadécimaux :

```yaml
# integer
19

# float 
8.7

# exponential
4.5e+13

# octal 
0o23

# hexadecimal
0xFF
```

Les booléens dans YAML, et dans d'autres langages de programmation, ont l'un des deux états et sont exprimés avec soit `true` soit `false`.

Les mots comme `true` et `false` sont des mots-clés dans YAML, donc ne les entourez pas de guillemets si vous voulez qu'ils soient interprétés comme des booléens.

Enfin, les valeurs nulles sont exprimées avec le mot-clé `null` ou le caractère tilde, `~`.

### Collections <a name="collections"></a>

Plus souvent qu'autrement, vous n'écrirez pas de simples scalaires dans vos fichiers YAML - vous utiliserez des collections à la place.

Les collections dans YAML peuvent être :

- Séquences (listes/tableaux)
- Mappages (dictionnaires/hachages)

Pour écrire une séquence, utilisez un tiret (`-`) suivi d'un espace :

```yaml
- HTML
- CSS
- JavaScript
```

Chaque élément de la séquence (liste) est placé sur une ligne séparée, avec un tiret devant la valeur.

Et chaque élément de la liste est au même niveau.

Cela dit, vous pouvez créer une séquence imbriquée (rappelez-vous, utilisez des espaces - pas des tabulations - pour créer les niveaux d'indentation) :

```yaml
- HTML
- CSS
- JavaScript
 - React
 - Angular
 - Vue
```

Dans la séquence ci-dessus, `React, Angular et Vue` sont des sous-éléments de l'élément `JavaScript`.

Les mappages vous permettent de lister des clés avec des valeurs. Les paires clé/valeur sont les éléments de base des documents YAML.

Utilisez un deux-points (`:`) suivi d'un espace pour créer des paires clé/valeur :

```yaml
Employees:
 name: John Doe
 age: 23
 country: USA
```

Dans l'exemple ci-dessus, un nom est attribué à une valeur spécifique.

La valeur `John Doe` est mappée (ou attribuée) à la clé `name`, la valeur `23` est mappée à la clé `age`, et la valeur `USA` est mappée à la clé `country`. Ensemble, celles-ci créent un objet.

Vous pouvez également utiliser un mappage avec une séquence.

Par exemple, en reprenant la séquence d'exemple précédente, voici comment vous construiriez une liste de `frontend_languages` :

```yaml
frontend_languages:
 - HTML
 - CSS
 - JavaScript
  - React
  - Angular
  - Vue
```

Dans l'exemple ci-dessus, j'ai créé une liste de `frontend_languages`, où il y a plusieurs valeurs sous la même clé, `frontend_languages`.

De même, vous pouvez créer une liste d'objets :

```yaml
Employees:
- name: John Doe
  department: Engineering
  country: USA
- name: Kate Kateson
  department: IT support
  country: United Kingdom
```

## Conclusion

Espérons que cet article a été utile et vous a donné un aperçu de ce qu'est YAML, à quoi ressemble la syntaxe du langage et comment il diffère de XML et JSON.

Merci d'avoir lu, et bon codage !