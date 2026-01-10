---
title: Apprendre les bases du développement web – HTML, CSS et JavaScript expliqués
  pour les débutants
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-08-10T21:02:00.000Z'
originalURL: https://freecodecamp.org/news/html-css-and-javascript-explained-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/HTMLCSS.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Apprendre les bases du développement web – HTML, CSS et JavaScript expliqués
  pour les débutants
seo_desc: 'If you are learning web development, you will come across terms like HTML,
  CSS, and JavaScript. These are often called the building blocks of the Web.

  These three tools dominate web development. Every library or tool seems to be centered
  around HTML,...'
---

Si vous apprenez le développement web, vous rencontrerez des termes comme HTML, CSS et JavaScript. Ceux-ci sont souvent appelés les briques de base du Web.

Ces trois outils dominent le développement web. Chaque bibliothèque ou outil semble être centré autour de HTML, CSS et JS. Donc, si vous voulez devenir développeur web, vous devez bien les apprendre.

Vous découvrirez également que les sites web sont principalement construits à partir de ces trois langages.

Mais vous vous demandez probablement ce que chacun d'eux est et à quoi il sert vraiment. Qu'est-ce qui rend ces langages si spéciaux et importants ? Et qu'est-ce qui les rend si omniprésents que vous ne pouvez pas vous empêcher de les voir dans chaque tutoriel et sujet basé sur le développement web ?

Eh bien, maintenant vous n'avez plus besoin de vous demander.

Dans cet article, je vais expliquer les bases de ce que sont HTML, CSS et JavaScript, comment ils font fonctionner le Web, et ce qu'ils font chacun de leur côté.

## Qu'est-ce qu'Internet ?

Internet est simplement un réseau d'ordinateurs qui communiquent entre eux pour envoyer et recevoir des données (informations).

Chacun de ces ordinateurs sur Internet peut être distingué et localisé par un numéro unique appelé **adresse IP**. Une adresse IP ressemble à ceci : `168.212.226.204`

### Qu'est-ce que le Web ?

Le Web est un sous-ensemble d'Internet.

Comme tout autre réseau d'ordinateurs, le Web est composé de deux principaux composants : le client navigateur web et le serveur web.

Le client demande les données et le serveur **partage** ou **fournit** ses données. Pour y parvenir, les deux parties doivent établir un accord. Cet accord est appelé **Interface de Programmation d'Application** ou en abrégé, **API**.

Mais ces données doivent être organisées et formatées de manière compréhensible par les utilisateurs finaux qui ont une gamme variée d'expériences et de compétences techniques.

C'est là que HTML, CSS, JavaScript et tout le concept de développement web entrent en jeu.

## Qu'est-ce que HTML ?

HTML signifie **Hyper Text Markup Language**.

