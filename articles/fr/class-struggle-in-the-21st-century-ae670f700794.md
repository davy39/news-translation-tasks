---
title: Lutte des classes au 21ème siècle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-12-30T05:55:18.000Z'
originalURL: https://freecodecamp.org/news/class-struggle-in-the-21st-century-ae670f700794
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sb3Lz9kaHSrMrWLosD2AqA.jpeg
tags:
- name: CSS
  slug: css
- name: learning
  slug: learning
- name: 'self-improvement '
  slug: self-improvement
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Lutte des classes au 21ème siècle
seo_desc: 'By Den McHenry

  Not that kind of class struggle. I’m talking CSS classes, which — Whoa! What was
  that?! Wait a minute. Important message incoming.


  You need a second level heading, text in red, in 60 seconds or this bus will explode.
  What do you do, h...'
---

Par Den McHenry

Pas ce genre de lutte des classes. Je parle des classes CSS, qui — Whoa ! Qu'est-ce que c'était ?! Attendez une minute. Message important en approche.

> Vous avez besoin d'un deuxième niveau de titre, texte en rouge, en 60 secondes ou ce bus va exploser. Que faites-vous, petit malin ? QUE FAITES-VOUS ?

Bon, c'est l'heure ! Donc, si vous avez suivi un tutoriel Web ou un framework populaire, je suppose que vous allez créer une classe appelée **.red-text**. Et … c'est fait.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uZcWDt_yGLknCV6215-Ytw.jpeg)
_Que faites-vous ?! Vous écrivez une nouvelle classe qui vous dit exactement ce qu'elle fait ! Crédit : Speed_

Bon, c'était rapide. Pourquoi Keanu fait-il semblant que c'est tant de travail ?

C'est une si bonne idée, aussi, parce que tout le monde qui regarde le HTML sait quel sera le style visuel ! Parce que ce sont deux couches que nous ne voulons définitivement pas séparer. Nous avons une feuille de style pour une autre raison, je pense.

Eh bien, à mesure que le projet grandit et que le site vieillit, les mémos continuent d'arriver que de plus en plus de morceaux de texte doivent être en rouge. Peut-être que tout le monde est convaincu que les utilisateurs ne remarqueront pas les trucs vraiment importants (c'est-à-dire, les trucs qu'ils possèdent) sans cela. Et donc vous jetez cette classe partout comme des guirlandes sur un sapin de Noël nu.

> <p class="red-text">, <span class="red-text">, <div clas_s="red-text">, <li class="red-t_ext">, und so weiter.

Si facile. Si efficace. Mais vous savez quoi, Peter ? Nous allons devoir vous demander de changer tout le texte rouge en texte bleu. Oui … nous refaisons notre image de marque et les recherches marketing disent que les jeunes se sentent vraiment en sécurité avec le bleu, donc … 'k. Merci !

