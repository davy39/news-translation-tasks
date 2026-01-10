---
title: Comment créer un générateur de citations aléatoires avec JavaScript et HTML,
  pour les débutants absolus
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-03T02:42:10.000Z'
originalURL: https://freecodecamp.org/news/creating-a-bare-bones-quote-generator-with-javascript-and-html-for-absolute-beginners-5264e1725f08
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9CjruUOhJY8hgQ_WAsSqWw.png
tags:
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment créer un générateur de citations aléatoires avec JavaScript et
  HTML, pour les débutants absolus
seo_desc: 'By Sophanarith Sok

  This tutorial is intended for beginners who want to learn how to create a simple
  web application using JavaScript. It will help you understand the interaction between
  JavaScript and an HTML document, and how they work together to d...'
---

Par Sophanarith Sok

Ce tutoriel est destiné aux débutants qui souhaitent apprendre à créer une application web simple en utilisant JavaScript. Il vous aidera à comprendre l'interaction entre JavaScript et un document HTML, et comment ils fonctionnent ensemble pour afficher des éléments sur le navigateur web pour que les utilisateurs puissent les voir.

Si vous n'avez absolument aucune expérience en HTML et JavaScript, pas de souci. Je vais vous guider à travers chaque ligne de code et expliquer tout en détail. À la fin de cette leçon, vous devriez avoir une bien meilleure compréhension de la manière dont JavaScript fonctionne avec HTML pour rendre les pages web interactives.

Dans ce projet, nous allons créer un générateur de citations aléatoires qui affiche une citation aléatoire à l'utilisateur chaque fois qu'il appuie sur un bouton. Pour commencer, vous aurez besoin de trois éléments essentiels qui sont presque toujours utilisés pour chaque projet web :

* un navigateur web
* un éditeur de texte
* l'envie de construire des choses

Pour ce tutoriel, j'utiliserai le navigateur web Google Chrome, l'[éditeur Sublime Text 3](https://www.sublimetext.com/3), et bien sûr, mon propre désir de construire et d'enseigner. Vous pouvez utiliser les outils avec lesquels vous êtes à l'aise.

### Commençons !

La première chose que nous allons faire est de créer le dossier qui contiendra tous nos fichiers constituant le projet. **Créez un dossier vide** sur votre bureau et nommez-le « générateur de citations ». **Ouvrez Sublime Text** et **glissez le fichier dans Sublime**. Maintenant, nous devrions avoir le dossier accessible via la barre latérale.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-128.png)
_Créez un dossier vide sur votre bureau_

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-129.png)
_Glissez le dossier dans Sublime Text. Il apparaît maintenant dans le menu de la barre latérale._

La plupart des projets web se composent d'au moins un fichier HTML, JavaScript et CSS. Créons ces fichiers dans le dossier « générateur de citations ».

Dans Sublime Text, faites un clic droit sur le dossier « générateur de citations » dans la barre latérale et cliquez sur **créer un nouveau fichier**. Une barre d'entrée apparaîtra en bas pour nommer le fichier. Tapez « index.html » et appuyez sur Entrée. Vous avez maintenant créé le fichier index.html. **Répétez cette étape deux fois de plus**, mais créez un fichier nommé « javascript.js » et « style.css » (sans les guillemets). Il est important de s'assurer que lorsque vous nommez un fichier, les lettres sont toujours en minuscules pour éviter toute complication.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-130.png)
_Vos fichiers devraient maintenant ressembler à ceci._

Maintenant que nous avons tous nos fichiers configurés, créons notre fichier HTML qui servira de base à notre projet web. Nous commencerons par un code HTML de base dans notre fichier index.html avant d'ajouter quoi que ce soit.

Ci-dessous se trouve notre fichier HTML vide. Vous pouvez considérer cela comme notre squelette HTML qui contiendra tout le contenu, que nous ajouterons plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-131.png)

