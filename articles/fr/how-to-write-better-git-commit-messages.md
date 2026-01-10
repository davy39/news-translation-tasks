---
title: Comment rédiger de meilleurs messages de commit Git – Un guide étape par étape
subtitle: ''
author: Natalie Pina
co_authors: []
series: null
date: '2022-01-04T22:34:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-better-git-commit-messages
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/gitcommitmessage.png
tags:
- name: Collaboration
  slug: collaboration
- name: Git
  slug: git
- name: teamwork
  slug: teamwork
- name: version control
  slug: version-control
seo_title: Comment rédiger de meilleurs messages de commit Git – Un guide étape par
  étape
seo_desc: "When first introduced to Git, it's typical for developers to feel uncomfortable\
  \ with the process. \nYou might feel uncertainty when encountering the Git commit\
  \ message, unsure how to properly summarize the changes you've made and why you've\
  \ made them...."
---

Lorsque l'on découvre Git pour la première fois, il est typique pour les développeurs de se sentir mal à l'aise avec le processus. 

Vous pourriez ressentir de l'incertitude lorsque vous rencontrez le message de commit Git, sans savoir comment résumer correctement les changements que vous avez apportés et pourquoi vous les avez faits. Mais plus tôt dans votre carrière vous pourrez développer de bonnes habitudes de commit, mieux ce sera.

Avez-vous déjà pensé à comment vous pourriez améliorer vos messages de commit Git ? Ce guide décrit les étapes pour améliorer vos messages de commit que vous pouvez commencer à mettre en œuvre dès aujourd'hui.

Cet article suppose que vous comprenez déjà le flux de travail de base de Git. Si ce n'est pas le cas, je suggère de lire le [Guide Git](https://guides.github.com/introduction/git-handbook/).

Il est également important de noter que vous devez suivre les conventions de votre équipe avant tout. Ces conseils sont basés sur des suggestions issues de recherches et d'un consensus général de la communauté. Mais à la fin de cet article, vous pourriez avoir quelques implémentations à suggérer qui pourraient aider le flux de travail de votre équipe.

> Je pense que git entre dans une toute autre dimension dès que vous commencez à travailler en équipe -- il y a tant de flux et de façons différentes et intéressantes que les gens peuvent commiter du code, partager du code, et ajouter du code à votre dépôt open-source ou closed-source.  [Scott Tolinski, Syntax.fm](https://syntax.fm/).

## Pourquoi devriez-vous écrire de meilleurs messages de commit ?

Je vous mets au défi d'ouvrir un projet personnel ou n'importe quel dépôt et d'exécuter `git log` pour voir une liste d'anciens messages de commit. La grande majorité d'entre nous qui avons suivi des tutoriels ou fait des corrections rapides diront "Oui... je n'ai absolument aucune idée de ce que je voulais dire par 'Corriger le style' il y a 6 mois."

Peut-être avez-vous rencontré du code dans un environnement professionnel où vous n'aviez aucune idée de ce qu'il faisait ou de ce qu'il signifiait. Vous avez été laissé dans le noir sans commentaires de code ou un historique traçable, et même en vous demandant "quelles sont les chances que cela casse tout si je supprime cette ligne ?"

### Retour vers le Futur

En écrivant de bons commits, vous vous protégez simplement pour l'avenir. Vous pourriez vous économiser, à vous et/ou à vos collègues, des heures de recherche en fournissant cette description utile.

Le temps supplémentaire qu'il faut pour écrire un message de commit réfléchi comme une lettre à votre futur vous-même est extrêmement précieux. Sur des projets à grande échelle, la documentation est impérative pour la maintenance.

La collaboration et la communication sont d'une importance capitale au sein des équipes d'ingénierie. Le message de commit Git en est un exemple parfait. Je vous suggère vivement de mettre en place une convention pour les messages de commit dans votre équipe si vous n'en avez pas déjà une.

## L'Anatomie d'un Message de Commit

#### Basique :

`git commit -m <message>`

#### Détaillé :

`git commit -m <title> -m <description>`

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-03-at-10.31.49-AM.png)

## 5 Étapes pour Écrire de Meilleurs Messages de Commit

Résumé des directives suggérées :

