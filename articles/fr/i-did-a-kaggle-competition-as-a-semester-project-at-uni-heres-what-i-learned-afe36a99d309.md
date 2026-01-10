---
title: J'ai participé à une compétition Kaggle dans le cadre d'un projet de semestre
  à l'université. Voici ce que j'ai appris.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-24T17:36:04.000Z'
originalURL: https://freecodecamp.org/news/i-did-a-kaggle-competition-as-a-semester-project-at-uni-heres-what-i-learned-afe36a99d309
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Q7IdllDE47WuWP-H
tags:
- name: kaggle
  slug: kaggle
- name: learning
  slug: learning
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
- name: university
  slug: university
seo_title: J'ai participé à une compétition Kaggle dans le cadre d'un projet de semestre
  à l'université. Voici ce que j'ai appris.
seo_desc: 'By Ane Berasategi

  It was my first competition and my first semester. I didn’t know what I was doing.


  _Photo by [Unsplash](https://unsplash.com/@miguel_photo?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Miguel Henriq...'
---

Par Ane Berasategi

C'était ma première compétition et mon premier semestre. Je ne savais pas ce que je faisais.

![Image](https://cdn-media-1.freecodecamp.org/images/9pu2uThG1h1G6Uasfc6HKW9SEEOuTNbYdcNv)
_Photo par [Unsplash](https://unsplash.com/@miguel_photo?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Miguel Henriques</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Voici l'histoire de comment j'ai décidé d'être créative dans un projet de semestre, comment mon choix initial de sujet a été écrasé et comment une compétition Kaggle de dernière minute a sauvé ma note.

Pour ce qui est de mon parcours personnel, j'ai étudié le génie des télécommunications, j'ai une certaine expérience en développement logiciel et en apprentissage automatique, mais je n'avais aucune idée du NLP à l'époque.

J'ai commencé mon master le semestre dernier et l'un des premiers cours auxquels j'ai assisté s'appelait « Classification et clustering » en NLP. Le professeur a expliqué les bases du traitement de texte pendant les premières semaines et ensuite chaque étudiant devait choisir un problème de classification ou de clustering en NLP, documenter la théorie, implémenter une solution et la présenter à la classe. L'implémentation pouvait être faite à la fin du semestre, pas immédiatement avec la présentation.

> J'étais nouvelle à l'université, alors j'ai décidé d'attendre et d'observer ce que les autres étudiants faisaient.

#### Choix du sujet

Très rapidement, les sujets des arbres de décision, de Naïve Bayes, des forêts aléatoires, des SVMs, de la régression logistique, etc., ont été choisis. Je connaissais à peine ces concepts, alors j'étais excitée à l'idée que mes pairs abordent ces sujets dans des présentations de 30 minutes, et je leur ai prêté toute mon attention et pris toutes les notes possibles.

Malheureusement, ces premières présentations étaient **purement théoriques**, car personne n'avait eu le temps d'implémenter quoi que ce soit si tôt dans le semestre. J'ai appris plus tard que la motivation derrière ces présentations précoces était l'urgence de « choisir un sujet facile avant que quelqu'un d'autre ne le prenne » et de « se débarrasser de la présentation », en reportant l'implémentation de l'algorithme à plus tard dans le semestre.

Autant j'ai essayé, je n'ai pas compris grand-chose aux présentations. J'ai besoin de visualiser les choses, de voir le code, de voir des exemples. Ce n'est pas facile pour moi de suivre une présentation remplie de notations et de formules mathématiques.

> Les semaines ont passé, le professeur a commencé à nous presser de choisir un sujet et de fixer une date pour la présentation, et je n'avais rien. J'ai attendu quelques présentations de plus avant de commencer à paniquer.

Les présentations suivantes étaient un peu plus avancées : LDA, LSI, perceptrons, réseaux de neurones, TensorFlow, Keras et plongements de mots, entre autres.

J'étais complètement ignorante sur certains sujets (LDA et LSI), mais je connaissais un peu de ML. Ces présentations incluaient du **code**, parfois même trop. Il y avait beaucoup de défilement et très peu de temps passé à analyser le code, l'accent était purement mis sur les résultats. J'ai appris les origines de TensorFlow et Keras, et je me suis sentie épuisée et confuse à la fin de chaque présentation. Autant j'avais essayé, je n'avais pas appris grand-chose.

> J'étais l'une des dernières étudiantes à choisir un sujet, et le professeur me regardait chaque fois qu'il mentionnait le « rappel amical ». J'ai compris le message.

J'ai essayé de penser rationnellement : il ne restait pas beaucoup de sujets évidents, et je voulais un sujet intéressant pour moi et pour les autres étudiants, où je pourrais tout mettre en pratique, pas seulement une structure de données ou un modèle de ML. Le cours valait 6 ECTS et je voulais utiliser ce temps pour produire quelque chose dont je pourrais être fière.

J'ai demandé à mon ami de chercher sur Google des problèmes de classification en NLP, et après quelques recherches, j'ai découvert l'**analyse de sentiment**. Cela regroupait tout magnifiquement, et j'avais mon sujet. J'ai vérifié si quelqu'un l'avait déjà choisi, personne ne l'avait fait, j'ai prévenu le professeur, il a dit « Enfin ! », et j'ai commencé à rassembler mes références. La roue était en mouvement.

La semaine suivante, lors d'un autre cours, un conférencier invité a donné une présentation très intéressante sur son mémoire de master, sur l'**analyse de sentiment**. Bien sûr. Mes camarades de classe et moi avons passé 90 minutes à apprendre à ce sujet, la motivation de son utilisation, les applications, le développement, le code, les résultats, _tout_. C'était un mémoire de master majestueux et une présentation très illustrative, et cela a ruiné ma présentation.

J'aurais encore pu faire mon projet sur le même sujet, mais tout le monde avait entendu le chercheur expérimenté parler de son mémoire de master pendant 90 minutes, il n'y avait aucun moyen que je puisse faire l'équivalent de son mémoire de master en quelques mois, alors j'ai décidé de continuer à chercher quelque chose d'unique, quelque chose que je pourrais présenter et que les gens diraient : « oooh ».

> À ce stade, le mode panique était activé.

Ma date de présentation était dans 2 mois, mon sujet génial n'existait plus, et j'avais besoin de quelque chose, rapidement. Je faisais défiler Twitter en essayant d'ignorer la pression quand j'ai vu que Kaggle annonçait leur toute nouvelle [**compétition de classification des questions insincères de Quora**](https://www.kaggle.com/c/quora-insincere-questions-classification/), et je me souviens avoir pensé :

* Quora ? J'aime Quora
* Questions insincères ? Cela semble amusant !
* Classification ? Cela pourrait être...

Je suis allée sur la page web, et c'était effectivement un problème de classification de texte. C'était comme si Kaggle m'avait vue me noyer et m'avait tendu une main secourable. Cette compétition pouvait résoudre tous mes problèmes.

![Image](https://cdn-media-1.freecodecamp.org/images/u9Ukm6X1wwRQ6aLue1jH8XrByi1scWr8z8CO)

1. Avais-je déjà participé à une compétition Kaggle ? J'ai fait quelques petits projets en ML mais jamais une compétition.
2. La compétition était-elle pour les débutants ? Non, elle était organisée par Quora avec de vrais prix, et des professionnels en compétition.
3. Avais-je la moindre idée de par où commencer ? Non, je n'en avais aucune.

Alors je me suis lancée. Faire ce projet serait faire quelque chose de complètement différent du reste de la classe, et bien sûr j'avais peur. Voici le dialogue mental que j'ai eu avec moi-même :

* Quel est le pire qui puisse arriver ?
* Le professeur pourrait refuser le sujet.
* D'accord, en supposant qu'il soit accepté, le pire ?
* Ne pas finir à temps, ne pas avoir quelque chose de complet à présenter.
* Juste, et si j'ai quelque chose de complet ?
* Cela pourrait être terrible, pire qu'une classification aléatoire.
* Cela serait effectivement mauvais.

Alors j'ai fixé mon objectif d'avoir quelque chose de terminé et idéalement avec un résultat décent en deux mois.

J'ai présenté l'idée avec enthousiasme au professeur, il a écouté, hoché la tête et dit : « Bien sûr, tu peux changer de sujet ». J'ai aussi entendu « si tu peux le faire » mais je suis quelque peu sûre que cette dernière partie venait de mon esprit et qu'il ne l'a pas vraiment dit.

J'allais faire la documentation et l'implémentation de ma soumission en même temps, alors je me suis mise au travail.

#### La compétition Kaggle

Puisque mes ambitions étaient modestes, je ne me suis pas soucieuse du syndrome de l'imposteur. J'ai fait une liste des kernels populaires sur le site, je les ai parcourus, compris, combinés, ajustés et j'ai fait le mien.

#### 1. EDA

La première chose à faire était l'analyse exploratoire des données (EDA). Avec le recul, j'ai passé beaucoup trop de temps à explorer les questions, mais à ma défense, je ne savais pas ce que je faisais, et certaines des questions insincères étaient drôles, je dois l'admettre. J'ai rassemblé toutes les questions que Quora classe comme insincères et j'en ai extrait certaines que je trouve personnellement drôles. [Vous pouvez les voir sur mon GitHub](https://github.com/anebz/kaggle/tree/master/quora_insincere_questions). Et vous pouvez voir mon [EDA sur Kaggle](https://www.kaggle.com/anebzt/quora-eda).

#### 2. Prétraitement

Les stratégies étaient un peu différentes dans le prétraitement, et cela a pris un peu plus de temps pour comprendre ce que les gens faisaient. J'ai appris à utiliser les plongements de mots, ajuster le texte d'entrée de sorte que la couverture du texte soit maximale et la quantité de mots inconnus soit minimale. J'étais assez fière de tout ce que j'ai appris sur le traitement de texte en si peu de temps.

J'ai utilisé Glove comme plongements pré-entraînés, la couverture du texte au début :

![Image](https://cdn-media-1.freecodecamp.org/images/MdCtirsEuSPJSJEbIyBEYKFxtsFPp6l5GKOJ)

Parmi tous les différents mots utilisés, 31,5 % sont reconnus par les plongements, et parmi tout le texte utilisé, 88 %. Il y a des mots plus fréquents que d'autres, comme « the », « a », etc. Ces 31,5 % du vocabulaire constituent jusqu'à 88 % du texte total.

Après avoir mis le texte en minuscules, développé les contractions et supprimé les caractères spéciaux et la ponctuation, la couverture est la suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/ZhXNxFC2JkSAWduggHBqRU9vt5TpLEo4PQRq)

Les mots hors vocabulaire (ceux non reconnus par les plongements) incluent les suivants, ainsi que leur fréquence :

![Image](https://cdn-media-1.freecodecamp.org/images/rG861sZlXpZO7nWxO5iT9Xq59PL9W1X7C-i3)

Vous pouvez voir mon [kernel de prétraitement sur Kaggle](https://www.kaggle.com/anebzt/quora-preprocessing-model).

#### 4. Le modèle

Ici, mes connaissances limitées en ML m'ont aidée à avancer un peu plus vite, le seul goulot d'étranglement était de décider quelle architecture utiliser. Les gens utilisaient des modèles allant des RNN aux LSTM en passant par BERT, ajoutant KFold, des taux d'apprentissage cycliques, des modèles bidirectionnels, quoi ?

Mon niveau de stress a augmenté, la date de présentation était dans deux semaines et je ne comprenais aucune des architectures. J'ai choisi la plus simple qui pouvait me donner un score décent, j'ai commencé avec une architecture LSTM.

J'ai tout connecté ensemble, et j'ai obtenu un résultat. Un résultat terrible, mais un résultat quand même. Mes besoins de base satisfaits, j'ai commencé à travailler sur la présentation tout en laissant l'ajustement du modèle comme activité de procrastination. Finalement, j'ai ajouté une couche d'Attention, et j'ai finalement transformé cela en un LSTM bidirectionnel. Le score était décent.

![Image](https://cdn-media-1.freecodecamp.org/images/RL7l3MyvHRdeMR3R40GoeCkDC1VVhr9GzwEQ)

L'architecture finale que j'ai utilisée, un BiLSTM avec une couche d'Attention. Il s'est entraîné assez rapidement et a donné un résultat relativement bon. Comme avant, vous pouvez voir [le kernel complet sur Kaggle](https://www.kaggle.com/anebzt/quora-preprocessing-model).

#### 5. La préparation

Pour la première fois de ma vie, j'avais trop de matériel pour ma présentation. J'ai dû en couper suffisamment pour tenir en 30 minutes, mais pas plus de peur de rendre mon discours trop général. Je devais montrer du code mais pas seulement du code, car selon mon expérience, il est difficile de se concentrer uniquement sur du code pendant une demi-heure.

J'ai passé les deux dernières semaines à documenter mon code, à ajouter toutes les références que j'avais utilisées, au cas où quelqu'un quelque part penserait que j'avais fait ce projet moi-même et que j'avais récupéré les informations de mon imagination.

> L'ouverture de Kaggle et la disponibilité de code public et bien documenté est l'un des plus grands incitatifs à utiliser Kaggle, à mon avis.

J'ai peaufiné ma présentation et je me suis entraînée avec des camarades de classe pour m'assurer que je ne parlais pas pendant plus de 30 minutes. Je l'ai fait, et ils m'ont donné des conseils pour réduire la répétition dans ce que je disais, en montrant dans les diapositives et en montrant à nouveau dans le code ; j'ai fait des transitions diapositive-code beaucoup plus simples en conséquence.

#### 6. La présentation

Pour ma présentation, j'ai uniquement utilisé des diapositives pour expliquer les spécificités de la compétition : motivation, définition du problème, données d'entrée, métriques, etc.

Pour l'EDA et le prétraitement, j'avais une diapositive expliquant ce que je montrerais dans le code, ensuite je suis passée au code, puis je suis revenue aux diapositives et j'ai montré un récapitulatif de ce que je venais de montrer. À la fin, j'ai inclus toutes les additions d'architecture de modèle avancées que je n'avais pas eu le temps de considérer.

La présentation s'est très bien passée, je n'ai parlé que pendant 30 minutes et il y a eu une discussion de suivi d'une autre demi-heure, où toute la classe a discuté de différentes stratégies pour classer les questions insincères. Le professeur a loué ma créativité et a dit qu'il envisagerait de changer la structure du semestre pour que plus d'étudiants fassent leurs projets similaires au mien.

Je considère cela comme un projet réussi !

#### 7. Conclusion

Puisque je ne savais pas ce que je faisais tout au long du projet, j'ai eu beaucoup de doutes, il est risqué de faire quelque chose de complètement opposé au reste de la classe, cela peut très bien se terminer ou terriblement.

J'ai appris que la créativité peut parfois être récompensée, et que les risques calculés valent la peine d'être pris. Dans ce cas, j'ai consulté le professeur avant de faire quoi que ce soit et il a approuvé, donc le risque était plus petit.

J'ai beaucoup appris en participant à la compétition Kaggle, j'ai obtenu un score dans le top 29 %, ce qui n'est pas si terrible ! Je suis assez fière de moi, considérant que c'était ma première compétition.

Si je peux dire quelque chose à retenir, c'est ceci :

> Si vous êtes à l'université ou dans un cours/programme, utilisez ce temps pour apprendre, expérimenter et vous mettre dans des situations où vous pourriez échouer, mais aussi réussir. Ma relation professionnelle avec le professeur s'est renforcée grâce à mon projet.

> Si vous pouvez vous permettre de faire plus que simplement compléter le sujet, envisagez d'aller au-delà de ce que dit le professeur. Lisez les références, faites des recherches en ligne, proposez des sujets. Qui sait où votre initiative pourrait vous mener.

> Et enfin, **vous n'avez pas à faire exactement ce que les autres étudiants font**. Juste parce que tout le monde suit une certaine structure ou un format de soumission ne signifie pas que c'est le bon. Parlez au professeur ou aux assistants d'enseignement, demandez aux étudiants qui ont eu le cours l'année précédente, puis décidez consciemment de la manière dont vous voulez aborder le sujet.

J'espère que vous avez aimé mon histoire ! Si vous voulez en savoir plus ou me contacter de quelque manière que ce soit, vous pouvez me joindre [sur Twitter](https://twitter.com/aberasategi).