Maintenant, nous devons lier notre fichier JavaScript à notre document HTML afin que notre code JavaScript puisse interagir avec le document HTML. Nous ajouterons également du texte dans les balises **<title>**, ajouterons un élément **<h1>**, créerons un élément **<div>** avec un **id** nommé « quoteDisplay », et aussi un élément **<button>** avec un attribut **onclick** avec « newQuote() » passé dedans.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-132.png)

### Décomposons cela

Si vous êtes confus quant à la manière dont chaque partie du code HTML sert son but, alors je vais vous l'expliquer ici. Si vous savez exactement ce que chaque élément fait et pourquoi il est là, alors vous pouvez passer à la section suivante pour continuer.

Tout d'abord, nous avons ajouté « Quote Gen » entre les balises **<title>**. La balise title prend le texte entre elle et l'affiche sur l'onglet de votre navigateur web lorsqu'il est ouvert.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-133.png)
_Le contenu entre les balises &lt;title&gt; s'affichera sur l'onglet du projet lorsqu'il est ouvert dans un navigateur._

Lors de la première étape, nous devons également nous assurer de lier le fichier javascript.js en bas du document HTML juste avant la balise de fermeture **<body>**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ecsEEifOsFJgppdzCLavaQ.png)
_Lien vers le fichier javascript.js_

Deuxièmement, nous avons créé un élément **<h1>** avec « Simple Quote Generator » à l'intérieur. Cela servira à afficher un titre dans notre page web.

![Image](https://cdn-media-1.freecodecamp.org/images/1*49TfOW4xx7CvTWV1G9N0vQ.png)
_La balise &lt;h1&gt; affichera un texte en grand_

Ensuite, nous avons créé un élément **<div>** avec un attribut **id** défini sur « quoteDisplay ». Un élément **<div>** fonctionne comme un diviseur pour les documents HTML. Les éléments **<div>** aident à organiser le contenu dans une page web. L'attribut **id** fonctionne comme un identifiant afin que JavaScript puisse facilement le récupérer et le manipuler. Dans ce cas, nous utiliserons JavaScript pour récupérer l'élément avec l'**id** « quoteDisplay » pour placer des citations dans l'élément **<div>**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*t4TyiuXnNPoc3VCyYIADiA.png)
_Les citations seront affichées dans cet élément &lt;div&gt; via notre fichier JavaScript_

Après cela, nous créons un élément **<button>** avec un attribut **onclick** avec « newQuote() » passé en tant que paramètre. L'élément **<button>**, comme vous l'avez deviné, est un bouton qui fera quelque chose lorsque vous cliquerez dessus. L'attribut **onclick** est utilisé pour définir une fonction au bouton, de sorte que chaque fois que vous cliquez sur le bouton, il exécutera la fonction qui a été passée dans l'attribut **onclick** du **<button>**.

Dans ce cas, chaque fois que vous cliquez sur le bouton, il exécutera la fonction newQuote(). Bien sûr, nous n'avons pas encore défini la fonction newQuote(). Si vous ouvrez le projet dans un navigateur et appuyez sur le bouton, il générera une erreur dans la console puisque la fonction n'existe pas actuellement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2oZ0sCSLwAMr-LkT4lR_hQ.png)
_Notre élément &lt;button&gt; produira ce bouton_

Enfin, voici un rappel pour montrer à quoi ressemble notre fichier index.html complet actuellement et ce qu'il produit dans le navigateur web. Pour ouvrir le projet, utilisez un navigateur web pour ouvrir le fichier index.html.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AkiS2Y0Pu8StCvZbANb_xg.png)
_Ce que nous avons jusqu'à présent_

### Réfléchir logiquement en utilisant du code

Il est enfin temps de commencer à travailler sur le JavaScript dans notre fichier javascript.js afin que nous puissions développer notre propre fonctionnalité de génération de citations.

Maintenant, avant de commencer à coder, réfléchissons logiquement à la manière dont nous pouvons créer une machine à générer des citations avec du code. Nous ne pouvons pas simplement commencer à coder sans réfléchir d'abord.

