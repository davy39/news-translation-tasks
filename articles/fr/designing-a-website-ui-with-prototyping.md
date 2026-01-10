---
title: Comment concevoir un prototype de site web à partir d'une maquette
subtitle: ''
author: Adrian Twarog
co_authors: []
series: null
date: '2020-09-21T17:19:57.000Z'
originalURL: https://freecodecamp.org/news/designing-a-website-ui-with-prototyping
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/ui-design-from-wireframe.png
tags:
- name: prototyping
  slug: prototyping
- name: Web Design
  slug: web-design
- name: Website design
  slug: website-design
- name: '#wireframe'
  slug: wireframe
seo_title: Comment concevoir un prototype de site web à partir d'une maquette
seo_desc: 'You may have heard the old saying: "Measure twice, cut once." Well that
  is exactly why you should plan out a website before you build it. And that''s where
  prototyping comes in.

  When we design our websites, we progress from wireframing to prototyping ...'
---

Vous avez peut-être entendu le vieux dicton : "Mesurez deux fois, coupez une fois." Eh bien, c'est exactement pourquoi vous devriez planifier un site web avant de le construire. Et c'est là que le prototypage intervient.

Lorsque nous concevons nos sites web, nous passons de la [maquette](https://www.freecodecamp.org/news/what-is-a-wireframe-ux-design-tutorial-website/) au prototypage pour arriver enfin à un design complet.

Je voulais explorer et approfondir ce que signifie réellement le prototypage en vous guidant à travers le processus complet.

%[https://youtu.be/_P3CrgFlXhg]

Notez que j'ai créé un autre cours qui couvre la première étape de la conception d'un site web : la création d'une maquette. Vous pouvez [lire à propos de la maquette et regarder mon cours vidéo de 30 minutes ici](https://www.freecodecamp.org/news/what-is-a-wireframe-ux-design-tutorial-website/).

Dans ce tutoriel, nous allons couvrir :

1. Qu'est-ce qu'un prototype précoce
2. Créer une structure : cadre, lignes, colonnes
3. Ajouter du contenu : en-tête, curseur, à propos
4. Concevoir des sections
5. Conclusion : ce que nous avons appris du processus de prototypage

## Qu'est-ce qu'un prototype précoce ?

Un prototype est normalement la deuxième itération d'un design, car il est construit sur une maquette.

Une maquette implique généralement un simple croquis dessiné via du papier, un stylo ou un outil en ligne. Ensuite, nous construisons le prototype, qui est notre maquettage plus raffiné pour le site web ou l'application.

Jetons un coup d'œil à la maquette précoce que nous avons construite [dans l'article précédent](https://www.freecodecamp.org/news/what-is-a-wireframe-ux-design-tutorial-website/) :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Wireframe.svg)
_La maquette que nous avons créée dans [mon précédent cours sur la maquette](https://www.freecodecamp.org/news/what-is-a-wireframe-ux-design-tutorial-website/)._

Elle comporte un certain nombre de pages, de sections et de zones où du texte et des images seront ajoutés plus tard.

L'objectif, alors, dans le prototype est de construire cela visuellement, mais sans ajouter de couleur ou d'images.

Dans cet exemple, j'utiliserai [Figma](https://www.figma.com/) pour faire le prototype. Vous pouvez [voir le prototype Figma complet ici](https://www.figma.com/file/mh52sQHBF8Bq2pIZhLKVuh/freeCodeCamp-Website-Ui?node-id=0%3A1).

## Comment créer une structure de prototype de site web : cadre, lignes, colonnes

![Image](https://www.freecodecamp.org/news/content/images/2020/09/columns-3.gif)

Lorsque nous avons créé la maquette, nous avons considéré les grilles, mais elles étaient dessinées à la main.

Lors de la création d'un prototype précoce, nous devons les définir correctement afin que l'ensemble du design suive la structure de la grille.

Dans cet exemple, j'utiliserai un design à 12 colonnes avec une largeur régulière de 1140px, qui est traditionnellement utilisée et vue dans les designs Bootstrap. Cela nous donne une marge de 15-30px entre les unités de grille.

Cela sera utile plus tard lorsque nous réduirons les colonnes en lignes pour la réactivité mobile.

Vous pouvez créer votre propre structure de grille dans Figma. Mais soyez conscient que vous (ou quelqu'un d'autre) devrez ensuite coder ces designs.

Lorsque vous concevez quelque chose, assurez-vous de prendre en considération le développeur.

## Comment ajouter du contenu à un prototype de site web : en-tête, curseur, sections

![Image](https://www.freecodecamp.org/news/content/images/2020/09/slider.gif)

Contrairement à la maquette, nous ne représentons plus le texte avec des lignes, et les en-têtes avec des blocs. Au lieu de cela, nous devons remplir le contenu pour une maquette.

Cela ne signifie pas ajouter des couleurs ou des images. Mais cela signifie que nous devons montrer du texte réel.

À ce stade, c'est une excellente idée de s'assurer que l'en-tête et les sections sont montrés avec le contenu réel qu'ils sont censés contenir. Cela permettra une meilleure sélection des couleurs et des images dans les étapes ultérieures du design.

Dans cette partie de l'exemple, j'ai construit le curseur avec du texte héroïque et une description en dessous. Il y a quelques choses à surveiller à cette phase du processus de prototypage :

* Taille et positionnement de la police
* Emplacement et espacement du contenu
* Marges et espacements entre les sections et le contenu

## Comment concevoir des sections du prototype de site web

![Image](https://www.freecodecamp.org/news/content/images/2020/09/about.gif)

Pour le prototypage et la maquette finale, il est important de commencer à superposer vos groupes et sections. Les sections peuvent inclure des éléments comme l'en-tête, la section "à propos de nous" et la section des sponsors.

Vous pouvez créer des groupes dans votre outil d'interface utilisateur (Figma le fait avec Ctrl+G). Étiquetez vos sections et définissez-les avec différentes couleurs de fond. Cela facilitera leur identification et vous permettra de les déplacer facilement.

Trop de fois, on m'a demandé de déplacer certaines parties d'un site web vers le haut et le bas du regroupement. En regroupant tous vos composants en sections, vous vous faciliterez grandement la tâche pendant la phase de prototypage du travail de design.

## Conclusion : ce que nous avons appris du processus de prototypage

![Image](https://www.freecodecamp.org/news/content/images/2020/09/conclusion.gif)

Alors que nous construisons le reste du design, il est important de s'assurer que ce prototype précoce ne devienne pas une maquette complète pour un design de site web.

Il est facile de se laisser emporter. Mais l'objectif de faire un prototype après une maquette est de s'assurer que nous pouvons continuer à planifier le développement du site web.

Il est beaucoup plus facile d'identifier les problèmes et les questions dans les premières phases de planification et de les mettre à jour avant de plonger dans la création du design complet. Un tel prototypage peut ne vous prendre que quelques heures, mais il peut économiser des jours de travail plus tard dans le processus.

Une fois que vous avez prototypé plusieurs pages, vous pouvez passer à la phase de design de la maquette complète. Cela impliquera de déterminer la théorie des couleurs, la typographie et les images qui fonctionnent en conséquence. Nous examinerons cela dans le prochain article de cette série le mois prochain.

## Bonus : ajouter une exécution de prototype interactif

Nous n'avons créé qu'une seule page pour cet exemple. Cela dit, le prototypage vous permet également de créer un exemple émulé du site en fonctionnement.

Cette émulation est très utile pour effectuer des démonstrations, tester comment les clients réagissent à la vue d'un exemple réel d'une maquette précoce, et réviser comment tous vos liens s'enchaînent.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/freeCodeCamp.jpg)

J'espère que vous avez apprécié cet article. Si vous ne savez pas qui je suis, je suis Adrian d'Australie. ? J'ai une petite chaîne sur Twitter et YouTube, alors si vous voulez en savoir plus sur moi ou apprécier mon contenu, passez me voir parfois ?

* **YouTube** : [https://youtube.com/adriantwarog](https://youtube.com/adriantwarog)
* **Twitter** : [https://twitter.com/adrian_twarog](https://twitter.com/adrian_twarog)