---
title: Comment créer votre propre extension VS Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-04T04:05:00.000Z'
originalURL: https://freecodecamp.org/news/making-vscode-extension
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/0-lDZSUwewtGWo6M4J.jpeg
tags:
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: Visual Studio Code
  slug: visual-studio-code
- name: Visual Studio Code
  slug: vscode
seo_title: Comment créer votre propre extension VS Code
seo_desc: "By Pramono Winata\nI just made my first VS Code extension. And it felt\
  \ good! This article will cover basic steps to help you create your own VS Code\
  \ extension. Along the way I'll share what I learned from making one for the first\
  \ time. \nI am not an ex..."
---

Par Pramono Winata

Je viens de créer ma première extension VS Code. Et c'était génial ! Cet article couvrira les étapes de base pour vous aider à créer votre propre extension VS Code. En cours de route, je partagerai ce que j'ai appris en en créant une pour la première fois. 

Je ne suis pas encore un expert en la matière, mais je peux vraiment dire que **rien n'est aussi difficile que cela en a l'air.** 💡

## Parlons de VS Code et de sa Place de Marché d'Extensions

Si vous avez ouvert cet article, vous avez probablement au moins entendu parler de VS Code (ou Visual Studio Code). Si ce n'est pas le cas, c'est essentiellement un éditeur de code léger développé par Microsoft.

Puisque VS Code est un éditeur de code, il peut fonctionner beaucoup plus rapidement et plus légèrement qu'un IDE typique comme Eclipse. Mais avec cette performance vient un inconvénient : les IDE offrent souvent de meilleurs outils tels que des linters intégrés, de meilleurs modèles de code, des outils de gestion de versions de code, et certaines fonctionnalités comme l'auto-complétion.

Mais là où VS Code brille vraiment, c'est grâce à la puissance de la communauté. Il vous permet d'installer des extensions qui proviennent directement de la place de marché de VS Code elle-même. Ces extensions vous permettent de le personnaliser comme vous le souhaitez. Vous pouvez, par exemple, ajouter un linter ou toute autre fonctionnalité comme des parenthèses colorées. Vous pouvez même mettre un nyan cat dans votre VS Code !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-from-2020-05-31-23-42-52.png)
_Qui n'aime pas un nyan cat ?_

## Pourquoi devriez-vous créer une extension VS Code ?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/0-EErfJXzBUg_qzUsI.jpeg)

Oui, « pourquoi » est le mot clé ici. C'est la première et la plus importante chose à aborder lorsque vous voulez commencer quelque chose. 

Demandez-vous pourquoi vous voulez le faire ? La plupart des gens répondent généralement parce qu'ils veulent **apprendre quelque chose** ou **gagner en notoriété**, ou peut-être les deux. Mais plus il y a de raisons, plus vous aurez de motivation.

Une chose que je peux dire, c'est que vous n'avez pas besoin de penser grand pour l'instant. Créez simplement un outil très spécifique, que peut-être seul vous utiliserez. La première étape est toujours la plus difficile. Et à la fin de la journée, au moins vous vous êtes aidé avec votre extension.

Pour ma part, j'ai construit une extension pour une raison particulière : je voulais créer un outil que je pourrais utiliser pour augmenter ma productivité. Et qui pourrait peut-être même aider une petite partie de la communauté autour de moi. (Spoiler : c'est un générateur de tests unitaires pour Golang)

C'est pourquoi les extensions que j'ai créées sont très précises et ont un cas d'utilisation très spécifique. Je ne vise pas un grand marché, je cherche à augmenter ma productivité et à apprendre quelque chose de nouveau. Je pense que c'est une raison suffisante pour moi.

