---
title: Ce que j'ai appris en construisant trois services en trois mois tout en travaillant
  à plein temps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-06T17:23:02.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-building-three-services-in-three-months-while-working-full-time-5cf1bbf207d0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gxHw9bxhEY-ezPeMC26kOQ.jpeg
tags:
- name: csv
  slug: csv
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: side project
  slug: side-project
- name: Vue.js
  slug: vuejs
seo_title: Ce que j'ai appris en construisant trois services en trois mois tout en
  travaillant à plein temps
seo_desc: 'By taira

  To give you a bit of a context, I’ll start off with a little bit about me. I’m a
  self-taught developer currently working in Japan. I’m not special in any way, I
  don’t have any Internet celebrity friends, but I do love coding and have a posit...'
---

Par taira

Pour vous donner un peu de contexte, je vais commencer par parler un peu de moi. Je suis un développeur autodidacte travaillant actuellement au Japon. Je ne suis pas spécial en aucune façon, je n'ai pas d'amis célébrités sur Internet, mais j'adore coder et j'ai une attitude positive et volontaire.

À la fin de l'année dernière, j'ai décidé de lancer un projet expérimental, essayer de créer un service par mois en 2018 pendant mon temps libre. Je voulais voir si moi, un Indie-hacker-wanna-be, pouvais faire quelque chose. Et voici mon histoire jusqu'à présent.

Je vais diviser ma discussion sur chaque service en ces sections :

* Comment l'idée est venue
* Ce que le service est
* Stack technique
* Combien de $ j'ai dépensé
* Leçons apprises

### Janvier : gratter ma propre démangeaison.

#### **Comment l'idée est venue**

La première chose qui m'est venue à l'esprit était de construire quelque chose que j'utiliserais beaucoup. Dans le pire des scénarios, si mon service n'attirait personne, cela m'aiderait toujours.

J'ai commencé à examiner mon flux quotidien. J'ai réalisé que je passais beaucoup de temps chaque jour à aller sur une variété de sites web. Alors, ne serait-il pas agréable d'avoir un service web pour surveiller ces sites pour moi et m'envoyer des mises à jour par e-mail ? Cela m'aiderait à me concentrer sur les choses importantes.

#### **Ce que le service est**

