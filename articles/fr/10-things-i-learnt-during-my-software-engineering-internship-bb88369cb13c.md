---
title: Ce que j'ai appris pendant mon stage en ingénierie logicielle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-02T03:21:01.000Z'
originalURL: https://freecodecamp.org/news/10-things-i-learnt-during-my-software-engineering-internship-bb88369cb13c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ixrHjysR8zRWlp9gBvroYQ.jpeg
tags:
- name: internships
  slug: internships
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Ce que j'ai appris pendant mon stage en ingénierie logicielle
seo_desc: 'By Carmen Chung

  As part of my coding bootcamp at Coder Academy, I was placed as a software engineering
  intern at Valiant Finance, winner of the Australian Fintech Start Up of the Year
  (2017) Award. In the four weeks I have been here, I have made more...'
---

Par Carmen Chung

Dans le cadre de mon bootcamp de codage à [Coder Academy](https://coderacademy.edu.au/), j'ai été placée en tant que stagiaire en ingénierie logicielle chez [Valiant Finance](https://valiant.finance/), lauréat du prix Australian [Fintech](http://fintechawards.net/) Start Up de l'Année (2017). En quatre semaines, j'ai fait plus de découvertes intellectuelles que je ne peux en compter : tout cela grâce au mentorat incroyable et à la patience de l'équipe avec laquelle j'ai travaillé.

Voici les 10 choses principales que j'ai apprises pendant mon stage, divisées en leçons techniques et non techniques.

### TECHNIQUE

#### **Soyez méticuleux**

Ayant été avocate d'entreprise pendant sept ans, j'ai toujours été fière de mon attention aux détails. Mais les erreurs arrivent.

Lors de la troisième semaine de mon stage, j'ai appuyé sur Ctrl + F pour trouver un mot que je cherchais dans mon fichier. Ensuite, j'ai dû appuyer accidentellement sur la barre d'espace, supprimant ainsi le mot entièrement.

À ma grande honte, je n'ai pas remarqué que je l'avais fait. C'était quelque chose qui n'aurait pas provoqué une erreur évidente — sinon nos tests l'auraient détectée. Plutôt, cela serait passé inaperçu et aurait "échoué silencieusement"… si ce n'avait été pour les yeux perçants de notre cofondateur, Ritchie.

Pour éviter de faire mon erreur, consultez GitHub Desktop. Il affiche toutes les modifications que vous avez apportées à un fichier et vous permet de les examiner ligne par ligne, une dernière fois avant de valider. Il est facile de sauter cette partie. Mais prendre le temps de revoir vos modifications une dernière fois **avant de valider/pousser** peut vous éviter des maux de tête sérieux — et des embarrassements — plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/GvfEtzAo27YBQbS5jspK6k9qyUOsEApsqe1n)
_Ne soyez pas Velma !_

Je ne peux pas assez insister sur l'importance de **l'attention aux détails**. Un point-virgule manquant dans certains langages peut arrêter votre code net. D'autres choses sont moins insidieuses, mais toujours ennuyeuses.

Même des choses simples comme vérifier les commits Git de votre entreprise pour voir comment ils sont écrits — par exemple, nous utilisons un émoticône spécifié pour indiquer ce que le commit est, nous mettons en majuscule le premier mot du commit, nous utilisons le présent, et nous n'ajoutons pas de ponctuation à la fin — vous évitent d'irriter vos collègues lorsque vous vous écartez du chemin de la cohérence.

#### **Prenez des notes (et étudiez dur)**

Oubliez la Fontaine de la Connaissance.

Presque tous les jours où j'ai été chez Valiant Finance, j'ai eu l'impression de boire à un tuyau d'incendie. La quantité de connaissances et de sagesse qui sort de la bouche de notre Directeur de l'Ingénierie ([Kris Hofer](https://twitter.com/krishofer)) et de notre cofondateur ([Ritchie Cotton](https://twitter.com/ritchie__c)) est suffisante pour faire tourner la tête de n'importe qui. À mon grand soulagement, ces deux gars sont très structurés et patients dans leur façon d'enseigner, donc tout se met en place de manière ordonnée.

Ils se mettent en place plus rapidement, cependant, si vous prenez des notes.

J'ai un cahier organisé avec des titres et une table des matières pour m'aider à garder une trace de tout ce que j'ai appris. Les morceaux de code que j'utilise fréquemment sont surlignés, et j'ai des onglets en laiton pour les sections que j'utilise souvent.

