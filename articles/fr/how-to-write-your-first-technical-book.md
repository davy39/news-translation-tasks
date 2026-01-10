---
title: 'Comment écrire votre premier livre technique : outils, techniques et ressources
  pour les auteurs développeurs débutants'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-22T19:35:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-your-first-technical-book
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/writing-cover.jpg
tags:
- name: books
  slug: books
- name: technical writing
  slug: technical-writing
- name: writing
  slug: writing
- name: writing tips
  slug: writing-tips
seo_title: 'Comment écrire votre premier livre technique : outils, techniques et ressources
  pour les auteurs développeurs débutants'
seo_desc: 'By Shubham Chadokar

  Recently, I wrote my first technical book – yes, I finally finished it. ?This project
  was on my list for a long time. And now that I''ve finally completed it, I''d like
  to share my experience with everyone.

  In this post, I tried to ...'
---

Par Shubham Chadokar

Récemment, j'ai écrit mon premier livre technique – oui, je l'ai enfin terminé. ?  
Ce projet était sur ma liste depuis longtemps. Et maintenant que je l'ai enfin terminé, j'aimerais partager mon expérience avec tout le monde.

Dans cet article, j'ai essayé de documenter tout mon parcours d'écriture du livre. Je discute de tout, de la motivation et des obstacles aux outils, techniques et ressources.

Mon livre se concentre sur l'outil [Hyperledger Composer Blockchain](https://schadokar.dev/ebooks/). Il est complètement gratuit et n'est disponible pour l'instant qu'au format PDF.  

Tous ces points sont également utiles pour l'écriture de blogs techniques. Alors, commençons et plongeons dans ce que j'ai appris.

# Motivation

J'écris des articles et des tutoriels techniques depuis fin 2018. À présent, je suis assez à l'aise avec le processus d'écriture d'un article ou d'un tutoriel. Je comprends comment aborder l'article et quels outils utiliser.

Mais lorsqu'il s'agit d'écrire un livre – et surtout un livre technique – le domaine est assez différent. 

Ma motivation était la curiosité. Je me demandais comment les auteurs écrivent des livres. Quel est leur processus de réflexion ? Quels outils utilisent-ils ? Et bien sûr, comment cela fait-il d'écrire un livre ? ?

