---
title: Les femmes n'ont prononcé que 27 % des mots dans les plus grands films de 2016.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-12T13:56:31.000Z'
originalURL: https://freecodecamp.org/news/women-only-said-27-of-the-words-in-2016s-biggest-movies-955cb480c3c4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*92SrZzQkJAqwJoHu1xPneQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: feminism
  slug: feminism
- name: Movies
  slug: movies
- name: Web Development
  slug: web-development
- name: women in tech
  slug: women-in-tech
seo_title: Les femmes n'ont prononcé que 27 % des mots dans les plus grands films
  de 2016.
seo_desc: 'By Amber Thomas

  Movie trailers in 2016 promised viewers so many strong female characters. Jyn Erso.
  Dory. Harley Quinn. Judy Hopps. Wonder Woman. I felt like this could be the year
  for gender equality in Hollywood’s biggest films.

  I was wrong.

  And I ...'
---

Par Amber Thomas

Les bandes-annonces de films en 2016 promettaient aux spectateurs tant de personnages féminins forts. Jyn Erso. Dory. Harley Quinn. Judy Hopps. Wonder Woman. J'ai eu l'impression que cette année pourrait être celle de l'égalité des sexes dans les plus grands films de Hollywood.

Je m'étais trompée.

Et je ne fais pas cette déclaration à la légère.

En tant que scientifique, je me tourne vers les données pour répondre aux questions que je me pose sur le monde. Et j'ai les données pour étayer ma revendication. En fait, vous pouvez avoir les données, le code et la [visualisation de données](http://amber.rbind.io/2016MovieDialogue/) résultante que j'ai créés pour mieux comprendre ce sujet. Mais d'abord, laissez-moi vous dire comment je suis devenue si intéressée.

Tout a commencé lorsque je suis allée voir Rogue One: A Star Wars Story. Tous les matériaux promotionnels du film indiquaient que Jyn Erso (jouée par Felicity Jones) était le personnage principal. Je veux dire, regardez simplement l'affiche.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wEaxUjOocqR_ObtsKJaz0w.jpeg)

Quand votre photo est plusieurs fois plus grande que celle des autres, vous êtes probablement le personnage principal.

Ce que je n'ai pas remarqué au début, c'est que Jyn est la seule femme sur cette affiche.

Je suis entrée au cinéma en m'attendant à voir des hommes et des femmes se battre côte à côte. Je suis partie en étant certaine que je pouvais compter tous les personnages féminins du film sur une seule main. Bien que Jyn _était_ le personnage principal, j'étais profondément consciente qu'elle était souvent la seule femme dans une scène.

C'était étrangement familier d'avoir un personnage féminin principal si largement surpassé en nombre. Puis j'ai réalisé que Jyn et la princesse Leia souffraient de la même inégalité 39 ans plus tard. J'ai été submergée par le besoin de savoir exactement comment la représentation féminine dans les films Star Wars a changé. Mais il semblait injuste de comparer des films réalisés aujourd'hui avec des films réalisés il y a des décennies.

J'ai donc décidé de chercher l'égalité féminine parmi les 10 films les plus rentables au monde en 2016. Ils étaient :

