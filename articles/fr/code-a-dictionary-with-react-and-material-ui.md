---
title: Cours React et Material UI – Codez un Dictionnaire
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-08-04T01:03:03.000Z'
originalURL: https://freecodecamp.org/news/code-a-dictionary-with-react-and-material-ui
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/dictionary.png
tags:
- name: React
  slug: reactjs
- name: youtube
  slug: youtube
seo_title: Cours React et Material UI – Codez un Dictionnaire
seo_desc: 'React continues to be a popular front-end JavaScript library. And you can
  improve your skills by building a dictionary project.

  We just published a course on the freeCodeCamp.org YouTube channel that will teach
  you how to create a dictionary app with...'
---

React continue d'être une bibliothèque JavaScript front-end populaire. Et vous pouvez améliorer vos compétences en construisant un projet de dictionnaire.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à créer une application de dictionnaire avec React et Material UI.

Vous apprendrez à créer un dictionnaire qui prend en charge plus de 12 langues. L'application permet également aux utilisateurs de basculer entre le thème clair et le thème sombre.

Roadside Coder a développé ce cours. Il a créé de nombreux cours populaires sur sa chaîne YouTube.

Voici les sujets abordés dans ce cours :

* Aperçu du Projet
* Initialiser une Nouvelle Application React
* API Google Dictionary
* Introduction à Material UI
* Installer Material UI
* Construire l'Application
* Déploiement sur Netlify
* Qu'est-ce qu'une PWA ?
* Convertir le Dictionnaire en une PWA
* Tester la PWA Finale

Regardez le cours complet ci-dessous ou sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/ToXna81iij0) (2 heures de visionnage).

