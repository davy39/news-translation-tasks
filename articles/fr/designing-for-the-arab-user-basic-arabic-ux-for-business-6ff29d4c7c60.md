---
title: Concevoir pour l'utilisateur arabe — UX arabe de base pour les entreprises
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-15T21:25:25.000Z'
originalURL: https://freecodecamp.org/news/designing-for-the-arab-user-basic-arabic-ux-for-business-6ff29d4c7c60
coverImage: https://cdn-media-1.freecodecamp.org/images/1*V0fcPJS3oA5t990wXkyQjA.png
tags:
- name: Design
  slug: design
- name: Entrepreneurship
  slug: entrepreneurship
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Concevoir pour l'utilisateur arabe — UX arabe de base pour les entreprises
seo_desc: 'By Anna Rubkiewicz

  What you’ll read about in this article:


  Mirroring layout for an Arabic interface is key, but has its limitations,

  Digits are written from left to right in Arabic, despite a right-to-left interface,

  Translating text into Arabic is ...'
---

Par Anna Rubkiewicz

### Ce que vous lirez dans cet article :

* La mise en miroir pour une interface arabe est essentielle, mais a ses limites,
* Les chiffres sont écrits de gauche à droite en arabe, malgré une interface de droite à gauche,
* Traduire le texte en arabe ne suffit pas pour créer une interface arabe,
* Tous les mots ne peuvent pas être traduits 1:1 en arabe ; certains nécessiteront des phrases longues et descriptives,
* L'écriture arabe nécessite généralement une police plus grande que celle utilisée pour l'alphabet romain,
* Il est judicieux de diriger les utilisateurs arabes vers du contenu en anglais (seulement environ 5 % du contenu mondial est en arabe).