* [Captain America: Civil War](http://www.imdb.com/title/tt3498820/?ref_=nv_sr_1)
* [Finding Dory](http://www.imdb.com/title/tt2277860/?ref_=nv_sr_1)
* [Zootopia](http://www.imdb.com/title/tt2948356/?ref_=nv_sr_1)
* [The Jungle Book](http://www.imdb.com/title/tt3040964/?ref_=nv_sr_1)
* [The Secret Life of Pets](http://www.imdb.com/title/tt2709768/?ref_=nv_sr_1)
* [Batman V. Superman: Dawn of Justice](http://www.imdb.com/title/tt2975590/?ref_=nv_sr_1)
* [Rogue One: A Star Wars Story](http://www.imdb.com/title/tt3748528/?ref_=nv_sr_2)
* [Deadpool](http://www.imdb.com/title/tt1431045/?ref_=nv_sr_1)
* [Fantastic Beasts and Where to Find Them](http://www.imdb.com/title/tt3183660/?ref_=nv_sr_1)
* [Suicide Squad](http://www.imdb.com/title/tt1386697/?ref_=nv_sr_1)

Avec autant de femmes puissantes dans ces films, certains d'entre eux doivent être égaux en termes de genre, n'est-ce pas ?

### **Les Données**

Maintenant que j'avais décidé ce que je voulais étudier, je devais déterminer comment le faire. Des projets similaires d'exploration de données se sont concentrés sur l'égalité des [dialogues](http://polygraph.cool/films/) ou du [temps à l'écran](https://seejane.org/research-informs-empowers/data/). Les deux semblaient être de bonnes options, mais je voulais la capacité de rendre compte de l'égalité au niveau du film et du personnage.

En fin de compte, j'ai décidé d'explorer les dialogues des films. Ce choix m'a permis de me concentrer sur les personnages ayant un rôle actif dans l'histoire et d'exclure les personnages non parlants de mon analyse.

Heureusement pour moi, des fans de cinéma dévoués transcrivent souvent les dialogues d'un film et les rendent librement disponibles en ligne. Si je ne trouvais pas de transcription, j'utilisais des fichiers de sous-titres à la place. Pour ceux-ci, j'ai regardé à nouveau le film et j'ai manuellement attribué les personnages à leurs répliques.

Ce processus a été un travail d'amour. C'était chronophage, mais je n'ai aucun regret.

### Analyse

Une fois que j'ai eu toutes les transcriptions, je devais simplement lire les fichiers .txt dans [R](https://cran.r-project.org/) et séparer les personnages de leurs répliques. Pour la transcription de Rogue One, ce processus ressemblait à ceci :

Maintenant que j'avais un tableau de données avec des colonnes pour les personnages et les mots, je devais attribuer des genres à chaque personnage. Pour rester cohérente avec mes catégorisations, j'ai établi quelques règles simples :

1. Lorsque cela est possible, attribuer le genre selon les pronoms que les autres personnages utilisent. Par exemple, si un personnage est désigné par les autres comme "il" ou "lui", alors il est catégorisé comme "masculin".
2. Si aucun pronom n'est utilisé tout au long du film mais que le personnage est nommé ou crédité (sur [IMDB](http://www.imdb.com/)), utiliser le genre de l'acteur ou de l'actrice. Notez que le genre d'un acteur ou d'une actrice a été supposé sur la base d'informations publiques disponibles en janvier 2017.
3. Si aucun pronom n'est utilisé pour le personnage et que le personnage n'est pas nommé ou crédité, se référer aux sous-titres. Parfois, ils identifieront le personnage qui a parlé.
4. Si tout le reste échoue, faire une supposition éclairée basée sur la voix du personnage.

Je serai la première à dire que ces méthodes ne sont pas parfaites. En fait, voici quelques mises en garde :

1. Si un personnage masculin était doublé par une actrice féminine (ou vice versa) et que le personnage n'était jamais désigné par d'autres personnages utilisant des pronoms, il pourrait être incorrectement étiqueté. (Je ne pense pas que cela soit arrivé, mais tout est possible.)
2. Les voix qui ne sont pas associées à une incarnation physique d'un personnage (par exemple, la voix d'un ordinateur) ont été catégorisées selon le genre de leur acteur/actrice de voix.
3. Je ne peux jamais _vraiment_ connaître le genre d'un personnage, mais j'utilise les indices et les informations que j'ai à ma disposition.

Encore une fois, je suis loin d'être infaillible, donc si vous avez repéré une erreur de ma part, veuillez [me le faire savoir](https://proquestionasker.github.io/contact/).

Donc, maintenant, je devais simplement compter le nombre de mots prononcés par chaque personnage. Encore une fois, j'ai pu le faire dans R en utilisant les packages `dplyr` et `stringi`.

Il est important de noter que j'ai inclus chaque personnage parlant dans cette analyse. Donc oui, chaque stormtrooper qui crie un simple "Attendez, arrêtez !" avant de se faire tirer dessus est inclus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Nix-DNJovl_3XwRVmJPc8Q.jpeg)
_Alerte spoiler : Les stormtroopers dans Rogue One sont tous doublés par des hommes._

### Visualisation des Données

J'avais mes données. Malheureusement, des tableaux et des tableaux de comptes de mots et de noms de personnages ne donnent pas beaucoup d'informations à quiconque. Comme tout bon projet d'exploration de données, il était temps de visualiser mes résultats. J'ai dû travailler à travers quelques itérations avant de trouver la meilleure.

Les nuages de points et les graphiques à barres masquaient tous deux les personnages avec de petits rôles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*79391ccZ2PRJ3bUjdtzOHA.jpeg)

Un simple graphique à bulles était mieux, mais il est devenu difficile d'identifier les personnages individuels. Il était également difficile de comprendre les statistiques au niveau du film.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ztI4yRBsYS7iKaJqe6D8PA.jpeg)
_Quelle bulle est laquelle ?!_

En fin de compte, j'ai décidé d'apprendre suffisamment de d3.js pour créer [un graphique interactif](http://amber.rbind.io/2016MovieDialogue/). Ici, chaque bulle représente un personnage, et la taille de la bulle est proportionnelle au nombre de mots prononcés. Les bulles féminines et masculines peuvent être séparées pour une meilleure compréhension. Les barres empilées ci-dessous indiquent les informations au niveau du film.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MH6WhQJc64Sy_ASXfSi9pA.gif)
_Version interactive complète [ici](https://proquestionasker.github.io/projects/MovieDialogueInteractive/" rel="noopener" target="_blank" title=")_

Allez-y, consultez la [version interactive complète](http://amber.rbind.io/2016MovieDialogue/).

Intéressé à explorer les données brutes de compte de mots par vous-même ? J'ai rendu toutes les données et le code utilisés pour générer ces visualisations open source. C'est disponible [ici](https://github.com/ProQuestionAsker/2016MovieDialogue) :

[**ProQuestionAsker/2016MovieDialogue**](https://github.com/ProQuestionAsker/2016MovieDialogue)
[_Contribuez au développement de 2016MovieDialogue en créant un compte sur GitHub._github.com](https://github.com/ProQuestionAsker/2016MovieDialogue)

### Conclusions

D'accord, donc l'analyse est terminée. J'ai une visualisation élégante (et amusante à utiliser). Qu'ai-je trouvé ?

Je recommande de prendre une seconde pour regarder quelque chose de "a-Dory-ble" avant de continuer, car cet article va devenir très déprimant très rapidement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MHd8U2CfQdn4uO32Kz7jbA.jpeg)

Aw, si mignon. Vous vous sentez bien ?

Très bien, c'est parti.

Voici une version statique de la visualisation pour les 10 films :

_(Si vous souhaitez consulter la visualisation interactive, allez [ici](https://github.com/ProQuestionAsker/2016MovieDialogue).)_

![Image](https://cdn-media-1.freecodecamp.org/images/1*8KRKoDWaCXmD2Vc8CTR2Hg.jpeg)
_La version interactive de cette visualisation peut être trouvée [ici](https://proquestionasker.github.io/projects/MovieDialogueInteractive/" rel="noopener" target="_blank" title=")._

Il y a quelques points ici que je dois souligner :

**Aucun des 10 meilleurs films de 2016 n'avait une distribution féminine à 50 % de rôles parlants.**

Finding Dory était le plus proche de ce niveau d'égalité avec 43 % de personnages féminins. Pour être égal, le film aurait eu besoin de 8 rôles féminins parlants supplémentaires.

Rogue One était le pire. Seulement 9 % de ses personnages parlants étaient des femmes. Parmi ces 10 personnages, 1 était une voix d'ordinateur, 1 est apparu à l'écran pendant pas plus de 5 secondes, et 1 était un caméo CGI qui a dit 1 mot.

**Seulement 1 des 10 meilleurs films de 2016 avait 50 % de dialogue par un personnage féminin.**

Finding Dory arrive également en tête ici avec 53 % de dialogue féminin. Mais 76 % de ce dialogue provenait de Dory seule.

En queue de peloton, The Jungle Book n'avait que 10 % de son dialogue prononcé par un personnage féminin. Gardez à l'esprit que c'est _après_ avoir choisi Scarlett Johansson comme voix du serpent historiquement masculin, Kaa.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6ntt5aIdPDh-w-gpxh71AA.png)
_Nous sommes égaux en termes de genre... Trusssssssst en moi..._

En voici quelques autres :

* Finding Dory et Zootopia étaient les seuls films parmi les 10 meilleurs de 2016 dans lesquels un personnage féminin avait le plus de dialogue.
* Les personnages féminins étaient surpassés en nombre dans la bataille finale de Captain America: Civil War, 5 contre 1. Tout au long du film, ils n'ont contribué qu'à 16 % du dialogue.
* Batman a parlé 2,4 fois plus que Superman et 6 fois plus que Wonder Woman dans Batman V. Superman.
* 78 % des répliques féminines dans Rogue One provenaient de Jyn Erso.
* Bien que Harley Quinn était un personnage très annoncé dans Suicide Squad, elle n'a parlé que 42 % autant de mots que Floyd/Deadshot (joué par Will Smith). Notamment, Amanda Waller (jouée par Viola Davis) a parlé fréquemment, totalisant seulement 222 mots (16 %) de moins que le compte de mots de Deadshot.

J'ai commencé ce projet parce que j'avais l'impression que la distribution et les dialogues de Rogue One n'étaient pas également divisés entre les personnages masculins et féminins. J'ai été choquée (et attristée) de constater que presque aucun des 10 meilleurs films de l'année dernière n'était égal en termes de genre.

Nous pouvons faire mieux.

_Ajouté_ : Si vous cherchez plus d'études et d'explorations de données comme celle-ci, consultez :

* [Inégalité dans 800 films populaires de 2007 à 2015](http://annenberg.usc.edu/sitecore/shell/Controls/Rich%20Text%20Editor/~/media/10575E37F34248C585602A69C18F2CBE.ashx) (inclut le genre, la race/ethnie, l'orientation sexuelle et le handicap)
* [Cette exploration](http://polygraph.cool/films/) de 2000 scripts de films sélectionnés aléatoirement des années 1980 à 2010
* [Cette recherche](https://seejane.org/research-informs-empowers/data/) sur les 200 plus grands films de 2014 et 2015
* [Représentations féminines dans les plus grands films de 2014](http://womenintvfilm.sdsu.edu/files/2014_Its_a_Mans_World_Report.pdf)
* [Ce fil Twitter](https://twitter.com/haleshannon/status/811669382065590272) sur l'égalité des genres dans les films animés de 2016

Version TL;DR : Les femmes représentent (en moyenne) 30 à 35 % des rôles parlants dans chacune de ces enquêtes.

_Ajouté_ : Vous avez des questions ou des commentaires sur ma méthodologie ou mes conclusions ? Consultez mon article de suivi présentant les questions les plus fréquemment posées.

[**J'ai analysé les dialogues des plus grands films de 2016 et cela a suscité beaucoup de conversations.**](https://medium.com/@ProQuesAsker/i-analyzed-the-dialogue-in-2016s-biggest-movies-and-it-started-a-lot-of-conversations-b9c815f24313)
[_Il y a quelques semaines, j'ai publié une histoire sur mon analyse des dialogues dans les 10 films les plus rentables de 2016. Je suis si..._medium.com](https://medium.com/@ProQuesAsker/i-analyzed-the-dialogue-in-2016s-biggest-movies-and-it-started-a-lot-of-conversations-b9c815f24313)

**Si vous avez aimé cet article et souhaitez en voir plus comme celui-ci, veuillez cliquer sur le cœur vert ci-dessous et partager sur votre réseau social préféré.**

Je passe actuellement mon temps à travailler sur des projets personnels et des visualisations de données comme celle-ci tout en cherchant un emploi en science des données. Donc, si vous avez une idée de projet amusant (ou une demande d'emploi) que vous aimeriez discuter avec moi, veuillez me contacter sur [Twitter](https://twitter.com/ProQuesAsker) ou par [email](mailto:amberthomasmsc@gmail.com).

Merci !