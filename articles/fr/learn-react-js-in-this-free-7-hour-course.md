---
title: Apprendre React JS dans ce cours gratuit de 7 heures
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-07-08T15:44:30.000Z'
originalURL: https://freecodecamp.org/news/learn-react-js-in-this-free-7-hour-course
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/reactcourse.png
tags:
- name: React
  slug: react
- name: youtube
  slug: youtube
seo_title: Apprendre React JS dans ce cours gratuit de 7 heures
seo_desc: 'According to Google trends, React is the most popular JavaScript frontend
  framework. Unless you''re in the U.S. state of Nebraska, that is. 😀


  Google Trends (React vs Angular)

  React is a declarative, efficient, and flexible JavaScript library for bui...'
---

Selon Google Trends, React est le framework frontend JavaScript le plus populaire. Sauf si vous êtes dans l'État américain du Nebraska, c'est-à-dire. 😀

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-21.png)
_Google Trends (React vs Angular)_

React est une bibliothèque JavaScript déclarative, efficace et flexible pour construire des interfaces utilisateur. Nous venons de publier un cours complet sur React sur la chaîne YouTube freeCodeCamp.org.

Thomas Weibenfalk a créé ce cours. Il est un excellent développeur et a développé de nombreux cours.

Dans ce cours, vous apprendrez React.js à partir des bases jusqu'à des sujets plus intermédiaires et avancés. Vous apprendrez en construisant une vraie application.

Vous apprendrez :

* React
* JSX
* Composants stylisés
* React Router
* État et Props
* Contexte
* CSS 
* Gestion des API
* Hooks 
* TypeScript
* Persistance de l'état dans SessionStorage
* Déploiement sur Netlify
* Et bien plus encore.

Regardez le cours complet sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/nTeuhbP7wdE) (7 heures de visionnage).