![Image](https://cdn-media-1.freecodecamp.org/images/1*tNX15eL8kX2r5Pz_8L1C7w.png)
_KMPPP_

[Keep Me PPPosted](https://kmppp.com) est ce que j'ai fini par construire. Pour rendre le service encore plus convivial, j'ai également construit une [extension Chrome](https://chrome.google.com/webstore/detail/keep-me-ppposted/fnfioeoaippeenifnfhpblddioiaaeji?utm_source=medium), qui permettait à l'utilisateur de s'abonner aux mises à jour de n'importe quel site web sur le champ. Vous pouvez consulter les histoires d'utilisateurs détaillées et les décisions de conception sur la page [À propos](https://kmppp.com/about?perspective=dev), et je suis en train d'ouvrir le code source de ce projet, voici le dépôt Github [repo](https://github.com/slashbit/spider-less) :)

#### **Stack technique**

J'ai opté pour ce avec quoi je suis le plus à l'aise : le front-end Vue.js et le back-end AWS Lambda Serverless combo. J'ai travaillé avec ces technologies dans mon entreprise actuelle au quotidien pendant l'année et demie dernière. Serverless correspond très bien à ma conception, considérant que la plupart des parties de mon service suivent le modèle event-sourcing.

#### **Combien j'ai dépensé**

22 $ au total : 7 $ pour le domaine, 10 $ pour l'abonnement Sendgrid (100 000 e-mails par mois, je pourrais l'utiliser pour mes autres services également), et des frais uniques de 5 $ pour la publication de l'extension sur le Chrome Web Store. Tout le reste était couvert par le plan gratuit AWS free tier.

#### **Leçons apprises**

C'était définitivement une expérience d'apprentissage précieuse, puisque c'était mon tout premier service web à grande échelle. Je l'ai posté sur Indie hackers et j'ai obtenu quelques utilisateurs. Mais plus important encore, j'ai eu l'occasion de parler directement avec mes utilisateurs, travaillant en tant que développeur dans l'entreprise.

Dans mon travail, je n'ai jamais l'occasion de parler avec mes utilisateurs finaux pour obtenir des retours instantanés et avoir un contrôle total sur le produit que je construis. Cela seul valait le temps et les efforts que j'y ai mis.

### Février : tirer parti de mes ressources.

#### **Comment l'idée est venue**

Janvier était assez tendu, alors j'ai décidé de prendre les choses facilement. J'ai pensé à ce que je pourrais offrir d'autre, en plus de ma demi-boîte d'ailes de poulet dans mon réfrigérateur. Quelque chose dont les autres pourraient avoir besoin.

Je suis au Japon, et travailler ici pourrait intéresser les développeurs. En plus de cela, je reçois souvent des recruteurs qui m'envoient des opportunités d'emploi. Connecter les développeurs et les recruteurs pourrait être quelque chose sur lequel je pourrais travailler.

#### **Ce que le service est**

Au lieu de me lancer directement dans le codage, j'ai créé une liste de diffusion en utilisant MailChimp. J'ai commencé à partager mon expérience dans les communautés de développeurs chaque fois que j'en avais l'occasion. Cela a fonctionné, et ma liste de diffusion a atteint 500+ abonnés en un mois.

En attendant, chaque fois qu'un recruteur me contactait, je mentionnais casuellement ma liste de diffusion et demandais si je pouvais la partager avec mes abonnés.

#### **Combien j'ai dépensé**

0 $. Les e-mails sortants sont couverts par le même compte Sendgrid, et le travail cron backend qui a été construit avec AWS Lambda était à nouveau couvert par mon plan gratuit AWS free tier.

#### **Leçon apprise**

Il semble que moins je passe de temps à coder, et plus de temps à promouvoir mon service, plus j'obtiens d'utilisateurs potentiels. Deux semaines après avoir commencé, j'ai reçu un e-mail de l'un de mes abonnés me remerciant pour ce que j'ai fait.

Il n'avait pas encore obtenu d'emploi en utilisant le service, il voulait juste me remercier pour avoir partagé ces informations. Cet e-mail a simplement réchauffé mon cœur, sachant que ce que je fais aide réellement les autres. C'est juste la meilleure sensation au monde !

### Mars : obtenir des idées des autres.

#### **Comment l'idée est venue**

À ce stade, j'avais un peu épuisé mes idées. C'est alors que j'ai commencé à parler avec mes amis non-développeurs. J'ai essayé de comprendre à quoi ressemble leur vie quotidienne et s'il y avait des points douloureux que je pourrais aider à résoudre.

Dans le cadre de son travail, l'un de mes amis reçoit des fichiers CSV de la part de clients, puis importe ces fichiers dans un système interne. Souvent, les fichiers qu'il reçoit ne correspondent pas aux exigences, manquent de colonnes ou contiennent des types de données incompatibles, etc.

Il doit souvent revenir en arrière et demander à son client de refaire et de renvoyer les fichiers. Il a essayé d'utiliser Excel pour automatiser le processus, mais a échoué parce que la plupart des fichiers étaient vraiment volumineux (300+ Mo avec 1M+ de lignes). Cela ressemblait certainement à quelque chose que je pourrais aider à résoudre.

#### **Ce que le service est**

![Image](https://cdn-media-1.freecodecamp.org/images/1*vlk_6w7yVafO3dkFjFTDyA.png)

J'ai créé [CSV Lint](https://csvlint.com), un service de validation de fichiers CSV pour les entreprises, qui permet à un utilisateur de créer facilement un schéma pour valider les fichiers CSV une fois le schéma créé. Il peut être partagé avec d'autres (qui pourraient l'utiliser sans avoir de compte). Cela signifie que une fois que mon ami a créé le schéma, il pourrait demander à ses clients de l'utiliser pour valider leurs fichiers avant de les lui envoyer.

#### **Stack technique**

Au lieu d'AWS, j'ai opté pour Google Cloud Platform, Firebase pour l'hébergement et la base de données, et Google Cloud Functions pour gérer la logique backend. Une fois de plus, leur niveau gratuit couvrait tout.

#### **Combien j'ai dépensé**

17 $ au total. J'ai dépensé 7 $ pour le domaine - et c'est un domaine assez génial, je dois dire, me tapant sur l'épaule. Et un autre 10 $ sur Udemy pour un cours sur comment faire une vidéo de démonstration en utilisant Keynote. C'était de l'argent bien dépensé, une autre nouvelle compétence apprise. 😊

#### **Leçons apprises**

Les idées que je me fais mènent à rien 9 fois sur 10. Parler avec les autres, surtout les personnes en dehors de mon cercle habituel, m'aide souvent à obtenir de nouvelles idées. Cependant, la partie triste est que je n'ai pas vraiment beaucoup d'amis avec qui je peux parler - il semble que je doive travailler sur cela aussi. 😢

### Conclusion

Donc, voici mon parcours jusqu'à présent. Aucun de mes projets n'a connu un grand succès, et je ne gagne actuellement rien avec eux. Mais chacun de ces services aide les gens d'une manière ou d'une autre, et cela me met un grand sourire sur le visage chaque jour lorsque je vais me coucher. De plus, ils ne m'ont presque rien coûté, il reste encore quelques ailes de poulet dans mon réfrigérateur. Tout va bien, tout va bien.