---
title: Outils populaires de développement Front End que vous devriez connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-03T02:35:19.000Z'
originalURL: https://freecodecamp.org/news/front-end-development-tools-you-should-know
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/frontend-dev-tools.png
tags:
- name: Babel
  slug: babel
- name: CircleCI
  slug: circleci
- name: eslint
  slug: eslint
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: npm
  slug: npm
- name: webpack
  slug: webpack
seo_title: Outils populaires de développement Front End que vous devriez connaître
seo_desc: 'By Yiğit Kemal Erinç

  If you are just getting started with JavaScript, the number of tools and technologies
  you''ll hear about may be overwhelming. And you might have a hard time deciding
  which tools you actually need.

  Or maybe you''re familiar with the...'
---

Par Yiğit Kemal Erinç

Si vous commencez tout juste avec JavaScript, le nombre d'outils et de technologies dont vous entendrez parler peut être écrasant. Et vous pourriez avoir du mal à décider quels outils vous avez réellement besoin.

Ou peut-être connaissez-vous les outils, mais vous n'avez pas beaucoup réfléchi aux problèmes qu'ils résolvent et à quel point votre vie serait misérable sans leur aide.

Je crois qu'il est important pour les ingénieurs logiciels et les développeurs de comprendre le but des outils que nous utilisons tous les jours.

C'est pourquoi, dans cet article, je me penche sur NPM, Babel, Webpack, ESLint et CircleCI, et j'essaie de clarifier les problèmes qu'ils résolvent et comment ils les résolvent.

## NPM

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-1.png)

NPM est le gestionnaire de paquets par défaut pour le développement JavaScript. Il vous aide à trouver et à installer des paquets (programmes) que vous pouvez utiliser dans vos programmes.

Vous pouvez ajouter npm à un projet simplement en utilisant la commande "**npm init**". Lorsque vous exécutez cette commande, elle crée un fichier "**package.json**" dans le répertoire courant. C'est le fichier où vos dépendances sont listées, et npm le considère comme la carte d'identité du projet.

Vous pouvez ajouter une dépendance avec la commande "**npm install (nom_du_paquet)**".

Lorsque vous exécutez cette commande, npm se connecte au registre distant et vérifie s'il existe un paquet identifié par ce nom de paquet. S'il le trouve, une nouvelle entrée de dépendance est ajoutée à votre **package.json** et le paquet, avec ses dépendances internes, est téléchargé depuis le registre.

Vous pouvez trouver les paquets ou dépendances téléchargés sous le dossier **"node_modules"**. Gardez simplement à l'esprit qu'il devient généralement assez volumineux – assurez-vous donc de l'ajouter à **.gitignore**.

![Comment garder vos bibliothèques JavaScript à jour - Blog LogRocket](https://i2.wp.com/blog.logrocket.com/wp-content/uploads/2020/06/node-modules-meme.jpeg?resize=730%2C525&ssl=1)

NPM ne facilite pas seulement le processus de recherche et de téléchargement de paquets, mais rend également plus facile le travail collaboratif sur un projet.

Sans NPM, il serait difficile de gérer les dépendances externes. Vous devriez télécharger manuellement les versions correctes de chaque dépendance lorsque vous rejoignez un projet existant. Et ce serait un vrai casse-tête.

Avec l'aide de npm, vous pouvez simplement exécuter **"npm install"** et il installera toutes les dépendances externes pour vous. Ensuite, vous pouvez simplement l'exécuter à nouveau chaque fois que quelqu'un de votre équipe en ajoute une nouvelle.

## Babel

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-2.png)

Babel est un compilateur ou transpileur JavaScript qui traduit le code ECMAScript 2015+ en code pouvant être compris par les anciens moteurs JavaScript.

Babel est le compilateur JavaScript le plus populaire, et des frameworks comme Vue et React l'utilisent par défaut. Cela dit, les concepts dont nous allons parler ici ne sont pas uniquement liés à Babel et s'appliqueront à tout compilateur JavaScript.

### Pourquoi avez-vous besoin d'un compilateur ?

"Pourquoi avons-nous besoin d'un compilateur, JavaScript n'est-il pas un langage interprété ?" vous pourriez demander si vous êtes familier avec les concepts de langages compilés et interprétés.

