---
title: Comment générer un fichier markdown GitHub à partir de Microsoft Word en utilisant
  TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-23T00:48:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-generate-a-github-markdown-file-from-microsoft-word-using-typescript-a8976ea958c3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*85IJbXqoCZIBLjS3oyQ1YA.jpeg
tags:
- name: GitHub
  slug: github
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: Comment générer un fichier markdown GitHub à partir de Microsoft Word en
  utilisant TypeScript
seo_desc: 'By Manish Bansal

  What? Why would one want to generate an MD file from a Microsoft word document?
  If that’s the first thought you had after reading this title, then let me give you
  a strong use case.

  Consider a situation where you are using Git or any...'
---

Par Manish Bansal

Quoi ? Pourquoi voudrait-on générer un fichier MD à partir d'un document Microsoft Word ? Si c'est la première pensée que vous avez eue après avoir lu ce titre, alors laissez-moi vous donner un cas d'utilisation solide.

Imaginez une situation où vous utilisez Git ou tout autre système de contrôle de version (VCS) pour les sources de votre projet ainsi que pour ses artefacts. Maintenant, comme la plupart des projets, vous décidez d'utiliser Microsoft Word pour la documentation et de l'enregistrer dans Git. Encore une fois, plusieurs membres de l'équipe modifient le même document. Après modification, ils enregistrent le document dans le dépôt.

Maintenant, Git sera en mesure de maintenir l'historique de votre document. Comment pourrez-vous voir les changements qui ont été apportés au document depuis la dernière fois que vous l'avez enregistré ? Oui, vous pouvez utiliser le mode de suivi des modifications de Microsoft Word, mais n'est-ce pas désordonné ? Ou pour l'amour du ciel, pourrez-vous utiliser l'utilitaire Git diff pour vérifier rapidement les différences ? Je dirais non.

Alors, quelle est la solution ? Devriez-vous arrêter d'utiliser Microsoft Word pour la documentation ? Ou devriez-vous passer à un autre VCS ?

Je dirais ni l'un ni l'autre. Et si vous mainteniez votre documentation dans Microsoft Word ? Ensuite, transformez-la en un fichier markdown (MD) (en termes simples, un fichier texte) pendant la phase de construction et enregistrez-la ? Si cette solution vous enthousiasme, alors continuez à lire.

Mais avant de plonger directement dans la conversion, laissez-moi d'abord vous dire ce qu'est exactement un fichier markdown.

### Qu'est-ce qu'un fichier markdown ou MD ?

Markdown est un langage de syntaxe visant à faciliter la lecture et l'écriture de texte structuré. De plus, il est facile à apprendre et ne nécessite qu'un éditeur de texte pour créer un document.

