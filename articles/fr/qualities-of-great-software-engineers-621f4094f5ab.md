---
title: Les qualités qui font un excellent ingénieur logiciel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-23T20:25:27.000Z'
originalURL: https://freecodecamp.org/news/qualities-of-great-software-engineers-621f4094f5ab
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Xv37PaIjTqZzoWQUk-4arw.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Les qualités qui font un excellent ingénieur logiciel
seo_desc: 'By Caleb Taylor

  Over the years, I’ve noticed some common traits of people that were incredibly valuable
  to a company. These engineers were smart, but that’s not why they were great. They
  tended to consistently do certain things that many other engine...'
---

Par Caleb Taylor

Au fil des années, j'ai remarqué certains traits communs chez les personnes qui étaient incroyablement précieuses pour une entreprise. Ces ingénieurs étaient intelligents, mais ce n'est pas pour cela qu'ils étaient excellents. Ils avaient tendance à faire régulièrement certaines choses que beaucoup d'autres ingénieurs ne faisaient pas. J'ai capturé certaines de ces qualités et les ai réduites à des concepts que tout ingénieur pourrait utiliser.

> **_Avertissement:_** _Ces choses ne sont pas toujours faciles à faire. J'ai personnellement échoué à chaque qualité à un moment donné de ma carrière. Je considère ces principes comme des "principes directeurs" pour toute personne qui souhaite devenir un excellent ingénieur, mais ce n'est pas une liste exhaustive. Votre définition d'un ingénieur "excellent" peut différer de la mienne._

### Se former pour devenir pompier

Quand j'étais un jeune ingénieur fraîchement diplômé, j'ai reçu ma première leçon précieuse de la part de mon manager. Il m'a dit,

> "Si tu veux être précieux pour ton entreprise, sois la personne qui court vers les incendies."

Il ne m'encourageait pas à me jeter dans un incendie (bien que je sois sûr que je l'ai mérité à certains moments), mais plutôt à être l'ingénieur prêt et capable de s'attaquer aux grands problèmes.

Les "incendies" peuvent être n'importe quoi, d'un bug de production désagréable à un refactoring intimidant d'un service majeur. Tout le monde ne peut pas éteindre ces incendies. La volonté de s'attaquer aux problèmes difficiles est la première étape, mais ce n'est pas suffisant. Vous devez être réellement capable d'éteindre l'incendie.

Se préparer à ces grands moments n'est pas toujours facile. Vous devez vous consacrer à la compréhension de l'architecture et de la conception de votre système. Plus un système est compliqué, plus cela prendra du temps.

Voici quelques méthodes que j'ai trouvées pour m'aider à me préparer à combattre les incendies :

