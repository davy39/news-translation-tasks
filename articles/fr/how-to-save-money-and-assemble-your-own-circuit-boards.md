---
title: Comment économiser de l'argent et assembler vos propres circuits imprimés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-03T20:33:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-save-money-and-assemble-your-own-circuit-boards
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Assemble-Circuit-Board-3-2.png
tags:
- name: Electronics
  slug: electronics
seo_title: Comment économiser de l'argent et assembler vos propres circuits imprimés
seo_desc: "By Jared Wolff\nSelf assembling circuit boards is the cheapest way to get\
  \ components on circuit boards.\nPeriod.\nDon’t believe me? Believe these screenshots:\
  \  \n\n\n\nSelf assembled: $143.84 + Tax & Shipping\n\nProfessionally assembled:\
  \ $362.83 + Tax & Shipp..."
---

Par Jared Wolff

L'auto-assemblage des circuits imprimés est **la** méthode la plus économique pour obtenir des composants sur des circuits imprimés.

Point final.

Vous ne me croyez pas ? Croyez ces captures d'écran :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-02-09_at_5.25.41_PM_copy-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-02-09_at_5.08.49_PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-02-09_at_5.09.57_PM.png)

Auto-assemblé : **143,84 $ + Taxes et Livraison**

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screen_Shot_2019-02-09_at_5.37.30_PM.png)

Assemblé professionnellement : **362,83 $ + Taxes et Livraison**

Cela fait environ 50 $ par carte contre 120 $ par carte. C'est **énorme**. De plus, 18 jours, c'est **long** à attendre pour trois circuits imprimés.

Dans cet article, je vais parler des meilleurs conseils et astuces que j'ai appris au fil des ans sur la façon d'assembler mes propres circuits imprimés. Je n'ai aucun doute qu'ils seront immédiatement utiles pour vos projets actuels et futurs.

Alors, commençons par parler de la CAO.

## Exporter votre CAO

Le standard de l'industrie est le fichier Gerber. Les fichiers Gerber sont la traduction de toutes les belles formes, traces, pastilles, sérigraphies et perçages en quelque chose d'utile pour un fabricant de cartes. Il existe d'autres formats comme ODB++. Si vous avez déjà regardé à l'intérieur d'un fichier ODB++, ce n'est qu'un ensemble de Gerbers regroupés. 🤷‍♂️

