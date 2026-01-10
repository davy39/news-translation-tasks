---
title: Coder du point de vue d'un météorologue
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-02-17T03:16:36.000Z'
originalURL: https://freecodecamp.org/news/coding-from-a-meteorologist-s-perspective-3c81aa9c1160
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WSOeSkBJKTWFaI1NzrFTvg.jpeg
tags:
- name: Meteorology
  slug: meteorology
- name: General Programming
  slug: programming
- name: 'Science '
  slug: science
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Coder du point de vue d'un météorologue
seo_desc: 'By Justin Lynn Reid

  Aside from researchers and TV weather people, few people are versed in the technical
  side of meteorology and atmospheric science.

  An eclectic field, atmospheric science combines aspects of mathematics, physics,
  technical writing, ...'
---

Par Justin Lynn Reid

En dehors des chercheurs et des présentateurs météo à la télévision, peu de gens maîtrisent l'aspect technique de la météorologie et des sciences atmosphériques.

Un domaine éclectique, les sciences atmosphériques combinent des aspects des mathématiques, de la physique, de la rédaction technique, de la recherche académique et de la communication de masse pour former un domaine avec une perspective unique.

J'ai travaillé sur de nombreux aspects des sciences atmosphériques. Ce dans quoi je me spécialise maintenant est un peu différent de ce que font la plupart des météorologues avec leur formation.

Au lieu de me concentrer sur les voies traditionnelles de la prévision opérationnelle, de la télévision ou de la recherche gouvernementale, je suis ce qu'on appelle un **programmeur météorologique** : à la fois météorologue et développeur logiciel.

Pour citer l'un de mes anciens collègues, la météorologie est le « premier problème de Big Data » où de nombreux précurseurs du nouveau domaine de la science des données existent. Les réseaux d'observation de la Terre (tels que les satellites, les stations météo de surface, les ballons-sondes et les radars Doppler) sont essentiellement une version à plus basse résolution de l'Internet des Objets qui fonctionne 24 heures sur 24. À partir de ces réseaux, plusieurs modèles physiques (appelés _Modèles de Prévision Numérique du Temps (NWP)_) sont exécutés sur des supercalculateurs par des agences gouvernementales ou des entreprises privées, produisant un ensemble de meilleures estimations des conditions atmosphériques futures que les prévisionnistes interprètent et analysent. Ce sont ces éléments en coulisses qui produisent les prévisions météo que vous obtenez en ligne ou via un média local.

