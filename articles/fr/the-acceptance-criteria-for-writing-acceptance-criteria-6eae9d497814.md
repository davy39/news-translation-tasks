---
title: Les Critères d'Acceptation pour la Rédaction des Critères d'Acceptation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-06T18:25:31.000Z'
originalURL: https://freecodecamp.org/news/the-acceptance-criteria-for-writing-acceptance-criteria-6eae9d497814
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eRFNul714YcZ-LcdQARm2Q.jpeg
tags:
- name: agile
  slug: agile
- name: kanban
  slug: kanban
- name: project management
  slug: project-management
- name: Scrum
  slug: scrum
- name: 'tech '
  slug: tech
seo_title: Les Critères d'Acceptation pour la Rédaction des Critères d'Acceptation
seo_desc: 'By Elijah Valenciano

  Many development teams are too familiar with the frustrations of unsatisfactory
  acceptance criteria or even the lack of criteria itself. Defining no requirements
  is like preparing for battle without a plan of action — the team ha...'
---

Par Elijah Valenciano

De nombreuses équipes de développement sont trop familières avec les frustrations des critères d'acceptation insatisfaisants ou même l'absence de critères. Ne définir aucune exigence revient à se préparer pour une bataille sans plan d'action — l'équipe a fait plus de pas vers l'échec que vers le succès. Je propose des suggestions spécifiques pour la rédaction de critères d'acceptation qui peuvent améliorer tout processus agile.

Tout d'abord, définissons rapidement les critères d'acceptation.

> Les critères d'acceptation sont les « conditions qu'un produit logiciel doit satisfaire pour être accepté par un utilisateur, un client ou d'autres parties prenantes. » (Microsoft Press)

Assez simple, n'est-ce pas ? Pas tout à fait. À ce stade, je me demanderais si c'est là que s'arrête ma définition des critères d'acceptation. En plus de la définition ci-dessus, tout propriétaire de produit devrait avoir des réponses prêtes pour les questions suivantes :

> À quoi ressemblent ces conditions ? Qui crée ces conditions ? Combien de conditions devrait-il y avoir ? Comment les résultats sont-ils mesurés ?

Généralement, les critères d'acceptation sont initiés par le propriétaire du produit ou la partie prenante. Ils sont rédigés avant tout développement de la fonctionnalité. Leur rôle est de fournir des directives pour une perspective centrée sur l'entreprise ou l'utilisateur.

**Cependant, la rédaction des critères n'est pas uniquement de la responsabilité du propriétaire du produit. Les critères d'acceptation doivent être développés comme un effort conjoint entre l'équipe de développement et le propriétaire du produit.**

Élaborer ces critères ensemble aide l'équipe de développement à comprendre la fonctionnalité souhaitée. Cela aide également le propriétaire du produit à repérer les détails manquants. De plus, le propriétaire acquiert une meilleure compréhension de la faisabilité, de la complexité et de la portée.