Il est vrai que nous appelons généralement quelque chose un "compilateur" s'il traduit notre code lisible par l'homme en un binaire exécutable pouvant être compris par le CPU. Mais ce n'est pas le cas ici.

Le terme transpileur peut être plus approprié puisqu'il s'agit d'un sous-ensemble d'un compilateur : les transpileurs sont des compilateurs qui traduisent le code d'un langage de programmation vers un autre langage (dans cet exemple, du JS moderne vers une version plus ancienne).

JavaScript est le langage des navigateurs. Mais il y a un problème avec les navigateurs : la compatibilité croisée. Les outils JavaScript et le langage lui-même évoluent rapidement et de nombreux navigateurs ne parviennent pas à suivre ce rythme. Cela entraîne des problèmes de compatibilité.

Vous voulez probablement écrire du code dans les versions les plus récentes de JavaScript afin de pouvoir utiliser ses nouvelles fonctionnalités. Mais si le navigateur sur lequel votre code s'exécute n'a pas implémenté certaines des nouvelles fonctionnalités dans son moteur JavaScript, le code ne s'exécutera pas correctement sur ce navigateur.

C'est un problème complexe car chaque navigateur implémente les fonctionnalités à une vitesse différente. Et même s'ils implémentent ces nouvelles fonctionnalités, il y aura toujours des personnes qui utilisent une version plus ancienne de leur navigateur.

Alors, que faire si vous voulez pouvoir utiliser les fonctionnalités récentes mais aussi que vos utilisateurs puissent consulter ces pages sans aucun problème ?

Avant Babel, nous utilisions des polyfills pour exécuter des versions plus anciennes de certains codes si le navigateur ne supportait pas les fonctionnalités modernes. Et lorsque vous utilisez Babel, il utilise des polyfills en arrière-plan et ne vous demande pas de faire quoi que ce soit.

### Comment fonctionnent les transpileurs/compilateurs ?

Babel fonctionne de manière similaire aux autres compilateurs. Il comporte des étapes d'analyse, de transformation et de génération de code.

Nous n'entrerons pas dans les détails ici sur son fonctionnement, car les compilateurs sont des choses compliquées. Mais pour comprendre les bases du fonctionnement des compilateurs, vous pouvez consulter le [projet the-super-tiny-compiler](https://github.com/jamiebuilds/the-super-tiny-compiler). Il est également mentionné dans la documentation officielle de Babel comme étant utile pour comprendre comment Babel fonctionne.

