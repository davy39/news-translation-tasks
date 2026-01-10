---
title: Comment j'ai créé un bot pour ajouter des contacts LinkedIn – et j'ai même
  obtenu quelques entretiens grâce à lui
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-26T15:33:06.000Z'
originalURL: https://freecodecamp.org/news/how-i-made-a-linkedin-contact-adding-bot-and-actually-got-a-few-interviews-with-it-37a6f5f85d4d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*TAOB-11BmEzHS-1b
tags:
- name: bots
  slug: bots
- name: career advice
  slug: career-advice
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment j'ai créé un bot pour ajouter des contacts LinkedIn – et j'ai même
  obtenu quelques entretiens grâce à lui
seo_desc: 'By YK Sugi

  On LinkedIn, there’s a section that’s titled, “People you may know.” It’s under
  the My Network tab.


  This is the page that suggests people you might want to connect with.

  You can click these Connect buttons to send connection requests to t...'
---

Par YK Sugi

Sur LinkedIn, il y a une section intitulée « Personnes que vous connaissez peut-être ». Elle se trouve sous l'onglet **Mon Réseau**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*TAOB-11BmEzHS-1b)

C'est la page qui suggère des personnes avec lesquelles vous pourriez vouloir vous connecter.

Vous pouvez cliquer sur ces boutons **Se connecter** pour envoyer des demandes de connexion aux personnes de cette liste.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OlQUSAu7j9W1waNDevacKg.png)

Il y a quelques années, j'ai trouvé cette page et j'ai commencé à ajouter des personnes au hasard. Je cliquais simplement sur le bouton de connexion pour chaque personne que je trouvais sur cette page.

Je me suis dit qu'il pourrait être utile d'avoir beaucoup de connexions sur LinkedIn pour obtenir les types d'emplois que je voulais, par exemple, des stages en ingénierie logicielle.

Mais après un certain temps, cela est devenu un peu fastidieux de continuer à cliquer manuellement sur ces boutons de connexion.

J'ai donc décidé de créer un petit bot pour cliquer sur ces boutons à ma place.

Cet article explique comment j'ai créé ce bot, ce qui s'est passé par la suite et ce que j'en ai appris.

### Comment j'ai créé le bot

#### Les outils que j'ai utilisés

J'ai créé ce bot simple pour ajouter des personnes au hasard sur LinkedIn avec **JavaScript** et [**Greasemonkey**](https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/).

Greasemonkey est une extension Firefox qui vous aide à gérer du code JavaScript personnalisé.

Avec lui, vous pouvez configurer les choses de sorte qu'un certain ensemble de code s'exécute automatiquement lorsque vous ouvrez une certaine URL.

Vous pouvez également stocker des données dans Greasemonkey. J'ai utilisé cette fonctionnalité pour suivre le nombre de personnes que j'ai ajoutées avec ce bot. Ainsi, j'ai pu suivre ce nombre de manière cohérente même lorsque j'ai fermé le navigateur ou actualisé la page.

#### Le code que j'ai utilisé

Malheureusement, je n'ai pas conservé le code que j'ai utilisé pour créer mon bot après l'avoir utilisé.

Donc, dans cet article, je vais faire de mon mieux pour le recréer le plus fidèlement possible.

Initialement, pour créer ce bout de code, j'ai utilisé Google Chrome. Plus tard, je suis passé à Firefox pour utiliser Greasemonkey, dont j'ai parlé plus tôt. J'ai choisi d'utiliser Chrome initialement simplement parce que j'en avais plus l'habitude.

Maintenant, parcourons ensemble comment je recréerais ce code aujourd'hui. Dans cet article, juste pour garder les choses simples, je ne vais vous montrer que la fonctionnalité principale de ce bot - ajouter des personnes. Donc, je vais sauter la partie sur l'utilisation de Greasemonkey pour stocker des données de manière persistante ici.

Veuillez me le faire savoir dans les commentaires si vous souhaitez que je couvre cette partie dans un article séparé.

#### Étape 0 : Les bases de JavaScript

Au cas où vous ne seriez pas trop familier avec JavaScript, passons rapidement en revue quelques bases de JavaScript ici.

Nous allons utiliser Google Chrome ici, mais vous pouvez utiliser n'importe quel navigateur que vous souhaitez.

Tout d'abord, ouvrez n'importe quel site web, disons, Google.com.

Ensuite, vous devrez ouvrir la console JavaScript du navigateur.

Sur Google Chrome, vous pouvez le faire de plusieurs manières différentes.

La manière dont je le fais habituellement est la suivante :

