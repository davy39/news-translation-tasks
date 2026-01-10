---
title: 'Un guide du scientifique des données pour le bonheur : les découvertes des
  expériences heureuses de 10 000+ humains'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-23T22:53:44.000Z'
originalURL: https://freecodecamp.org/news/a-data-scientists-guide-to-happiness-findings-from-the-happy-experiences-of-10-000-humans-fc02b5c8cbc1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*EsFDmp-QfBLa0vBf.png
tags:
- name: Data Science
  slug: data-science
- name: Happiness
  slug: happiness
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: topic modeling
  slug: topic-modeling
seo_title: 'Un guide du scientifique des données pour le bonheur : les découvertes
  des expériences heureuses de 10 000+ humains'
seo_desc: 'By Jordan Rohrlich

  Modern life throws a lot at us. We often find ourself struggling to manage anxiety,
  wrangle responsibilities, adapt to new conditions, and maintain a happy state of
  mind.

  But happiness is a noisy space these days. Self help books, ...'
---

Par Jordan Rohrlich

La vie moderne nous lance beaucoup de défis. Nous nous retrouvons souvent à lutter pour gérer l'anxiété, dompter les responsabilités, nous adapter à de nouvelles conditions et maintenir un état d'esprit heureux.

Mais le bonheur est un domaine bruyant ces jours-ci. Les livres de développement personnel, les articles, les blogs et les applications de méditation ne peuvent pas aider tout le monde, et augmentent souvent le fardeau mental nécessaire pour rester content. C'est un problème sérieux. Ainsi, alors que la santé mentale devient de plus en plus vulnérable et que les solutions deviennent de plus en plus complexes, il est important de s'ancrer aux fondamentaux. **C'est-à-dire, nous devons recentrer nos vies quotidiennes sur les choses ordinaires qui rendent les gens heureux.**

### Données

