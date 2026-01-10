---
title: Pourquoi la documentation est importante et pourquoi vous devriez l'inclure
  dans votre code
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2018-08-07T17:17:30.000Z'
originalURL: https://freecodecamp.org/news/why-documentation-matters-and-why-you-should-include-it-in-your-code-41ef62dd5c2f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OQGgMhx12tTMWgv0
tags:
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Pourquoi la documentation est importante et pourquoi vous devriez l'inclure
  dans votre code
seo_desc: 'There are a plethora of acronyms when it comes to software development.
  KISS, DRY, SOLID… and so on and so forth. But, when it comes to documenting or commenting
  your code, there is no simple catchphrase.

  Why is that?

  Documentation should be as impor...'
---

Il existe une pléthore d'acronymes en matière de développement logiciel. KISS, DRY, SOLID… et ainsi de suite. Mais lorsqu'il s'agit de documenter ou de commenter votre code, il n'existe pas de phrase d'accroche simple.

Pourquoi en est-il ainsi ?

**La documentation devrait être aussi importante pour un développeur que tous les autres aspects du développement**

Dans cet article, je vais expliquer pourquoi documenter votre code vous aidera à devenir un meilleur développeur et contribuera à faire de vous un excellent membre d'équipe.

### Personne n'a le temps pour ça

La principale raison pour laquelle le code reste non documenté est le manque de temps.

Lors du développement d'une fonctionnalité qui doit être terminée dans un certain délai, nous avons rarement un moment pour tout arrêter et nous concentrer sur la documentation de notre code.

En plus de concevoir et d'écrire le code lui-même, nous devons également effectuer des revues de code, des tests d'automatisation et ajouter des tests unitaires (pour n'en citer que quelques-uns). La documentation est pratiquement laissée de côté.

**C'est le détail le moins pensé qui peut faire la plus grande différence à l'avenir.**

Quoi que vous développiez, il est probable qu'un jour, vous ou l'un de vos collègues devrez le revisiter. Ce jour-là, vous ne vous souviendrez pas si vivement de ce que vous avez écrit et pourquoi.

Et même si vous vous souvenez, il peut y avoir des cas particuliers ou des utilisations spécifiques qui ne sont pas clairement apparentes. La solution évidente est la **documentation**.

Prendre ce temps supplémentaire pour écrire une description appropriée de ce sur quoi vous avez travaillé vous fera économiser **énormément** de temps à l'avenir.

La prochaine fois que quelqu'un voudra comprendre ce qui se passe dans votre code, tout ce que vous aurez à faire sera de le diriger vers la documentation. Cela vous fera économiser du temps, car vous n'aurez pas besoin d'expliquer les choses, et cela leur fera économiser du temps, car ils ne dépendront pas de vous.

Et après tout, lorsque vous, en tant que développeur, devez comprendre quelque chose sur un certain aspect de la programmation, que faites-vous ?

> ? Vous consultez la documentation ?

### Le bon code n'a pas besoin de documentation

Oui, je sais, je sais… un code bien écrit, concis et bien pensé, n'a pas besoin d'être documenté. **Il se lit comme une histoire.**

Bien que cela puisse être vrai, cela ne dispense pas du besoin de documentation, et voici pourquoi :

1. Nous sommes tous trop familiers avec la robustesse du code qui compose une fonctionnalité. Regarder une section de code peut ne pas rendre clair qu'il existe d'autres sections qui y sont profondément liées.
2. Chaque service que vous créez a une API unique. Écrire comment utiliser cette API nécessite une documentation qui peut être lue en dehors du code. Vous ne voulez pas gonfler la classe elle-même avec des détails sur la façon d'utiliser l'API.
3. Les collègues qui travaillent dans différents départements (qui peuvent ne pas être développeurs) peuvent vouloir comprendre ce que vous avez fait et comment cela fonctionne.
4. Le simple fait de documenter peut vous amener à regarder différemment le code que vous avez écrit. Expliquer ce que fait votre code vous amènera à évaluer sa validité et peut-être à envisager de changer des choses si elles ne répondent pas à vos attentes.
5. Pour la postérité

![Image](https://cdn-media-1.freecodecamp.org/images/5jPNlmEKOGjTR294BEYE1stmTaQuIP38GzPM)
_« Une personne écrivant avec un crayon dans un cahier avec des copeaux de crayon dessus » par [Unsplash](https://unsplash.com/@thoughtcatalog?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Thought Catalog</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Comment écrire une bonne documentation

Une bonne documentation est comme un bon bloc de code. Court, simple et facile à comprendre. Voici quelques directives que vous pouvez suivre :

* Comprenez à qui la documentation est destinée. Est-elle uniquement pour les développeurs ? Y a-t-il un public plus large ? Comprendre cela vous fera économiser du temps, car vous saurez dès le départ combien vous devez élaborer dans vos explications.
* Écrivez un bref mais descriptif contexte expliquant les points principaux de ce que vous avez construit. Cela aidera les lecteurs à comprendre le but de la fonctionnalité et à en déterminer la pertinence par rapport à ce qu'ils veulent savoir.
* Listez et décrivez les principales perspectives de votre fonctionnalité, en veillant à souligner les dépendances qui existent avec d'autres fonctionnalités.
* Assurez-vous qu'il y a un horodatage, pour indiquer aux lecteurs la validité de la documentation. De plus, si vous utilisez certaines bibliothèques, assurez-vous d'inclure leurs versions également.
* Soyez généreux avec vos exemples de code, détaillant comment utiliser correctement la fonctionnalité que vous avez écrite et montrant les résultats attendus.

### Exemples

Pour mieux comprendre à quoi ressemble une bonne documentation, nous allons examiner quelques excellents exemples : [Mozilla Developer Network (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API), [Django](https://docs.djangoproject.com/en/2.0/) et [Stripe](https://stripe.com/docs).

![Image](https://cdn-media-1.freecodecamp.org/images/ttMCqH73G7L0lkB4Pg5RTAjPcnH9Q2-bfCRN)
_Remarquez les liens rapides en haut pour une navigation plus facile_

Dans la documentation de MDN, vous pouvez clairement voir que chaque page commence par une brève explication sur le sujet.

Ensuite, elle détaille les cas d'utilisation et les méthodes. Enfin, elle montre quels navigateurs sont compatibles avec la fonctionnalité et donne des liens vers des matériaux pertinents.

![Image](https://cdn-media-1.freecodecamp.org/images/n8TyfIok8mUQEmt6OeypnOV6pVp-TwJRSFaH)
_Dans la documentation de Stripe, chaque sujet contient des extraits de code qui peuvent être consultés dans divers langages de programmation_

![Image](https://cdn-media-1.freecodecamp.org/images/6AgI3-4qhfO2BH7hrr0fXt8kbUScCjCI1KnV)

La documentation de Django est très robuste. Peu importe votre niveau de codage, ils commencent par un aperçu et des tutoriels.

Ensuite, ils passent en revue chaque sujet, le détaillant méticuleusement, donnant des extraits de code courts et concis qui démontrent ce qui doit être fait.

J'espère avoir réussi à souligner l'importance de la documentation et vous avoir donné quelques conseils sur la façon de commencer à documenter votre code. Si vous avez une idée pour un acronyme pour la documentation, n'hésitez pas à le partager dans les commentaires ci-dessous.

Peut-être KID — **K**eep **I**t **D**ocumented ?

_Si vous avez aimé cet article, applaudissez pour que d'autres puissent également en profiter ! ???_