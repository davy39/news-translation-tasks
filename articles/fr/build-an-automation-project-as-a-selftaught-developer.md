---
title: Comment j'ai construit un projet d'automatisation informatique en tant que
  développeur logiciel autodidacte
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-23T14:55:00.000Z'
originalURL: https://freecodecamp.org/news/build-an-automation-project-as-a-selftaught-developer
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/Python-2.jpg
tags:
- name: automation
  slug: automation
- name: projects
  slug: projects
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
seo_title: Comment j'ai construit un projet d'automatisation informatique en tant
  que développeur logiciel autodidacte
seo_desc: "By Kushal Bhatia\nI have always been obsessed with how technologies work,\
  \ namely computers. But my passion was hindered by a voice in my head that echoed\
  \ time and time again – \"you are not smart enough to study computer science.\"\
  \ \nI thought I needed t..."
---

Par Kushal Bhatia

J'ai toujours été obsédé par le fonctionnement des technologies, notamment des ordinateurs. Mais ma passion était entravée par une voix dans ma tête qui résonnait encore et encore – "**tu n'es pas assez intelligent pour étudier l'informatique.**"

Je pensais devoir être hautement qualifié en mathématiques quantitatives et être un génie pour même envisager une entreprise computationnelle, et encore moins poursuivre une carrière à temps plein en développement logiciel.

Tout cela a changé en mars 2020. J'ai été licencié de mon poste de Business Development Manager dans une startup leader en analyse de données et automatisation marketing, en raison de la pandémie de Coronavirus.

C'est alors que j'ai décidé de me lancer dans un voyage pour enfin poursuivre mes rêves de devenir développeur logiciel.

Vous voyez, j'ai obtenu mon diplôme de l'Université de Californie, Los Angeles en 2012 avec un Bachelor of Arts en sciences politiques, convaincu que je irais à la faculté de droit et deviendrais avocat.

Depuis lors, j'ai travaillé pour un certain nombre de startups, occupant de nombreux rôles, y compris Coordinateur de compte technique et Business Development Manager. J'ai même exploré le monde puissant de la finance, travaillant comme analyste en banque d'investissement pendant quelques années.

Mais aucun de ces emplois ne m'attirait même de loin, et je savais que j'avais besoin d'un changement pour de bon.

## Feuille de route pour devenir développeur logiciel

J'ai commencé mon voyage en développement logiciel en utilisant deux sites web : [freeCodeCamp](https://www.freecodecamp.org/) et [The Odin Project](https://www.theodinproject.com/). Grâce à eux, j'ai appris HTML, CSS, Git, Bash et Github.

C'était ma première véritable entrée dans le monde unique de la technologie, où j'ai construit des mini-projets, comme recréer la page d'accueil de Google. J'utilisais des commandes Bash, puis je poussais mes changements Git vers GitHub. C'était fascinant de voir quelque chose de tangible prendre vie avec seulement quelques lignes de code !

Parce que HTML et CSS sont des langages de balisage et de style, j'ai dû apprendre un vrai langage de programmation. Après des recherches approfondies en ligne (principalement sur Reddit), j'ai choisi entre Java ou Python. J'ai opté pour ce dernier.

J'ai commencé à lire deux livres d'introduction sur Python qui m'ont vraiment excité au sujet de ce beau langage. Il s'agissait de _Automate the Boring Stuff with Python_ par [Al Sweigart](https://twitter.com/AlSweigart) et _Python Crash Course_ par [Eric Matthes](https://twitter.com/ehmatthes).

Ces deux auteurs sont aussi brillants qu'hilarants, et j'ai vraiment apprécié parcourir chaque chapitre, complétant les devoirs requis.

À ce stade, je connaissais les bases, mais je voulais apprendre à construire avec cette nouvelle connaissance.

J'ai donc suivi une spécialisation de cinq cours sur Coursera appelée _[Python for Everybody Specialization](https://www.coursera.org/specializations/python)_ par le grand Charles Severance, alias [Dr. Chuck](https://twitter.com/drchuck). C'était exactement ce dont j'avais besoin pour combler le fossé entre le niveau débutant et intermédiaire en Python.

Cette spécialisation m'a pris presque deux mois à compléter. J'ai appris SQL, les protocoles Internet, JSON, XML, et une variété de bibliothèques Python, y compris _[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)_ et _[Urllib](https://urllib3.readthedocs.io/en/latest/)_ (utilisées pour le web scraping).

Dr. Chuck est une véritable légende dans le monde de la technologie, et il n'est pas surprenant que ses cours soient parmi les plus suivis sur Coursera.

À ce stade, j'avais assez de connaissances en HTML, CSS, SQL et Python pour dire en toute confiance que j'étais un développeur logiciel intermédiaire.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/cover.jpeg)
_Il est temps de créer un projet significatif !_

## Comment (et pourquoi) j'ai construit mon projet d'automatisation informatique

Cependant, à ce stade, j'ai réalisé que je n'avais rien créé de significatif qui pourrait attirer l'attention des employeurs potentiels. Rien que je puisse publier sur GitHub, qui serait cloné des centaines de fois, forké des milliers de fois. En un sens, ma présence open-source était inexistante.

J'ai parcouru Internet, à la recherche d'idées de projets en Python. Bien sûr, j'aurais pu créer un web-scraper ou un autre bot Twitter ennuyeux, mais je voulais construire quelque chose de différent.

En réfléchissant, je me suis souvenu de mon ancien emploi de Business Development Manager. Là-bas, j'étais chargé de la tâche ardue et monotone de trouver des comptes en double sur notre CRM Salesforce (il y avait plus d'un million d'enregistrements !).

Comme j'aurais souhaité pouvoir écrire un simple script pour faire faire le travail à mon ordinateur en quelques minutes, au lieu de semaines.

Puis une idée m'est venue – pourquoi ne pas construire un utilitaire qui parcourrait tous les fichiers de mon ordinateur et chercherait les doublons ? La personne moyenne a probablement une tonne de fichiers sur son ordinateur, dont beaucoup sont créés plusieurs fois et complètement oubliés.

Les idées ont commencé à fuser. J'ai pensé à de nombreux cas d'utilisation pour des industries telles que la finance et la santé qui pourraient définitivement utiliser quelque chose comme cela pour parcourir leurs enregistrements en un rien de temps.

J'ai décidé de me lancer dans VS Code, de créer un fichier .py, et de le nommer duplicate_files. Il était enfin temps de mettre mon chapeau de concepteur de logiciels et de construire mon chef-d'œuvre.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/Screen-Shot-2020-10-22-at-2.50.59-PM-1.png)