1. Capitalisation et Ponctuation : Capitalisez le premier mot et ne terminez pas par une ponctuation. Si vous utilisez les Conventional Commits, souvenez-vous d'utiliser tout en minuscules.
2. Forme : Utilisez l'impératif dans la ligne de sujet. Exemple  `Add fix for dark mode toggle state`. L'impératif donne le ton que vous donnez un ordre ou une demande.
3. Type de Commit : Spécifiez le type de commit. Il est recommandé et peut être encore plus bénéfique d'avoir un ensemble cohérent de mots pour décrire vos changements. Exemple : Bugfix, Update, Refactor, Bump, et ainsi de suite. Voir la section sur les Conventional Commits ci-dessous pour plus d'informations.
4. Longueur : La première ligne ne devrait idéalement pas dépasser 50 caractères, et le corps devrait être limité à 72 caractères.
5. Contenu : Soyez direct, essayez d'éliminer les mots et phrases de remplissage dans ces phrases (exemples : though, maybe, I think, kind of). Pensez comme un journaliste.

### Comment Trouver Votre Journaliste Intérieur

Je n'aurais jamais pensé que mon mineur en Journalisme bénéficierait à ma future carrière d'Ingénieur Logiciel, mais nous y voilà !

Les journalistes et les écrivains se posent des questions pour s'assurer que leur article est détaillé, direct et répond à toutes les questions du lecteur.

Lors de la rédaction d'un article, ils cherchent à répondre à _qui_, _quoi_, _où_, _quand_, _pourquoi_ et _comment_. Pour les commits, il est surtout important de répondre au quoi et au pourquoi pour nos messages de commit.

Pour rédiger des commits réfléchis, considérez ce qui suit :

* Pourquoi ai-je fait ces changements ?
* Quel effet ont eu mes changements ?
* Pourquoi ce changement était-il nécessaire ?
* À quoi ces changements font-ils référence ?

Supposez que le lecteur ne comprend pas ce que le commit traite. Il peut ne pas avoir accès à l'histoire détaillant le contexte du changement.

Ne vous attendez pas à ce que le code soit auto-explicatif. Cela ressemble au point précédent.

Cela peut sembler évident pour vous, le programmeur, si vous mettez à jour quelque chose comme des styles CSS puisque c'est visuel. Vous pouvez avoir une connaissance intime de pourquoi ces changements étaient nécessaires à ce moment-là, mais il est peu probable que vous vous souveniez pourquoi vous l'avez fait des centaines de pull requests plus tard.

Rendez clair _pourquoi_ ce changement a été fait, et notez s'il peut être crucial pour la fonctionnalité ou non.

Voir les différences ci-dessous :

1. `git commit -m 'Add margin'`
2. `git commit -m 'Add margin to nav items to prevent them from overlapping the logo'`

Il est clair lequel de ces messages serait plus utile aux futurs lecteurs.

Faites semblant d'écrire un article important. Donnez le titre qui résumera ce qui s'est passé et ce qui est important. Ensuite, fournissez plus de détails dans le corps de manière organisée.

En cinématographie, il est souvent cité "montrer, ne pas dire" en utilisant des visuels comme moyen de communication par rapport à une explication verbale de ce qui se passe.

Dans notre cas, "**dire**, ne pas [juste] montrer"  bien que nous ayons quelques visuels à notre disposition comme le navigateur, la plupart des spécificités proviennent de la lecture du code physique.

Si vous êtes un utilisateur de VSCode, téléchargez l'extension [Git Blame](https://marketplace.visualstudio.com/items?itemName=waderyan.gitblame). C'est un exemple parfait de l'utilité des messages de commit pour les futurs développeurs.

Ce plugin listera la personne qui a fait le changement, la date des changements, ainsi que le message de commit commenté en ligne.

Imaginez à quel point cela pourrait être utile pour résoudre un bug ou retracer les changements effectués. D'autres mentions honorables pour voir les informations historiques de Git sont [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) et [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens).

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-03-at-10.45.49-AM.png)

## Conventional Commits

Maintenant que nous avons couvert la structure de base d'un bon message de commit, je voudrais vous présenter les Conventional Commits pour vous aider à fournir quelques détails sur la création de messages de commit solides.

Chez D2iQ, nous utilisons Conventional Commit, une excellente pratique parmi les équipes d'ingénierie. Conventional Commit est une convention de formatage qui fournit un ensemble de règles pour formuler une structure de message de commit cohérente comme suit :

```
<type>[portée optionnelle]: <description>

[corps optionnel]

[pied de page optionnel(s)]
```

