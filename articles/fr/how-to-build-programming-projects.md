---
title: Comment construire un projet de programmation étape par étape
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-30T22:08:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-programming-projects
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6040a754a7946308b7681492.jpg
tags:
- name: Problem Solving
  slug: problem-solving
- name: General Programming
  slug: programming
- name: projects
  slug: projects
- name: 'self-improvement '
  slug: self-improvement
seo_title: Comment construire un projet de programmation étape par étape
seo_desc: "By Ogundiran Ayobami\nThis tweet about building projects really resonated\
  \ with me: \n\nIt says a lot about how programmers build the projects we all admire.\
  \ It pin-points the less glamorous parts of our activities which beginners don't\
  \ always pay attent..."
---

Par Ogundiran Ayobami

Ce tweet sur la construction de projets a vraiment résonné en moi :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/projects-tweet.png)

Il en dit long sur la manière dont les programmeurs construisent les projets que nous admirons tous. Il met en lumière les parties moins glamour de nos activités auxquelles les débutants ne prêtent pas toujours attention, probablement en raison de leur manque d'expérience.

Et cela me rappelle mon expérience récente de construction d'une extension VSCode. L'extension est censée me faire paraître comme un génie dans les tutoriels vidéo et réduire mes défis d'enregistrement. (Mais hey – je ne suis vraiment pas un génie 😜).

L'extension affiche le contenu d'un fichier caractère par caractère chaque fois qu'une touche est pressée. Elle simule une expérience de codage réel tandis que je ne fais attention qu'à l'enregistrement vocal. Wow ! Comment ai-je construit cela ? Eh bien, voyons comment cela s'est passé.

Cela peut aller sans dire, mais vous ne savez pas comment construire un nouveau projet jusqu'à ce que vous l'ayez réellement construit. Avant de commencer, je ne savais pas quoi faire et quoi rassembler. Mais j'étais sûr d'une chose – je savais comment trouver ce dont j'avais besoin. Boom ! La recherche a commencé.

Alors laissez-moi vous dire comment je l'ai fait, afin que vous puissiez vous aussi vous améliorer dans la construction de vos propres projets.

## Décomposer le projet en unités plus petites

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-310.png)
_Photo par [Unsplash](https://unsplash.com/@markusspiske?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Markus Spiske</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Je savais qu'il serait difficile de trouver un tutoriel complet sur ce que je voulais construire. Mais il était relativement facile de trouver des tutoriels liés à chaque unité du projet. J'ai donc décomposé le projet en ces parties :

1. Installer l'extension VSCode.
2. Obtenir le contenu d'un fichier actif.
3. Décomposer le contenu du fichier en caractères. (Mot => m, o, t).
4. Écouter les pressions de touches.
5. Afficher le caractère un par un chaque fois qu'une touche était pressée.

Ce sont les choses de base que je m'attendais à ce que l'extension puisse gérer.

Mais attendez ! Et si je construis un site web entier ? Ne vous inquiétez pas – c'est toujours le même processus. Voici ce que j'aurais fait si je voulais construire un site web aussi.

### Étape 1 : Décomposer tout en sections

Pour un site web, vos sections gérables pourraient ressembler à ceci :

1. En-tête
2. Principal
3. Barres latérales
4. Pied de page

### Étape 2 : Décomposer les sections en composants

Pour ce faire, je me serais demandé ce que je voulais dans chaque section. Ensuite, j'aurais listé ces éléments un par un.

✅ En-tête : Je veux un logo, une boîte de recherche, un bouton d'inscription/connexion (ou d'autres boutons de navigation) et des paramètres dans l'en-tête.

✅ Principal : Combien de colonne(s) ai-je besoin ? Doit-il inclure une barre latérale gauche ou droite ou une liste ?

✅ Pied de page : Est-ce que je veux des informations de copyright et de navigation dans le pied de page ? Autre chose ?

Ensuite, je me serais demandé quelles autres choses je voulais et je les aurais notées au fur et à mesure que je les pensais.

En bref, vous devez lister tout ce que vous voulez dans chaque section et composant. Mais ne perdez pas trop de temps à planifier, car l'exécution est la clé. Faites-le aussi rapidement que possible car une fois que vous avez un travail, vous aurez probablement à peine du temps libre pour planifier vos projets.

Mais vous pourriez penser, Oh, non ! Je suis confus. Comment puis-je connaître toutes les sections et composants dont j'ai besoin en tant que débutant ?

C'est une bonne observation car je ne suis pas un débutant et j'ai eu de l'expérience avec tous ces composants. C'est pourquoi je peux les lister facilement.

Mais ce n'est pas grave. Vous apprendrez toutes ces choses en cours de route. Vous devez simplement prêter attention à mon histoire d'extension VSCode. :)