Cette recherche plonge dans un ensemble de données pratique qui peut aider à éclairer les fondamentaux du bonheur. [HappyDB](https://github.com/rit-public/HappyDB) est un ensemble de 100 000+ expériences heureuses recueillies via Amazon Mechanical Turk de mars à juin 2017. Il contient les expériences et les données démographiques de dizaines de milliers de contributeurs du monde entier. Intéressamment, certaines méthodes d'analyse de texte de base peuvent nous aider à apprendre beaucoup de ces données.

En comprenant l'intensité émotionnelle et les motifs de mots-clés tirés de ces expériences heureuses, HappyDB nous enseigne deux leçons précieuses.

Vous pouvez consulter le code vous-même sur [GitHub](https://github.com/jrohrlich/DSGuideToHappy).

### 1. Le bonheur n'est pas conditionné par la démographie.

Cela est contre-intuitif.

La plupart d'entre nous ressentent un effet de "l'herbe est toujours plus verte" en ce qui concerne le bonheur. Les jeunes anticipent une carrière et une famille heureuses plus tard dans la vie. Les personnes âgées se remémorent une époque où elles étaient jeunes et aventureuses. Les célibataires aspirent à la compagnie. Les couples espèrent avoir des enfants.

Et, malgré le fait de le savoir, nous pensons tous que quelqu'un d'autre est plus heureux, ou qu'une autre étape de notre vie nous apportera plus de joie. Examinons les données.

L'[analyse de sentiment](https://web.stanford.edu/class/cs124/lec/sentiment.pdf) pèse l'intensité émotionnelle d'un texte. En utilisant un package R appelé "Syuzhet", j'ai mesuré le sentiment de ces expériences heureuses pour déterminer comment leurs intensités varient. Cela a créé un spectre d'expériences heureuses qui pourraient être décomposées par groupes démographiques spécifiques :

![Image](https://cdn-media-1.freecodecamp.org/images/vtSR9KdR4zPHMmWcHn7v1MPvZ640dX8VRe6M)
_Sentiment des expériences heureuses (par genre, statut familial)_

![Image](https://cdn-media-1.freecodecamp.org/images/dBKgVGpc2rWvemRIUZryNLznFVUVlxWVRHuK)
_Sentiment des expériences heureuses (par groupe d'âge)_

Assez surprenant, il y a peu de changement dans la répartition des expériences heureuses à travers ces groupes démographiques de genre, famille et âge. Voici les points saillants :

* Globalement, les expériences sont définitivement positives. Mais le quartile inférieur a un sentiment négatif (certaines choses heureuses naissent poétiquement de l'inconfort et de la tragédie)
* Les distributions ont des queues de haute intensité et des bornes inférieures assez limitées — certaines expériences sont extrêmement positives, et peu sont frappantes négatives
* Les femmes s'identifiant elles-mêmes ont des scores de sentiment légèrement plus élevés que les hommes pour la plupart de leurs expériences (une différence de 0,05 à 0,1 point)
* Les parents mariés ont des scores de sentiment légèrement plus élevés que les célibataires et les couples sans enfants pour la plupart de leurs expériences (une différence de 0,05 à 0,1 point)
* Les quartiles des expériences heureuses (25e, 50e et 75e percentiles) à travers les groupes d'âge sont virtuellement identiques

**En somme, il n'y a pas de différence significative dans la gamme des expériences heureuses rapportées par différentes démographies.** Bien que les femmes et les parents tendent à avoir marginalement plus d'expériences heureuses à enregistrer, les différences sur l'échelle de sentiment ne peuvent pas être prises au sérieux — elles correspondent à une fraction d'une fraction d'un seul mot heureux par expérience enregistrée. C'est une différence minuscule.

Cependant, cet ensemble de données n'inclut aucun champ de données pour la race, le statut socio-économique ou d'autres positions d'identité qui peuvent influencer matériellement les expériences quotidiennes. Les futures recherches sur le bonheur devraient inspecter ces relations de près.

### 2. Le bonheur est déterminé par des types spécifiques d'expériences.

Il est facile de penser au bonheur comme une substance mystérieuse et éthérée qui pénètre nos expériences de manière incompréhensible. Cette vision prône une compréhension métaphysique du bonheur comme quelque chose au-delà de la compréhension humaine.

Mais ce n'est pas très utile, surtout pour les personnes qui comptent sur des expériences heureuses et significatives comme la bouée de sauvetage de leur santé mentale.

Entrez la Modélisation de Sujets. Cette méthode d'analyse de texte (expliquée [ici](http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/) ; j'utilise le package "Mallet" de R) fournit une approche constructive pour expliquer ce que les 10 000+ participants de HappyDB trouvent être des expériences heureuses.

En segmentant l'ensemble de données en documents des expériences de chaque répondant, puis en exécutant un modèle de sujet LDA pour identifier des groupes de mots-clés couramment utilisés, nous pouvons commencer à isoler des types distincts d'expériences qui nous rendent heureux. Les sujets et les mots-clés associés peuvent être vus ci-dessous, dans aucun ordre particulier :

![Image](https://cdn-media-1.freecodecamp.org/images/bSlgdQrleybiwhVeNzAzevuLqtRXteuIFEpQ)
_Sortie du Modèle de Sujet de 100 922 Expériences Heureuses_

#### **Temps en famille**

Cela semble évident. Des mots comme "fille", "fils", "mari", "bébé", "femme" et "temps" semblent montrer que beaucoup de gens réfléchissent très positivement aux expériences qui impliquent leurs proches. Ces expériences impliquent souvent des cadres des plus communs et tirent le bonheur simplement de la compagnie et de l'affection.

Essayez de passer plus de temps avec vos proches : appelez votre mère, allez au match de football de votre enfant. Cela pourrait payer plus que vous ne le pensez.

#### **Être payé**

Bien que les gens n'aiment pas penser que l'argent est lié au bonheur, leurs expériences disent le contraire. Recevoir un salaire, solder un solde de carte de crédit ou donner de l'argent à un ami peut rendre les gens vraiment heureux. Et le sentiment d'accomplissement et de sécurité économique qui en découle expliquerait certainement pourquoi.

#### **Nourriture**

Les gens adorent manger. Cuisiner un repas préféré, manger au restaurant avec des amis ou se gaver d'une pinte de crème glacée devant la télévision peuvent tous rendre quelqu'un heureux. Une bonne nourriture avec des amis devrait définitivement faire partie d'un mode de vie heureux.

#### **Temps de sommeil**

Étonnamment, les gens documentent beaucoup d'expériences heureuses autour du sommeil : se blottir dans son lit, s'endormir avec un ami à fourrure, se réveiller à une nouvelle journée prometteuse, et ainsi de suite. Il y a beaucoup de choses à rendre heureux, si l'on prend un moment pour réfléchir la nuit après une journée productive, ou le matin motivé avant quelque chose d'excitant.

#### **Jeux et compétition**

Les humains sont compétitifs. Ils adorent jouer à des jeux vidéo, regarder des sports et faire d'autres choses qui stimulent leur instinct biologique de dominer. Jouez à un jeu de société avec des amis ou excitez-vous pour votre équipe sportive locale. Il y a de fortes chances que vous soyez heureux de l'avoir fait.

#### **Réussite et éducation**

Après des semaines de travail, c'est génial de terminer de grandes entreprises. Terminer une classe, obtenir son diplôme de l'école ou lancer un projet peuvent tous sérieusement améliorer l'humeur d'une personne. Mais terminer de grandes entreprises nécessite d'en commencer quelques-unes, alors sortez et commencez quelque chose de nouveau ! L'apprentissage et le faire sont généreusement récompensés.

#### **Célébrations et anniversaires**

Évidemment, les célébrations rendent les gens heureux (pensez aux anniversaires, aux anniversaires de mariage et aux amisgivings). Les gens aiment trouver une raison — peu importe son importance ou sa stupidité — pour se retrouver avec leurs proches, être heureux à propos d'une occasion et faire quelque chose pour briser une routine hebdomadaire terne.

#### **Équilibre mental et introspection**

L'acte de se connecter à son état mental semble apporter beaucoup de bonheur en soi. Réfléchir de manière introspective à son bien-être, à son espace mental et à son bonheur semble avoir des effets positifs sur ces mêmes choses ! Essayez de méditer, de réfléchir sur des expériences heureuses ou simplement d'être conscient de votre état mental — cela pourrait être la chose même pour aider à le stimuler.

#### **Dépenses**

Satisfaire nos désirs matériels, bien sûr, apporte beaucoup de bonheur aux gens. Trouver de bonnes affaires, enfin acheter cette voiture ou cette maison, et obtenir quelque chose de bien pour soi-même ou un proche créent toutes une sorte de bonheur. Profitez de manière responsable.

#### **Voyages de week-end**

Les gens aiment être hors du travail, mais en profitent beaucoup plus s'ils sont en bonne compagnie, tout en faisant quelque chose de différent. Partez en voyage quelque part, faites une sortie à proximité ou trouvez une autre excuse novatrice pour passer du temps avec d'autres personnes dans de nouveaux décors. Les données disent que vous ne le regretterez certainement pas.

#### **Lecture et musique**

Que ce soit en s'emmitouflant à la maison avec un nouveau livre ou en découvrant une chanson lors du trajet en bus à la maison, beaucoup de gens deviennent heureux grâce au simple acte de lire ou d'écouter. Prendre une heure avant de se coucher pour lire quelque chose de nouveau ou parcourir Discover Weekly vaut probablement l'investissement en temps.

#### **Décisions**

Les décisions figurent également parmi les grandes activités génératrices de bonheur. C'est excitant de passer du temps à réfléchir à un grand changement, de décider de faire quelque chose de nouveau et d'en parler aux gens. Cela laisse un regain d'humeur persistant pour beaucoup de gens, aussi. Alors faites un changement que vous avez eu l'intention de faire depuis un moment ; et engagez-vous !

### Conclusion

Ces douze catégories d'expériences représentent les fondements du bonheur quotidien pour des dizaines de milliers de personnes. Étant donné que les humains se ressemblent plus que nous ne leur en donnons souvent crédit, il en va probablement de même pour vous.

Cette méthode, comme toute autre, est imparfaite. Certaines démographies contribuent plus lourdement que d'autres, ce qui peut introduire des mots curieux dans certains sujets, ou peut biaiser les sujets qui sont représentés dans le modèle. Les données textuelles sont désordonnées et les gens ne pensent pas non plus au bonheur en catégories d'expériences clairement définies.

Mais, en utilisant ces deux leçons comme une structure de base pour comprendre la positivité dans nos vies quotidiennes, je pense que cela peut nous aider à nous rappeler que le bonheur n'est jamais aussi loin que nous pourrions le penser.

Nous savons déjà que beaucoup de ces sujets heureux sont vrais à un certain niveau. Mais nous reconnaissons rarement le pouvoir qu'ils ont sur notre humeur, et donc nous ne les structurons pas dans nos vies quotidiennes aussi facilement que nous le devrions.

Ces catégories sont des stimulants d'humeur certifiés empiriquement. Ce sont des dunks de bonheur.

Alors nous devrions prendre ce que nous pouvons obtenir. Jetez les manuels de développement personnel et concentrez-vous sur de vraies expériences heureuses. Vous pourriez aimer ce que vous trouvez.

*Si vous avez trouvé cet article utile, partagez-le avec un ami ou donnez quelques applaudissements ?.*

Voir le code vous-même sur [GitHub](https://github.com/jrohrlich/DSGuideToHappy) !