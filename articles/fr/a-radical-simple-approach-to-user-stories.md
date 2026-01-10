---
title: Une approche radicalement simple pour les user stories
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-17T19:01:36.000Z'
originalURL: https://freecodecamp.org/news/a-radical-simple-approach-to-user-stories
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/adorable-book-boy-1250722.jpg
tags:
- name: agile
  slug: agile
- name: backlog
  slug: backlog
- name: Scrum
  slug: scrum
- name: user story
  slug: user-story
seo_title: Une approche radicalement simple pour les user stories
seo_desc: 'By Bertil Muth

  User stories are a great way to plan development work. In theory. But how do you
  avoid getting burned in practice? I propose a radically simple approach.

  Here''s a popular template to describe a user story:


  Here''s an example user story...'
---

Par Bertil Muth

Les user stories sont un excellent moyen de planifier le travail de développement. En théorie. Mais comment éviter de se brûler les ailes en pratique ? Je propose une approche radicalement simple.

Voici un modèle populaire pour décrire une user story :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/grafik-18.png)

Voici un exemple de user story :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/grafik-22.png)

Les user stories examinent le logiciel du point de vue de la valeur utilisateur. Après avoir implémenté une story, les développeurs peuvent obtenir des retours des utilisateurs pour savoir s'ils sont satisfaits ou s'il y a quelque chose qu'ils aimeraient changer. C'est l'idée centrale du développement agile.

Les bonnes user stories suivent les trois C : **Card**, **Conversation** et **Confirmation** [1].

**Card** signifie : les user stories sont courtes. Elles se concentrent sur la valeur apportée à l'utilisateur. Vous pouvez les écrire sur une fiche ou un Post-it. Bien sûr, un Post-it ne contient pas toutes les informations nécessaires au développement.

L'équipe développant le logiciel a donc des **conversations** sur les stories. Les contributions des utilisateurs et des parties prenantes sont nécessaires, mais les développeurs apportent également leurs idées. Il est important que tout le monde garde l'esprit ouvert lors de ces discussions.

L'équipe documente les résultats des conversations sous forme de critères d'acceptation. Vérifier les critères d'acceptation plus tard sert de **confirmation** que l'équipe a correctement implémenté la story.

## Critères d'acceptation et INVEST

Les critères d'acceptation doivent répondre à des questions comme :

* Quelles sont les entrées possibles de l'utilisateur ?
Par exemple : "Les options de paiement sont MasterCard, Visa, [...] PayPal."
* Comment le système réagit-il à l'entrée de l'utilisateur ou à un événement pertinent pour l'entreprise ? Dans quelles conditions ?
Par exemple : "Lorsque l'utilisateur entre un numéro de carte de crédit incorrect, le système affiche le message d'erreur suivant : [...]"

Il existe de nombreuses façons de documenter les critères d'acceptation : puces, croquis, exemples, tableaux. Le développement commence quelques jours après la conversation sur la story. Les développeurs ont donc besoin de suffisamment de documentation pour se souvenir de la conversation.

Comment une équipe vérifie-t-elle si une story a une qualité suffisante pour commencer à l'implémenter ? Les critères **INVEST** définissent une liste de contrôle de qualité pour chaque story [2] :

* **I** pour **Indépendant**. La story peut être implémentée indépendamment des autres stories. Cela facilite les changements de priorité.
* **N** pour **Négocié**. La conversation entre les développeurs et les parties prenantes sur les détails de la story a eu lieu.
* **V** pour **Valable**. La story apporte une valeur visible aux utilisateurs. Contrairement aux tâches d'implémentation comme l'interrogation de la base de données, par exemple.
* **E** pour **Estimable**. Les développeurs peuvent estimer la story.
* **S** pour **Petit**. La story peut être implémentée rapidement. Dans Scrum, par exemple, dans un Sprint.
* **T** pour **Testable**. La story est suffisamment concrète pour que l'équipe puisse en dériver des cas de test.

## Les problèmes en pratique

J'aime les user stories. En planification de produit, elles déplacent le focus des détails techniques vers les utilisateurs et leurs besoins. C'est bien.

Et pourtant, dans mon travail de coach agile et de formateur pour les approches agiles, j'ai commencé à remettre en question la manière courante dont les gens les traitent.

J'ai vu des backlogs avec des centaines de stories qui sont devenues extrêmement difficiles à gérer. J'ai été témoin de personnes utilisant les termes "feature", "epic" et "business requirement" sans partager une compréhension de ce que cela signifie même. J'ai entendu des discussions sans fin sur les critères d'acceptation détaillés et sur la manière de découper les stories en fonction de ceux-ci. C'était frustrant.

Je affirme qu'il existe une alternative. Une manière simple d'éviter tous ces pièges. D'abord, vous devez comprendre qu'il existe deux niveaux fondamentaux de user stories.

## Les objectifs apportent de la valeur, mais ne peuvent pas être implémentés

Dans l'un de mes cours, je pose des questions comme : "Que pouvez-vous faire avec une boutique en ligne ?"
Les réponses typiques sont : "Acheter un produit", ou "Commander des produits".