Maintenant, il existe plusieurs implémentations du langage (comme [GFM](https://github.github.com/gfm/) aka Github flavored Markdown). Chacune de ces implémentations a ses propres améliorations et fonctionnalités qui ne sont pas nécessairement compatibles les unes avec les autres.

Chaque implémentation supporte diverses fonctionnalités courantes comme les paragraphes, les citations, les titres et les listes. Cela aide à maintenir le texte de manière structurée comme Microsoft Word. Mais, au lieu d'utiliser des codes binaires internes, les fichiers MD utilisent des caractères de texte brut pour ces fonctionnalités. Cela fait d'un fichier MD un fichier texte mais pas un fichier binaire comme un fichier docx.

Par exemple, dans la version markdown de GitHub, voici les différentes fonctionnalités et les moyens de les représenter sous forme de texte par rapport à un document Word.

![Image](https://cdn-media-1.freecodecamp.org/images/EmrHeOtVuSp1R-hU7j6UqWwzB9r7DhCjGY0Y)

Pour les avantages détaillés des fichiers MD par rapport aux documents Word, vous pouvez également vous référer à [cet](https://hackernoon.com/say-yes-to-markdown-no-to-ms-word-be4692e7a8cd) article.

### D'accord ! Je suis convaincu. Montrez-moi le code.

Avertissement : Ce projet est inspiré par le code source de TypeScript. En le parcourant, j'ai trouvé cette idée de convertir un document Word en un fichier MD. Vous pouvez voir son code source [ici](https://github.com/manishbansal8843/TypeScript/blob/1b880f8ad445c778911a71b8cdec94ae885299bf/scripts/word2md.ts#L407).

Pour simplifier, j'ai supprimé quelques sections de code dans mon dépôt. Le code original était destiné à convertir la documentation de spécification de TypeScript en un fichier MD. Ce fichier contient de nombreux styles personnalisés. Donc, une fois que vous avez terminé cet article, vous pouvez très bien parcourir le code de conversion de TypeScript et apprécier ses capacités à effectuer des conversions plus complexes.

Le code complet mentionné dans cet article peut être consulté [ici](https://github.com/manishbansal8843/word2mdconverter). L'ensemble du code peut être divisé en 3 sections :

1. Configurations Gulp.
2. Exécution de CScript.
3. Fonction principale TypeScript

Comme indiqué précédemment, vous pouvez convertir un document Word en un fichier MD pendant la phase de construction. Cela peut être fait par n'importe quel gestionnaire de tâches. Ici, j'ai choisi gulp.

Dans les configurations Gulp, j'ai défini 3 tâches. La première consiste à nettoyer le répertoire de construction, ce qui est assez standard. La deuxième consiste à compiler le code TypeScript. Et la dernière consiste à appeler le CScript pour exécuter le JavaScript.

### Qu'est-ce que CScript ?

CScript.exe (présent dans C:\Windows\System32) est un exécutable basé sur la console pour l'hôte de script qui est utilisé pour exécuter les scripts. Il peut interpréter des langages de script comme VB Script ou JavaScript. De même, nous avons WScript mais il est utilisé pour les applications Windows. Dans ce cas, la console n'est pas attachée. Donc, si vous avez besoin de créer une application basée sur la console, nous pouvons utiliser CScript.

Maintenant, dans notre projet, le travail principal de CScript est de fournir un environnement d'exécution à notre script, c'est-à-dire JavaScript. Maintenant, vous devez vous demander pourquoi je n'ai pas utilisé node au lieu de CScript pour exécuter mon JavaScript.

Les deux fournissent un environnement d'exécution pour un JavaScript. CScript fournit un support inhérent pour la technique du modèle d'objet composant Windows. Donc, si vous essayez d'exécuter ce script via Node, vous obtiendrez une erreur comme celle-ci.

> var fileStream = new ActiveXObject("ADODB.Stream");

> ReferenceError: ActiveXObject is not defined

**Maintenant, qu'est-ce qu'une technique de modèle d'objet composant ?**

Le modèle d'objet composant est une technologie développée par Microsoft. Ce n'est pas un langage mais une norme binaire. Selon la définition,

> Le modèle d'objet composant Microsoft ([COM](https://docs.microsoft.com/en-us/windows/desktop/com/the-component-object-model)) est un système orienté objet, distribué et indépendant de la plateforme pour créer des composants logiciels binaires qui peuvent interagir. COM est la technologie de base pour les OLE de Microsoft (documents composés), ActiveX (composants compatibles Internet), ainsi que d'autres.

En termes simples, les objets COM sont des interfaces vers divers objets d'exécution. (C'est pourquoi la définition contient un terme appelé "composants logiciels binaires"). Ce n'est pas un langage, mais une technique qui est agnostique en matière de langage de programmation.

La seule exigence linguistique pour COM est que le code est généré dans un langage capable de créer des structures de pointeurs. Soit explicitement, soit implicitement, appeler des fonctions via des pointeurs. Les langages orientés objet tels que C++ et Smalltalk fournissent des mécanismes de programmation qui simplifient la mise en œuvre des objets COM.

Après cela, nous pouvons utiliser tout autre langage comme Java, VB ou JavaScript pour interagir avec ces objets COM. Cela nous donnera également accès aux applications d'exécution. Dans notre cas, aux applications Microsoft Word.

**Donc, dites-vous que nous ne pouvons pas du tout utiliser Node ici ?**

Non, ce n'est pas vrai. Nous pouvons également utiliser Node au lieu de CScript. Mais pour supporter COM, nous devrons installer un autre package appelé win32com pour le support COM. Les détails peuvent être trouvés [ici](https://helloacm.com/using-com-object-in-nodejs/).

### Code final

Maintenant, afin d'interagir avec l'application Word, diverses API ont été utilisées. Et puisque nous utilisons le modèle d'objet COM, je me suis référé au [modèle d'objet Word](https://docs.microsoft.com/en-us/visualstudio/vsto/word-object-model-overview?view=vs-2017).

Word fournit des centaines d'objets avec lesquels vous pouvez interagir. Ces objets sont organisés dans une hiérarchie qui suit de près l'interface utilisateur. En haut de la hiérarchie se trouve l'objet Application. Cet objet représente l'instance actuelle de Word. L'objet Application contient les objets Document, Selection, Bookmark et Range. Chacun de ces objets a de nombreuses méthodes et propriétés auxquelles vous pouvez accéder pour manipuler et interagir avec l'objet.

Maintenant, dans notre script, nous avons d'abord créé un objet d'application Word en utilisant ActiveXObject. Une fois l'objet d'application obtenu, l'objet document est créé en passant le nom du document (obtenu à partir des arguments de la ligne de commande de l'appel de cscript).

Maintenant, cela représente l'objet actif du document réel. Cet objet est capable d'analyser ainsi que de manipuler le document Word. Cependant, dans notre cas d'utilisation, nous devons uniquement analyser le document et écrire un fichier texte.

Ce code est très générique, qui est utilisé pour convertir des fonctionnalités très basiques d'un document Word comme les références croisées, les listes, les textes en indice, les caractères gras et italiques, etc. en format GFM. Cependant, vous pouvez écrire votre propre code pour convertir vos styles personnalisés du document Word dans le format souhaité.

Vous pouvez trouver le code TypeScript réel [ici](https://github.com/manishbansal8843/word2mdconverter/blob/master/src/word2mdconverter.ts). Le code est assez facile à lire. Voici quelques points forts majeurs :

1. [Premièrement](https://github.com/manishbansal8843/word2mdconverter/blob/4acca1877451c7929eddbdce09c2ea113525769e/src/word2mdconverter.ts#L357), un objet document est passé à la fonction convertDocumentToMarkdown qui retourne le texte à écrire dans un fichier MD.
2. Ensuite, dans convertDocumentToMarkdown, les méthodes et propriétés de l'objet document sont appelées pour trouver et remplacer les fonctionnalités pertinentes de Word par la syntaxe correspondante du langage GFM. Par exemple, les textes en indice et les textes en gras et en italique sont d'abord recherchés. Après cela, le texte est remplacé par le code spécifique GFM. Et enfin, les styles Word sont supprimés. Tout cela est fait [ici](https://github.com/manishbansal8843/word2mdconverter/blob/4acca1877451c7929eddbdce09c2ea113525769e/src/word2mdconverter.ts#L332-L334).
3. Après cela, les références croisées sont [remplacées](https://github.com/manishbansal8843/word2mdconverter/blob/4acca1877451c7929eddbdce09c2ea113525769e/src/word2mdconverter.ts#L336-L338). Cependant, cela est délicat. Tout d'abord, la fonction toggleShowCodes est appelée. Cela a un impact similaire à alt+F9 dans un document Word. Cela remplace toutes les références croisées dans un document par le code. Après cela, la méthode de recherche et de remplacement est appelée pour trouver et remplacer toutes les références croisées par le style GFM. Ici, "19 REF" est passé en argument à une fonction. Il s'agit d'un critère de recherche standard pour trouver toutes les références croisées dans un document Word. Enfin, après le remplacement, la fonction toggleShowCodes est à nouveau appelée pour ramener le document à sa forme originale.
4. Enfin, la fonction writeDocument est appelée, qui fait le travail principal. Elle lit le document paragraphe par paragraphe, puis, en utilisant un switch case, recherche les styles des paragraphes (comme s'il s'agit d'un titre ou d'un tableau ou d'un paragraphe de liste ou d'une image). Maintenant, en fonction du style trouvé, le texte souhaité est écrit dans le fichier MD.

**Un mot ou deux sur l'incorporation d'images :** L'incorporation d'images dans un fichier MD est un peu délicate.

Tout d'abord, vous devez stocker les images dans votre dépôt git. Ensuite, le lien doit être donné dans le fichier MD pour l'incorporer. La syntaxe est ![texte alternatif](chemin/dans/le/dépôt/image1.jpg).

Maintenant, afin de générer automatiquement ce lien pour une image lors de la conversion de Word en un fichier MD, un texte caché est créé (juste après l'image sans aucun espace) avec le contenu comme le lien lui-même. Ensuite, dans le [code](https://github.com/manishbansal8843/word2mdconverter/blob/4acca1877451c7929eddbdce09c2ea113525769e/src/word2mdconverter.ts#L258-L263), ce texte caché est supprimé et inséré dans le fichier MD.

Maintenant, vous pourriez trouver le code réel pour faire tout cela très fastidieux, mais tout cela est conforme à l'[API](https://docs.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word._document?view=word-pia) exposée par l'application Word. Donc, ne vous inquiétez pas de cela. Vous pouvez définitivement vous référer à mon code ou au code original de TypeScript. Les deux seront un bon point de départ pour votre prochain projet.

Oh attendez !! C'est tout. Vous avez réussi jusqu'à la fin ?. Eh bien, alors ? Félicitations ! ? Et, si vous avez aimé cet article, n'hésitez pas à cliquer sur ce bouton d'applaudissements ? ci-dessous. Cela signifierait beaucoup pour moi et cela aidera d'autres personnes à voir l'histoire. Santé ! ?