Je suis ingénieur logiciel et je travaille sur la Blockchain depuis 2018. J'ai appris à connaître différentes blockchains comme Ethereum et Hyperledger Fabric. J'ai également utilisé de nombreux outils comme [truffle](https://www.trufflesuite.com/), [remix](https://remix.ethereum.org/) et [hyperledger composer](https://hyperledger.github.io/composer/).

Il y avait quelques sujets différents dont je voulais parler, comme **Ethereum** ou **Hyperledger Fabric**. 

Mais comme c'était mon premier livre, ces sujets n'étaient pas idéaux pour moi. Ils auraient nécessité beaucoup plus de temps et d'efforts que je ne pouvais en donner. Alors, j'ai choisi un sujet simple : Hyperledger Composer.

# Premier obstacle
Avant de commencer, je me demandais quel outil ou éditeur utiliser pour écrire le livre. 

Devrais-je écrire dans MS Word, Google Docs, ou utiliser autre chose ?  
Le problème majeur était de savoir comment formater correctement les extraits de code. Ces éditeurs ne sont pas conçus pour l'écriture technique. 

Il existe différentes solutions pour ajouter du code, mais cela nécessiterait un formatage supplémentaire.  

J'ai lu de nombreux articles sur **les bons outils disponibles pour l'écriture de livres techniques**. J'en ai essayé beaucoup, mais aucun ne m'a satisfait. J'ai perdu beaucoup de temps à chercher l'outil parfait.  

Finalement, j'ai réalisé que les éditeurs ne font que faciliter le processus d'écriture et rendre la gestion du livre plus simple. Mais ce qui compte vraiment, c'est le contenu. Alors, j'ai arrêté de chercher l'éditeur parfait et je suis revenu aux bases.

## Les bases : VS Code

J'ai utilisé mon éditeur de code préféré pour écrire le livre. Oui, **VS Code** ?. 

Après avoir passé des jours à chercher sur Internet, aucun article ne suggérait que vous aviez besoin d'un outil ou d'un éditeur spécifique pour écrire un livre technique. VS Code ou Atom seraient plus que suffisants.

J'ai écrit tout le livre dans **VS Code** dans mon format markdown préféré. Pour faciliter mon écriture, j'ai utilisé quelques plugins markdown comme **Markdown All in One** et **Markdown Preview Enhanced**.  

Le premier plugin vous aide à écrire en markdown tandis que le second aide en mode aperçu. Il montre comment le markdown apparaîtra et se comportera après sa conversion en HTML ou d'autres formats. 

**Markdown All in One** a également un mode aperçu, mais **Markdown Preview Enhanced** dispose de plusieurs thèmes et options pour exporter le fichier markdown en HTML, PDF et d'autres formats lisibles comme epub ou Mobi. 

Juste un petit conseil – ces autres formats nécessitent que vous installiez **Pandoc** sur votre machine.

> Je suis un utilisateur de Windows. Pour les utilisateurs de Mac, j'ai trouvé qu'il existe de nombreux éditeurs disponibles comme [bear](https://bear.app/), [ulysses](https://ulysses.app/) et bien d'autres.

Récemment, j'ai découvert qu'il existe de nombreux éditeurs markdown disponibles sur **Windows** et **MacOS** que vous pouvez utiliser pour écrire un livre. Consultez [Notion](https://www.notion.so/), [Typora](https://typora.io/), [iA Writer](https://ia.net/writer), et [SimpleNote](https://simplenote.com/).

En résumé, **ne perdez pas trop de temps à chercher l'éditeur parfait**. Commencez simplement à écrire dans l'éditeur de votre choix. Avec le temps, vous trouverez la solution.

# Deuxième obstacle

Ensuite, je me suis demandé par où commencer à écrire ? Comment devrais-je écrire ? Comment devrais-je aborder cela ?  

En bref, je voulais savoir exactement comment écrire ce livre pour que le lecteur en tire le meilleur parti.

Ces questions m'ont fait beaucoup réfléchir. Au début, j'ai changé mon approche 4 ou 5 fois.  

À ce stade, je suggère de prendre un peu de temps pour vraiment réfléchir à votre approche. Car une fois que vous êtes au milieu du livre, il ne sera pas facile de la changer.

### Posez les questions

Je me suis posé ces questions sur le livre et j'ai noté mes réflexions.

1. Qui est mon public cible ? Sont-ils débutants, intermédiaires ou experts ?
2. Ont-ils besoin de connaissances préalables sur le sujet ? 
3. Comment devrais-je organiser le livre ?
4. Comment devrais-je nommer les fichiers ou les chapitres pour qu'il soit facile de trouver chaque sujet ?
5. Comment devrais-je suivre ma progression ?
6. Comment devrais-je maintenir les versions des chapitres et les brouillons du livre ? Il y aura de nombreuses occasions où la dernière édition était en fait beaucoup meilleure que la version actuelle.

Ce sont quelques questions de base que je me suis posées, et elles ont été utiles.

## Mon approche

Je vais maintenant décrire l'approche que j'ai adoptée pour écrire ce livre.

### Créer une liste de tâches

Tout d'abord, j'ai créé une liste de tâches. Dans cette liste, j'ai noté tous les points principaux, les sujets, les sous-sujets, les références, la préface, la couverture, le titre, etc. 

J'ai ajouté toutes les idées qui me sont venues à l'esprit concernant le livre.

Je suggérerais de créer 2 listes de tâches : une sur papier et une autre en version numérique.  

Tout d'abord, notez tous les points sur papier. Une fois que vous avez tout noté, lisez-le 2-3 fois. Ensuite, quelles que soient les nouvelles idées qui vous viennent à l'esprit, notez-les.

Par exemple, si vous réfléchissez à la manière dont vous allez expliquer un sujet particulier, notez-le. Cela rendra votre travail beaucoup plus facile. Ensuite, lorsque vous commencerez à écrire sur ce sujet, vous pourrez vous référer à ces notes.

Une fois que vous avez une liste de **tâches** sur papier, créez une copie numérique et enregistrez tous les points dans l'ordre chronologique.  

Voici à quoi ressemblait ma liste de **tâches** :

#### Tâches

- [x] Index
- [x] Couverture
- [x] Titre
- [x] Sous-titre
- [x] Préface
- [x] Qu'est-ce que la Blockchain et Hyperledger Fabric ?
- [x] Introduction à Hyperledger Composer
- [x] Exigences et configuration de l'environnement
  - [x] Azure
  - [x] AWS
  - [x] GCP
- [x] Objectif du projet
- [x] Configuration du projet dans Composer
- [x] Fichier de modèle
  - [x] Définition
  - [x] Langage de modélisation
  - [x] code du projet
- [x] Fichier de script
  - [x] Définition
  - [x] syntaxe
  - [x] code du projet
- [x] Fichier de requête
  - [x] Définition
  - [x] Langage de requête
  - [x] code du projet
- [x] Fichier ACL
  - [x] Définition
  - [x] syntaxe
  - [x] code du projet
- [x] Déploiement dans Composer Playground
- [x] Test dans Composer Playground
- [x] Exporter le .bna
- [x] Serveur Rest Composer
- [x] Frontend
- [x] Conclusion
- [x] Références
- [x] À propos de moi
- [x] Vérification grammaticale 1
- [x] Vérification grammaticale 2
- [x] Lire le brouillon
- [x] Lire le brouillon final
- [x] Format PDF
- [x] Ajouter le numéro de page au PDF
- [x] Nouveau chapitre commence sur une nouvelle page
- [x] Note de remerciement
- [x] Licence
- [x] Quatrième de couverture

J'ai utilisé le format markdown pour ma liste de **tâches**. Vous pouvez utiliser le format qui vous semble le plus facile.

## Commencez petit mais commencez

Gardez à l'esprit que vous n'avez pas besoin d'écrire sur chaque sujet dans l'ordre. Il peut y avoir de nombreux sujets qui dépendent des sujets précédents, mais d'autres non. 

De plus, vous n'avez pas à finir d'écrire sur le sujet en une seule fois. Quels que soient les sujets avec lesquels vous vous sentez à l'aise, commencez par là.

Votre objectif devrait être de commencer le livre. Essayez d'écrire 10-20 % de votre livre en quelques semaines. Une fois que vous commencez, cela vous rappellera constamment que vous devez terminer le livre. Avec le temps, vous réaliserez que cela devient un excellent motivateur.

Si un sujet vous est moins familier, ne vous inquiétez pas. N'hésitez pas à demander de l'aide sur Internet. Lisez comment d'autres personnes l'ont expliqué. Inspirez-vous et écrivez-en à votre manière. 

Et n'oubliez pas – Si vous utilisez du contenu provenant du travail d'autres personnes, assurez-vous de les en informer, de le citer correctement dans votre texte et de lister leur travail comme référence à la fin.

> Considérez cela comme une courtoisie professionnelle. -- John Wick ?

## Ordre chronologique

Il m'a fallu un certain temps pour comprendre l'importance d'avoir une convention de nommage des fichiers. 

Au début, j'ai commencé à suivre une convention de nommage _Chapitre 1_, _Chapitre 2_ pour chaque sujet. Cela s'est avéré être une mauvaise idée. 

Le problème avec ce schéma de nommage est que vous devez maintenir un fichier séparé où vous expliquez ce qu'il y a dans le fichier. Ou vous devez ouvrir chaque fichier pour voir ce qu'il contient. 

Un autre problème est que si vous ajoutez un nouveau chapitre entre les autres, vous devez renommer tous les chapitres suivants.

Il y a deux conventions que j'ai trouvées utiles, mais chacune a ses inconvénients.

Une option est d'utiliser **numéro de chapitre-sujet** : Nommer le fichier avec un numéro de chapitre suivi du sujet du chapitre. Comme ceci **10-introduction-de-la-blockchain**. 

Nommer le numéro de chapitre en 2 chiffres. Cela vous aidera à ajouter des sous-sections au même chapitre dans différents fichiers. Comme ceci **11-histoire-de-la-blockchain**. 

Un autre avantage de cette convention de nommage est qu'elle affichera tous les fichiers dans l'ordre des chapitres de votre livre.

**Inconvénient** : L'ajout d'un nouveau chapitre entre les autres nécessite que vous renommiez tous les chapitres suivants.

La deuxième option est d'utiliser **le nom du fichier comme sujet** : Nommer tous les fichiers avec le nom du sujet. Cela vous donnera la liberté d'écrire les sujets dans un ordre aléatoire. Et vous pouvez maintenir l'ordre du livre dans votre liste de tâches.

**Inconvénient** : Tous les fichiers seront classés par ordre alphabétique. Après 10-15 fichiers, il sera difficile de suivre tous les fichiers, et il sera plus difficile de les rassembler dans un brouillon.

Finalement, j'ai suivi la deuxième méthode. Cela a bien fonctionné pour moi.

Pour créer un brouillon, j'ai créé un script Node.js. Dans ce script, j'ai entré tous les sujets dans un tableau. Ensuite, j'ai créé un fichier brouillon et j'ai ajouté tous les sujets. Bien sûr, en les lisant d'abord ?. Quelques avantages d'être ingénieur logiciel ?.

Ce script a été un sauveur lorsque je faisais des modifications. Plusieurs fois, j'ai mis à jour les sujets ou les images. J'ai corrigé les erreurs grammaticales. Ici, Grammarly m'a vraiment sauvé... mais pas complètement car j'utilisais la version gratuite. ?

## Chronique du parcours du livre

Écrire un livre n'est pas un sprint, c'est un marathon. Enregistrez toujours votre travail lorsque vous terminez un sujet ou que vous avez fini pour la journée. 

Le lendemain, vous pourriez avoir une nouvelle idée pour le même sujet que vous avez déjà terminé. Vous pourriez passer une heure dessus, mais cela ne semble pas bon. Dans ce cas, ANNULER est génial mais cela a aussi des limites (et ses limites varient d'un éditeur à l'autre). **Ne testez pas trop ses limites**.

Au lieu de vous fier à l'éditeur ou de faire des copies en double, j'ai utilisé **Git** pour le contrôle de version. Ne pensez pas que **git** ne peut être utilisé que pour gérer votre code. C'est un outil polyvalent et ses applications ne sont limitées que par votre imagination.

Pour les lecteurs qui ne connaissent pas **git** :

> Git est un système de contrôle de version distribué pour suivre les changements dans le code source pendant le développement logiciel. Il est conçu pour coordonner le travail parmi les programmeurs, mais il peut être utilisé pour suivre les changements dans n'importe quel ensemble de fichiers. --[Wikipedia](https://en.wikipedia.org/wiki/Git)

Vous n'avez pas besoin d'apprendre tout sur **git** pour l'utiliser pour l'écriture. Les commandes de base comme **init**, **add**, **commit**, **logs** et **checkout** sont plus que suffisantes pour maintenir vos versions et garder votre texte accessible et sécurisé.  

Il existe de nombreuses plateformes d'hébergement de code Git disponibles, comme [GitHub](https://github.com/), [GitLab](https://about.gitlab.com/) et d'autres. Pour héberger votre livre sur l'une de ces plateformes, vous pouvez suivre les étapes ci-dessous :

1. Créez un compte. Mon choix personnel est **GitHub**.
2. Créez un dépôt privé avec les choix par défaut. Vous pouvez changer sa visibilité en public à l'avenir.
3. Suivez les instructions fournies une fois le dépôt créé. Basiquement, dans cette étape, vous connectez votre **Git** local à votre dépôt hébergé.
4. Apprenez 2 commandes supplémentaires, **push** et **pull**. Utilisez **push** pour envoyer les modifications locales vers le dépôt cloud et utilisez **pull** pour obtenir le contenu du cloud.

Après cela, chaque fois que vous faites des modifications, faites simplement **add**, **commit** et **push**. Simple, n'est-ce pas ? ?  

Après quelques commits, vous vous sentirez à l'aise avec **git**.  

> Consultez cet article incroyable pour en savoir plus : [Apprendre Git et le contrôle de version en une heure](https://www.freecodecamp.org/news/learn-git-and-version-control-in-an-hour/)

# Les outils et ressources que j'ai utilisés

J'ai utilisé de nombreux outils et ressources lors de l'écriture, de l'édition, de la mise en forme et de la conception du livre.

## Écriture

Pour l'écriture, j'ai utilisé l'éditeur VS Code avec quelques plugins markdown, comme je l'ai discuté ci-dessus.

Pour les emojis, j'ai utilisé [copier et coller des emojis](https://getemoji.com/).

## Édition

Pour corriger les erreurs grammaticales, j'ai utilisé la version gratuite de Grammarly. Dans la version gratuite, il corrige toutes les erreurs de base comme les articles incorrects ou manquants, les prépositions, les virgules, etc.

J'ai utilisé l'[éditeur de PDF en ligne](https://www.ilovepdf.com/add_pdf_page_number) pour ajouter des numéros de page au livre.

## Mise en forme

J'ai utilisé le plugin Markdown in Preview dans VS Code pour générer le format PDF. J'ai utilisé la mise en forme markdown par défaut de Git. Vous pouvez changer la mise en forme dans les paramètres.

### Sauts de page dans le PDF

Comme j'écrivais au format markdown, la sortie PDF était incohérente. Par exemple, il commence un nouveau sujet à partir de la dernière page au lieu d'une nouvelle page. 

Pour corriger cela, j'ai utilisé le code de saut de page `html` à la fin de chaque sujet.

```html
<div style="page-break-after:always;"></div>
```

Cela fera en sorte que le contenu qui suit commence sur une nouvelle page.  
Vous pouvez également ajouter la fin de la séquence de pages comme \***\*\*\*\*** ceci.

```html
<div style="page-break-after:always; display:block; text-align:center; border:none">*****</div>
```

### Page À propos de moi

Dans la section **À propos de moi** de mon livre, j'ai divisé le contenu en deux colonnes : une brève présentation de moi et une photo de profil. 

Il m'a fallu un certain temps pour réaliser toutes les capacités du format markdown. Nous pouvons y ajouter du code `html` simple. Voici ce que dit ma page "à propos de moi" :

```html
<div >
  <img align="right" style="padding-left:65px" src="../images/profilepic.JPEG" width="400px" height="450px" />
</div>

Bonjour, je suis **_Shubham Kumar Chadokar_**.

Je suis ingénieur logiciel et dans ma courte carrière de presque 4 ans, j'ai eu l'opportunité de travailler sur la Blockchain, Nodejs, Golang et Docker.

J'ai appris d'autres technologies, mais ce sont mes principaux centres d'intérêt. J'aime écrire des articles et des tutoriels sur les nouvelles technologies en suivant une approche pratique. C'est mon premier livre.

Le développement front-end n'est pas ma spécialité, et c'est pourquoi je ne l'ai pas inclus dans le livre.

Si vous avez des questions ou des interrogations, n'hésitez pas à m'envoyer un e-mail.

:e-mail: [hello@schadokar.dev](hello@schadokar.dev)
:globe_with_meridians: [schadokar.dev](https://schadokar.dev)
<img src="https://github.githubassets.com/images/icons/emoji/octocat.png" style="width:20px;" />[github.com/schadokar](https://github.com/schadokar)
```

Pour octacat, j'ai utilisé la balise `img`.

Cela ressemble à ceci.  

![about-me-3](https://www.freecodecamp.org/news/content/images/2020/09/about-me-3.PNG)

### Page de remerciements

J'ai ajouté une page de remerciements pour exprimer ma gratitude à la **communauté Hyperledger Composer** pour leur travail. J'ai essayé d'ajouter le contenu au milieu de la page.

```html
<div style="padding-top:40%; text-align: center; font-size:35px;">
Merci <img src="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/microsoft/209/person-with-folded-hands_1f64f.png" style="width:40px" />
</div>
<div style="text-align: center; font-size:25px;">
Je veux particulièrement remercier toute la
<a href="https://github.com/hyperledger/composer/graphs/contributors">communauté Hyperledger Composer</a> pour avoir créé un
outil aussi incroyable. De nombreux développeurs sont entrés dans le domaine de la blockchain grâce à la simplicité du composer. <br />
Il est malheureux qu'il soit obsolète, mais il établit un excellent exemple d'automatisation facile,
enveloppant un Hyperledger Fabric complexe dans le Hyperledger Composer facile à utiliser.
</div>
```

Cela ressemble à ceci.  

![thanks-note](https://www.freecodecamp.org/news/content/images/2020/09/thanks-note.PNG)  

## Titre et sous-titre du livre

Le titre du livre doit rendre le contenu du livre clair en quelques mots ou une phrase courte. 

Pendant que vous écrivez le livre, notez tous les mots-clés que vous utilisez. Cela vous aidera à trouver un excellent titre. Vous voulez capturer l'essence du livre et faire savoir aux lecteurs, par exemple, s'il est théorique ou plus pratique.

Un sous-titre doit donner aux lecteurs plus de détails sur ce qu'ils obtiendront de ce livre ou ce qu'ils vont apprendre. 

Un sous-titre en une phrase est idéal et ne doit pas dépasser deux phrases. Ne faites pas trop – laissez les lecteurs lire le livre. L'idée est de donner aux lecteurs un aperçu du livre complet en une phrase mais sans tout révéler ?.

Le titre de mon livre est **_Playtime with Hyperledger Composer_** et le sous-titre est **Créer un projet de gestion de la chaîne d'approvisionnement dans la Blockchain en utilisant Hyperledger Composer**.

Lorsque vous commencez à écrire votre livre, ne passez pas trop de temps sur le titre du livre. Lorsque vous aurez terminé l'écriture, vous serez dans une bien meilleure position pour décider du titre du livre. Tout est écrit, vous savez de quoi il s'agit, et ce que les autres en tireront. 

Dans mon cas, j'ai changé le titre du livre et la couverture du livre au dernier moment avant de le publier. Avant cela, c'était si ennuyeux ?.

## Conception de la couverture du livre

Vous avez peut-être entendu l'idiome **Ne jugez pas un livre par sa couverture**.  
Mais la réalité est que la couverture d'un livre est très importante. C'est la face du livre. 

Essayez de la garder simple et informative. Ne faites pas trop. Un titre simple et un sous-titre court avec une ou deux images suffisent.   

J'ai commencé à concevoir la couverture du livre en prenant des références d'autres livres et en essayant de les éditer dans Paint. Le résultat était un désastre complet, et je ne pouvais pas penser à quelque chose de bien. 

Puis j'ai réalisé que _la conception n'est pas ma tasse de thé_. J'ai décidé d'engager un freelance pour cela, alors j'ai consulté des sites de freelance comme **UpWork** et **Fiverr**.

Ensuite, j'ai trouvé [**Canva**](https://canva.com). C'est un outil si génial. Incroyable ! ? ? ? ?

> Canva est une plateforme de conception graphique qui permet aux utilisateurs de créer des graphiques pour les réseaux sociaux, des présentations, des affiches et d'autres contenus visuels. Il est disponible sur le web et mobile et intègre des millions d'images, de polices, de modèles et d'illustrations. [Wikipedia](https://en.wikipedia.org/wiki/Canva)

J'ai utilisé l'un des modèles de la section couverture de livre de Canva et j'ai créé ma couverture de livre. Pas mal, n'est-ce pas ? ?

![book-cover](https://www.freecodecamp.org/news/content/images/2020/09/book-cover.png)


## Licence

J'ai écrit ce livre par curiosité et pour le plaisir. Donc, je voulais qu'il soit gratuit et open-source, mais je ne voulais pas que d'autres le monétisent. Sans licence, il n'y a aucune restriction.  

J'ai cherché un moment et j'ai trouvé une excellente réponse sur StackOverflow concernant les licences gratuites, [Licences Creative Commons](https://creativecommons.org/licenses/).

> **Creative Commons est une organisation à but non lucratif qui aide à surmonter les obstacles juridiques au partage des connaissances et de la créativité pour répondre aux défis pressants du monde.**

Ils ont fourni un [formulaire](https://creativecommons.org/choose/) avec quelques questions liées au type de licence que vous souhaitez. Remplissez le formulaire et voilà ?, votre licence est prête. Copiez et collez-la ou utilisez le lien intégré.

![license](https://www.freecodecamp.org/news/content/images/2020/09/license.PNG)



# Publier votre livre

Il existe de nombreuses options parmi lesquelles vous pouvez choisir pour publier votre livre. Vous pouvez approcher une maison d'édition et envoyer votre brouillon. Si elles veulent le publier, vous pouvez conclure un accord.

Après cela, la maison d'édition s'occupe des autres processus comme la mise en forme, l'édition de votre livre, la création d'une couverture de livre attrayante, toutes les licences, le processus de publication et, surtout, le marketing.

En bref, si vous voulez monétiser votre livre et que vous attendez un bon montant, alors une maison d'édition est la meilleure option disponible.

Une autre option est l'auto-édition. Oui, nous pouvons auto-publier nos propres livres. Amazon's [Kindle Direct Publishing](https://kdp.amazon.com/en_US/) offre une excellente plateforme pour cela. C'est gratuit et il publie le livre dans le monde entier. 

Vous obtiendrez 70 % des profits pour chaque vente. Le kdp s'occupe de tout le processus de publication. Vous devez simplement écrire le livre, le télécharger et le formater. 

Vous entrez simplement le prix que vous souhaitez facturer, ainsi que quelques informations de base sur le livre et sur vous-même. Vous pouvez suivre leurs tutoriels pour plus d'informations – ils ont fait un excellent travail.

Mais je voulais garder mon livre gratuit et je n'avais pas la patience pour les processus ci-dessus. Donc, je l'ai auto-publié sans utiliser de tiers. 

J'ai simplement converti le livre au format PDF et je l'ai enregistré dans un bucket AWS S3 afin que tout le monde puisse le télécharger. Ensuite, j'ai hébergé le livre sur mon site web. Simple. ?

# Partagez votre travail

Une fois que vous avez terminé votre chef-d'œuvre, il est temps de le montrer au monde.  
Si vous ne vous êtes pas associé à un éditeur ou même si vous l'avez fait, vous devez faire connaître votre livre.

Ce sont les quelques plateformes que j'ai utilisées, mais ne vous limitez pas.

## LinkedIn
LinkedIn est une plateforme professionnelle et de nombreux développeurs y sont présents, quelle que soit leur spécialité dans le monde de la technologie. Vous y trouverez également des personnes de toutes les professions, vous l'avez nommé. 

Partagez votre travail avec eux, demandez des commentaires. 90 % du temps, vous obtiendrez une réponse. J'ai partagé mon travail avec Dan Selmon, l'un des contributeurs d'Hyperledger Composer, ainsi qu'avec Srinivas Mahankali, qui a écrit de nombreux livres sur la Blockchain. 

Ils ont tous deux été très utiles et ont donné leur avis honnête. Je suis reconnaissant à Dan, qui a même proposé de partager le livre parmi son réseau sur LinkedIn et Twitter. ?

## Reddit 
Reddit est un hub communautaire. Vous y trouverez de nombreuses communautés actives sur divers sujets. Vous devez simplement rejoindre la communauté pertinente pour votre travail et le partager là-bas. 

Vous trouverez beaucoup de membres actifs sur Reddit, dans ces groupes, et ils ne sont pas timides pour partager leur opinion. S'il y a une marge d'amélioration, certains d'entre eux pourraient proposer de l'aide. 

_Mais avant de partager, LISEZ LES DIRECTIVES. Si vous violez l'une d'entre elles, ils supprimeront votre publication._

## Twitter 
Twitter n'est pas seulement une plateforme sociale où les gens partagent leurs opinions. Donc, ne le sous-estimez pas. 

Si vous aimez les faits et les chiffres, voici : il y a 1,3+ milliard de comptes sur Twitter, 330 millions d'utilisateurs actifs mensuels, 152 millions d'utilisateurs actifs quotidiens et 500 millions de tweets par jour. C'est énorme. 

Vous devez simplement rédiger votre message et sélectionner les bons mots-clés dans la limite de 280 caractères et vous pouvez potentiellement atteindre un large public.

## Blogs
Faites quelques recherches et découvrez quelles publications ou magazines numériques publient des articles dans la catégorie de votre livre. Partagez le résumé et les détails de votre livre avec eux. 

Demandez-leur s'ils peuvent écrire un article sur votre livre. Ou vous pouvez écrire un article sur votre livre et partager le brouillon avec ces publications.

Il existe également de nombreuses autres plateformes que vous pouvez essayer – il suffit de faire un peu de recherche.

# Conclusion

C'était ma première expérience d'écriture d'un livre. Cela a pris un certain temps, mais cela en valait la peine. Maintenant, j'ai un autre badge sur mon portfolio. ?

J'ai beaucoup appris de cette expérience. Cet article sert de documentation de tout mon apprentissage pour quiconque souhaite écrire son premier livre ou son prochain livre.

Ci-dessous se trouve la liste finale des outils que j'ai utilisés jusqu'à présent.  
Toutes suggestions pour d'autres sont les bienvenues.

Merci d'avoir lu et n'oubliez pas de partager votre premier livre avec moi. ?

# Liste finale des outils que j'ai utilisés

- **Éditeur** : [Visual Studio Code](https://code.visualstudio.com/) avec 2 plugins Markdown
- **Outil de versioning** : Git et [GitHub](https://github.com)
- **Emojis** : [Copier et coller des emojis](https://getemoji.com/)
- **Vérification grammaticale** : [Grammarly](https://app.grammarly.com/)
- **Licence** : [Licences Creative Commons](https://creativecommons.org/licenses/)
- **Conception de la couverture** : [Canva](https://www.canva.com/)
- **Numéro de page PDF** : [éditeur de PDF en ligne](https://www.ilovepdf.com/add_pdf_page_number)
- **Stockage du eBook** : [Bucket AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html).
- **Hébergement du livre** : [Sur mon blog](https://schadokar.dev/ebooks/)


## Merci d'avoir lu
Si vous avez des commentaires ou des suggestions pour m'aider à améliorer cet article, veuillez me contacter sur [twitter](https://twitter.com/schadokar1) ou m'envoyer un [e-mail](hello@schadokar.dev).  

- [Lire mes autres articles](https://schadokar.dev)
- Abonnez-vous à [Ma Newsletter](https://schadokar.dev/newsletter/)


<span>Photo de couverture par <a href="https://unsplash.com/@thoughtcatalog?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Thought Catalog</a> sur <a href="https://unsplash.com/s/photos/writers?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>