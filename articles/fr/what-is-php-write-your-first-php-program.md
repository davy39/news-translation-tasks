---
title: Qu'est-ce que PHP ? Comment écrire votre premier programme PHP
subtitle: ''
author: Michael Para
co_authors: []
series: null
date: '2022-08-03T11:00:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-php-write-your-first-php-program
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Untitled-2-1.jpg
tags:
- name: PHP
  slug: php
seo_title: Qu'est-ce que PHP ? Comment écrire votre premier programme PHP
seo_desc: 'In this article, you will learn what the PHP programming language is and
  how to write your first program with it.

  History of PHP

  PHP is the most used and popular scripting language generated for web development.
  You can embed it in HTML documents.

  PH...'
---

Dans cet article, vous apprendrez ce qu'est le langage de programmation PHP et comment écrire votre premier programme avec celui-ci.

## Histoire de PHP

PHP est le langage de script le plus utilisé et le plus populaire généré pour le développement web. Vous pouvez l'intégrer dans des documents HTML.

PHP est écrit dans le langage de programmation C de haut niveau. La première génération de PHP était PHP/FI, créée en 1994 par Rasmus Lerdorf. Il l'a écrite pour suivre les visiteurs de son CV.

Ce qui lui a permis de créer facilement la première page d'accueil avec PHP était la possibilité d'intégrer le code PHP dans le balisage HTML.

La deuxième génération a été publiée sous le nom de PHP/FI Version 2 en 1995, qui faisait référence aux outils de page d'accueil personnelle. À cette époque, PHP dépendait d'un petit moteur d'analyse pour traduire et comprendre quelques instructions spéciales et certaines utilités qui étaient utilisées sur la page d'accueil personnelle PHP.

PHP est officiellement né et est devenu plus largement utilisé en 1996. Au début, il était utilisé sur plus de 15 000 applications web dans le monde. Ce nombre est passé à 50 000 l'année suivante.

Actuellement, PHP dépend entièrement d'un interpréteur avancé appelé le Zend Engine. Pour en savoir plus sur [ce qu'est PHP et comment écrire un programme PHP avancé](https://codedtag.com/php/what-is-php-write-a-program/), vous devriez en apprendre davantage sur sa syntaxe.

Comme je l'ai mentionné précédemment, PHP dépend de l'interpréteur Zend Engine. Mais la question est, qu'est-ce qu'un interpréteur ? Et comment fonctionne-t-il ?

Dans la section suivante, je vais tout expliquer à partir de zéro – du code source à la réponse du serveur PHP. Mais avant cela, vous devez connaître la différence entre l'interpréteur et le compilateur.

Plongeons-nous directement dans le sujet.

## Quelle est la différence entre un interpréteur et un compilateur ?

L'interpréteur est un programme qui prend le code source ligne par ligne et le traduit en bits binaires (0 et 1) – langage machine. Pendant ce processus, le développeur peut modifier le code source.

L'interpréteur ne met pas longtemps à analyser le code – comme supprimer les commentaires du code source, les espaces blancs, etc. Mais le temps global d'exécution est un peu plus lent.

D'autre part, le compilateur est un programme qui prend le code source complet déjà écrit dans un langage de programmation de haut niveau et le traduit en binaire ou en langage machine.

Pendant ce processus, vous ne pouvez pas modifier le code source car il est traité en un seul bloc par le compilateur. Le compilateur est lent à analyser le code mais traduit très rapidement.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/WhatsApp-Image-2022-07-27-at-2.34.06-PM.jpeg align="left")

Examinons plus en détail l'interpréteur PHP pour voir comment il fonctionne.

## Comment fonctionne l'interpréteur PHP ?

Comme je l'ai mentionné précédemment, l'interpréteur PHP s'appelle le Zend Engine et il comporte quatre phases pendant lesquelles il interprète le code source PHP – dans cette section, nous allons approfondir chaque phase.

### Analyse lexicale

L'interpréteur PHP prend le code source du serveur et commence la première phase appelée analyse lexicale (ou tokenisation). Dans ce processus, l'interpréteur supprime tous les espaces blancs et la syntaxe des commentaires, recherche toute erreur dans le code source, puis génère une séquence de tokens.

L'analyse lexicale ne provoque aucune erreur pendant cette phase car elle est uniquement responsable de la production d'une séquence de tokens. Mais elle génère une erreur d'analyse fatale pour arrêter directement cette phase si elle trouve une erreur dans le code source.

### L'analyseur syntaxique

Dans l'étape suivante, l'analyseur syntaxique prend le relais. Dans cette phase, l'analyseur syntaxique reçoit la séquence de tokens et définit certaines des instructions pour créer la machine virtuelle Zend Engine (VM) – qui est similaire au langage d'assemblage – pour manipuler la séquence de tokens qui a déjà été créée avec la phase précédente.

### La compilation

Cette phase est déjà sous la phase de l'analyseur syntaxique, et ici l'analyseur syntaxique commence la compilation en générant l'AST (Abstract Syntax Tree) – puis en le passant au générateur de code.

Le résultat de la compilation est un code intermédiaire qui dépend déjà du Zend Engine VM. Cela est connu sous le nom de codes d'opération (OPCodes). Les Opcodes contiennent certaines des instructions pour effectuer toutes les opérations qui nécessitent la mise en œuvre du contrôle de flux.

### L'exécution

