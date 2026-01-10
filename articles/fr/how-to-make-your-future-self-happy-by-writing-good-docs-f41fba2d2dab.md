---
title: Comment faire le bonheur de votre futur moi en rédigeant une bonne documentation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-18T17:04:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-future-self-happy-by-writing-good-docs-f41fba2d2dab
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bJKzkdJMBUhmDAnhwmpNsQ.jpeg
tags:
- name: docs
  slug: docs
- name: engineering
  slug: engineering
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment faire le bonheur de votre futur moi en rédigeant une bonne documentation
seo_desc: 'By Gabriele Cimato

  Or how to be less miserable when dusting off an old code base


  This is a little overview of common problems faced when working on a new or old
  project. Sometimes making a little effort up front can save you time and energy
  down the...'
---

Par Gabriele Cimato

#### Ou comment être moins misérable en dépoussiérant une ancienne base de code

![Image](https://cdn-media-1.freecodecamp.org/images/RH-mg3pmhVjtkFBzYfiWrfexlQZjf5KnUshr)

Ceci est un petit aperçu des problèmes courants rencontrés lors du travail sur un projet, qu'il soit nouveau ou ancien. Parfois, faire un petit effort au préalable peut vous faire gagner du temps et de l'énergie par la suite. Rédiger une bonne documentation, c'est comme se préparer à recevoir un high-five de son futur moi ✋ ! Nous verrons un exemple un peu bête et quelques pratiques recommandées pour commencer avec un bon `README.md`.

### La difficulté

Je suis presque certain que dans votre carrière, ou dans votre vie quotidienne, vous avez déjà été confronté à une situation qui vous fait penser :

> « Ce problème me semble familier, je suis presque sûr de l'avoir déjà résolu. Si seulement je pouvais me rappeler comment j'ai fait ! »

C'est particulièrement fréquent d'un point de vue technique. Des schémas répétés, des fonctions ou des bugs que nous avons déjà rencontrés et qui nous obligent à fournir exactement le même effort passé pour surmonter un problème. Parfois, nous sommes prêts à le refaire, alors nous nous lançons et trouvons la solution une fois de plus. Mais d'autres fois…

### Un exemple

Je dirige le département R&D chez Hutch et nous devons souvent explorer en profondeur de nouvelles technologies, frameworks ou langages. On essaie et on expérimente beaucoup, et on ne peut pas s'attendre à se souvenir de tout ce avec quoi on interagit. On travaille sur quelque chose pendant quelques mois puis, une fois terminé, on passe à quelque chose de très différent. Ou peut-être travaille-t-on simplement sur l'étape suivante d'un pipeline.

Puis, quand on s'y attend le moins, cela arrive. Vous devez revenir à ce framework que vous avez utilisé 3 mois auparavant pour effectuer une modification. Vous y jetez un coup d'œil, un regard perplexe 🧐.

> « Oh, en fait je m'en souviens. Pour qu'il se comporte de cette autre manière, je vais ici… je change ça… et voilà ! »

À ce moment-là, vous vous sentez plutôt bien. Vous avez réussi à vous rappeler comment les choses fonctionnaient. Vous êtes même fier de vous pour avoir laissé une documentation simple sur bon nombre des fonctions que vous avez écrites il y a bien longtemps. Puis, d'un léger clic de souris, vous lancez le projet et…

⛔ **ERREUR ! Le châssis principal a des cloches à vache dirigées vers Mars, ce n'est pas autorisé.**

😱 Aïe ! Cela semble très cryptique. Vous jetez un coup d'œil au code que vous avez modifié et, eh bien… vous essayez de le relancer. Peut-être que quelque chose changera automatiquement. Peut-être que le fait de le regarder à nouveau a eu un effet quantique quelconque. Non.

⛔ **ERREUR ! Le châssis principal a des cloches à vache dirigées vers Mars, ce n'est pas autorisé.**

Vous lisez ensuite les commentaires ou la doc. Rien ne mentionne cette erreur, rien ne vous oriente dans la bonne direction. Cette erreur est si distinctive que vous êtes sûr de l'avoir déjà vue, et aussi de l'avoir déjà résolue. Aussi décourageant que cela puisse paraître, vous devez trouver la solution… encore une fois !

Vous commencez à chercher le problème sur Google et remarquez des liens déjà visités.

> « Super ! Ce lien est probablement celui qui m'a aidé avec l'erreur… ouf. Crise évitée ! »

Vous faites ensuite défiler la page et, oh non ! Encore… beaucoup d'autres liens visités. Vous n'avez donc aucune idée de celui qui a mené à une solution, s'il y en a une. Et la recherche continue jusqu'à ce que, finalement, vous trouviez la solution — des minutes, des heures ou même des jours plus tard.

### Une bonne documentation couvre plus que les cas nominaux 💡

Je l'ai appris à mes dépens. Plusieurs fois. Il est souvent facile, bien qu'admirable, d'ajouter de la doc à vos fonctions/méthodes/classes en supposant que tout fonctionnera bien.

J'essaie toujours de faciliter la vie de quiconque se plongera dans mon code. Cela inclut mon futur moi ! Je documente donc consciencieusement presque toutes mes fonctions, sauf les plus triviales. Comme beaucoup le disent depuis des décennies :

> Vos commentaires devraient expliquer le **pourquoi** plus que le **quoi**.

Votre code devrait être « auto-documenté » de sorte que tout commentaire ajouté traitant du « quoi » devienne redondant.

En toute honnêteté, j'ai tendance à ajouter des commentaires même pour le « quoi », uniquement lorsque je sais qu'une fonction est soit longue, soit complexe. Ajouter quelques lignes de commentaires me permettrait d'éviter d'examiner chaque ligne de code. Cela a été utile d'innombrables fois et je le recommande absolument !

Mais la documentation ne se résume pas à des lignes de commentaires sur une fonction. Une bonne documentation, c'est un `README.md` bien écrit. Dans certains scénarios, c'est même un site web dédié complet pour les projets plus importants (voir [React](https://reactjs.org/docs/getting-started.html), [Redux](https://redux.js.org/introduction/getting-started), [Vue](https://vuejs.org/v2/guide/), [Slate](https://docs.slatejs.org/), …).

Les projets mentionnés sont tous open source. Les équipes sont pratiquement obligées d'entrer dans les détails pour aider les gens à commencer à utiliser leur framework ou leur bibliothèque (et elles font un excellent travail à cet égard !). Mais qu'en est-il des petits projets privés ? Qu'en est-il de ces projets qui ne vivront qu'au sein de l'entreprise (quelle que soit la taille de l'équipe) ? Et qu'en est-il de tous ces problèmes qui ne sont pas purement liés au code ?

Le plus souvent, nous avons tendance à ignorer le fichier `README.md` ou à l'expédier en quelques lignes seulement. Je suis une pratique simple mais puissante pour rendre cette tâche moins intimidante et aider à aller au-delà des cas nominaux.

### Une approche de base pour créer un bon README

En mentionnant les « cas nominaux » (happy paths), je fais référence à la pratique consistant à supposer que tout se passera sans accroc. Cela signifie que nous n'abordons chaque étape d'un processus que comme si elle allait toujours réussir.

Malheureusement, ce n'est pas toujours le cas. Alors, comment pouvons-nous nous faciliter la vie ? Comment s'assurer que même les cas moins favorables sont couverts ?

Voici quelques suggestions :

* Commencez par écrire quelques lignes sur l'objet du projet et **le problème que vous essayez de résoudre.** Cela vous aide, ainsi que quiconque le parcourt, à comprendre l'intention du projet.
* Au fur et à mesure que vous configurez tout, assurez-vous d'ajouter chaque étape au `README.md`. Il n'est pas nécessaire que ce soit parfaitement formaté ou formulé, il faut juste que ce soit là pour le moment. Cela prend généralement la forme d'instructions d'installation.
* Si à n'importe quel moment vous rencontrez une erreur de n'importe quel type, ajoutez une section en bas. Vous pouvez l'appeler **Erreurs courantes.** Vous y ajoutez des détails sur l'erreur rencontrée et comment vous l'avez résolue. Une chose cruciale que j'aime faire ici est d'ajouter des liens vers la source de la solution (ou tout ce qui m'a aidé à y parvenir).
* Lorsque j'atteins un point stable dans le projet, j'essaie de l'installer sur une nouvelle machine (si c'est possible). L'objectif ici est de **s'assurer que les étapes de configuration listées précédemment sont correctes** et fonctionnent comme prévu.
* Plus important encore, vous devez avoir une section répondant à la question : **comment utiliser/lancer ce projet ?** Cela doit être aussi clair que possible, alors faites un effort ! Parfois, cependant, vous ne pouvez pas répondre à cette question avant plus tard. Vous pouvez attendre d'être dans un état fonctionnel pour mettre à jour le `README.md`.
* Prévoyez du temps pour **réviser et nettoyer** votre fichier `README.md`. La plupart du temps, vous aurez probablement besoin de le **mettre à jour**.

