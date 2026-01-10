---
title: Qu'est-ce que la programmation collaborative ? Pair Programming, Mob Programming
  et comment tout cela fonctionne
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-02T20:13:44.000Z'
originalURL: https://freecodecamp.org/news/collaborative-coding-tips
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/collaborative-coding-tips.jpg
tags:
- name: Collaboration
  slug: collaboration
- name: pair programming
  slug: pair-programming
- name: teamwork
  slug: teamwork
seo_title: Qu'est-ce que la programmation collaborative ? Pair Programming, Mob Programming
  et comment tout cela fonctionne
seo_desc: "By Andrej Kovacevic\nCoding can be challenging, but it can become a lot\
  \ easier if you have the right strategies and tools. \nAfter all, as noted software\
  \ engineer and writer Joel Spolsky says, \"it is harder to read code than to write\
  \ it.\"\nOne way to ma..."
---

Par Andrej Kovacevic

La programmation peut être difficile, mais elle peut devenir beaucoup plus facile si vous avez les bonnes stratégies et les bons outils. 

Après tout, comme le dit l'ingénieur logiciel et écrivain [Joel Spolsky](http://blogs.perl.org/users/buddy_burden/2013/12/perl-and-me-part-4-a-worthy-program-exceedingly-well-read.html#note1), "il est plus difficile de lire du code que d'en écrire".

Une façon de rendre vos projets de développement plus réussis est de faire de la programmation collaborative. Cela fait référence au processus de travail sur le code avec une équipe ou avec un autre développeur. Dans un projet qui utilise la programmation collaborative, chaque membre de l'équipe aide à construire le code et le vérifie pour détecter les bugs ou les erreurs.