* Cliquez avec le bouton droit n'importe où sur la page.
* Ensuite, cliquez sur **Inspecter** dans le menu qui s'affiche.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RnSqub0Ljw3asxj5hi-UBg.png)

* Lorsque vous cliquez dessus, une fenêtre comme celle-ci devrait s'afficher.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EdFB6fMXV9FLv9x-TQZFRw.png)

* Ensuite, cliquez sur l'onglet **Console** pour afficher la console JavaScript.
* Une fois que vous avez cliqué sur l'onglet **Console**, vous devriez voir la console JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ExR9I9a7O6yfk4-5JB3Dxg.png)

C'est ici que vous pouvez taper n'importe quel code JavaScript pour le tester. Vous pouvez utiliser le code que vous entrez pour interagir avec la page qui est ouverte dans votre navigateur.

Par exemple, essayez de taper le code suivant dans la console et appuyez sur Entrée.

```
selected = document.querySelector('body');
```

Cela sélectionne la balise **body** dans la page qui est ouverte sur le navigateur. Ensuite, il l'assigne à une nouvelle variable appelée **selected**.

Dans Chrome et Firefox, il y a un raccourci pour :

```
selected = document.querySelector('body');
```

Au lieu de cela, vous pouvez simplement écrire :

```
selected = $('body');
```

[Ce code est équivalent à celui ci-dessus.](https://stackoverflow.com/questions/22244823/what-is-the-dollar-sign-in-javascript-if-not-jquery)

Je vais utiliser cette notation raccourcie avec le signe dollar tout au long de cet article pour garder notre code court et simple.

De plus, ne vous inquiétez pas si vous ne connaissez pas encore les bases de HTML et JavaScript. Je vais essayer de mon mieux d'écrire cet article pour qu'il soit facile à comprendre même pour les débutants.

Si vous n'êtes pas intéressé par le code que je vais vous montrer, vous pouvez également sauter aux sections sur ce qui s'est passé et ce que j'ai appris de cette expérience à la fin.

Maintenant, parcourons le code de notre bot, étape par étape.

#### Étape 1 : Trouver l'élément cible

Tout d'abord, vous devrez écrire le bout de code qui trouve les boutons que vous voulez cliquer.

Tout d'abord, connectez-vous à LinkedIn. Ensuite, allez dans l'onglet Mon Réseau. Il se trouve actuellement à [https://www.linkedin.com/mynetwork/](https://www.linkedin.com/mynetwork/) (juillet 2018).

Vous devriez pouvoir trouver la section **Personnes que vous connaissez peut-être** là.

Ensuite, sur Chrome, cliquez avec le bouton droit sur le bouton « se connecter » sur l'une des personnes recommandées. Ensuite, cliquez sur **Inspecter**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QNH8JeKcFlNNcSRDlJ7k3g.png)

Une fois que vous l'avez fait, l'élément sur lequel vous avez cliqué sera mis en surbrillance dans la fenêtre du développeur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1s3975-NyQ4UEE4_RjGmvg.png)

Voici le code HTML qui est mis en surbrillance en bleu ici :

```
<span aria-hidden="true">Connect</span>
```

C'est une balise **span** qui affiche le texte : **Connect**. Ce que nous voulons vraiment cliquer, ce n'est pas celui-ci, mais son élément parent, qui est un bouton.

Vous pouvez le trouver juste au-dessus de l'élément span que nous avons sélectionné.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mFx3ou-b4BjE9iTQz00sCw.png)

Examinons maintenant cet élément bouton :

```
<button data-control-name="invite" class="button-secondary-small" data-ember-action="" data-ember-action-1596="1596" data-is-animating-click="true"> <span aria-hidden="true">Connect</span> <span class="visually-hidden"> Invite Azul Pinochet Barros to connect </span></button>
```

Il y a beaucoup de choses ici, mais voici la partie importante :

```
<button data-control-name="invite" ...> <span aria-hidden="true">Connect</span> ...</button>
```

En gros, il s'agit d'un élément bouton dont l'attribut **data-control-name** est « invite ».

Dans notre script, tout ce que nous devons faire est de sélectionner des éléments comme celui-ci et de cliquer dessus.

Vous pouvez sélectionner ces éléments avec ce morceau de code :

```
selected = $("button[data-control-name=invite]");
```

Cela se lit comme suit : sélectionnez tous les éléments bouton dont le data-control-name est « invite ».

> _NOTE : Il semble que le site web de LinkedIn utilise jQuery. Donc, la notation ci-dessus est en fait un sélecteur jQuery, [pas une fonction d'assistance définie par Chrome](https://stackoverflow.com/questions/22244823/what-is-the-dollar-sign-in-javascript-if-not-jquery). De manière déroutante, leurs comportements sont légèrement différents ?_

En tout cas, une fois que vous exécutez ce code dans votre console Chrome, vous devriez pouvoir voir que les éléments corrects ont été sélectionnés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gkmjHPk7wCgX5BsoXIWb9w.png)
_C'est ainsi que vous pouvez vous assurer que les éléments corrects ont été sélectionnés._

Maintenant, avec ce morceau de code - `selected = $("button[data-control-name=invite]");` - votre navigateur trouve plusieurs éléments bouton et les place dans un tableau. Pour choisir le premier, vous pouvez simplement sélectionner le premier élément de ce tableau comme ceci :

```
toClick = $("button[data-control-name=invite]")[0];
```

Ensuite, vous pouvez cliquer dessus avec ceci :

```
toClick.click();
```

Si cela fonctionne, vous devriez voir une fenêtre de confirmation apparaître.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mGV1IV56IA17NFDx6JfAEA.png)
_Une fenêtre de confirmation qui apparaît lorsque vous cliquez sur l'un des boutons **connect**_