C'est souvent suffisant pour les projets de petite taille. Pour les projets de taille moyenne à grande, cela peut être un point de départ pour développer de bonnes pratiques. Parlez-en avec le reste de l'équipe et convenez d'une approche commune qui satisfera tout le monde. Gardez à l'esprit que **maintenir la doc à jour est crucial !** Soyez mutuellement responsables de cela et, après l'effort initial, cela deviendra naturel, tout comme un simple refactoring !

### Conclusion

Rédiger une bonne documentation implique de maintenir un bon `README.md` et de documenter les **pourquoi** dans votre code plus que les **quoi**.

Si vous faites un petit effort et construisez progressivement un bon `README.md`, cela semblera moins intimidant. Non seulement cela vous facilitera la vie à l'avenir, mais cela aidera toute autre personne qui y contribuera.

Ne couvrez pas seulement les cas nominaux en espérant que tout fonctionnera, couvrez également les erreurs éventuelles que vous rencontrez ou tout problème qu'un nouveau venu pourrait rencontrer. Gardez une section dédiée à cela.

**Bonus :** lors de l'estimation de votre travail avec un PM, tenez compte de l'effort requis pour rédiger/mettre à jour la doc. Ne sous-estimez pas le fait qu'une bonne documentation nécessite pas mal de temps. Mais ce temps est très bien investi !

✨ Salut, je suis Gabri ! J'adore l'innovation et je dirige la R&D chez Hutch. J'aime aussi React, Javascript et le Machine Learning (parmi un million d'autres choses). Vous pouvez me suivre sur Twitter @[**G**abriOnTheRocks](https://twitter.com/GabriOnTheRocks) et sur GitHub @[Gabri3l](https://github.com/Gabri3l). Laissez un commentaire si vous avez d'autres recommandations que vous aimeriez partager, ou envoyez un DM sur Twitter si vous avez des questions !