Travailler en paires ou en équipes aide à ce que le code final contienne [moins d'erreurs](https://www.freecodecamp.org/news/how-to-be-a-team-player-in-the-tech-world-c78aa9f4e898/) et de bugs, et cela se traduit par une meilleure qualité de code et des projets terminés plus rapidement.

Cela permet également un débogage plus rapide et une plus grande résilience du projet, car cette configuration facilite la prise de relais par d'autres développeurs en cas de départ de l'un d'eux du projet.

Mais la programmation collaborative ne produira pas tous ces avantages par défaut. Les obtenir dépend de la manière dont vous mettez en œuvre votre stratégie de développement collaboratif et de la manière dont vous l'exécutez. Voici quatre points à considérer lors de la mise en place de cette stratégie.

## Vous avez besoin d'un processus de développement sécurisé

Bien que le fait d'avoir plusieurs paires d'yeux vérifiant le code d'un projet devrait produire un bénéfice net pour la sécurité du code, cela peut également introduire un nouveau type de vulnérabilité dans le mélange. Cela est dû au fait que le partage de code via une plateforme de collaboration crée la possibilité d'une violation de données.

Les humains, après tout, sont le maillon le plus faible de la chaîne de cybersécurité. Ainsi, plus l'équipe est grande, plus les chances que quelqu'un commette une erreur de sécurité non forcée pendant le développement sont grandes.

Et des choses comme des identifiants de connexion exposés ou volés peuvent mettre en danger un projet, en particulier s'il est conçu pour gérer des informations sensibles comme les détails bancaires et personnels.

Cela signifie que les chefs de projet doivent choisir une plateforme de collaboration construite avec la sécurité à l'esprit. Certaines plateformes de programmation collaborative ont déjà des fonctionnalités de sécurité intégrées, mais d'autres non. Et différents types de projets de programmation nécessiteront différents ensembles de fonctionnalités, il n'y a donc pas de solution universelle.

Il existe cependant de nombreuses plateformes de programmation collaborative qui peuvent convenir. [Teletype](https://teletype.atom.io/), par exemple, offre un chiffrement de bout en bout et l'option d'utiliser des messages autodestructeurs.

Une autre option populaire est [Brackets](https://brackets.io/), qui offre une protection des données lors de l'interaction avec des plugins tiers et dispose d'un mécanisme pour prévenir l'accès non approuvé et l'escalade de privilèges.

Certaines équipes ou développeurs peuvent utiliser des plateformes de collaboration établies non spécifiquement conçues pour la programmation. Microsoft Teams, par exemple, peut faciliter la collaboration de programmation informelle. Et bien que ce ne soit pas un système intrinsèquement non sécurisé, il présente des faiblesses que les développeurs peuvent résoudre avec une solution supplémentaire de [sécurité Microsoft Teams](https://www.avanan.com/teams-security).

Ces solutions incluent des fonctionnalités telles que la protection contre les logiciels malveillants, la protection des URL, le contrôle d'accès aux données confidentielles, des outils de conformité et des alertes de sécurité, ce qui améliore considérablement la sécurité de la plateforme.

Quelle que soit la plateforme que vous choisissez, il est important d'utiliser des outils de sécurité ou d'installer des solutions de sécurité tierces qui garantissent la meilleure sécurité possible pour votre projet.

## Choisissez la bonne plateforme pour le travail

Il est également important de reconnaître que la sécurité n'est pas la seule considération lors du choix d'une plateforme de programmation collaborative.

Il est également crucial de choisir une plateforme qui fournira à chaque membre de l'équipe les outils et les ressources nécessaires pour faire son travail. La bonne plateforme doit répondre aux critères suivants :

### Elle est conçue pour un langage de programmation ou un écosystème spécifique

Il y a de nombreux avantages à utiliser une plateforme créée pour un langage de programmation spécifique. Tout d'abord, elle a probablement tous les outils nécessaires pour travailler efficacement sur un projet dans un langage particulier. Et elle n'aura pas de fonctionnalités inutiles ajoutées pour répondre à d'autres exigences et préférences.

Une plateforme spécifique à un langage est également conçue en tenant compte des meilleures pratiques pour les développeurs travaillant avec des langages ou des frameworks particuliers. Ainsi, par exemple, lors de l'utilisation de langages de programmation dynamiques tels que Go, Ruby et Python, il est préférable d'utiliser une plateforme comme [Cloud9](https://aws.amazon.com/cloud9/).

### Elle est rapide à installer

Idéalement, tous les participants devraient déjà être familiers avec la plateforme de programmation collaborative que vous utiliserez. Mais si ce n'est pas le cas, il est important de choisir une plateforme facile à apprendre avec une configuration minimale ou nulle.

Une plateforme qui nécessite la configuration de l'IDE, du serveur, du terminal, de la base de code et de la bibliothèque, ainsi que d'autres procédures de configuration, n'est pas l'option la plus adaptée pour la programmation en direct entre paires ou équipes de développeurs.

### Elle doit avoir une interface utilisateur personnalisable

La programmation est un travail très détaillé et les développeurs ont tendance à avoir leurs propres préférences en matière d'interface utilisateur pour pouvoir travailler facilement et commodément.

Obliger tout le monde à utiliser une plateforme avec laquelle ils ne sont pas à l'aise n'est pas une bonne façon de procéder avec la programmation collaborative. Il est donc utile d'avoir la possibilité de modifier l'interface utilisateur ou le tableau de bord dans une certaine mesure.

En résumé, la plateforme de programmation collaborative doit être facile à utiliser pour tout le monde. Les développeurs peuvent être des personnes très qualifiées, mais tout le monde n'est pas un maître en tout. Ceux qui collaborent doivent se mettre d'accord sur une plateforme et un arrangement de travail qui conviennent à tous.

## Définissez des rôles d'équipe clairs dès le départ

Nous pouvons catégoriser la programmation collaborative en trois configurations générales :

* la programmation en paire
* la programmation en groupe, et
* le partage de code.

Et comprendre le fonctionnement interne de chacune de ces configurations est important, car différents projets de programmation nécessitent différentes configurations.

Mais il est tout aussi important de comprendre les rôles des membres de l'équipe dans chaque configuration et de les définir avant de commencer à coder.

Comme le suggère l'expression, la [programmation en paire](https://www.freecodecamp.org/news/things-ive-learned-from-pair-programming-interviews-35a4db7d7443/) implique deux participants. Habituellement, l'un sert de conducteur et l'autre agit en tant que navigateur. Le conducteur écrit le code tandis que le navigateur examine la sortie.

Dans cette configuration, le conducteur est responsable des aspects tactiques du travail tandis que le navigateur définit la direction stratégique du code. Les deux peuvent ensuite échanger leurs rôles pour avoir un regard plus approfondi sur ce qu'ils ont produit.

La [programmation en groupe](https://searchsoftwarequality.techtarget.com/definition/mob-programming) est similaire à la programmation en paire mais implique plus de deux personnes. Pour éviter d'en faire un arrangement chaotique ou désorganisé, il est également important d'avoir les affectations de rôles conducteur-navigateur.

C'est légèrement plus compliqué, cependant, car il y a plus de deux développeurs qui doivent se mettre d'accord sur la manière d'attribuer les rôles conducteur-navigateur. Cela signifie que la communication claire et le respect mutuel sont cruciaux.

La configuration de partage de code ne nécessite pas une dynamique conducteur-navigateur. Au lieu de cela, les développeurs collaborateurs partagent simplement leur code respectif pour permettre à chacun de réviser, modifier, déboguer ou ajouter au code des autres.

C'est le type de collaboration sur lequel les développeurs open source ont tendance à s'appuyer car il permet aux nouveaux venus de participer à volonté et aux développeurs existants de mettre leur travail en pause chaque fois qu'ils en ont besoin.

Les participants ici peuvent travailler sur le code ensemble en temps réel ou de manière asynchrone. Ce qui est important, c'est qu'ils aient un système fiable pour le contrôle de version.

C'est là que les systèmes de contrôle de version comme [Git](https://git-scm.com/) excellent. Ils aident les équipes à éviter de faire un travail en double et s'assurent que tous les développeurs révisent, révisent ou ajoutent à la dernière version du code à tout moment.

## Créez des équipes équilibrées en compétences pour obtenir les meilleurs résultats

Bien que certains pourraient considérer la programmation collaborative comme une [opportunité d'apprendre](https://www.smashingmagazine.com/2020/04/collaborative-coding-ultimate-career-hack/) de codeurs plus expérimentés et compétents, cela ne signifie pas que chaque projet collaboratif est propice à cela.

Cela est dû au fait que pour certains types de projets, avoir trop de disparité dans le niveau de compétence des membres de l'équipe peut bloquer tout le projet.

C'est un problème qui alimente l'une des plus grandes critiques de la programmation collaborative en tant que méthode de développement. Lorsque les membres de l'équipe doivent contribuer en tant qu'égaux mais manquent des compétences pour suivre, le progrès stagne. Lorsque le temps est de l'essence, créer une équipe équilibrée en compétences est la seule option.

Cela dit, la programmation collaborative peut être une opportunité d'apprentissage collaboratif, mais seulement lorsque les délais ne sont pas impliqués. Dans ce scénario, les membres de l'équipe peuvent prendre leur temps pour apprendre du travail de leurs pairs plus expérimentés. Et à la fin, tout le monde bénéficie de l'expérience.

Mais si l'objectif est de faire du projet une entreprise d'apprentissage collaboratif, il est important de le clarifier dès le départ. Sinon, les développeurs plus expérimentés pourraient avoir l'impression d'avoir été dupés pour fournir une formation au lieu de mener à bien le projet. Et cela ne se termine jamais bien.

## Conclusion

Les avantages de la programmation collaborative sont indéniables, mais il y a aussi des inconvénients à considérer.

Ainsi, avant de décider de se lancer dans la voie collaborative, il est important d'examiner soigneusement les avantages et les inconvénients en ce qui concerne un projet spécifique.

Et pour les développeurs qui souhaitent essayer la programmation collaborative, il est bon de se familiariser avec les outils et plateformes populaires utilisés pour de tels projets au préalable. Ainsi, à la fois les planificateurs de projet et les membres de l'équipe tireront le meilleur parti du processus collaboratif, mais sans rencontrer certains des problèmes qu'il peut entraîner.

_Photo en vedette par snowing 12 - stock.adobe.com_