#### Étape 2 : Parcourir plusieurs éléments cibles

Maintenant, l'étape suivante consiste à parcourir plusieurs éléments cibles à cliquer afin que nous puissions ajouter plusieurs personnes.

Après quelques expérimentations, j'ai réalisé qu'il y avait une manière plus simple de sélectionner plusieurs boutons et de les parcourir que celle que j'ai montrée précédemment.

Voici comment je le ferais.

Tout d'abord, utilisez Inspecter l'élément pour analyser un peu plus la structure de cette page. Ensuite, vous devriez pouvoir voir que les **personnes que vous connaissez peut-être** ne sont qu'une liste non ordonnée.

Vous devriez pouvoir trouver du code qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*EgTc1y_-qQXvC_UcJw2UGQ.png)

L'élément parent est un élément `ul` (liste non ordonnée). Ses enfants sont des éléments `li` (élément de liste).

Chaque élément `li` représente chacune des cartes **personnes que vous connaissez peut-être** que vous voyez à l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XnIgeADO5OUKj3YFlQ1ePw.png)

En sélectionnant ces éléments `li` au lieu de sélectionner directement les boutons, il devient en fait plus facile de parcourir plusieurs personnes.

Vous pouvez sélectionner cet élément `ul`, le parent des éléments `li`, comme ceci :

```
ul = $('ul.mn-pymk-list__cards')[0];
```

Cela signifie : sélectionnez l'élément `ul` avec la classe `ul.mn-pymk-list__cards`. Nous devons ajouter `[0]` à la fin car le résultat brut est un tableau contenant un seul élément.

Ensuite, vous pouvez sélectionner le premier élément `li` (la première carte de personne) sous l'élément `ul` comme ceci :

```
firstLi = ul.querySelector('li');
```

Nous n'avons pas besoin d'ajouter `[0]` à la fin de cette instruction car la fonction querySelector() ne retourne qu'un seul élément.

Ensuite, à partir de `firstLi`, vous pouvez sélectionner le bouton que nous devons cliquer comme ceci :

```
buttonToClick = firstLi.querySelector("button[data-control-name=invite]");
```

Après avoir cliqué sur ce bouton avec `buttonToClick.click()`, nous devons supprimer cet élément `li` afin de pouvoir passer au prochain élément `li` (la prochaine carte de personne). Nous pouvons faire cela avec ceci :

```
ul.removeChild(firstLi);
```

En les mettant tous ensemble et en les plaçant dans une boucle while, vous obtiendrez quelque chose comme ceci :

```
ul = $('ul.mn-pymk-list__cards')[0];firstLi = ul.querySelector('li');while(firstLi){ // faire ceci tant que firstLi existe encore.  buttonToClick = firstLi.querySelector("button[data-control-name=invite]");  ul.removeChild(firstLi);  firstLi = ul.querySelector('li');}
```

Ce code devrait fonctionner, mais il présente plusieurs problèmes.

1. Nous ajoutons des personnes _très_ rapidement avec ceci, donc il sera difficile de savoir ce qui se passe lorsque vous exécutez ce code.
2. Nous ne suivons pas le nombre de personnes que nous avons ajoutées.
3. Nous supposons que `buttonToClick` est toujours le bon bouton à cliquer. Parfois, ce bouton a le texte « Invite » au lieu de « Connect ». Nous ne voulons pas cliquer sur trop de ces boutons « Invite ».