Et bien sûr, tout semblait impossible au début. Créer des extensions VS Code semble être un travail de génie (mais bien sûr, ce n'est pas le cas). Comme j'ai beaucoup de temps libre en ce moment, je me suis dit que je pourrais aussi bien essayer.

## La toute première étape pour créer une extension VS Code

Pour commencer, vous devez avoir VS Code installé. Au cas où vous ne l'auriez pas encore, je vais simplement mettre le lien de téléchargement [ici](https://code.visualstudio.com/download).

Les extensions VS Code supportent deux langages principaux : JavaScript et TypeScript. Avoir des connaissances dans l'un de ces langages est donc assez obligatoire.

Assurez-vous également d'avoir Node.js installé, car nous allons utiliser beaucoup de paquets npm ici.

## Comment générer un modèle d'extension VS Code

Ah, les modèles. Très pratiques. VS Code a déjà son propre générateur de modèles, alors plongeons directement dedans.

Tout d'abord, installez votre générateur de modèles avec `npm install -g yo generator-code`

Ensuite, exécutons-le avec `yo code`. Il affichera cette chose étrange (🤔) et la sélection de la langue. Choisissez simplement votre langue préférée et continuez. (J'ai choisi JavaScript ici).

![Image](https://www.freecodecamp.org/news/content/images/2020/06/yo-code.png)
_yo code_

Ensuite, vous devrez modifier le nom et la description de votre extension. Vous pouvez simplement continuer avec ce que vous préférez.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-from-2020-05-26-23-07-28.png)
_ou peut-être simplement entrer tout le long_

Maintenant, un dossier appelé hellovscode sera créé dans votre répertoire personnel. Ouvrez-le avec VS Code en tapant simplement `code hellovscode` dans le répertoire du dossier.

Utilisez la touche `F5` pour exécuter votre extension et une autre fenêtre s'ouvrira. Maintenant, appuyez sur `ctrl+shift+p` et trouvez la commande `Hello World`, exécutez-la, et une fenêtre contextuelle devrait apparaître dans le coin inférieur droit. Comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/sample-hello.gif)
_Magie ? Non. Juste une collection de code._

Voilà ! Vous venez d'exécuter votre première extension. Mais que se passe-t-il réellement avec tout cela ? Ne vous inquiétez pas, je vais expliquer quelques éléments ci-dessous, principalement concernant deux fichiers : `extension.js` et `package.json`.

## Qu'est-ce que le fichier Extension.js dans VS Code ?

C'est là que vous passerez la plupart de votre temps à coder. Ce fichier contiendra tous vos blocs de code et votre logique de flux.

Il n'y a pas beaucoup de différence entre cela et le code Node normal. Mais l'une des principales différences est l'enregistrement de vos commandes. Vous rencontrerez ce bloc `vscode.commands.registerCommand('hellovscode.helloWorld'`.

En résumé, cela enregistrera votre appel de fonction pour qu'il soit utilisé.

Une autre différence est l'utilisation fréquente de l'API VS Code – mais nous y reviendrons plus tard.

Si vous avez parcouru le code, vous verrez aussi ceci : `vscode.window.showInformationMessage('Hello World from hellovscode!');` 

En tant qu'expérience, essayez de changer la valeur du message et essayez de l'exécuter à nouveau.

### Package.json

Ce fichier est celui qui reliera essentiellement les commandes que vous avez créées dans `extension.js` avec les commandes que vous avez définies.

Vous verrez la commande que vous avez enregistrée ci-dessus `hellovscode.helloWorld` mise comme une partie de la commande intitulée `Hello World`. Et c'est ainsi que la commande se lie réellement à votre code.

Outre cela, ce fichier permettra également de placer la commande dans la barre de clic droit. Il filtrera également où la commande doit apparaître (type de fichier).

## Comment publier votre plugin VS Code

Au cas où vous voudriez publier votre extension, je vais vous montrer comment faire cela ici :

Étape 1 : Tout d'abord, installez vsce avec `npm install -g vsce`. Nous allons utiliser cela la plupart du temps pour publier.

Étape 2 : Si vous n'avez pas encore de compte Microsoft, vous devriez [vous inscrire ici](https://signup.live.com/) car nous aurons besoin du jeton d'accès que vous obtiendrez.

Étape 3 : Une fois que vous avez le compte, connectez-vous à la [place de marché](https://marketplace.visualstudio.com/VSCode). Créez votre [organisation](https://aex.dev.azure.com/me?mkt=en-US) et cliquez dessus (vous devriez voir quelque chose comme ci-dessous).

![Image](https://www.freecodecamp.org/news/content/images/2020/06/ss.png)

Étape 4 : Maintenant, cliquez sur le coin supérieur droit où se trouve le cercle rouge et sélectionnez Jeton d'Accès Personnel. Créez votre jeton d'accès personnel et choisissez toutes les organisations accessibles avec un accès complet.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-from-2020-05-29-23-56-42.png)

Étape 5 : Mémorisez votre jeton car vous l'utiliserez lors du téléchargement de votre extension.

Étape 6 : Vous devrez maintenant créer votre identité de publieur. Alors, allez dans votre invite de commande et tapez `run vsce create-publisher VOTRE_NOM_DE_PUBLIEUR`.  
Insérez votre propre nom, email et jeton d'accès personnel lorsque vous y êtes invité. Votre compte de publieur devrait être créé avec succès.

Étape 7 : C'est l'heure de la publication ! Préparez votre environnement d'extension dans l'invite de commande et tapez `vsce package`. Cela packagera votre extension au format de la place de marché. Ensuite, tapez `vsce publish`.

Et c'est tout, votre extension sera publiée.

En passant, lors de la publication, vous devriez modifier votre readme (au moins la première partie où il est écrit `This is Readme for..` ) car vsce le détectera et vous demandera de le modifier.

## Quelques conseils supplémentaires pour créer des extensions VS Code

Maintenant, vous devriez avoir une compréhension de base de comment fonctionnent les extensions VS Code. Ici, je vais partager quelques choses que j'ai apprises.

### Utilisation de l'API de VS Code

VS Code lui-même a fourni de nombreuses API pour vous aider à créer votre extension. Vous pourriez rencontrer plusieurs obstacles courants lors de la création de votre extension, comme obtenir la position de votre curseur, obtenir la position de la ligne, ou peut-être obtenir le mot surligné. Tout cela peut être résolu en utilisant l'API de VS Code.

Vous devriez lire leur [documentation](https://code.visualstudio.com/api/references/vscode-api) et expérimenter avec leur API. Vous pouvez même essayer de lire leur code API ! Avec la quantité de documentation à l'intérieur du code lui-même, vous devriez pouvoir déterminer quelle API sera la plus utile.

### Googler des choses (lire la documentation ou le code)

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-169.png)

La plupart du temps dans notre vie de programmeur, lorsque nous sommes bloqués, il y a toujours Google ou [Stack Overflow](https://stackoverflow.com/) qui peuvent fournir une aide rapide.

Mais cette fois, cela ne vous sauvera pas toujours.

Tout d'abord, googler pour obtenir de l'aide dans ce cas est assez délicat. Par exemple, disons que vous voulez surligner un mot sur le curseur – vous pourriez rechercher `vs code extension how to get total line...` ou quelque chose de similaire.

Mais laissez-moi vous dire, la plupart du temps, cela vous dirigera vers l'extension réelle elle-même ou vous donnera un manuel sur la façon d'utiliser VS Code.

Une façon de vous faciliter la tâche est d'ajouter le mot-clé « API » dans votre recherche, comme `vs code extension api how to ...`.

De plus, il est assez difficile de trouver les réponses pertinentes sur Google, car la communauté des développeurs n'est pas si grande, et les extensions VS Code peuvent sembler intimidantes pour de nombreux nouveaux venus. Mais en vérité, **ce n'est pas exactement si difficile**.

C'est pourquoi parfois la meilleure façon d'apprendre à développer une extension VS Code est de lire la documentation ou le code.

## Un exemple de dépôt GitHub d'extension VS Code

J'ai fourni un exemple de manipulation de texte dans mon [dépôt GitHub](https://github.com/pramonow/vscode-extension-ut) qui pourrait aider pour les références de code (attention à certains codes désordonnés cependant !). Le code générera quelques tests unitaires de modèle dans le langage Go.

## Conclusion

Ce que j'ai couvert ici ne sont que les bases de la création d'une extension VS Code. Un message que je veux que vous gardiez à l'esprit est que **ce n'est pas aussi difficile que cela en a l'air.** Parfois, vous devez simplement vous pousser un peu et essayer.

Vous pourriez rencontrer quelques défis en cours de route, mais si vous ne commencez même pas, vous passez complètement à côté.

En fin de compte, merci d'avoir pris le temps de lire cela. J'espère que vous l'avez apprécié et que vous avez commencé à comprendre toutes les choses que je viens d'expliquer.

Et j'espère que vous commencerez également à créer une extension !

_Bon codage à vous tous en cette période de distanciation sociale._