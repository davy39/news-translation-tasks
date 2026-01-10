---
title: Écriture de scénarios assistée, avec Pychronia Tools
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-05T21:44:28.000Z'
originalURL: https://freecodecamp.org/news/assisted-script-writing-with-pychronia-tools
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/pychroniatools.png
tags:
- name: larp
  slug: larp
- name: Python
  slug: python
- name: roleplay
  slug: roleplay
- name: Script
  slug: script
- name: tools
  slug: tools
- name: writing
  slug: writing
seo_title: Écriture de scénarios assistée, avec Pychronia Tools
seo_desc: 'By Pakal de Bonchamp

  Let software tooling check the consistency of your roleplay scripts for you!

  (French version of this article available here on Electro-GN)

  Issue

  Every  writer will confirm it to you: it is not easy to remain coherent when  you
  ar...'
---

Par Pakal de Bonchamp

**Laissez les outils logiciels vérifier la cohérence de vos scénarios de jeu de rôle pour vous !**

*(Version française de cet article disponible [ici sur Electro-GN](https://www.electro-gn.com/12495-lecriture-de-scenarios-assistee-avec-pychronia-tools))*

### Problématique

Tout écrivain vous le confirmera : il n'est pas facile de rester cohérent lorsque l'on travaille, pendant plusieurs mois, sur une longue histoire. Cela l'est encore moins lorsque l'histoire en question est vécue par des dizaines de personnages, chacun ayant sa propre vision partielle de la vérité. Et les jeux de rôle grandeur nature (GNs) sont particulièrement exposés à ce problème.

Le danger ne réside pas dans le premier jet de l'écriture : si l'auteur a bien toutes ses idées en place, il ne risque pas grand-chose, à part quelques coquilles et interversions de noms. C'est lors des modifications ultérieures (changements dans la chronologie des faits, ajouts de rebondissements, etc.) que les informations — disséminées et dupliquées dans les documents des divers participants — deviendront progressivement obsolètes et incohérentes. Finalement, même les fiches de personnages d'une commune "murder&mystery party" finiront remplies d'improbabilités spatiales, temporelles, lexicales et structurelles si elles ne sont pas rigoureusement vérifiées et comparées après chaque évolution du scénario.

Que faire pour éviter cela, sans passer une vie à faire des relectures comparatives ? D'abord, sans doute, *dédoubler les textes communs à plusieurs joueurs*, qui conduisent à des copier-coller fastidieux (multipliant les erreurs et gonflant artificiellement la masse du texte). Ensuite, *permettre à l'auteur de revoir les ensembles de modifications interdépendantes* qu'il a successivement appliquées à son scénario. Enfin, lui donner des *résumés des informations clés*, plus faciles à relire que des textes littéraires verbeux. Et tout cela de *manière aussi automatisée que possible*, car le nombre de documents à gérer peut rendre la plus petite opération très chronophage (et à risque d'inattention).

### Les avantages de la machinerie Pychronia Tools

Pour bénéficier de ces précieuses facilités d'écriture lors de la création de la [Chrysalis:Mindstorm](https://chrysalis-game.com/fr/cms/soiree-mystere-chrysalis-mindstorm/) (en français uniquement), j'ai mis en place un processus d'écriture spécifique, impliquant des fichiers texte simples (qui contiennent le scénario), divers outils logiciels existants, ainsi qu'un module « Pychronia Tools » développé pour l'occasion.

Une fois cette machinerie en place, il suffit de la lancer et — magie — une centaine de fichiers PDF apparaissent les uns après les autres dans le dossier de sortie : manuel du maître de jeu, fiches de personnages complètes et résumées pour les joueurs, documents à imprimer sur de beaux parchemins servant d'indices en jeu, fiches récapitulatives pour les figurants…

Cet outil est bien plus qu'un simple générateur de documents : il inclut une **vérification automatique de la cohérence du scénario**. Maintenant, si un indice est mentionné à un endroit mais non fourni à un autre, ou si le même symbole a des valeurs différentes d'un fichier à l'autre, l'erreur est signalée.

**Extrait des erreurs de cohérence retournées par le programme :**

> !!! ERREUR DANS le registre des indices pour la clé golden_box_with_blood : ['needed'] nécessite un indice fourni
> !!! ERREUR DANS le registre des symboles pour la clé murder_date : ['3 janvier 2018', '15 mars 2018']

Et grâce aux tableaux récapitulatifs générés automatiquement, il est possible de vérifier d'un coup d'œil que chaque joueur est bien informé des faits le concernant, que la distribution des informations clés est plus ou moins équilibrée, et que les événements majeurs sont correctement enregistrés dans les fiches récapitulatives.

**Extrait du résumé automatique des « faits » du scénario :**

*Les noms de personnages sont en italique lorsqu'ils ont le « fait » en question uniquement dans leur fiche de personnage complète, et non dans leur fiche récapitulative.*

![Image](https://cdn-media-1.freecodecamp.org/images/1*ytuGvYFYAwYxk2h9mf-Z_A.png)

En conséquence, le maître de jeu peut s'appuyer tranquillement sur ses propres documents (auto-générés) pour mettre en place et surveiller le jeu : scénario détaillé, planning de la soirée, checklist du matériel et des écrits à placer dans les locaux, résumé automatique des missions et compétences spéciales de chaque joueur…

En plus de cela, cette machine peut également envoyer ses documents de jeu, par email, à chaque joueur (par exemple, fiche de personnage et documents initialement possédés). Cela évite le drame qui attend chaque organisateur : gâcher la surprise d'un participant en lui envoyant les mauvais documents.

Ce système ajoute évidemment une certaine complexité au projet, par rapport à quelques fichiers Word/LibreOffice classiques. Mais il apporte un soutien inestimable en termes d'évolutivité et de robustesse du scénario, détectant les incohérences et automatisant les tâches fastidieuses. Personnellement, il m'a sauvé plus d'une fois, lorsque j'ai interverti les noms de certains personnages dans les fiches, ou oublié de prévenir certains joueurs des nouveaux méfaits qu'ils étaient censés avoir commis dans le passé.

### Comment mettre en place un tel processus ?

**Étape 1 :** S'éloigner des fichiers bureautiques riches (docx, odt, pdf…) pour un format de texte brut, facilement manipulable, où la mise en forme est explicitement indiquée par des caractères spéciaux. Les documents *en jeu* avec des besoins graphiques et typographiques élevés (affiches, parchemins, journaux…) peuvent être mis de côté, dans des fichiers bureautiques plus usuels : Word, LibreOffice, InDesign…

**Exemple de texte brut (format restructuredtext) :**

```restructuredtext
Manuel du Maître de Jeu
############################

.. contents:: Table des Matières
    :depth: 2

Concept de la soirée mystère
================================

**Chrysalis:Mindstorm** est un huis clos entre `enquête 
<https://fr.wikipedia.org/wiki/Enqu%C3%AAte>`_ criminelle et conflit
géopolitique, où des agents secrets et des civils de divers pays se 
retrouvent face à un *redoutable* inspecteur de police, qui va les 
pousser dans leurs derniers retranchements.
```

**Rendu de ce texte une fois converti en PDF :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*gzF6lDg3aFQ4cYiHogwlUw.png)

**Étape 2 :** Utiliser un gestionnaire de versions pour les fichiers du scénario. Cela permet de revenir en arrière à tout moment, d'éviter des modifications de fichiers accidentelles horrifiantes, et de vérifier la cohérence de chacune des modifications apportées (renommage d'un lieu, ajout d'informations pour un groupe de joueurs…).

**Visualisation d'une modification apportée aux règles du jeu :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*coZjpx5FCi1RERBRrOYIOQ.jpeg)

**Étape 3 :** Ajouter un petit moteur de traitement, pour enrichir le texte avec des fonctionnalités simples et pratiques : permettre à un fichier d'en inclure un autre, définir des blocs de texte réutilisables, insérer des variables (par exemple, la date d'un événement crucial, différente pour chaque session de la soirée mystère), afficher différentes informations selon l'équipe à laquelle appartient le joueur ciblé…

**Étape 4 :** Automatiser les vérifications de cohérence. Pour cela, j'ai créé des balises spécifiques dans le moteur de traitement, que j'ai ensuite insérées au fur et à mesure de l'écriture :
— La balise {% fact %} sert à annoncer un fait (par exemple, « untel a tenté de voler Loyd Georges »), et à indiquer si le joueur en est l'auteur ou simplement un témoin.
— La balise {% hint %} permet de demander l'existence d'un indice physique (lettre, objet…) à remettre au joueur.
— La balise {% symbol %} garantit qu'une valeur est unique dans tous les fichiers du scénario (par exemple, l'heure exacte d'un crime), tout en évitant l'utilisation de « variables » qui obscurcissent le texte.

**Exemple d'utilisation de balises spéciales pour enrichir un texte de scénario :**

> À l'attention de {{agent_gamma_fake_name }} : le pays de {% symbol "Balberith" pour "first_country_at_war" %} est entré en guerre, suite au complot mené par l'agent Epsilon {% fact "agent_epsilon_triggered_war" as author %}. Vous avez un témoignage signé par lui et attestant de cela. {% hint "epsilon_signed_testimony_for_agent_gamma" is needed %}.

Comme on peut le voir, ces balises ont chacune leur propre syntaxe, et peuvent utiliser d'autres fonctionnalités du moteur de traitement, comme les variables (dont nous avons un exemple avec _{{agent_gamma_fake_name }}_).

**Étape 5 :** Relier tout cela avec des scripts, qui automatiseront les différentes étapes de création des documents de jeu : collecte des données utiles (y compris les photos des joueurs), distribution des pages de scénario pour chaque participant (contexte global, contexte personnel, règles du jeu…), transformation en format PDF, et génération de fiches récapitulatives pour le maître de jeu.

**Certains des documents PDF générés, à côté de leurs sources en texte brut :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*weQW6mnReW0hV9TNieakNw.png)

### L'avenir

Tout cela est très bien, mais qu'en est-il du reste de la communauté du jeu de rôle ? Peut-elle bénéficier, plus largement, des fonctionnalités offertes par ce système d'assistance à l'écriture de scénarios ?

La réponse est oui. Cependant, comme on l'a vu dans les étapes ci-dessus, cet outil nécessite une certaine affinité avec des processus généralement réservés au développement informatique ; une affinité que beaucoup d'auteurs de GN n'ont pas.

Je suis donc à l'écoute des auteurs tentés par l'expérience, afin de voir avec eux comment ils travaillent, quels formats et outils ils sont capables d'utiliser, et comment ce système pourrait être généralisé pour s'adapter à leur usage. Je pourrais alors voir à extraire ce code (qui est actuellement fortement lié à la structure des fichiers de jeu Chrysalis), pour le rendre plus autonome et plus facilement déployable.

Notez que des logiciels comme [Twine](https://twinery.org/) permettent déjà de créer des scénarios de manière assez simple, avec un mini-langage pour définir des variables et utiliser des opérations logiques. La machinerie Pychronia Tools n'a donc de sens que pour le très haut niveau d'intégration qu'elle offre, avec ses vérifications de cohérence automatisées et ses scripts de génération de bout en bout.

Intéressé par ce système d'assistance à l'écriture de scénarios ? N'hésitez pas à me contacter en utilisant les informations sur le [site Chrysalis](https://chrysalis-game.com/fr/cms/contacts/).

### Annexe : Détails pour les personnes initiées à l'informatique

Ma machinerie est basée sur le langage Python et son écosystème de manipulation/création de documents.

Quant au format de « texte brut » du scénario, de nombreux « langages de balisage » peuvent être utilisés à cette fin : restructuredtext, markdown, textile, latex, voire html… J'ai choisi [restructuredtext](http://docutils.sourceforge.net/docs/user/rst/quickstart.html) pour sa clarté, sa polyvalence, et son intégration avancée avec le langage Python. Pour éditer ces fichiers texte, bien sûr, Pycharm, Notepad++, Geany, ou un simple bloc-notes peuvent faire l'affaire.

Pour le gestionnaire de versions (ou « VCS »), j'ai choisi Git et son excellente interface graphique TortoiseGit (disponible uniquement sous Windows, malheureusement). Mercurial, Bazaar, DARCS, ou d'autres sont tout aussi pertinents. À minima, on peut utiliser la sauvegarde versionnée de fichiers proposée par Dropbox et al., même si elle n'offre que peu de fonctionnalités pour visualiser les différences entre plusieurs étapes d'écriture…

**Visualisation, via GIT, des ensembles de modifications apportées au scénario :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*GzYryvzHO22pB5UoanSL7Q.png)

Concernant le moteur de template utilisé pour traiter les fichiers texte (et pour les balises spécifiques), j'ai finalement intégré le puissant [Jinja2](http://jinja.pocoo.org/), qui permet de créer des variables et des macros directement dans les templates. Les données traitées par ce moteur proviennent, dans mon cas, d'une structure arborescente de fichiers Yaml, mais de nombreuses autres sources (fichier python, csv, xml…) s'intègrent très facilement.