* Créer un HLD ([Conception de haut niveau](https://en.wikipedia.org/wiki/High-level_design)) pour votre application/service
* Documenter les parties compliquées de votre code
* Déboguer les flux courants de votre code ligne par ligne
* Prendre le temps de creuser tout code que vous rencontrez et que vous ne comprenez pas
* Rechercher les technologies que votre équipe utilise et devenir un expert

Lorsque vous travaillez sur des tâches individuelles, soyez à l'affût de tout ce que vous ne comprenez pas. **N'acceptez pas les choses qui "fonctionnent simplement"**. Chaque fois que vous touchez à votre code, vous avez une chance de renforcer votre compréhension. C'est pourquoi se former pour devenir "pompier" est si difficile. Cela peut être un effort quotidien fastidieux pour être prêt à affronter les incendies.

Les excellents ingénieurs sont ceux qui font régulièrement ce genre de choses. Ils sont prêts à se pencher sur des problèmes qu'ils ne savent pas résoudre. Ils ont tendance à creuser plus profondément que l'ingénieur moyen parce qu'ils veulent vraiment comprendre les choses. Cela n'a rien à voir avec l'intelligence. C'est une question d'état d'esprit.

**À retenir :** Consacrez-vous à acquérir une compréhension approfondie de votre application. Lorsque des problèmes difficiles surviennent, soyez prêt à plonger et à éteindre l'incendie.

### Reconnaître les goulots d'étranglement

Combien de fois avez-vous vécu une situation comme celle-ci ?

> Développeur A : "Je vais déployer la dernière modification, d'accord ? Une fois que j'aurai mis à jour manuellement chacun des fichiers statiques et supprimé les paramètres de configuration locaux, je pourrai le télécharger."

> Nouveau Développeur : "Attendez, vous éditez manuellement ces fichiers à chaque déploiement ?"

> Développeur A : "Oui, c'est pénible. Nous avons aussi cassé la production quelques fois lorsque nous faisons une erreur. C'est assez ennuyeux."

> Nouveau Développeur : "Cela semble être une mauvaise façon de faire les déploiements.."

> Développeur A : "Oui, nous devrions vraiment corriger cela."

C'est malheureusement un problème assez courant pour les équipes logicielles. Des parties importantes ou courantes du flux de travail de votre équipe sont manuelles, fragiles et lentes. Occasionnellement, l'équipe reconnaîtra que c'est un problème et le corrigera. Au minimum, ils pourraient créer une carte dans le backlog.

> Le vrai problème est lorsque personne ne reconnaît un goulot d'étranglement

Alors, par où commencer ? Un bon point de départ est de penser à automatiser tout. Commencez par les tâches les plus critiques que vous effectuez manuellement. Votre équipe a-t-elle des tests que tout le monde exécute manuellement pour chaque pull request afin de s'assurer qu'ils passent ? Pourquoi ne pas les connecter à un serveur CI comme [Jenkins](https://jenkins.io/) ou [Travis CI](https://travis-ci.org/) et afficher les résultats directement dans la pull request avec des webhooks ?

Les membres de votre équipe passent-ils du temps à examiner le style et le formatage du code ? Pourquoi ne pas lint automatiquement votre code en utilisant un hook Git sur chaque commit avec un outil comme [Husky](https://github.com/typicode/husky) et [lint-staged](https://github.com/okonet/lint-staged) ?

Ces types d'optimisations peuvent être faciles à manquer. Les équipes acceptent ces points de douleur comme "la façon dont les choses sont", plutôt que comme des candidats à l'optimisation. Les excellents ingénieurs ont tendance à réfléchir à ces problèmes. Ils prennent le temps de les corriger, et les changements qui en résultent sont de grandes victoires pour toute l'équipe.

> _J'ai récemment lu [Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations](https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations-ebook/dp/B07B9F83WM)_ et je l'ai trouvé être une excellente ressource. Il donne un aperçu des meilleures pratiques d'ingénierie et de leur impact sur la performance et le bonheur de l'équipe. Il peut également être utile pour justifier le travail sur les goulots d'étranglement de votre équipe auprès des dirigeants et des équipes produit de votre entreprise avec des données provenant de nombreuses autres entreprises.

**À retenir :** Recherchez les goulots d'étranglement dans le processus de développement de votre équipe ou dans le pipeline de déploiement. Faites un effort pour prioriser et corriger les problèmes les plus importants afin d'améliorer la qualité de vie de votre équipe.

### Ne suivez pas aveuglément les modèles existants

Les ingénieurs adorent les modèles. Des milliers de livres existent sur les meilleurs modèles de programmation et comment les utiliser. Malheureusement, tous les modèles de code ne devraient pas être réutilisés.

Occasionnellement, j'ai examiné une pull request et trouvé une section de code étrange ou mal écrite. Lorsque je demande pourquoi elle a été écrite de cette manière, la réponse est généralement la même : "C'est comme ça que c'était fait avant. Je l'ai simplement copié d'ailleurs."

> Rompre avec les anciens modèles est la première étape pour en établir de nouveaux

La tendance des développeurs à copier le code existant est l'une des principales raisons de la dette technique. Il est facile de permettre ces changements car cela ressemble à d'autres codes en production.

Les excellents ingénieurs sont très prudents quant à la réutilisation du code existant. Cela s'applique à la fois à l'écriture et à la révision du code. Ils ont tendance à poser les questions suivantes :

* Le code copié est-il la meilleure façon de résoudre le problème ?
* S'il est similaire à un morceau de code existant, pouvons-nous le combiner en un seul module pour réduire la duplication ?
* Y a-t-il des bugs logiques dus à des différences subtiles entre le nouveau code et le code existant ?
* Ce code correspond-il aux dernières normes et discussions de conception de mon équipe ?

Ces principes s'appliquent également aux mises à jour des anciens morceaux de code. Il est très facile de glisser une modification de code dans une section de code obsolète ou mal écrite sans rien corriger, mais **les excellents ingénieurs font rarement cela**. Ils ont tendance à embrasser le concept de [refactoring continu](https://martinfowler.com/bliki/OpportunisticRefactoring.html).

Cela ne signifie pas que chaque mise à jour de code entraîne un refactoring massif. Les améliorations peuvent être (et sont généralement) une variété de choses simples :

* Améliorer les noms de variables ou de fonctions
* Décomposer une fonction grande et complexe en fonctions plus petites
* Abstraire la logique copiée en plusieurs endroits dans un composant partagé

Les excellents ingénieurs réfléchissent constamment à des moyens d'améliorer le code et laissent presque toujours le code dans un meilleur état que celui dans lequel ils l'ont trouvé.

> _J'ai récemment lu le livre [Refactoring: Improving the Design of Existing Code](https://martinfowler.com/books/refactoring.html)_ de Martin Fowler, et je l'ai trouvé être une excellente ressource sur le refactoring.

**À retenir :** Réévaluez constamment les structures de code, les modèles et la conception. Copier et coller du code est la racine de tous les maux. Laissez toujours le code dans un meilleur état que lorsque vous l'avez trouvé.

### Conclusion

Tout ingénieur logiciel peut appliquer ces qualités à son travail. Cela peut être difficile à faire de manière constante. Certaines caractéristiques nécessitent une volonté d'aller plus loin dans les nombreuses facettes de votre travail. Si vous êtes prêt à travailler sur ces qualités, vous deviendrez un meilleur ingénieur logiciel.

Cette courte liste est basée sur mes propres expériences, mais j'aimerais savoir ce que les autres en pensent. Quelles qualités les excellents ingénieurs ont-ils tendance à avoir selon votre expérience ? Faites-le moi savoir !