Si vous êtes intéressé à en savoir plus sur les Gerbers et mon processus de vérification, [allez regarder cette vidéo](https://www.circuitdojo.org/fundamentals/#reviewing-your-gerbers) puis revenez. Pas de souci, je serai là.

Heureusement, la plupart des fournisseurs accepteront les fichiers CAO bruts, surtout si vous utilisez quelque chose comme Eagle CAD. Par exemple, lorsque je vais acheter un circuit imprimé sur [OSH Park](https://www.oshpark.com), je télécharge mon fichier `.brd`. Dans la plupart des cas, il est rapidement traité et renvoie un prix.

Ces mêmes fichiers peuvent également être utilisés pour l'achat d'un **pochoir à pâte à souder**. Les pochoirs à pâte à souder vous permettent d'appliquer la pâte à souder uniquement sur les ouvertures du masque de soudure de votre circuit imprimé. Oui, vous pouvez assembler un circuit imprimé sans utiliser de pâte à souder ou de pochoir à souder, mais je le recommande vivement, surtout si vous vous souciez de l'esthétique de votre carte.

Une note sur l'esthétique : je recommande pour les premiers prototypes d'inclure des désignateurs de référence visibles **lorsque la carte est entièrement assemblée**. Cela facilite grandement le placement manuel des composants. Voyez ce dont je parle ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/DSC01271.jpeg)

Voyez tous les désignateurs de référence en blanc ? Ils seront très utiles très bientôt...

Pour les pochoirs, mon choix est [OSH Stencils](https://www.oshstencils.com). Leur coût est raisonnable et cela fait gagner beaucoup de temps lorsque l'assemblage est en cours. De plus, comme vous l'avez peut-être deviné, les lignes d'assemblage de circuits imprimés utilisent de grands pochoirs métalliques pour accomplir la même chose.

Enfin, vous voulez exporter votre liste de matériaux. J'utilise le script `bom.ulp` qui vient avec Eagle. J'exporte toujours par _valeur_ afin que toutes les pièces des mêmes attributs soient regroupées. Cela donne une liste de matériaux propre et compacte qui peut être facilement importée dans quelque chose comme Octopart. J'utilise souvent Octopart pour rechercher les prix. Si c'est une liste de matériaux particulièrement grande, je peux diviser les commandes entre, par exemple, Mouser et Digikey. Parfois même [Arrow](https://www.arrow.com) a des pièces pour quelques dollars de moins que les deux autres.

Lors de la commande, tous les fournisseurs vous permettent d'importer un fichier `.xlsx` ou `.csv`. Lors de l'importation, vous avez parfois le choix de mettre un numéro de pièce client (ou similaire). Vous pouvez utiliser cela pour stocker le désignateur de référence. Cela sera imprimé sur l'étiquette qu'ils collent sur le sac.

Tant que vos pièces ne sont pas trop lourdes, vous pouvez généralement utiliser l'option de courrier de première classe que propose Digikey. Il semble qu'ils aient récemment augmenté leurs prix de livraison (c'était 3,5 $, maintenant c'est ~4,5 $ pour le Connecticut). Les pièces arrivent généralement dans les 2-3 jours ouvrables. Ce qui n'est pas si mal ! 😊

Astuce pro : Une fois que vous avez les pièces, vérifiez votre inventaire. J'ai fait l'erreur de ne pas commander assez de pièces pour plusieurs assemblages. Si vous vous retrouvez à court, faites simplement une autre commande. Si vous ne le faites pas, vous pourriez être désagréablement surpris lorsque le jour de l'assemblage arrivera et que vos composants seront en manque.

## Placer les composants sur votre carte

Préparez votre espace d'assemblage. Utilisez les découpes en plastique et placez-les autour de votre circuit imprimé. Ensuite, fixez-les avec du ruban adhésif comme un cadre permanent sur votre bureau. Vous pouvez les fabriquer vous-même en utilisant un service comme Ponoko ou simplement acheter ceux que propose OSH Stencils.

Ensuite, fixez le pochoir par-dessus en alignant tous les trous. Cela prend un peu de temps et de finesse. Assurez-vous de le fixer pour qu'il ne bouge pas.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/DSC00558.jpeg)

Placez le pochoir à plat sur la carte. Ensuite, prenez votre seringue à souder et déposez un peu de soudure sur le dessus du pochoir. Utilisez une vieille carte de crédit ou la carte en plastique qui accompagne un pochoir pour étaler la soudure. Essayez d'étaler en vous éloignant de l'endroit où le pochoir est fixé à votre surface de travail. Sinon, si vous déplacez le pochoir, vous ferez un désordre et devrez recommencer.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/DSC00561.jpeg)

Une fois la pâte déposée, comme sur l'image ci-dessus, placez la carte sur une surface plane. Il n'y a rien pour maintenir les composants sur la carte, il est donc préférable de la placer sur une carte de circuit plus grande et non peuplée. Ainsi, vous avez une base mobile et il y a moins de risques de détruire votre travail. De plus, cela protège la surface en dessous une fois que vous passez à l'étape suivante.

N'oubliez pas, utilisez les désignateurs de référence sur la carte de circuit et comparez-les avec le désignateur de référence sur l'emballage de vos composants. Tant que vous avez exporté votre liste de matériaux correctement, il n'y a aucune raison de revenir en arrière et de vérifier les numéros de pièces. Voir un exemple d'emballage avec le désignateur de référence ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/DSC01272.jpeg)

Enfin, faites cuire votre carte de circuit. J'utilise généralement mon pistolet à air chaud à environ 380°C et je fais lentement le tour de toute la carte en soudant toutes les pièces. Mon débit d'air est réglé très bas lorsque je fais cela, sinon les pièces s'envolent. Cela s'applique à toute configuration de pistolet à air chaud.

Cela peut également être accompli en utilisant une plaque chauffante ou un vieux four à griller. N'oubliez pas, vous ne voulez pas utiliser le même four que celui que vous utilisez pour griller votre pain !

![Image](https://www.freecodecamp.org/news/content/images/2020/08/DSC00564.jpeg)

![Image](https://www.freecodecamp.org/news/content/images/2020/08/DSC00568.jpeg)

Précaution supplémentaire : certains ingénieurs un peu salés pensent qu'il n'y a rien de mal à respirer les fumées de la soudure. Je suis très loin de ce camp. Non seulement vous manipulez des métaux lourds (moins un problème avec la soudure sans plomb) d'une manière ou d'une autre, mais les fumées du flux de soudure sont nocives. La meilleure façon de résoudre cela est de faire fonctionner un ventilateur vers la fenêtre ou d'utiliser un extracteur de fumées.

## Temps de jouer

![Image](https://www.freecodecamp.org/news/content/images/2020/08/DSC00570.jpeg)

Vous avez donc commandé toutes vos pièces, pochoirs et cartes. Vous avez patiemment et diligemment assemblé et soudé tous les composants. Félicitations, vous êtes arrivé dans la cour des grands ! La prochaine étape est le test, le développement du firmware ou [tout ce que vous devez faire avec votre conception](https://www.jaredwolff.com/getting-started-in-product-development/#show1).

De plus, pour être honnête, je n'ai rien contre des entreprises comme Macrofab. Elles fournissent un excellent service et je les ai même utilisées auparavant pour [d'autres projets](https://www.circuitdojo.org/iot-motion-light/#introduction). Rappelez-vous simplement du rapport coût/temps de quelqu'un d'autre faisant le travail pour vous. Est-ce que cela en vaut la peine ? Seul vous pouvez décider.

Construire votre propre circuit imprimé à moindre coût non seulement économise de l'argent, mais c'est gratifiant une fois terminé. Lorsque je construis de nouveaux appareils et prototypes pour mes clients, je garde toujours cette méthode comme une option. Cela me permet d'avoir une meilleure idée de la façon dont un circuit peut fonctionner avant d'avoir à débourser une tonne d'argent pour une carte assemblée en machine.

Vous cherchez de l'aide pour votre projet ? [Allez en bas de cette page et envoyez-moi un message.](https://www.jaredwolff.com/about/)

Vous pouvez également consulter mes autres articles sur mon blog à l'adresse [www.jaredwolff.com](https://www.jaredwolff.com/how-to-self-assemble-circuit-boards/).