Nous devons déterminer ce que nous voulons et quand nous le voulons. Pour ce projet, nous voulons des citations ! Quand les voulons-nous ? Nous les voulons maintenant ! Oh, euh... Je veux dire que nous les voulons chaque fois que l'utilisateur appuie sur le bouton.

Maintenant que nous avons résolu la première question, nous devons poser la deuxième. Qu'est-ce que les citations ? Je veux dire, vraiment, qu'est-ce que c'est ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*7KnvfVpZXP7aw9NRQca1lw.jpeg)
_« Les citations sont des chaînes de caractères. »_

Merci Jaden ! Oui ! Les citations sont composées de lettres, qui forment des mots. Dans le monde de la programmation, les mots sont classés comme des chaînes de caractères, donc nos citations devront être des [**chaînes de caractères**](http://www.w3schools.com/jsref/jsref_obj_string.asp) !

Puisque nous savons que nous aurons plusieurs citations, et que chacune sera choisie aléatoirement, le meilleur choix serait de stocker plusieurs chaînes de caractères dans un [**tableau**](http://www.w3schools.com/js/js_arrays.asp).

Si vous ne le saviez pas déjà, les éléments d'un tableau sont récupérés en appelant leur [**numéro d'index de tableau**](http://www.w3schools.com/js/js_arrays.asp). Les détails techniques sont hors du cadre de ce tutoriel, mais en termes simples, chaque élément d'un tableau est représenté par un nombre entier dans l'ordre chronologique. Le premier élément d'un tableau a un numéro d'index de 0, chaque élément suivant augmente de un.

Pour récupérer une citation aléatoire d'un tableau, nous savons maintenant que nous devons produire un nombre aléatoire chaque fois que l'utilisateur clique sur le bouton. Ensuite, nous utiliserons ce nombre aléatoire pour récupérer une citation du tableau et placer cette citation dans le document HTML, ce qui, à son tour, affichera la citation sur le navigateur pour l'utilisateur.

C'est tout ! Nous avons résolu comment créer un générateur de citations aléatoires en réfléchissant logiquement en code ! Voici un résumé de la logique que nous avons élaborée pour notre projet :

1. Les citations sont plusieurs chaînes de caractères qui doivent être stockées dans un tableau.
2. Chaque fois que le bouton est pressé, un nombre entier aléatoire doit être généré.
3. Le nombre servira de représentation du numéro d'index de tableau pour le tableau de citations.
4. Une fois que nous avons récupéré la citation choisie aléatoirement du tableau en utilisant notre nombre entier généré aléatoirement, nous la placerons dans le document HTML.

### C'est l'heure de coder !

Wow ! Nous en sommes arrivés là et nous n'avons pas encore commencé à programmer ! Bienvenue dans le monde de la programmation !

Je plaisante.

Pas vraiment.

Vous allez passer beaucoup de temps à coder dans cette carrière (ou ce passe-temps). Mais mon point est que vous allez passer encore plus de temps à réfléchir à la logique de programmation et à la manière de résoudre des problèmes. La programmation ne consiste pas à taper 100 mots par minute pendant 20 minutes sur le clavier. Cela n'arrivera pas.

<iframe src="https://giphy.com/embed/HoffxyN8ghVuw" width="480" height="275" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

Maintenant que nous avons tout la logique en place. Commençons à coder. Nous allons maintenant travailler dans le fichier **javascript.js**.

Nous devons soit créer nos propres citations, soit les copier à partir d'une source en ligne.

J'ai recherché « Best Quotes » sur Google et j'ai copié les 10 premières d'un [_site web_](http://www.briantracy.com/blog/personal-success/26-motivational-quotes-for-success/), puis je les ai placées dans un tableau séparées par des virgules. Assurez-vous de placer vos citations entre des guillemets simples ou doubles. Si votre citation contient des apostrophes, des guillemets simples ou doubles, vous devrez peut-être utiliser des barres obliques inverses pour [**échapper ces caractères**](http://www.w3schools.com/js/js_strings.asp) afin que JavaScript sache que les symboles font partie de la chaîne de caractères, et non de la syntaxe de codage.

Comme vous pouvez le voir sur l'image ci-dessous, j'ai défini une variable appelée « quotes » et je l'ai mise égale à un tableau rempli des citations que j'ai choisies sur [internet](https://i.ytimg.com/vi/cNycdfFEgBc/maxresdefault.jpg).

![Image](https://cdn-media-1.freecodecamp.org/images/1*SVJuLemM2aHiuiwAHBqmzg.png)
_Mon tableau de citations._

Maintenant, nous devons créer notre fonction newQuote() dont j'ai parlé plus tôt dans la section HTML de ce tutoriel. Pour notre fonction newQuote(), nous devons générer un **nombre entier aléatoire allant de 0 à la longueur de notre tableau de citations**. Je vais expliquer plus en détail ci-dessous.

Tout d'abord, nous appelons la fonction Math.floor(). La fonction Math.floor() prend un paramètre et arrondit le nombre vers le bas à l'entier le plus proche. Par exemple, si nous appelons Math.floor(5.7), elle retournera 5.

Deuxièmement, nous allons passer Math.random() comme paramètre dans Math.floor(). La fonction Math.random() générera un nombre décimal aléatoire entre 0 et 1.

Donc, supposons que nous avons ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*seX2GQBGVyg7iAj59tj7GQ.png)
_Appel de Math.floor() avec Math.random() passé comme paramètre_

Si nous affichons notre randomNumber dans la console à cet état, il retournera toujours 0. Cela est dû au fait que Math.random() sera toujours un décimal entre 0 et 1 tel que 0.4, 0.721, 0.98, et ainsi de suite. Parce que nous passons Math.random() dans Math.floor() comme paramètre, Math.floor() arrondit toujours vers le bas au décimal le plus proche, donc chaque décimal entre 0 et 1 reviendra toujours à 0.

Alors, quel est l'intérêt de faire cela ? Eh bien, pour créer nos numéros d'index de tableau, nous avons besoin de nombres entiers, mais nous avons besoin de nombres entiers aléatoires. Pour générer des nombres entiers aléatoires et éviter de toujours retourner 0, nous devons prendre notre décimal aléatoire et le multiplier par un nombre entier.

Maintenant, essayons quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*brj-QRKTZCUvwbBzVF8CBQ.png)
_Un décimal généré aléatoirement multiplié par 20, puis arrondi à l'entier le plus proche_

Si nous affichons randomNumber dans la console, les résultats seront compris entre 1 et 19. Maintenant, je pourrais utiliser cet état actuel de randomNumber pour extraire une citation du tableau de citations, mais cela ne fonctionnera que si le numéro d'index du tableau existe dans le tableau, sinon une erreur sera générée.

Par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3JaYVWqjXP9neimXXAz34Q.png)
_Cela retournera undefined_

J'ai actuellement seulement 10 chaînes de caractères dans mon tableau de citations, donc tout nombre supérieur à 9 retournera **undefined** puisque cela n'existe pas dans le tableau.

Pour résoudre ce problème, nous devons multiplier Math.random() uniquement par la longueur de notre tableau de citations. En faisant cela, nous pouvons ajouter ou supprimer autant de chaînes de caractères du tableau que nous le souhaitons et notre variable randomNumber retournera toujours un nombre valide puisque nous utilisons la méthode quotes.length pour toujours obtenir la longueur actuelle de notre tableau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xm3wHx2OriKnMUetoU_MEQ.png)
_randomNumber générera toujours un numéro d'index de tableau valide pour notre tableau de citations_

