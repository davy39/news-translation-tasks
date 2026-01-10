---
title: Comment accélérer les reconstructions de Node en utilisant les builds multi-étapes
  de Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-20T01:52:58.000Z'
originalURL: https://freecodecamp.org/news/speed-up-node-re-builds-leveraging-docker-multi-stage-builds-and-save-money-65189a4ab115
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Nsp3DqX0_RyNxggv
tags:
- name: Docker
  slug: docker
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment accélérer les reconstructions de Node en utilisant les builds multi-étapes
  de Docker
seo_desc: 'By John Standish

  Reinstalling npm dependencies can be a wasteful use of time and money. Depending
  on the size of your project, this can take several minutes. In my personal experience,
  I’ve seen npm install take upwards of 5 minutes. Now, if you have...'
---

Par John Standish

Réinstaller les dépendances `npm` peut être une perte de temps et d'argent. Selon la taille de votre projet, cela peut prendre plusieurs minutes. Dans mon expérience personnelle, j'ai vu `npm install` prendre plus de 5 minutes. Maintenant, si vous avez des étapes séparées (Gate, CI, différentes branches d'environnement) dans votre pipeline, ce temps d'attente devient encore pire. Sans blague, attendre coûte cher !

![Image](https://cdn-media-1.freecodecamp.org/images/1*NhZ8Ts1Xe0SlreW2Ljzo6g.png)
_[https://www.reddit.com/r/ProgrammerHumor/comments/6s0wov/heaviest_objects_in_the_universe/](https://www.reddit.com/r/ProgrammerHumor/comments/6s0wov/heaviest_objects_in_the_universe/" rel="noopener" target="_blank" title=")_

### Le gaspillage est coûteux, très coûteux

#### TL;DR

C'est une somme significative d'argent (~**9 918 $/an par développeur**) et de temps (18 792 minutes par an ou 13,05 jours par an) qui est gaspillée à attendre que les dépendances s'installent pendant que notre code passe par le pipeline. Ces chiffres sont une moyenne de 4 validations par jour. À bas régime, en attendant la gate, c'est **~3 132 $/an par développeur**. *Voir les calculs ci-dessous pour savoir d'où viennent ces chiffres.*

Faisons un peu de maths rapides pour voir pourquoi 5 minutes posent un gros problème. Supposons que vous avez une Gate et une build CI pour vos 2 environnements (Staging et Production). Chaque étape nécessite de démarrer une build propre.

Donc, additionnons le temps que nous attendons pour que `npm install` se termine :

Temps de build : 1 minute  
Gate : 5 minutes  
CI Staging : 5 minutes  
CI Production : 5 minutes  
**Temps d'attente NPM : 15 minutes**  
**Temps total de build : 18 minutes**

D'accord, 18 minutes ne semblent pas si graves. C'est une pause café, et nous aimons tous le café. Mais ces 18 minutes sont du temps d'inactivité, du temps passé à attendre que quelque chose soit prêt.

Maintenant, développons un peu ces maths et multiplions par une petite équipe (4 développeurs), et pour le fun, nous calculerons un nombre moyen de validations et un taux horaire. Le temps, c'est de l'argent, non ? Le nombre moyen de validations est ce que j'ai vu dans mon travail quotidien, et vos chiffres peuvent varier.

Temps de build : 3 minutes  
Temps d'attente NPM : 15 minutes  
Développeurs : 4  
Moyenne des validations : 4  
Taux horaire : 30 $ (votre taux horaire peut être plus élevé)

**Temps d'attente Gate : 96 minutes** **(Temps d'attente Gate X Développeurs X Moyenne des validations)**  
**Coût Gate : 48 $ (Temps d'attente Gate en heures x Taux horaire)**  
**Temps total : 288 minutes (Temps de build et NPM X Développeurs X Moyenne des validations)**  
**Coût : 144 $/jour (Temps total en heures X Taux horaire)**

Nous parlons donc de 144 $/jour de temps d'inactivité, soit 720 $/semaine, ou **37 584 $/an**. Et c'est en attendant que notre logiciel soit livré ! À bas régime, si nous validons notre code et attendons la gate, cela représente **12 528 $/an**. OUCH ! Le coût annuel était basé sur 261 jours ouvrés américains dans une année ([https://hr.uiowa.edu/payroll/2015-fiscal-year-payroll-calendar](https://hr.uiowa.edu/payroll/2015-fiscal-year-payroll-calendar))

### Mettons en cache et construisons cette chose !

#### TL;DR

Voici mes instructions sur la façon de procéder. [https://github.com/jstandish/cached-node-module-build-example/blob/master/DOCKER_BUILD.md](https://github.com/jstandish/cached-node-module-build-example/blob/master/DOCKER_BUILD.md)

D'accord, nous avons établi que attendre coûte cher. Par conséquent, nous devrions essayer de réduire le temps passé sur les étapes `npm install`. Nous ne devrions réexécuter `npm install` que lorsque le fichier `package.json` change. En exécutant sélectivement cette commande, nous pouvons réduire considérablement le temps nécessaire pour les nouvelles builds Gate/CI/CD, passant de plusieurs minutes à moins d'une minute (selon la taille de votre projet).

#### Phase 1 — Créer une étape de cache

Notre première étape consistera à créer un `dockerfile` multi-étapes. Cela nous permettra de copier le fichier `package.json` et d'exécuter une certaine étape uniquement si ce fichier a changé.

#### Phase 2 — Créer une étape de build

L'étape suivante consistera à créer l'étape suivante qui transmettra une commande à `npm`. Cela est fait en utilisant l'instruction `ENTRYPOINT` dans votre `dockerfile`. Cela exécutera la commande donnée en transmettant tous les arguments. Nous utilisons une image docker qui a déjà `Chromium` installé ; cela nous permettra d'exécuter Chrome Headless pour nos tests unitaires.

Voici le dockerfile complet :

#### Phase 3 — Construire l'image

Maintenant que notre `dockerfile` est configuré, construisons-le. Vous devrez faire cela chaque fois que les fichiers changent, mais le temps nécessaire pour copier vos nouveaux fichiers est trivial car docker ignorera les couches suivantes qui n'ont pas changé. Youpi !

Cela a pris environ **2 minutes**. Mais cela pourrait prendre plus de temps selon votre connexion internet, la vitesse du disque, le CPU, etc.

Toute build après notre `docker build` initial prendra moins de temps car nous ne réexécuterons `npm install` que si le fichier package.json a changé !

#### Phase 4 — Construire le code !

Maintenant, construisons notre code à l'intérieur de l'image node-build-test. Nous spécifierons un point de montage afin de pouvoir copier notre sortie de build dessus. Cela nous permettra d'extraire le code compilé de l'environnement dockerisé ! J'utilise un projet angular forké comme exemple, mais vous pouvez l'utiliser maintenant pour n'importe quel projet.

Le temps de build a pris environ 45 secondes. Mais c'était pour compiler notre code, pas pour attendre `npm install`. OUI !

Et nous avons maintenant nos fichiers compilés !

![Image](https://cdn-media-1.freecodecamp.org/images/1*vx3LTl-eZWIT0eZwxB7tyA.png)

#### Donc, ce sera seulement 45 secondes pour toutes les builds suivantes ?

Oui ! Parce que l'étape `npm install` est complètement ignorée, car le fichier `package.json` n'a pas changé, vous en tirerez les avantages. Si vous changez le `package.json`, vous subirez la même pénalité de temps que vous auriez eue de toute façon.

### Donc, combien de temps et d'argent avons-nous économisé ?

Revenons donc à notre calcul précédent, et soustrayons maintenant notre temps d'attente `npm install`. Nous garderons le temps de build car vous ne pouvez pas y échapper.

Temps de build : 3 minutes  
Développeurs : 4  
Moyenne des validations : 4  
Taux horaire : 30 $ (votre taux horaire peut être plus élevé)

**Temps Gate : 16 minutes** **(Temps d'attente Gate X Développeurs X Moyenne des validations)**  
**Coût Gate : 8 $ (Temps d'attente Gate en heures x Taux horaire)**  
**Temps total : 48 minutes (Temps de build X Développeurs X Moyenne des validations x Environnements)**  
**Coût : 24 $/jour (Temps total en heures X Taux horaire)**

Donc, regardons cela sur une journée, une semaine et une année.

**Jour : 24 $**  
**Semaine : 120 $**  
**Année : 6 264 $**

#### Et combien avons-nous économisé pour notre équipe de 4 développeurs ?

Le format ci-dessous est (**montant précédent — nouveau montant**). Et oui, c'est beaucoup d'économies sur l'année !

**Jour : (144 $ - 24 $) = 120 $**  
**Semaine : (720 $ - 120 $) = 600 $**  
**Année : (37 584 $ - 6 264 $) = 31 320 $**

### Conclusion

J'espère que vous avez apprécié voir comment l'utilisation d'une build multi-étapes de docker peut vous faire économiser une quantité significative de temps, ainsi que de l'argent. Les builds multi-étapes de Docker sont très puissantes et peuvent vous permettre de livrer et de construire plus rapidement.

Si vous voulez jouer avec cela, veuillez cloner mon dépôt GitHub et amusez-vous !

[https://github.com/jstandish/cached-node-module-build-example](https://github.com/jstandish/cached-node-module-build-example)

Merci d'avoir lu !

[https://www.instagram.com/john.does.code](https://www.instagram.com/john.does.code)