![Image](https://www.freecodecamp.org/news/content/images/2024/08/Screen-Shot-2020-10-22-at-2.55.32-PM.png)
_Extrait de mon utilitaire de fichiers en double sur GitHub_

## Construction de l'utilitaire de fichiers en double

L'une des parties les plus difficiles de la conception de votre projet est de décider quelles bibliothèques vous voulez utiliser.

* Je savais que je voulais accéder aux fichiers de mon ordinateur, donc j'ai ajouté la bibliothèque OS.
* Je savais que je voulais trouver le hash unique de chaque fichier pour les différencier, donc j'ai choisi la bibliothèque hashlib.
* Je savais que je voulais que les utilisateurs fournissent leurs propres arguments lors de l'exécution de cet utilitaire, donc j'ai choisi la bibliothèque argparse.
* Et bien sûr, je voulais chronométrer le temps total de traitement de l'utilitaire, donc j'ai ajouté la bibliothèque time.

Une autre partie difficile de la conception de votre projet est de décider quelles structures de données fonctionnent le mieux. Après quelques essais et erreurs, j'ai choisi deux dictionnaires et une liste (qui appliquerait les répertoires ignorés par l'utilisateur sur Windows, macOS et Linux).

Il était extrêmement important pour moi que cela englobe en fait **"Un programme simple mais puissant qui recherche des fichiers en double avec des hash uniques sur votre ordinateur Windows, macOS ou Linux"**.

C'est pourquoi je voulais utiliser les blocs de construction de base que Python avait à offrir - boucles, conditionnelles et **FONCTIONS**. Je n'ai pas utilisé de programmation orientée objet complexe que vous pourriez voir dans d'autres projets. Ce programme a simplement trois fonctions principales, c'est tout !

J'ai terminé ma conception en ajoutant un fichier README, et j'ai également inclus un fichier .gitignore chaque fois que j'ai poussé mes changements vers GitHub. J'ai soigneusement testé ce programme via le débogueur VS Code (en modifiant le fichier launch.JSON), ainsi que sur plusieurs ordinateurs qui avaient tous les principaux systèmes d'exploitation.

En fait, ce programme a été exécuté sur une machine Windows, où le chemin donné contenait un fichier de 6 Go. Le programme semblait s'arrêter temporairement lorsqu'il atteignait ce fichier, puis a continué et s'est terminé en un temps extrêmement rapide.

Dans cet exemple, le chemin contenait 100 000 fichiers, et s'est terminé en cinq minutes. Il y a quelques mois, j'étais émerveillé par la façon dont quelque chose que j'avais écrit en HTML et CSS de base était affiché sur un site web.

Après avoir exécuté ce programme aujourd'hui, je suis vraiment fasciné par la vitesse et la complexité avec lesquelles les ordinateurs peuvent fonctionner lorsqu'on leur donne seulement quelques lignes de code !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/naval.jpg)
_Naval Ravikant, l'un de mes idoles_

## Conclusion

Cela a été un voyage incroyablement difficile, mais gratifiant de 8 mois (et plus) pour apprendre à devenir développeur logiciel.

Pendant un moment, j'ai pensé à suivre un bootcamp. J'ai même envisagé un programme de maîtrise en informatique.

Mais avec les excellents matériaux gratuits et open-source disponibles sur Internet, j'avais confiance en ma capacité à apprendre par moi-même.

Je tiens à remercier chaleureusement [Quincy Larson](https://twitter.com/ossia) pour m'avoir motivé à commencer mon voyage sur freeCodeCamp. Je tiens également à remercier Al Sweigart, Eric Matthes, Charles Severance et Guido van Rossum, qui, directement ou indirectement, ont été instrumentaux pour m'aider tout au long de mon voyage jusqu'à présent.

J'espère que cet article accomplira deux choses :

1. Motiver les autres qui sont soit incertains quant à ce qu'ils veulent faire en termes de carrière, soit simplement effrayés, à se lancer et à commencer à coder !
2. Qu'un employeur me donne une chance, afin que je puisse réaliser l'un de mes plus grands rêves de devenir développeur logiciel (bien qu'autodidacte).

Pour conclure : L'un de mes plus grands idoles, _[Naval Ravikant](https://twitter.com/naval)_, un programmeur informatique renommé, investisseur et philosophe moderne, a une citation qui a toujours résonné en moi.

> "Apprenez à vendre. Apprenez à construire. Si vous pouvez faire les deux, vous serez imparable."

Eh bien, j'ai construit une carrière en vendant dans les industries de la finance et de la technologie, et maintenant j'ai appris à construire. **JE SERAI IMPARABLE.**

Vous pouvez me trouver sur _[Twitter](https://twitter.com/Kushal_Bhatia)_, _[LinkedIn](https://www.linkedin.com/in/kushalbhatia)_ et _[GitHub](https://github.com/kushalbhatia)._