![Image](https://cdn-media-1.freecodecamp.org/images/1*KYyhccFIbUVTHj8TOx8SQw.jpeg)
_Si vous pouviez juste — ajouter un truc de couleur — ce serait super. Aaaand le mettre partout. Oui. Crédit : Office Space_

Pas de problème.

> .red-text {  
>  color: blue;  
> }

Oh. Hmm. Eh bien, changeons _.red-text_ en _.blue-text_. Attendez — tout le texte est bleu maintenant, mais il dit qu'il est rouge. Oh, snap ! Je dois aller dans chaque document du site et changer l'assignation de classe **"red-text"** en **"blue-text"**. Mais je suis malin. Je suis doué en informatique. Je peux faire une recherche et un remplacement rapides et corriger tous … whoa … 9 347 instances de 'red'. Bon, allons-y … et … BOOM !

Maintenant nous parlons. Le texte est bleu partout. Le site me fait sentir en sécurité et à l'aise. Ils avaient raison à propos de cette recherche marketing. Les gens peuvent toujours voir la source et constater que, oui, le texte bleu est bien étiqueté **"blue-text"**. Tout est en ordre dans le monde.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nc_w92cbjBf_fudP-5O3_g.jpeg)
_Pas si vite, Hackerman ! Crédit : Kung Fury_

Mais soudain vous entendez des pas précipités sur le sol, et le patron est de retour.

> Peter, _l'assistante de Stephanie Redner vient d'appeler_ depuis le siège social. Ils veulent savoir pourquoi le site dit "_Stephanie Bluener (pictublue ici) usheblue dans une nouvelle ère._" Ce n'est pas bon, Peter. Ce n'est pas bon du tout.

Exemple idiot ? Peut-être. Mais c'est arrivé. Peut-être pas exactement comme ça, mais c'est arrivé. Mais ce n'est même pas ce scénario qui est vraiment le problème. C'est que lorsque vous nommez vos classes de cette manière, vous — presque — pourriez aussi bien écrire des styles en ligne.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KVXyqwj_RMBaj5uhJfMYAg.jpeg)
_Crédit : [http://www.bonkersworld.net/building-software/](http://www.bonkersworld.net/building-software/" rel="noopener" target="_blank" title=")_

Cela arrive naturellement comme conséquence d'une conception non intentionnelle. Le site a un aspect et une fonction donnée parce qu'il a été bricolé, pièce par pièce. Et le refactoring est difficile à faire dans le monde réel lorsque la culture ne le valorise pas.

Vous manquez de temps. Les personnes qui ont l'argent ne comprennent pas pourquoi c'est important — ou que cela peut être problématique en premier lieu. Et vraiment, lorsque votre enfant fait un trou dans le mur en plaques de plâtre, vous le réparez. Vous ne démolissez pas le mur et ne le reconstruisez pas. C'est aussi une solution super rapide lorsque quelqu'un au-dessus de vous a des notes sur un site existant.

Donc je comprends. Mais c'est un peu devenu la norme. Et ce n'est pas une bonne chose.

Voici un problème connexe : vous utilisez un framework et vous voulez que les boutons aient l'air et agissent comme des boutons. Il ne suffit pas d'ajouter un **<butt**on> : vous devez le charger comme une pomme de terre au four :

> <button class="btn btn-default">

Alors, que pourriez-vous faire différemment ?

Dans le dernier exemple, peut-être que **<butto**n> devrait suffire pour le défaut. Avons-nous vraiment besoin de dire que le bouton fait partie de la classe des boutons, et devrions-nous jamais avoir besoin de déclarer un défaut ?

Dans notre entreprise hypothétique, peut-être qu'il s'avère que lorsque vous regardez de plus près, le **<**h2> n'est rouge que lorsqu'il se trouve dans un div i**n le .**widget class. **May**be <p> n'est rouge que dans ces divs de termes financiers que la comptabilité vous a fait ajouter, celui avec **h that** dumb .notice class (si criard, mais ils ont insisté). Et ainsi de suite.

Eh bien, voici une meilleure façon : laissez votre HTML non encombré, et familiarisez-vous avec vos sélecteurs CSS. Nous n'avons même pas besoin de nous compliquer la vie (pour l'instant). Nous pouvons utiliser un simple sélecteur descendant, que vous connaissez peut-être mieux sous le nom d'espace.

> .widget h2, .notice p {  
>  color: red;  
> }

C'est ce dont je rêvais il y a presque 20 ans lorsque je faisais des sites web pour moi-même et que je m'excitais tant pour l'avenir de CSS. C'est un peu déchirant maintenant de revenir dans le domaine, pour constater que CSS est blâmé pour la prévalence déconcertante d'une mauvaise pratique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fNYstHfVVW08a6a6wqqVQA.jpeg)
_Great Scott, Marty ! L'état de CSS est-il devenu si mauvais dans le futur ? Crédit : Back to the Future_

En encombrant vos éléments HTML avec des classes — surtout des classes trop déclaratives — vous créez des cauchemars de maintenance, produisez un balisage encombré, et défaites un peu le but de séparer la sémantique et le style.

Donc, si vous pouvez, ne montez simplement jamais dans ce bus. Mais si vous le faites, essayez d'atténuer les choses là où vous pouvez. Et en fin de compte, rappelez-vous ce que vous essayez de faire dans chaque document, et ne dupliquez pas vos efforts.