Maintenant, nous avons besoin d'un moyen d'utiliser la valeur de randomNumber pour récupérer aléatoirement une citation du tableau de citations et placer la citation dans notre document HTML et l'afficher à nos utilisateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RJIAwk-neVc82TcgYCZ1sg.png)
_Placer la citation dans l'élément HTML quoteDisplay_

Vous souvenez-vous comment j'ai mentionné que nous utilisons les ID HTML pour permettre à JavaScript de récupérer et de manipuler facilement les éléments HTML ? Eh bien, c'est ce que nous faisons maintenant avec l'ID HTML **quoteDisplay** que nous avons créé précédemment.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CfRX7oTE08Jmu5FBI6NHyQ.png)
_Récupération de l'élément HTML avec l'id quoteDisplay_

En utilisant document.getElementById(), nous pouvons passer n'importe quelle chaîne de caractères et JavaScript parcourra notre document HTML et la récupérera pour que nous puissions faire ce que nous voulons avec elle. Nous allons passer 'quoteDisplay' comme paramètre pour récupérer l'élément HTML avec l'id « quoteDisplay ».

Maintenant, nous allons utiliser la méthode .innerHTML pour passer une citation récupérée aléatoirement de notre tableau comme valeur qui sera ajoutée à notre élément HTML quoteDisplay.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HoxL49JVaVwpggIkiCL2lQ.png)
_Passer notre citation aléatoire comme valeur interne de l'élément quoteDisplay_