![Image](https://cdn-media-1.freecodecamp.org/images/Hzk0Rmb3UArySx-mxJXWBxlajmYZiNQ9rTyr)
_Image par [Maryna Z. & Dmiriy G](https://rubygarage.org/blog/clear-acceptance-criteria-and-why-its-important" rel="noopener" target="_blank" title=")._

### Formater les critères d'acceptation

Les critères peuvent être rédigés dans une variété de formats. La plupart des équipes penchent vers deux types spécifiques : **orientés règles** ou **orientés scénarios**.

Les exigences orientées règles sont simples. Elles listent les résultats observables. « Afficher le solde du relevé après une authentification réussie. »

D'autre part, les critères orientés scénarios tendent à suivre le modèle « Étant donné…Quand…Alors… ». Cela a été dérivé du développement piloté par le comportement (BDD). Cette exigence décrit le résultat observable attendu. Cela se produit _quand_ une action particulière est exécutée _étant donné_ un certain contexte.

### **3 caractéristiques des critères d'acceptation efficaces**

#### **1. Testables avec des résultats de réussite/échec clairement définis**

Avoir des critères testables. Cela permet aux testeurs de confirmer correctement que toutes les conditions souhaitées ont été remplies. Si les critères n'étaient pas testables, il n'y aurait aucun moyen de vérification. Ces critères doivent soit être remplis, soit ne pas l'être. Un développeur doit savoir à quel moment le critère a été atteint. Toute ambiguïté peut prolonger l'effort sur l'histoire.

Par exemple, un critère d'acceptation stipule « augmenter le nombre d'entrées disponibles dans un menu déroulant ». Le développeur ne saurait pas combien de nouvelles entrées ajouter et pourrait prendre la liberté de supposer un nombre basé sur son expérience avec le produit. De même, un testeur manuel pourrait prendre la même liberté et supposer une définition différente d'augmentation. Cela entraîne une confusion qui reviendra au propriétaire du produit.

#### 2. Non ambigus et concis

C'est là que la rédaction des critères d'acceptation devient un art. Les essais académiques soulignent l'importance de la clarté et de la concision. De même, la rédaction des critères d'acceptation exige le même niveau d'organisation et de soin.

Similaire à l'écriture d'une pièce littéraire, le public doit être gardé à l'esprit. Ceux qui lisent les critères d'acceptation doivent comprendre ce qui est écrit. Sinon, ces mots sont complètement inutiles. S'ils sont longs et remplis de jargon, les points principaux des conditions décrites peuvent ne pas être compris. Beaucoup de gens peuvent négliger des détails essentiels dans un océan de mots lorsqu'ils sont pressés par le temps. Même lorsqu'ils ne sont pas pressés par le temps, beaucoup de gens peuvent facilement passer outre de longs passages.

Au lieu de blâmer les autres pour leur manque de lecture attentive, on peut présenter proactivement des critères d'acceptation faciles à lire, directs et dépourvus de détails superflus.

#### 3. Établir une compréhension partagée

C'est probablement la caractéristique la plus importante et celle qui est le plus souvent prise pour acquise. Si tous les membres de l'équipe ne sont pas sur la même longueur d'onde, alors le processus et la productivité sont compromis. Faire examiner les critères d'acceptation par l'équipe de développement avant de poursuivre l'histoire minimise la confusion. Des clarifications doivent être faites sur les critères, et les critères doivent être mis à jour en conséquence.

J'ai eu des expériences où tous les membres de l'équipe ont participé à la rédaction des critères d'acceptation. Cela a permis à tout le monde de comprendre toutes les parties de l'histoire. Cela a également offert des opportunités aux membres de l'équipe de poser des questions et de partager des idées. Cependant, un tel processus n'est pas toujours idéal, surtout pour les grandes équipes.

Néanmoins, il est important que chaque membre puisse lire les critères d'acceptation. À partir de là, chaque membre devrait comprendre comment mener l'histoire à son terme. Qu'il s'agisse de développement ou de test.

![Image](https://cdn-media-1.freecodecamp.org/images/-ZwiZDhnjvum-WpwyTy2etTL1X1OY2zbOWPm)

### **Quand trop c'est trop**

Nous avons déjà exploré le danger des critères d'acceptation flous. Cela entraîne le risque d'introduire des fonctionnalités superflues dans une histoire. Cependant, le cas opposé surprenant peut également exister : les critères d'acceptation peuvent devenir trop détaillés.

> **« Les critères d'acceptation doivent indiquer l'intention, pas une solution » (Segue Technologies)**

Fournissez un plan de « quoi » (intention) au lieu de « comment » (implémentation). Sinon, l'équipe de développement peut être privée de l'opportunité d'explorer différentes façons de résoudre le problème. Sur ces lignes, de meilleures implémentations peuvent être imaginées après les premières réflexions sur une solution.

**Une fois que vous avez rédigé vos critères d'acceptation, vous pouvez vous demander, « Combien est trop ? »**
J'ai vu des histoires allant de zéro critère d'acceptation à plus de quinze (ou du moins, c'est ce que cela semblait).

En règle générale, j'aime personnellement voir trois à huit critères d'acceptation par histoire. Cependant, vers la limite supérieure de cette fourchette, autour de cinq critères d'acceptation ou plus, je vérifierais la gérabilité. Je vérifierais soigneusement si l'histoire ne pourrait pas être divisée en histoires plus petites et plus gérables.

D'autres seraient en désaccord et soutiendraient que huit est déjà trop. Cependant, j'aime pencher vers la fourniture de autant de détails « quoi » que possible sans sacrifier la concision.

### **Et maintenant ?**

**D'accord, j'ai menti.** Je n'ai pas fourni une liste exhaustive de critères d'acceptation pour la rédaction des critères d'acceptation. Les caractéristiques souhaitées telles que la concision, la clarté et la compréhension sont subjectives. Je les ai voulues ainsi.

**Je crois qu'il n'y a pas de format « correct » pour la rédaction des critères d'acceptation. Leur exactitude est mesurée par l'efficacité au sein de l'équipe.**

Je recommande vivement d'utiliser initialement un modèle. Ils ont fourni à de nombreuses équipes une structure solide et sûre qui favorise la rédaction de bons critères d'acceptation. Cependant, ne laissez pas cette structure vous empêcher d'avancer vers des idées qui peuvent promouvoir l'efficacité et l'efficacité.

Si vous êtes un propriétaire de produit ou un client rédigeant des critères d'acceptation, je vous mets au défi de demander à votre équipe de développement un retour sur les critères d'acceptation actuels. Avec un peu de soin, de pratique et d'organisation, la rédaction de critères d'acceptation efficaces devient un outil puissant pour améliorer le flux de travail de toute équipe.

### Plus à lire

* [https://rubygarage.org/blog/clear-acceptance-criteria-and-why-its-important](https://rubygarage.org/blog/clear-acceptance-criteria-and-why-its-important) — par Maryna Z. et Dmiriy G.
* [https://www.leadingagile.com/2014/09/acceptance-criteria/](https://www.leadingagile.com/2014/09/acceptance-criteria/) par Steve Povilaitis
* [https://www.seguetech.com/what-characteristics-make-good-agile-acceptance-criteria/](https://www.seguetech.com/what-characteristics-make-good-agile-acceptance-criteria/) par Segue Technologies
* [http://agileforgrowth.com/blog/acceptance-criteria-checklist/](http://agileforgrowth.com/blog/acceptance-criteria-checklist/) — par Kamlesh Ravlani