Ce dont parlent les participants sont des objectifs. Si nous étions une équipe développant une boutique en ligne, nous pourrions proposer la user story suivante :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/grafik-23.png)

Cette story de niveau objectif est-elle précieuse pour l'utilisateur ? Oui ! Elle reflète les besoins du client de la boutique en ligne.

Pouvez-vous implémenter directement cet objectif ? Non ! Pour implémenter un objectif, vous devez d'abord en dériver les étapes pour l'atteindre. Pour la story "Acheter un produit", les étapes pourraient ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/grafik.png)

Chaque étape pourrait être documentée avec le modèle de user story : "En tant que client d'une boutique en ligne, je veux entrer l'adresse afin que le produit me soit livré."

Pouvez-vous implémenter directement cette story de niveau étape ? Oui ! Dès que vous avez clarifié les critères d'acceptation. Mais est-ce précieux pour l'utilisateur ? Sans les autres étapes, non.

La valeur n'émerge que lorsque l'objectif est atteint. Chaque étape représente un progrès vers l'objectif. Mais indépendamment, l'étape n'a aucune valeur. Est-il judicieux d'utiliser le modèle de story pour cela alors ?

## Une approche radicalement simple

Les stories au niveau des objectifs sont à gros grains. Elles peuvent être utilisées pour une planification à long terme, sans gaspiller d'efforts sur les détails :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/grafik-1.png)

Vous pouvez souvent réaliser de bonnes user stories au niveau des objectifs indépendamment les unes des autres. Et elles apportent de la valeur. Elles sont **I**ndépendantes, **N**égociées et **V**alables. Mais elles ne sont pas **P**etites, facilement **E**stimables et **T**estables. Parce que vous ne pouvez pas définir de critères d'acceptation pour elles sans parler des étapes.

Les stories au niveau des étapes sont **N**égociées, **E**stimables, **P**etites et **T**estables. Cependant, elles ne sont pas **I**ndépendantes et n'apportent pas de **V**aleur seules.

Comment combinez-vous les deux types de stories en une seule approche simple ? Voici ma proposition.

L'équipe choisit un objectif, par exemple "Acheter un produit". L'équipe réfléchit ensuite : "Quel est le moyen le plus simple d'atteindre l'objectif ? Et comment pouvons-nous réduire les risques architecturaux tôt ?"

Supposons que l'équipe voie le plus grand risque dans la communication avec PayPal, car ils n'ont jamais implémenté une interface avec PayPal auparavant.

À quoi ressemble un moyen simple d'atteindre l'objectif "Acheter un produit" ? L'équipe place la story de niveau objectif, les stories de niveau étape et les critères d'acceptation sous forme de notes autocollantes les unes sous les autres :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/grafik-2.png)

Voici ce que disent les critères d'acceptation (notes autocollantes vertes). Il n'y a qu'un seul produit fixe qui peut être commandé. Pas de recherche, pas de choix. L'interface utilisateur est basique et ne permet aux utilisateurs de payer qu'avec PayPal.

Ce sont les premières étapes que les développeurs implémentent. Une fois qu'un développeur a implémenté une étape, il la démontre aux parties prenantes internes de l'entreprise. Au plus tard lorsqu'un objectif est atteint, l'équipe implique les utilisateurs. Obtenir des retours et en dériver des insights pour les itérations suivantes est crucial.

Dans les itérations ultérieures, l'équipe ajoute et modifie des stories. Des exemples incluent : plus de produits, une capacité de recherche et de nouvelles méthodes de paiement. Ou l'équipe choisit une autre story comme objectif. Ce qui est le plus précieux et a du sens à un moment donné.

## Résumé

Vous vous concentrez sur quelques objectifs pour voir plus loin. Mais vous ne discutez des critères d'acceptation des étapes que vous implémenterez dans quelques jours. Vous implémentez les étapes et recueillez des retours. Vous utilisez les retours pour informer ce que vous développerez à l'avenir.

De cette manière, tout le monde a une idée claire de ce qui se passe dans le développement. Vous évitez les discussions inutiles. Et vous gardez la gestion du backlog à un minimum.

J'ai suivi cette approche à de nombreuses reprises. Lorsque tout le monde est à bord, cela fonctionne très bien. Cela rend le développement agréable.

Et c'est tout.

Sources :

[1] Ron Jeffries 3Cs : [https://ronjeffries.com/articles/019-01ff/3cs-revisited/](https://ronjeffries.com/articles/019-01ff/3cs-revisited/)

[2] Bill Wake sur les critères INVEST : [https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/)

_Pour [maîtriser les bases du développement logiciel agile](https://skl.sh/2Cq497P), visitez mon cours en ligne. Si vous souhaitez suivre ce que je fais ou me laisser un mot, suivez-moi sur [dev.to](https://dev.to/bertilmuth), [LinkedIn](https://www.linkedin.com/in/bertilmuth/) ou [Twitter](https://twitter.com/BertilMuth). Ou visitez mon [projet GitHub](https://github.com/bertilmuth/requirementsascode)._