Nous définissons innerHTML égal à notre tableau de citations avec notre variable randomNumber passée comme numéro d'index de tableau. Maintenant, notre fonction newQuote() est complète !

![Image](https://cdn-media-1.freecodecamp.org/images/1*bHjHZVJf05BCUpeEciSGTQ.png)
_Votre fichier javascript.js devrait ressembler à ceci_

### Mission accomplie !

Si vous êtes arrivé à cette partie du tutoriel, vous avez terminé le projet ! Félicitations ! Vous avez presque terminé la construction du générateur de citations aléatoires.

Maintenant, tout ce que vous avez à faire est d'ouvrir le projet dans votre navigateur et de voir si cela fonctionne ! Faites cela en glissant votre fichier index.html dans votre fenêtre de navigateur.

Appuyez sur le bouton, et il devrait afficher une citation aléatoire à l'écran. Appuyez sur le bouton autant de fois que vous le souhaitez. Chaque fois, une nouvelle citation devrait remplacer celle actuellement à l'écran.

Vous pouvez ajouter autant de citations que vous le souhaitez dans le tableau de citations.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yKlV6ORDPIsTc0qMaP0Log.png)
_Produit fini_

Jetez un coup d'œil à un aperçu de l'ensemble de nos fichiers de projet côte à côte qui composent ce générateur de citations aléatoires.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6byNQiPEKjPVwQg1CbQZDA.png)
_Le code source de notre projet_

### Et maintenant ?

Vous avez créé un générateur de citations aléatoires entièrement fonctionnel et vous vous demandez probablement où aller à partir de là.

Vous pensez probablement que ce générateur de citations aléatoires est très ennuyeux et que personne ne l'utiliserait probablement. Et vous avez absolument raison. Ce projet semble assez simple, et c'est à vous de changer cela.

Vous pouvez améliorer ce projet en ajoutant vos propres fonctionnalités et styles.

Au début de ce tutoriel, nous avons créé un fichier style.css que nous n'avons pas utilisé. [**CSS**](http://www.w3schools.com/css/css_intro.asp) **est utilisé pour rendre les pages web jolies et colorées.** C'est à vous d'ajouter au fichier CSS pour le style si vous le souhaitez.

Vous pouvez rechercher des tutoriels CSS pour des conseils supplémentaires. Laissez libre cours à votre imagination et faites de ce projet le vôtre ! Faites ce que vous voulez ! Le codage est magique et vous êtes un sorcier, Harry !

Si vous êtes curieux de voir à quel point un projet peut changer avec CSS et quelques lignes de code JavaScript supplémentaires, consultez ma propre version de ce générateur de citations aléatoires que j'ai intitulée « Epiphany Clock » [**ici**](http://codepen.io/sok213/full/NqJYzb/).

---

Si vous avez apprécié ce tutoriel, veuillez cliquer sur le bouton cœur et le partager ! N'hésitez pas à laisser des commentaires, des questions ou des retours. Merci et bon codage !