Il s'agit de la dernière phase, et ici l'exécuteur reçoit le code intermédiaire qui a déjà été généré par la phase précédente. Il peut lire ces OPCodes à partir du tableau des instructions et les exécuter un par un.

Dans l'ensemble, le Zend Engine a deux fonctions séparées, la compilation et l'exécution, qui sont zend_compile et zend_execute.

Dans la section suivante, vous allez écrire votre premier programme PHP ! Mais avant cela, [vous devez installer un serveur Wamp (pour Windows) ou XAMPP (pour Linux/MacOS)](https://www.freecodecamp.org/news/how-to-get-started-with-php/) selon le système d'exploitation que vous utilisez.

## Comment installer XAMPP

Dans cette section, je vais expliquer le serveur XAMPP et comment exécuter le serveur PHP sur votre machine locale.

Tout d'abord, XAMPP est un logiciel gratuit utilisé pour créer un serveur web PHP. Mais que signifie XAMPP ?

1. "X" fait référence aux **systèmes d'exploitation** tels que Windows, Linux ou macOS. Cela signifie donc que nous pouvons installer le serveur XAMPP sur l'un des systèmes d'exploitation mentionnés dans cette ligne.

2. "A" fait référence à **Apache**, qui est le logiciel de serveur web PHP.

3. "M" fait référence à **MariaDB - MySQL**, les systèmes de gestion de bases de données.

4. "P" fait référence à **PHP** (Personal Home Page) – le langage de script côté serveur qui nous aide à créer des pages web dynamiques.

5. "P" fait référence à **Perl** qui est utilisé dans le développement web, la programmation réseau ou l'administration système.

Ainsi, XAMPP fait référence à tous les packages dont vous avez besoin pour développer des applications web.

Pour installer le serveur XAMPP sur votre machine locale, rendez-vous sur la [page officielle de XAMPP](https://www.apachefriends.org/) et téléchargez l'installateur selon votre système d'exploitation.

Une fois que vous l'avez téléchargé, installez simplement le programme selon les instructions que vous lisez dans l'installateur.

Le résultat final devrait ressembler à l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-2.png align="left")

*Le panneau de contrôle de XAMPP*

Vous n'avez qu'à cliquer sur le bouton "start" à côté du module Apache pour exécuter le serveur PHP.

Explorons les dossiers importants à l'intérieur de l'application du serveur XAMPP.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-3.png align="left")

*Dossiers importants de XAMPP*

L'image ci-dessus vous montre tous les dossiers importants, mais nous devons nous concentrer uniquement sur le dossier "**htdocs**". Ce dossier est le répertoire public qui contient tous les projets PHP.

Ainsi, vous placerez tout nouveau projet PHP à l'intérieur du dossier "**htdocs**". Et pour ouvrir le résultat dans le navigateur web, vous devez simplement naviguer vers "**localhost/votre_dossier_de_projet**".

Écrivons un programme PHP pour clarifier cela.

## Comment écrire votre premier programme PHP

Pour vous aider à écrire votre premier programme PHP, nous allons simplement afficher un petit message – "Hello World".

Tout d'abord, assurez-vous que votre serveur PHP est en cours d'exécution sur votre machine locale – j'utilise le serveur XAMPP sur ma machine locale.

Deuxièmement, créez un dossier à l'intérieur du répertoire de votre application serveur et nommez-le [codedtag](http://codedtag.com/).

L'image ci-dessous vous montre que mon dossier public dans l'application du serveur XAMPP est (**htdocs**) sur Windows.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-273.png align="left")

*Le dossier public du serveur XAMPP*

Pour l'étape suivante, créez une page d'index qui se termine par une extension PHP. À l'intérieur du dossier "codedtag", copiez-collez le code PHP suivant :

```php
<?php 
   echo "Hello World";
?>
```

Pour exécuter le script, ouvrez le navigateur et naviguez vers **localhost/codedtag**. Vous verrez le message d'impression comme dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-274.png align="left")

*Le message d'impression PHP*

Et c'est tout ! Vous avez imprimé votre premier programme PHP.

## Conclusion

Dans cet article, nous avons discuté de ce qu'est PHP et résumé son histoire en quelques lignes. Nous avons également appris la différence entre le compilateur et l'interpréteur.

De plus, nous avons discuté des étapes exactes du fonctionnement de l'interpréteur PHP. Pour résumer, jetons un coup d'œil au moteur Zend de PHP depuis le début.

1. La première étape est l'analyse lexicale. À ce stade, l'interpréteur supprime tous les espaces blancs et les commentaires du code source et génère une séquence de tokens.

2. L'étape suivante s'appelle l'analyseur syntaxique, et ici l'analyseur syntaxique définit les instructions pour créer la machine virtuelle Zend Engine afin de manipuler la séquence de tokens.

3. La phase de compilation crée et passe l'AST (Abstract Syntax Tree) au générateur de code et le résultat final de la compilation est les OPCodes.

4. L'étape suivante est celle de l'exécuteur, et à ce stade, l'exécuteur lit et exécute les instructions à partir du tableau.

Si vous souhaitez en savoir plus sur PHP, voici un [manuel complet qui couvre toutes les bases en profondeur](https://www.freecodecamp.org/news/the-php-handbook/).

Restez à l'écoute pour mon prochain article. Vous pouvez lire plus de mes articles sur [FlatCoding](https://flatcoding.com/).