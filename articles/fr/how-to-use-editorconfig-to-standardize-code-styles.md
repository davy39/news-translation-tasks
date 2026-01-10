---
title: Pourquoi vous devriez utiliser EditorConfig pour standardiser les styles de
  code
subtitle: ''
author: Seth Falco
co_authors: []
series: null
date: '2021-07-21T21:28:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-editorconfig-to-standardize-code-styles
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/untitled.png
tags:
- name: automation
  slug: automation
- name: configuration
  slug: configuration
- name: configuring settings
  slug: configuring-settings
- name: editor
  slug: editor
- name: Productivity
  slug: productivity
seo_title: Pourquoi vous devriez utiliser EditorConfig pour standardiser les styles
  de code
seo_desc: 'You use EditorConfig to define formatting conventions for textual files
  in a project. It''s great because it''s widely supported, and it''s not tied to
  any particular language, framework, or code editor.

  EditorConfig on its own is just a vendor-agnostic...'
---

Vous utilisez [EditorConfig](https://editorconfig.org/) pour définir des conventions de formatage pour les fichiers textuels dans un projet. C'est génial car il est largement supporté et n'est pas lié à un langage, un framework ou un éditeur de code particulier.

EditorConfig en soi n'est qu'un fichier de configuration agnostique. Il repose sur des outils tiers ou des intégrations pour implémenter le support des règles déclarées dans le fichier.

Ces règles peuvent être lues par des IDE (Environnements de Développement Intégrés), des éditeurs de code ou des outils de build pour appliquer ou imposer des conventions de formatage.

## Qu'est-ce qu'EditorConfig résout ?

Les utilisateurs configurent généralement les paramètres de style de code dans un éditeur selon *leurs* préférences. Malheureusement, leurs préférences ne correspondent probablement pas aux vôtres.

Que se passe-t-il lorsqu'ils contribuent à un projet partagé ? Il peut s'agir d'un projet au travail ou d'un projet open-source sur GitLab ou GitHub.

Les paramètres de style de l'utilisateur sont appliqués aux fichiers qu'il modifie. Cela peut entraîner des projets incohérents ou désordonnés, avec certains ou tous les problèmes suivants :

* Utilisation mixte de tabulations et d'espaces.

* Utilisation mixte de fins de ligne. (Généralement pas un problème significatif avec [Git](https://git-scm.com/).)

* Les fichiers peuvent ne pas avoir l'encodage de caractères souhaité.

* Différentes tailles d'indentation dans les fichiers.

Sans cohérence, le code peut paraître désordonné et être difficile à lire, selon l'environnement de développement de l'utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/3.png align="left")

[*eclipse.jdt.ls*](https://github.com/eclipse/eclipse.jdt.ls/blob/master/org.eclipse.jdt.ls.core/src/org/eclipse/jdt/ls/core/internal/EventNotification.java?ts=8) *mélange les tabulations et les espaces, voici comment cela apparaît sur GitHub avec une taille de tabulation de 8.*

Une solution courante consiste à partager les paramètres de l'éditeur dans le cadre du projet, mais cela suppose que tous les contributeurs utilisent le même éditeur que vous, ce qui n'est probablement pas le cas.

Pour le développement Java seul, les choix suivants sont tous populaires :

* [Visual Studio Code](https://code.visualstudio.com/) (Ce que j'utilise !)

* [Eclipse](https://www.eclipse.org/)

* [IntelliJ](https://www.jetbrains.com/idea/)

* [NetBeans](https://netbeans.apache.org/)

Vous allez alourdir votre projet avec des fichiers sans rapport si vous ajoutez la configuration pour chaque éditeur que quelqu'un pourrait utiliser.

Alors, pourquoi ne pas utiliser une solution agnostique où les éditeurs sont responsables de l'utilisation d'une configuration partagée ?

## Comment EditorConfig aide

Définir des conventions aide tout le monde tout au long du cycle de vie d'un projet. Il y a notamment trois façons dont cela fait gagner du temps.

### EditorConfig rend le code plus lisible

Rendre le code plus lisible est de loin la raison la plus importante de l'utiliser. Cela améliore la maintenabilité du projet et la vitesse à laquelle les gens peuvent travailler.

> « En effet, le rapport entre le temps passé à lire et à écrire est bien supérieur à 10 contre 1. Nous lisons constamment l'ancien code dans le cadre de l'effort pour écrire un nouveau code... Par conséquent, le rendre facile à lire le rend plus facile à écrire. »
> — Robert C. Martin

Il y a de nombreuses autres raisons pour lesquelles quelqu'un pourrait lire le code en dehors du développement :

* Les chercheurs qui doivent mieux comprendre comment le projet fonctionne.

* Les analystes de sécurité qui vérifient les vulnérabilités.

* Les rédacteurs techniques qui documentent le comportement de l'application.

Les gens pourront accomplir leur rôle plus efficacement si votre code est maintenu propre, cohérent et lisible.

### EditorConfig facilite les revues de code

En tant que mainteneur de projet, vous devrez inévitablement examiner le code contribué par d'autres. Il peut s'agir d'un collègue de l'équipe ou de contributeurs open-source qui découvrent votre projet.

L'application du formatage doit être déléguée à un logiciel. Cela rendra la lecture et la révision du code plus efficaces et évitera la nécessité de demander des modifications basées sur le formatage.

Réduire la boucle de rétroaction fait finalement gagner du temps à tout le monde.

### EditorConfig facilite le développement

Les développeurs peuvent éviter beaucoup de maux de tête en ayant des conventions qui sont automatiquement appliquées par leur éditeur.

Sans cela, ils doivent trouver un guide de contribution, un guide de style ou vérifier manuellement d'autres codes pour apprendre les conventions du projet.

Même lorsque les conventions sont connues, elles peuvent entrer en conflit avec les paramètres d'un développeur. Ils devront alors coder contre le formatage automatique de l'éditeur ou changer fréquemment les paramètres entre les projets.

Cela est particulièrement utile pour les développeurs qui passent souvent d'un projet à l'autre. Par exemple, les contributeurs open-source écrivent fréquemment du code pour des projets dans différentes organisations qui suivent des conventions de codage différentes.

## Comment fonctionne EditorConfig

EditorConfig utilise un simple fichier de type [INI](https://en.wikipedia.org/wiki/INI_file) nommé `.editorconfig`. Ce fichier déclare des règles qui seront traduites en paramètres dans votre éditeur ou appliqueront un formatage sur votre espace de travail.

Par exemple, dans mon éditeur, j'utilise des indentations de 2 espaces pour les fichiers XML, mais un projet auquel je contribue peut préférer des indentations de 4 espaces.

```plaintext
[*.xml]
indent_size = 4
```

Lorsque j'ouvre le projet, mon éditeur verra le fichier `.editorconfig` et remplacera les paramètres pour s'adapter aux conventions du projet.

![Instance de Visual Studio Code. Il y a un fichier XML sur le côté gauche qui utilise des espaces comme défini dans EditorConfig, mais ma taille d'indentation par défaut est de 2.](https://www.freecodecamp.org/news/content/images/2021/07/1.png align="left")

*Écriture d'un fichier XML avec mes paramètres d'éditeur par défaut. J'utilise des espaces pour l'indentation avec une taille de 2.*

![Instance de Visual Studio Code. La configuration EditorConfig inclut une section XML qui définit le style d'indentation sur tabulation et la taille à 4. Le fichier XML sur la gauche est reformatté pour refléter ce changement.](https://www.freecodecamp.org/news/content/images/2021/07/2-1.png align="left")

*Reformatage automatique du fichier après avoir remplacé les paramètres de formatage XML.*

## Comment utiliser EditorConfig

Selon votre éditeur de choix, il peut avoir un support natif pour EditorConfig. Il y a une liste d'éditeurs "[No Plugin Necessary](https://editorconfig.org/#pre-installed)" sur le site web, qui inclut les IDE JetBrains et Visual Studio.

Si votre éditeur n'a pas de support natif, vous pourrez probablement l'ajouter avec un plugin. Des éditeurs comme Visual Studio Code et Eclipse le supportent de cette manière, que vous pouvez également trouver sur le site web d'EditorConfig sous "[Download a Plugin](https://editorconfig.org/#download)".

Une fois installé, votre éditeur devrait automatiquement trouver le fichier EditorConfig dans votre projet s'il existe et commencer à appliquer les règles.

## Comment définir des règles dans EditorConfig

Vous pouvez trouver une liste de règles sur le [EditorConfig Wiki](https://github.com/editorconfig/editorconfig/wiki/EditorConfig-Properties). Il contient toutes les règles officiellement supportées, ainsi que des propositions pour des règles spécifiques à un domaine qui peuvent être supportées par certaines implémentations.

Toutes les implémentations ne supportent pas toutes les règles. Cela est particulièrement vrai pour les règles spécifiques à un domaine comme `curly_bracket_next_line`. Il peut toujours valoir la peine de déclarer ces propriétés pour les utilisateurs qui peuvent les utiliser, ou au moins pour documenter la préférence.

Vous devez définir `root` sur `true` pour le niveau supérieur EditorConfig dans le projet, qui est normalement à la racine de votre répertoire de projet.

Des fichiers EditorConfig supplémentaires peuvent être définis dans des répertoires imbriqués, mais ne doivent pas définir `root` sur `true`.

Ensuite, vous pouvez définir un en-tête qui sélectionne les fichiers, avec des règles pour ce qu'il faut appliquer aux fichiers correspondants.

```plaintext
# Déclare que ceci est la configuration de niveau supérieur
root = true

# S'applique à tous les fichiers
[*]
indent_style = space
indent_size = 2

# S'applique à tous les fichiers Markdown
[*.md]
trim_trailing_whitespace = false

# S'applique à tous les fichiers C# et Java, en remplaçant les règles déclarées précédemment
[*.{cs,java}]
indent_size = 4
```

Il n'y a pas de conventions standard pour écrire un fichier `.editorconfig`, mais il y a deux approches notables que vous pouvez prendre.

### Définir des règles par projet

Ajoutez simplement des règles au fur et à mesure de vos besoins. Cela signifie simplement définir des règles ou ajouter des formats de fichiers à mesure que votre projet grandit.

Vous pouvez commencer par générer le fichier avec votre éditeur ou simplement créer un fichier nommé `.editorconfig` manuellement. Vous pouvez copier-coller l'[exemple](https://editorconfig.org/#example-file) du site officiel.

### Définir des règles pour tous les projets

Alternativement, vous pouvez rassembler toutes vos préférences et planifier la configuration idéale pour tous les fichiers avec lesquels vous pourriez interagir.

Vous pouvez partir de zéro ou commencer avec le mien et faire les ajustements nécessaires.

```plaintext
root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
curly_bracket_next_line = false
spaces_around_operators = true

[*.bat]
end_of_line = crlf

[*.cs]
curly_bracket_next_line = true

[*.{cpp,cs,gradle,java,kt,py,rs}]
indent_size = 4

[*.{js,ts}]
quote_type = single

[*.md]
trim_trailing_whitespace = false

[*.tsv]
indent_style = tab
```

## Recommandations de règles EditorConfig

Voici des règles que je recommanderais objectivement de déclarer, si votre projet contient le format de fichier respectif. Cela vous aidera à éviter des problèmes fastidieux qui peuvent survenir en raison de l'environnement de développement d'un utilisateur.

### Batch

Les fins de ligne doivent avoir une représentation textuelle lorsqu'elles sont stockées. Il s'agit généralement de quelque chose que vous ne verriez pas ou n'auriez pas à vous soucier.

Cependant, différents systèmes utilisent différents caractères pour représenter la fin d'une ligne. ([Plus d'informations](https://en.wikipedia.org/wiki/Newline#Representation))

* Les systèmes Unix utilisent un saut de ligne. (`lf` ou `\n`)

* Windows utilise un retour chariot et un saut de ligne. (`crlf` ou `\r\n`)

Les fichiers [Batch](https://en.wikipedia.org/wiki/Batch_file) peuvent avoir un comportement inattendu s'ils se terminent par des fins de ligne Unix. Vous pouvez éviter cela en définissant `end_of_line` sur `crlf` pour vous assurer qu'ils ont des fins de ligne Windows à la place. ([Plus d'informations](https://serverfault.com/questions/429594/is-it-safe-to-write-batch-files-with-unix-line-endings))

```plaintext
[*.bat]
end_of_line = crlf
```

### Markdown

Dans [Markdown](https://en.wikipedia.org/wiki/Markdown), vous pouvez écrire un saut de ligne dans le paragraphe actuel en ajoutant 2 espaces à la fin d'une ligne. ([Plus d'informations](https://en.wikipedia.org/wiki/Markdown#Example))

Vous voudrez définir `trim_trailing_whitespace` sur `false` pour éviter que votre éditeur ne supprime ces espaces lorsque vous enregistrez.

```plaintext
[*.md]
trim_trailing_whitespace = false
```

### Valeurs séparées par des tabulations

Les fichiers [TSV](https://en.wikipedia.org/wiki/Tab-separated_values) (Valeurs Séparées par des Tabulations) sont très similaires aux fichiers [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) (Valeurs Séparées par des Virgules), mais utilisent des tabulations au lieu de virgules comme délimiteur de colonne.

Il est très courant pour les développeurs de convertir automatiquement les tabulations en espaces. Vous devez définir `indent_style` sur `tab` pour éviter que le délimiteur ne soit remplacé, sinon votre tableau entier pourrait devenir une seule colonne.

```plaintext
[*.tsv]
indent_style = tab
```

## Conclusion

Si vous êtes un mainteneur, travaillant dans un environnement collaboratif ou en open-source, je vous recommande fortement d'ajouter un fichier `.editorconfig` définissant les conventions du projet à la racine de votre dépôt.

Les mainteneurs peuvent alors passer plus de temps à examiner des pull requests propres qui adhèrent au guide de style, car l'éditeur commencera automatiquement à imposer ou à appliquer les conventions.

Les contributeurs obtiennent une meilleure expérience, car le projet remplacera leurs paramètres d'espace de travail. Cela réduit le besoin de reformater le code ou de travailler contre les paramètres préconfigurés de l'éditeur.

Et les projets seront plus propres, car les conventions seront dans un seul fichier agnostique, plutôt que dans des fichiers spécifiques à l'éditeur que seuls certains contributeurs peuvent utiliser de toute façon.