![Image](https://cdn-media-1.freecodecamp.org/images/OKEnsvJjZ4ktK7HNBURVSXJyADkEjTADEY5E)

En plus de cela, j'ai un planificateur hebdomadaire où je note toutes les tâches que nous devons accomplir chaque jour, et un cahier sans lignes pour dessiner des organigrammes — pour une logique de programmation plus compliquée — et des maquettes.

Plus important encore, j'écris une liste de toutes les choses que Ritchie et Kris mentionnent et que je sais que je devrai approfondir par moi-même.

![Image](https://cdn-media-1.freecodecamp.org/images/EN6SMceBtwLodxTu8aqoch-5YzNJdTawTbiz)

#### **Ne réinventez pas la roue**

L'une des choses que j'ai découvertes était que Ritchie avait mis en place un système CSS incroyable, avec ses propres feuilles de style entièrement personnalisées (en utilisant la [méthode BEM](http://getbem.com/introduction/)) — et un guide de style qui ferait chanter le cœur de tout amateur de documentation.

Avant de me familiariser avec le système, j'ai été tentée de créer certaines classes CSS que je pensais faciles à accéder et à appliquer. Ce que j'ai fini par réaliser et respecter, c'est qu'il n'y avait pratiquement aucun besoin pour moi de le faire. Dans presque tous les cas, il existait déjà un ensemble de styles clairs et flexibles que je pouvais échanger — comme des pièces de Lego interchangeables — tous à portée de main. En créant des classes de style inutiles, je serais en train d'encombrer un système structuré et propre, le rendant plus difficile à naviguer plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/1KtLKQWsMC21g-NpM5f4zVqAvxpvNNWnbTbh)
_Si vous avez de grandes pièces de Lego, ne les refaites pas. Concentrez-vous plutôt sur la création de choses avec elles._

#### **Évitez la verbosité**

L'un des principes clés de Ruby on Rails est DRY (Don't Repeat Yourself). C'est quelque chose qui a été inculqué aux développeurs Rails juniors dès le premier jour… mais oh, comme la lutte est réelle.

Mon collègue stagiaire et moi avions pour tâche de créer un code qui compterait le nombre de personnes qu'un utilisateur avait référées à la plateforme. Pour chaque trois références, l'utilisateur recevait 50 $. La logique était gérable, mais ce que nous avons découvert, c'est que nous devions tenir compte d'un **ami** contre **plusieurs amis** lors de l'affichage du résultat.

Voici comment notre code est initialement sorti :

```
- if @invite_count == 1
 %p
 Vous avez invité 1 ami à faire partie de Valiant Finance.
 — if @invite_count > 1
 %p
 Vous avez invité
 %strong #{@invite_count} amis
 à faire partie de Valiant Finance !
 
- if (@invite_count % 3) == 0 || (@invite_count % 3) == 1
 %p
 Invitez un autre
 %strong #{3 — (@invite_count % 3)} amis
 pour recevoir 50 $ !
 — if (@invite_count % 3) == 2
 %p
 Invitez un autre
 %strong ami
 pour recevoir 50 $ !
```

Quand j'ai montré cela à Ritchie, il nous a dit de regarder [pluralize](https://apidock.com/rails/ActionView/Helpers/TextHelper/pluralize).

Esprit.   
Soufflé.

Voici comment notre code est sorti ensuite :

```
%p Vous avez invité #{@invite_count} #{"ami".pluralize(@invite_count)} à faire partie de Valiant Finance.
 %p
 Invitez un autre
 %strong #{3 — (@invite_count % 3)} #{"ami".pluralize(3 — (@invite_count % 3))}
 pour recevoir 50 $ !
 %p
```

#### **Soyez conscient des intrications de votre langage de programmation**

Un certain nombre de développeurs web juniors utilisent certains termes de manière interchangeable sans être conscients qu'il existe des différences — parfois minimes, parfois pas si minimes ! — entre eux. Je suis coupable de souvent chercher sur Google les différences entre `.present?`, `.exists?`, et `.any?` ; et `.empty?`, `.nil?`, et `.blank?`. D'autant plus embarrassant que `.exists?` a [en fait été déprécié](https://apidock.com/rails/ActiveRecord/Base/exists%3F/class). Oups.

![Image](https://cdn-media-1.freecodecamp.org/images/fMyJ-tJVWuLl263uB8Njy7GGPo-wqOq4uInh)
_Il semble que je ne suis pas la seule à oublier cela._

Parfois, les intrications sont presque imperceptibles — lors de la première semaine de mon stage, je tapais `Product.all.map(&:name)`. Mais on m'a ensuite appris que je pouvais simplement utiliser `Product.pluck(:name)`. Il **y a** une différence entre les deux en termes d'efficacité — à la fois en ce qui concerne le fait que je le tape réellement, et en termes de vitesse de recherche. Pour plus d'informations, consultez cet [article](https://rubyinrails.com/2014/06/05/rails-pluck-vs-select-map-collect/).

Essayez de découvrir les différentes façons dont les choses peuvent être faites dans votre langage de programmation — et s'il y a plus d'une façon, voyez si vous pouvez apprendre les différences entre elles.

**Conseil de pro** : Demander les différences entre certaines fonctions/méthodes/requêtes est également un passe-temps favori des intervieweurs techniques, alors étudiez bien.

### NON-TECHNIQUE

#### **Impliquez-vous dans l'entreprise**

Cela semble simple, n'est-ce pas ? Mais lorsque vous jonglez avec de nombreuses tâches et essayez de vous orienter dans une nouvelle entreprise, il est facile d'oublier les petites choses qui comptent pour les personnes qui vous entourent.

Dès notre premier jour dans l'entreprise, l'autre stagiaire et moi avons été encouragés à nous inscrire sur Twitter. Dans le train pour aller travailler le lendemain matin, j'ai dûment créé un compte et j'ai suivi le compte de notre entreprise, ainsi que les comptes de quelques collègues.

Étant donné que j'ai déjà plusieurs comptes de réseaux sociaux, j'étais initialement réticente à en ajouter un autre. Mais cela s'est avéré vraiment bénéfique.

J'ai pu me tenir au courant des nouvelles de l'entreprise ainsi que des nouvelles des partenaires clés, et consulter des tweets intéressants de mes collègues. J'ai tweeté des publications sur les événements de l'entreprise et les nouvelles fonctionnalités des produits sur lesquels notre équipe travaille. C'est une façon facile de s'impliquer et cela montre que vous vous souciez vraiment de l'endroit où vous travaillez.

![Image](https://cdn-media-1.freecodecamp.org/images/mwVLN-X2SDvnji3xpv3z8EpxYtiWSR64kHPz)
_La fierté de Valiant Finance en compétition lors de notre compétition interne des Jeux Olympiques d'Hiver._

#### **Posez des questions — mais plus important encore, écoutez**

Kris, notre Directeur de l'Ingénierie, nous a très gentiment dit qu'« il n'y a pas de questions stupides », et que nous sommes encouragés à poser tout ce qui nous passe par la tête.

Moi, en revanche, je crois fermement qu'il existe des questions stupides. Habituellement, celles-ci se produisent lorsque vous n'avez tout simplement pas prêté attention, ou lorsque vous êtes trop paresseux pour réfléchir par vous-même à ce qui a été dit. Poser des questions est important, en particulier lorsque vous ne comprenez vraiment pas quelque chose. Mais écouter les réponses est encore plus important.

Prenez le temps d'écouter ce qui est dit et réfléchissez-y. C'est dans la nature humaine d'entendre les mots sortir de la bouche de quelqu'un d'autre et de commencer à préparer mentalement une réponse pendant qu'il parle. Ne le faites pas. **Prêtez attention à ce qu'on vous dit.**

![Image](https://cdn-media-1.freecodecamp.org/images/bmtPk9Pbivm-7qSGtuQdaDQL9ccnsPumPvvm)
_Ne soyez pas ce petit gars (sauf si vous êtes vraiment, vraiment mignon)_

#### **Sachez à qui parler**

L'une des grandes choses de ce stage était que nous étions encouragés à contacter les membres d'autres équipes pour discuter des fonctionnalités produits qu'ils voulaient et de la manière dont nous pourrions les implémenter. Nous avons appris à nous en remettre à leur expertise à certains égards, et au jugement de notre équipe Produit à d'autres.

Par exemple, nous avions pour tâche de construire les onglets du tableau de bord du courtier afin que les prospects qui ont été soumis par un courtier soient soigneusement divisés en Actifs, Inactifs et Réglés. En outre, nous avons créé une carte de lien de parrainage — comme mentionné précédemment.

Ces deux tâches nécessitaient de collaborer avec le Directeur des Partenariats Tiers afin que la fonctionnalité et le langage de la fonctionnalité soient adaptés au public des courtiers.

![Image](https://cdn-media-1.freecodecamp.org/images/v-bU8hOaVzLyGgSnS833fOm42Pmq83VYI8Xj)
_Nous avons travaillé avec le Directeur des Partenariats Tiers pour produire les onglets du tableau de bord réactif et la fonctionnalité Parrainer un Courtier_

Cela dit, il y avait des moments où nous essayions de construire quelque chose qui suscitait un grand intérêt de la part de plusieurs personnes dans l'entreprise — ce qui entraînait des retours (parfois contradictoires). À des moments comme ceux-ci, nous nous en remettions à nos responsables d'équipe Produit, qui nous donnaient des conseils — et tout aussi important — intervenaient en tant que tampon si le bruit des autres équipes devenait trop fort.

N'ayez pas peur de demander de l'aide à vos superviseurs dans ces cas — ils sont généralement mieux équipés et plus expérimentés pour dire aux autres équipes que ce qu'ils demandent est utterelement ridiculeus va prendre un peu plus de temps que prévu à implémenter et que, parce que c'est utterelement ridiculeus pas critique pour l'entreprise, cela sera ajouté à la utterelement ridiculeus liste liste des choses à faire des développeurs.

#### **Restez humble**

Parce qu'il y a tant de façons d'écorcher un chat dans le monde du développement, il est facile de se laisser emporter par une certaine façon de faire les choses et de supposer que votre façon est meilleure que celle de tout le monde.

Ne vous méprenez pas — il y a des meilleures pratiques, et il y a, sans aucun doute, de bonnes règles que chaque entreprise suit afin d'assurer la cohérence du code. Mais ne rejetez pas ce que les autres ont fait simplement parce que cela ne correspond pas à ce à quoi vous êtes habitué. Cela peut (ou non) être même mieux que votre code.

![Image](https://cdn-media-1.freecodecamp.org/images/lTZTI-yEgrBVvADz7t0hRPwJqNCY6UO2jFos)
_Ne soyez pas ce gars non plus (sauf si vous plaisantez)_

Sur ce point : lorsque vous avez fait une erreur, sachez qu'il est temps de manger de l'humilité.

Avouez-la, présentez vos excuses, apprenez de l'erreur et essayez de ne pas la laisser vous ronger. La dernière partie est la plus difficile pour moi. J'ai fait des cauchemars pendant une semaine après l'erreur de suppression mentionnée au début.

#### **Amusez-vous**

Chez Valiant Finance, nous célébrons les victoires. Nous avons un canal Slack entier dédié à nous encourager mutuellement dans nos efforts professionnels et personnels.

Nous faisons des activités de consolidation d'équipe, nous avons des peluches et des chiens au bureau, et nous faisons des apéros informels le vendredi soir.

![Image](https://cdn-media-1.freecodecamp.org/images/eC7CQ2oLtetN05tbXWDARyzdjAdEm4xn-ZPO)
_Le colis de bienvenue que nous avons reçu le premier jour du stage_

Cela semble évident, mais les gens veulent travailler autour de personnes heureuses. Bien que vous ne soyez pas là pour vous faire des amis de beuverie dans votre entreprise de stage (des points bonus si vous le faites, cependant !), vous voulez profiter de votre temps là-bas — et l'entreprise devrait vouloir que vous le fassiez aussi. Le but de tout le stage est d'essayer de voir si vous êtes un bon ajustement pour l'entreprise — et vice versa.

Essayez de profiter de votre stage — mais si ce sur quoi vous travaillez est fastidieux et monotone, essayez d'en faire un jeu. Je suis une connaisseuse chevronnée pour rendre le travail ennuyeux amusant — peut-être quelque chose que j'approfondirai dans un autre article.

Si vous êtes malheureux en tant que stagiaire, il y a des chances que vous soyez malheureux en tant qu'employé à temps plein.

Et personne ne veut cela.

Un grand merci à notre cofondateur Ritchie Cotton et au Directeur de l'Ingénierie Kris Hofer pour leur patience incroyable, leur mentorat et leurs connaissances tout au long de mon stage chez Valiant Finance. Je n'aurais jamais imaginé apprendre autant en si peu de temps — ou m'amuser autant à le faire. Merci les gars.

Suivez-moi sur [Twitter](https://twitter.com/carmenhchung).