%[https://youtu.be/nTeuhbP7wdE]

## Transcription

(autogénérée)

react est l'un des frameworks JavaScript les plus populaires dans ce cours complet et bien fait.

Thomas Weibenfalk vous enseignera tout ce que vous devez savoir pour commencer à utiliser react.

Bonjour, et bienvenue.

Je suis Tomas vevo, développeur de Suède.

Et merci de vous être inscrit à ce cours.

Je suis en fait un peu plus fier de celui-ci, car j'ai créé beaucoup de cours au fil des années maintenant, mais celui-ci est le premier cours que j'ai jamais créé parce que j'aime react.

Et je voulais créer des cours.

Donc c'est la troisième itération, la troisième version, ce qui signifie que je l'ai beaucoup amélioré et écouté vos demandes sur ce que vous voulez dans le cours.

Donc je pense qu'il est en fait vraiment bon.

Il y a toujours place à l'amélioration, bien sûr, mais celui-ci, j'ai vraiment apprécié celui-ci.

Et c'était amusant de le faire aussi.

Donc, espérons que vous trouverez beaucoup de choses de base et intermédiaires, et peut-être quelques choses avancées à apprendre dans ce cours.

Et je pense que nous devons commencer.

Donc faisons cela.

Jetons un coup d'œil à l'application que nous allons construire dans ce cours.

Et c'est une belle petite application de films qui est basée sur l'API de la base de données de films.

Donc vous devrez créer un compte sur la base de données de films.

Mais nous allons faire cela dans la prochaine vidéo.

Donc j'ai pensé que je pourrais vous montrer l'application afin que vous ayez une petite idée de ce que nous allons construire dans ce cours.

Et celle-ci va toujours montrer le film le plus populaire ici, nous avons cette image héroïque.

Donc nous allons créer celle-ci.

Et nous avons aussi du texte, et nous avons un en-tête ici aussi, puis nous pouvons rechercher des films, ou des exemples, Star Wars.

Et nous verrons tous les films ici.

Donc c'est ainsi que fonctionne la fonctionnalité de base de cette application.

Et si nous cliquons sur le film, vous pouvez voir que nous obtenons toutes les données de ce film.

Donc c'est bien.

Nous allons montrer l'actrice et aussi quelques informations sur le film lui-même, nous pouvons voir les recettes, le budget et le temps de fonctionnement, par exemple.

Et ici, vous pourriez penser que vous pouvez aussi cliquer sur les acteurs.

Et oui, bien sûr, nous pourrions faire cela.

Mais je dois limiter ce tutoriel quelque part.

Donc ce cours ne va pas aller là.

Mais c'est une grande fondation, si vous voulez construire sur cette application.

Donc vous pouvez ajouter la fonctionnalité de montrer les informations sur les différents acteurs et ce genre de choses.

Nous avons aussi ce petit menu de fil d'Ariane qui apparaît, nous pouvons revenir à la page d'accueil.

Et dans cette version du cours, c'est la version trois, je vais vous montrer comment créer les styles aussi, cela va être assez rapide lorsque je montre les étoiles parce que je veux toujours avoir le focus principal sur react lui-même.

Donc c'est quelque chose de nouveau dans cette version trois de ce cours.

Et bien sûr, tout va être réactif, nous allons créer cela aussi, comme vous pouvez le voir ici, la grille, par exemple, avec les films, elle change en fonction de la taille de la fenêtre.

Donc c'est bien.

Donc c'est une application entièrement fonctionnelle.

Et pour être honnête, je suis assez fier de ce design, j'ai créé le design moi-même, bien sûr, je suis à la fois développeur et designer.

Donc c'est pourquoi j'aime faire des trucs de design aussi.

Et je pense que cela a l'air assez soigné.

En fait, je l'ai légèrement mis à jour, depuis les deux versions précédentes pour avoir l'air un peu plus moderne.

Mais je pense que c'est surtout oui, j'ai changé quelques couleurs, par exemple, en bas et ce genre de choses.

D'accord, donc c'est l'application.

Dans la prochaine vidéo, je vais parler de l'API de la base de données de films et de la façon dont vous pouvez vous inscrire pour obtenir votre propre clé API gratuite que je vais utiliser dans ce cours.

D'accord, parlons de l'API de la base de données de films.

C'est l'API que nous allons utiliser dans ce cours.

Et la base de données de films a une excellente API pour récupérer beaucoup de films, d'émissions de télévision et ce genre de choses, nous allons nous concentrer sur les films.

Donc c'est ce que nous allons faire ici.

Et vous pouvez vous inscrire pour un compte gratuit sur la base de données de films.

Donc allez simplement sur le site moviedb.org.

Et cliquez sur Rejoindre TMDB.

Et puis vous pouvez remplir un nom d'utilisateur et un mot de passe, un email et créer un compte.

Et lorsque vous avez créé un compte, vous recevez probablement un email où vous devez vous vérifier avant de pouvoir vous connecter.

Mais lorsque vous avez créé votre compte, assurez-vous de revenir sur la base de données de films et de cliquer sur connexion.

Et puis vous entrez votre nom d'utilisateur et votre mot de passe comme un site régulier sur lequel vous vous connectez.

D'accord, et puis vous êtes présenté avec ce genre de tableau de bord.

Je pense que c'est un tableau de bord.

Et la seule chose que vous avez à faire est d'aller ici vers votre profil et de cliquer sur ce bouton rond ici.

Et puis vous avez les paramètres ici, donc elle aura les paramètres.

Et puis dans le menu de gauche ici, vous pouvez voir que vous avez quelque chose qui s'appelle API.

Donc cliquez sur API, je suppose que je dois probablement flouter celui-ci parce que je ne veux pas vous montrer ma propre clé API.

C'est celui que nous utilisons, la clé API version trois auth.

Donc c'est celui que nous allons utiliser.

Donc assurez-vous de le sauvegarder quelque part pour l'instant parce que nous allons l'ajouter à notre application dans un petit moment.

Donc assurez-vous d'avoir un accès facile à celui-ci car nous allons le coller dans notre application dans un petit moment lorsque nous aurons démarré notre application avec quelque chose qui s'appelle create react app.

Et je vais en parler plus tard aussi.

Avant de commencer à créer notre application, je veux juste parler un peu de react et de ce que c'est.

Donc si vous allez sur le site Reactjs.org, vous pouvez en lire plus sur react.

Et c'est un excellent point de départ, si vous commencez tout juste avec react, ils ont différentes documentations, ils ont des tutoriels, et un blog et ce genre de choses.

Et vous pouvez lire tout ce que vous devez savoir pour commencer avec react.

Donc j'ai essayé de rendre ce cours un peu convivial pour les débutants.

Mais react est un peu au moins intermédiaire dans sa propre nature.

Donc il est difficile de le rendre vraiment, vraiment convivial pour les débutants.

Cela dépend aussi beaucoup de la façon dont vous apprenez les choses, j'aime apprendre les choses de cette manière orientée produit, où je construis simplement un produit et j'apprends en cours de route.

Donc je ne crée des cours que sur la façon dont je veux apprendre les choses moi-même, mais c'est très individuel.

Donc certains peuvent penser que ce n'est pas du tout convivial pour les débutants, et tant de choses que c'est le cas.

C'est pourquoi je recommande également de consulter reactjs.org pour lire sur les choses très, très basiques, au moins dans react.

Donc qu'est-ce que react ? Oui, React est une bibliothèque JavaScript pour construire des interfaces utilisateur, comme ils vous le disent ici, je pense, en fait, que cette phrase est un peu trompeuse, car vous utilisez react pour bien plus que simplement construire une interface utilisateur.

Par exemple, je construis beaucoup de choses, je construis de petits jeux, j'ai construit un jeu Pac Man, par exemple.

Et je construis toute la logique dans react aussi.

Donc ce n'est pas seulement la couche de vue, donc cela peut être un peu trompeur ici, je pense.

En pensant simplement que vous créez les composants pour la vue.

Mais ce n'est pas le cas, vous pouvez utiliser react pour bien plus si vous voulez le faire.

Et dans cette application, nous construisons tout dans react.

Donc nous avons tous les appels API et tout est fait à partir de react.

Donc c'est ainsi que nous allons l'utiliser dans ce cours.

Et react utilise le déclaratif peridinium.

Je ne sais même pas si je l'ai prononcé correctement.

Mais espérons que vous savez ce que je veux dire.

Donc react est déclaratif.

Mais par exemple, jQuery est impératif.

Et lorsqu'une chose est déclarative, vous expliquez, dans ce cas, l'interface utilisateur, comment elle va ressembler, vous n'avez pas à lui dire exactement comment vous voulez atteindre cet aspect, vous lui dites simplement que nous voulons que notre UI ressemble à une certaine manière.

Et puis react s'occupe du reste.

Par exemple, dans jQuery, nous devons attraper les éléments DOM.

Et nous devons modifier les éléments DOM.

Et nous devons les créer ligne par ligne, puis attacher l'élément au DOM lui-même.

Donc il peut y avoir beaucoup de code impliqué dans la réalisation de quelque chose de simple, en fait.

Mais dans react, par exemple, nous avons le Sauveur, il est basé sur les composants.

Donc nous créons un composant, puis nous disons simplement à react d'utiliser ce composant.

Et il le rendra dans le dôme pour nous.

Et cela sera plus clair au fur et à mesure que nous avancerons dans le cours et créerons nos propres composants et l'application elle-même.

Donc ne vous inquiétez pas si vous ne comprenez pas tout maintenant.

Donc c'est déclaratif, sa base de composants et apprendre une fois écrire n'importe où encore à vous dire ici, ils ne se soucient pas du reste de la pile technologique.

Donc c'est super, vous pouvez utiliser beaucoup de choses en combinaison avec react.

Donc qu'est-ce qu'un composant react ? Oui, nous pouvons regarder ici, par exemple, ici ils créent, c'est une classe et c'est un peu, j'aime l'appeler l'ancienne façon, les classes existent encore, je ne les utilise plus.

Et dans ce cours, nous allons nous concentrer sur la création de composants fonctionnels.

Et je vais vous en dire plus à ce sujet plus tard.

Et à la fin du tutoriel, lorsque nous avons terminé l'application, je vais aussi vous montrer comment convertir certains des composants, les composants avec état en composants de classe, juste au cas où, vous devez savoir comment créer des composants de classe aussi, car la réalité est, si vous commencez à travailler pour une entreprise ou un client, il y a probablement encore des composants qui sont encore des composants de classe.

Parce qu'il y a beaucoup d'applications faites en react qui sont faites avant que nous ayons l'état dans les composants fonctionnels.

C'est pourquoi vous deviez avoir une classe avant pour avoir de l'état en eux.

Et nous allons en parler plus tard aussi.

Donc c'est un composant qu'ils ont créé avec une classe et ils l'appellent Hello message.

Et comme vous pouvez le voir ici, ils utilisent quelque chose qui est très similaire au HTML régulier, ils ont cette balise ici avec un Hello message.

Et ce nom est ce qu'on appelle une prop qu'ils envoient, et nous allons en parler plus tard aussi, donc ne vous inquiétez pas de cela.

Mais ce n'est en fait pas du HTML.

C'est quelque chose qui s'appelle JSX.

Et c'est quelque chose que nous allons aussi apprendre dans ce cours.

Donc nous créons le composant ici, nous lui disons d'utiliser ce composant et react s'occupera du reste et créera ce div avec notre texte Hello.

Et dans ce cas, il va être le nom que nous envoyons avec une prop.

Donc le nom va être Taylor.

Il va taper Hello Taylor.

Comme vous pouvez le voir ici.

Donc c'est très, très soigné avec react, nous pouvons réutiliser ces composants dans notre application.

Donc c'est court sur ce qu'est react.

Et comme je vous l'ai dit, nous allons apprendre beaucoup plus de choses dans le cours lui-même lorsque nous créerons l'application.

Et espérons qu'à la fin du cours, vous aurez une meilleure compréhension de react et de sa puissance.

Parce que j'aime vraiment react, je suis vraiment passionné par l'utilisation de react.

Et en fait, ce cours est aussi quelque chose dont je suis très passionné.

Parce que c'est mon tout premier cours que j'ai créé.

Et c'est la troisième version, ce qui signifie que j'ai écouté les gens qui se sont inscrits à ce cours avant et changé des choses et ajouté des choses pour le rendre plus optimal et plus parfait.

Et espérons que vous allez apprécier ce cours.

Pour ce cours, je vous ai fourni un fichier zip que vous devriez télécharger avant de commencer le cours.

Et ce fichier zip contient quelques dossiers ici, comme vous pouvez le voir, et il peut sembler peut-être un peu différent lorsque je fais l'enregistrement de ce cours, car je ne l'ai pas vraiment enregistré encore, mais je pense qu'il ressemblera à ceci.

Mais s'il semble un peu différent, ce n'est pas grave.

Espérons que vous pouvez lire les noms des dossiers et comprendre ce qu'ils représentent.

Donc je vais vous fournir un dossier qui s'appelle files to be copied to the project folder.

Ce sont des fichiers que nous allons utiliser pour le cours.

Donc j'ai créé un fichier pour nous, l'API de configuration, donc nous n'avons pas à écrire nos propres fonctions pour récupérer les données.

Donc je vais vous montrer cela lorsque nous récupérerons les données de l'API, j'ai un fichier de configuration et un fichier d'aide.

Et je vais en parler plus tard aussi.

Et puis j'ai quelques images dont nous avons aussi besoin pour le cours.

Donc c'est pourquoi j'ai ce dossier que nous allons copier dans un projet lorsque nous l'aurons créé, et le dossier public, le fichier index.html, j'ai ceci ici, parce que j'utilise une police Google pour celui-ci.

Donc je l'ai déjà fourni dans l'index.html, donc nous n'avons pas à le faire nous-mêmes.

Donc c'est celui que nous devons copier plus tard.

Cette clé API est ensuite utilisée dans le dossier source dans mon fichier config.js.

Vous pouvez voir que nous l'avons ici, process.env.REACT_APP_API_KEY.

Et tout cela est géré à l'intérieur de Create React App.

Lorsque l'environnement de développement démarre ou crée tous les fichiers pour nous, etc.

Il s'occupera de ces variables vraiment importantes à marquer avec react_ avant le nom réel de la variable d'environnement et tout cela est quelque chose que j'ai créé pour vous.

Donc vous n'avez pas à vous en soucier.

Donc je crée les différentes ressources à partir du point de terminaison sur la base de données de films ici.

Et nous allons utiliser ces ressources dans le cours plus tard.

Et puis je vais en parler plus.

Donc j'ai différents points de terminaison pour la recherche, par exemple, et pour obtenir les films populaires.

Et c'était pour les vidéos bonus à la fin, où je crée la connexion, et le vote qui est également fourni avec l'API de la base de données de films, vous pouvez vous connecter avec votre compte, et voter pour un film, ou sur de vieux films.

Si vous voulez faire cela.

Ensuite, nous avons l'URL de base de l'image.

Celle-ci provient également de la base de données de films.

Donc ceux-ci sont fournis par l'API.

Donc utilisez-les selon leurs instructions.

Et nous avons une taille de fond, nous pouvons définir la taille du fond et la taille de l'affiche sur les images, nous pouvons définir différentes tailles ici et je les marque ici pour vous si vous voulez essayer de les changer et voir ce que cela fait.

Donc nous n'avons pas à penser plus à ceux-ci car je les ai configurés pour vous.

Et il y a aussi un fichier, il s'appelle API.js.

Et à l'intérieur de celui-ci, j'ai créé le code réel qui va récupérer les données, nous pouvons appeler ces fonctions plus tard lorsque nous récupérons les données.

Et nous n'avons pas à taper tout cela nous-mêmes.

Et bien sûr, je vais aussi parler plus de ces fonctions plus tard lorsque nous récupérons les films.

Donc celle-ci est pour récupérer tous les films, et celle-ci est pour récupérer un film.

Et puis nous avons celle-ci ici qui va récupérer les crédits.

Et en dessous ici, celles-ci sont toutes pour le matériel bonus aussi.

Donc vous n'avez pas à vous soucier de celles-ci dans la partie principale du cours.

Donc nous avons trois fonctions ici qui vont récupérer les données pour nous.

Donc c'est une chose que j'ai changée en fait, dans cette version du cours avant cela, nous avons créé celles-ci nous-mêmes dans le cours, mais je pense que c'est un peu avancé pour un cours pour débutants.

Et je pense aussi que cela détourne l'attention de react lui-même, car ceci est JavaScript, ce n'est pas un code spécifique à react.

Donc c'est pourquoi et je veux cette expérience, je veux que ce cours soit aussi un cours amusant.

Donc vous ne vous fatiguez pas et n'arrêtez pas le cours et ne le terminez pas.

Donc c'est pourquoi je les ai créés pour nous.

D'accord, donc c'est le config et le fichier API.

Et puis j'ai un autre fichier qui s'appelle helpers.js.

Et celui-ci contient deux fonctions, qui vont nous aider à calculer le temps et aussi à convertir en argent, car les nombres que nous obtenons de l'API doivent être convertis à la fois le temps et l'argent.

Donc je vais utiliser ceux-ci plus tard dans le cours aussi.

D'accord, donc créez le fichier .env, créez une variable, React_app_API_key en majuscules, égale et puis vous collez votre clé API.

Sinon, cela ne fonctionnera pas car vous ne pouvez pas accéder à l'API.

Une chose vraiment importante à noter ici est que cette variable d'environnement ne sera pas sécurisée, car elle sera visible dans le client.

Donc ne pensez pas que celle-ci ne s'affichera pas dans le navigateur, bien sûr, vous devez la chercher.

Mais si vous êtes bon pour chercher à travers le code, vous serez en mesure de trouver cette clé API.

Donc ce n'est pas une manière sécurisée de fournir une clé API si vous voulez la cacher du navigateur.

Dans notre cas, ce n'est pas ce genre de clé secrète, cela n'a pas d'importance.

Et pour le bien du cours, il serait trop avancé de créer un système qui la cachera complètement pour nous.

Donc notez, celle-ci ne sera pas sécurisée dans le client.

Avant de continuer, je veux parler d'un aspect vraiment important de react que je pense que beaucoup de gens oublient en fait.

Et c'est lorsque nous créons des choses avec react, nous utilisons aussi quelque chose qui s'appelle JSX.

Et cela signifie JavaScript, XML.

Et si nous regardons ici, je suis sur la page Reactjs.org maintenant, et ils nous montrent ici comment créer le composant.

Et c'est un composant de classe.

Et comme je vous l'ai dit avant, nous allons créer des composants fonctionnels.

Donc nous ne allons pas créer des composants de classe pour cette application.

Mais ils utilisent JSX.

Ici, et c'est JSX.

Vous pouvez penser que c'est du HTML, mais ce n'est en fait pas du HTML, c'est du JSX.

Et JSX est quelque chose qui est vraiment génial à utiliser en combinaison avec react, car nous pouvons rendre nos différents composants comme ceci en utilisant une syntaxe de type HTML.

Je pense que beaucoup de gens l'oublient en fait.

Parce que je ne connais pas exactement le pourcentage, mais je pense qu'au moins 99% des applications utilisent JSX.

En combinaison avec react, certaines personnes ne l'utilisent pas.

Et c'est ce dont je vais parler ici.

Parce que vous pouvez créer des composants sans JSX dans react.

Et c'est si nous faisons défiler vers le bas ici, vous utilisez quelque chose qui s'appelle create element sur les objets React react.createElement, nous spécifions si nous voulons des props.

Et puis nous spécifions les éléments enfants pour cet élément.

Et vous pouvez voir ici, React.createElement, nous avons le composant que nous voulons créer, nous avons les props, et aussi nous avons les enfants et c'est la syntaxe de propagation en JavaScript, il a six.

C'est pourquoi ils utilisent trois points ici pour expliquer cela.

Celui-ci ici est en fait le même que celui-ci, celui-ci ici, sera transpilé en react.createElement.

Mais il ne serait pas pratique d'utiliser react.createElement pour chaque composant et tout ce que vous faites dans react, vous pouvez voir que ce n'est pas très lisible, et cela deviendra un peu désordonné.

Et je pense en fait que react ne serait pas très amusant à utiliser si vous l'utilisez de cette manière.

Donc je vais juste vous montrer comment créer un élément avec react.createElement aussi.

Et dans la prochaine vidéo, je vais parler plus de JSX.

Mais maintenant je vais vous montrer juste un petit exemple de la façon dont vous pouvez créer un élément avec react.createElement.

Donc revenons à notre terminal et assurons-nous que notre environnement de développement est en cours d'exécution.

Donc NPM start, utilisez toujours NPM.

Start, lorsque vous démarrez votre serveur de développement, vous pouvez voir que nous l'avons en cours d'exécution ici maintenant.

Ensuite, je reviens à Visual Studio code.

Et je vais être dans le fichier app.js.

Pour celui-ci, il est à l'intérieur du dossier src.

Et c'est en quelque sorte le cœur de notre application, nous avons le index.js.

C'est le fichier de démarrage de l'application.

Et vous pouvez voir qu'ils importent le composant app ici, ces importations sont la syntaxe e6 pour l'importation.

Donc nous pouvons importer un modèle.

Et dans ce cas, le modèle est un composant.

Et il s'appelle app.

Donc je l'importe ici.

Et puis il est utilisé ici et celui-ci est JSX.

Donc c'est le cœur de notre application, nous avons une bibliothèque qui s'appelle react.

Et nous avons react Dom parce que react peut être utilisé pour d'autres choses que le DOM, par exemple, vous pouvez créer des applications natives avec react.

Mais nous allons utiliser la bibliothèque react DOM.

Et celle-ci est déjà configurée avec create react app pour nous.

Donc vous pouvez voir que depuis le React Dom que nous importons ici, nous appelons la méthode render.

Et nous lui donnons le composant que nous voulons rendre.

Et nous lui disons où nous voulons le rendre.

Donc depuis le document.getElementById, nous obtenons l'élément root.

Donc si nous regardons à l'intérieur de la racine publique et de l'index.html, vous pouvez voir que nous avons un div ici, qui s'appelle root.

Et c'est à l'intérieur de cette div, que nous allons rendre notre application complète dans le nœud public, et revenir au fichier index.js.

Donc nous disons à react de rendre notre application dans une div qui s'appelle route.

Et c'est aussi dans quelque chose qui s'appelle react strict mode.

Ce n'était pas comme ça avant.

Mais c'est un défaut.

Maintenant avec create react app que le strict mode est en fait génial.

Il va faire quelques vérifications supplémentaires si vous faites des choses que vous ne devriez pas faire lorsque vous codez votre application.

Donc c'est toujours une bonne idée d'utiliser le strict mode dans react.

D'accord, donc revenons au fichier app.js.

Et comme vous pouvez le voir, ici, nous avons cet élément ici, nous avons la div qui s'appelle AP.

Et je rends ici start here.

Et c'est celui que nous avons vu avant, lorsque nous avons démarré l'application.

Vous n'avez pas à taper cela si vous ne le voulez pas, parce que je veux vous montrer cela, cela n'a rien à voir avec l'application que nous allons construire.

Donc je vais créer un petit composant maintenant.

Et puis je vais le supprimer et nous pouvons continuer à créer notre application.

Je vais le faire avec une fonction fléchée, j'aime utiliser les fonctions fléchées, ils ne le font pas ici.

Mais vous pouvez changer celui-ci si vous voulez en une fonction fléchée const app égale, et puis nous créons une flèche ici comme ça, je suis habitué à utiliser les fonctions fléchées.

Donc je les utilise pour les composants aussi.

Donc const, je vais créer un composant qui s'appelle store, et j'ai une fonction fléchée.

Et puis depuis react, nous importons react ici, vous devez toujours importer react en haut, et un autre appel create element, j'ai une parenthèse, je vais créer une div.

Et puis nous n'allons pas avoir de props parce que nous n'avons pas encore parlé des props.

Donc je le mets à null, et puis je vais rendre l'écran.

C'est une petite étoile comme ça, et je vais supprimer la sidebar, nous pouvons voir le composant ici.

Donc c'est au lieu d'utiliser JSX.

Et si nous voulons rendre celui-ci, au lieu de retourner celui-ci ici, je vais retourner le store.

Et comme c'est la fonction maintenant, je dois aussi l'appeler comme ceci, l'enregistrer.

Et puis je vais revenir à l'application.

Et vous pouvez voir que c'est une petite étoile, donc il rend parfaitement.

Et ce n'est qu'un petit exemple.

Et je veux juste pour vous de noter que vous n'avez pas besoin d'utiliser JSX.

Et c'est en fait la fonctionnalité React à son cœur.

Donc vous n'avez pas à utiliser JSX.

Mais nous allons utiliser JSX parce que c'est génial, et c'est amusant de travailler avec.

Et je pense en fait que ce serait un petit l créer des applications sans JSX au moins je pense.

Donc, je supprime tout ce que j'ai créé ici et j'enregistre le fichier.

Encore, juste pour être sûr que cela fonctionne stocké ici.

Et cela fonctionne et c'est génial.

Donc c'est un peu sur react.createElement et l'utilisation de react sans JSX, juste une petite note sur celui-ci, je ne vais pas aller plus loin dans le sujet, car je ne pense pas que ce soit vraiment pertinent d'utiliser react sans JSX.

Donc c'est pourquoi.

D'accord, j'ai parlé un peu de l'utilisation de react sans JSX.

Mais je ne pense pas en fait que ce soit une bonne idée.

C'est pourquoi je veux aussi parler un peu de JSX avant de continuer avec cette application.

Donc JSX signifie JavaScript, XML, et il est assez similaire au HTML régulier.

Donc si nous regardons ici, vous pouvez voir qu'ils créent une balise h1 ici qui dit hello word.

Et cela ressemble exactement au HTML brut.

Mais comme ils le disent ici, cette syntaxe de balise amusante n'est ni une chaîne ni du HTML, je ne pense pas en fait que ce soit une balise amusante à dire ici, mais d'accord, vous obtenez l'ID, pourquoi JSX.

Nous pouvons lire ici plus sur pourquoi nous utilisons JSX.

Et la chose principale ici est qu'ils ne veulent pas mettre la mise en page dans un fichier et la logique dans un autre fichier, ils veulent les avoir combinés dans un seul fichier.

Et cela peut sembler effrayant pour certains, car il y a quelques années, vous ne deviez jamais les mélanger.

Mais dans react, cela fonctionne vraiment bien.

Et comme ils le disent ici, les composants react contiennent à la fois la mise en page et la logique.

Donc JSX est quelque chose qui est créé pour ressembler beaucoup au HTML, il y a quelques différences.

Et je voulais en parler ici.

Parce que dans ce cas, nous créons un élément h1.

Et cela ressemble exactement à la même chose.

Mais il y a des choses qui diffèrent du HTML régulier.

Et par exemple, vous pouvez voir que vous pouvez intégrer des expressions JavaScript ici.

Pour la zone de source dans la balise image, par exemple, vous pouvez utiliser des accolades, et puis vous intégrez votre expression JavaScript.

Et c'est super génial que vous puissiez les combiner de cette manière.

Et aussi, comme vous regardez l'index de tabulation, il est en casse camel qui diffère du HTML.

Et ils le disent aussi ici semble que JSX est plus proche de JavaScript que de HTML, react, Dom utilise la convention de nommage des propriétés en casse camel au lieu des noms d'attributs HTML.

Donc rappelez-vous cela, que vous devez utiliser la casse camel dans JSX.

Et il y a quelques différences.

Par exemple, lorsque vous définissez une classe sur un élément, vous n'utilisez pas le mot-clé class, vous utilisez className, en casse camel.

Et ils le mentionnent aussi ici.

Et cela m'a pris un peu de temps pour m'y habituer.

Et non, je tape en fait className lorsque je tape le HTML régulier.

Et aussi, il est bon de savoir que JSX est assez sûr, il empêche les attaques par injection et ce genre de choses.

Donc je pense que vous allez apprendre beaucoup sur JSX.

Au fur et à mesure que nous avancerons dans ce cours, car nous allons utiliser des exemples pratiques dans ce cours, la partie la plus importante est de se souvenir que JSX n'est pas HTML.

Et il utilise aussi la casse camel lorsque vous créez un attribut.

Avant de plonger et de créer nos composants avec l'état et les props, et toutes ces choses vitales dans react, vous pouvez vous asseoir, vous détendre, prendre un verre, prendre une bière, prendre une tasse de thé, ou ce que vous buvez.

Et écoutez-moi simplement dans cette vidéo, où je vais parler un peu des props et de l'état dans react, la première chose que vous pouvez faire est d'imaginer que ceci est une pièce vue d'en haut.

Et le cercle gris ici est une lampe qui n'est pas allumée.

Et l'orange est une lampe qui est allumée, chacune de ces lampes a un interrupteur qui est souvent allumé.

Donc si je clique sur celui-ci ici, je peux allumer cette lumière et l'interrupteur va changer pour allumé.

Et celui-ci je peux l'éteindre.

Donc les deux lampes sont éteintes, et j'allume celle-ci, et j'allume celle-ci.

Et cela est possible parce que je peux utiliser l'état dans react.

Donc j'ai deux états pour les lampes.

J'ai un état pour la première lampe et un pour la seconde lampe qui est un booléen qui indique si la lampe est allumée ou éteinte.

Mais si nous y réfléchissons, nous avons en fait un état de la pièce aussi, car nous avons besoin d'un état aussi pour que l'interrupteur change de éteint à allumé.

Parce que ceux-ci sont en quelque sorte liés ensemble de sorte que vous pouvez regarder l'état sous différents angles.

Dans ce cas, je vais regarder l'état du point de vue de la pièce.

Donc je n'ai pas placé les états dans les lampes ou dans les interrupteurs, j'ai placé les états dans la pièce elle-même car nous avons un état de pièce et pour la pièce, il va être si les lampes et les interrupteurs sont allumés ou éteints.

Donc nous avons un état pour la pièce elle-même.

Et c'est ce dont je parlais dans la documentation React, par exemple, ils vous disent que vous pouvez remonter l'état à un composant parent si vous voulez utiliser cet état dans plusieurs composants enfants.

Parce que si nous plaçons l'état dans la lampe elle-même, par exemple, nous ne pouvons accéder à cet état que dans la lampe et ses composants enfants.

Bien sûr, nous pourrions placer les interrupteurs comme un enfant de la lampe, mais ce ne serait pas la manière la plus efficace de le faire.

Et cela compliquerait les choses si vous voulez réutiliser votre code.

Donc ce que j'ai fait ici, c'est que j'ai cette pièce ici et j'ai placé les composants dans la pièce et je vais aussi avoir l'état dans la pièce afin que nous puissions utiliser cet état à la fois pour les lampes et les interrupteurs et je vais vous montrer comment faire cela maintenant, et aussi parler un peu plus de l'état et des props.

Donc si nous regardons à l'intérieur du code ici, c'est l'application que j'ai créée pour vous.

Vous pouvez aussi l'ouvrir à partir des fichiers sources de ce cours, je l'ai fourni là.

Donc j'ai le fichier index, le fichier index standard qui montre le composant app, et le composant app va en fait être la pièce.

Donc je pourrais aussi le nommer pièce car c'est en fait le composant pièce.

Et comme vous pouvez le voir ici, dans le composant pièce, je crée deux états.

Dans react, lorsque vous créez un état avec des hooks, vous utilisez quelque chose qui s'appelle le hook use state.

Avant que nous ayons des hooks, nous devions utiliser des classes pour avoir des états en eux.

Donc vous ne pouviez jamais créer un composant fonctionnel qui a des états en eux.

Mais maintenant nous avons des hooks, et cela signifie que nous pouvons avoir des composants fonctionnels avec état.

Et c'est génial.

Donc lorsque nous appelons ce hook use state, nous pouvons l'initialiser avec une valeur initiale.

Dans ce cas, je lui donne false, car je veux que cette lampe soit éteinte initialement.

Ensuite, je fais quelque chose qui s'appelle la destruction e6 ici sur la destruction de ce tableau que je reçois du hook use state.

Donc nous pouvons nommer notre état ici comme nous le voulons.

Dans ce cas, je le nomme is lamp one on et ensuite nous avons le setter pour l'état setter is lamp one on.

Et il y a quelques choses que vous devez savoir sur l'état dans react.

Et la première est que vous devez considérer l'état comme immuable, vous ne devez jamais muter l'état, cela signifie que vous devez toujours utiliser le setter d'état que vous obtenez pour définir l'état dans react.

Si vous modifiez l'état directement, par exemple, essayez de changer celui-ci.

Cela signifie que votre composant ne se réaffichera pas.

Et ce n'est pas bon.

Et cela peut aussi causer beaucoup de problèmes dans le futur pour vous dans l'application.

Mais si vous utilisez le setter et changez l'état et ne mutez pas l'état, votre composant se réaffichera et mettra à jour le DOM.

Et c'est ainsi que les choses fonctionnent dans react, vous mettez à jour le DOM lorsque vos composants se réaffichent.

Et une autre chose avec les composants fonctionnels est que nous pouvons ajouter autant d'états que nous voulons avec le hook use state dans les composants de classe, vous ne pouvez avoir qu'un seul état, donc vous devez créer un objet avec différentes propriétés pour contenir votre état.

Donc c'est super génial, nous pouvons diviser les états maintenant en fonction de la manière dont nous voulons structurer l'état.

Dans ce cas, j'ai créé deux états, j'en ai un pour la lampe un, et j'en ai un pour la lampe deux.

Donc ils font exactement la même chose.

La seule différence ici est lorsque je l'initialise, je mets celui-ci à vrai et cela allumera la lampe deux.

D'accord, maintenant j'ai deux fonctions.

Et celles-ci vont être appelées lorsque nous cliquons sur l'interrupteur.

Donc j'en ai une pour l'interrupteur un et une pour l'interrupteur deux, vous pourriez en avoir une seule à la place.

Mais je veux vraiment, vraiment clarifier le fonctionnement des choses.

Donc c'est pourquoi j'en ai créé deux.

Donc nous avons une fonction pour le commutateur un et une pour le commutateur deux.

Et celui-ci va définir is lamp one, c'est le setter pour l'état un pour la lampe un.

Et ce que je fais ici, c'est que je lui fournis une fonction en ligne.

Et lorsque vous fournissez le setter d'état avec une fonction, il sera appelé avec l'état précédent.

Donc dans ce cas, je vais inverser cette valeur booléenne.

Donc lorsque je clique sur le bouton, la première fois cette valeur va être vraie au lieu d'être fausse initialement.

Et celle-ci pour le bouton deux va être fausse car elle est vraie.

D'accord, ce sont les fonctions pour les interrupteurs.

Donc si nous regardons le JSX ici, ce que nous retournons au dôme, celui-ci est un composant de pièce.

Et si je monte ici, vous pouvez voir que c'est le composant de style que nous allons aussi beaucoup discuter dans ce cours, je crée un composant de style, qui est un div ici.

Donc je définis un style sur celui-ci sur la pièce elle-même, je le fais 500 pixels de largeur et 500 pixels de hauteur, puis je définis une bordure dessus, et la marge zéro dans l'ordre va le centrer sur l'écran.

Donc tout est enveloppé dans ce composant de pièce, puis j'ai un composant, qui est la lampe, je vais en parler dans une seconde.

Et j'ai aussi l'interrupteur.

Donc nous avons l'état dans ce composant d'application.

C'est la pièce.

Donc c'est là que je rassemble tous les états pour cette petite application simple.

Et de cette façon, je peux utiliser cet état à la fois dans le composant lampe et l'interrupteur.

Parce que comme vous pouvez le voir ici pour le composant lampe, j'ai créé quelque chose qui s'appelle props, props est quelque chose que vous pouvez créer et qui sera envoyé avec votre composant que vous créez, props est un objet.

Donc vous pouvez créer autant de propriétés sur cet objet que vous le souhaitez.

Dans ce cas, j'ai créé une prop de lampe allumée.

Donc celle-ci sera envoyée dans le composant lampe dans l'objet prop.

J'ai aussi créé une prop qui s'appelle position.

Et c'est ainsi que je peux faire apparaître la lampe à gauche ou à droite dans la pièce.

Et lamp on va être l'état des lampes.

Donc celui-ci va être un booléen.

Et de cette façon, ce composant saura si la lampe est allumée ou éteinte.

Et je vais vous le montrer dans une seconde.

Et je fais la même chose avec un interrupteur.

Et pour celui-ci, j'ai le callback comme je l'ai montré ici.

Je donne à celui-ci une prop que j'appelle callback.

Il n'a pas besoin d'être appelé callback, c'est le nom que j'ai choisi.

Et le switch on, je vais lui donner un état de lampe pour celui-ci.

Donc vous pouvez voir que j'utilise les états de lampe à la fois pour la lampe et les interrupteurs.

Et c'est ce dont je parlais avant, si nous créions l'état pour la lampe dans la lampe elle-même, nous ne pourrions pas accéder à cet état pour l'interrupteur, alors nous devons créer l'interrupteur comme un enfant de la lampe.

Et ce n'est pas bon, comme vous pouvez probablement le voir maintenant, car maintenant nous pouvons placer autant de lampes et d'interrupteurs que nous voulons dans notre pièce.

Donc ce serait beaucoup plus difficile à faire si nous plaçons l'état dans la lampe elle-même.

Et j'ai aussi une prop de position pour l'interrupteur.

Donc entrons dans le composant lampe que j'ai créé ici.

J'ai aussi un div wrapper pour celui-ci qui est un composant stylisé.

Donc j'enveloppe tout dans ce div.

Et la chose intéressante avec les composants stylisés est qu'ils peuvent aussi avoir des props car ils sont aussi des composants react valides.

Donc nous pouvons utiliser des props dans nos composants stylisés pour modifier notre CSS.

Et c'est l'une des super forces avec les composants stylisés, je pense, car comme vous pouvez le voir ici, c'est ce qu'on appelle un littéral de modèle.

Et dans ce littéral de modèle, nous pouvons saisir les props qui sont envoyées dans ce composant.

Donc dans ce cas, je crée un signe dollar et des accolades, et je peux utiliser une expression JavaScript.

Et j'ai cette fonction en ligne ici qui obtient les props.

Donc si nous regardons le composant wrapper ici, vous pouvez voir que j'envoie aussi une prop lamp on et la position.

Donc je transmets simplement ces props qui sont initialement envoyées dans le composant lampe.

Donc je les obtiens dans le composant lampe, et puis je les transmets aussi au composant wrapper.

C'est le composant stylisé.

Et en faisant cela, je peux, par exemple, vérifier ici, si les props.dot position est égal à gauche, alors je vais définir la valeur de gauche à 20 pixels.

Sinon, je la définis à trois ou en dessous de deux pixels, et cela la placera à droite dans la pièce.

Donc de cette façon, je peux modifier mon CSS et le rendre très, très dynamique.

Donc c'est vraiment génial que vous puissiez aussi utiliser des props dans les composants stylisés.

D'accord, c'est ainsi que fonctionnent les composants stylisés et les props.

Donc si nous regardons le composant lampe ici, j'envoie ces props ici.

Et ce que je fais ici, c'est que j'utilise la destructuration iOS six.

Donc à partir des objets que nous obtenons et que vous appelez généralement props, je destructure ces valeurs qui sont envoyées, si je ne faisais pas la destructuration ici, et que je faisais simplement comme ceci, vous pouvez voir qu'il me le demande maintenant, alors je dois taper props.dot et props.not parce que les props est un objet, donc je dois saisir ces propriétés spécifiques de la bascule.

Mais si je les destructure comme je le fais ici, je n'ai pas à taper cela à chaque fois.

Donc je structure simplement les propriétés ici à la place.

Et il y a quelques choses que vous devez savoir sur les props car elles diffèrent de l'état.

Et la principale différence est que les props sont passées dans les composants.

Et vous ne devez jamais jamais changer les props dans le composant qui reçoit les props, les valeurs des props sont changées par le parent qui envoie les props au composant.

Donc si les props changent dans le parent, cela va aussi déclencher un nouveau rendu de ce composant ici.

Donc ne changez jamais les valeurs des props dans ce composant, vous pouvez changer l'état dans le composant avec un setter d'état.

Et c'est ainsi que vous pouvez, par exemple, déclencher un nouveau rendu.

Lorsque vous changez l'état dans un composant.

Donc c'est bien, vous devez changer l'état dans le composant avec les setters.

Mais une prop ne doit jamais être changée dans un composant qui reçoit les props.

Lorsque la valeur de la prop change, ce composant se réaffichera et il aura la nouvelle valeur dans les props.

Donc c'est ainsi que fonctionnent les props.

D'accord, nous pouvons vérifier l'interrupteur.

Aussi, je fais la même chose ici, je destructure les props ici.

Et j'ai ce composant bottom.

C'est le composant star.

Et je le modifie avec les props ici aussi.

Donc je fais exactement la même chose ici.

Et vous pouvez voir ici que nous envoyons le callback, c'est la fonction que j'ai dans le composant app ici.

Donc c'est celui que j'envoie avec une prop de callback dans l'interrupteur.

Et puis j'ai mon bouton, et le bouton a un gestionnaire onClick, un gestionnaire onClick va déclencher cette fonction de callback.

Et cela rend ce composant très dynamique car en utilisant les props, vous pouvez rendre votre composant dynamique.

Et vous pouvez l'utiliser dans différentes situations.

Dans ce cas, je peux envoyer n'importe quelle fonction de callback que je veux être déclenchée lorsque je clique sur le bouton.

Donc cela signifie que je peux utiliser ce bouton dans différentes situations.

Dans ce cas, je montre aussi l'interrupteur marche et arrêt parce que j'ai envoyé la prop switch on.

Donc il ne sera probablement pas utile, moins que ce cas d'utilisation spécifique.

Mais si vous voulez, vous pouvez utiliser ce bouton pour autre chose, pour déclencher une lampe pour l'allumer ou l'éteindre, vous pouvez allumer ou éteindre autre chose et avoir une autre fonction de callback et cela fonctionnera.

Donc c'est à quoi servent les props.

Aussi, vous pouvez rendre vos composants dynamiques et réutilisables en leur donnant quelques props.

Et en utilisant ces props à l'intérieur du composant.

Vous pouvez adapter votre composant et changer la logique, vous pouvez changer le JSX et ce qu'il doit rendre et ce genre de choses.

Donc cela est vraiment utile pour nous.

Props pour cela.

D'accord, c'est court sur l'état et les props.

J'espère que cela vous a donné un aperçu avant que nous commençons à créer les nôtres.

Donc passons à la vidéo suivante, je vais parler plus des composants stylisés et de ce qu'ils sont.

Il y a une chose de moins dont je veux parler avant de commencer à créer du code pour de vrai.

Et c'est les composants stylisés.

Parce que dans la prochaine vidéo, nous allons créer un style global pour notre application.

Donc juste une petite discussion sur les composants stylisés et pourquoi c'est si génial.

Et je pense que le plus grand avantage est que vous obtenez du CSS scopé.

Et cela signifie que vous pouvez avoir les mêmes noms de classe pour différents composants, cela n'a pas d'importance car il est scopé à ce composant.

Et le numéro deux est que vous pouvez utiliser une syntaxe, un peu comme sass, par exemple, vous pouvez imbriquer des choses, et vous n'avez pas besoin d'avoir des polyfills, et ce genre de choses, il va créer tout cela automatiquement pour vous.

Et le numéro trois, est que vous pouvez avoir des props à l'intérieur.

Et les props sont quelque chose dont nous allons beaucoup parler dans ce cours, car c'est une partie essentielle dans react.

Et cela signifie que vous pouvez modifier le CSS en envoyant différentes props à vos styles, vous n'avez pas besoin de savoir exactement maintenant comment fonctionnent les props, car nous allons en parler plus tard dans le cours.

Et aussi, vous pouvez utiliser juste du CSS régulier, et c'est super génial aussi.

Donc ce sont quelques avantages que les composants stylisés vous fourniront lorsque vous les utiliserez dans votre application.

Donc nous avons déjà installé cette bibliothèque.

Et lorsque vous l'utilisez, vous devez importer quelque chose qui s'appelle style, je pense qu'ils ont un exemple ici, ici, input styled from styled components.

Et style est un objet qui contient différentes propriétés.

Par exemple, dans ce cas, ils veulent styliser un bouton.

Donc ces propriétés correspondent à ce qu'elles sont appelées en HTML.

Donc si vous voulez styliser un bouton, si vous voulez créer un composant stylisé, qui est un bouton, vous utilisez style.dot button, et puis vous avez un littéral de modèle.

Donc c'est quelque chose qui s'appelle un littéral de modèle de balise.

Et c'est une fonction que vous appelez avec un littéral de modèle.

Donc c'est la syntaxe e6 en JavaScript.

Et c'est super génial, car si nous remontons ici, encore, vous pouvez voir, nous avons ce littéral de modèle.

Ici, vous avez la première backtick.

Et vous avez la fin de la backtick ici.

Et à l'intérieur de celle-ci, nous pouvons écrire notre CSS.

Dans ce cas, ils utilisent style.dot A, car ils veulent styliser une balise a.

Et puis ils font quelques trucs ici, du CSS régulier.

Mais ici, il se passe quelque chose.

Qui n'est pas du CSS régulier.

Et c'est parce que nous utilisons un littéral de modèle ici, nous pouvons utiliser des expressions JavaScript à l'intérieur de ce littéral de modèle.

Et lorsque vous voulez utiliser une expression à l'intérieur d'un littéral de modèle, vous le faites avec un signe $1, et vous l'enveloppez à l'intérieur d'accolades.

Et puis vous pouvez avoir n'importe quelle expression JavaScript que vous voulez à l'intérieur de celle-ci, et elle l'interpolera dans la chaîne.

Et dans ce cas, vous pouvez voir qu'ils ont leurs props, et ils ont une fonction fléchée en ligne.

Et à partir des props, ils attrapent une prop.

Qui s'appelle primary.

Et vous pouvez définir ce CSS conditionnellement, en fonction de cette prop primary.

Et nous allons en parler plus tard, comme je vous l'ai dit, donc ne soyez pas intimidé.

Si vous ne comprenez pas cette syntaxe maintenant, espérons que vous la comprendrez pleinement lorsque ce cours sera terminé.

C'est juste une petite introduction, avant de créer le style global.

Et nous allons le faire dans la prochaine vidéo.

Il est temps de commencer à coder.

Et nous allons commencer par créer quelques styles globaux.

La première chose que vous devez faire est de démarrer votre environnement de développement.

Et vous le faites en naviguant à l'intérieur du dossier de votre application.

Et puis vous tapez NPM start, et cela va tout démarrer pour vous.

Et espérons qu'il ressemble à ceci, il devrait dire start here.

Et c'est toujours une bonne idée d'avoir votre console ouverte.

Je suis sur Chrome maintenant.

Donc cela ressemble à ceci.

Et je peux aussi recommander une extension.

Qui s'appelle react developer tools.

Et puis vous aurez accès à quelque chose qui s'appelle components ici.

Et si nous l'ouvrons, nous pouvons voir notre application ici.

Mais dans ce cas, nous n'avons pas encore de composants.

Donc il va juste montrer le composant app ici.

Mais c'est un excellent outil lorsque vous développez des choses dans react.

Donc fortement recommandé d'installer react developer tools.

D'accord, donc passons à notre application à l'intérieur de Visual Studio code, ou quel que soit l'IDE que vous utilisez et à l'intérieur du dossier src, nous allons créer un nouveau fichier que je vais appeler que je vais appeler global style, en majuscules G et S.js.

Donc cela va contenir tous les styles globaux pour notre application.

Et nous allons créer un style global avec des composants stylisés.

Donc c'est pourquoi nous devons importer une chose spéciale des composants stylisés.

Qui s'appelle create global style.

Donc nous commençons par faire cela import curly brackets.

Create Lobel style camel case, cela signifie qu'il y a une majuscule D et une majuscule S.

Et nous avons importé de style dash components.

Et c'est ainsi que nous importons le module avec la syntaxe e6.

Dans ce cas, ce n'est pas ce qu'on appelle l'exportation par défaut de cette bibliothèque.

Donc c'est pourquoi nous le saisissons à l'intérieur des accolades, nous allons créer des exportations par défaut de nos différents composants.

Et puis nous n'avons pas besoin d'utiliser les accolades.

Mais je vais vous montrer cela plus tard lorsque nous créerons notre premier composant.

D'accord, donc nous avons cette méthode create global style que nous avons importée.

Ici, nous allons utiliser un style global à l'intérieur de notre composant app plus tard, ce qui signifie que nous voulons l'importer ici et l'utiliser ici dans le JSX.

Donc cela signifie aussi que nous devons exporter ce composant stylisé de ce fichier, donc export.

Et c'est une const.

Aussi syntaxe e6, cela signifie constante.

Donc c'est ce que nous avons en JavaScript.

Maintenant nous avons let's nous avons const.

Et nous avons various, je suis toujours en train d'utiliser const.

Avant de savoir si celui-ci va changer, et puis je le change en un left, il va changer dans l'application.

Mais généralement const suffira, au moins lorsque vous faites de la programmation fonctionnelle, ce que nous allons faire principalement dans ce cours.

Donc const signifie que celui-ci ne va pas changer.

Comme pour tout, il y a des cas spéciaux où il peut changer.

Par exemple, si vous créez un objet avec un const, vous pouvez changer les propriétés de cet objet, mais vous ne pouvez pas changer l'objet lui-même.

D'accord, assez sur cela.

Celui-ci va s'appeler Global style.

Et c'est un composant, et chaque composant que vous créez dans react va avoir une lettre majuscule pour commencer.

Donc majuscule G et majuscule S dans ce cas, et il va être égal et puis nous appelons cette méthode que nous avons importée ici, create global style.

Et dans ce cas, nous n'allons pas avoir un point et quelque chose ici parce que c'est le style global.

Donc nous allons avoir des doubles backticks, créant notre littéral de modèle.

Et puis je fais comme ceci.

Et puis nous pouvons écrire notre CSS à l'intérieur de ce littéral de modèle.

Et le reste de votre est du CSS régulier.

Donc d'abord, je veux configurer quelques variables CSS.

Pour appeler sur Route, nous faisons cela sur la route.

Et lorsque vous créez une variable CSS, vous le faites avec un double tiret.

Et puis vous avez le nom de votre variable.

Donc max width, cela est en casse camel, comme vous pouvez le voir ici, nous allons définir la largeur maximale à 1280 pixels.

Et puis j'ai une autre variable double dash white.

Et puis je définis ma couleur blanche, une autre variable double dash light gray.

Celle-ci va être E double dash med grade, ou medium grade.

Et celle-ci va être 335 re 535 double dash, dark gray.

Et celle-ci est 1c 1c 1c double dash font super big.

C'est un nom amusant, j'ai oublié que je l'appelle comme ça.

D'accord, vous pouvez l'appeler comme vous voulez.

Celui-ci va être 2.5 REM.

Et le suivant va être double dash et font big 1.5 REM double dash font med ou medium 1.2.

REM.

Et le dernier va être double dash font small, 1 REM.

Et ce sont nos variables CSS que nous allons utiliser pour cette application.

Ensuite, je vais définir la police pour toute l'application et aussi faire un peu de réinitialisation ici.

Donc j'ai un astérisque.

Comme cela, je définis le box sizing à border dash box.

Et puis je définis la famille de polices à able et c'est la police Google qui est importée du fichier index dot HTML.

Et puis une police de secours ou sans serif.

D'accord, c'est la réinitialisation puis sur le corps.

Je vais aussi définir quelques choses.

Donc nous allons définir la marge à zéro, le padding va être zéro, comme cela.

Et puis comme je vous l'ai dit avec les composants stylisés, vous pouvez imbriquer des choses à l'intérieur du corps, nous pouvons imbriquer la balise h1 comme ceci, et définir la taille de la police à deux REM font weight va être 600 et la couleur et je vais la prendre de mes variables que j'ai créées ici.

Et lorsque vous prenez une variable en CSS, vous le faites en tapant var parenthèse et puis le nom de la variable dans ce cas, il va être double dash white.

Donc c'est le h1 puis je vais définir le h3 La taille de la police va être 1.1 ou M.

Et le font weight va être 600 sur celui-ci aussi.

Et puis une chose de plus à faire ici, et c'est la balise p.

Donc la taille de la police, 1 REM pour la balise p, et la couleur est aussi going to be white.

Donc var, double dash white.

Et puis je fais aussi un peu de formatage automatique.

Et parfois lorsque je fais cela, créer un style global, le formatage automatique ne fonctionne pas.

Je ne sais pas pourquoi.

Donc je le fais manuellement à la place et j'enregistre le fichier.

Toujours se souvenir d'enregistrer vos fichiers, il est très facile d'oublier d'enregistrer le fichier, et puis cela ne fonctionne pas.

Donc c'est tout ce dont nous avons besoin pour nos styles globaux.

Maintenant nous allons nous déplacer à l'intérieur du fichier app.js.

Et ici où nous importons react, nous pouvons le marquer avec styles.

Et puis nous importons global style de dot forward slash global style.

Donc cela signifie que nous importons celui-ci que nous avons créé ici, cette constante appelée Global style, nous pouvons l'importer parce que nous l'exportons à l'intérieur de ce fichier.

Nous ne faisons pas une exportation par défaut, comme je vais vous le montrer lorsque nous créons des composants.

C'est pourquoi nous utilisons des accolades et l'importons comme une importation nommée.

Et nous l'importons du fichier qui s'appelle Global style.

Vous n'avez pas à taper .js.

Il suffit de taper global style, il va trouver l'extension de fichier lui-même.

Là nous avons notre composant global stock.

Mais comment l'utilisons-nous dans notre application, nous devrions placer celui-ci au niveau supérieur de notre application.

Et comme nous allons avoir un composant qui enveloppe notre application complète.

Dans ce cas, c'est le div qui s'appelle app, il a un nom de classe de app, nous allons le changer plus tard lorsque nous aurons la configuration du routage.

Mais pour l'instant, c'est un div enveloppant.

Donc à l'intérieur de celui-ci, nous pouvons utiliser un style global.

Et nous l'auto-fermons comme ceci, nous n'avons pas de props à envoyer dans celui-ci.

Et nous ne définissons pas de nom de classe ou ce genre de choses.

Donc lorsque vous utilisez le composant de jeu sans nom de classe, et les props dans react, vous le faites comme ceci.

Et cela est très similaire à une balise HTML.

Donc nous enregistrons le fichier, nous retournons à un navigateur.

Et la seule chose que nous pouvons voir maintenant est que les marges et le padding ont changé ici, c'est juste à droite des bords ici maintenant.

Et ce n'était pas comme ça avant.

Donc nous savons que nos styles globaux fonctionnent.

Et nous pouvons en fait simplement commenter celui-ci, enregistrer le fichier, retourner à un navigateur.

Et vous pouvez voir que la marge est là maintenant.

De cette façon, nous savons que cela fonctionne.

Et espérons que nous n'avons pas fait d'erreur dans le CSS lui-même.

Donc cela devrait fonctionner.

Sinon, nous devons l'ajuster plus tard.

D'accord, dans la prochaine vidéo, nous allons commencer à créer le composant d'en-tête pour l'application.

Donc nous allons créer notre premier vrai composant dans cette application.

Et ce sera le composant d'en-tête.

Donc la première chose que nous faisons lorsque nous créons un nouveau composant est de créer un fichier pour ce composant.

Et vous pouvez voir que nous avons notre dossier src ici et nous avons un dossier d'images.

Mais nous n'avons pas de dossier, qui va contenir nos composants, généralement je crée un dossier, qui s'appelle components.

C'est ce que je vais faire maintenant.

components, toutes les lettres en minuscules, et à l'intérieur de ce dossier, nous allons créer tous nos composants.

Et le truc, c'est que la structuration d'une application est quelque chose de très subjectif.

Donc vous pouvez avoir vos propres opinions sur la façon dont vous voulez la structurer.

Et si vous voulez la structurer différemment, vous pouvez bien sûr le faire.

Mais soyez conscient que ce cours aura cette structure de dossier.

Et vous devez y réfléchir.

Si vous changez des choses vous-même.

Si vous voulez juste vous concentrer sur l'apprentissage de react, je vous recommande fortement d'utiliser cette structure de dossier que j'ai créée pour le cours, je vais aussi avoir un dossier pour chaque composant parce que je veux séparer mes styles et avoir les styles dans un fichier séparé et avoir le composant lui-même dans un fichier séparé, j'ai créé ce cours vous n'avez pas à créer les styles si vous voulez.

Donc c'est plus facile pour moi de gérer cela de cette manière en séparant la bouche.

Donc, pour cette raison, je pense aussi que c'est bien d'avoir tout ce qui est lié au composant dans son propre dossier.

Donc nous allons créer un nouveau dossier à l'intérieur du dossier des composants.

Qui s'appelle header.

Majuscule H.

Donc nous sommes à l'intérieur du dossier header, et c'est quelque chose dans Visual Studio code.

Il ne montrera pas une structure d'arbre complète ici lorsque vous avez juste un dossier.

Mais cela changera plus tard.

Mais nous sommes à l'intérieur d'un dossier header.

Et à l'intérieur du dossier header, j'ai dû créer un nouveau fichier qui s'appelle index.js.

Et c'est aussi quelque chose de très subjectif en fait, parce que je vais créer mon composant dans le fichier index.js.

Donc nous allons avoir un dossier pour chaque composant, et chaque dossier va avoir un fichier index.js.

Et c'est génial lorsque vous importez des choses comme je vais vous le montrer plus tard.

Mais ce n'est pas si génial si vous avez, par exemple, 10 composants ouverts ici, ils vont tous s'appeler index.js.

Donc c'est l'inconvénient de le faire comme ça.

Mais c'est une application assez petite.

Donc je ne pense pas que cela compte.

Mais je peux en fait vous montrer cela si nous avons un composant qui s'appelle test component, nous l'importons comme ceci.

Et de dot forward slash, nous avons notre dossier, qui s'appelle test component.

Comme ceci, bien sûr, nous ne l'avons pas Oh, ceci est juste un exemple.

Il est exporté comme une exportation par défaut.

Donc nous l'importons comme test component sans les accolades, nous pouvons le nommer comme nous voulons.

Mais j'aime les nommer juste exactement comme ils sont dans les fichiers.

Et nous l'importons du dossier test component.

Et puis si nous avons un fichier, qui s'appelle index.js, nous n'avons pas à taper quoi que ce soit de plus ici, il va automatiquement prendre ce fichier index.js.

Mais si nous avons nommé ce fichier, par exemple, test component, aussi, nous devons le spécifier comme ceci.

Nous devons le taper deux fois.

Et je n'aime pas avoir à le taper deux fois.

Donc c'est pourquoi j'utilise un fichier index.js à la place, comme c'est une application assez petite.

Donc nous ne sommes pas confus ici lorsque nous avons beaucoup de composants ouverts.

Donc c'est mon explication de pourquoi j'utilise cette structure.

Et c'est aussi pourquoi nous avons nommé nos fichiers comme ceci.

D'accord, donc supprimez celui-ci ici, nous allons aussi créer des composants de remplissage pour les styles, car nous allons utiliser les composants stylisés à l'intérieur de ce composant lui-même.

Donc c'est ce que nous allons faire.

Et nous le faisons en créant un autre fichier.

Qui s'appelle heather.styles.js.

Et c'est ainsi que j'aime nommer mes fichiers de composants stylisés.

Donc j'ai le nom du composant, puis j'ai un point, puis je le marque avec styles.

Et puis j'ai le .on, l'extension du fichier.

D'accord, donc de styled components, nous importons styled, comme ceci import styled from styled components, components, il devrait y avoir un S.

Maintenant, je vais simplement créer des composants de remplissage parce que je vais créer les styles dans la prochaine vidéo.

Donc si vous avez choisi de sauter les styles, vous n'avez pas à les faire.

Justice avant, vous devez toujours exporter ceux-ci, parce qu'ils sont dans un fichier séparé, et nous allons les importer dans le fichier index.js bientôt.

Export const I have a component that I like to name wrapper, and it's going to be a style dot div.

So this is a div that I'm going to start.

And I just have the double takes.

And I ended there because this is just a placeholder now, so we could just copy this one.

But as I told you, I want to repeat stuff and type it in many times when you learn things.

So we export const, I have another component that is going to be called content.

And it equals from the start, we have another div double backticks and then we export const logo, IMD and it equals a style.

And this is an image, it's the logo that we're going to style, double backticks and and it and then we export const TMDB logo.

img, be careful with the capital letters here.

This is the Movie Database logo.

So capital TMDB, capital L and capital II.

From the styled, we're going to style another image like this.

So this is the four style components that we're going to use for this react component.

So save the file, and I'm going to show you in the next video, how to create the styles the actual CSS, but move inside of the app.js file.

And up here where we import react, we can mark it with styles.

And then we import global style from dot forward slash global style.

So this means that we import in this one that we created here, this constants called Global style, we can import it because we export it inside of this file.

We don't do a default export, as I'm going to show you when we create components.

That's why we use curly brackets and import this as a named import.

And we're importing it from the file that's called Global style.

You don't have to type out.js.

It's enough we just typing out global style, it will figure the file extension out itself.

Right there we have our global stock component.

But how do we use it in our application, we should place this at the top level of our application.

And as we're going to have a component that wraps are complete application.

In this case, it's the div that's called app, it has a class name of app, we're going to change this out later when we have the routing setup.

But for now, that's a wrapping div.

So inside of that one, we can use a global style.

And we self close it like this, we don't have any props to send into this one.

And we're not setting a class name or stuff like that.

So when you use the playing component without class name, and props in react, you do it like this.

And this is very similar to an HTML tag.

So we save the file, go back to a browser.

And the only thing we can see now is that the margins and padding have changed here, it's just right at the edges here now.

And it wasn't that before.

So we know that our global styles are working.

And we can actually just comment this one out, save the file, go back to a browser.

And you can see that the margin is there now.

That way, we know that it's working.

And hopefully we didn't do any mistake in the CSS itself.

So it should work.

Otherwise, we have to adjust that later.

All right, in the next video, we're going to start creating the header component for the application.

So we're going to create our first real component in this application.

And it's going to be the header component.

So the first thing we do when we create a new component is to create a file for that component.

And you can see that we have our src folder here and we have an images folder.

But we don't have a folder, that's going to hold our components by usually create a folder, that's called components.

That's what I'm going to do now.

components, all lowercase letters, and inside of this folder, we're going to create all of our components.

And the thing is that the structuring of an application is something that's highly subjective.

So you can have your own opinions on how you want to structure it.

And if you want to structure it in a different way, you can of course do that.

But please be aware that this course will have this folder structure.

And you have to think about it.

If you change stuff yourself.

If you just want to focus on learning react, I highly recommend that you use this folder structure that I created for the course, I also going to have a folder for each component because I want to separate out my styles and have the styles in separate file and have the component itself in a separate file, I've created this course you don't have to create the styles if you want.

So that's easier for me to handle it that way by separating the mouth.

So therefore, I also think it's nice to have everything related to component in its own folder.

So we're going to create a new folder inside of the components folder.

That's called header.

capital H.

So we inside the header folder, and this is something in Visual Studio code.

It won't show a complete tree structure here when you just have one folder.

But this will change later.

But we're inside a header folder.

And inside a header folder, I got to create a new file that's called index.js.

And this is also something that's highly subjective actually, because I'm going to create my component in the index.js file.

So we're going to have one folder for each component, and each folder is going to have an index dot j s file.

And this is great when you import stuff as I'm going to show you later.

But it's not that great if you, for example, have 10 components open up here, they all are going to be named index dot j s.

So that's the downside by doing it like this.

But this is a fairly small application.

So I don't think it matters.

But I can actually show this if we have a component that's named test component, we import it like this.

And from dot forward slash, we have our folder, that's called test component.

Like this, of course, we don't have this one Oh, this is just an example.

It's exported as a default export.

So we import it like test component without the curly brackets, we can name it to whatever we want.

But I like to name them just exactly as they are in the files.

And we import it from the test component folder.

And then if we have a file, that's called index.js, we don't have to type out anything more here, it will automatically grab that index.js file.

But if we named this file, for example, test component, also, we have to specify it like this.

We have to type it out two times.

And I don't like to have to type it in two times.

So that's why I'm using an index.js file instead, as this is a fairly small application.

So we don't get confused up here when we have a lot of components open.

So that's my explanation to why I'm using this structure.

And that's also why are named my files like this.

Alright, so delete this one here, we're also going to create placeholder components for the styles, because we're going to use the style components inside of this component itself.

So that's what we're going to do.

And we do that by creating another file.

That's called heather.styles.js.

And this is how I like to name my style component files.

So I have the component name, and then I have a dot, and then I mark it with styles.

And then I have a.on, the file extension.

Alright, so from the style components, we import styled, like this import style from style components, components, it should be an S.

Now, I'm just going to create placeholder components because I am going to create the styles in the next video.

So if you have choose to skip the styles, you don't have to do them.

Justice before, you always have to export these ones, because they are in a separate file, and we are going to import them in the index.js file soon.

Export const I have a component that I like to name wrapper, and it's going to be a style dot div.

So this is a div that I'm going to start.

And I just have the double takes.

And I ended there because this is just a placeholder now, so we could just copy this one.

But as I told you, I want to repeat stuff and type it in many times when you learn things.

So we export const, I have another component that is going to be called content.

And it equals from the start, we have another div double backticks and then we export const logo, IMD and it equals a style.

And this is an image, it's the logo that we're going to style, double backticks and and it and then we export const TMDB logo.

img, be careful with the capital letters here.

This is the Movie Database logo.

So capital TMDB, capital L and capital II.

From the styled, we're going to style another image like this.

So this is the four style components that we're going to use for this react component.

So save the file, and I'm going to show you in the next video, how to create the styles the actual CSS, but move inside of the index.js, we're going to create our header component.

Now, the first thing you do when you create a react component is to import react, import react from react, then I'm going to create a little comment here and call it config because we're going to import some stuff from the file, let's call config.js.

And inside of this file, I've set everything up for you that's needed for the Movie Database API, and I export them here in an object.

So we're going to import a few things from this file in the home component.

So go back to the home dot j s, and we import curly brackets, we're going to import the poster underscore size, all capital letters, we're going to import the backdrop, underscore size.

And the image underscore base underscore URL.

Remove this sidebar here.

We're going to import them from dotnet, forward slash config, like this, and be very careful here with the spelling all capital letters and underscore.

Alright, then later, we're going to import a lot of components here.

So for now, I just mark it like this, we're also going to import to hook.

So I marked that one also.

And we're also going to import an image.

So if we go back and look here in the images folder, I have this image that's called no underscore image.

And this one is a fallback image if we don't get an image back from the Movie Database API.

So we have this funny little smiley balloon here that will fall back to if we don't have an image to go back to the home.js.

And we import are going to call it no image.

And when you do an import like this, you can call it whatever you want.

So doesn't need to be named like this.

I'm going to import from doc dot forward slash images.

And I grabbed the no underscore image dot jpg, very important to have the file extension when importing images like this.

Alright, then I'm going to create the component itself.

And as I told you, I like to create it with an arrow function, you can have a regular function, if you want to have that also.

I have a const home, I have a capital H.

All react components always have a capital first letter.

Very important always name your components with a capital first letter.

So home capital H.

And then we don't have any props for this one.

So I just leave it empty here the parenthesis and then I have an arrow function.

And I have curly brackets because this one is going to have some logic inside of it, we have to have a return statement and make an explicit return.

So return for now we can just return a div that says homepage like this.

Alright, then we can also actually scaffold out our states that we're going to have in this component.

And for that one, we're going to need a hook that's called use state.

So make sure to import that one up here.

You type in a coma and then you have curly brackets.

And we import use state from the React library.

And the use state hook is the hook that you use in functional components in react to create a state.

So when we call the use state hook, we'll get an array back.

The first value is going to be the state value itself and the second value is going to be the setter for the state.

And the standard for grabbing and using these values is to use the Six syntax for destructuring.

So I create a const, or the structure of the state and the setter for the state set state.

And you can call it whatever you want here, but I want to call this state, you could call it cool like this, but I don't actually think it's that cool.

So I'm gonna stick with state like this.

And then we have an equal sign, and we call the use state hook.

For now, we'll leave it empty, but it could provide it with an initial state in here.

But we don't do that for now.

So as you can see, here, I'm calling use state and this one will give us an array back.

So from that array, I destructor out the state and the setter for the state.

Otherwise, we could do it like this.

But you shouldn't do that.

We have a const stayed, you stayed like this, and this state will be an array with the first value date value here.

And then we have the setter, or the state as the second value.

And then as we didn't destructor, this one out here, we just put it in this constant called state.

If we want to grab the state, we have to type it in like this, to use the index zero because that's the first value in the array.

And if we want to set the state, we have to grab the setter like this with the second value in the array, that is the index one.

So that's no good.

Actually, it's much better to do it like this, instead, we destructed out and we can also name them individually by doing it like this.

Alright, so this is the way to go, this is the way you should do it.

So that's the state we'll that will hold all the movies, then we're going to have the state for the loading, the loading and set loading equals use state and this one, I'm going to give an initial state, I'm going to set it to false.

And this is also great with the use state hook, you can have as many of these ones as you want, you can split the state up into multiple ones.

And you couldn't do that in the class components in react, because before we had the use state hook, we needed to create a class to have state in react.

And then we just had one state and you have to have a state object with all the stuff in it.

But now we can separate them out into different states.

And that's super great.

So I'm going to create the third one that are called error and set error.

And this one is going to be used if we receive an error from the API.

So we can have this as a flag, and we set this one to false also.

Right.

So that's the states, we have to do one more thing, because we have created this component.

And we also have to export it.

So export default, home like this.

See if we can get some more formatting.

Now it looks great.

Anyways, alright, save the file.

But if we go back to our application, you can see that we don't see anything yet it just start here.

That's because we have created a component, but we're not actually using it.

So in the app.js file, up here, where we import the header, we're going to import home from dot forward slash components, and home like that.

And then we can use that component down here.

So we remove start here and use a component and we self close it, because we're not sending in any props.

So we just type out the name in a tag like this, save the file, go back to the application.

And you can see that it says homepage.

And that's great.

We know that it's working.

And you may wonder why we have all these warnings here.

But they are just warnings because we're not using these values.

Now, they will disappear later when we use them in the component.

So nothing to worry about there.

In the next video, I'm just going to do a short talk on the standard hooks, that's indirect library, and then we move on and actually fetch some data from the Movie Database API.

Okay, before we move on, I just want to make a brief talk about the built in hooks that's in the React library, we can also create our custom hooks.

And we're going to do that in this course also, but we have some hooks that's built in that you probably going to use most of the time when you create react applications.

So I'm on the React js.org.

And I'm in this chapter here that's called hooks.

This is great if you want to know more about hooks, because honestly hooks can be a little bit hard to grasp in the beginning.

So I highly recommend that you actually read this chapter here if you're completely new to hooks.

And if you're new to react, this is a great way to start doing some reading before you do any course or create anything with react.

It's always a good idea to have some basic theoretical knowledge before you start with something.

But of course, it depends on how you like to learn stuff, so I shouldn't tell you how to do it.

Alright, so they have an introduction to hooks, they have different chapters here, we actually going to look at this one number seven hooks API reference, and I'm going to talk about the hooks that's built in the library, sort of separated in basic hooks and additional hooks.

And the basic hooks are probably the ones that you're going to use not maybe 99% but perhaps 95% of the time, and then you're going to create some own custom hooks and use some special hooks sometimes.

So we already talked a little about the use state hook.

That's the one that you use for creating state in a functional component in react.

So that one we imported in the last video, and we initialized it and set it up in the home component, we're also going to use the hook that's called use effect.

And use effect is a hook that you can use for side effects.

So in our case, we're going to grab data from an API, and that's a side effect.

So we're going to use the use effect hook for grabbing that data.

And we're going to use the state to keep that data in our application, then you have a hook that's called use context, we're not going to use that hook in the main part of this course.

But I am going to use the use context hook in the extra chapter at the end, where I create a Movie Database, login in the application and make it possible for you to cast a vote on the movies, then I'm going to set up a global state that holds the login information of the user by using the use context.

So that's the basic hooks.

And then you have some additional hooks use reducer, that's something that's very similar to if you, for example, have used Redux.

The use reducer is very similar to that one.

And it can be used instead of the use state hook if you want more.

I don't know if it's a more complex state.

But yeah, yeah, maybe a more complex state than the use state, we want to use it in this course.

And the use callback and use memo hooks are hooks that you can use to memorize stuff.

If you don't want to recreate for example, a function on each render, they are very handy if you for example, run into something that's called an infinity loop with the use effect.

That's very common actually, in react that you can do that.

Because if you set the state in a use effect that will trigger a rerender.

And if you have a dependency in the use effect, for example, a function that recreates on each render, that will trigger that effect again, and that will set the state again, and it will trigger the effect again.

And yeah, you get the point here, it will create an infinity loop, then you can use the use callback to wrap that function inside the use callback hook.

And that won't recreate the function on each render.

Because by default, if you create just a regular function, React will recreate that function on each render.

And use effect.

If you specify that one in one in something that's called a dependency array that we're going to talk about, then that use effect will trigger again, because it will think it's a new function because that function has been recreated on the next render.

So use callback and use memo or hooks you can use to memorize stuff in react, but I think there are a little bit more advanced, so I won't use them in this course, they use ref hooked, we actually going to use that one because I'm going to show you a little trick in this application.

And a neat little use case to use this one use ref is basically a hook you can use to create a mutable value that won't trigger a rerender, you can see just maybe like you're kind of a regular variable that won't trigger a rerender.

So we can use this one to create a mutable value.

Because if we have it in a state, it will always trigger a rerender when we change that value.

But if we change the value with the use ref hook, it won't trigger a rerender.

Use imperative handle, I've never used this one.

So I'd actually don't know what is for use layout effect, it's very similar to use effect.

They only differ in when they trigger.

So there's no use case for the use layout effect in this course.

So I won't go into detail.

And use debug value.

I haven't used this one either.

These are the built in hooks in react.

But I think the strength about hook is that you actually can create custom hooks.

And we're going to do that in this course also, that was a brief introduction to hooks in react.

So in the next video, we're going to fetch some data from the Movie Database API, we're going to use the use effect hook and the use state hook for that.

Alright, let the fun begin, because now we're actually going to fetch some data from the Movie Database API.

And that's super exciting, because it's always great when you see the magic happens when you have that nice little JSON object with all the data that we fetch from an external source.

I like that I love it.

Alright, so we're going to be in the home.js file for this one.

Now, the later we're going to kind of break this one out and place it in its own custom hooked.

But for now, we're going to be in the home component and created inside of here.

So we're already importing US state.

But we're also going to import use effect, because we're going to use this one for fetching the data.

Then I have this file here, that's called api.js.

And inside of this file, I created all the functions for fetching data from the API.

And I will also say that this will probably one of the most advanced videos in this course and also one of the longest so you can care a little extra about this video because it's kind of advanced stuff in this one.

Alright, in this file.

api.js, I have this omit here where I export a couple of functions.

The three first ones are the ones that we actually need to care about the other ones is for the bonus material for this course.

So you don't have to care about that now.

So this one is the one that we're going to use now fetch movies, and this will fetch a lot of movies, multiple movies, then I have this fetch movie without the s and this one will fetch an individual movie.

And then I have fetch credits.

And that's the credits for the movie itself.

So these ones are going to be used for the individual movie page.

And if we take a quick look at this fetch movies, here, you can see that this one has two parameters of search term and page.

So we're going to give it the search term and the page that we want to fetch.

And I have a ternary operator here.

And that's ies six syntax for kind of a shortcut for if an else so I do a check here, I check if I have a search term, and then I have a question mark.

And if this one is true, if I have a search term, it will run this one to the right to the question mark.

And if this one is false, I have a colon here, it will run this one to the right of the colon.

It's a shorthand for if and else, then I have to do this because we have different resources from them point depending on if we're doing a search, or if we're grabbing the most popular movies.

So that's why I have this ternary operator here.

If we in the search, we're going to use this resource from the endpoint here and also attach the search term.

And then we also grab the correct page.

So we add this as a parameter to the URL.

And then I return on the wait.

And I actually waited two times.

And that's because I first await the fetch from endpoint.

And then I await when I actually converted with JSON, because this one is also async.

So that's why I have to await.

And as I have an await, I have marked this one with an async.

So I'm using the async await syntax for this one, you could also use the good old them.

But I think that's not as readable.

I actually like this a lot more.

So that's why I'm using the async await syntax for this one.

Alright, and I think that's it for this file.

We don't have to care about this, because we're going to import this function.

So go back to home.js.

And just below here, I'm also going to remove the sidebar on market with API.

And then I import API from dot dot forward slash API.

And this will give us this object where we can access those functions are talked about.

Alright, so that's the API, then down in the actual component here, just above the return statement, we can create a new function that we're going to call fetch movies.

And as we fetching from the API, and we're going to use a wait, we have to mark this with async.

And then it's going to have two parameters is going to have the page and the search term.

And we can set the default value on the search term to an empty string like this.

And I have an arrow, and I call the brackets.

So we create this function here is an async function, because we're going to fetch from the API and await the data.

This one is going to get the page we can send in what page we want to grab.

And then we can also send in the search term, we haven't actually created this one yet, because this one is going to be another state when we create the search bar.

So we're going to add in more states here later, and also have a state for the search term.

And if we don't send in a search term, we're going to fall back to an empty string.

So we set this one as default.

So that's the fetch movies function.

We're going to read this in a try and catch block, try and catch.

And we can get the error in this case, I'm not actually going to set the error, I'm just going to have a flag that setting if it's true or false.

But of course, you can have a state where you can store the message from error Also, if you want to do that.

So in the catch, we're just going to have set error, and we set it to true.

And here to see how I use this setter for the state.

So we destructor it out here.

And to set a new state for that one, we call this one and we give it the value.

So I call set error, and I give it the value true and this will change that state to true inside of try block will first going to set the error to false.

Because now we grab a new data.

So we have to make sure that this one isn't set to true because we don't have an error before we have fetched anything.

And we're going to set the loading to true because now we're fetching so we set this flag to true.

And this is how we can keep track on when we actually fetching and we can show the loading spinner and stuff like that.

All right.

Then I create a course that I call movies.

And this course is going to hold all the movies.

So I'm going to wait.

And from the API that we imported up here.

We have that function that I showed you.

That's called fetch movies with an s really important, and then we're going to give it the search term and the page So this will hopefully grab the movies for us.

And we can try yourself with console log movies.

But if we go back to our application, you can see that we don't actually get anything here because we haven't triggered this function.

And we have to do that in a use effect.

So we have the function now, but we haven't triggered it, do some more formatting, and go below the function here.

And we call the use effect.

And the use effect is called with an inline function like this.

And then we can do what we want inside of this use effect.

So what we want now is to trigger this only on Mount only when we mount this home component on the initial run of this one.

So we can do this by specifying a comma here, and an empty array.

This is what's called a dependency array.

For the use effect, we can specify different dependencies on when we want this use effect to trigger.

In our case, we just wanted for now, the trigger when we start up the application, and when the home component mounts, so I specify this as an empty array for now.

And when we specify it as an empty array, it will just run once.

So that's really neat.

In this case, we can just call fetch movies, we're going to send in one, because we want to fetch the first page, we can also mark this one actually with initial render.

So we are specified an empty dependency array, meaning that it will only run once on the initial render.

And inside the use effect, we call our fetch movies function.

And hopefully, we will get the console log of all the movies if we save this one and go back to our browser.

And yes, you can see here we have the movie object here.

So in this object, we have the page one.

And this is all from the Movie Database API.

So it's nothing that we have set up here, we have a total pages of 500, total results of 10,000.

And we have the actual movies in a property that's called result.

And this is an array, and we get 20 movies at a time from the API.

So that's sweet, we know that we grabbing data, and we know that it does triggers once.

And that's super great.

So now when we have the data here, we can actually set our state because we have our state up here and we want to put our movies in the state.

So I'm going to call set state.

And for this one, I'm going to provide it with an inline function is a callback function, that's going to be called with the previous state by the state setter, if you provide a state setter with a function, it's going to be called with the previous state.

And that's great, because we need a previous state when we set the state.

And I'm going to show you why in a second.

So we have a parameter that are called prayer, you can call it whatever you want.

In the state, we want to set an object, so we want to return an object, so I have a parenthesis and curly brackets.

If we didn't have the parenthesis, it would think that these curly brackets marks the scope of the function itself.

And that's no good.

We want to return an object and an object also is marked with the curly brackets.

So we have this parenthesis before and this parenthesis after, this will make sure that we return an object.

And this parenthesis here is for the setter, of course, so we have two parentheses here at the end.

So I have this little neat little plugin.

Also in Visual Studio code where you can see I get these different colors of the parentheses.

So it's really easy to see the parenthesis, I think it's called rainbow brackets that plugin.

So we're going to set the state we have the movies inside of this cost.

So I'm going to use the e6 syntax that's called spread, I use three dots and spread the movies.

And this is because I'm going to take this object here and spread it out here.

That means that we creating a new object, it's going to take all the properties from this movies and spread them out inside of this object here.

When you set the state in react, you should always provide it with a new value, you should never mutate the state in react because if you mutate the state directly, it won't trigger a rerender.

And there can be a lot of trouble.

You should always use a satellite this to modify the state.

And you should always provide it with a new value and not mutate the state.

Really, really important.

Never mutate the state in react.

Okay, so we have the movies.

And then if you remember, we have this property here that's called results.

So this is holding all the movies.

But in our case, we need to decide on how this new state should look because if we load more movies, we want to append the new movies to the old state to the old movies and not wipe them out.

So we have to do some check here for that on the results.

So we have the results property, colon, and then I'm going to put it on a new row.

I'm going to check if the page is greater than one.

Then I have a question mark.

This is a ternary operator here again, are going to return a new array are spread out from the previous state prep.

That's the one here as I told you, this one is getting called with the previous state So from the previous state, I spread out the old result, three dot prevot dot results with an S at the end.

All right, so that's the old movies that we already have in the state, then I have a coma.

And I'm going to attach the new movies from the new movies, dot dot dot movies, dot results.

And this one is going to append the new movies to this array.

So we get an array with the old movies and the new movies.

And that's great.

Then we have a colon because if we're not loading more, we can wipe out the old movies and just give it the new movies that we got in this concept called movies.

So dot dot, dot, movies, dot results, like this is some auto formatting.

And this will hopefully work.

We don't know if it works, because we haven't created a load more button yet.

So we'll see that later in the course.

And there's one more thing we have to do, because we setting the loading to true here.

And we have to set it to false when we have grabbed all the movies.

So just below the try and catch block here at the end of this function, we're going to set loading to false like this, save the file, go back to see that it works.

reload it, and yes, it works.

And that's super great.

But we call slogging it out here, we don't know if it works with the state.

So we remove this console log, and go down here somewhere just above the return statement, and we can console log out the state instead, save the file.

And we hope for the best.

Go back to the browser.

And yes, you can see we have the state here.

And you may wonder why is it showing this many times.

And that's because if we look in the home component, we have three different states here.

So it will rerender each time we change one of these states.

And some may say and go crazy, oh, we have a lot who renders that crazy, it will make this application so slow.

But yeah, you shouldn't worry about that, actually, because react will diff those things and only update things in the DOM that has changed.

So it doesn't matter if it rerender this many times.

And to be honest, React is fast.

So even if you had a lot of rear Enders, you won't have any performance issue in an application of this scale, don't worry, it's completely okay that it renders all these times because it won't rerender the complete page, it will only run the stuff that has changed.

All right, that's how you fetch data from the Movie Database API with a use effect hook and then you put it in the state with the use state hook.

In the next video, we're going to take all this logic here and create our own custom hook and place that data inside of there.

And then we can get rid of this one in the home component.

So it will look a lot cleaner.

Okay, we're grabbing data from the Movie Database API with the use effect hook and we place it in the state with the use state hook, we're going to move all this logic inside of a custom hook instead, because that will make this component A lot cleaner.

And it's always great to separate out this logic, if we want to reuse it somewhere else in the application.

In our case, we don't need to do that.

So we do it just because we want to clean it out and to separate out this logic.

So that's why you create custom hooks.

Either you do it because you want to reuse some logic somewhere in your application, or you want to clean it out and have that separated out.

So inside of the src folder, not in the components folder, this time inside of the src folder, create a new folder, that's called hooks.

And inside of that folder, create a new file that's called use home fetch camel casing, dot j s, capital H, capital F.

And why do I name it like this? Well, React wants you to name all your custom hooks with use and then your name.

That way react knows that this is a custom hook, you could skip to use use.

But you shouldn't do that you should always name them with use before the name, always do it like that.

Otherwise, it can give you trouble in the future.

So inside of this file, I'm going to create a new function.

I'm going to export it also because we're going to import this one in our home component and use this custom hooked, export const use home sets.

And I create a regular arrow function like this.

Alright, so that's our function, then we go back to our home component inside of the components folder.

And we're going to grab all this logic here, all the states, the first move is function and the use effect.

We can keep the console log for now is going to give us an error but that's okay, we're going to fix that soon.

Go back to the use home fetch custom hooked paste the logic in here and it complains now because we haven't imported this ones here.

So we could actually just copy them from the home component but just as before, I want us to type in stuff a lot here because we learning stuff.

So we're going to import from the rack.

library, we're going to need the use state.

So import curly brackets, you state coma use effect.

And we're also going to use the hook that's called use ref laters, we can import that one also.

And we import it from react.

And you can see the red, don't import react in this one, because we not need the actual react library, we just need this stuff from that library.

So that's why we don't have any JSX or anything here.

So that's why we don't need to import react itself, we also need to import the API.

And that one, we can actually just copy this one from the home.

So go back to the home, cut this one out here, the import API like this, go back to the US home fetch hooked and paste it in here.

And this one should be it.

All right, is more of mining.

And we only have this function or we're not actually returning something, we have to return something in our custom hook also.

So go down to the bottom of the function.

And here we're going to return our state's for now, we're going to return more stuff in this one later, when we create more stuff.

But now we return on object.

And we have the state, we have the loading and error like this.

And this is also a sixth syntax, as we return this object, this one is automatically going to get the property state because it has the same name.

And all of these ones has the same name.

So we don't have to specify them explicitly, it will figure this out itself.

Alright, there's one more thing I want to do inside of this one before we finished for this video.

And that is I want to create an initial state.

So up here, I create a const initial state, it's always a great idea to have an initial state if you want to reset stuff.

And we want to do that later.

So I'm going to structure the state just as the one that we got back from the Movie Database API.

So we have the page, it's going to be zero initially, then we have the results.

That's the property that holds all the movies are going to provide it with an empty array initially, where the total underscore pages is going to be zero.

And the total underscore results, it's going to be zero also.

So this is the initial state.

And now we can give this initial state to the use state here where we create a state.

So provided with the initial state, and this will make sure that it gets the state.

Alright.

So that's our custom hook.

For now, we go back to the home component.

And now we have to use this custom hook.

I already created this comment here where we're going to import it.

So we import curly brackets, use movie fetch, like this, from dot dot forward slash hooks, and use home fetch.

Then inside our sad little empty home component, we're going to use this one.

And yet again, I'm going to use ESX destructure syntax to get those properties from the object that we exported here.

We export an object with all these values here.

So I'm going to destructure them out here.

curly brackets stayed loading an error, equal sign and our call my custom hook use movie fit.

So this will hopefully work.

We console log in out to state so save this file, make sure that you also save the hook itself.

And go back to the browser.

reload it.

Yeah, I have some arrow here.

Use movie fetch is not exported, didn't I export it? export const? Yeah, it should be used home fetch, of course, not use movie fetch.

A change this one to use home fetch.

us home fetch homefacts like this, save the file, go back to the browser.

And you can see that we have our state here.

And that's great.

You can see there's a lot of renders.

And a lot of people will say, oh, crazy.

There's too many renders, this is a performance issue.

But it's actually not.

So this is totally fine.

But you can see that it we have our initial state here first, and it's zero, everything is zeroed out.

And then we get the data here.

And we have all the movies inside here.

So that's sweet.

And I promise you it won't be any performance issue in this application because of these renders.

So this is how you create a custom hook in react.

Always name your custom hooks with use before you have your name.

That's really important, you should always name them like this.

In the next video, we're going to start creating the components for the homepage and we're going to start with the hero image.

In this video, we're going to create this hero image here in the application.

So we're going to grab a background image and all the text here from the Movie Database API.

Actually, we have already grabbed them.

So we're going to use that data inside of the hero image component.

So let's go back to our code editor.

And inside the components folder, create a new folder that we call hero image, capital H capital I, and inside the hero image folder and create a new file that we call index dot j, s, and also file that we call hero image dot styles.

dot j s, just as before, are just going to scaffold out the style so we can use them in the component, but I'm going to create the actual styles in the next video instead.

So if you already have this file here and choose to not create the styling for this course, you already have this file here and don't need to do this.

So in the hero image.styles.js import style from style components like this, then I'm going to export a cost that are called rapper is going to equal from style dot div, I'm going to create a div I have backticks like this, then I'm going to export const content equals styled.do, exactly the same and double backticks.

And I'm going to have one that's called export const text equals styled dot div double backticks.

And that's it.

That's three Olam, save this file and go inside the index.js file or the thumb.

So we import react from react, then we're going to import the styles.

So I marked it with styles, import, wrapper, calm content, and text from dot forward slash hero image styles.

Right? Then I create the component itself const hero image capital letters h n i equals, and this one is actually going to receive some props.

And a probe is something that you can send into component.

So that component can change dynamically, depending on the props, a prop should never be changed inside a component that receives the props.

So they can only change if something rerun this and they get a new prop.

So that's how that works.

And the props is sent into component on a prop object like this.

So we have the Prop, I have an arrow function.

And for this one, I'm just going to return JSX.

So I can make an implicit return.

So I have parenthesis so I can skip the return statement.

And then I have my wrapper.

And this is a style component, we scaffold it out just recently, this one can also receive a prop.

So when you send in a prop to a component, you do it by naming the prop and then you give it the value.

In this case, it's going to be from the prop that this component get prop.

There's going to be a prop that called image.

So we send out along to this style component, that's named wrapper.

And in the next video, I'm going to show you how we can set the background image in this component by sending in the image URL to the style component that's named wrapper.

So that's what I'm doing here.

So I'm sending this URL along to the style component on a prop that's called image inside this wrapper, we're going to have the content.

And inside the content, we're going to have the text like this.

And inside the text, we're gonna have a regular h1 tag.

And in JSX, when you want to use a JavaScript expression, you create curly brackets, and then you type in your expression.

In our case, we want to show the title.

And this hero image is going to receive the title from the prop that's called title like this, and you end it with a curly bracket.

You can have any JavaScript expression inside of here that you want.

So you can do some calculations and map through stuff and things like that, that we're going to do later also are going to show you that now we have a p tag.

Yet again, I have curly brackets, I have the text and curly brackets.

And that one is from the prop dot txt.

There's more formatting.

And then I export default hero image.

This looks fine, actually.

But I want to show you a little trick here now that you should use when you create your components, because now we have to type out prop dot image prop dot title prop dot text.

So instead you can use e6 syntax up here and destructure out these props from the prop object.

So we have parenthesis, number of curly brackets, so we have destruction of this object.

And then we have the image, title and the text And then we can remove prop here on all of these.

So I think you should get used to always doing it like this because it will look a lot more cleaner with the structure mount up here.

So we don't have to type in prop every time.

Alright, save the component.

And just as usual, we can't see anything.

Now if we go back to our application, because we haven't used the component yet, save it, go back to home.

And up here, where I marked it with components, we import hero image from dot forward slash, hero image.

And now we can use this component.

So below here, instead of homepage and this div, we can just return the hero image like this.

But we want to send along some props to this one also, because this one needs the title and stuff like that.

And we also need to check that we actually have any movies in the state.

So we can't actually do it like this, because it will throw an error if we don't have any movies in that array.

So what we can do here, instead it we return something here inside of the parenthesis, because we're going to need multiple rows to move this one inside of here, instead.

And as I told you before, we can only return one parent element in JSX.

So we have to wrap this one because we'll have more components here later.

So we can create something that's called a fragment in react, we could of course, create a div like this and move this one inside.

But sometimes we don't actually want to create a div, we just want to return this without creating a div.

And you can do that by creating a fragment.

And this is the shorthand for fragments, you just create this angle brackets and an end angle bracket.

And this will work.

So inside of here, we also want to check if we actually have some results in the state.

So just as before, as I did in the hero image itself, if you can see are in the JSX, where I have a JavaScript expression, I can do the same in the home.

To go back to the home, I have a curly bracket, and now I can use any JavaScript expression that I want.

So I want to check if state results.

And the hero image is going to be the first movie, it's going to be the most popular movie.

So I grabbed the first element in the array, I check if that one exists.

And then I do something that's called a short circuit.

So I have double ampersands.

And I'm going to move this column bracket to the end of here, because I want this one to be nested inside of this one.

So this means that if this one is true, it will run this code here.

If it's false, it will just fall back.

And sometimes some argue that you shouldn't do it like this, because it will return the actual value false here, but JSX won't show it.

But if you want, you could instead do a ternary operator like this.

So if this one is true, we return the hero image.

And then we have colon otherwise we return null, we can put it on its own roll.

And this will also work.

And we want to give this theory some props.

So we have a prop of image.

And that one is going to equal.

And this one I have to construct because the image URL is constructed by the image base URL that we that we get here, and also the backdrop size.

So I have backticks in dollar sign curly brackets, I'm going to grab the image base URL like this.

And this one is going to be long, so I'm going to remove the sidebar.

So this is a template literal.

And you can interpolate expressions like this in a string literal.

Alright, then I'm going to add the backdrop size, like this.

And then I'm going to add, you can see I have dollar sign and curly brackets for all of them here, dollar sign and curly brackets again, from the State DOT results, I grab the first element again.

And then we have something that's called backdrop, underscore path.

Be very careful about the spelling here.

So you get that correctly.

It's really, really easy to make a typo here.

And then it won't work.

This will get us the image URL.

And these ones are all set up in this file here.

Let's call config.

They are set up as per instructions from the Movie Database API.

You can see the image base URL is this URL here.

So that's the one and then I set the backdrop size.

You can change this size if you want and try it here.

You can make them smaller, and you can set them to the original size.

I set them to width 1280 in this case.

So that's what I'm grabbing here.

And I'm generating the string here by merging them together in this template literal here.

Right now we have the title.

And we get that one from state auth results.

The first element and we have a property that's called original underscore title like this.

And then we have the text yet again from state results.

From the first element, you could also break this out in its own variable if you don't want to type this in every time.

So there's probably been a lot of things you can optimize in this application.

But as this is a beginner slash intermediate course, I don't want to do a lot of stuff like this, because it will only take time.

And it will be confusing with all the other stuff going on.

So we have a property here, that's called overview.

And these are, of course, all from the Movie Database API is nothing that I have created.

These are named like this from the Movie Database API.

All right, do some auto formatting.

So you can see here I send in three props, image, title, and text.

And these are the ones that I destructured out in this component itself.

So when you want to give a prop two a component, you do it like this, you named the Prop, and then you give it the value.

And then you can grab those props inside of this component.

So save the file, go back to the browser, and you can see that we can't see anything yet.

But if I mark it here, you can see that we have the text.

But we don't actually have set any styling for this one yet.

So that's what we're going to do in the next video.

And then we'll hopefully see this nice little hero image in our application.

It's time to create the styles for the hero component.

So move back inside of the code editor, and the file that's called hero image dot style dot j s that we created in the last video.

So we have all these components here, and just give it some space here.

And we're going to start with a wrapper, and to the wrapper, we send in a prop.

If you remember this one here, you can see we have this image prop here.

So just as we do with regular component, we can send him props to style component.

And this is something that is super great with style components.

Because this way, we can do some stuff with a CSS.

And in our case, we want to set a background image, the usual way you did that back in the days was that you had to create some inline CSS when you had a dynamic image.

And you didn't know from the beginning where it came from, or what didn't what his name was, you had to set it with an inline styling on the element itself in the HTML.

But in this case, we can do it much, much cleaner and sending a prop to this component.

And we set the image here.

And also we're going to create if you look here at the finished application.

I don't know if you see it now.

But there's a slight little gradient down here also, because I want this text to be able to be seen on any different background.

That's why I have a dark little gradient below this text here.

So that's what we're also going to create.

So in the repple component, we have this div that we styling here with style components.

So we have the background.

And we're going to set a linear gradient first linear gradient, parenthesis, and is going to go to bottom RGB a and I use this because I want to set the alpha value 0000.

And these values are auto generated from somewhere on the internet, I usually do that when I create gradients, it's so easy to just go there and type in your gradient and it will give you the code.

So that's why all these values may seem a little bit odd.

This one is 39%.

And the RGBA is going to be 0000 again, and 41%, rgba, 000 and 0.65.

That's the alpha value.

And I see you know that this one shouldn't even need to have to have these ones here.

I think actually, I can remove this one here.

We don't need that one.

And then we said 100%.

And just after the parenthesis, the end parenthesis, we have a comma.

And then we specify the URL.

And now we can grab that prop that was sent in here.

And you do that as this is a template literal, just as before we use dollar sign in curly brackets, and we can grab those props, you create an inline function and this one will get called with the props.

And from the props, we grab the image and if you want to destructure amount, you can do that also here, then you have a parenthesis and then hold the object.

Then we restructure the image.

And we do it like this.

Right.

Now we have a coma from the variable, regret dot Ray.

And hopefully this will work.

Do some auto formatting and save it go back to the browser.

And you can see that we actually had the image here but we haven't set any other properties.

So that's why it will look like this.

So let's go back here and we're going to set the background On size 100% and cover, we're going to set the background position to center the height is going to be six 600 pixels.

position is going to be relative, because we're going to absolute position or text.

So that's why we have to set this to relative.

And we're also going to have a slight animation on this one.

So I set an animation that are going to call animate hero image, and is going to be for one second.

If we look at the finished here, you can see that it kind of fades up.

So that's the animation that I'm going to create.

And I do that below here.

And nested inside of here.

So act keyframes, and the name is animate hero image.

I go from Opacity is going to be zero to Opacity is going to be one, save it, go back and see what we've got.

There you have it, there's some little border up here.

I don't know why.

Let's see if it's sort itself out when I create other styles.

But you can see that it it animates in here quite smoothly.

So that's great.

Alright, let's fix the other components.

So we have the content, padding is going to be 20 pixels on that one, we set a max width, and we grabbed from our variable max width.

And Morgan is going to be zero in order to save it, let's check it out, you can see that it's in the center now.

That's great.

And that one removed that nasty little border up there also, that's sweet.

Then we have the text.

Let's create that one also, I set the cell index 200.

Just to place it on top, I set the max with the 700 pixels on this text position is going to be absolute.

from bottom we're going to set it to 40 pixels and margin right is going to be 20 pixels.

The min height is going to be 100 pixels.

And the color is going to be from the variables we have the white.

All right, so that's our text.

And inside we have the h1 tag.

So for that one, I set the font size.

And for more variables, we have font, super big camel casing.

And then I'm going to have a media query on this one media screen.

And Max course I have to end this way to see my colon max with 720 pixels.

And I set the font size to variable dash dash formed big, so I'm making it slightly smaller.

Right, that's the h1.

Then we have the p tag, it's gonna have a font size.

From the variables, we grab font med.

That's the medium size.

And then we have a media query media screen and you set the max with the 720 pixels.

For that one, the font size is going to be a variable font small.

So this means of course, that up until 720 pixels, we will use the form small otherwise it will use the font medium.

And the same goes here, we use the font big up until 720 pixels otherwise was used the font super big.

All right, then we're going to have a media query on the text itself.

So media screen and max width 720 pixels.

And we set the max with 200%.

And there may be room for optimization in the CSS because I haven't put the most focus in the CSS for this course, as this is a course in react.

But I wanted to show you how to create the CSS also.

So that's why I included it.

But there are room for optimization I'm sure of that.

Go back and see what we got in it.

seems to be working.

Let's see what happens.

Yeah, you can see it gets smaller.

And that's great.

Now, it's actually starting to get fun because now we see different stuff happening here, things are displaying on the screen.

And that's what I like with front end development to actually see it's put together like this.

Alright, in the next video, we're going to create the logic for the grid component.

So we have our hero component, and the next component would be the actual search bar.

But I'm going to save that one for later.

So we're going to create this grid now instead, in this video.

So let's start by creating a logic just as usual.

And in the next video, we create the styles, go back to the code editor.

And inside the components create a new folder, that's called grid.

And inside the grid, create a new file that's called index dot j s.

And another file is called grid dot styles dot j, s and capital G on the grid, of course, and just as before, we're going to be in the grid dot styles dot j s first to create the placeholders for the style components.

So import styled from styled components, then we export the columns that we call wrapper.

And as you can see here, this is great with starter components, because I named them the same, but it doesn't matter, they will be scoped to that component.

So we can have this exact same name.

That's super sweet.

So the styles won't interfere with each other.

So style dot div, double backticks.

And then we export const content, and that equals A styled dot Dave, also n double backticks, save it and go inside of the index.js file.

So we import react from react, hopefully you're starting to learn is now so this will be in your muscle memory later.

Then we have the styles, we import the wrapper, and the content from dot forward slash grid styles.

Then we create a component itself const grid equals, and I'm going to destructure or two props that we're going to send into this one.

So header and children.

I have an arrow function, and I'm going to do an implicit return.

And you may wonder what children is.

And that is a default prop that we can use in react.

When we nest stuff inside a component, they will be accessible in the children prop.

So that's great, I'm going to show you how that works in a second, we're going to have a wrapper.

Then we have an h1 tag.

And then I have curly brackets because I'm going to grab the header prop and display that here.

Then we have the content.

And for that one, I create another curly bracket, and I grab the children.

So that means that whatever I wrap inside of this component, when I use it, I can display it here by displaying the children, then we need to export default grid like this and save it.

So this is pretty much it for the grid component.

If we go back to the home.js file, we can import it up here.

Import grid from dot forward slash grid.

And then just below here below the hero image, I'm going to use the grid here.

And this one is going to get one prop is the header equals popular movies.

So inside the grid, I'm going to map through all of the movies in the state.

So I have curly brackets and State DOT results.

I map that's also a sixth syntax, we have a movie.

In this inline function, I can make an implicit return.

So I have parenthesis.

And I use a lot of e6 syntax here as you can see, and hopefully you know a bit about it before you start this course because it will be too long of a course if I explain every little syntax in detail, but I try to explain some stuff for you.

And hopefully, you'll learn a lot also from it.

But the map method is something you can use instead of a for loop.

So use the map on the array, the results array, and it will map to each item in the array.

We haven't created a thumbnail yet.

So we're going to create a div.

And I think we have a property that's called title.

So I map through every movie and now I'm just going to show a div in the grid that shows us the movie title.

Or format it save it go back to the application.

And you can see that we have all the movies here so displaying the title, and you can see that it also warns us now each child in a list should have a unique key prop That's when we map through things, we have to market with a key also otherwise, React will complain.

React is using this internally to diff stuff and to optimize itself.

So we can set a key on this one.

And we're going to give it the movie.id.

So this is a unique ID that we get from the Movie Database API, it's sometimes return two of the same movie, and this one will actually give a warning done.

So it's some bug in the API, I think, because it should only return one of each movie.

So if it gives you a warning, it's probably that because it has probably returned more than one of the same movie.

So you could actually add something else, you could add a random number, also to the movie ID if you have that problem.

So let's go back to the application.

And you can see that it doesn't complain now.

So now it's happy, we have provided a unique key.

And we have the titles, but it looks like crap.

Now because we haven't styled it and we haven't created the thumbnails yet.

In the next video, we're going to style the grid itself, and then we're going to create the thumbnails.

So we have our grid, but we have to style it also.

And that's what we're going to do in this video.

Move back to the code editor and in the file that's called grid doc stars dot j s in the grid folder, we have already created this one here.

So we're just going to fill them up with CSS.

And also I can tell you, if you don't have that plugin installed in Visual Studio code, I have a plugin that's called VS code dash style dash components.

So that's the one that's create this nice syntax highlighting inside of this style components.

So that's a little tip if you haven't installed that one.

Alright, so let's create the stars for the wrapper.

First, we're going to set the max width from our variable that's called max width.

Then we set the margin to zero auto, that will center the div, and we give it some padding zero and 20 pixels that's padding on the sides.

And then we have the h1 tag, I'm going to set the color from the variable mid gray on that one.

And then also, I'm going to have a media query.

So at media screen, and Max dash with 768 pixels.

And this one is going to change the font size from the variable font big.

Alright, save it go back to the browser.

And you can see that we have this nice Morgan's here, but we haven't actually created a grid yet.

So that's what we're going to do next.

Inside the content component, we're going to display a grid.

Then we set something that's called grid template columns, grid dash template dash columns, we're going to set this one to repeat.

And this is a little trick you can use if you want to create a responsive grid, so we repeat these columns, we set it to auto fill a coma, and then we use the min max 200 pixels, that's the minimum width that those little thumbnails can have.

And then we set it to one fragment, so we don't specify an exact pixel width on the max value.

And this is CSS Grid syntax.

And the CSS Grid will probably require a complete course on its own.

So I'm not going to go there.

Grid gap, we're going to set that one to two REM so that will give it some spacing between the rows and the columns, save it, go back to the browser, and you can see that we have our grid.

So now it's showing us five items on each row.

If we do like this, you can see that it is responsive.

And that's super great.

That's a neat trick you can use if you have a grid like this, just with one row in CSS Grid, you can make it fully responsive.

So that is really, really cool, actually.

And it works because we set this one to repeat the columns, and we set it to autofill.

And then we set a min and max value.

So we're telling it when it's 200 pixels wide, it can't go lower.

So then it removes one column instead.

And it's going to do that all the way down to the mobile devices.

All right, that's the styling for the grid.

It was pretty fast.

I think.

In the next video, we're going to start creating the thumbnails.

We have the grid now, but we haven't created the thumbnails for the movies.

So that's what we're going to do next.

Move back inside of the code editor and inside the components folder, create a new folder that you call thumb, capital T inside of that folder, you create a new file that's called index dot j s.

And then you create another file that's called thumb dot styles, dot j s, I hope you're beginning to see the pattern here on how I structure the components.

So first, we're going to start in the thumb dot style dot j s, just as before.

So we import styled from styled components.

And for this one, we're only gonna have one component.

So export const.

Image capitalized.

And this one is going to be styled dot IMG because we styling the image here.

Right, save it and go back to the index.js file or the thumb.

So first, we import react from react.

Then we mark it with styles an import image from dot forward slash thumb styles.

We're going to import some more stuff here later, because these thumbnails are going to be clickable, we're going to create that later when we have set up the routing, and also started to create our movie page.

So for now, we create our thumb component, cost thumb equals, I'm going to destructure out an image prop movie ID and clickable, I make an implicit return on this one, because I'm only going to return JSX.

For this one, I'm going to have a wrapping div, like this.

And then we're going to use this prop to tell if it's clickable or not.

And then we're going to have a ternary operator here.

But for now, we're just going to return an image.

That's the image that we created here.

The source is going to be wrong the image prop.

Eric is that an old of movie thumb on that one.

With self, close it.

And then down below here, we export default, some save the file, then we're going to go back to the home component and also import this one.

So up here, import some from dot forward slash thumb.

Alright, and below here, where we map through all of the movies, we're going to use a thumb instead of this div, remove this one here, and we use the sum, then we're gonna have a key for this one also, because we always need to have a key when we are mapping through components like this and display them.

So the key is going to be just as before the movie.id we're going to set it to clickable, that's going to be true, it's always default to true.

So you don't have to do this, if you want to set it to true.

For now that one isn't working, because we didn't utilize it in the component itself.

But we're going to fix that later.

Then we have the image prop and we're going to give it the URL to the image.

And for this one, we're also going to use that fallback image if we don't have any image for the movie.

So we're gonna have a taller operator here, movie dot poster underscore path.

So we're checking if we have imposed a path if we don't have that we're going to display the fallback image.

But if we have this path, we know that we can grab that image.

So we have a question mark.

I'm typing it on another row here, but it's the regular ternary operator.

Then we have the image base URL.

And I'm actually going to show you the other way now not do it like this here.

But you can do it the old way with plus, instead, where the poster size, and then we have the movie dot poster path, movie dot poster underscore path.

Be very careful with the spelling, it's very easy to make a little typo here.

And that will break everything.

Alright, so that is when we have a poster path, then we have the colon.

And we're going to display the no image if we don't have a poster path.

So that's the image, then we're going to send in the movie ID.

And that is because when we click on a thumbnail, we need to have the movie ID for that thumbnail.

So we know what movie to grab and display on the individual movie page.

So movie.id and then we're going to close the thumb component.

So be very careful here.

It's a little bit nested.

And it's very easy to type something wrong here.

But this should be right i think i really hope so.

I save it back to the browser.

And as you can see we have the thumbnails but it doesn't look right.

And that's because I haven't styled them yet.

But at least we display something.

So in the next video, we're going to start the thumbnails some to make it look something like this instead.

Really pretty modern.

I hope Okay, we soon have a grid with nice little thumbnails, we just have to style the thumb component itself.

Inside the thumbnail styles dot j s, we already created this one, we're going to style it inside of the image style component.

So we're going to set the width to 100%.

The max width is going to be 720 pixels, transition, all 0.3 seconds.

And that is because I want some nice transition on hover.

Objects object dash fit is going to be cover border dash radius is going to be 20 pixels.

And the cover here will center the image and make it fit nicely into the thumbnail.

So that's a really handy little rule you can use in CSS for stuff like that.

I also got to have an animation on this one because I want it to fade up, we can actually look at that in the finished application.

You know, you can see here that these thumbnails are also fading up just as the hero image.

That's what I wanted animation for.

So I call it animate thumb.

0.5 seconds.

So we're going to create that animation.

So add keyframes and animate them.

Right from a set the opacity to 02.

It's going to be opacity one, that's the animation.

And then I also want to set the hover effect.

So colon hover like this.

And I said to pacity to 0.8, there's an auto formatting and save it back to the application.

And as you can see, it's looking great.

So that's nice, it's working, it's starting to look like something, we can compare it to this one here, and it looks exactly the same without the search bar.

So we have a few things left to do, we have to create the spinner also when we loading and the search bar and the bottom for loading more.

In the next video, we're actually going to create the spinner component.

So we have that ready when we want to show it when we're fetching more.

Okay, we have our hero image on our grid.

So we're going to create the spinner in this video.

Back inside of the code editor and the components folder, and inside a components folder, create a new folder that we call spinner.

And then we create a file, let's call index dot j s and another file.

Let's call spinner dot styles, dot j s, it's been beginning to be a little bit repetitive here.

But as I said so many times before now is always great to repeat stuff when you learn it.

So even if it's boring, it's better to repeat it, because then it will be in your muscle memory later.

So that's why I repeat a lot of stuff also in this course.

And this one is a little bit special actually because we have the component itself in the index.js file, but the component is really just going to be a styled component.

So in this index.js file, we're just going to import the start component in this file.

So we can create this actually in this video and then we import it and then it will be finished.

So in the spinner.styles.js file, we import styled from styled components.

We export a const that we named spinner, and it equals A styled dot div double backticks and inside the backticks we write our CSS, we set the border to five pixels solid.

And we have the variable of light gray.

We set the border dash top to five pixels solid with a variable dash dash med gray.

We set the border dash radius to 50% because this one is going to be a circle so that's why the width is going to be 50 pixels and the height is also going to be 50 pixels.

We have an animation on this one also.

We call it spin 0.8 seconds is going to be a linear animation and is going to be infinite.

That was at the Morgan 220 pixels.

All right, then we create an animation at keyframes.

Spin we go from 0% Transform.

we rotated Cyril degree, here, I'm using PreSonus data.

So you can use whatever you want.

We didn't do that in the thumb styles I'm using from two in that one instead.

So I like to change stuff a little bit when I create courses like this so that you see that you can create it in many different ways.

So here, I'm using percent instead.

And it should say, transform, not Transform, transform, and rotate zero degrees, and it will see my colon.

And then we go to 100%.

And the transform is going to be rotate 360 degrees, some auto formatting, and save it.

Then we go back to the index.js file in the spinner folder.

And for this one, we just import the spinner that we created a style component.

So from dot forward slash spinner dot styles.

And then we export it, export default spinner.

So that's it for this component, we can actually see if it works also.

So go back to the home page home.js, we import it first here.

Imports spinner from dot forward slash spinner.

Alright, and then here just below the grid, we can place the spinner and also a soy, we don't actually need the use state and use effect here more so we can delete those ones also save the file, go back to the browser.

And as you can see, just below here, it's spinning like crazy.

And of course, it's only going to be shown when we fetch data from the API.

But for now, we're showing it all the time, but we're going to fix that later.

So that's how you create a really simple spinner with some CSS and style components in react.

In the next video, we're going to start creating the search bar.

So we created a grid with a thumbs and we have our hero image and we want to create our search bar.

Next, if we look at the search bar in the finished application, we can see that we have this nice little icon here and I created this myself, first I had an icon from Font Awesome.

But then I thought maybe we shouldn't import the whole Font Awesome library just to have one outcome.

So that's why I created an SVG image instead.

And then it says search movie, and then we can type in something to search for in here.

So this is how it works.

So let's go back to our code.

And inside a component folder, create a new folder, that's called search bar, capital S, capital B.

And inside of that folder, you probably guessed it, we create a file, let's call it index dot j s, and a file that's called search bar dot styles.

dot j s.

And we do as we always do, we're going to be in the search bar dot styles dot j s, and we're going to scaffold out the style components import style, from style components, then we export a const, called wrapper.

And he's going to equal a style of theme.

And we have double backticks.

And we export, not triple backticks double backticks and a semi colon, then we export the course that called content.

It's going to equal style dot div, double backticks and a semi colon, save it go back to the index.js in the search bar folder, we import react coma, we're also going to import a few other stuff here, we're going to need to use state we're going to need to use effect.

And we're also going to need to use ref this one.

And we import it from react.

So why do I need these things? Well, the state we're going to use to create what's called a control component.

And that means that we're going to have our input field but it's going to be controlled by react, the input field is going to be based on the value in the state.

We're going to use the use effect to trigger when this local state changes.

And then we're going to update the search term so that it will fetch new movies from the API.

And use ref is going to be used to show you a little trick that we can use if we don't want to do something in the use effect on the initial render.

So then we're going to import the image that's going to be that little icon I showed you.

So import search icon, camel casing from dot dot forward slash dot forward slash again, images and we have something that's called search dash icon dot SVG.

Don't miss the file extension there.

Then we have the styles, the import, curly brackets, wrapper and content from dot forward slash sport dot styles.

All right, so that's our imports.

And then we create a component const search bar, capital S capital V equals, and we're going to destructure out the prop that's going to be set search term camel cased by a narrow.

Now for this one, we're going to make an explicit return because we want to have some logic in it.

So we have a return statement, parenthesis.

Now we have our wrapper.

And inside a wrapper, we're going to have our content like this.

So the first thing we need is the icon and it's going to be an image.

So image SRC is going to be the search icon.

We can set an author on that one, also search dash icon with self, close it like this, just a regular img tag, then we're going to have an input field.

And it's going to be a type text.

We're going to have a placeholder.

Let's go going to be searched movie.

And then we're going to have an on change handler and value.

But for now, I'm just going to surf close this.

And to do some auto formatting and export this component, export default search bar.

And then we're going to import it in the home component just to see that we got something here.

So go back to the home, and close all this, go back to the home.

And just below the hero image, we're going to place that component But first, we need to import it.

So import search bar from dot forward slash search bar right down below the hero image just above the grid, we can place a search bar, save it go back to the browser.

And you can see that we have our input field here.

But we haven't started yet, of course.

So hopefully it's gonna look something like this, when we're finished, go back to the code and the search bar in index.js file, we're going to make this what's called a controlled component, a controlled component in react is a component that react control.

So the input value is going to be based on a state that we create.

And when that state changes, it also changes the value in the input box.

And this is great because then we know that our state is in sync with the actual value in the input field.

We create a state of here const, we can call it state and set state equals use state.

And it's going to be an empty string for stores.

On our input field, it's all formatted them like this, I want to have them like this, instead, we're gonna have an on change handler equals, and for this one, I want to create an inline function, you could also create a function up here for that one if you want to do that instead.

But I want to show you how to do things differently.

So in this case, I created an inline function, we have the event, or you can just type in E, for example, you can name it whatever you want, then we set the state with the event dot turn target dot value, and this will give us the value in the input field.

And we need to have this inline function as we are actually invoking this function here with that value, otherwise, it won't work.

So by having this inline function, we can provide this one with value.

So that's why you have this inline function.

Otherwise, it will run this function instantly.

And that's no good.

So if we, for example, had a function that we didn't want to send in some arguments to that we just want to trigger on change, we can have it like this instead.

And that will work but in this case, we want to send in the argument or the current value.

So that's why we have this inline function.

Alright, so that's the unchanged and then we set the value to the state.

And there we have successfully created a control component.

We can see if it works, go back to the browser, type something in and you can see the value here now is controlled by react.

As soon as we set this value to some state value here, we are making this a control component.

And every time it changes, it's going to trigger reset state and it gets the value here and replace the value from the text input.

In the state, and then the value is displayed in the textbox itself.

So it's kind of a closed circle here on how things work.

It goes around in this way.

Now we have our input field, but we want something to happen.

Also, we want to set the search term that we're going to create in our hook that we created before.

So we actually going to create a new state inside of use home fetch.

So up here in the US home fetch hook, we're going to create a cost, call it search term capital T, and set search term, then it's going to equal use state.

And we'll set it as an empty string initially, then we also need to export this one.

So export it down here.

And we only need a setter for this one.

So we can export the set search term like this, save the file, go back to the home.js.

And up here, where we where we use or use home fetch hooked, we can destructure out the set search search term, the set search term arrived.

And this one is going to be the prop for our search bar.

So I'm going to call this prop set search term also.

You can call it whatever you want.

And then I give it to set search term.

So this way, we pass this along down to our component to the search bar, so that we can use it in the search bar.

So when this one triggers when we set the search term is going to trigger here.

So actually changing the state in our hook here.

That's exactly what we want, because then we can use it in our hook when we fetch stuff.

But in this case, we want to have a slight delay when the user types something in before it tries to fetch the data, we can look here in the finished application, you can see when I type something in here, that I have a slight delay, otherwise, it wouldn't be a good user experience if it just instantly started to fetch data.

So that's why I do it this way instead, otherwise, we could have used this state to actually fetch the data.

But in our case, we want a slight delay.

And then we set the search term that we're going to use for fetching.

So that's why I have dual states for this one.

So let's create a use effect in the search bar use effect.

We have an inline arrow function just as before.

And we have the dependency array.

And we're going to fill it out in a second.

I'm going to show you how to create a timeout in react now and how we can use it in a use effect.

So first we create a timer.

We use the set timeout that's built in JavaScript, we have an inline function for that one.

And then we're going to call the set search term.

That's the one that we created.

And we're going to give it the state like this.

And I'm going to set it to half a second, that's 400 milliseconds.

So this one will trigger after 500 milliseconds.

If you want some other value, you can of course type that in instead.

And you can see here now that it instantly complains, because we haven't specified this as a dependency.

So we specify and set search term as a dependency.

And it also complains, because it needs the state, that's also dependency to this use effect.

So this linting rules are actually really good.

It tells us stuff so that it is so that we actually do this correctly.

And we should always specify the dependencies and handle it inside of the use effect if we need to.

Alright, but there's one more important thing we have to do with the timer.

And that is declared a timer on each render, because otherwise, it will just create a lot of timers.

And that's no good.

And there's a handy little thing with the use effect that we can use for this.

Because if we return a function in the use effect, so every time before a new render, it will trigger this function.

So we can clear our timeout inside of that function.

And this will take care of that we clean up this timer.

So we don't have a lot of timers that just ticks in the background.

And you can imagine you have a lot of stuff that you want to do maybe to clean up stuff.

So you can always do that in a return function with the use effect.

This one doesn't trigger until this render has finished and is going to render again.

So that is sweet.

We can say this one.

And we can actually go back to the use on fetch.

And up here.

We can console log the search term, so we can see that something is happening.

So go back to the application again.

Yeah, I have a typo somewhere.

Maybe I didn't save the home.

Save go back to the browser.

Yeah, no, it's worse.

You can see it's really important to save your files because it will break otherwise, be sure to save all the files.

So if I type in test, and you can see here after 500 millisecond it will trigger.

So that's sweet.

We know that that is working and we Use this to fetch data from the API.

But there are one more thing I want to do.

And I promised you to show you a little trick with the use ref.

And that is because the use effect always trigger on the initial render, and we don't want to trigger a fetch.

When this component mounts, we only want it to trigger when the user has typed something in.

So that's why I'm going to create a cost that's called initial up here.

And I'm going to use ref.

And I set it to true.

So when we call the use ref hook, this one will create a mutable value for us that you can compare to something similar as a mutable variable.

So we have this initial const, and the actual value is going to be in the initial dot current, that property will hold the value true right now.

So I set is the true and inside the use effect, I'm going to check if initial dot current, that's going to be the true value right now, if it is true, in it, it should say initial, like this, right? Then I instantly going to set the initial dot current to false.

And you can see here, I can mutate this variable directly, I don't have to have a setter for this one, because this one won't trigger a rerender.

That's the biggest difference from a state that when you use ref, it won't trigger a rerender.

And then if this one is true, we know that this is the initial render, and then I'll just return, we don't do anything more inside of the use effect.

And we set it to false.

So next time, this one triggers, this one is going to be false.

And it's going to run our logic.

So this is how you can create a neat little code snippet here, to skip the initial render in the use effect, save the file, just make sure that it works.

Yeah, and it seems to be working.

We've learned how to create a control component in react, and the component controls the input field with the state.

So the input field always has the same value as the state and that's the control component or state is synced with the input field.

And then we created a timer that will trigger each half a second and call this set search term to set the stay there.

And the state is going to be the value from the input field.

And we also pass this one along from the US home fetch.

So that's how you pass data down to your components.

That's what props are for, you can pass data down to your component, and we can use it in that component.

And that means that we also have this value in our use home fetch hook to use the fetch data later, that can remove this console log for now, save the file, and this will be it actually for the search bar.

In the next video, we're going to style the search bar.

And then we're going to create the logic for fetching the data.

were created our search input field, but it doesn't look good.

So we have to style it also.

And that's what we're going to do now.

So in our search bar dot styles file, we're going to create the wrapper first.

And I'm going to display it as a flex.

I'm going to align items center.

Now not aligned a line I set the height 200 pixels.

The background is going to be from the variables, we have the dark gray.

And I'm going to give it some padding on the sides, zero and 20 pixels, do some more formatting, save it go back to the browser.

And you can see that we have the search bar here.

And now we have to style kind of the inner part of the search bar.

And we do that in the content.

Inside the content, I'm going to set the position to relative because we want to place the icon with an absolute position.

The max width is going to be from the variables we have our max width, the width is going to be 100%.

The height is going to be 55 pixels, the background is going to be from the variables met gray.

And Morgan is going to be zero in order.

And the border dash radius is going to be four pixels and the color from the variables we have our white.

Save it go back and see what we've got so far.

So we have this inner part now of the of the search bar to add the style icon and the search bar input field itself.

So inside the content, we're going to nest some stuff here we have our icon that's the IMG I set the position to absolute.

And this is why I use relative appear, otherwise it won't work.

So it needs to be relative to the actual content div is going to be left 15 pixels.

So 14 pixels, and will is going to be 30 pixels, save it go back.

And now it seems to align correctly and it also has the correct size.

Great.

Then we have the input field itself.

So down below the IMG type in input, we set the font size to 20 pixels in this one position is going to be absolute left is zero, margin is eight pixels.

And zero padding is going to be 000 and 60 pixels.

border is zero, the width is going to be 95%.

The background is going to be transparent.

The height is going to be 40 pixels.

And the color is from the variables and is going to be white.

So go back to the browser.

And you can see that it works now but we have this nasty little outline, you shouldn't remove the outlines, actually, but in this case, I think it's fair to do it because it doesn't look good.

So I'm going to remove them.

So inside the input, I'm going to nest focus.

And I'm going to remove the outline, I set it to none.

And hopefully that will remove it.

Yeah, you can see it removed.

Now.

One thing you can do also, if you want is to style this for mobile devices, maybe make it a little bit less insight in font size, and stuff like that, if you want to really fine tune it here, but it seems to be working now.

All right, and that's it for the search bar.

That's the style for the search bar.

In the next video, we're actually going to hook this up to the API and fetch some data.

We've created our search functionality on our search bar, but we can't really search for anything.

Yep.

So if we type something in, we just get this console log here.

So we're going to implement the actual functionality where we fetch the search data from the API.

Let's go back inside of the code editor.

And we're going to be in the use home fetch hooked.

And down here, where we say initial render, we're going to change this one to initial and search like this, because we're going to use this use effect both for the initial render and the search.

And it's actually pretty easy, because now we just have this empty dependency array, meaning that we only trigger this use effect once on Mount.

But we also want to trigger this one each time to use the search for something.

And up here we have our search term.

And in this one, we're going to store what the user typed in in the search bar.

And that means that we want to trigger the use effect when the search term changes down here in the dependency array, we specify a search term, meaning that this use effect will trigger each time the search term changes, and it will also trigger one time on Mount.

So we can actually use this one for the initial setting also.

Because when we search for something, we always want to fetch the first page just as we do on the initial amount.

So that's fine, we're fetching the page one.

But we also want to provide the search term.

And that's also fine for the initial fetching, because the search term is going to be an empty string.

So we know that we're fetching the most popular movies, because we're not specifying any search term.

There's one more thing though, that we have to do, and that is to wipe out the old state before we make a new search, because we want to wipe it out and then make a search, show the loading spinner and then show the new movies that we grabbed from the search.

So we can set state to the initial state here, and that will wipe out the state.

And that's really all there is to it.

So we say this file, go back to our application, we try to search for something.

And you can see that it works.

Now this one changes because this one will always grab the first element in the array of movies.

And that's fine.

Actually, you can have it like this if you want, but I want to remove this hero image when we're in a search.

We can do that also to go back to our code.

And then inside of the home.js.

Down below here where we show the hero image.

We can also specify that we don't want to show this one if we have a search term, so not search term, double ampersand so now we're checking that we don't have a search term and also that we actually have a first element in the array.

or movies.

But you can see that you won't see her now.

And that's because we haven't exported this one from our hooked.

So go back to the hooked.

And down below here, we can export this one also search term like this, save the hook, go back to the home notice, and up here where we destructure out everything from the hood, we can also destructure out the search term like this, save the file, go back to our application, we tried to search again.

And now you can see that it disappears.

This is exactly what I want.

If you want to keep the hero image, you don't have to do this.

And then it reappears when we don't have anything in the search bar.

All right, there's one small thing that I also want to do, and that is in the home.js.

And if we look down below here, where we have the grid, I'm going to create a ternary operator now because now it says popular movies, even when we're in a search.

So this one, I'm going to create a curly bracket and also curly bracket here at the end, and then I check if I have a search term, I have a question mark.

And if we have a search term, I create a string I wanted to say, search result.

And if we're not in a search, it's gonna say popular movies.

So if we have a search term, it's gonna return what's the right to the question mark, and that search result.

Otherwise, it's going to return popular movies, save the file, go back to the application.

This time, I'm going to search for Indiana Jones.

And now you can see that the header on the grid changes.

So that's great.

It says search results.

And I remove this and it says popular movies.

So that's our search, we have implemented all the logic for the search bar.

And in the next video, we're going to start trading the Load More button.

Okay, let's start creating a button that will go at the bottom here.

And the spinner will not show all the time, it will only show when we loading stuff back in the code.

And inside the components create a new folder that's called baronne capital V.

And you guessed it, we create a new file, let's call index dot j s.

And we create another file that's called Baran dot styles dot j s.

And we're going to be in that file and import styled bomb style components.

And for this one, we only going to have one style component.

So we export const.

And it's going to be a wrapper equals a style dot button in this case, and double backticks Auto format it and save it and then we go back to the index.js file.

And we're going to create a bottom.

So we import react from react.

Then we have our styles, we import the wrapper that we created wrapper from dot forward slash buttons and dot styles.

Right, now we have our component const bottom.

Then I just structure two props.

One is called text and one is called callback.

And I create an error and I make an implicit return on this one.

I'm going to add the rapper is going to be type button.

And it's going to have an onClick handler.

And it's going to be the callback that was sent in as a prop.

And then I'm going to display the text inside of the bottom.

So this is a button that we created as a start component and call it wrapper.

And it's going to trigger a callback function when the user clicks on the button, and then we show the text we can send in what text we want to this button.

If we want to reuse it, then we export default, bottom, save it, then we go back inside of the home component.

And at the top, we're going to import bottom from dot forward slash bottom.

And then at the end over JSX, we're going to show the bottom.

And we have to think about this because we don't want to show the bottom if we read the last page of movies.

So we have to take that one into consideration.

So just below the spinner here, I'm going to use the curly bracket and create a JavaScript expression, we're going to check from the State DOT page.

If that one is less than State DOT total underscore pages, we know that we're still not on the last page.

And I have a double ampersand make a short circuit here.

I also want to check so that we're not loading anything.

So if not loading, and then I have another pair of ampersands.

And I have a parenthesis, put it on a new road just to make it a little bit more readable.

And then I'm going to show my bottom.

So the text is going to be load more.

And for now I'm not giving it the callback.

This is it for now.

So this statement will check if the page we're currently on is less than the total pages.

And then we know that we still want to show the Load More button.

And it will also check that we're not loading anything because when we loading something, we want to show the spinner instead.

And we have the spinner here.

So we can actually create another statement here, the creator curly bracket, and type in loading and double ampersand, and we end it with another curly bracket like this.

So this will show the spinner if the loading is set to true.

And if it's set to false, it will not display the spinner, but then it will display the button instead.

If we go back to the application, we can see the button down below here in the corner.

But it doesn't look right, we have decided also to look like this here.

And that's what we're going to do in the next video.

We have our ugly little button here down at the corner, so it's time to style it, go back to the code, and inside of button dot styles dot j s file and we have the wrapper here, we're going to give it some nice little style here, we start by displaying it as blocked display block, we set the background.

For more variables, we have the dark gray, we set the width to 25%.

The min width is going to be 200 pixels, the height is going to be 60 pixels.

The border dash radius is going to be 30 pixels.

And the color is from the variables dash dash white, the border is going to reset to zero, the font size is going to be from the variables font big Morgan is going to be 20 pixels and auto transition is going to be all 0.3 seconds.

I'm lazy here I can set it just the property data wants to have a transition, but I said it all outline is going to be none.

And the cursor is going to be pointer, then I want a little hover effect all sorts of over a set of pacity to 0.8.

That's why I had this transition here.

Also, I just want to check also, the font sizes here.

Font big.

Maybe we can use this one instead on the styles for the search bar because I think I have.

Yeah, I have the font size, or 20 pixels, we can use the variable instead variable on big and see how it looks.

Yeah, I think that looks nice.

Actually, we can use that one instead.

But let's check out the button.

Yeah, you can see that it works.

It looks great.

Now, we only have to create a logic footer button now when so that we actually can load more movies.

So that's what we're going to do in the next video.

This is actually the last video for the homepage.

So we're going to create the fetching logic for loading more movies.

And we're going to start in the US home fetch hook that we have in our hooks folder.

And we're going to start by creating a new state.

So this is going to work in a way that we have a state with a kind of a flag that was set to true or false.

And we set that one to true when we click on a button.

And then we're going to trigger reuse effect.

Because as I said before, I think this is great practice with the use effect hook and also the state hooks.

So you could do this in other ways also.

But this is a quite neat way of doing it we have this state that was set to true or false.

And when it changes, we trigger that use effect.

And then we can trigger to load more movies, we first create the state const is loading more camel casing as always.

And then we have the setters set is loading more, it's going to equal and we call the use state hook we set it to false initially.

And this one is going to be triggered from the button itself.

So we have to export it down here also.

So after the set search term, we can export set is loading more.

So there you have it, I removed the sidebar, so we can see the complete row here.

Now we're exporting six of those.

So that's our state.

So we can go back to the home.js file.

And here we have our button but we first need to destructure out the set is loading more set is loading more.

There's some auto formatting, and it will clean it up for us a little bit.

So we just structure that one also.

And that means that we can use it in this component.

And one thing that we also didn't do is to actually check if we have an error so we can do that before the return statement here.

If error We can return a div that says something went wrong.

Like that.

And that will make sure that if we get too narrow, we won't display everything here, we will display this error message instead of.

So you can create a more sophisticated stuff here, if you want to do that.

In our case, I think it's enough for this course.

Alright, so let's move on to this set is loading more.

So we have our button down below here.

And we already created a callback prop.

So we give it the callback prop curly brackets, and this one is going to have an inline arrow function.

Because I want to call this one with an argument set is loading more.

Yeah, I'm going to remove the sidebar set is loading more, and we're going to set it to true like this.

So this will change this state when we click the bottom.

And if we check out the application, we won't actually be able to see anything.

Now, you can see that it renders when we click the bottom because it costs logs this out, so we know that it's working.

And one great thing to know that is that if I click a few more times here, you can see that it don't rerender anymore.

And that is because we're giving it the same value.

So react won't update the state if it gets the same value.

So it's good to know that with react, if you give it the same state value, it won't rerender it.

So react is kind of smart, it already knows that it has the same value.

So it won't do anything, a quick little pro tip in react.

Alright, so we know that the button is working.

So we move back to the use home fetch hook.

And we're going to create another use effect down here.

below the search use effect, I'm going to mark it with load more.

So just as before I create another use effect, an inline arrow function, and we have the dependency array.

And we want this to trigger when the is load more is changing.

So it's load loading more like this.

And the thing is that we only want this use effect to trigger when we actually is loading more.

So if not, is loading more if this one is false, we're just going to return we don't want to do anything else in this use effect.

This one should only do something when we load more movies.

And what we want to do now is to call or fetch movies function again.

In this time, we want to give it a State DOT page, plus one because we want to load the next page.

And we also give it a search term if we're in a search.

And now you can see that it was associated because it wants a few other dependencies, it tells us that we need to specify the search term and the State DOT page.

That's what we're going to do the search term and the State DOT page.

And now it will be happy at us.

And that is because these ones are outside of the use effect.

So we should always specify dependencies in the dependency array.

And we should handle them inside of the use effect hook.

If there's something we don't want to do when something change, we should account for that inside of this use effect.

So we fetching movies, and then we set is loading more to false.

Do some more formatting and save it.

And hopefully this should work.

So we have the use effect of triggers.

When we change the is loading more Boolean.

If we're not loading more, we will just return we don't do anything else in this effect.

Otherwise, we call the fetch movies function.

And we give it the next page that we want to fetch.

And we also give it a search term.

And then we set it slowly more to force again so that we go back to what it was before.

And then we can do it all over again, if we want to click the Load More button again, save it and go back to the browser and see if this works.

We click the load more.

And as you can see, it works.

And I love when stuff just works.

And you can see that our loading spinner is showing showing up also.

It's fast, so we can't hardly see it, but it's there.

So it's working.

And we can also see in the console, here we are at page 11.

And we have 220 results now.

So that's great.

We know that load more is working.

We can also try it out so that it works when we search for something.

And it does.

So that's sweet.

I'm happy with this.

Hope you like it too.

You can see also those those images, some of them has some strange proportions.

So if you want you can tweak the CSS to take that into account also.

In the next video, we're going to start creating our routes for application.

We're going to start creating the routing for our application.

And before we do that, I just want to talk shortly about react router.

Especially the version six that we're using.

It's not officially released when I record this tutorial.

So hopefully it released now, when you watch this tutorial, because it is, as they say, here, it's around the corner.

And I actually talked to this guy, Michael Jackson here on Twitter.

And he said that I should use this version in my course, because it's that stable now, and it's not going to change that much.

And we're not going to use all the advanced functionality in the router itself.

So that's why we installed the next version of react router when we install the dependencies for this application.

And there are a few changes in it if you compare it to version five.

And I actually don't want to talk about version five, because that will soon be deprecated.

So just wanted to mention why I chose to use the version six of the React router, because this is the future version.

And it has the API that is going to be used for a long time, hopefully, in the future.

So that's why I use it.

In this tutorial, I want to make sure that this tutorial uses the latest stuff, so that you know that you're up to date on the things that you learn.

So that's why so just a few words, words here you can compare, for example, they brag here with a react router, version five, that the bundle size is 20.4 kilobytes minified.

And the version six is only going to be 8.5 kilobytes minified.

So if you care a lot about size on your packages, this one is drastically smaller than the version five.

And then they also show you some stuff here on how you use the router.

But that's what I'm going to show you in the next video.

But if you want to read more about this one here, you can go to react training.com forward slash blog forward slash react dash router dash version six dash pri, forward slash.

And then you can read more about it or just google react router version six, and you will probably find a lot of information about it if you want to read more about it.

So let's get started.

We're going to create the routing in the next video.

We're finished the home page and we have our application here.

And we have this nice little grid with all the movies, but we can't actually click on them to view a movie.

And we can't click on the logo up here.

So we have to fix that.

And we're going to do that by creating some routes for our application.

So the first thing we're going to do is if we go back to the code, we're going to create two more components inside a components folder, we're going to create a new file that called not found dot j s, and also not a file that's called movie dot j s, capital M on movie and capital and capital F are not found.

So we're just going to scaffold This one's out.

So we have something to route to.

If we're in the movie.js file, we import react from react, then I create a component are called movie that is going to be an arrow function.

And I'm just going to return a div that says movie.

And now export default movie, do some more formatting and save it always save your files.

Alright, then I copy this one.

And I go inside of the notfound file that we just created.

I paste it in and I change this one, I'm going to share them in one go not found like this and save it.

And there you have it we have two components to play with.

And this one, the movie dot j s is going to be the individual movie component for showing the movie.

So we're going to be working a lot in this component later.

This one is going to be a series I'm not going to create a fancy and not found component.

So you can do some stuff on your own in this one if you want to do that.

So we scaffold out two components.

And then we can move inside the app.js file that you find in the src folder not in the components folder.

So app.js.

And the first thing we have to do is to actually import all the components we need from the router library from react router.

We can mark it here with routing.

If we want to do that.

Then we import we have curly brackets, we're going to import something that's called browser router, capital D capital R.

And this name is a little bit long.

So if you want to rename this module, you can do that by typing s and router.

So we import it as router.

I think I'm going to remove this sidebar also.

Alright, so that's the first one we import browser router, but we import it as router so we can use it with the name router instead.

Then we import another component that's called routes.

And then we import another component that's called route very similar names here.

So be careful when you import these ones.

And we import them from something that's called react dash router.

So be very careful here.

We're not importing it from just react dash router.

We Pulling it from react router DOM.

So this one is using react router in the background.

But this one is specifically created for using in the dome.

Alright, so that's all the inputs that we're going to do.

So let's create our components down below here.

And I'm actually going to change this one to an implicit return.

So I delete the return and the curly bracket.

And I want to create an arrow function instead const f equals because it's only with arrow functions, you can do an implicit return and I remove the curly bracket there, do some auto formatting, to me, it looks a little bit cleaner.

And this div is going to be replaced this wrapper div that has a class name of app going to be replaced with a router to so we wrap our complete application with the router.

So it's really important where you want to put the routes, you should wrap it with the router.

And that is the browser router that we imported here, but we renamed it to router.

So that's why I use it as router here.

Then the header is going to be shown on both the home page and the individual movie page.

So the header is going to be left out of the routes.

So I'll leave that one here.

And then I use the route component.

And inside of the routes component, we can create our routes.

And the first route, we're going to use the component that's called route.

So we have three different components here from the router library router, we're going to wrap our complete application in this case, and then we have routes, that's going to wrap a route because you can route in different components if you want to do that.

So let's say that you have a component deep down in your app tree, and then you want to create some routes for just that component, you can wrap them in this route component, and then you create the routes.

So you don't need to have them here in the top of your application.

And then you use the route component to actually create your route.

And this route component has a prop that's called path.

So we can specify the path where we want to show a specific component.

And in this case, it's a forward slash because it's the homepage.

And then we have another prop that's called element is going to equal and here we can give it a component.

And we want to give it the home component like this.

And then we also have to self close the route component.

That means that we can remove this home component here.

So that's the first wrote, if we want, we can save this to see that it still works, go back to the application, reload it, and you can see that it works.

So that's nice, then we're going to create another route.

So we use the route component again, we set the path, and this one is going to be shown when we go to the path login, the forward slash login and the element is going to be our component.

Login.

And then we close the route component and some more formatting, save it, go back to our application, make sure that it's running.

I'm actually not running mine.

So I'm going to type in NPM start.

Whoa, I heard it really sumed in here.

And I'm going to bring up the console for later.

So if we go up here in the route, and type in forward slash login, you can see that we show our component here.

So that is working.

Great.

Go back to the application and the login component.

We're going to create a few states for this one.

So at the top of the login component, we create a state that we call user name and set the username, equals use state are going to create an empty string as initial state for this one, we create another state, that's called password.

And the setter is called Set password equals use state with an empty string as initial value also for this one, something like that.

And then I also want to notice state, that's called error and set error.

And we have a use state call.

And we set it to false initially.

So these are the three states that we have, you could also have won combined states for input fields, if you want to have that is used to create them separately like this, then we're going to grab our context, we're importing it up here.

And we can grab the context with a hook that's called use context.

And our context is going to be the state that we created.

So we create a new cost.

And we can just structure it out just as before, we have the state, the state is actually going to be the user.

So we can be more specific, we call it the user and the set user.

And it equals, we call the use context hook.

And this works as simple as we just give it the context.

And this one is going to bring in the context for us.

And the user, we're not going to use this one, we're only going to use the set user, we can mark it with an underscore.

If we want to do that.

This is also very subjective on how you like to do stuff like this, then we have a hook that we will see imported for our navigation.

So we create a course that we call navigate.

And we call that hook use navigate.

And this will make it possible for us to use this navigate const to navigate programmatically in our application.

Alright, so first, we're going to make these input fields controlled by this component.

So we have to hook them up with state just as we did with the search bar.

And we have this handle input here, where we get the event from the input field, so the input fields, the value for this one, we can change this one now.

It's going to be the state that's called username.

No, not a capital N, all lowercase letters, and this one is going to have the value from the password state.

All right.

So this will make sure that it is connected to the state.

So now when these input fields change, we can make that change in the handle input because we have an on change handler on them.

And we can set the different states in the handle input.

And you can see here that I give them a name.

So first, we want to grab the name.

So I create a const name equals e dot current target dot name, and this one is going to grab the name that are set here on the name prop.

Then we have another cost with the value.

And we get that one from e dot current target dot value.

So we need the name and the value.

And actually, you could do this in a one liner.

If we use just one state for our input fields, we could set the name of the properties in an object dynamically with the name that we get from the input field.

And then we set the value so that will create new values in the object.

Depending on how many input fields we add to our application.

But in this case, I have a separate state for each input field.

So I do it like this instead, in a small application like this, I think this is more readable, actually.

But this means that we have to check now what input box that we type in.

So we have an if statement.

If named equals username, then we're going to set the username stayed with the set username, stay setter, and we have the value.

So we set the name of the input box, and then we get the value.

If the name is username, we know that we should set the state for the username.

So that's what we do in here.

And if the name equals password, we're going to set the password state.

And we give this one the value also.

This one maybe should have a lowercase m instead not an uppercase, so we change this one just to be consistent.

Or format it save it and we can see if it works, go back to the application.

And we can type something in here.

And yeah, it works.

So we know that we have our control components.

So that's great.

So our input fields are working, then we'll have to submit something and actually grab something from the API to make the login.

And we do that in the handle submit function.

The first thing we're going to do is to set the error to false just when we did when we finished our movies, and then I have a try block and then a catch block and we have the error.

For this catch.

We can set that or True.

That's the only thing we're going to do inside of the catch block.

So we're going to be in the try block now.

And first, we need to get the request token.

So I create a new const.

I actually noticed now also that I forgot to bump up the font size.

So I'm going to do that now, from now on is going to be bigger.

Okay, so I have a cost with a request token.

We're going to wait from the API, I have this function GET request token.

And of course, this one has to be an async function, because we are waiting here.

So Mark this one with a sync.

So that will hopefully get us the request token, if something goes wrong here, the catch block will set the error to true and we're going to handle that just in a second down in the JSX.

The cost, we're going to grab the session ID We await again, from the API, I have a function that's called authenticate.

And for this one, we're going to give it the request token first.

And then we give it the username, and then the password.

All right, that will hopefully get us our session ID.

And then we can set the user.

And this one, the set user is actually the context that we created, because we're grabbing the context here and the setter for the user.

So we're setting this one in the context, I'm going to set it with an object First, I want to set the session ID.

So I gave it from the session ID that's the one that we'll get back from the API.

We have a property that's called session underscore ID, all lowercase letters, and then I'm going to set the username.

And as this is also e6 syntax, I don't have to type out this twice, because it will interpret this automatically.

Alright, and then we just have one more thing to do.

And that is we have to navigate somewhere when we successfully logged in.

So we can navigate programmatically with react router, we use the navigate that we got here from that hook us navigate, we placed that one, we placed what we get back here in the navigate cost.

So navigate parenthesis and we just specify the URL.

And in this case, we want to go to the homepage.

So we specify it like this.

And I want to do some console, log in here, console log, the session ID just to see that we get something here, save the file, go back to our application.

And now we haven't styled this one.

We're going to do that in the next video.

But we can use the input fields here anyways.

So my login is vevo and then I have my password that I'm not going to tell you something like this, and I tried to log in.

And you can see that we get this object back from API, we get the session ID and the success is telling us true.

So that's really, really neat.

We know that our login system is working, and it redirected us to the homepage.

To go back to the login page.

I want to do one more thing here before we finished with the logic for this component.

Down below here just above the first label, I have a curly bracket and I'm going to create a short circuit, I'm going to check if the error is true.

Double ampersand If the error is true, we're going to have a div with a class name of error.

And then I'm just going to say there was an error, something like this.

And then I want to format it.

And then I'm going to say this file.

So you can of course type in whatever you want to save the file, go back to the application.

So just try to type something in here and click Login.

And you can see that we show this one here.

Instead, there was an error.

And we also get an error in our console.

So we know that the try and catch block is working.

So this is our login component and the logic and in the next video, we're going to create the styles for this component.

We have our login component and the functionality for that one.

And now we're going to create the stars for it.

So go back inside of the code editor and the login dot styles dot j s file.

We have our wrapper that's the only style component that we use him for this one.

First, we're going to display it as a flex.

we align dash items to center and we justify the content Center also just the center stuff.

Then we set the flex direction on this one is going to be column and we can save it to see what we've got so far.

You can see that we're centering it here in the middle of the screen.

So that's great.

Go back to the code, I'm going to set a max width to 320 pixels, the padding is going to be 20 pixels.

And the color is going to be from the variables, we have a color that's named dark gray.

So double dash dark grey.

Save it go back just to see what we've got, right? When I set the max width to 320 pixels, it's showing it to the left.

But if we set the margin to zero and auto, and save it, that will place it in the center again, so that's great.

Alright.

So that's everything for the wrapper.

Now we have the input, we nest, this one inside of the wrapper component, we set the width to 100%.

On the input fields, the height is going to be 30 pixels.

border is going to be one pixel solid.

We have a variable for color.

And we also use dark gray for that one.

Then we set the border dash radius to 20 pixels, the margin is going to be 10 pixels and zero.

And the padding is going to be 10 pixels, save the file, go back to the application.

And you can see that we created this nice little input fields here sweet with rounded corners, and it matched the overall the overall look of the application.

Then we just want to style our error class also dot error.

And for that one, I'm just going to set the color to red.

You can style this a little bit better if you want to do that.

So if we type something in here and click login, you can see that this is the error.

All right.

And that's actually it for this login component, I'm not going to do any heavy styling, as this is the bonus section of this course.

So if you want to do it nicer, you can do that yourself.

In the next video, we're going to be in the header and showed a logged in user and also have a log in bottom.

Okay, let's create the login system from the header, we're going to show a bottom to log in.

And I'm just going to place it in the middle actually here.

It may be should be to the right.

But yeah, as I told you, I'm not doing any heavy styling for this section.

So you can style it to your own liking later.

So let's go back inside of the application and inside the header component, so the header folder and the index.js file.

The one thing we need to add to the imports here is to actually import the context.

So we import context.

From dot dot forward slash and dot dot forward slash, again, we have the context file like this.

And this one is making an implicit return.

Now we need to have some functionality inside of it, we have to change this one into an explicit return.

Like this, we add the return statement here or reformat it just to make it a little bit nicer.

Some people also have the formatting to activate when you save the file, I'll actually I actually don't like that, because sometimes when I save it, and I'm not finished, it starts to format stuff.

And I don't like that.

That's why I do it manually, instead.

Alright, const user, we're going to grab the user from the context, we don't need to set anything here, we just need the user.

And recall the use context hooked, we actually need to import that one also appear.

So import react comma, curly brackets use context.

So we give this use context, hook the context.

And this will bring us the user.

So we don't need to destructure out the setter for the state, we just need to use so so that's why we're not destructuring out that one.

And we can do a console log user like this.

Save the file, go back to our application, I'm going to try to login again.

I click Login.

And you can see that we get this console log here.

So we have the session ID and the username of vaman.

And that's of course for vaman fault.

Alright, so we know that our context is working great.

And that's sweet.

So go back to the index.js file in the header folder.

And now we can use this one here.

So just between the two logos here.

I'm going to create curly brackets.

And the first thing I'm going to do is to check if we have a user and then I create a ternary operator.

So I have a question mark, parenthesis and the first thing I'm going to do if we have User are going to show a span with a class name of logged in, like this.

And I'm going to type out logged in as colon.

And then I have new quarter brackets, and I grabbed the use of dot username.

And that's from the object that we get back from the context, of course.

So when we are logged in, we're going to show the text logged in as and we also show in the username.

Otherwise, if we're not logged in, we have a colon, here, we have a new pair of parenthesis, are going to use the link component.

And it's going to link to if you remember this one, the link component is the one that we use from react router to navigate inside of our application.

This one is going to link to the login page like this.

And inside the link, I'm going to have a spam that has a class name of login.

And it says login and then do some nice auto formatting.

I'm going to move this one off and save the file and see if it works.

Go back to the application, we can't hardly see it here.

We're going to style this in a second.

But we have a login button.

So it takes us to the login page.

So here again, I'm going to log in.

And this is something that you also can do if you want you can store the user information in the session storage or in the local stories, there's a lot of discussion going on, on what is the best practices to use.

In this case, we have a session ID, so we have to request a new session ID on each session from the Movie Database API.

So I'm just storing it in the application itself.

So that means that it will get wiped out every time you reload application, I had to log in.

Again, if this was in the real world, we probably would have a login system that will also save this token somewhere.

So you don't have to log in every time.

And I actually have a YouTube video, where I show how to create a back end and set up JSON Web tokens and how to create a login system in a react application.

So this is a very simple use case on how you can create a login system here.

Alright, that was a side note, I'm going to click the Login button.

And hopefully up here Yeah, you can see that we showing logged in as beiben.

So it's working, we have to give it some styling also.

And this is just going to be a couple of rows.

So I'll do it in this video.

So inside the header.styles.js inside here, we actually don't need the class names that are set, we can just set the color to a variable of white, like this, and then we have the a tag, I set the color to the same variable there, double dash white.

And the text dashed declaration is going to be set to none.

Auto format.

Let's save it.

And also if we want, we can remove these classes, we don't need them, we can just have a span on this one's awesome thing like this, save the file, go back to the application, you can see that now we see it.

And yeah, this is probably not the most beautiful way, it doesn't look that good, because I'm just placing it in the middle.

Now, we would have some dedicated space for a login button and stuff like that.

But this is just to show the functionality.

So I'm not going to style it any better than this.

So I clicked the login.

And I log in again.

click the Login button, whoops, something, I guess I typed the password wrong here.

I log in again.

And that works.

And now we can see that we have this white text instead.

And it tells us that I'm logged in.

So that's great.

In the next video, we're going to create the rate component that we're going to show somewhere here, I think we're almost finished with the voting system.

But we need a rating component that we can place here in the movie info component.

So we're going to create that will now move back inside of the code editor and inside of components create a new folder that we call Wraith, capital R.

And inside of that folder, we create a new file that's called index dot j s and I actually not going to have any styling for this one.

I'm going to use the components as they are.

So first I'm going to import react.

And I'm also going to need the use state for this one.

Because it is going to be a control component I imported from react.

Then I create my component rate equals, and I'm going to destructure out the callback for this one.

Because when we vote, we need to have a callback function that will do something.

And in this case, it's going to send a request to the API.

That's a component I'm also going to export default rate like this.

And the first thing we do in this component is to create a state with a value and set value equals use state And we're going to start with the value five, the rating is going to be between one and 10.

And then we have the return statement and we return our JSX.

So I'm going to make it simple here, I create a wrapping div, and then I create an input.

And the type is going to be range.

So we create a range slider, the min value is going to be one, the max is going to be turn, and the value is going to be our state value.

And then on change, we have to change this state value.

So I want to show you also that you can create an inline function instead of creating a function up here to where the event E, I create an inline arrow function.

And then we set the value e dot turn target dot value, and this is enough.

And we will close this component.

Alright, so that's a range slider after the range slider, we want to show of our value like this.

And then I create a p tag just to get it on a new row.

And I create a button.

I have an onClick handler on this button.

And in this case, we have an inline arrow function because we are going to call our callback with a value.

And we give it the value if we don't have this inline arrow function here, and we just type it out like this, then it's going to instantly run this and it won't work.

So we have to have an inline function here as we providing an argument to this callback function.

Right, close it and inside of the button with type out rate, do some more formatting, save it, we're gonna move inside of movie info component in the index.js file.

And up here where we import the thumb, we also got to import our rate component, dot dot forward slash rate.

And then we're going to show the rate component somewhere below.

theme, we're going to place it Yeah, maybe here, just above the M tag for the text.

So I create a new div and inside that div, I have a p tag rate movie.

And below that one, we use a rate component.

And for now, we don't have a function that we're going to send into this one the callback function.

So just showing the component just to see that it works and shows up, save the file.

Go back to the application.

And you can see that we have the rate slider here.

And we have a rate bottom, it doesn't work.

Now, as you can see, because we're not sending in the callback function to it.

But this one will work in the next video, because we're going to tie all this together and make it work so that when we press this red button, we will send along this rating number to the API, and we will rate this movie.

Alright, we're almost finished.

And this is actually the last video in this course.

So hope you enjoy the course, we're going to tie this together.

So let's move inside of the code and inside the movie info component in the index.js file, the first thing we have to do is to grab the context, the context or import context, from dot dot forward slash and dot dot forward slash, again, and context.

So we're going to use the context.

And that means that we also need to import from up here, the use context hooked.

Right.

And now you hopefully can see how handy it is to have this global state because we can access it from any component in the application.

And in this case, we're going to grab the user and the session ID.

So you can send along the session ID to the API when the user rate the movie.

And now we're making this implicit return, we're going to change this one to an explicit return, so return and I created curly bracket, and then we need to have one below also.

There is some auto formatting, and go back up if it's in space.

And first, we're going to grab the user from our context, just as we did before the cost user use context.

And we've given you the context.

So this will give us the user here.

And then we are going to send in a callback function to our rate component here. So we're creating this function here in this component and send it along to the rate component.

We're going to call this function calls handle rating. This is going to be an async function because we're making a an API call.

We have the value And then we can do some stuff inside of here.

So this value is going to be the value from the range slider.

So create a new cost rate equals, then I wait.

And from the api.id and I imported up here.

No, I also need to import the API.

We do that up here, import API from dot dot forward slash dot dot forward slash API, like this, then I go back down here and change this one.

API dot, I'm going to grab the function that's called rate movie.

And if you want to know more about these functions, you can always check them out in the api.js file.

Because I told you probably too many times now that I pre made these functions for you.

So you don't have to do that in this course.

Alright, move back to the movie and for an index.js file.

So the rate movie function is going to take in three arguments.

So we have the user dot session ID.

And we have the movie ID, because we need to know the movie ID of the movie that we want to rate.

And we also want to give it the value, that's the rating value.

Right.

And that's actually everything we need to do.

In this case, I just want to console log out to rate to see that we get something back and that the rating was working.

So we can use this handle rating.

Now down below here, we can give it to the rate component, we have a prop.

That's called callback.

And we give it to hand reading and save the file. And hopefully this should be it.

Go back to the application.

Yeah, we have one more thing to do, because I don't want to show this rate slider when we're not logged in.

So we can do that also.

So just here, when we have the rating, outside of the wrapping dem are going to create a ternary operator, I'm going to check if you sir.

Then I'll double ampersand, and I move my M curly bracket down here or to format it.

And it will also auto generate this parenthesis.

So if the user exists, if we're logged in, we're going to show the rating.

Otherwise, we don't show anything.

Save the file go back to our application, you can see that we're not showing the rate slider now we have to log in.

So we click the Login button, and I log in.

And now we're logged in, we're going to go to movie here.

Now you can see that we see the rating slider.

So I don't actually know if this movie is any good, but I'm going to give it a rating or eight.

And I click the red button.

And here you can see in the console that we got a success of true and status code one, a status message success.

And if we click rate again, you can see that we get another message because it says that the item record was updated successfully.

So you can update your rating score.

If you want to do that.

There's also a resource in the endpoint if you want to remove the score also.

So there are some neat stuff that you can do with the Movie Database API.

And I hope this inspired you to actually build more stuff into this application, because now you have a good foundation.

And for example, the next step you can do is to create a logout button for the user.

And the way I would do it in this case is that I can just wipe out the global context the state here and remove the user from the global state.

And that will log out the user we don't have to do anything else with the Movie Database API or something like that.

Alright, that's it for this course.

I hope you enjoy this.

I sure enjoy this.

This is the third iteration of the course.

So this is the third time that I actually update it and re recorded from scratch.

And if you want free tutorials, you can always visit my YouTube channel, search for vaman Fox, or you can go to vevo in fact.com if you want more courses from me.