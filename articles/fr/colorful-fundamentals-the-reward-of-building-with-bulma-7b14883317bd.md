---
title: Mon voyage dans le framework CSS Bulma
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-25T20:31:44.000Z'
originalURL: https://freecodecamp.org/news/colorful-fundamentals-the-reward-of-building-with-bulma-7b14883317bd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_NUWv4R8wXKkd2SO9OYzyw.jpeg
tags:
- name: Bulma
  slug: bulma
- name: CSS
  slug: css
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Mon voyage dans le framework CSS Bulma
seo_desc: 'By Henrik Ståhl

  I recently decided to try out a CSS framework. As a journalist, I’ve been taught
  to work from the ground up, do things thoroughly, and never “borrow” stuff from
  others (in the news industry, that’s considered plagiarism). Therefore I’...'
---

Par Henrik Ståhl

J'ai récemment décidé d'essayer un framework CSS. En tant que journaliste, on m'a appris à travailler à partir de zéro, à faire les choses de manière approfondie et à ne jamais "emprunter" des choses aux autres (dans l'industrie de l'information, cela est considéré comme du plagiat). Par conséquent, j'ai été plutôt réticent à utiliser des frameworks depuis le début de mon [parcours en codage](https://news.maythecode.com). Simplement parce que je sentais que ce serait comme tricher, si vous voyez ce que je veux dire.

Je n'aurais pas pu avoir plus tort.

D'abord, après avoir expérimenté un peu par moi-même avec une vidéo en arrière-plan plein écran — un défi très amusant et intéressant, soit dit en passant — je voulais plus de contenu réel à travailler avant de plonger tête la première dans [Bulma](http://bulma.io), un framework moderne basé sur Flexbox créé par [Jeremy Thomas](https://www.freecodecamp.org/news/colorful-fundamentals-the-reward-of-building-with-bulma-7b14883317bd/undefined).

C'est pourquoi j'ai finalement décidé de _ne pas_ expérimenter avec Bulma sur mon site [May The Code](http://maythecode.com).

Au lieu de cela, j'ai choisi de redessiner un site web que j'avais créé pour mon groupe de rock suédois maintenant défunt [Evangeliet](http://play.spotify.com/album/2bXUzHUmEZpXpTc6mNbQgH) (nous sommes en pause depuis 2014).

Dans cette histoire, je vais vous dire pourquoi je me suis senti intimidé par PHP, comment j'ai échoué encore et encore malgré la lecture répétée de la documentation, et ce que j'ai finalement appris en gâchant tout.

### La nouvelle page d'accueil

J'avais déjà implémenté une première itération d'une page d'accueil avec une vidéo en plein écran en arrière-plan et une barre de navigation simple, donc la première chose que j'ai faite a été de remplacer ma barre de navigation quelque peu inesthétique par une navigation Bulma.

Ajouter la barre de navigation n'a pas été particulièrement difficile. Du moins, pas après avoir lu la [documentation](http://bulma.io/documentation/components/navbar/) plusieurs fois. Mais la vidéo en plein écran en arrière-plan était un peu plus délicate. Après quelques expérimentations infructueuses avec différents éléments de mise en page Bulma, tels que `.hero` et `.container is-fluid`, j'ai créé un CSS personnalisé pour gérer l'arrière-plan plein écran :

![Image](https://cdn-media-1.freecodecamp.org/images/-ZGqYF8cCpi-JMaFsHY3GaCA3D6pzEaug8OH)
_Mon CSS personnalisé._

Cela a fonctionné ! Au moins sur desktop. Dès que j'ai pris mon téléphone pour vérifier sur un viewport plus petit, j'ai rapidement découvert que j'avais été brutalement puni par mon approche obsolète "desktop-first" :

![Image](https://cdn-media-1.freecodecamp.org/images/MJ-29W0oP39KFc6FkIE2jGBWpw-DcgseAHkG)
_L'image GIF que j'ai créée n'a pas remplacé la vidéo sur mobile._

Et comme vous pouvez le voir, j'ai accidentellement placé la barre de navigation et la vidéo d'arrière-plan plein écran dans des `sections` séparées dans le document HTML, ce qui a fait que la première était détachée de la seconde.

J'étais néanmoins motivé à avancer, alors je l'ai laissé tel quel pour le moment.

### La page audio

Ensuite, je voulais créer une page audio soignée. La page elle-même est assez simple : elle est [composée de](https://medium.com/backchannel/meet-the-ultimate-wikignome-10508842caad) trois "blocs" d'albums avec des listes Spotify. D'abord, j'ai créé un `conteneur fluide` avec une image :

```
<div class="container is-fluid">  <figure class="image">    <img src="/smoke.jpeg" alt="Evangeliet">  </figure></div>
```

Ensuite, j'ai parcouru la documentation de Bulma [documentation](https://bulma.io/documentation/form/general/) dans l'espoir de trouver un composant qui conviendrait à mon besoin. J'ai finalement opté pour une `carte` :

```
<div class="card">          <div class="card-image">            <figure class="image is-square">              <img src="/Konturen.jpeg" alt="Konturen av en dröm">            </figure>          </div>          <div class="card-content">            <div class="media">              <div class="media-left">              </div>              <div class="media-content">                <p class="title is-4">Konturen av en dröm</p>                <p class="subtitle is-6">2013</p>              </div>            </div>
```

J'ai ensuite inséré une classe `.card-content` à l'intérieur du composant `card` :

```
<div class="content">              <iframe src="https://open.spotify.com/embed?uri=spotify:album:2bXUzHUmEZpXpTc6mNbQgH&theme=white" width="100%" height="380" frameborder="0" allowtransparency="true"></iframe>              <br>              <small><strong>UPC:</strong> 0885014300335</small>              <small><strong>Numéro de catalogue :</strong> RU 27130</small>              <br>              <small><strong>Date de sortie :</strong> 18 déc. 2013</small>            </div>          </div>        </div>
```

Pour obtenir un beau [lecteur Spotify](https://developer.spotify.com/technologies/widgets/spotify-play-button/), j'ai récupéré un code d'intégration dans la documentation [Spotify Developer](https://developer.spotify.com). (J'ai changé la largeur de `300px` à `100%`, et le thème de noir par défaut à blanc, ce qui convient mieux à mon design.)

J'ai créé trois cartes, ajouté quelques informations sur les albums, et les ai regroupées avec des éléments `column`. Le résultat était satisfaisant :

![Image](https://cdn-media-1.freecodecamp.org/images/IHpzh37izjj1QmGVLbZ5qpEIUGylMYR9a1Fy)

### La grille d'images

Après cela, je voulais créer une sorte de page contenant des photos du groupe. Je voulais quelque chose de plus stimulant qu'une page standard de "biographies des membres du groupe", qui n'aurait pas été très différente de la page audio.

J'ai parcouru la [documentation](http://bulma.io/documentation/grid/tiles/) une fois de plus et j'ai décidé de faire quelque chose avec l'élément `tiles`. Cet élément est

> "un élément **tile** unique pour construire des grilles 2D de type Metro, Pinterest, ou autre."

J'ai lu et contemplé la documentation encore et encore, et j'ai atteint une conclusion : puisque je me considère encore comme un débutant en balisage, j'avais besoin de faire quelques expérimentations pratiques pour comprendre les tiles de Bulma. Parce que lire... eh bien, cela ne m'a pas mené très loin.

Alors, j'ai essentiellement copié-collé l'un des exemples de la documentation et j'ai modifié le contenu. J'ai retourné des choses, brisant effectivement _tout_. Apprendre en gâchant tout, n'est-ce pas ? :)

Après avoir joué avec les différentes classes, j'ai opté pour une structure de grille à 3 colonnes, composée de divers éléments de tile. Voici un exemple du balisage :

```
<div class="tile is-ancestor">        <div class="tile is-parent">          <article class="tile is-child box">            <figure>              <img src="/bilder/molotov.jpg">              <figcaption>                Henrik joue des riffs doux dans les <strong>Molotov Studios</strong> en 2010. L'enregistrement a été produit par Martin Karlsson.              </figcaption>            </figure>          </article>        </div>        <div class="tile is-parent">          <article class="tile is-child box">            <p class="title">Stadsmissionen</p>            <p class="subtitle">2009</p>            <figure>              <img src="/bilder/duo.jpg">              <figcaption>                À cette époque, <strong>Evangeliet</strong> était encore un duo.                <br>                PHOTO : Noelia Ivars Rico              </figcaption>            </figure>          </article>        </div>        <div class="tile is-parent">          <article class="tile is-child box">            <figure>              <img src="/bilder/bandbild2.jpg">              <figcaption>                Cristóbal, David, Henrik R et Henrik S dans la salle de répétition à Fruängen, janvier 2011.              </figcaption>            </figure>          </article>        </div>      </div>
```

L'exemple ci-dessus est celui des **trois images du haut** sur la page web. La structure des `tile boxes` sur la page est plus ou moins la même que dans la documentation, sauf que j'ai ajouté des images dans toutes les cases sauf une. De plus, j'ai inséré des éléments `column` et ajouté trois images dans l'une des cases.

Ce qui a nécessité un peu de patience, étant donné que :

1. Je suis encore facilement étourdi par toutes les balises et les balises de fermeture lorsque je nest les éléments, et
2. Je n'étais pas au courant de la fonctionnalité visuelle dans [Atom](http://atom.io) qui met en évidence les balises HTML d'ouverture et de fermeture. ??

J'aurais pu opter pour l'une des différentes structures que j'ai testées pendant la phase expérimentale, mais j'ai considéré que la mise en page fournie dans la documentation Bulma était la mieux adaptée. Pourquoi réparer quelque chose qui n'est pas cassé ?

Et honnêtement, j'aime le fait que les utilisateurs mobiles voient quelques images _avant_ d'arriver au bloc de texte. C'est pourquoi je suis revenu à la structure actuelle après avoir initialement reflété la 2ème colonne et placé ses cinq cases en haut de la page, positionnant effectivement la case verticale haute dans le coin supérieur gauche sur desktop.

![Image](https://cdn-media-1.freecodecamp.org/images/zvlvyo8qzGPf8TSVOkz021Pgw6jet7snxNZq)

### La page de contact

Enfin, je voulais une page de contact. Avec un formulaire de contact et tout.

Encore une fois, la [documentation](http://bulma.io/documentation/elements/form/) a fourni tout ce dont j'avais besoin en termes de balisage. Un jeu d'enfant. Heureusement, j'avais déjà essayé d'apprendre un tout petit peu de PHP dans le seul but de créer un formulaire en ligne (pour un autre site web cependant).

Et j'ai échoué. Dur.

Je ne sais pas pourquoi les autres semblent détester PHP, je suppose que c'est pour diverses raisons. Mais je sais que personnellement, je n'aime pas PHP parce que je me suis senti intimidé par lui.

J'avais l'impression d'avoir essayé _tout_. J'ai lu une série d'articles de blog et j'ai travaillé sur l'ensemble du tutoriel [W3Schools](https://www.w3schools.com/pHp/default.asp). Mais je n'ai toujours pas saisi une fraction de PHP.

En tout cas, pendant mon court passage en tant que maraudeur PHP, je suis tombé sur [Formspree](https://github.com/formspree/formspree), un service de formulaire en ligne créé par [Rohit Datta](https://www.freecodecamp.org/news/colorful-fundamentals-the-reward-of-building-with-bulma-7b14883317bd/undefined).

Comme j'avais déjà utilisé Formspree sur le site [May The Code](http://maythecode.com) avec de grands résultats, je savais que cela fonctionnerait également pour le site web de mon groupe.

J'ai ajouté les classes `field` et `label` nécessaires, ainsi que la classe requise `form action="https://formspree.io/xx@xx.se" method="POST"` — et c'était tout !

Après avoir soumis le formulaire et confirmé mon email, tout a fonctionné comme un charme.

![Image](https://cdn-media-1.freecodecamp.org/images/NcU1VqEQT9kL4auEY4hm9y9q90nvnlDNiPr7)

J'ai fixé la taille du formulaire sur desktop avec quelques lignes de CSS dans ma feuille de style personnalisée, mais pas avant bien plus tard. Le formulaire était opérationnel et j'étais heureux.

#### Et le menu hamburger ?

Maintenant, il ne me restait qu'un seul défi : comment faire en sorte que le menu hamburger sur mobile fonctionne réellement ? ?

La documentation Bulma ne fournissait que le balisage. La fonctionnalité elle-même était à moi de corriger.

Depuis, Jeremy a mis à jour la documentation et remplacé l'ancien composant `nav` par le nouveau composant `navbar`. Voici un exemple de l'ancien :

```
<!-- Ce menu hamburger "nav-toggle" n'est visible que sur mobile -->  <!-- Vous avez besoin de JavaScript pour basculer la classe "is-active" sur "nav-menu" -->  <span class="nav-toggle">    <span></span>    <span></span>    <span></span>  </span>  <!-- Ce "nav-menu" est caché sur mobile -->  <!-- Ajoutez le modificateur "is-active" pour l'afficher sur mobile -->  <div class="nav-right nav-menu">    <a class="nav-item">      Accueil    </a>    <a class="nav-item">      Documentation    </a>    <a class="nav-item">      Blog    </a>
```

J'ai fait beaucoup de progrès en quelques mois, mais je ne suis pas encore assez à l'aise avec HTML et CSS pour faire le saut vers la programmation réelle, alors je voulais vraiment que cela fonctionne sans plonger dans le vaste océan de JavaScript.

Je n'avais aucune idée de comment faire.

C'est pourquoi j'ai opté pour une barre de menu horizontale jusqu'aux plus petits viewports, après ce qui m'a semblé être des heures d'investigation. Tout ce que je devais faire était d'ajouter le modificateur `is-mobile` à la classe `nav-item` :

```
<nav class="nav has-shadow">    <div class="container">      <div class="nav-left">        <a class="nav-item is-tab is-mobile" href="/">Accueil</a>        <a class="nav-item is-tab is-mobile" href="/musik">Musique</a>        <a class="nav-item is-tab is-mobile" href="/bandet">Groupe</a>        <a class="nav-item is-tab is-mobile is-active" href="/kontakt">Contact</a>      </div>  </nav>
```

J'ai pu faire cela parce que mon menu était composé de seulement quatre éléments : page d'accueil, page audio, page du groupe et page de contact. Grâce à cela, tout était visible — et accessible — même dans les plus petits viewports.

Une semaine ou deux plus tard, je suis tombé sur [ce super fil de discussion](https://github.com/jgthms/bulma/issues/238) sur GitHub. L'utilisateur [rudedogg](https://github.com/rudedogg) avait exactement le même problème que moi. De nombreuses solutions différentes sont proposées dans le fil, telles que

> Ouais, vous avez simplement besoin d'un événement JS pour gérer le clic et "ajouter" ou "supprimer" la classe 'is-active' sur '#nav-menu'.

et

> Extrait React (sans jQuery) sur un élément avec `className="nav-toggle" onClick={() => { let toggle = document.querySelector(".nav-toggle"); let menu = document.querySelector(".nav-menu"); toggle.classList.toggle("is-active"); menu.classList.toggle("is-active");` }}

Rien ne semblait répondre complètement à mon besoin. Jusqu'à ce que je fasse défiler vers le bas et que je trouve ce commentaire incroyablement humble, court et brillant de [shaneturner](https://github.com/shaneturner) :

> Un peu plus succinct sur l'élément de navigation lui-même : `<span class="nav-toggle" onclick="document.querySelector('.nav-menu').classList.toggle('is-active')`;">

Je ne suis pas en position de déterminer si c'est la meilleure solution, ni si elle est réellement meilleure que toute autre suggestion dans le fil GitHub. Mais je l'ai essayée et cela a fonctionné immédiatement, dès la sortie de la boîte.

![Image](https://cdn-media-1.freecodecamp.org/images/pkkqVwjpP-7RLOt8QqA6rEDJDvL4s7U62CZR)
_Photo par [Unsplash](https://unsplash.com/@mkwlsn?utm_medium=referral&utm_campaign=photographer-credit&utm_content=creditBadge" rel="noopener" target="_blank" title="">Mike Wilson</a> sur <a href="https://unsplash.com/photos/vAqmcvSMWMU" rel="noopener" target="_blank" title=")._

### Itérations

J'avais terminé. Mission accomplie.

Cela faisait tellement de bien ! Non seulement j'avais été capable de construire un site web entier en utilisant Bulma — j'avais aussi appris beaucoup de choses sur HTML et CSS en parcourant la documentation et en expérimentant avec les différents éléments.

Ce qui avait d'abord semblé être une montagne à gravir s'est transformé en une colline de taille moyenne, et me voilà debout au sommet.

Je n'étais pas entièrement satisfait cependant. Maintenant, je savais comment utiliser Bulma pour construire un site web, mais le site web que j'avais construit était loin d'être parfait. Ensuite, je voulais gravir la colline suivante, celle plus haute, et me rapprocher un peu plus de la perfection. En d'autres termes : utiliser Bulma pour construire un site web dont je suis réellement fier.

Et je l'ai fait.

Mais c'est une autre histoire.

_Henrik Ståhl est un journaliste avec plus de 15 ans d'expérience, récemment devenu Product Owner chez Bonnier News, travaillant sur le développement numérique de [Dagens industri](http://beta.di.se) et [Dagens Nyheter](http://dn.se). Dans son temps libre, il essaie d'apprendre la programmation._