#### Étape 3 : Affiner notre code

J'ai corrigé tous les problèmes que j'ai mentionnés ci-dessus et j'ai mis ensemble un morceau de code relativement simple ci-dessous.

Il est également [ici](https://gist.github.com/ykdojo/aea4cf27fec4bbb5a175e11bae39cb2d) sur Gist. Peut-être est-il plus facile à lire là-bas.

```
// cette fonction nous permet d'arrêter notre code pendant |ms| millisecondes.function sleep(ms) {  return new Promise(resolve => setTimeout(resolve, ms));}
```

```
// J'ai mis notre code principal dans cette fonction.async function addPeople() {  ul = $('ul.mn-pymk-list__cards')[0];  firstLi = ul.querySelector('li');  count = 0; // c'est le compte du nombre de personnes que vous avez ajoutées  while(firstLi && count < 100){ // arrêter après avoir ajouté 100 personnes    buttonToClick = firstLi.querySelector("button[data-control-name=invite]");    // assurez-vous que ce bouton contient le texte "Connect"    if (buttonToClick.innerText.includes("Connect")){      buttonToClick.click();      count += 1;      console.log("J'ai ajouté " + count + " personnes jusqu'à présent.");    }    ul.removeChild(firstLi);    await sleep(1000); // arrêter cette fonction pendant 1 seconde ici.    firstLi = ul.querySelector('li');  }}
```

```
addPeople();
```

Si vous examinez ce code attentivement, vous devriez pouvoir remarquer les quelques changements que j'ai apportés :

1. J'ai mis notre code dans une fonction _async_ appelée addPeople(). Dans cette fonction, chaque fois que nous ajoutons quelqu'un, nous faisons une pause d'1 seconde avec la fonction sleep(). Plus d'informations sur ce modèle [ici](https://stackoverflow.com/questions/951021/what-is-the-javascript-version-of-sleep).
2. J'ai ajouté une variable `count` pour suivre le nombre de personnes que nous avons ajoutées.
3. J'ai ajouté cette instruction if : `if (buttonToClick.innerText.includes("Connect"){...}`. De cette façon, nous pouvons nous assurer que le bouton sur lequel nous cliquons contient le mot « Connect » à l'intérieur.

Avec ces changements, lorsque j'exécute ce code, cela ressemble à ceci :

#### Étape 4 : Apporter d'autres améliorations !

En plus de ce que j'ai montré ci-dessus, j'avais quelques fonctionnalités supplémentaires lorsque j'ai effectivement utilisé mon bot pour ajouter un tas de personnes sur LinkedIn.

Tout d'abord, j'ai utilisé Greasemonkey, dont j'ai parlé plus tôt, pour suivre le nombre total de personnes que j'ai ajoutées.

De plus, pour éviter d'être détecté comme un bot par LinkedIn, j'ai ajouté quelques choses :

1. J'ai randomisé l'ordre dans lequel j'ajoutais des personnes.
2. J'ai randomisé la quantité de temps que j'attendais chaque fois que j'ajoutais une nouvelle personne.

Je vais laisser tout cela comme des problèmes d'exercice pour vous à résoudre au cas où vous seriez intéressé à les résoudre ?

### Ce qui s'est passé

Avec mon script, j'ai fini par ajouter 2000+ connexions. Ensuite, si je me souviens bien, environ 400 d'entre elles m'ont ajouté en retour.

En conséquence, je suis passé d'environ 300 connexions à 700+ connexions en une semaine environ !

Ensuite, après un certain temps, j'ai été banni par LinkedIn d'ajouter d'autres personnes. Je ne savais pas que je pouvais être banni ! J'ai eu un peu peur, mais le bannissement a été levé après 2 mois environ.

Plus important encore, j'ai pu obtenir quelques entretiens grâce à ces 400+ nouvelles connexions. L'un des entretiens était avec une entreprise appelée Palantir.

Voici une capture d'écran du message que j'ai reçu d'eux :

![Image](https://cdn-media-1.freecodecamp.org/images/1*u7fIRKAxBAk8rJTFeqyrXw.png)

### Ce que j'ai appris de cette expérience

Je pensais que ce que je faisais était assez idiot à l'époque, mais j'ai fini par apprendre beaucoup de cette expérience.

#### Leçon #1

Tout d'abord, grâce à cette expérience, j'ai réalisé que LinkedIn fonctionne réellement pour obtenir des emplois. J'ai pu obtenir quelques entretiens d'embauche avec mon bot, après tout.

Ensuite, après un certain temps, j'ai également réalisé que l'ajout de milliers de personnes au hasard n'était pas la manière la plus efficace d'utiliser LinkedIn. Avec ce genre d'approche, vous finissez par ajouter beaucoup de personnes que vous n'avez pas besoin d'ajouter.

Donc, après cette expérience, j'ai changé mon approche pour une approche plus ciblée.

Avec ma nouvelle approche, je n'ajoutais que les recruteurs des entreprises où je voulais travailler. Ensuite, je n'envoyais des messages qu'aux personnes qui m'avaient ajouté en retour.

Cela s'est avéré être une stratégie beaucoup plus ciblée et efficace pour utiliser LinkedIn. Avec cette nouvelle stratégie, j'ai pu obtenir quelques entretiens d'embauche supplémentaires avec plusieurs entreprises technologiques, dont Yelp et Xamarin. Cette fois, je n'ai pas eu à ajouter des milliers de nouvelles connexions pour obtenir ce résultat ?

NOTE : Je parle plus de cette stratégie dans [cet article](https://medium.freecodecamp.org/here-are-4-best-ways-to-apply-for-software-engineer-jobs-and-exactly-how-to-use-them-a644a88b2241), au cas où vous seriez curieux à ce sujet.

#### Leçon #2

S'amuser est la meilleure façon d'affiner ses compétences en programmation !

Grâce à ce projet particulier, j'ai pu affiner mes compétences en JavaScript. Ce que j'ai appris inclut :

* Comment définir un intervalle de temps entre les exécutions de fonctions
* Comment sélectionner certains éléments HTML avec JavaScript
* Comment stocker des données localement avec Greasemonkey

J'ai appris ces choses grâce à ce projet, et cela ne ressemblait pas du tout à des études car c'était tellement amusant.

#### Leçon #3

De cette expérience, j'ai appris qu'il est parfois payant de faire quelque chose d'étrange. Donc, n'ayez pas peur d'être un peu espiègle et aventureux si vous en avez l'inclination.

Même après cette petite expérience, j'ai continué à faire des choses étranges pour le plaisir.

Par exemple, lorsque je faisais un stage chez Microsoft, j'ai mené une petite expérience où j'ai « volé » un tas de mots de passe d'employés. Je l'ai fait en envoyant un e-mail de phishing. Cela devait être une énorme loterie avec des prix comme des Xbox et des ordinateurs portables Surface. C'était mon projet de hackathon là-bas.

J'ai également lancé une [chaîne YouTube sur l'éducation en programmation](https://www.youtube.com/csdojo), et j'ai finalement décidé de [travailler dessus à temps plein et de quitter mon emploi à temps plein d'ingénieur logiciel](https://medium.freecodecamp.org/why-i-left-my-100-000-job-at-google-60b5cf4ebefe).

Peut-être que toutes ces choses semblaient un peu étranges aux autres. Mais chaque fois que je suis passé par chacune de ces expériences, j'ai appris quelque chose de nouveau, et je me suis beaucoup amusé en cours de route. Je dirais que la dernière m'a même fait une carrière.

Donc, encore une fois, n'ayez pas peur d'essayer quelque chose d'étrange juste pour le plaisir ! Vous pourriez apprendre quelque chose de précieux en cours de route.

#### D'accord, c'est tout pour cet article.

Cela devait être une sorte d'article amusant, mais j'écris généralement sur des sujets plus sérieux.

Par exemple, j'ai des articles sur [l'écriture de votre CV d'ingénieur logiciel](https://medium.freecodecamp.org/heres-the-resume-i-used-to-get-a-job-at-google-as-a-software-engineer-26516526f29a), [les meilleures façons de postuler pour des emplois d'ingénieur logiciel](https://medium.freecodecamp.org/here-are-4-best-ways-to-apply-for-software-engineer-jobs-and-exactly-how-to-use-them-a644a88b2241), et [comment obtenir un emploi dans une grande entreprise technologique](https://medium.freecodecamp.org/how-to-get-a-software-engineer-job-at-google-and-other-top-tech-companies-efa235a33a6d).

N'hésitez pas à les consulter. Ils sont tous ici sur Medium.

De plus, comme toujours, si vous avez des questions à ce sujet ou sur autre chose, n'hésitez pas à me le faire savoir dans un commentaire ci-dessous ou sur [Instagram](https://www.instagram.com/ykdojo/) ou [Twitter](https://twitter.com/ykdojo) (@ykdojo sur les deux).

Merci d'avoir lu cet article !