En tant que traductrice avec plus de 10 ans d'expérience (anglais, arabe et polonais), ainsi qu'ancienne employée de startup responsable du développement de la base de données de produits [FMCG](https://en.wikipedia.org/wiki/Fast-moving_consumer_goods), je ne peux m'empêcher de remarquer une sous-représentation apparente du monde arabe en matière de contenu et de design centré sur l'utilisateur. 

Intéressamment, cela ne correspond pas à une faible pénétration d'Internet au Moyen-Orient, comparé au reste du monde. Au 31 mars 2017, il y avait près de 142 millions d'utilisateurs dans la région. Cela signifie que 57,4 % de ses habitants étaient en ligne — comparé à la moyenne mondiale de 49,2 % ([1](http://www.internetworldstats.com/stats5.htm)).

En même temps, **60 % des Arabes (et jusqu'à 97 % en Arabie Saoudite et en Égypte) déclarent que l'arabe serait leur langue de choix** lors de la navigation ou des achats en ligne. Pendant ce temps, **seulement 5 % du contenu mondial est dans cette langue** ([2](https://arabiangazette.com/an-online-arabic-content-revolution-in-the-making/)) :

![Image](https://cdn-media-1.freecodecamp.org/images/9VXx6lGlWBn2A4cIqbdZ776-XxDoJwyiMYIm)

![Image](https://cdn-media-1.freecodecamp.org/images/wo4a8oHvoT1cpxZx9YHPAyeauVVtVYyE-6iW)

Un rapport de l'International Data Corporation (IDC) indique également que le marché mondial de l'IoT atteindra une valeur de 1 710 milliards de dollars d'ici la fin de 2020, dont 6,6 milliards proviendront du Moyen-Orient et de l'Afrique ([3](https://www.wamda.com/memakersge/2017/07/digital-middle-east-making)).

![Image](https://cdn-media-1.freecodecamp.org/images/CzPAvUcV98UFtoSxqS-wlAh3H7O9gZL0sP6u)

Les statistiques ci-dessus prouvent que les sociétés du Moyen-Orient sont aussi compétentes en technologie et actives sur les réseaux sociaux que dans le reste du monde ([4](https://www.thenational.ae/uae/facebook-and-twitter-key-to-arab-spring-uprisings-report-1.428773)). 

Pourquoi, alors, doivent-ils se tourner vers des sites et services en anglais pour profiter pleinement des nouvelles technologies ? De plus, pourquoi les entreprises manquent-elles l'incroyable potentiel commercial de la région en ne s'adaptant pas aux spécificités sociologiques, linguistiques et culturelles locales ?

Cela ne concerne pas uniquement les petites entreprises avec une exposition limitée ou des équipes de design réduites. Comme l'a remarqué la société de conseil en UX Yalantis, même Apple, qui aspire à être le leader du design innovant, n'avait pas pleinement adapté son iOS pour l'utilisateur RTL (de droite à gauche) avant la sortie d'iOS 9 à la fin de 2015 ([5](https://yalantis.com/blog/japanese-chinese-and-arabic-layouts-in-user-interface-and-user-experience-design/)).

Enfin, que peut-on faire pour l'utilisateur arabe, afin qu'il puisse utiliser sa langue maternelle tout en bénéficiant des ressources abondantes en anglais ?

Voici plusieurs aspects à prendre en considération lors de la conception pour un locuteur natif arabe, dont le sens de l'ordre chronologique, de l'affichage, etc., diffère des utilisateurs élevés dans des pays utilisant des scripts LTR.

## Miroir, miroir

La mise en miroir est souvent citée comme la règle 101 que quiconque souhaitant lancer une application dans le monde arabe devrait suivre. Bien que ce soit une généralisation, le concept principal est que la disposition RTL devrait refléter celle créée pour l'utilisateur LTR (de gauche à droite). 

Alors que la plupart des images de mouvement dans le monde occidental sont montrées de gauche à droite (par exemple, les publicités de voitures en mouvement), les pays utilisant l'écriture arabe (donc pas seulement le Moyen-Orient, mais aussi, par exemple, l'Iran et le Pakistan) sont plus susceptibles de percevoir la progression et le mouvement vers l'avant s'ils sont montrés de droite à gauche.

![Image](https://cdn-media-1.freecodecamp.org/images/GsW3I-AHqZbb9F114iEbfsuh5hHz6qmpkDlu)
*Bien que l'homme à droite court en fait de droite à gauche, je suis presque sûr que l'histoire était censée être lue de gauche à droite... Source : [http://gosmellthecoffee.com/archives/9570](http://gosmellthecoffee.com/archives/9570" rel="noopener" target="_blank" title=")*

Cela, exhaustivement expliqué par les directives de Material Design de Google, inclut, entre autres, les icônes de direction (icônes pour "avancer" et "retour") et d'autres symboles et icônes qui indiquent le mouvement. Cela ne signifie pas, cependant, que tous les symboles doivent être changés en conséquence. 

Il faut garder à l'esprit que les Arabes sont simultanément des utilisateurs d'interfaces et de programmes LTR, donc certains symboles (pensez à Facebook ou à la recherche Google) n'ont pas besoin d'être changés.

![Image](https://cdn-media-1.freecodecamp.org/images/KiVulSeen4Pyx8RHUY-VqhqJIwcE1RTdFQ16)

![Image](https://cdn-media-1.freecodecamp.org/images/wqrcJxOiY2asiHA7ZxCGOvN2lajTsGjSTcdn)
*Exemples de mise en miroir — comme vous pouvez le voir, l'espace de stockage et le volume sont montrés de droite à gauche.*

![Image](https://cdn-media-1.freecodecamp.org/images/U0hEz0ByhI0PiqZV43MrbiTsC6Sul8OMejU3)
*Exemples d'icônes qui n'ont pas besoin d'être mises en miroir lorsqu'elles sont utilisées dans une interface RTL.*

![Image](https://cdn-media-1.freecodecamp.org/images/QLw-Tm9wHeCZXhLix6Hf9mInLOxrWCtMFxgt)
*Une application intéressante de deux règles — la direction de l'icône n'est pas mise en miroir, mais le nombre est changé pour l'utilisateur arabe (ici, les chiffres indo-arabes sont utilisés, qui sont toujours utilisés simultanément dans le monde arabe, avec les chiffres arabes). Tous les exemples ci-dessus cités de : [https://material.io/guidelines/usability/bidirectionality.html#bidirectionality-rtl-mirroring-guidelines](https://material.io/guidelines/usability/bidirectionality.html#bidirectionality-rtl-mirroring-guidelines" rel="noopener" target="_blank" title=")*

Une autre limitation importante de la mise en miroir est la **bidirectionnalité**, courante non seulement en arabe, mais aussi dans les scripts d'Asie de l'Est. À savoir, bien que le texte soit aligné à droite, les nombres sont toujours lus de gauche à droite. Que signifie cela pour le designer ? Il ou elle doit faire attention et considérer qu'une longue séquence de nombres peut "entrer en conflit" avec l'écriture arabe, si la mise en page n'est pas conçue de manière responsive.

Exemples de chiffres dans des phrases arabes :

 641 64a  641 62a 631 629  645 627  628 64a 646  627 644 62d 631 628 64a 646  627 644 639 627 644 645 64a 62a 64a 646 **1919 20131939**  
Anglais : *Dans les années entre les guerres : 1919 20131939 (remarquez comment la première date est écrite à droite et la date de fin à sa gauche, malgré les nombres étant lus de gauche à droite).*

 628 644 63a  639 62f 62f  633 643 627 646  628 648 644 646 62f 627  641 64a  62f 64a 633 645 628 631 [2007](https://ar.wikipedia.org/wiki/2007)  62d 648 627 644 64a **38,116,000**  646 633 645 629  
Anglais : En décembre 2007, le nombre d'habitants de la Pologne a atteint environ **38,116,000.**

Un fait intéressant est que les Arabes utilisent actuellement aussi les chiffres indo-arabes (mentionnés ci-dessus), qui sont également écrits de gauche à droite.

## Traduction et vérification

Je ne peux pas insister assez sur le fait qu'il ne suffit pas d'engager un interprète pour traduire le texte en arabe et considérer le travail de création d'une version arabe d'un site/application comme terminé. 

C'est une semi-tragédie de voir un design LTR avec un script arabe appliqué à la place, disons, du texte anglais. C'est une tragédie à part entière — et j'en ai été témoin à plusieurs reprises — lorsque les entreprises essaient d'utiliser le script arabe, mais, après avoir traité le texte dans un CMS ou un éditeur, les lettres se séparent et ne forment plus de mots. 

La seule chose pire qu'un design chaotique et impraticable est celui où les lettres arabes sont déconnectées à l'écran/livre/couverture de produit et ne constituent plus des mots.

C'est une erreur courante qui a ses racines dans le fait que les lettres arabes prennent différentes formes, selon leur place dans un mot donné :

![Image](https://cdn-media-1.freecodecamp.org/images/FbGtAceIsQs7kfjraneq8OYTsUHo4rmJKrar)
*Source : [http://tjhomeschooling.blogspot.com/2015/11/thm-sadaqa-group-has-nice-simple-arabic.html](http://tjhomeschooling.blogspot.com/2015/11/thm-sadaqa-group-has-nice-simple-arabic.html" rel="noopener" target="_blank" title=")*

Si nous ne savons pas comment lire le script arabe, nous risquons d'avoir des phrases entières affichées sous une forme illisible. Voici un exemple qui montre deux erreurs :

* les lettres sont dans leur forme isolée (donc ne forment pas de mots)
* les lettres sont écrites de gauche à droite au lieu de droite à gauche (donc, à l'envers).

![Image](https://cdn-media-1.freecodecamp.org/images/2L0f4XXnl1-iBKTym7pEhbX-loI-h7LtMV9k)
*Source : [http://www.arabicgenie.com/wp-content/uploads/2009/08/disconnected-lefttoright.jpg](http://www.arabicgenie.com/wp-content/uploads/2009/08/disconnected-lefttoright.jpg" rel="noopener" target="_blank" title=")*

Par conséquent, il est préférable de toujours faire relire par une personne arabophone tout texte traduit avant de l'envoyer en production. 

De plus, s'il y avait une police que je recommanderais pour traduire du texte dans des scripts non romains, ce serait [**Noto**](https://www.google.com/get/noto/), une **police universelle conçue par Google.** Elle éliminera, au moins, le risque de "tofu" :

![Image](https://cdn-media-1.freecodecamp.org/images/rmBMW3vWEm-JuVE85vr33duWDjG33AhScKYz)
*Source : [http://www.monotype.com/resources/case-studies/more-than-800-languages-in-a-single-typeface-creating-noto-for-google/](http://www.monotype.com/resources/case-studies/more-than-800-languages-in-a-single-typeface-creating-noto-for-google/" rel="noopener" target="_blank" title=")*

## Traductions 1:1

Éviter les erreurs techniques n'est pas la seule chose à surveiller, car la traduction mot à mot ne fonctionne pas toujours non plus. Alors que certains pays arabes sont assez libéraux avec l'utilisation de mots étrangers en cas d'absence d'équivalent littéral, d'autres préfèrent utiliser des traductions descriptives. 

Le premier cas est particulièrement vrai pour les applications conçues pour les jeunes clients, et sont souvent créées dans des dialectes locaux et colloquiaux. D'autres, comme les applications utilisées à des fins professionnelles ou académiques, applicables à plusieurs marchés arabes, sont plus susceptibles d'être écrites en arabe standard moderne (MSA), qui est assez formel et standardisé. 

En conséquence, un mot de 10 lettres en anglais, traduit en arabe formel, peut aboutir à une phrase descriptive arabe de 2 20133 mots (occupant ainsi plus d'espace). De plus, gardez à l'esprit qu'il y a relativement peu d'abréviations en arabe, donc pas de raccourcis là.

Voici quelques exemples de mots avec leur traduction en arabe (remarquez la longueur des mots) :

* TV —  62a 644 641 632 64a 648 646 (c'est un mot emprunté lu : te-le-fee-syoo-n)
* KFC —  62f 62c 627 62c  643 646 62a 627 643 64a
* Émission de TV —  628 631 646 627 645 62c  62a 644 641 632 64a 648 646 64a

Un autre défi est que la plupart des lettres arabes sont écrites ensemble, beaucoup ont des points (regardez :  628,  62a,  62c,  62b,  64a), et, dans certains cas, des diacritiques (petits symboles pour les voyelles) sont écrits au-dessus des lettres (lisez à ce sujet [ici](https://en.wiktionary.org/wiki/vowelization#English)). Tout cela signifie que, pour rendre la lecture confortable pour l'utilisateur final, **une police plus grande peut être nécessaire** que celle utilisée pour le même mot en anglais.

L'exemple suivant montre une police arabe 3 points plus grande que le texte anglais (première image) et des polices de même taille (deuxième image) :

![Image](https://cdn-media-1.freecodecamp.org/images/pPm16O8SlXG015mnd8skxXn4aeJA3GQ99uyu)

![Image](https://cdn-media-1.freecodecamp.org/images/PxjoMOe7XUgN-OXDPiu2kL1TYATruEFksRe4)

> Pour en savoir plus sur l'alphabet arabe, cliquez [ici](http://www.arabic-course.com/arabic-alphabet.html).

J'ai travaillé sur une tâche linguistique similaire lors de mon emploi dans une startup ciblant les FMCG. Le produit, une application d'achats quotidiens, devait accommoder à la fois les locuteurs polonais et anglophones. Les textes JSON originaux, écrits en anglais, devaient ensuite être traduits en polonais, et finalement lancés dans l'Apple Store et Google Play pour les utilisateurs polonophones. 

Bien que le vocabulaire polonais soit riche, et que les langues originale et cible soient des scripts LTR, il était assez difficile de traduire toutes les chaînes de texte de sorte qu'elles ne perturbent pas la mise en page, et de maintenir un style de communication cohérent (détendu) dans les deux langues. 

Il est donc crucial que les traducteurs soient impliqués dans le processus de design, aient accès aux prototypes, et soient conscients de l'endroit où chaque texte traduit ira dans l'application.

## Internet en langue anglaise comme alternative

Alors que divers rapports indiquent que les utilisateurs arabes sont en ligne et apprécieraient grandement de naviguer et d'utiliser des services en arabe, il faudra des années aux entreprises et services en ligne pour fournir la quantité et le type de contenu qui rendraient une expérience monolingue possible. 

Les interfaces des appareils, disponibles entièrement en arabe, sont une chose. Une autre est d'effectuer une tâche, comme rechercher un sujet complexe en arabe ou acheter en ligne, et trouver des informations suffisantes dans la langue donnée.

Le système de référence de Wikipedia est un excellent exemple de la manière dont un utilisateur peut être dirigé vers des informations en anglais, si sa langue de choix n'était pas suffisante. Le même principe pourrait être appliqué avec succès par d'autres sites web — un utilisateur d'interface arabe pourrait être dirigé vers du contenu en anglais, ou des résultats en anglais pourraient être incorporés dans les résultats d'une recherche en arabe.

Cela améliorerait définitivement l'expérience utilisateur et, par conséquent, augmenterait les ventes et l'exposition d'un service donné. 

Imaginons un produit que nous avons en stock, mais sans contenu disponible en arabe à part le nom du produit. Cela ne devrait pas nous empêcher de montrer à un consommateur arabe les informations sur le produit en anglais — il ou elle est plus susceptible d'acheter si une description en anglais, les conditions de livraison et les détails de disponibilité sont disponibles à la place de champs vides. Une interface bien conçue devrait rendre ce mélange flexible LTR et RTL possible.

## Conclusion

Concevoir pour les utilisateurs de l'écriture arabe ne se limite pas à la traduction de contenu à partir d'une langue étrangère. Cela nécessite de la considération, de l'attention aux détails, et la conscience que, bien que des pratiques courantes, comme la mise en miroir, puissent être appliquées, les utilisateurs arabes sont déjà habitués à certains outils et solutions des interfaces de gauche à droite. 

Les entreprises devraient observer le marché MENA, sa scène locale de startups, les tendances en ligne et les changements sociopolitiques. Cela, parmi d'autres arguments dont je parlerai dans de futurs articles, devrait fournir une manière cohérente de communiquer et de livrer des services pour le marché arabe.

Si vous cherchez des **consultations en UX arabe** pour votre entreprise/projet, vous êtes plus que bienvenu pour me contacter via ma page [LinkedIn](https://www.linkedin.com/in/annarubkiewicz/).

Avez-vous apprécié cet article ? Vous pourriez aussi aimer mes articles sur l'[**UX du Hajj**](https://medium.com/@anna.rubkiewicz/the-ux-of-hajj-new-technologies-for-the-modern-pilgrim-3af9c6dad1c) et la [**Réinvention de la typographie arabe**](https://medium.com/@anna.rubkiewicz/reinventing-arabic-type-old-meets-new-5183239d4d96).

Vous pouvez en apprendre plus sur mon travail et trouver plus d'articles sur [www.contentki.com](http://www.contentki.com/).

### Lectures recommandées :

* Un excellent guide en 3 parties pour créer des interfaces arabes :  
[http://uxbert.com/designing-an-arabic-user-experience-usability-arabic-user-interfaces/](http://uxbert.com/designing-an-arabic-user-experience-usability-arabic-user-interfaces/)
* Harvard Business Review sur la compréhension du consommateur arabe :  
[https://hbr.org/2013/05/understanding-the-arab-consumer](https://hbr.org/2013/05/understanding-the-arab-consumer)
* Smashing Magazine sur le design web dans le monde arabe :  
[https://www.smashingmagazine.com/2010/09/showcase-of-web-design-in-the-arab-world/](https://www.smashingmagazine.com/2010/09/showcase-of-web-design-in-the-arab-world/)
* Pourquoi est-il si difficile de concevoir des polices arabes :  
[https://www.wired.com/2015/10/why-its-so-hard-to-design-arabic-typefaces/](https://www.wired.com/2015/10/why-its-so-hard-to-design-arabic-typefaces/)
* Ressources de design de sites web arabes par CXPartners :  
[https://www.cxpartners.co.uk/our-thinking/arabic-website-design-resources/](https://www.cxpartners.co.uk/our-thinking/arabic-website-design-resources/)
* Un article fascinant et une application pour ceux qui s'intéressent au design pour les locuteurs d'ourdou :  
[http://wahibhaq.com/blog/introducing-urdu-font-comparator-app/](http://wahibhaq.com/blog/introducing-urdu-font-comparator-app/)