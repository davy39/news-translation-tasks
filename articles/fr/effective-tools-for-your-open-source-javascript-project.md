---
title: Les meilleurs outils pour vous aider à construire votre projet JavaScript open-source
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-10T16:53:28.000Z'
originalURL: https://freecodecamp.org/news/effective-tools-for-your-open-source-javascript-project
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c35740569d1a4ca30ac.jpg
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Developer Tools
  slug: developer-tools
- name: JavaScript
  slug: javascript
- name: npm
  slug: npm
- name: open source
  slug: open-source
seo_title: Les meilleurs outils pour vous aider à construire votre projet JavaScript
  open-source
seo_desc: 'By Tyler Hawkins

  I recently published a package on npm: a data structures and algorithms library
  implemented in JavaScript.

  The purpose of the project is to help others learn and understand data structures
  and algorithms from a JavaScript perspective...'
---

Par Tyler Hawkins

J'ai récemment publié un package sur npm : une bibliothèque de structures de données et d'algorithmes implémentée en JavaScript.

Le but du projet est d'aider les autres à apprendre et à comprendre les structures de données et les algorithmes d'un point de vue JavaScript.

Plutôt que de contenir uniquement des extraits de code avec des explications accompagnatrices, le projet est conçu pour fournir à un apprenant motivé un code entièrement fonctionnel, de bons cas de test et un terrain de jeu rempli d'exemples.

