---
title: Comment j'ai construit un miroir intelligent, avec un peu d'aide de ma fille
  et de son grand-père
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-21T04:31:11.000Z'
originalURL: https://freecodecamp.org/news/crafting-a-smart-mirror-with-my-dad-and-daughter-c3bdd151fefd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0MC93WQzKqFGisGM2WisVQ.png
tags:
- name: Internet of Things
  slug: internet-of-things
- name: life
  slug: life
- name: Raspberry Pi
  slug: raspberry-pi
- name: smart home
  slug: smart-home
- name: technology
  slug: technology
seo_title: Comment j'ai construit un miroir intelligent, avec un peu d'aide de ma
  fille et de son grand-père
seo_desc: 'By Coding with Cookie

  This month I built a smart mirror with my dad and daughter. This project spanned
  across three generations.

  The idea started a few years ago with the novelty of a smart mirror. But before
  I was going invest the time and money to ...'
---

Par Coding with Cookie

Ce mois-ci, j'ai construit un miroir intelligent avec mon père et ma fille. Ce projet a impliqué trois générations.

L'idée a commencé il y a quelques années avec la nouveauté d'un miroir intelligent. Mais avant d'investir du temps et de l'argent pour en fabriquer un, j'avais besoin d'une raison pratique. Récemment, cette raison s'est présentée.

Dans notre cuisine, nous avons un tableau blanc où nous listons nos plans de dîner pour la semaine, et je voulais le moderniser. J'ai soumis une idée de présentation pour le miroir intelligent à une conférence technologique locale. Ma présentation sur le miroir intelligent a été [sélectionnée](https://seattle.codecamp.us/Session/Details/217). Cela a accéléré mon calendrier.