Vous vous demandez peut-être comment tout cela est lié à quelque chose comme [Free Code Camp](https://www.freecodecamp.org/news/coding-from-a-meteorologist-s-perspective-3c81aa9c1160/undefined), JavaScript ou le développement web ? Je vais souligner quelques façons dont je pense que le sujet se prête directement au processus de développement logiciel, et aide même à en obtenir une meilleure compréhension.

#### La Méthode Scientifique et le « Principe de Mme Frizzle »

![Image](https://cdn-media-1.freecodecamp.org/images/1*_onUUp-cboGbIcLc6G2lwQ.png)
« Prenez des risques, salissez-vous, faites des erreurs ! » — Source de l'image : [lead_large.png](http://cdn.thewire.com/media/img/upload/wire/2014/06/11/Screen_Shot_2014_06_11_at_11.24.39_AM/lead_large.png" rel="noopener" target="_blank" title=")

En sciences atmosphériques, comme dans d'autres domaines STEM, de nouvelles découvertes ou insights sont réalisés via l'expérimentation, les tests et la revue par les pairs. Même après avoir été impliqué dans l'industrie de la météorologie pendant de nombreuses années professionnellement, j'appelle toujours ce processus le « Principe de Mme Frizzle ».

Dans un épisode de Magic School Bus où Mme Frizzle et ses élèves étaient en excursion pour explorer un volcan sous-marin, l'un des personnages citait constamment des recherches déjà écrites comme sa principale source de compréhension. Pendant l'excursion, l'élève perd ses livres, perdant ainsi l'accès aux « recherches » qu'elle citait constamment. Au cours de cela, elle doit apprendre à tirer des conclusions basées sur ses propres observations. À la fin de l'épisode, les conclusions de l'élève se sont avérées correctes, car elle avait raisonné que le volcan sous-marin entrerait en éruption et formerait une nouvelle île.

S'il y a une chose constante dans le travail de programmation que j'ai fait, c'est que je suis ce genre de processus pour chaque projet ou tâche que je complète. Bien que j'aie accès à des « recherches » sous forme de documentation, de posts sur des forums et de collaboration, il n'y a personne pour me dire comment assembler toutes les pièces pour créer l'application que je dois développer.

Pour écrire une application correctement, je dois décomposer un grand problème en une série de petits problèmes. Et pour chacun de ces petits problèmes, je dois essayer de trouver des connexions entre les idées afin de formuler une solution possible.

C'est une hypothèse et en programmation, je peux littéralement écrire ma meilleure supposition sous forme de lignes de code. Ensuite, je teste ces lignes de code pour ce petit problème donné et je vois si elles ont le comportement qui devrait être correct. Si le code fonctionne, je passe au petit problème suivant, sinon j'essaie de comprendre _pourquoi_ le code a échoué. Et j'utilise ensuite cette information pour faire une autre tentative de résolution du petit problème.

Lorsque vous résolvez tous les petits problèmes, l'application est terminée. C'est pourquoi, lorsque j'ai entendu parler du Développement Piloté par les Tests et des frameworks comme [Jasmine](http://jasmine.github.io), j'ai trouvé que regarder le code de cette manière était naturel pour moi personnellement. Cela a simplement été placé dans une manière formelle de faire les choses.

Si je pouvais vous donner juste deux conseils sur la programmation, ils seraient :

* ne jamais aborder un grand problème dans son ensemble
* ne jamais laisser un manque de connaissances vous intimider, car chaque nouveau projet est un voyage dans l'inconnu, et l'échec accompagne toujours l'inconnu.

#### Les Technologies Spécifiques à la Météorologie et le Web sont des Parents Très Proches

Outre la méthode scientifique, la météorologie possède de nombreuses technologies spécifiques au domaine qui rendent la transition vers le développement web pas si difficile.

En plus d'être exposé au web via des APIs ou des applications web conçues pour utiliser des données météorologiques, de nombreux concepts sous-jacents du calcul en sciences atmosphériques se traduisent directement.

Par exemple, des éléments tels que les images radar que vous voyez à la télévision sont des _visualisations de données_, une forme simplifiée d'un grand ensemble d'observations/données qui peuvent être interprétées efficacement.

Dans le cas du radar et des satellites, chaque observation est un pixel recueilli via la _télédétection_ et au lieu d'avoir des valeurs de pixels dans un tableau, les données sont rendues sous une forme plus utile.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ozaLl5Q3BjkV92FLJWoqzA.tiff)
_Un exemple d'image radar météorologique standard. La variable visualisée s'appelle Réflectivité et est corrélée avec des précipitations plus intenses. Les visualisations de données comme celles-ci sont le pain et le beurre de la prévision météorologique opérationnelle. Source : RadarScope par WDT_

En développement web, les données sont au cœur du comportement et de l'apparence des applications, ainsi que du contenu qu'elles possèdent.

Au lieu de manipuler des données dans un contexte météorologique courant (par exemple, trouver la température moyenne ou maximale), sur le web, les mêmes concepts sont utilisés de manière beaucoup plus générale, comme avec [D3.js](https://d3js.org).

Même au-delà de la visualisation, les technologies météorologiques courantes ont des analogues plus standardisés dans l'industrie du web, comme avec [Unidata LDM](http://www.unidata.ucar.edu/software/ldm/ldm-current/factsheet.html) et [Node.js](http://nodejs.org). La météorologie est inévitablement liée à la programmation et au web, et les deux sont des parties essentielles pour être un scientifique atmosphérique et un professionnel technique.

En conclusion, voici comment j'en suis venu à voir la programmation de mon point de vue personnel. La raison de chaque personne pour programmer est différente. J'espère que cela vous donnera une perspective sur la manière dont elle peut être appliquée aux domaines scientifiques.