Si vous êtes intéressé, le projet peut être trouvé sur npm [ici](https://www.npmjs.com/package/js-data-structures-and-algorithms).

Mais, plutôt que de parler du projet lui-même, ce dont je veux parler aujourd'hui, ce sont tous les outils pratiques que j'ai appris et utilisés lors de la création du projet.

J'ai travaillé sur des tonnes de projets secondaires et de démonstrations au cours des six dernières années, mais chacun d'eux est très visible comme étant simplement des "projets personnels". Ils n'ont en aucun cas les qualités qui les feraient paraître professionnels ou prêts pour la production.

Ce que je me suis fixé de créer était quelque chose qui pourrait être considéré comme un package open-source respectable. Pour cela, j'ai décidé que mon projet aurait besoin d'une documentation appropriée, d'outils, de linting, d'intégration continue et de tests unitaires.

Voici quelques-uns des outils que j'ai utilisés. Chacun sert un but unique. J'ai lié la documentation pour chaque package afin que vous aussi, vous puissiez commencer à utiliser ces outils dans vos propres projets.

**Note** : Cet article suppose que vous êtes déjà familier avec le processus de création d'un simple package JavaScript et de sa publication sur npm.

Si ce n'est pas le cas, l'équipe npm dispose d'une [excellente documentation pour commencer](https://docs.npmjs.com/creating-and-publishing-unscoped-public-packages) qui vous guidera à travers l'initialisation d'un projet et les étapes de publication.

Alors, commençons.

# Prettier

Prettier est un formateur de code opinionné qui formate automatiquement votre code pour vous. Plutôt que de simplement utiliser ESLint pour appliquer les normes de formatage sur lesquelles votre équipe s'est accordée, Prettier peut s'occuper du formatage pour vous.

Plus besoin de s'inquiéter de corriger l'indentation et les largeurs de ligne ! Je l'utilise spécifiquement pour mon JavaScript, mais il peut gérer de nombreuses langues différentes.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/prettier.png)
_Exemple de JavaScript avant et après l'exécution de Prettier_

Vous pouvez consulter la documentation de Prettier ici : [https://github.com/prettier/prettier](https://github.com/prettier/prettier)

# stylelint

stylelint formate automatiquement votre CSS pour vous. Similaire à Prettier, cet outil vous aide à garder votre CSS propre tout en prenant en charge le travail fastidieux pour vous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/02-stylelint.png)
_Exemple de sortie après l'exécution de stylelint_

Vous pouvez consulter la documentation de stylelint ici : [https://github.com/stylelint/stylelint](https://github.com/stylelint/stylelint)

# ESLint

ESLint gère tout le reste de mon linting JavaScript pour attraper les erreurs de syntaxe et appliquer les meilleures pratiques.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-09-at-9.10.38-PM.png)
_Exemple de sortie du linting avec ESLint dans leur environnement de playground_

Vous pouvez consulter la documentation d'ESLint ici : [https://eslint.org/](https://eslint.org/)

# Commitizen

Commitizen est un outil CLI qui vous guide à travers l'écriture de vos messages de commit. Il génère le message de commit pour vous en fonction de votre entrée et garantit que le message de commit résultant suit la norme Conventional Commits.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/04-comitizen.png)
_Interface de ligne de commande de Commitizen lors de la création d'un nouveau commit_

Vous pouvez consulter la documentation de Commitizen ici : [https://github.com/commitizen/cz-cli](https://github.com/commitizen/cz-cli)

# commitlint

commitlint vérifie que vos messages de commit suivent la norme Conventional Commits. Tant que vous utilisez Commitizen pour créer vos messages de commit, vous ne rencontrerez aucun problème.

Le vrai avantage d'utiliser commitlint est d'attraper les commits que les développeurs ont écrits eux-mêmes et qui ne suivent pas vos normes de formatage.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/05-commitlint.svg)
_Démonstration de commitlint pour montrer les messages d'erreur possibles_

Vous pouvez consulter la documentation de commitlint ici : [https://github.com/conventional-changelog/commitlint](https://github.com/conventional-changelog/commitlint)

# lint-staged

lint-staged exécute des linters sur le code que vous essayez de commiter. C'est ici que vous pouvez valider que votre code respecte les normes imposées par Prettier, stylelint et ESLint.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/06-lint-staged-prettier.gif)
_Exemple de lint-staged qui exécute ESLint sur le code vérifié_

Vous pouvez consulter la documentation de lint-staged ici : [https://github.com/okonet/lint-staged](https://github.com/okonet/lint-staged)

# Husky

Husky facilite l'exécution des hooks Git.

Tous les outils mentionnés précédemment peuvent être exécutés via Husky sur des hooks Git comme `pre-commit` ou `commit-msg`, c'est donc ici que la magie opère.

Par exemple, j'exécute lint-staged et mes tests unitaires pendant le hook `pre-commit`, et j'exécute commitlint pendant le hook `commit-msg`. Cela signifie que lorsque j'essaie de vérifier mon code, Husky effectue toutes les validations pour s'assurer que je respecte toutes les règles que j'impose dans mon projet.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-09-at-9.21.17-PM.png)
_Configuration Husky exemple qui s'exécute sur les hooks Git pre-commit et commit-msg_

Vous pouvez consulter la documentation de Husky ici : [https://github.com/typicode/husky](https://github.com/typicode/husky)

# Rollup

Rollup est un bundler de modules pour JavaScript. Il prend tout votre code source et le bundle dans les fichiers que vous souhaitez réellement distribuer dans le cadre de votre package.

La sagesse conventionnelle semble être que si vous construisez une application web, vous devriez utiliser webpack. Et si vous construisez une bibliothèque, vous devriez utiliser Rollup.

Dans mon cas, je construisais une bibliothèque de structures de données et d'algorithmes, donc j'ai choisi d'utiliser Rollup. Un avantage semble être que la sortie que Rollup génère est significativement plus petite que ce que webpack produit.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-09-at-9.24.23-PM.png)
_Une configuration Rollup très minimale qui crée un bundle de sortie au format CommonJS_

Vous pouvez consulter la documentation de Rollup ici : [https://rollupjs.org/guide/en/](https://rollupjs.org/guide/en/)

# Standard Version

Standard Version aide à automatiser votre gestion de version et la génération de votre journal des modifications.

Précédemment, j'ai mentionné des outils comme Commitizen et commitlint pour formater vos commits selon la norme Conventional Commits. Pourquoi, pourriez-vous demander, est-ce utile ?

La réponse, du moins en partie, est qu'en utilisant un format de message de commit cohérent, vous pouvez utiliser des outils capables de comprendre quel type de changements vos commits apportent.

Par exemple, corrigez-vous des bugs ? Ajoutez-vous de nouvelles fonctionnalités ? Faites-vous des changements majeurs dont les utilisateurs de votre bibliothèque devraient être informés ? Standard Version est capable de comprendre vos messages de commit et de générer ensuite un journal des modifications pour vous.

Il est également capable d'augmenter intelligemment la version de votre package selon la norme de version sémantique (majeure, mineure, corrective).

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-09-at-9.27.32-PM.png)
_Script de pré-version exemple de Standard Version qui s'exécute avant les augmentations de version_

Vous pouvez consulter la documentation de Standard Version ici : [https://github.com/conventional-changelog/standard-version](https://github.com/conventional-changelog/standard-version)

# Travis CI

Travis CI est un outil d'intégration continue (CI) qui peut être intégré avec GitHub, où mon code est hébergé.

Les outils CI sont importants car ils permettent à vos commits d'être testés une fois de plus avant de les fusionner dans votre branche principale. On pourrait dire que l'utilisation de Travis CI et d'un outil comme Husky duplique les fonctionnalités, mais il est important de garder à l'esprit que même Husky peut être contourné en passant un drapeau `--no-verify` à votre commande de commit.

Via GitHub, vous pouvez spécifier que vos travaux Travis CI doivent réussir avant que le code puisse être fusionné, ce qui ajoute une couche supplémentaire de protection et vérifie que seul le code réussi entre dans votre dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-09-at-9.29.33-PM.png)
_Sortie Travis CI d'une build réussie_

Vous pouvez consulter la documentation de Travis CI ici : [https://docs.travis-ci.com/](https://docs.travis-ci.com/)

# Codecov

Codecov est un autre outil CI qui examine la couverture de code de votre projet.

J'écris des tests unitaires JavaScript en utilisant Jest. Une partie de mon travail Travis CI exécute ma suite de tests et s'assure qu'ils passent tous. Il envoie également la sortie de couverture de code à Codecov, qui peut ensuite vérifier si ma couverture de code diminue ou reste élevée. Il peut également être utilisé en conjonction avec les badges GitHub, dont nous parlerons ensuite.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-09-at-9.31.34-PM.png)
_Tableau de bord Codecov (regardez cette belle couverture de code de 100 % !)_

Vous pouvez consulter la documentation de Codecov ici : [https://docs.codecov.io/docs](https://docs.codecov.io/docs)

# Badges

Avez-vous déjà regardé un projet sur GitHub et vu de petits badges près du haut du README ? Des choses comme si la build passe, quelle est la couverture de code, et quelle est la dernière version du package npm peuvent toutes être montrées en utilisant des badges.

Ils sont relativement simples à ajouter, mais je pense qu'ils ajoutent une touche vraiment agréable à n'importe quel projet. [Shields.io](http://shields.io/) est une excellente ressource pour trouver de nombreux badges différents qui peuvent être ajoutés à votre projet, et il vous aide à générer le markdown à inclure dans votre README.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-09-at-9.33.10-PM.png)
_Badges GitHub pour mon package npm js-data-structures-and-algorithms_

Vous pouvez consulter la documentation de Shields.io ici : [https://shields.io/](https://shields.io/)

# Documentation

Un peu de documentation va loin. Dans mon projet, j'ai ajouté un README, un CHANGELOG, des directives de contribution, un code de conduite et une licence.

Ces documents servent à aider les gens à savoir ce qu'est votre projet, comment l'utiliser, quels changements ont été apportés avec chaque version, comment contribuer s'ils veulent s'impliquer, comment ils sont censés interagir avec les autres membres de la communauté, et quels sont les termes légaux.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-09-at-9.35.02-PM.png)
_Le CHANGELOG pour mon package npm js-data-structures-and-algorithms_

Vous pouvez consulter la documentation de mon projet ici : [https://github.com/thawkin3/js-data-structures-and-algorithms](https://github.com/thawkin3/js-data-structures-and-algorithms)

# Modèles GitHub

Saviez-vous que vous pouvez créer des modèles dans GitHub pour des choses comme les rapports de bugs, les demandes de fonctionnalités et les pull requests ? Créer ces modèles rend parfaitement clair, par exemple, quelles informations quelqu'un devrait fournir lors de la soumission d'un bug.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-09-at-9.36.30-PM.png)
_Modèles GitHub pour les rapports de bugs et les demandes de fonctionnalités_

Vous pouvez consulter la documentation des modèles GitHub ici : [https://help.github.com/en/github/building-a-strong-community/about-issue-and-pull-request-templates](https://help.github.com/en/github/building-a-strong-community/about-issue-and-pull-request-templates)

# Conclusion

C'est tout. Lorsque j'ai montré ce projet à quelques amis pour la première fois, l'un d'eux a commenté : « Oh, ma soupe d'outils de build ! » Et il a peut-être raison. C'est beaucoup. Mais je crois fermement que l'ajout de tous les outils ci-dessus en vaut la peine. Cela aide à automatiser de nombreuses choses et à garder votre base de code propre et en ordre de marche.

Mon plus grand enseignement de la construction de ce projet est que la configuration de tous les outils ci-dessus n'est pas aussi intimidante qu'il y paraît. Chacun de ces outils dispose d'une bonne documentation et de guides utiles pour commencer. Ce n'était vraiment pas si mal, et vous devriez vous sentir confiant d'adopter certains (si ce n'est tous) de ces outils dans votre projet également.

Bon codage !