![Image](https://cdn-media-1.freecodecamp.org/images/DeTO06lHtTL-b0AmprtydowA3tWFIwc4dern)
_Programmation du miroir intelligent avec ma fille_

J'avais besoin d'aide pour la conception du cadre du miroir intelligent

puisque je vis dans le monde numérique en concevant des logiciels qui vivent dans le cloud. Mon père est ingénieur mécanique et vit dans le monde physique, concevant les avions que nous utilisons pour voler à travers les nuages tous les jours. En parlant avec mon père un soir, il a suggéré de créer quelques croquis initiaux du miroir.

![Image](https://cdn-media-1.freecodecamp.org/images/VYfIYuOgsKPTY5nsFkZmxPsY83hYF2SFfNkd)
_Conception initiale du miroir intelligent_

Après quelques autres conversations avec mon père et plusieurs révisions de conception, nous nous sommes arrêtés sur un design de cadre en forme de boîte simple. Mon père en savait plus sur le travail du bois que moi, et il avait quelques suggestions pour moi.

Comme utiliser des côtés de tiroirs de meuble pour les côtés du cadre, car ils venaient déjà avec une rainure pour tenir le verre. Et utiliser des [taquets français](https://en.wikipedia.org/wiki/French_cleat) pour fixer le miroir au mur. Cela permettait également de le retirer facilement pour le transport.

![Image](https://cdn-media-1.freecodecamp.org/images/eq70lB300bPWUI2zzdVaTePyHuCQWh0CaEDa)
_Conception révisée du miroir intelligent_

Ma femme a été d'un grand soutien dans cette entreprise. Elle a aidé en triant des dizaines de téléviseurs à la recherche du bon prix et des bonnes fonctionnalités. La taille devait être suffisamment grande pour notre cuisine, mais pas trop grande pour rendre le transport difficile. Finalement, elle a pu obtenir un téléviseur chez Best Buy qui avait tout ce que je cherchais. Et le meilleur, c'est qu'il était en solde.

La partie la plus visible du miroir intelligent est le miroir réfléchissant. La plupart des miroirs domestiques sont fabriqués en verre. Mais le plus gros inconvénient de l'utilisation du verre est qu'il est fragile et ne se transporte pas bien. J'ai choisi le plastique car il est plus léger, plus transparent et plus durable.

C'est agréable de parler à des experts et je vis à Seattle, qui dispose d'un excellent fournisseur local de [plastique](https://www.tapplastics.com/). Ils ont été excellents et ont pu m'aider à sélectionner le bon plastique. Ils ont suggéré de l'acrylique et nous avons même testé le film miroir que j'avais acquis sur un échantillon qu'ils avaient. Et ce n'était pas le premier miroir intelligent pour lequel ils avaient fourni le plastique, donc je savais que j'étais sur la bonne voie.

Le choix était simple lorsqu'il s'agissait de décider où assembler le cadre. Mon père a un nouvel atelier et tous les outils dont nous avions besoin, et j'ai un garage et une seule boîte à outils. Une fois que j'ai acquis le bois, l'acrylique et le film miroir, je suis allé dans l'atelier de mon père pour assembler le cadre.

Je pensais que cela prendrait 4 à 5 heures. Mais cela a pris environ 15 heures pour assembler le miroir. Cela peut être dû à l'affinement de la conception pendant que nous fabriquions le miroir. Cela peut aussi être dû au fait que je posais beaucoup de questions, comme pourquoi coller cela au lieu de visser cela. Ou cela était dû au fait de passer un bon moment avec mon père. En regardant en arrière, c'était une combinaison de tout cela.

Sur trois jours séparés, nous avons coupé, collé, cloué et vissé le cadre ensemble. Il tiendrait le téléviseur, le miroir acrylique et le Raspberry Pi.

Plusieurs outils électriques ont été utilisés, notamment une scie sur table, une scie à onglet et un pistolet à clous, donc ma fille n'a pas aidé pour cette partie. Mais elle a pu aider à l'assemblage final lorsque le miroir acrylique a été inséré. Elle a même pu utiliser la perceuse pour visser le haut lors de l'assemblage final.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Ma fille utilisant une perceuse pour visser le haut du miroir_

Avec tout le travail du bois terminé, ma fille et moi avons commencé à câbler tout ensemble. Comme le rose est sa couleur préférée, il était évident que le seul choix était d'imprimer en 3D le boîtier du Raspberry Pi en rose.

Nous avons mis le Raspberry Pi dans le boîtier rose et l'avons attaché à l'arrière de la télévision via du Velcro adhésif.

En utilisant du Velcro, le Raspberry Pi peut être déconnecté. Ainsi, je peux montrer la taille de l'ordinateur transformant le miroir en un miroir intelligent.

![Image](https://cdn-media-1.freecodecamp.org/images/Kv-0LGWfO0ueT1o-xHr6C-znSspCJIJMBuX8)
_Boîtier Raspberry Pi rose imprimé en 3D_

Les téléviseurs modernes incluent généralement un port USB, et celui que ma femme a trouvé en avait effectivement un. J'ai testé le port USB sur la télévision et il était capable de fournir suffisamment de puissance au Raspberry Pi. Cela signifiait que le cordon d'alimentation de la télévision était le seul câble que je devais brancher sur la prise murale.

Ensuite, nous avons branché les câbles USB et HDMI à la fois sur le Raspberry Pi et la télévision, et nous étions prêts à partir.

Avec le WiFi intégré, j'ai connecté le miroir intelligent à Internet sans aucun autre fil. Et lorsque le courant est coupé, il fonctionnera toujours comme un miroir traditionnel non intelligent.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)
_Ma fille et moi connectant tous les fils à l'arrière du miroir intelligent_

Quand on a 4 ans, taper sur un clavier et coder, c'est cool. On verra comment elle se sentira quand elle aura 14 ans.

Ma fille a pu aider beaucoup sur la partie logicielle du miroir intelligent. Puisque ses capacités d'orthographe se limitent à son nom, elle a pu le taper et était très excitée quand elle l'a vu sur le miroir intelligent.

Pour faire apparaître son nom, nous avons utilisé du HTML. Pour garder cela simple, une page HTML statique avec un style en ligne via Chrome, en plein écran `F11`, était tout ce que nous avions à faire pour que cela fonctionne. Le fond doit être aussi sombre que possible pour minimiser la lumière traversant le miroir.

Lorsque l'écran est éteint ou complètement noir, il apparaît comme un miroir commun. Le texte et les graphiques doivent être aussi brillants que possible pour apparaître à travers, le transformant en un miroir intelligent. Sur mon miroir, j'ai pu trouver un film avec une transparence de 5 %.

![Image](https://cdn-media-1.freecodecamp.org/images/a-EnHz7xBvtQyA7VmWtqAGQOnGUwSV3DTJNx)
_Installation du miroir acrylique dans le cadre_

En revisitant mon miroir jusqu'à présent, je ferais quelques choses différemment la prochaine fois. Tout d'abord, je prendrais un téléviseur plus fin. Actuellement, le cadre du miroir fait 4,5 pouces de profondeur, ce qui est suffisamment profond pour que l'on remarque, mais pas au point d'être encombrant.

Ensuite, je commanderais de l'acrylique avec le film miroir déjà installé. Mon père et moi avons pu installer le film en 20 minutes, mais cela a résulté en plusieurs petites bulles. Probablement dues à quelques petites particules de poussière piégées entre le film et l'acrylique.

De plus, j'ajouterais une façade plus stylisée. Si vous regardez les coins de mon miroir intelligent, vous verrez toutes les couches de contreplaqué. Cela pourrait être caché avec du bois plus joli pour ressembler davantage à un cadre de tableau.

Enfin, j'ajouterais un petit espace entre la télévision et l'acrylique. Actuellement, l'acrylique aide à supporter la télévision. Cela exerce une pression sur l'acrylique, le faisant plier légèrement. Cela entraîne une légère distorsion du miroir.

Construire le miroir intelligent a été une expérience formidable et si vous avez des questions, n'hésitez pas à [me contacter](https://codingwithcookie.com/contact/).

Le prochain projet sur lequel ma fille et moi travaillons consiste à câbler des capteurs dans la cuisine pour suivre la température dans le réfrigérateur et le congélateur. J'espère la faire participer davantage à ce projet et aux projets futurs, car elle est enthousiaste à l'idée d'aider et de câbler les capteurs sur une plaque d'essai.

J'ai hâte de partager cette histoire avec vous une fois que nous l'aurons terminée.

![Image](https://cdn-media-1.freecodecamp.org/images/8xBLYzrWXyZMltzMYYVKY5C2ARAcu9nHZlZ9)