## Écrivez votre première ligne de code et restez bloqué

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-311.png)
_Photo par [Unsplash](https://unsplash.com/@fx24?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Fernando Jorge</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Après avoir une image claire de ce qu'il faut construire, je crois que la chose la plus importante pour lancer un projet est d'écrire votre première ligne de code et de rester bloqué. C'est pessimiste, mais cela vous aide à devenir orienté solution.

Au lieu de vous inquiéter inutilement parce que vous n'êtes pas sûr de la manière de commencer, ouvrez votre éditeur de code de choix et écrivez votre première ligne de code – même si vous restez bloqué juste après cela.

Votre première ligne de code sera probablement supprimée ou améliorée plusieurs fois, et c'est bien. Elle est censée vous aider à surmonter la procrastination.

En réalité, vous serez toujours confus sur la manière de commencer et sur ce qu'il faut faire. Ne procrastinez pas à cause de tels sentiments, surtout après avoir compris comment le projet devrait fonctionner dans votre tête ou sur papier.

N'essayez pas de tout comprendre avant d'écrire votre première ligne de code. Vous ne comprendrez jamais tout. Au moins, personne n'a jamais tout compris jusqu'à présent.

## Aucun projet n'est parfait – y compris Google

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-312.png)
_Photo par [Unsplash](https://unsplash.com/@brett_jordan?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Brett Jordan</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Il est facile de vouloir que votre projet soit le meilleur jamais construit, surtout lorsque vous êtes un débutant. J'ai été là, donc je sais comment cela se sent.

J'étais juste un étudiant en art essayant de résoudre un problème en utilisant la technologie web. Après avoir échoué à embaucher un développeur web pour construire le projet pour moi parce que je ne pouvais pas me permettre le prix qu'ils ont cité, j'ai décidé d'apprendre à le construire par moi-même.

Le moi stupide a essayé de construire presque toutes les fonctionnalités sur Internet pour m'assurer que mon projet avait toutes les fonctionnalités que les autres n'avaient pas. De toute façon, j'ai finalement tué le projet.

Le point que je fais est de ne pas essayer de construire un projet qui ne peut pas être critiqué – il n'y a rien de tel. Vous devez vous concentrer sur les fonctionnalités principales, pas sur les fonctionnalités supplémentaires qui pourraient rendre le projet inutilisable.

N'essayez pas de faire un projet ou une fonctionnalité parfaite – faites des projets et des fonctionnalités utilisables et aimables à la place.

## Chaque projet est construit sur d'autres projets

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-313.png)
_Photo par [Unsplash](https://unsplash.com/@lidyanada?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Lidya Nada</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Après avoir eu une image claire de ce dont j'avais besoin pour construire l'extension VSCode, j'ai dû examiner des projets connexes. J'ai ouvert le code source de vscode-hacker-typer pour étudier comment le projet gère certaines des choses que je voulais implémenter. En faisant cela, j'ai appris un peu sur les API d'extension VSCode.

Comme j'étais totalement inexpérimenté dans la création d'extensions VSCode, l'examen de vscode-hacker-typer m'a aidé à passer de totalement ignorant à savoir ce qu'il fallait rechercher.

Connaître le nom de ce avec quoi vous voulez travailler est la première étape la plus importante pour résoudre tout problème en programmation.

Par exemple, disons qu'il y a une fonctionnalité que vous aimez sur un site web connexe mais que vous ne savez pas comment elle s'appelle. Comment allez-vous rechercher cette fonctionnalité ? Eh bien, ce n'est pas de la science-fiction.

Vous pouvez prendre une photo de la fonctionnalité et demander son nom dans des groupes de programmation ou demander à quelqu'un. Ou vous pouvez découvrir son nom ou son API en plongeant dans le code source d'un projet connexe comme je l'ai fait. Alors consultez des projets similaires au vôtre, apprenez d'eux et copiez leurs fonctionnalités.

## N'ayez pas peur de Googler

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-314.png)
_Photo par [Unsplash](https://unsplash.com/@mitchel3uo?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Mitchell Luo</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Avant de me lancer dans la création de l'extension VSCode, je ne savais même pas par où commencer – mais j'étais sûr de pouvoir rechercher mon chemin vers quelque chose de raisonnable. J'ai commencé à googler différentes questions :

✅ Comment obtenir le contenu d'un éditeur actif de VSCode ?

✅ Comment utiliser activeTextEditor de VSCode ?

✅ Comment utiliser onDidTextDocumentChange de VSCode ?

Et ainsi de suite.

Comprendre ce que vous voulez construire est la première étape pour obtenir des résultats de recherche pertinents, surtout lorsque vous construisez un projet que vous n'avez jamais construit. Vous devez conceptualiser l'idée ou les fonctionnalités que vous voulez implémenter afin de pouvoir trouver les solutions dont vous avez besoin.

### Conseils de base pour googler qui peuvent vous aider à obtenir de meilleurs résultats

#### Connaître les mots-clés qui vous intéressent.

Par exemple, si je veux construire une page de destination avec uniquement HTML et CSS, je ne rechercherai pas quelque chose comme "Comment construire une page de destination". Cela apportera beaucoup de choses que je ne veux pas. Cela doit inclure les mots-clés qui m'intéressent.

Voici des exemples à étudier :

* Comment construire une page de destination avec HTML et CSS ?
* Comment créer une extension VSCode avec Typescript (si je veux Typescript) ?
* Comment créer une extension VSCode avec JavaScript ?

Assurez-vous que vos mots-clés attendus sont inclus – soyez spécifique.

Googler (Comment construire une page de destination avec HTML et CSS ?) peut donner un résultat générique. C'est un problème. Mais cela peut être corrigé avec des correspondances exactes.

#### Utilisez des guillemets pour obtenir des correspondances exactes dans Google

Par exemple, "Comment construire une page de destination avec HTML et CSS" vous donnera un résultat avec les mots exacts de cette recherche.

Si vous voulez explorer des idées générales sur la construction d'une page de destination, retirez les guillemets.

#### Exclure un terme de recherche avec (-)

Parfois, vous ne voulez qu'un résultat avec HTML et CSS, mais vous obtenez ceux avec HTML, CSS et JavaScript.

Vous pouvez utiliser "- JavaScript" pour exclure JavaScript. Par exemple, vous pouvez rechercher "Comment construire une page de destination avec HTML et CSS - JavaScript".

Cela est utile lorsque vous voulez exclure certains mots-clés.

#### Remplacez vos termes

Lorsque vous voulez passer d'un langage, d'une bibliothèque ou d'un framework à un autre, vous devez utiliser tout ce que vous savez du premier langage ou framework.

Par exemple, vous voulez passer de JavaScript à Python et vous savez comment JavaScript fonctionne. Tous vos termes de recherche ou approches précédents pour JavaScript seront toujours très utiles lors de l'utilisation de Python.

Vous devez simplement remplacer vos termes spécifiques – remplacez JavaScript par Python dans toutes vos recherches. Ensuite, vous pouvez googler "Array in Python" au lieu de "Array in JavaScript".

## Vous serez toujours bloqué – et c'est normal

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-315.png)
_Photo par [Unsplash](https://unsplash.com/@ianstauffer?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Ian Stauffer</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Le problème avec les tutoriels "Comment faire" est qu'ils ne vous informent pas toujours que rester bloqué fait partie du processus. L'extension VSCode sur laquelle je travaille ne fonctionne toujours pas parce que je suis bloqué. Après avoir réfléchi à chaque partie, je suis resté bloqué lors de l'implémentation des fonctionnalités.

L'API de l'extension VSCode que j'utilisais ne peut pas être itérée, donc je dois trouver un moyen de le faire. De plus, vscode-hacker-typer n'utilise pas l'approche que j'utilise. Il enregistre les frappes et les rejoue. Je veux éviter d'enregistrer les frappes. Je veux seulement afficher le contenu d'un activeTextEditor caractère par caractère chaque fois qu'une touche est pressée.

Vous serez toujours bloqué, et c'est pourquoi vous devez apprendre [Comment améliorer vos compétences en débogage](https://www.freecodecamp.org/news/how-to-improve-your-debugging-skills/). Rester bloqué est une partie significative du processus. Votre capacité à surmonter les défis de rester bloqué déterminera jusqu'où vous irez dans la réalisation de projets.

## Conclusion

Il peut être tentant de vouloir abandonner parce que vous avez l'impression de ne pas être aussi bon que les autres. La réalité est que nous luttons tous en coulisses. Nous avons tous résolu beaucoup de problèmes par essais et erreurs. Nous nous sentons tous stupides et faux parce que nous construisons toujours sur les projets des autres.

Mais n'oubliez pas que chaque projet amazing a une histoire moins glamour que vous ne connaissez pas derrière lui. Ce qui compte, avant tout, c'est de s'assurer que vous construisez le projet à la fin.

N'oubliez pas :

> "La chose géniale que nous avons faite, c'est que nous n'avons pas abandonné" - Jay Z.

[**Ayobami**](https://twitter.com/codingnninja) aime écrire l'histoire avec le développement logiciel et aide actuellement ceux qui luttent pour comprendre et construire des projets avec HTML, CSS et JavaScript [ici](https://aw194b5a.aweb.page/p/5c07dec9-f1bd-4a8f-a788-87e4f0a6a6a1).