[Dictionary.com](https://www.dictionary.com/browse/markup) définit un Markup comme :

> *un ensemble d'instructions détaillées, généralement écrites sur un manuscrit à composer, concernant le style de police, la composition des pages, et ainsi de suite.*

Vous pouvez donc considérer HTML comme le langage utilisé pour créer des instructions détaillées concernant le style, la police, le format, la structure et la composition d'une page web avant qu'elle ne soit imprimée (affichée pour vous).

Mais dans le contexte du développement web, nous pouvons remplacer le terme « imprimé » par « rendu » comme terme plus précis.

HTML vous aide à structurer votre page en éléments tels que des paragraphes, des sections, des titres, des barres de navigation, et ainsi de suite.

Pour illustrer à quoi ressemble une page, créons un document HTML de base :

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="./styles.css">
  <title>Document</title>
</head>
<body>
  <h1>Ceci est un titre de premier niveau en HTML. Avec CSS, je vais le transformer en couleur rouge</h1>
  <h2>Ceci est un titre de deuxième niveau en HTML. Avec CSS, je vais le transformer en couleur bleue</h2>
  <h3>Ceci est un titre de troisième niveau en HTML. Avec CSS, je vais le transformer en couleur verte</h3>
  <p>Ceci est un <em>paragraphe</em> Comme vous pouvez le voir, j'ai placé une emphase sur le mot "paragraphe". Maintenant, je vais aussi
    changer la couleur de fond du mot "paragraphe" en noir, et sa couleur de texte en vert, tout cela avec juste CSS.</p>
  <p>L'essence principale de ce tutoriel est de :</p>
    <ul>
       <li>Vous montrer comment formater un document web avec HTML</li>
       <li>Vous montrer comment concevoir une page web avec CSS</li>
       <li>Vous montrer comment programmer un document web avec JavaScript</li>
    </ul>

  <p>Ensuite, je vais additionner les deux nombres suivants et afficher le résultat, tout cela avec JavaScript<p/>
    <p>Premier nombre :<span id= "firstNum">2</span> <br></p>
    <p>Deuxième nombre : <span id= "secondNum">7</span> </p>
    <p>Par conséquent, la somme de ces deux nombres est : <span id= "answer">(emplacement pour la réponse)</span></p>
    <input type="button" id="sumButton" value="Cliquez pour additionner !">
</body>
</html>
```

Voici comment vous pouvez formater et structurer un document avec juste HTML. Comme vous pouvez le voir, ce balisage contient certains éléments web tels que :

* Titre de niveau 1 `h1`
    
* Titre de niveau 2 `h2`
    
* Titre de niveau 3 `h3`
    
* Un paragraphe `p`
    
* Une liste non ordonnée avec des puces `ul` `li`
    
* Un bouton d'entrée `input`
    
* Et tout le corps de la page `body`
    

Voici à quoi ce balisage ci-dessus se rend sur un navigateur web :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/HTML.png align="left")

*localhost:3000/index.html*

Vous pouvez également ajouter des attributs à ces éléments que vous pouvez utiliser pour identifier les éléments et y accéder depuis d'autres endroits du site.

Dans notre exemple, nous avons défini les attributs `id` pour les trois éléments `span`. Cela nous aidera à y accéder depuis notre JavaScript comme vous le verrez plus tard.

Pensez à cet attribut de la même manière que votre nom d'utilisateur sur les réseaux sociaux. Avec ce nom, les autres peuvent vous trouver sur les réseaux sociaux. Et quelqu'un peut également vous mentionner avec ce nom (vous pouvez être tagué dans une publication, et ainsi de suite).

Cette page est très basique et peu attrayante, cependant. Si vous construisez autre chose qu'une démo, vous devrez ajouter un style de base pour la rendre plus présentable. Et nous pouvons faire exactement cela avec CSS.

Vous voulez en savoir plus sur HTML ? Vous pouvez [commencer avec la certification Responsive Web Design de freeCodeCamp](https://www.freecodecamp.org/learn/responsive-web-design/) et ce [tout nouveau cours complet sur HTML de Beau Carnes](https://www.freecodecamp.org/news/html-crash-course/).

## Qu'est-ce que CSS ?

Alors que HTML est un **langage de balisage** utilisé pour formater/structurer une page web, CSS est un **langage de design** que vous utilisez pour rendre votre page web belle et présentable.

CSS signifie **Cascading Style Sheets**, et vous l'utilisez pour améliorer l'apparence d'une page web. En ajoutant des styles CSS réfléchis, vous rendez votre page plus attrayante et agréable pour l'utilisateur final à voir et à utiliser.

Imaginez si les êtres humains étaient juste faits pour avoir des squelettes et des os nus – à quoi cela ressemblerait-il ? Pas très beau si vous me demandez. Donc CSS est comme notre peau, nos cheveux et notre apparence physique générale.

Vous pouvez également utiliser CSS pour disposer des éléments en les positionnant dans des zones spécifiées de votre page.

Pour accéder à ces éléments, vous devez les "sélectionner". Vous pouvez sélectionner un ou plusieurs éléments web et spécifier comment vous voulez qu'ils apparaissent ou soient positionnés.

Les règles qui régissent ce processus sont appelées [sélecteurs CSS](https://www.freecodecamp.org/news/use-css-selectors-to-style-webpage/)**.**

Avec CSS, vous pouvez définir la couleur et l'arrière-plan de vos éléments, ainsi que la police, les marges, l'espacement, le remplissage et bien plus encore.

Si vous vous souvenez de notre exemple de page HTML, nous avions des éléments qui étaient assez explicites. Par exemple, j'ai mentionné que je changerais la couleur du titre de niveau un `h1` en rouge.

Pour illustrer comment CSS fonctionne, je vais partager le code qui définit la couleur d'arrière-plan des trois niveaux d'en-têtes en rouge, bleu et vert respectivement :

```css
h1 {
  background-color: #ff0000;
}

h2 {
  background-color: #0000FF;
}

h3 {
  background-color: #00FF00;
}

em {
  background-color: #000000;
  color: #ffffff;
}
```

Le style ci-dessus, une fois appliqué, changera l'apparence de notre page web en ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/CSS.png align="left")

Cool, n'est-ce pas ?

Nous accédons à chacun des éléments sur lesquels nous voulons travailler en les "sélectionnant". Le `h1` sélectionne tous les titres de niveau 1 dans la page, le `h2` sélectionne les éléments de niveau 2, et ainsi de suite. Vous pouvez sélectionner n'importe quel élément HTML unique que vous voulez et spécifier comment vous voulez qu'il apparaisse ou soit positionné.

Vous voulez en savoir plus sur CSS ? Vous pouvez consulter la [deuxième partie de la certification Responsive Web Design de freeCodeCamp](https://www.freecodecamp.org/learn/responsive-web-design/) pour commencer.

## Qu'est-ce que JavaScript ?

Maintenant, si HTML est le **langage de balisage** et CSS est le **langage de design**, alors JavaScript est le **langage de programmation**.

Si vous ne savez pas ce qu'est la programmation, pensez à certaines actions que vous entreprenez dans votre vie quotidienne :

Lorsque vous sentez un danger, vous courez. Lorsque vous avez faim, vous mangez. Lorsque vous êtes fatigué, vous dormez. Lorsque vous avez froid, vous cherchez de la chaleur. Lorsque vous traversez une route fréquentée, vous calculez la distance des véhicules par rapport à vous.

Votre cerveau a été programmé pour réagir d'une certaine manière ou faire certaines choses chaque fois que quelque chose se produit. De la même manière, vous pouvez programmer votre page web ou des éléments individuels pour réagir d'une certaine manière et faire quelque chose lorsque quelque chose d'autre (un événement) se produit.

Vous pouvez programmer des actions, des conditions, des calculs, des requêtes réseau, des tâches concurrentes et de nombreux autres types d'instructions.

Vous pouvez accéder à n'importe quel élément via l'[API Document Object Model (DOM)](https://www.freecodecamp.org/news/how-to-manipulate-the-dom-beginners-guide/) et les faire changer comme vous le souhaitez.

Le DOM est une représentation arborescente de la page web qui est chargée dans le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/DOM-.png align="left")

*Chaque élément sur la page web est représenté sur le DOM*

Grâce au DOM, nous pouvons utiliser des méthodes comme `getElementById()` pour accéder aux éléments de notre page web.

JavaScript vous permet de faire en sorte que votre page web **"pense et agisse"**, ce qui est l'essence même de la programmation.

Si vous vous souvenez de notre exemple de page HTML, j'ai mentionné que j'allais additionner les deux nombres affichés sur la page et ensuite afficher le résultat à la place du texte de l'espace réservé. Le calcul s'exécute une fois que le bouton est cliqué.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/CSS-1.png align="left")

*Cliquer sur le bouton "Obtenir la somme" affichera la somme de 2 et 7*

Ce code illustre comment vous pouvez faire des calculs avec JavaScript :

```js
function displaySum() {
  let firstNum = Number(document.getElementById('firstNum').innerHTML)
  let secondNum = Number(document.getElementById('secondNum').innerHTML)

  let total = firstNum + secondNum;
  document.getElementById("answer").innerHTML = ` ${firstNum} + ${secondNum}, égale à ${total}` ;
}

document.getElementById('sumButton').addEventListener("click", displaySum);
```

Vous vous souvenez de ce que je vous ai dit sur les attributs HTML et leurs utilisations ? Ce code montre exactement cela.

La fonction `displaySum` récupère les deux éléments de la page web, les convertit en nombres (avec la méthode Number), les additionne et les passe en tant que valeurs internes à un autre élément.

La raison pour laquelle nous avons pu accéder à ces éléments dans notre JavaScript est que nous avions défini des attributs uniques sur eux, pour nous aider à les identifier.

Donc grâce à ceci :

```html
// l'attribut id a été défini dans les trois

<span id= "firstNum">2</span> <br> 
    ...<span id= "secondNum">7</span> 
    ...... <span id= "answer">(emplacement pour la réponse)</span>
```

Nous avons pu faire ceci :

```js
// getElementById récupérera tous les éléments HTML par un attribut "id" spécifique
...
let firstNum = Number(document.getElementById('firstNum').innerHTML)
  let secondNum = Number(document.getElementById('secondNum').innerHTML)

  let total = firstNum + secondNum;
  document.getElementById("answer").innerHTML = ` ${firstNum} + ${secondNum}, égale à ${total}` ;
```

Enfin, après avoir cliqué sur le bouton, vous verrez la somme des deux nombres sur la page nouvellement mise à jour :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/JAVASCRIPT.png align="left")

*2 plus 7 est égal à 9*

Si vous voulez commencer avec JavaScript, vous pouvez consulter la certification [JavaScript Algorithms and Data Structures](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) de freeCodeCamp. Et vous pouvez utiliser ce [grand cours d'introduction à JS](https://www.freecodecamp.org/news/learn-javascript-full-course/) pour compléter votre apprentissage.

## Comment combiner HTML, CSS et JavaScript

Ensemble, nous utilisons ces trois langages pour formater, concevoir et programmer des pages web.

Et lorsque vous liez ensemble quelques pages web avec des hyperliens, ainsi que tous leurs actifs comme des images, des vidéos, et ainsi de suite qui sont sur l'ordinateur serveur, cela est rendu dans un **site web**.

Ce rendu se fait généralement sur le front-end, où les utilisateurs peuvent voir ce qui est affiché et interagir avec.

D'autre part, les données, en particulier les informations sensibles comme les mots de passe, sont stockées et fournies depuis la partie back-end du site web. C'est la partie d'un site web qui existe uniquement sur l'ordinateur serveur, et qui n'est pas affichée sur le navigateur front-end. Là, l'utilisateur ne peut pas voir ou accéder facilement à ces informations.

## Conclusion

En tant que développeur web, les trois principaux langages que nous utilisons pour construire des sites web sont HTML, CSS et JavaScript.

JavaScript est le langage de programmation, nous utilisons HTML pour structurer le site, et nous utilisons CSS pour concevoir et disposer la page web.

De nos jours, CSS est devenu plus qu'un simple langage de design. Vous pouvez en fait implémenter des animations et des transitions fluides avec juste CSS.

En fait, vous pouvez également faire de la programmation de base avec CSS. Un exemple de cela est lorsque vous utilisez des requêtes média, où vous définissez différentes règles de style pour différents types d'écrans (résolutions).

JavaScript a également évolué au-delà de son utilisation dans le navigateur. Nous l'utilisons maintenant sur le serveur grâce à **Node.js**.

Mais le fait fondamental reste : HTML, CSS et JavaScript sont les principaux langages du Web.

Donc, c'est tout. Les langages du Web expliqués en termes simples. J'espère vraiment que vous avez tiré quelque chose d'utile de cet article.

Pour conclure cet article, j'ai quelque chose à partager. J'ai récemment commencé une **série de défis de codage hebdomadaires** visant à enseigner aux débutants comment programmer en JavaScript. Consultez-la sur [mon blog](https://ubahthebuilder.tech/day-1-who-likes-it).

Merci d'avoir lu et à bientôt.

> **P/S** : Si vous apprenez JavaScript, j'ai créé un eBook qui enseigne 50 sujets en JavaScript avec des notes numériques dessinées à la main. [Découvrez-le ici](https://ubahthebuilder.gumroad.com/l/js-50).