%[https://youtu.be/ToXna81iij0]

## Transcription

(générée automatiquement)

Améliorez vos compétences React en apprenant à construire une application de dictionnaire.

Dans ce cours de roadside coder, le dictionnaire utilise Material UI et prend en charge 12 langues.

Salut tout le monde, bienvenue sur Free Code Camp.

Et aujourd'hui, nous allons construire une application de dictionnaire géniale en utilisant React JS et Material UI.

Donc, cette vidéo a deux sections.

Dans la première, nous allons construire et déployer cette application sur Netlify.

Et dans la deuxième section, nous allons la convertir en une PWA ou application web progressive, afin que vous puissiez installer cette application en tant qu'application native Android ou iOS sur votre téléphone.

Donc, explorons d'abord cette application.

Donc, ce dictionnaire prend en charge plus de 12 langues.

Cherchons un mot rapidement.

Cherchons "plain".

Maintenant, vous pouvez voir qu'il fournit la définition, l'exemple et le synonyme pour ce mot particulier.

Et non seulement une définition, il fournit toutes les définitions de ce mot particulier.

Et ce qui est encore mieux, c'est cet audio de prononciation, vous pouvez jouer ce "plane", il vous indique la prononciation de ce mot particulier.

Donc, oui, c'est génial.

Et je pense que seule la prononciation est prise en charge en anglais.

Donc, allons à la langue hindi.

Et je vais chercher mon nom, qui est "bu ish".

Et voilà, vous avez la signification de ce nom particulier.

Donc, c'est une application incroyable.

Maintenant, ce qui est mieux dans cette application, vous voyez dans ce petit coin ici, Tara, mode clair et mode sombre, il a cette fonctionnalité incroyable de cette application, vous pouvez l'implémenter en utilisant Material UI ainsi que "swamp".

C'est pourquoi j'ai choisi Material UI parce qu'il est si facile d'implémenter cette fonctionnalité de mode sombre et clair dans Material UI.

Aussi, si vous êtes intéressé par plus de tutoriels sur React JS, assurez-vous de consulter ma chaîne, qui s'appelle "roadside coder".

Récemment, j'ai téléchargé un projet de pile Myrn complet avec Redux sur ma chaîne, le lien sera dans la description ci-dessous.

Donc, sans plus attendre, commençons.

Donc, ce que nous allons faire, c'est ouvrir un nouveau projet rapidement, laissez-moi sélectionner mon dossier.

Je vais aller ici et sélectionner ce dossier particulier.

Je veux dire, laissez-moi fermer ces fichiers rapidement.

Oui, donc nous devons aller dans notre terminal et taper et PX créer une application React.

Et nous allons nommer cela, nous allons nommer cette application "word hunt", oops, j'ai fait une erreur.

Laissez-moi corriger ce NPM en NP x et appuyer sur Entrée.

Maintenant, ce qu'il va faire, c'est aller dans le dépôt NPM, il va prendre tous les fichiers nécessaires pour créer notre application React, je vais les amener dans ce dossier "word hunt".

Donc, en attendant, cela s'initialise.

Laissez-moi juste vous montrer l'API que nous allons utiliser pour cette application.

Donc, l'API que nous allons utiliser s'appelle Google Dictionary API.

C'est une API officielle de Google Dictionary créée par ce gars, me developer.

Merci beaucoup, le développeur pour cette API.

Donc, cette API nous fournit ces supports pour ces nombreuses langues.

Et comment allons-nous utiliser cette API, nous allons fournir un code de langue à cette API et un mot particulier.

Donc, cela va chercher les données sous cette forme.

Donc, nous allons voir comment nous pouvons gérer ces données plus tard.

Donc, vous pouvez voir que nous avons un support de langue, ou ici avec plus de ces nombreuses langues, l'anglais et l'espagnol, le français, etc.

Langues d'amour ici.

C'est une API incroyable.

Donc, oui, explorons également Material UI rapidement.

Donc, qu'est-ce que Material UI ? Material UI est une bibliothèque de composants React pour un développement web plus rapide et plus facile.

C'est une bibliothèque de composants React.

Maintenant, qu'est-ce qu'une bibliothèque de composants React ?

Donc, une bibliothèque de composants React est quelque chose qui vous fournit un composant préconstruit, non, un composant préconstruit dans cette bibliothèque particulière, que vous pouvez utiliser dans votre propre projet.

Laissez-moi vous montrer en cliquant sur "get started" ici.

Je vais fermer ce projet, qui était déjà ouvert.

Donc, oui, nous pouvons installer cela en utilisant NPM, installer material, UI slash core.

Donc, nous allons installer cela également.

Laissez-moi voir si notre application est installée.

Non, elle est encore en cours d'installation.

Attendons cela.

Cela nous fournit également des icônes Material UI.

Donc, cela, laissons cela pour plus tard.

Je vais vous montrer comment vous pouvez utiliser cette bibliothèque.

Maintenant.

Allons aux composants et allons à button.

D'accord, vous pouvez voir que nous avons différents types de boutons ici.

Donc, vous, ces boutons sont préconstruits dans la bibliothèque Material UI, vous pouvez simplement les importer directement en tapant une ligne.

Lorsque vous tapez cette ligne, ce bouton sera important.

Si vous changez la couleur en primaire, ce bouton sera importé.

Donc, oui, c'est une bibliothèque incroyable.

Et vous pourriez penser qu'il y a peut-être d'autres bibliothèques également.

Oui, il y en a.

Il y a une bibliothèque appelée react bootstrap.

J'utilise cette bibliothèque tout le temps.

Mais j'ai décidé d'utiliser cette bibliothèque Material UI parce qu'il est vraiment facile de travailler sur la fonctionnalité de mode clair et sombre également.

Et vous allez également découvrir quelque chose de nouveau dans React.

Donc, oui, bootstrap est vraiment, vous savez, une bibliothèque de type grand public, mais Material UI fait des vagues sur le marché.

Donc, nous utilisons une bibliothèque vraiment bonne.

Donc, que allons-nous utiliser de cette bibliothèque Material ? Nous allons utiliser quelque chose appelé text field en tant que limiteur de texte via text field là-bas.

Donc, en fait, nous allons utiliser ce composant ici.

Donc, ce qu'il va faire, c'est nous fournir un composant d'entrée préconstruit, où nous pouvons rechercher notre mot particulier, nous allons utiliser cela, et nous allons utiliser ce select où aller, oui, ici, le voici, nous allons utiliser ce composant select également.

D'accord, donc vérifions si notre application s'est initialisée avec succès ou non.

Oui, elle s'est initialisée avec succès, laissez-moi juste basculer vers cela en tapant cd, word hunt.

Ou ce que vous pouvez faire, c'est aller dans Fichier, Ouvrir le Dossier, et aller simplement à votre dossier particulier, dans mon cas, ce dossier et sélectionner ce dossier.

Et le voici, il a ouvert ce dossier particulier dans une fenêtre séparée.

Donc, allons-y.

Et nous allons d'abord installer Material UI.

Donc, oui, allons-y, où était cette ligne particulière ? Allons à l'installation et copions cette ligne ici, copions et collons-la ici.

Donc, cela va prendre un peu de temps pour installer Material UI, car Material UI est une énorme bibliothèque.

Donc, cela prend juste un peu de temps.

Donc, une fois installé, je serai de retour, une éternité plus tard.

D'accord, enfin, notre bibliothèque Material UI s'est installée avec succès.

Donc, ce que nous allons faire maintenant avec notre application React, c'est nous débarrasser des fichiers inutiles dont nous n'avons pas besoin pour l'instant.

Donc, supprimons ces fichiers, ces quatre fichiers ici.

Nous n'avons pas besoin de ces fichiers du tout.

Mais d'abord, laissez-moi juste exécuter cette application pour la première fois, et je vais vous montrer à quoi cela ressemble lorsqu'elle s'exécute pour la première fois.

Donc, la voici, notre application React a démarré avec succès.

Donc, ce que je vais faire, je vais juste l'amarrer ici.

Et je vais supprimer ces fichiers, comme je l'ai mentionné précédemment, donc supprimons simplement ces quatre fichiers.

Et allons-y et vous pouvez voir, cette application va maintenant se plaindre parce qu'elle utilisait ces fichiers quelque part.

Donc, vérifions simplement.

Donc, le logo était utilisé ici, nous n'en avons pas besoin, nous allons simplement nous débarrasser de toutes ces informations à l'intérieur de ce fichier ici.

Nous allons aller à index j s, nous allons supprimer cela.

Nous allons supprimer cela.

Et c'est à peu près tout.

Allons à notre app.

J s et exécutons Hello, world.

Hello, world.

Oui.

Le voici.

Hello, world, mais il démarre au centre.

Parce que je pense que nous n'avons pas encore supprimé ces tuiles.

Supprimons toutes ces tuiles dans l'app j s, nous ne allons pas toucher l'index CSS ou l'index j s pour l'instant.

Parce que nous n'en avons pas besoin pour l'instant ou à tout moment parce que nous n'avons pas besoin de faire quoi que ce soit avec eux.

Donc, oui, le HelloWorld a été imprimé avec succès ici.

D'accord, donc quoi ? Que allons-nous faire en premier ? Commençons par importer notre API dans notre application.

Allons sur notre site web API.

Était-ce le dictionnaire ? API ? Laissez-moi vérifier.

Oui, la voici.

API révolutionnaire, nous allons avoir besoin de ce lien particulier.

Mais comment allons-nous récupérer ce lien, nous allons utiliser un package appelé axios.

Donc, nous allons devoir installer ce package.

Donc, je vais ouvrir un autre terminal ici.

Et nous allons faire NPM I axios.

Et voici.

axios a été installé avec succès.

Donc, que allons-nous faire maintenant, nous allons créer une fonction.

Appelons cette fonction dictionary API.

Juste une seconde.

Oui, nous allons appeler cette fonction dictionary API.

Nous allons créer une fonction fléchée ici.

Et aussi, puisque nous récupérons l'API, nous devons rendre cette fonction asynchrone.

Nous devons en faire une fonction asynchrone.

Et nous allons taper try catch ici pour attraper si une erreur se produit dans notre application.

Donc, je vais simplement logger cette erreur ici.

Et à l'intérieur du bloc try, que allons-nous faire, d'abord, laissez-moi fermer ce terminal ici.

Donc, oui, nous sommes de retour en ligne dans le terminal, donc que allons-nous faire dans ce bloc try, nous allons récupérer cette API.

Donc, const, tapons data equals await.

Donc, nous avons besoin de ce mot-clé await à l'intérieur de cette fonction async, sinon, cela va nous donner une erreur.

Donc, axios dot get.

Donc, copions le lien du site web.

C'est le lien.

Copions ce lien ici.

D'accord, vous voyez, vous pouvez voir qu'il y a un code de langue, fournissons-le par défaut, un mot anglais, désolé, un mot-clé anglais, peu importe.

Donc, et pour le mot, je vais lui donner, donnons simplement plain.

D'accord, donc aussi, nous allons devoir appeler cette fonction quelque part.

Donc, nous allons appeler cette fonction, nous allons utiliser quelque chose appelé use effect.

Use effect.

Donc, qu'est-ce que use effect ? Laissez-moi clarifier cela.

Use effect est, lorsque vous gardez ces crochets vides ici, use effect est appelé chaque fois que votre composant est rendu pour la première fois.

Mais si vous mettez quelque chose à l'intérieur de ces crochets, ou ceux-ci sont appelés dépendances, alors ce qu'il va faire, c'est qu'il va être appelé chaque fois que ces variables vont changer.

Vous allez le savoir en cours de route, donc je vais appeler cette dictionary API à l'intérieur de ce use effect.

Voyons ce qui se passe.

useeffect n'est pas défini, évidemment, parce que nous n'avons pas importé use effect.

Oui.

Je vais importer.

Use effect.

Oups, qu'est-ce qui vient de se passer ? Use effect de react.

Oui.

Cela ne va pas me donner aucun de cela.

Non, oui.

Data est une valeur assignée, mais jamais utilisée.

Évidemment, nous avons appelé cette variable data, mais nous ne l'avons pas utilisée.

Faisons simplement un log de cela.

Voyons ce que nous obtenons dans cette API.

Je vais logger cela ici et aller dans notre navigateur et aller dans notre application.

Et vous pouvez voir que notre application est vide actuellement.

Faisons simplement un print de dictionary.

Oui, c'est tout.

Oui, dictionary, le mot là.

Donc, vérifions la console rapidement.

Que recevons-nous à l'intérieur de notre console ? Donc, nous recevons, nous recevons ces données, nous recevons appelé fake data headers, etc, dont nous allons avoir besoin de ce tableau de données ici.

Donc, à l'intérieur de ceux-ci, chaque élément de ce tableau, il y a une signification différente pour ce mot appelé plain.

Donc, allons à l'intérieur.

Allons à l'intérieur d'un élément.

Et à l'intérieur d'un élément, nous pouvons voir qu'il y a deux sections.

La première est la signification, et l'autre est la phonétique.

Donc, à l'intérieur de la phonétique, nous recevons ce lien.

Oui, c'est la prononciation pour ce mot particulier.

Donc, nous allons utiliser cela plus tard.

Tout d'abord, nous devons utiliser cet élément de significations à l'intérieur de cet élément de tableau.

Donc, allons à l'élément de signification, nous pouvons voir un autre tableau d'objets.

Donc, à l'intérieur de chacun de ces objets, nous avons une définition.

Nous avons un exemple.

Et nous avons des synonymes pour ce mot particulier.

Donc, c'est ainsi que cette API va fonctionner.

Donc, utilisons-la.

Donc, tout d'abord, qu'avons-nous besoin, nous allons aller à l'intérieur de cela et prendre ces données pour utiliser ces données et les stocker ailleurs, nous allons créer quelque chose appelé un état dans React, nous allons taper use state, whoops, use est, entrer, vous pouvez voir qu'il nous a donné ce code.

Et nous allons nommer cela meanings.

Et puisque cela va être un tableau, nous allons lui donner un tableau vide pour commencer.

Cette partie ici contient l'état initial de cet état particulier.

Et cela va être la fonction que nous allons utiliser pour changer l'état.

Et cela va être une variable réelle.

Laissez-moi vous montrer maintenant, cela va se plaindre parce que nous n'avons pas encore importé l'état.

Donc, importons simplement use state de react.

D'accord, donc nous allons importer toutes ces données à l'intérieur de ce set meanings.

Donc, entrons simplement et set avec une seconde, set meanings.

Et à l'intérieur de set meanings.

Nous allons taper data.

Whoops, data dot data.

Oui.

Et faisons simplement un log de ces meanings.

Je vais descendre ici et logger ces meanings.

Oui.

Vérifions notre navigateur.

Actualisons cette page une fois.

Et vous pouvez voir que nous obtenons uniquement la partie data de ce tableau API, donc nous avons besoin de ces meanings.

De toute façon.

Donc, voyons simplement ce que nous allons faire ensuite.

Donc, tout d'abord, ce que nous devons faire, c'est créer un autre état.

Pour notre mot qui sera vide par défaut.

Commençons par créer la section d'en-tête de notre application.

Tout d'abord, nous allons retourner à Material UI, ce que je vais vous présenter, c'est quelque chose appelé container dans Material UI.

Donc, ce container aide beaucoup à rendre votre application réactive.

Chaque fois que la taille de l'écran de votre application change, il va s'adapter à cette taille particulière.

Laissez-moi vous montrer tout cela rapidement.

Donc, à l'intérieur de cette app Dev, ce que je vais faire, c'est écrire cette balise container, et vous pouvez voir que VS code a automatiquement importé ce container.

Si vous allez et appuyez sur CTR espace, il va vous montrer les suggestions et vous pouvez cliquer sur la session particulière pour importer cela automatiquement.

Et je vais donner à ce container une largeur maximale de medium MD, vous pouvez parcourir toute cette largeur maximale medium small à l'intérieur de cette documentation de Material UI, vous pouvez voir qu'ils vous ont donné une taille small et accept, accept accept Trump.

Maintenant, nous verrons ce qui arrive à notre application, tapons simplement dictionary.

Voyons ce qui se passe.

D'accord, laissez-moi fermer ce terminal.

Et vous pouvez voir que votre dictionnaire a été aligné au centre du très centre.

Et vous pouvez voir lorsque je redimensionne cette fenêtre, vous pouvez voir qu'il s'adapte à cette taille particulière, le container aide notre écran à s'adapter à la taille de l'écran.

Donc, c'est ainsi que le container nous aide.

Laissez-moi lui donner quelques styles également.

Je vais lui fournir quelques styles en ligne avec une hauteur de 100, viewport.

Et la couleur de fond.

Couleur de fond où elle est oui, elle est ici.

Je vais lui donner hash 282 c trois, quatre.

Voyons comment cela ressemble.

Oui, cela a l'air bien.

Mais notre dictionnaire a été caché.

Donc, je vais lui donner une couleur également.

Donc, la couleur, elle va être blanche.

Oui, c'est à peu près tout.

Cela a l'air joli.

D'accord, donc nous allons donner quelques styles à notre container également.

Donc, comme vous le savez peut-être tous, Flexbox, ce qu'est Flexbox dans CSS, nous allons donner un style de display, flex afin que tous les éléments soient alignés de haut en bas, nous allons donner une direction de flex, colonne.

Nous y voilà.

Et nous allons lui donner une hauteur de 100 we edge et le contenu justifié.

D'accord, je ne vais pas le donner maintenant, je vais vous montrer plus tard pourquoi c'est utile pour nous.

Donc, tout d'abord, laissez-moi travailler sur cette partie d'en-tête ici où notre titre, et notre recherche et notre boîte de sélection vont se trouver.

D'accord, donc ce que je vais faire, c'est aller dans SRC, et créer un nouveau dossier appelé components.

Et à l'intérieur de ce composant, je vais créer un nouveau fichier ou un nouveau dossier appelé header.

Maintenant, dans le dossier header, lorsque vous créez un nouveau fichier appelé header dot j s, et un autre fichier pour CSS également header dot CSS.

Donc, allons à header dot j s, je vais vous montrer un raccourci, r A, F, C E, si vous allez et tapez cela et appuyez sur entrer, cela va vous donner un code de base pour une fonction react basique.

Donc, créons ce composant d'en-tête rapidement.

Tout d'abord, je vais simplement aller et taper header.

Ou je vais utiliser, disons, un titre ici.

Je vais lui donner une balise span.

Donnez-lui un nom de classe de titre.

Je vais d'accord.

Word, hunt.

Oui, cela a l'air bien.

Donnons-lui un nom de classe également.

Off header.

Oui, cela a l'air bien.

Importons simplement cela à l'intérieur de notre app, votre app.js.

Laissez-moi me débarrasser de ce dictionnaire ici.

Et je vais taper header.

Maintenant, vous pouvez voir qu'il donne des suggestions d'importation automatique.

Donc, nous allons cliquer dessus.

Et vous pouvez voir que header a été automatiquement importé ici.

Donc, nous allons faire une balise auto-fermante.

Et voyons si cela a été rendu ou non.

Le voici.

word count a été rendu.

Sandra style ce word 100.

Rapidement.

Je vais aller à header header dot CSS.

Mais tout d'abord, nous devons importer ce fichier CSS à l'intérieur de ce header.

Comment allons-nous faire cela ? Nous devons taper import dot slash dot signifie le répertoire courant slash header dot CSS.

Whoops.

Oui, cela a l'air bien.

Maintenant, nous allons devoir fournir à ce titre quelques styles, simplement fournir à ce titre un peu de style.

Disons simplement une taille de police de sept viewport width.

Viewport width est la largeur de l'écran sur lequel vous vous trouvez actuellement sur votre téléphone ou sur votre ordinateur.

C'est cette largeur particulière.

Je vais taper text trans form to uppercase.

Pour qu'il soit en majuscules, et je vais lui donner une famille de polices.

Tout d'abord, ne lui donnons pas de famille de polices.

Maintenant, vérifions simplement cela.

D'accord, cela a l'air bien, mais cela a l'air un peu moche.

Donc, nous voulons que cela soit un peu plus joli.

Donc, ce que je vais faire, c'est que je vais aller sur Google, Google.

Désolé, Google, je vais taper Monserrat font, si je ne me trompe pas avec l'orthographe, oui, Montserrat.

Donc, nous avons besoin de cette police Montserrat ici.

Je vais aller ici.

10 100.

Sélectionnez ce style, et allez à importer.

Et je vais prendre cette police ici.

Je vais copier cela.

Et je vais retourner à notre éditeur de texte et je vais aller à index dot CSS.

Ajoutez simplement en haut.

Je vais coller ce style de police.

Maintenant, voyons ce qui se passe.

Si nous tapons font family.

Nous allons devoir corriger l'orthographe m o n d, e s e r r a t.

Oui.

Correct.

Et sans serif ? Allons vérifier.

Regardez, cela ne fonctionne pas.

Pourquoi donc ? Espérons que je n'ai pas mis la mauvaise orthographe ici.

Peut-être que je l'ai fait ? Oui, je l'ai fait.

D'accord, maintenant voyons.

Oui, cela a l'air vraiment bien.

Donc, un conseil pour vous tous, si vous allez rendre le monde un peu plus grand, le titre un peu plus grand, réduisez simplement son poids de police.

Donc, cela va avoir l'air joli.

Ce sont quelques conseils de design, vous savez, pour un moment.

Donc, oui, cela a l'air bien.

Donc, qu'avons-nous besoin, autre que ce titre à l'intérieur de notre en-tête, nous allons avoir besoin du composant texte, comme vous le savez tous.

Donc, je vais créer un autre div ici.

D'accord, je vais donner le nom de classe de ce div comme inputs.

Oui.

Aussi, je pense que nous devons styliser notre en-tête également un peu.

Je vais apporter les styles pour notre en-tête.

Donc, ce que je vais faire ici, que fais-je ici, donc je fournis un affichage de flex align items au centre et justify content de space evenly.

Donc, ce que cela va faire, laissez-moi vous montrer tous les glissements ont créé ce Dev, laissez-moi simplement dire n'importe quoi Hello.

Si vous retournez ici, vous pouvez voir qu'il s'aligne de haut en bas.

Cela se produit à cause de cette direction de flex colonne, nous avons défini l'affichage sur flex flex direction colonne, et nous définissons l'affichage justify content space evenly.

Donc, cela va avoir un espace égal entre eux.

Et cela va avoir la hauteur de 35 viewport height.

Si j'augmente cela à, disons, 50 viewport height, voyez-vous, vous pouvez voir que la hauteur a été augmentée.

Donc, nous voulons une hauteur de 35 viewport height, vous pouvez voir qu'il y a un espace entre ces composants.

Donc, et cela va être 100%.

Donc, ce sont tous les styles.

Je ne vais pas entrer trop en profondeur dans le CSS car c'est un projet React, pas un projet CSS.

Donc, oui, supportons-moi.

D'accord, donc à l'intérieur des inputs, qu'avons-nous besoin maintenant ? Nous allons avoir besoin d'un champ de texte.

Donc, allons sur notre navigateur rapidement, trop.

Faites-vous vraiment pourquoi ? Allons au champ de texte, champ de texte.

Whoops, nous y voilà.

Nous allons avoir besoin de ce champ de texte standard.

Donc, je vais copier cela et copier cela ici et aller à notre éditeur de texte.

Je vais coller cela ici.

Et vous pouvez voir qu'il va nous donner une erreur car le champ de texte que nous avons un champ de texte important, donc nous allons, je vais aller ici, CTR l espace, il va me montrer une suggestion, je vais cliquer ici, et vous pouvez voir que le champ de texte a été importé.

Donc, oui, VS code aide beaucoup pendant le codage.

D'accord, il est sombre, maintenant vous pouvez voir parce que le fond est aussi sombre, et le composant est aussi sombre.

Donc, cela ne fonctionne pas.

Donc, que devons-nous faire ici ? Nous allons importer un thème sombre ici.

Où trouvons-nous ce thème sombre ? Et nous allons aller à Material UI, nous allons rechercher dark mode.

Nous y voilà.

Et je vais simplement copier cela.

Celui-ci ou un autre ? Laissez-moi vérifier.

Non, pas celui-ci.

Nous allons copier.

Oui, je pense que je vais copier celui-là.

Oui, nous allons faire quelques changements à celui-ci.

Donc, voici le thème sombre, il va se plaindre, parce que nous n'avons pas importé create em UI theme.

Cliquez sur importer celui-ci également.

Donc, le type est sombre.

Donc, je vais simplement faire ce que je vais faire, je vais copier le nom, et aller à l'intérieur de cela, et importer quelque chose appelé theme provider.

Donc, theme provider nous permet de, vous savez, appliquer des thèmes aux composants Material UI.

Nous allons aller ici, theme.

Donc, j'ai auto-importé cela en tapant CTL espace, vous pouvez voir qu'il a été auto-importé.

Je vais aller ici, taper theme equals dark theme.

Maintenant, vérifions notre composant rapidement.

Cela s'est amélioré ? Oui, c'est le cas.

Mais encore, vous pouvez voir lorsque je clique ici, cela devient un peu bleu foncé.

Donc, nous ne voulons pas cela.

Donc, que allons-nous faire ici ? À l'intérieur de la palette, nous allons lui fournir une couleur primaire.

Primary of main, cela va être comment hash, F F F.

Aussi, une virgule est nécessaire ici.

Je pense que cela devrait fonctionner.

Nous y voilà.

Lorsque nous cliquons dessus, cela va devenir actif avec une couleur blanche.

Donc, oui, nous avons importé notre thème sombre ici.

Que devons-nous faire d'autre que cela ? Nous allons avoir besoin d'un composant select.

Trouvons notre composant select.

Laissez-moi revenir au champ de texte.

Oui.

Laissez-moi faire défiler jusqu'ici.

C'est ce dont nous avons besoin.

D'accord.

Whoops.

Oui, je vais cliquer ici.

Vous pouvez voir qu'il nous a fourni une tonne de code ici.

Donc, que devons-nous ? Nous avons besoin du premier, n'est-ce pas ? Oui, nous avons besoin du premier.

Je vais aller et copier celui-ci, ce champ de texte ici, de ici à ici.

Copions-le.

Collons-le ici.

Cela va se plaindre car il manque beaucoup de choses.

Tout d'abord, ce champ de texte est tout oui, c'est important.

Nous n'avons pas besoin de cet élément de menu, je vais aller CTL espace et appuyer sur entrer.

Donc, mon nouvel élément est important.

Mais vous pouvez voir ces devises et gérer les changements.

Ce sont toutes leurs données, elles ne sont pas présentes dans le fichier, vous pouvez voir les devises gérer les changements des devises.

Donc, que allons-nous avoir besoin de ce select ? Tout d'abord, nous allons avoir besoin de ce select pour nos pays.

Laissez-moi simplement supprimer cela.

Supprimer cela.

Cette fonction map également.

Oui, nous allons utiliser desc plus tard.

Oui, à l'intérieur de l'élément de menu, je vais taper, disons Anglais.

Je vais supprimer ces clés et valeurs également.

Voyons si cela fonctionne ou non.

Cela fonctionne.

Oui, vous pouvez voir, mais il n'a qu'un seul composant.

Donc, que devons-nous faire, nous devons importer toutes ces langues.

Donc, ce que j'ai fait pour vous, j'ai déjà créé un fichier.

Ici, laissez-moi simplement aller à l'éditeur de texte et créer un autre dossier avec le nom de data.

Et je vais aller et créer un nouveau fichier appelé category.

Category dot j s.

Oui, category dot j s à l'intérieur de cette category.

Je vais aller et fournir ces données particulières.

Donc, si vous voulez ces données particulières, que devez-vous faire, je vais fournir un lien dans la description à mon dépôt GitHub, vous allez aller à mon dépôt GitHub, vous allez aller à ce dépôt GitHub particulier, vous allez aller à SRC, aux data à la category.js, vous allez copier ce fichier, je vais copier cela à l'intérieur de votre code, donc nous allons simplement faire, cela fournit la valeur, et le label est juste dans la documentation de cette API, vous pouvez le créer vous-même, ou vous pouvez le copier de mon GitHub.

Donc, nous avons créé ce category.js.

Enregistrons-le.

Et à l'intérieur de notre header.js, je vais importer cela.

Ici, importer category de, je vais remonter d'un cran.

Un autre cran en arrière, et à l'intérieur des data, vous allez avoir besoin de category, nous y voilà.

Donc, nous avons besoin de cette variable category ici.

Donc, nous allons, nous allons mapper cela, à l'intérieur de cet élément de menu.

Donc, ce que je vais faire maintenant, cela, et category roadmap, nous allons aller et parcourir cela, je vais fournir cet élément de menu à l'intérieur.

Et donnons-lui le nom de variable.

Donnons-lui le nom d'option.

Et à l'intérieur de cela, nous allons aller et taper option, dot value, car nous voulons que la valeur soit à l'intérieur de notre boîte de sélection.

Voyons si cela fonctionne ou non.

Oui, cela fonctionne.

Mais nous devons lui fournir une clé et une valeur également.

Donc, allons ici.

À l'intérieur de cette clé, je vais taper option dot value.

Désolé, option dot label.

Et la valeur sera option dot label.

Enregistrons cela rapidement.

Et vérifions cela.

Toujours la même chose ? Que devons-nous faire maintenant ? Nous devons fournir une valeur ici également.

Donc, nous avions créé un état pour cela, je pense que nous n'avons pas créé d'état.

Donc, créons simplement un état appelé category.

Donc, je suis désolé, whoops, que fais-je ? US state ? category ? Oui, cela a l'air bien.

Et je vais fournir une valeur par défaut d'Anglais.

Oui.

Nous devons amener ces deux choses à ce composant d'en-tête.

Comment allons-nous faire cela ? Nous allons aller ici au composant d'en-tête.

À cela, nous allons envoyer cela en tant que prop, la category et le set category également.

Oui.

Donc, nous allons aller à l'intérieur de notre en-tête, et nous allons recevoir ces deux variables ici.

En faisant de la déstructuration en tapant des accolades, entrer, et Diggory.

Oui, ces deux sont ici.

Laissez-moi simplement renommer cela en categories.

Get a go race.

Donc, nous ne sommes pas confus entre cela et cela.

Donc, categories, oui, c'est bien.

D'accord.

Donc, quelle sera la valeur ? La valeur sera category.

Et on change où cela va se faire, cela va définir cette category particulière sur cette chose.

Donc, on change, nous allons avoir un événement set category, e dot target, dot value.

Enregistrons cela et vérifions cela.

Espérons que cela devrait afficher la langue en premier.

Oui, cela affiche Anglais ici.

D'accord, faisons fonctionner cette chose.

Cela affiche actuellement standard, nous allons également devoir nommer celui-ci.

Donc, nous allons simplement ne pas avoir besoin de cet ID ici.

À la place du label, nous allons taper search word.

Et nous allons lui donner un nom de classe de search.

Oups, en train de faire cela au mauvais endroit.

Cela devrait être ici.

Ces deux choses devraient être ici.

C'était celui du select.

Donc, au lieu de celui du select, que allons-nous faire, nous allons le labelliser language.

Et nous n'avons pas besoin de ce texte d'aide ici.

Supprimons cela.

D'accord.

D'accord, donc à l'intérieur de celui-ci, nous devons amener notre état de mot que nous avons créé.

Laissez-moi vous montrer quoi.

Où est-il ? Oui, word et set word.

Je vais prendre ces deux et les envoyer à header.

Donc, word equals word.

Et set word equals set word.

Il n'y aura pas de virgules ici.

Donc, oui, nous avons envoyé cela, recevons-les simplement ici.

Word et set word.

Oui, je vais donner à cela une valeur de word.

Et on change, que va-t-il se passer ? Cela va changer ce set word.

Donc, il va changer ce set word, e dot target, dot value, voyons cette chose en action.

Ce que je vais faire ici, c'est que je vais vérifier si, y a-t-il quelque chose dans Word ? Je vais taper comme ceci dans des accolades ? Y a-t-il quelque chose dans Word point d'interrogation ? S'il y a quelque chose dans Word, nous allons rendre word.

Sinon, ce que nous allons faire, nous allons rendre, word hunt.

Cela va se mettre à jour en temps réel.

Là, vérifions.

Tapons ici.

Regardez, vous pouvez voir, cela fonctionne absolument bien.

Chaque fois que nous le changeons.

Cela appelle cette fonction on change, pour changer cet état, et fournir cette valeur particulière à cette boîte particulière.

Et changer cela, s'il n'y a rien à l'intérieur, cela ne va pas changer s'il y a quelque chose.

Oui, cela fonctionne bien.

D'accord, je vois un problème.

Quoi ici ? Pourquoi est-ce compressé ? Si peu, parce qu'il n'a pas de chemin ici.

Et ni cette chose ici a-t-elle un peu ?

Donc, voyons ce que je vais faire.

Je vais lui donner un nom de classe de search, je vais lui donner une classe.

Donnons-lui un nom de classe de select.

Oui, c'est bien.

Maintenant, je vais aller à header dot CSS, tout d'abord, je dois fournir à inputs un peu de style.

Aussi, nous devons nous assurer d'une chose ici, je vais rendre ces deux réactifs également.

Parce que lorsque vous allez ici, lorsque vous le rendez plus petit, vous pouvez voir que hunt devient un peu trop petit.

Donc, nous voulons que cela ait l'air un peu mieux que cela.

Donc, nous allons le rendre réactif.

Donc, nous allons le rendre réactif en utilisant des requêtes média.

Donc, ajoutons un média, whoops, média, nous allons taper max width.

Si la largeur maximale est inférieure à 900 pixels, que va-t-il se passer ? Cela va faire en sorte que le header justifie le contenu de l'espace de manière égale.

Et la hauteur va être de 25 ans, nous allons diminuer un peu la hauteur.

Deuxième chose, que allons-nous faire, dans le titre, nous allons augmenter la taille de la police de ce word hunt.

Donc, la taille de la police de, disons, 11, VH.

Whoops, que se passe-t-il ici ? Je pense que je dois lui fournir un peu plus de hauteur.

Laissez-moi vérifier.

Non, c'est bien.

Voyons.

Si je vais ici et que je fournis un style aux inputs, je vais d'abord styliser les inputs.

Je vais lui donner une largeur de 100%.

Et je vais fournir un affichage de flex et justifier le contenu.

Je vais lui fournir un espace entre ces espaces autour afin que vous puissiez voir qu'il a l'espace entre ceux-ci.

Vérifions cela, je pense que je dois le faire avec la largeur de 100%, si je ne me trompe pas, mais j'ai fourni le poids de 100%, alors qu'est-ce qui ne va pas ici ? C'est correct et bien.

Au centre, bonjour, désolé, espacé de manière égale.

Je ne pense pas avoir besoin de le fournir ici une fois de plus, donc je vais le supprimer.

Tout a l'air bien.

Découvrons cela plus tard.

Pour l'instant, ce que je vais faire, d'accord, c'était le problème, je lui ai donné v.

H, je dois lui donner v w.

Oui, c'était le problème, parce que c'était en respect de la hauteur de l'écran.

D'accord, c'était un problème.

Donc, oui, cela a l'air bien.

Maintenant.

Vous pouvez voir, cela ne se réduit pas trop.

Lorsque réactif.

Donc, oui, nous parlons de cela, donnons-lui un peu de poids ici.

Tout d'abord, je vais styliser cette boîte d'entrée ici.

Donc, search, search va avoir une largeur de 43%.

Et ce sera la même chose pour select également.

Donc, je vais faire une virgule, dot select.

Ces deux classes vont avoir 43%.

Oui, cela a l'air joli, vous pouvez voir que cela a l'air vraiment bien.

Si vous fournissez quelque chose, cela va changer l'état.

Donc, nous y voilà, nous avons terminé avec notre en-tête.

Allons à notre app JS à nouveau, voyons si nous avons quelque chose de laissé dans notre en-tête ici.

Je ne pense pas que nous ayons quelque chose de laissé dans l'en-tête.

D'accord, une autre chose que je pense que je vais faire, c'est que lorsque nous tapons, nous allons rechercher un texte, disons si je recherche plain, et si je change la category, donc ce qu'il devrait faire, c'est effacer cela, et la partie meanings également.

L'état de meaning également.

Donc, ce que je vais faire, c'est créer une autre fonction ici, const, handle change.

Donc, nous allons appeler cette fonction ici, ce champ de texte, je vais appeler cette fonction ici.

Et à l'intérieur de cela, puisque cela nous envoie cette e dot target dot value, nous allons la recevoir ici, ce que cette valeur a, la valeur a la langue.

Nous allons fournir cette langue à set category.

La langue devrait encore fonctionner, et le set world devrait être vide.

Maintenant.

Essayons cela.

Puis-je changer notre category ? Oui, c'est vide.

Si je tape quelque chose, changez-le.

Oui, c'est vide.

Cela fonctionne.

Super.

D'accord, une autre chose que nous devons faire, que nous avons omise, c'est comment changer notre API ? Lorsque nous changeons cette boîte, ou cette boîte de sélection particulière ? Donc, nous allons utiliser des backticks ici, supprimer ces balises de chaîne normales.

Et nous allons utiliser le backtick et aller à la partie langue.

Nous allons taper le signe dollar et ces accolades, je vais taper category.

Antara au lieu de ce mot.

Nous allons faire la même chose et taper word.

Super.

Vérifions si notre API répond à cela.

Whoops, qu'est-ce qui vient de se passer ? Oui.

Allons à notre console.

Oui, cela montre une erreur parce qu'il n'y a rien à l'intérieur.

Tapons simplement Hello.

Et encore, voyez ? Oui.

Qu'était-ce encore en train de montrer quoi d'accord, parce que je pense que je n'ai pas de mots.

Je n'ai pas de mots.

Bien, cela a l'air bien.

Rafraîchissons simplement cette page une fois de plus.

Et tapons Hello.

D'accord.

D'accord, React hooks a une dépendance manquante, bien sûr, parce que nous devons appeler cette API chaque fois que nous changeons notre monde ou notre category.

Donc, nous allons lui fournir word et category.

Donc, c'est ce qui va se passer.

C'est ce qui n'allait pas dans le précédent.

Chaque fois que nous changeons ce mot, disons hello.

Cela va appeler l'API à nouveau.

Vous pouvez voir qu'il appelle l'API.

Et vous pouvez voir qu'il nous fournit la signification et tout ce dont nous avons besoin pour travailler.

Oui, c'est super.

C'est ce dont nous avons besoin.

Donc, commençons à travailler sur cela.

Nous allons supprimer ce console, le laisser être ici.

Nous allons travailler sur ce pique.

Donc, ce que je vais faire, c'est créer un autre composant pour cela.

Je vais aller ici, au lieu de nos composants, nous allons créer un nouveau dossier appelé, disons definitions.

Je vais le mettre en majuscule.

C'est très important.

Pas le dossier, mais le fichier que vous créez.

Il doit être en majuscule, et un autre fichier pour CSS.

Je pense que je l'ai créé à l'intérieur de l'en-tête.

Donc, je vais le sortir de l'en-tête.

Oui, maintenant c'est bien.

Donc, notre definition.js, allons-y et tapons A f c et obtenons le code de base.

Tapons simplement Hello.

Et je vais l'importer.

Tout d'abord, laissez-moi simplement créer un fichier CSS pour cela également.

Definitions dot CSS et importer ce fichier CSS à l'intérieur.

Import dot slash definitions.

dot CSS ? Whoops.

Oui.

Importons simplement les definitions dans notre app j s.

En dessous de ce header.

Je vais taper definitions.

Oui.

Exhibits out auto importé.

Oui, c'est le cas.

Allons à notre app et vérifions.

Oui, hello, est imprimé ici avec succès.

Super.

Donc, que devons-nous créer à l'intérieur des definitions, nous devons créer une boîte comme je vous l'ai montré plus tôt, à l'intérieur de celle-ci, nous allons rendre toutes nos significations pour ce mot particulier, vous savez, Word, et la category.

Donc, voyons quelles sont toutes les choses que nous devons envoyer aux definitions ? Donc, je pense que nous allons devoir envoyer ce mot et la category et non, ha, oui, nous allons devoir envoyer ce mot et les significations car les categories ne sont pas nécessaires là-bas.

Parce que la category change l'API.

C'est tout ce qu'elle fait.

Donc, nous allons envoyer le mot, commençons par envoyer le mot.

Et nous allons envoyer l'état des significations.

D'accord.

Et nous allons définir la category également.

Voyons si nous en avons besoin ou non.

category.

Fermons simplement les dossiers inutiles.

Oui, revenons à la definition et recevons tout cela ici.

Word, category.

Et meanings.

D'accord, enregistrons cela.

Aussi, je vais rendre ces definitions uniquement lorsqu'il y a quelque chose à l'intérieur de ces meanings.

Vous savez, s'il n'y a rien à l'intérieur de l'état, alors nous n'avons pas besoin de voir quoi que ce soit ici.

Donc, ce que je vais faire, c'est lorsque j'ai fourni dans des accolades, lorsque je dis meanings, et cela, donc il y a quelque chose à l'intérieur des meanings seulement, alors les definitions seront rendues.

Allons à l'intérieur des definitions.

Et voyons.

Donc, tout d'abord, nous allons avoir besoin d'un composant audio également, mais je vais laisser ce composant audio pour plus tard.

Donc, commençons par taper.

S'il y a quelque chose à l'intérieur du mot, donc s'il n'y a rien à l'intérieur du mot, tout d'abord, ce qu'il va rendre, c'est qu'il va rendre une balise span.

Une balise span, le nom de classe de, disons, sub, title, whoops.

title.

Et cela va dire start by typing a word in search.

Oui.

Et s'il y a quelque chose à l'intérieur du mot, où cela va-t-il rendre ? Pour rendre cette autre chose ? Disons quelque chose.

Il y a quelque chose ici.

Oups.

Je vais simplement faire cela.

Oui.

Voyons.

Oui, start by typing a word in.

Donc, laissez-moi simplement le styliser un peu.

Je vais donner à ce div un nom de classe de, disons, meanings, ou meanings.

Nous avons importé at CSS également.

Il y a un style pour ces deux premiers, afin que nous en ayons terminé avec cela.

Je vais taper meanings.

Que devons-nous faire tout d'abord, nous avons besoin d'une bordure comme je l'ai affiché plus tôt, mais tout d'abord, nous allons faire, c'est que nous allons taper Display flex, brillant, nous allons devoir en faire un flex box.

Et nous avons besoin que tout soit aligné de haut en bas.

De haut en bas.

Nous allons faire flex direction a column.

Et oui, et nous allons faire, lorsqu'il y a beaucoup d'éléments affichés ici, nous allons devoir faire overflow.

Pourquoi comme un scroll ? Ou flow ? Pourquoi comme un scroll ? Vous savez ce que je pense, appliquons simplement ce style plus tard.

Donc, attendez, quelque chose ne va pas.

Non.

30, quelque chose à voir, tout d'abord, je vais importer quelque chose au lieu de, au lieu de ce quelque chose écrit ici.

Donc, oui, bien, tout d'abord, laissez-moi démontrer si cela fonctionne ou non.

Vous avez quelque chose, vous pouvez voir qu'il y a quelque chose d'imprimé, s'il n'y a rien, cela va dire start by having a word in search.

Stylisons ce subtitle.

Je vais aller et styliser ce subtitle seulement.

Pour l'instant.

Donc, title, je vais lui donner une taille de police similaire à celle que nous avons fournie plus tôt, cinq, viewport width, et la famille de polices va être la même.

Monserrat, laissez-moi simplement la copier pour ne pas faire de faute d'orthographe cette fois.

Oui.

Oui, cela a l'air bien.

Pour moi, taille de police cinq VH.

Et à quoi je pense ? Non, oui, c'est bien.

De toute façon, donc oui, bien, ce que nous allons faire, nous allons rendre ces meanings au lieu de cette chose.

Donc, allons ici.

Je vais taper meanings.

Je vais mapper cela.

Et map.

Je vais lui donner un mot mean.

Et faire cela.

Faisons simplement un log.

Voyons ce que nous obtenons à l'intérieur.

Je veux dire, il y a quelque chose de mal.

Oui, point-virgule.

Voyons, que recevons-nous ? Si je tape quelque chose plain ? Eh bien, vous pouvez voir que nous obtenons beaucoup de choses ici, nous obtenons un tableau de word et de phonetics et d'accord, ce n'est pas le dernier mot que c'est le mot final.

Nous obtenons des meanings et des phonetics, donc nous devons nous dépêcher à travers ces meanings.

Pour aller, je vais supprimer cela maintenant.

D'accord, donc ce que je vais faire, c'est sortir d'ici, votre mean, dot meanings.

dot map.

Je vais nommer cette variable item.

Voyons ce qu'il y a à l'intérieur.

Faisons un log.

Item.

Maintenant, faisons un log base rapidement.

Et tout d'abord, je dois supprimer ce log d'ici, pour qu'il ne crée pas de confusion.

Laissez-moi simplement fermer ce terminal.

Oui, faites de la place.

Voyons ce que nous obtenons.

Laissez-moi actualiser cela ici.

Je vais taper plane.

Nous y voilà, nous pouvons voir beaucoup de choses ici, nous pouvons voir nos définitions.

Donc, maintenant nous devons rendre, vous savez, mapper à travers ces définitions.

Donc, nous obtenons chacune des définitions et l'autre chose doit être des synonymes et des exemples.

D'accord, cela n'a pas ici.

Cela va être quelque part ici.

Cela va être quelque part à l'intérieur de cela.

parts of speech parts of speech definitions.

Vous pouvez voir l'exemple.

Et celui-ci a une chose supplémentaire, il va être synonyme.

Nous allons rendre cet exemple et synonyme optionnel, car vous pouvez voir quelque part il apparaît quelque part, il n'apparaît pas.

Donc, nous allons rendre cela optionnel.

Donc, retournons à notre code.

Laissez simplement supprimer cela à l'intérieur.

Je pense que j'ai supprimé autre chose.

Faire quelque chose de mal.

Non.

Je devrais supprimer cela.

Oui, donc à l'intérieur de cela.

Donc, nous avons notre item.

Donc, avec notre item, laissez-moi le déplacer en arrière ici.

Avec notre item, que allons-nous faire, nous avons besoin de definitions.

Nous allons mapper la définition.

Je sais que c'est beaucoup de mapping ici.

Ce n'est pas l'enfer du mapping.

Donc, je vais faire, définitivement item dot definitions dot map, et donnons-lui le nom de variable à D, F.

D'accord, maintenant nous devons créer un div.

Whoops, le IB.

Oui, voici notre div, je vais lui donner un nom de classe de single meaning, ou single mean, peu importe comment vous voulez l'appeler, je vais lui donner un style.

Un peu de style.

Je donne, je vais lui donner une couleur de fond.

Le composant single va avoir une couleur de fond blanche, disons.

Et quoi d'autre avons-nous besoin, je vais lui donner puisque c'est large, je vais rendre le contenu noir, couleur, noir.

Voyons si je tape quelque chose à l'intérieur de cela.

Imprimons notre définition en premier.

Donc, je vais imprimer la définition en gras.

Donc, def dot definition.

Vérifions.

D'accord, nous y voilà.

Ce sont les différentes définitions que nous obtenons de l'API pour le mot plane.

Si je tape ball, nous y voilà.

Nous obtenons différentes significations pour le ball.

Donc, nous n'avons pas seulement besoin des définitions, nous allons avoir besoin des exemples également.

Donc, je vais créer une ligne entre ces deux.

Je vais lui donner un style de couleur de fond.

Noir et la largeur, pas la largeur de 100%.

Disons.

J'espère que cela va créer une petite séparation.

Oui, cela le fait.

mean voir ce overflow est également ici.

Je vais le cacher dans un moment.

Donc, nous avons cet HR No.

D'accord.

Maintenant, ces parties optionnelles def dot example.

Si un exemple existe, alors où allons-nous imprimer cela, nous allons créer une balise span.

Au lieu de la balise span, tout d'abord, nous devons taper example.

Donc, nous allons rendre l'exemple en gras example.

D'accord, et nous allons imprimer d f dot example.

Vérifions cela.

D'accord, ce n'est pas approprié.

Cela avait des significations ombragées.

Oui.

Donc, oui, vous pouvez voir l'exemple de définition.

Définition exemple.

Oui.

Nous y voilà.

Donc, quoi d'autre avons-nous besoin ? Nous avons besoin des synonymes.

Juste en dessous de l'exemple.

Je vais taper def dot synonym.

Si le synonyme existe, synonyms, aussi sera là.

Donc, si seulement le synonyme existe, que allons-nous faire, nous allons faire la même chose que nous avons fait ici, nous allons copier cela.

Je vais le coller ici.

Je vais simplement changer synonyms.

Et d f, dot synonyms.

synonyms, puisque ce sont de nombreux synonymes, je vais faire un map à travers les synonyms.

s.

Et je vais faire avec le backtick.

Je vais faire cela.

Je vais imprimer s et virgule.

Voyons comment cela ressemble.

Vous pouvez voir les synonymes exemple, mais cela a l'air un peu moche, vous savez, c'est sur la même ligne.

Donc, nous devons faire, que devons-nous faire, c'est que nous allons avoir cela dans toutes ces lignes différentes.

Donc, tout d'abord, stylisons le conteneur extérieur d'abord.

Je vais styliser ce conteneur de meanings d'abord, n'est-ce pas ? Lorsque je vais à definitions dot CSS, et continuons à partir d'ici.

Je vais taper cette barre de défilement laide, je dois la rendre un peu plus petite.

Donc, je vais taper scroll avec, je pense, oui, scroll bar width, je vais lui donner 10.

Maintenant, vous pouvez voir que la barre de défilement a l'air beaucoup mieux.

Vous pouvez voir que la barre de défilement latérale est plus fine.

Je vais lui donner une hauteur de 55 viewport height et la bordure et obtenir une bordure de 10 pixels, 10 pixels de solide, j'ai une couleur ici, nous allons copier cela, vous pouvez simplement copier cette couleur où vous pouvez simplement expérimenter avec ces couleurs en cliquant ici et en sélectionnant simplement une couleur.

J'ai choisi cette couleur, elle avait l'air bien.

Et je vais lui donner un border radius de 10 pixels.

Voyons comment cela ressemble.

D'accord, ce n'est pas très bien, je pense que je dois lui donner un peu de padding.

Je vais lui donner un padding.

En haut et en bas, je vais lui donner 10 pixels et à gauche et à droite, je vais lui donner 20 pixels.

Et le overflow x sera caché, nous ne voulons pas la barre du bas, overflow x sera caché.

Oui, nous avons juste besoin de cette barre.

Aussi, nous devons créer quelques séparations entre ces deux.

Maintenant, je vais fournir ce style.

Mais laissez-moi simplement vérifier si c'est réactif pour l'instant.

Donc, si vous pouvez voir, nous le rendons plus petit.

Il y a un peu d'écart entre cela.

Je veux dire, en dessous de cela.

Nous allons le rendre un peu plus haut en hauteur lorsqu'il est plus petit.

Donc, je vais faire une requête média.

max width de 900 pixels.

Faisons his meanings.

Oui, meanings, et je vais lui donner une hauteur de 60, viewport height.

Oui, cela a l'air beaucoup mieux.

Et overflow.

Voyez-vous, pourquoi est-ce que je laisse un peu d'espace ici, parce que nous allons avoir un composant en haut, qui sera responsable de la commutation de nos thèmes.

Donc, je laisse simplement l'espace pour cela.

overflow, x va être caché et overflow va être scroll.

Mieux.

Donc, dans ce composant single meaning, laissez-moi simplement revenir à cela.

Dans ce composant single meaning, nous devons styliser ce div également, vous savez, chacun de ces devs doit styliser cela également.

Je vais aller ici.

Je vais taper display flex.

Le moment où je tape cela, vous pouvez voir qu'il est simplement en ligne horizontale.

Cela a l'air vraiment moche.

Donc, je vais taper flex direction as column.

Oui, c'est beaucoup mieux.

Je vais lui donner un border radius de, disons, 10 pixels.

Essayons, cela a l'air bien.

Oui, cela a l'air mieux.

Nous allons simplement créer un espacement entre eux par padding de 10 pixels en haut et en bas et à gauche et à droite, cela va être 20 pixels.

Oui.

D'accord, quatre espaces entre maintenant, j'ai besoin de la margin.

Pour, j'ai juste besoin de l'espacement en haut et en bas et à gauche et à droite va être zéro.

Oui, c'est beaucoup mieux.

Vous pouvez voir.

Donc, nous sommes à mi-chemin de l'application de dictionnaire.

Voyons si notre Hindi fonctionne ou non.

Je vais taper mon nom.

Oui.

Cela fonctionne.

Cela fonctionne, mec.

Super.

Tapez-vous dans le dos.

Vous avez fait du bon travail.

De toute façon, en mettant le cringe de côté.

Donc, que allons-nous faire ensuite ? Nous allons créer un composant de commutateur de thème ? Avons-nous besoin de cette category maintenant ? Je ne pense pas que nous en ayons besoin.

Laissez-moi simplement vérifier.

Je pense que nous allons en avoir besoin dans notre composant audio.

Oui, je vais faire, ce que je vais faire, c'est créer le composant audio rapidement.

Donc, meanings.

Il n'est disponible que dans le premier élément de ce tableau de meanings.

Donc, je vais taper si meanings, le premier élément est disponible.

Et s'il y a quelque chose à l'intérieur de Kanu, pas quelque chose à l'intérieur de, je veux dire, si c'est l'anglais, si la category est l'anglais, si ces trois conditions sont vraies, alors seulement cela va aller et rendre notre app.

Désolé, composant audio.

Je vais aller à l'intérieur de cela.

Et maintenant, je vais rendre le composant audio.

D'accord, si le composant audio n'est pas pris en charge, je vais taper votre navigateur ne prend pas en charge l'élément audio.

C'est mieux.

Je vais simplement donner un message ou quelque chose comme ça.

Désolé.

Oui.

Donc, à l'intérieur de cette tuile, nous allons nommer la couleur de fond.

Nous allons utiliser une couleur de fond de hash F F F, qui est blanc, et le border radius de 10.

Voyons si cela pleut ou non.

Bien sûr, cela ne pleut pas parce que nous n'avons rien tapé.

Cela ne rend toujours pas.

Évidemment, nous n'avons pas fourni le src.

Donc, SRC sera à l'intérieur de nos meanings.

Le premier élément de notre meaning.

C'est pourquoi j'ai inclus le premier élément à l'intérieur des phonétiques, comme je vous l'ai montré plus tôt, phonétiques, et désolé, phonétiques, au lieu du premier élément des phonétiques.

Donc, d'accord, parfois ce qui se passe, c'est que les phonétiques sont également manquantes.

Donc, je vais tester si les phonétiques sont présentes ou non.

Donc, les phonétiques sont là, elles sont présentes, alors nous allons taper la même chose à nouveau.

Et à l'intérieur de cela, il y a quelque chose appelé audio.

Et aussi, je vais lui fournir le contrôle.

Donc, nous avons les contrôles pour mettre en pause et jouer l'audio, etc.

Maintenant, voici le composant audio.

Donc, quelle est la dernière chose que nous devons faire, nous devons créer un composant de commutateur de thème, nous devons créer un composant de commutateur de thème ici.

D'accord, retournons à notre app j s.

Et ce que je vais faire, tout d'abord, je vais retourner à ce matériel, pourquoi je vais importer quelque chose appelé switch, nous en avons besoin parce que, évidemment, lorsque nous allons avoir besoin d'un switch pour changer le thème.

Donc, ce sont les switches normaux avec secondaire, primaire, non contrôlé, etc, nous allons avoir besoin d'un switch que nous allons changer de couleur.

Donc, voici le composant de couleur personnalisé, je vais copier cela, je vais aller ici et copier ce composant particulier, c'est le composant, vous pouvez parcourir notre documentation, vous comprendrez également ce qui se passe ici.

Donc, je vais copier cela.

Allons voir, drlc l'a copié.

Donc, à l'intérieur de notre app, j s, je vais le coller ici.

Et cela va se plaindre, parce que certaines choses ne sont pas importées, comme with styles.

Importons cela avec styles.

Il y a autre chose, oui, la couleur violette, mais nous n'avons pas besoin de la couleur violette.

Nous allons la remplacer par la couleur grise.

Donc, entrer, vous pouvez voir que la couleur grise a également été importante.

Switch n'est pas défini.

Oui, switch, nous devons également importer le switch, importer le switch, et espérons que cela va fonctionner, ou cela ne va pas s'afficher ici.

Jusqu'à ce que nous le rendions dans notre app.

Laissez-moi simplement créer un niveau d'espacement ici.

Facez là-bas, donc je vais simplement le rendre ici à l'intérieur de notre Comm.

container.

Oui, juste au-dessus de l'en-tête.

Ce que je vais faire, c'est lui donner un autre accord.

Parce que nous allons rendre ce div comme absolu.

Donc, la position de ce div est toujours le coin supérieur droit.

Rendez cela absolu et le style va être position comme absolu.

Et le haut sera zéro.

Laissez-moi simplement écrire quelque chose à l'intérieur de cela, disons theme.

Vous verrez que votre équipe apparaît ici.

Nous allons le rendre à droite.

Avec, disons, 15.

Oui, c'est un bon endroit.

Et nous allons fournir un peu de padding sur le haut de 10.

Super.

D'accord, maintenant nous devons utiliser ce switch violet, il a encore le nom de purple switch.

Laissez-moi simplement changer le nom, disons theme change.

J'espère que ce n'est pas un composant préconstruit, Material UI.

Je vais simplement l'appeler dark mode.

Oui, je vais l'appeler dark mode.

C'est mieux.

Pour insérer au lieu de ce thème, je vais rendre le dark mode ici.

Nous y voilà.

Espérons que cela va se rendre maintenant.

Oui, nous y voilà.

Oui ou donc avant ce dark mode, je dois fournir une balise span, qui va dire, un mode particulier, disons pour l'instant, disons qu'il dit light mode, pour basculer le light mode, vous pouvez simplement appuyer sur cela, et cela va basculer vers ce mode particulier.

Aussi, à l'intérieur de ce dark mode, lorsque nous devons fournir quelques composants, fournissons checked.

c, h, e, k, Ed, oui, checked, equals, nous allons fournir un état particulier à l'intérieur.

Donc, nous devons créer un état pour notre dark mode et light mode, je vais aller créer un US state, je vais l'appeler light mode, j'aurais dû appeler ce composant light mode également.

Mais de toute façon, donc light mode par défaut va être false.

D'accord, parce que vous pouvez voir, nous allons charger cette application en dark mode, parce que nos yeux sont utiles, nous ne voulons pas devenir aveugles par le light mode.

Donc, votre light mode ici et on change, il va simplement basculer le switch.

Donc, ce que je vais faire, c'est set light mode, et l'opposé de la valeur actuelle.

Donc, l'opposé de light mode.

Oui.

Nous y voilà.

Je pense que nous devons fournir le style à cette chose.

Le style flex à cette chose.

Donc, je vais aller à l'intérieur de notre à l'intérieur ici, je pense que je vais devoir fournir à cela un peu de style.

Ou peut-être notre container, flex direction, column height, 100, VH.

Oui, nous n'avons pas fourni le justify content evenly.

justify content, space evenly.

Space evenly.

Maintenant, vous verrez beaucoup plus joli.

Maintenant.

Si vous avez une confusion dans le code, vous pouvez simplement aller à mon dépôt GitHub, le lien est fourni dans la description pour voir tous les changements de code, si vous avez une confusion.

Je l'ai dit deux fois.

Oui.

Oui.

Donc, où en étais-je ?

Oui, dark mode.

Donc, ce que je vais faire, si la personne bascule en light mode, ce texte devrait également changer.

Tout d'abord, prenons soin de cela.

Je vais fournir une balise JavaScript ici.

Et disons light mode, si light mode est activé, alors il va rendre dark.

Sinon, il va rendre light.

Voyons si cela fonctionne ou non.

Par défaut, c'est dark mode.

Donc, je vais l'activer, regardez, il va montrer dark mode, si je l'éteins, light.

D'accord, donc finalement, voici le moment de vérité.

Comment implémentons-nous cette fonctionnalité ? Donc, ce que nous devons faire, c'est là où nous avons dit ces couleurs, nous devons simplement mettre une condition là-bas.

Donc, commençons par le meilleur endroit, notre composant d'application, je vais le mettre en plein écran.

Et je vais vérifier ensuite.

est-ce que le mode light est activé ? Si oui, alors je vais lui donner une couleur de blanc, triple F.

Sinon, cette couleur.

Et la couleur sera également affectée par cela, est-ce que le mode light est activé, nous allons poser cette question à nouveau.

Si cela sonne, alors je vais lui donner noir.

Whoops, je ne peux pas taper.

Nous y voilà.

Cela compile.

Testons cela.

Whoa, cela fonctionne comme par magie.

Mais nous avons encore quelques choses dont nous devons nous occuper.

Aussi, nous ne voulons pas que ce light mode nous frappe simplement en pleine figure, nous voulons simplement fournir un type de transition, c'est doux, cela a l'air bien.

Nous allons fournir toutes les point cinq secondes, vous pouvez simplement configurer cela selon votre propre.

Et lenio maintenant, cela va être un peu doux, nous y voilà.

Cela a l'air beaucoup mieux.

Donc, je vais styliser cela également.

Ou où est cette chose ? Tout d'abord, laissez-moi voir s'il y a quelque chose qui doit être changé ou quoi ici en ce qui concerne le dark mode ou le light mode ? Non, je pense que nous allons simplement envoyer le light mode ici dans notre header également.

Donc que nous puissions travailler avec cette chose, oui, et je vais le définir ici également, mec.

Whoops, pas le light theme.

Light mode.

Whoa.

Apparemment, je ne peux pas taper light mode equals light mode.

Je vais le fournir à ce theme.

Et juste aller, whoops.

Je vais à notre theme maintenant.

Je veux dire, head maintenant, je ne peux pas parler, je ne peux pas écrire ? Je suis si stupide.

Oui.

Venez ne pas utiliser snort un très gros tutoriel.

Light mode, voyez ? light allait le coller.

Light mode.

Donc, ici, je vais vérifier si le light mode est activé ? Point d'interrogation.

Si c'est activé, je vais lui donner une couleur noire.

Hash 000.

Sinon, blanc.

Je vais vérifier cela à nouveau, est-ce activé.

Si c'est le cas, je vais lui donner un light theme.

Sinon, whoops.

Sinon dark.

Yo, vérifions cela.

Encore.

Assez joli.

Mais tapons ici quelque chose.

Voyez-vous ? Eh bien, cela ne ressemble pas à bien.

Nous devons le créer un peu dans ce juste besoin de donner quelque chose de noir theme ou quelque chose.

Voyons s'il reste quelque chose ici ? Je ne pense pas.

Donc, nous allons fournir la même chose à notre composant definitions également.

D'accord.

Oui.

Comme mode.

Je vais aller à ce que j'ai déjà fait ici.

Donc, que vais-je faire ici, voyons.

Oui, ici, nous allons vérifier si le light mode est activé ou non.

Point d'interrogation, est-ce que le light mode est activé.

Donc, nous allons lui fournir une couleur de trois b 5360.

Sinon, blanc.

Nous allons tester cela à nouveau ici, est-ce qu'il y a un light mode, alors nous allons lui fournir une couleur blanche, sinon, une couleur noire ? Vérifions cela.

Nous y voilà.

Damn, cela a l'air vraiment joli.

Très bien.

D'accord.

Et je pense qu'avec cela, nous avons créé notre application avec succès.

D'accord, allons simplement rapidement sur netlify.

Et je vais héberger ce site web.

Donc, comment hébergons-nous ces sites web sur netlify.

Donc, j'ai déjà hébergé ce site web sur netlify.

Déjà, ce, ce word hunt, je vais cliquer sur nouveau site à partir de get et puis cliquer sur ce bouton GitHub ici, puis je vais me connecter.

Donc, vous pouvez voir que j'ai déjà autorisé GitHub, donc il va montrer mes dépôts, puis je vais sélectionner ce dépôt react dictionary où se trouve mon code.

Donc, après l'avoir poussé sur GitHub, vous devez simplement cliquer sur ce bouton deploy side, et le site sera déployé.

Et c'est tout ce que vous devez faire.

Et disons que si vous voulez changer le domaine de votre site web, où allez-vous faire, vous allez aller dans votre application web et cliquer sur domain settings.

Cliquez sur options added site name, et vous pouvez fournir un nom de site personnalisé ici.

Donc, ce que je vais faire dans la vidéo suivante, je vais faire de cette application une pw a progressive web app.

Donc, qu'est-ce qu'une pw a ou progressive web app ? Donc, pwd vous permet d'installer une application web particulière dans votre téléphone de manière native.

Ce que je veux dire par là, c'est que lorsque vous allez sur cette application web dans le navigateur de votre téléphone ou de votre bureau, elle va vous inviter avec une icône d'installation.

Donc, lorsque vous appuyez sur cette invite d'installation, elle va commencer à installer cette application de manière native dans votre téléphone.

Donc, vous pouvez utiliser cette application comme une application native dans votre téléphone ou votre bureau.

Donc, c'est une fonctionnalité incroyable d'une application web progressive.

Donc, commençons.

Donc, comme vous pouvez le voir, nous exécutons actuellement notre application de dictionnaire dans notre navigateur, et j'ai ouvert ce fichier de projet également.

Donc, que allons-nous faire maintenant ? Nous allons aller dans les outils de développement Chrome en cliquant sur inspecter et aller à lighthouse.

Donc, ce que lighthouse nous permet de faire, c'est qu'il va scanner notre application, et il va nous dire quelles sont les fonctionnalités manquantes pour en faire une application web progressive.

Donc, il va, dans votre cas, il va vous montrer toutes ces icônes comme cochées.

Donc, vous devez cocher toutes ces icônes sauf l'application web progressive et cliquer sur Générer un rapport.

Donc, il va scanner votre site web et vous dire quelles sont les choses manquantes pour créer une application web progressive.

Donc, vérifions.

D'accord, nous y voilà.

Donc, ce sont les choses, ces erreurs rouges sont les choses que nous devons compléter.

Donc, tout d'abord, commençons par le bas.

Donc, tout d'abord, il nous demande que le manifest n'a pas d'icône masquable.

Donc, nous devons créer une icône masquable.

Mais tout d'abord, ce que je vais faire, c'est que, tout d'abord, comme vous pouvez le voir, ces icônes ont ces icônes react.

Donc, nous ne voulons pas de ces icônes react, nous allons changer ces icônes par notre propre icône de l'application.

Donc, allons sur Google et recherchons dictionary, je peux PNG, le voici.

Allons aux images.

Et nous allons avoir cette icône avec dans laquelle nous avons tous les droits d'utilisation.

Allons cliquer ici.

Et choisissons cette icône.

Et je vais cliquer sur cette icône, cela va nous amener sur le site web, et à partir de là, nous pouvons télécharger gratuitement cette icône, oh, nous devons nous enregistrer.

Laissez-moi faire cela rapidement.

D'accord, donc nous avons téléchargé cette icône ici, cela va être gratuit, cela ne coûtera pas d'argent.

Donc, convertissons cette icône en favicon.

Donc, nous allons aller sur le navigateur, et taper PNG to favicon.

Allons sur ce site web.

Et nous devons glisser et déposer notre fichier ici.

Donc, prenons ce fichier, et déposez-le ici.

Et cliquons sur télécharger.

Donc, il nous a fourni ce fichier zip.

Gardons notre fichier zip ici et extrayons-le.

D'accord, nous y voilà.

Donc, quels sont les fichiers dont nous avons besoin ? Nous allons avoir besoin de celui-ci.

D'accord, nous allons avoir besoin de tous ceux-ci.

Et celui-ci.

Oui.

Découpons ces icônes ici.

Et nous allons aller ici dans le dossier public, et nous allons les coller ici et remplacer le fichier.

Et voici, nous avons ces fichiers favicon.

Donc, nous y voilà, nous allons supprimer ces deux fichiers.

Oui, nous n'en avons pas besoin, nous allons les supprimer.

D'accord, donc retournons à notre code.

Et dans notre dossier public dans index dot HTML, nous allons devoir ajouter quelques lignes.

Donc, ici, vous pouvez voir qu'il y a une icône tactile apple ici.

Donc, nous allons simplement changer le H ref en autre chose.

Voyons quel était le nom de notre fichier.

Voici le nom de notre fichier, Apple touch icon dot png.

Donc, Apple, touch icon dot png, nous y voilà.

Cela a auto-suggéré ce nom.

Et l'autre chose dont nous avons besoin, c'est de notre favicon.

icon.

Donc, link, short.

Vous l'avez ? D'accord, maintenant nous devons lui donner un href.

Donc, cela va être favicon dot Ico.

Oui, nous avons besoin de cela.

Nous y voilà.

Qu'est-ce qui ne va pas ? D'accord, nous n'avons pas fermé la balise.

Maintenant, nous avons terminé.

Allons sur notre site web et vérifions.

Nous y voilà.

Vous pouvez voir que l'icône a changé.

Laissez-moi simplement recharger cette page, et aller à inspecter et aller à application.

Maintenant, nous pouvons voir ici, vous pouvez voir que notre code favicon a changé avec succès.

Maintenant, que devons-nous faire pour cette étape deux, nous devons générer un fichier manifest.

Donc, qu'est-ce qu'un fichier manifest dot JSON, si vous allez dans votre application react, vous pouvez voir ce quelque chose sur manifest dot Jason.

Il a favicon dot Ico.

Il a les logos, différents logos ou fichiers de logo que nous avons supprimés.

Nous n'allons pas utiliser cela, nous ne l'avons pas supprimé ici.

Et je vais le supprimer également.

Nous n'en avons pas besoin.

Je vais supprimer ceux-ci également.

Fondamentalement, tout ce que nous allons supprimer.

Tout d'abord, laissez-moi générer les données de vos fichiers manifest.

Donc, ce que je vais faire, c'est que je vais aller sur ce site web Manny, fast generator.

Voyons.

Nous y voilà.

Hey, vous l'avez.

Donnons à notre application un nom.

Word hunt.

Je vais lui donner un nom court de word hunt.

Couleur de l'équipe.

Disons que je vais choisir le noir.

D'accord.

Le mode d'affichage va être autonome car nous voulons que cela agisse comme une application native.

Donc, nous allons faire en sorte que ce soit autonome.

Orientation.

Cela dépend de votre application.

Si votre application prend en charge le mode portrait ainsi que le mode paysage, vous pouvez sélectionner n'importe lequel.

Dans mon cas, je vais sélectionner n'importe quelle portée d'application, rien à changer ici.

Donc, nous y voilà.

Nous avons ces données de manifest générées.

Donc, je vais les copier.

Et je vais aller dans notre VS code et les coller ici.

Une virgule est nécessaire là.

Oui.

D'accord, maintenant nous devons générer nos icônes.

Donc, comment allons-nous faire cela ? Donc, plus tôt, nous avons téléchargé ce fichier.

Où est-il ? Oui, word hunt, nous allons utiliser cela pour générer nos différentes tailles.

Donc, il y a quatre tailles que vous devez générer.

La première est 190 2x 192, la deuxième est 256 3354, et la quatrième est 512.

Allons sur notre navigateur.

Et entrons image size.

Oui, allons sur Image resizer.com.

D'accord, nous y voilà, nous allons lui fournir notre image ici.

Donc, tout d'abord, qu'avons-nous besoin, nous allons avoir besoin de générer 192 x 192.

Nous y voilà.

Redimensionner l'image maintenant.

D'accord, nous y voilà, il y a télécharger cette image.

Nous y voilà.

Donc, nous allons aller dans notre dossier de projet.

Et nous allons le coller ici.

Donc, faisons simplement un glisser-déposer ici.

Donc, le voici.

Maintenant, le deuxième.

Aussi, je vais le nommer.

Nommons-le logo.

192.

Nous allons suivre cette convention.

D'accord, générons-en un autre.

Prenons cela.

Je vais simplement générer pour tout puis je vais tout coller ensemble là.

Le deuxième est 256 dans 256.

Il y a télécharger cela.

Le troisième.

Oui, le troisième était 384 dans 384.

Nous y voilà.

Le fichier final sera 512 et 251251 2x.

Cinq un à redimensionner cette image.

D'accord, nous y voilà.

Voyez-vous, j'ai téléchargé cela deux fois par erreur ? Allez-vous le supprimer ? Oh, non, peu importe.

D'accord, donc nous allons copier tous ces fichiers dans ce dossier, le dossier public.

Puis je vais les nommer de la même manière que j'ai nommé ce logo un et deux.

Donc, celui-ci est logo 256.

Celui-ci est logo.

384.

Et celui-ci était logo.

512.

Nous y voilà.

D'accord, donc nous avons généré toutes les icônes avec succès.

D'accord, donc nous avons tous les icônes générées avec succès.

D'accord, allons dans notre VS code.

Et créons nos icônes.

Donc, ce que nous devons faire maintenant, c'est cela.

Nous allons entrer cela.

Donc, qu'ai-je fait ici ? Voyons.

Oui, donc nous allons fournir le SRC de l'endroit où se trouve l'icône.

Je vais supprimer cela.

Et taper logo 192.

Même chose pour celui-ci également.

Logo 256.

Logo 384.

Enfin, logo 512.

Voyons application.

Enregistrons cela.

Oui, et allons dans Chrome.

Actualisons cette page.

Compilé avec succès.

Allons à inspecter et application.

Nous y voilà.

Nous avons toutes les icônes ici.

Super.

Et nous devons également ajouter un ServiceWorker.

Je vais expliquer ce qu'est un ServiceWorker plus tard.

Allons à notre lighthouse ici.

Générons le rapport.

Et maintenant, commençons à travailler sur cela.

D'accord, le premier est que le manifest n'a pas d'icône masquable.

Donc, qu'est-ce que l'icône masquable.

Donc, l'icône masquable est quelque chose qui, lorsque vous installez l'application dans votre téléphone, l'icône et celle qui est affichée là dans votre menu.

C'est ce que l'icône masquable est.

Donc, comment générons-nous une icône masquable.

Donc, il y a un site web appelé mass cable dot app.

Je vais fermer ces deux, je vais aller à Mass cable, dot app slash editor.

Nous y voilà.

Donc, nous devons lui fournir.

Tout d'abord, nous devons lui fournir notre icône ou l'image que nous devons utiliser.

Donc, celle-ci, je vais la glisser et la déposer ici.

Donc, nous y voilà.

Maintenant, nous devons la faire selon nos, vous savez, selon nos goûts, donc je vais faire, disons, rectangle arrondi.

Oui, cela a l'air bien.

Je vais lui donner un peu de padding.

Je vais la déplacer un peu ici.

Cela a l'air bien.

Je pense que c'est bien.

Je pense que cela a l'air bien.

Oui, donc je vais simplement l'exporter.

Cela l'a téléchargé.

Allons dans notre dossier public.

Et je vais glisser et déposer cela ici.

Faisons glisser et déposer ici.

Je vais lui donner le nom de maskable.

maskable.

Oui, super.

Donc, maintenant dans notre fichier manifest, nous devons fournir l'emplacement de ce maskable.

Allons dans le manifest ou JSON.

Et en haut ici, je vais ouvrir une autre accolade.

Tout comme les autres, nous devons lui fournir en tant que SRC tout d'abord, whoops, en tant que C.

Donc, ce que va être le SRC maskable.

Le nom que nous avons donné, ne doit pas être en.

jpg.

Donc, quelle est la taille, la taille va être 1-967-219-6196.

Dans 2196.

C'est nous devons ajouter le type type va être image slash PNG.

Et le but but va être any maskable.

Le voici.

Enregistrons cela.

Et vérifions notre site web.

Allons ici, ici et actualisons-le.

Je vais le fermer et l'ouvrir dans un nouvel onglet.

Allons à inspecter au Lighthouse et Générer un Rapport.

Une fois de plus.

D'accord, nous y voilà.

Le manifest a une icône masquable.

Voyons ce qu'il reste.

Mieux.

D'accord, la chose suivante, que devons-nous faire, c'est qu'il ne redirige pas le trafic HTTP vers HTTPS.

Donc, cela va être corrigé lorsque nous le déployons sur netlify.

Puisque netlify, dirige tout le trafic vers HTTPS, donc cela ne va pas être le problème.

Donc, laissons cela pour l'instant.

Et le troisième, c'est qu'il ne registre pas un ServiceWorker, qui contrôle la page et l'URL de départ.

Donc, ces trois sont liés ensemble.

Donc, nous devons fournir cela, allons ici.

Où est-ce ? Donc, comme vous pouvez le voir, nous n'avons actuellement aucun fichier ServiceWorker.

Donc, comment devons-nous générer le fichier ServiceWorker ? Donc, allons à une nouvelle fenêtre.

Ce que je vais faire, c'est que je vais ouvrir un dossier.

Ouvrons un dossier ici.

Je vais nommer ce dossier, service.

work ou quelque chose, n'importe quoi, cela n'a pas vraiment d'importance.

Donc, ce que je vais faire, c'est que je vais initialiser une nouvelle application react.

Mais ce ne sera pas de la manière conventionnelle.

Ce que je vais faire, c'est que je vais entrer NP x create react app.

Et que devons-nous faire ? Oui, nous devons écrire n'importe quel nom, disons my app.

Et je vais écrire un modèle pour CR a dash template, dash pw A.

Donc, lorsque vous tapez cela, cela va générer une application react, spécialement configurée pour une application pw a.

Donc, entrons cela.

Et voyons ce qui se passe.

D'accord, nous y voilà.

Cela a initialisé avec succès une nouvelle application react.

Donc, qu'avons-nous besoin de cette application react ? Nous avons besoin de ces deux fichiers serviceworker.js et service worker registration dot j s nous allons donc sélectionner ceux-ci et les copier et les copier dans notre Projet ici dans le dossier src, je vais aller et les coller.

Donc, nous avons ces deux fichiers ServiceWorker.

Allons dans ce projet.

Et allons à l'intérieur de index dot j s, voyons comment ces fichiers sont utilisés.

Donc, il est utilisé ici.

Et nous devons ajouter cette ligne également.

Donc, je vais ajouter cette ligne d'abord, importons cela, copions et collons dans notre fichier index.js.

Nous y voilà.

Retournons.

Et copions cette partie également.

Copions et collons ici.

Et enregistrons cela.

Et voyons l'application a compilé avec succès.

Retournons à notre localhost.

Et je vais l'ouvrir dans un nouvel onglet à nouveau.

Allons à inspecter et vérifions lighthouse.

Lisons le rapport.

D'accord, voyons ce qui s'est passé.

D'accord, cela donne toujours la même erreur.

Pourquoi ? Parce que, parce que, à l'intérieur de register, vous pouvez voir qu'il ne fonctionne que sur une application de production.

Donc, notre application est actuellement en développement.

Donc, construisons cette application.

Et voyons si cela fonctionne ou non.

Donc, ce que je vais faire, c'est que je vais taper NPM, run, build.

Donc, cela va construire notre application, une application prête pour la production.

D'accord, tout d'abord, whoa, whoa, whoa, nous avons oublié de faire cela.

Au lieu de unregister.

Nous devons le changer en register.

Oui, afin qu'il puisse enregistrer notre ServiceWorker.

Donc, maintenant, exécutons la construction.

D'accord, l'application a été construite avec succès.

Donc, que dit-il ? Il dit que vous pouvez exécuter cette commande pour exécuter la construction de production.

Mais tout d'abord, si vous n'avez pas ce sir, que devez-vous faire ? Vous pouvez exécuter NPM I sir, dash g lorsque vous exécutez cette commande, désolé, ce n'est pas un om, c'est NPM.

Donc, lorsque vous exécutez cette commande, ce qu'elle va faire, c'est qu'elle va installer cette commande serveur sur votre machine.

Donc, exécutons simplement cette commande maintenant.

Sir, dash s build.

Je vais la copier et l'exécuter ici.

Donc, il dit qu'il sert sur notre localhost dans notre localhost 5000.

Donc, allons sur localhost 5000.

Maintenant.

localhost, je vais changer cela en 5000.

Et notre application s'exécute, allons à inspecter et à lighthouse.

Et générons le rapport à nouveau.

D'accord, nous y voilà.

Ces vérifications ont terminé l'experto.

Maintenant, vous pouvez voir qu'il a éclairci cette icône d'application web progressive.

Donc, tout ce que nous devons faire maintenant, c'est qu'il ne redirige pas le trafic HTTP vers HTTPS.

Donc, lorsque vous déployez cette application sur netlify, ce qu'elle va faire, c'est qu'elle va rediriger avec succès tout le trafic de HTTP vers HTTPS, puis elle sera créée en tant qu'application web progressive.

Donc, si vous ne savez pas comment déployer cette application sur netlify, vous pouvez vérifier notre vidéo précédente où j'ai où nous avons créé cette application de dictionnaire.

Donc, vérifions notre site web déployé.

Maintenant.

Allons sur word hunt dot netlify dot app.

C'est notre site web déployé.

Maintenant, vérification finale, tout d'abord, vous pouvez voir qu'il y a un bouton Installer ici.

Si je clique sur ce bouton Installer, il va me demander d'installer cette application, comme je vous l'ai montré plus tôt sur le téléphone.

C'est ainsi que vous pouvez l'installer sur votre bureau.

Cliquons sur Installer.

Et nous y voilà, cette application a été installée avec succès.

Nous y voilà.

Notre application est ici, word hunt lorsque nous cliquons dessus, elle a été installée en tant qu'application native dans notre PC.

Et vérifions une dernière fois, il y a un nouveau rapport et il va nous montrer que notre application est maintenant avec succès une pw a.

Hey, vous y voilà.

Nous y voilà.

Notre application progressive fonctionne bien, l'application web progressive fonctionne bien.