Le type de commit peut inclure ce qui suit :

* `feat`  une nouvelle fonctionnalité est introduite avec les changements
* `fix`  une correction de bug a eu lieu
* `chore`  des changements qui ne concernent pas une correction ou une fonctionnalité et ne modifient pas les fichiers src ou test (par exemple, la mise à jour des dépendances)
* `refactor`  du code refactorisé qui ne corrige pas de bug ni n'ajoute de fonctionnalité
* `docs`  des mises à jour de la documentation telles que le README ou d'autres fichiers markdown
* `style`  des changements qui n'affectent pas le sens du code, probablement liés à la mise en forme du code comme les espaces blancs, les points-virgules manquants, etc.
* `test`  incluant de nouveaux tests ou corrigeant des tests précédents
* `perf`  des améliorations de performance
* `ci`  lié à l'intégration continue
* `build`  des changements qui affectent le système de build ou les dépendances externes
* `revert`  annule un commit précédent

La ligne de sujet du type de commit doit être entièrement en minuscules avec une limite de caractères pour encourager des descriptions succinctes.

Le corps de commit optionnel doit être utilisé pour fournir des détails supplémentaires qui ne peuvent pas tenir dans les limites de caractères de la description de la ligne de sujet.

C'est également un bon endroit pour utiliser `BREAKING CHANGE: <description>` pour noter la raison d'un changement majeur dans le commit.

Le pied de page est également optionnel. Nous utilisons le pied de page pour lier l'histoire JIRA qui serait fermée avec ces changements, par exemple : `Closes D2IQ-<JIRA #>`.

#### Exemple Complet de Conventional Commit

```
fix: corriger foo pour activer bar

Cela corrige le comportement cassé du composant en faisant xyz.

BREAKING CHANGE
Avant cette correction, foo n'était pas activé du tout, le comportement passe de <ancien> à <nouveau>

Closes D2IQ-12345
```

Pour s'assurer que ces conventions de commit restent cohérentes entre les développeurs, le linting des messages de commit peut être configuré avant que les changements ne puissent être poussés. [Commitizen](https://commitizen-tools.github.io/commitizen/) est un excellent outil pour faire respecter les normes, synchroniser la version sémantique, ainsi que d'autres fonctionnalités utiles.

Pour aider à l'adoption de ces conventions, il est utile d'inclure des directives pour les commits dans un fichier markdown de contribution ou README au sein de vos projets.

Conventional Commit fonctionne particulièrement bien avec la version sémantique (en savoir plus sur [SemVer.org](https://semver.org/)) où les types de commit peuvent mettre à jour la version appropriée à publier. Vous pouvez également [en savoir plus sur les Conventional Commits ici](https://www.conventionalcommits.org/en/v1.0.0/).

## Comparaisons de Messages de Commit

Passez en revue les messages suivants et voyez combien de directives suggérées ils respectent dans chaque catégorie.

#### Bon

* `feat: améliorer les performances avec l'implémentation du chargement paresseux pour les images`
* `chore: mettre à jour la dépendance npm à la dernière version`
* `Corriger le bug empêchant les utilisateurs de soumettre le formulaire d'abonnement`
* `Mettre à jour le numéro de téléphone incorrect du client dans le pied de page selon la demande du client`

#### Mauvais

* `corrigé le bug sur la page d'accueil`
* `Changé le style`
* `oops`
* `Je pense que je l'ai réparé cette fois ?`
* messages de commit vides

## Conclusion

Écrire de bons messages de commit est une compétence extrêmement bénéfique à développer, et cela vous aide à communiquer et à collaborer avec votre équipe. Les commits servent d'archives des changements. Ils peuvent devenir un manuscrit ancien pour nous aider à déchiffrer le passé et prendre des décisions raisonnées dans le futur.

Il existe un ensemble de normes convenues que nous pouvons suivre, mais tant que votre équipe s'accorde sur une convention descriptive avec les futurs lecteurs à l'esprit, il y aura sans aucun doute des bénéfices à long terme.

Dans cet article, nous avons appris quelques tactiques pour améliorer nos messages de commit. Comment pensez-vous que ces techniques peuvent améliorer vos commits ?

J'espère que vous avez appris quelque chose de nouveau, merci d'avoir lu !

Connectez-vous avec moi sur Twitter [@ui_natalie](https://twitter.com/ui_natalie).