Nous pouvons généralement nous en sortir en connaissant les plugins et les présélections de Babel. Les plugins sont les extraits que Babel utilise en arrière-plan pour compiler votre code en versions plus anciennes de JavaScript. Vous pouvez considérer chaque fonctionnalité moderne comme un plugin. Vous pouvez consulter [ce](https://babeljs.io/docs/en/plugins/) lien pour voir la liste complète des plugins.

![Image](https://erinc.io/wp-content/uploads/2020/10/image.png)
_Liste des plugins pour ES5_

Les présélections sont des collections de plugins. Si vous souhaitez utiliser Babel pour un projet React, vous pouvez utiliser la présélection **@babel/preset-react** qui contient les plugins nécessaires.

![Image](https://erinc.io/wp-content/uploads/2020/10/image-1.png)
_Plugins de la présélection React_

Vous pouvez ajouter des plugins en modifiant le fichier de configuration de Babel.

### Avez-vous besoin de Babel pour votre application React ?

Pour React, vous avez besoin d'un compilateur car le code React utilise généralement JSX et JSX doit être compilé. De plus, la bibliothèque est construite sur le concept d'utilisation de la syntaxe ES6.

Heureusement, lorsque vous créez un projet avec **create-react-app**, il vient avec Babel déjà configuré et vous n'avez généralement pas besoin de modifier la configuration.

### Exemples d'un compilateur en action

Le site web de Babel dispose d'un compilateur en ligne et il est vraiment utile pour comprendre comment il fonctionne. Il suffit de saisir du code et d'analyser la sortie.

![Image](https://erinc.io/wp-content/uploads/2020/10/image-4.png)

![Image](https://erinc.io/wp-content/uploads/2020/10/image-5.png)

## Webpack

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image.png)

Webpack est un bundler de modules statique. Lorsque vous créez un nouveau projet, la plupart des frameworks/bibliothèques JavaScript l'utilisent désormais par défaut.

Si l'expression "bundler de modules statique" semble confuse, continuez à lire car j'ai quelques excellents exemples pour vous aider à comprendre.

### Pourquoi avez-vous besoin d'un bundler ?

Dans les applications web, vous allez avoir beaucoup de fichiers. C'est particulièrement le cas pour les applications monopages (React, Vue, Angular), chacune ayant ses propres dépendances.

Par dépendance, j'entends une instruction d'importation – si le fichier A doit importer le fichier B pour fonctionner correctement, alors nous disons que A dépend de B.

Dans les petits projets, vous pouvez gérer les dépendances de modules avec des balises `<script>`. Mais lorsque le projet devient plus grand, les dépendances deviennent rapidement difficiles à gérer.

Peut-être, plus important encore, diviser le code en plusieurs fichiers rend votre site web plus lent à charger. Cela est dû au fait que le navigateur doit envoyer plus de requêtes par rapport à un seul fichier volumineux, et votre site web commence à consommer une tonne de bande passante, à cause des en-têtes HTTP.

Nous, en tant que développeurs, voulons que notre code soit modulaire. Nous le divisons en plusieurs fichiers car nous ne voulons pas travailler avec un seul fichier contenant des milliers de lignes. Pourtant, nous voulons également que nos sites web soient performants, qu'ils utilisent moins de bande passante et qu'ils chargent rapidement.

Alors maintenant, nous allons voir comment Webpack résout ce problème.

### Comment fonctionne Webpack

Lorsque nous parlions de Babel, nous avons mentionné que le code JavaScript doit être transpilé avant le déploiement.

Mais la compilation avec Babel n'est pas la seule opération dont vous avez besoin avant de déployer votre projet.

Vous devez généralement l'uglifier, le transpiler, compiler le SASS ou SCSS en CSS si vous utilisez des préprocesseurs, compiler le TypeScript si vous l'utilisez... et comme vous pouvez le voir, cette liste peut facilement devenir longue.

Vous ne voulez pas avoir à gérer toutes ces commandes et opérations avant chaque déploiement. Ce serait bien s'il existait un outil qui faisait tout cela pour vous dans le bon ordre et de la bonne manière.

La bonne nouvelle – il existe : Webpack.

Webpack offre également des fonctionnalités comme un serveur local avec rechargement à chaud (ils l'appellent hot module replacement) pour améliorer votre expérience de développement.

Alors, qu'est-ce que le rechargement à chaud ? Cela signifie que chaque fois que vous enregistrez votre code, il est compilé et déployé sur le serveur HTTP local en cours d'exécution sur votre machine. Et chaque fois qu'un fichier change, il envoie un message à votre navigateur pour que vous n'ayez même pas besoin de rafraîchir la page.

Si vous avez déjà utilisé "npm run serve", "npm start" ou "npm run dev", ces commandes démarrent également le serveur de développement de Webpack en arrière-plan.

Webpack commence à partir du point d'entrée de votre projet (index) et génère l'arbre de syntaxe abstraite du fichier. Vous pouvez le considérer comme l'analyse du code. Cette opération est également effectuée dans les compilateurs, qui recherchent ensuite les instructions d'importation de manière récursive pour générer un graphe de dépendances.

Il convertit ensuite les fichiers en [IIFEs](https://developer.mozilla.org/en-US/docs/Glossary/IIFE#:~:text=An%20IIFE%20(Immediately%20Invoked%20Function,soon%20as%20it%20is%20defined.) pour les modulariser (rappelons que mettre du code à l'intérieur d'une fonction restreint sa portée). En faisant cela, ils modularisent les fichiers et s'assurent que les variables et fonctions ne sont pas accessibles aux autres fichiers.

Sans cette opération, ce serait comme copier et coller le code du fichier importé et ce fichier aurait la même portée.

Webpack fait beaucoup d'autres choses avancées en arrière-plan, mais cela suffit pour comprendre les bases.

## Bonus – ESLint

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-3.png)

La qualité du code est importante et aide à garder vos projets maintenables et facilement extensibles. Bien que la plupart d'entre nous, développeurs, reconnaissent l'importance du code propre, nous avons parfois tendance à ignorer les conséquences à long terme sous la pression des délais.

De nombreuses entreprises décident des normes de codage et encouragent les développeurs à respecter ces normes. Mais comment pouvez-vous vous assurer que votre code respecte les normes ?

Eh bien, vous pouvez utiliser un outil comme ESLint pour appliquer des règles dans le code. Par exemple, vous pouvez créer une règle pour imposer ou interdire l'utilisation de points-virgules dans votre code JavaScript. Si vous enfreignez une règle, ESLint affiche une erreur et le code n'est même pas compilé – il est donc impossible de l'ignorer à moins de désactiver la règle.

Les linters peuvent être utilisés pour appliquer des normes en écrivant des règles personnalisées. Mais vous pouvez également utiliser les configurations ESLint préétablies par de grandes entreprises technologiques pour aider les développeurs à prendre l'habitude d'écrire du code propre.

Vous pouvez consulter la configuration ESLint de Google [ici](https://github.com/google/eslint-config-google) – c'est celle que je préfère.

ESLint vous aide à vous habituer aux meilleures pratiques, mais ce n'est pas son seul avantage. ESLint vous avertit également des bugs/erreurs possibles dans votre code afin que vous puissiez éviter les erreurs courantes.

![Image](https://erinc.io/wp-content/uploads/2020/11/image-1024x717.png)

## Bonus – CI/CD (CircleCI)

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-4.png)

L'intégration/développement continu a gagné en popularité ces dernières années, car de nombreuses entreprises ont adopté les principes Agile.

Des outils comme Jenkins et CircleCI vous permettent d'automatiser le déploiement et les tests de votre logiciel afin que vous puissiez déployer plus souvent et de manière plus fiable sans avoir à passer par des processus de construction difficiles et sujets aux erreurs par vous-mêmes.

Je mentionne CircleCI comme produit ici car il est gratuit et fréquemment utilisé dans les projets JavaScript. Il est également assez facile à utiliser.

Passons en revue un exemple : Supposons que vous avez un serveur de déploiement/QA et votre dépôt Git. Vous souhaitez déployer vos modifications sur votre serveur de déploiement/QA, voici donc un exemple de processus :

1. Poussez les modifications vers Git
2. Connectez-vous au serveur
3. Créez un conteneur Docker et exécutez-le
4. Récupérez les modifications sur le serveur, téléchargez toutes les dépendances (npm install)
5. Exécutez les tests pour vous assurer que rien n'est cassé
6. Utilisez un outil comme ESLint/Sonar pour garantir la qualité du code
7. Fusionnez le code si tout est correct

Avec l'aide de CircleCI, vous pouvez automatiser toutes ces opérations. Vous pouvez le configurer pour effectuer toutes les opérations ci-dessus chaque fois que vous poussez une modification vers Git. Il rejettera la poussée si quelque chose ne va pas, par exemple un test qui échoue.

Je ne vais pas entrer dans les détails de la configuration de CircleCI car cet article est plus sur le "Pourquoi ?" de chaque outil. Mais si vous êtes intéressé à en apprendre plus et à le voir en action, vous pouvez consulter [cette série de tutoriels](https://www.youtube.com/watch?v=CB7vnoXI0pE&ab_channel=TheCodingTrain).

## Conclusion

Le monde de JavaScript évolue rapidement et de nouveaux outils gagnent en popularité chaque année.

Il est facile de réagir à ce changement en apprenant simplement à utiliser l'outil – nous sommes souvent trop occupés pour prendre le temps de réfléchir à la raison pour laquelle cet outil est devenu populaire ou au problème qu'il résout.

Dans cet article, j'ai choisi les outils que je pense être les plus populaires et j'ai partagé mes réflexions sur leur importance. J'ai également voulu vous faire réfléchir aux problèmes qu'ils résolvent plutôt qu'aux détails de leur utilisation.

Si vous avez aimé l'article, vous pouvez consulter et vous abonner à mon [blog](https://erinc.io/) où j'essaie d'écrire fréquemment. De plus, faites-moi savoir ce que vous en pensez en commentant afin que nous puissions échanger des idées ou vous pouvez me dire quels autres outils vous aimez utiliser :)