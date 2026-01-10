---
title: Comment j'ai construit une application complexe d'analyse de texte en un mois
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-03T19:19:14.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-complex-text-analysis-app-in-a-month-61917877cd72
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aIewSM1E9TbQvqxIvLy9jQ.png
tags:
- name: JavaScript
  slug: javascript
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: text analysis
  slug: text-analysis
seo_title: Comment j'ai construit une application complexe d'analyse de texte en un
  mois
seo_desc: 'By Jeffrey Flynt

  How it started

  I was in a week-long humanities intensive learning workshop at the University of
  Texas at Austin, in a Text Analysis session. One of the participants asked:


  “Why doesn’t a software developer make this easier instead o...'
---

Par Jeffrey Flynt

### **Comment tout a commencé**

Je participais à un atelier intensif d'une semaine en sciences humaines à l'Université du Texas à Austin, dans une session d'analyse de texte. L'un des participants a demandé :

> « Pourquoi un développeur de logiciels ne rend pas cela plus facile au lieu de nous obliger à connaître R ou Python ? »

Je me sentais à l'aise dans la session, car j'avais déjà de l'expérience avec les deux. Mais je pouvais définitivement comprendre le sentiment des utilisateurs qui ne sont pas à l'aise avec l'écriture de commandes pour voir des résultats rapides.

Je suis associé de recherche au Quantitative Criticism Lab (QCL) de l'UT Austin. Les investigateurs principaux m'ont suggéré de suivre ce cours. Ce cours m'a définitivement aidé à affiner et à découvrir de nouvelles compétences en traitement du langage naturel (NLP).

Sans le vouloir, j'ai mis ce problème de côté pendant que je me concentrais sur d'autres boîtes à outils et projets. En participant à un atelier d'études classiques à Boston, j'ai remarqué que beaucoup montraient de la frustration face au manque d'outils plus simples pour l'analyse et la visualisation de texte.

L'équipe à laquelle je participe à l'UT Austin développait une boîte à outils [stylométrique](https://en.wikipedia.org/wiki/Stylometry) basée sur le web pour plusieurs langues, mais il n'y avait actuellement pas d'option complète pour la langue anglaise.

Il est vrai qu'il existe des options comme [Voyant](https://en.wikipedia.org/wiki/Voyant_Tools). Mais il n'existe pas de solutions prêtes à l'emploi qui offrent des fonctionnalités telles que l'extraction d'entités nommées, l'étiquetage des parties du discours (POS), la segmentation des mots à partir de texte bruyant et l'analyse des sentiments aux personnes sans connaissances préalables en programmation. Couplé à cela et à ce qui précède, cela a renforcé l'idée de lancer une application plus simple pour le NLP.

### Par où commencer ?

En attendant de monter dans l'avion, mon esprit a commencé à tourner autour de la question de savoir par où commencer. J'ai fini par me décider à créer l'interface utilisateur. Ma raison était que cela rendrait plus facile la création des fonctions une fois que j'aurais compris le flux de travail pour l'utilisateur.

Une fois que le capitaine a dit que c'était bon pour les appareils électroniques portables, j'ai sorti mon ordinateur portable et je me suis mis au travail. Je suis sûr que le gars assis à côté de moi pensait probablement que je piratais quelque chose avec tout mon temps passé dans la console.

Au moment où j'ai atterri après le vol de cinq heures, j'avais terminé les écrans de connexion, d'inscription, de mot de passe oublié et de construction de corpus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Iy5L74n4CgKbBY2acEMLrA.png)

Vous pourriez demander comment il est possible de terminer tout cela avec les fonctions JavaScript correspondantes et les tests. Une bonne pratique que j'ai apprise tôt pour réduire le temps de développement est de garder le code boiler plate juste pour ces situations.

Mon code prêt à l'emploi consiste généralement en :

* Inscription / Connexion
* Notifications
* Visualisation (Chart.js, Bootstrap Tables, Handsontable.js)
* Routage

Une autre approche pour réduire le temps de développement, surtout lorsque vous travaillez sur un projet seul, est d'utiliser des templates d'administration pré-faits pour l'UI. La section [Themeforest Admin Website Templates](https://themeforest.net/category/site-templates/admin-templates) a quelques bons éléments d'UI que j'utilise dans mes projets. J'ai réduit de plus de 50 % le temps de développement habituel en utilisant des actifs pré-construits.

Bien sûr, je devais connaître mon chemin autour de HTML, CSS et jQuery. Mais ayant ces actifs déjà conçus, je n'avais qu'à m'inquiéter du placement et de l'intégration des données.

Mon framework de choix est [Meteor.js](https://www.meteor.com/). Meteor est un framework JavaScript qui repose sur Node.js. J'utilise MongoDB comme base de données et Python pour les tâches NLP lourdes.

Pour ceux d'entre vous qui sont familiers avec Meteor, j'ai opté pour ne pas inclure les publications et abonnements, seulement les méthodes et appels, et j'ai plutôt utilisé des imports dynamiques pour toutes les bibliothèques tierces fonctionnant sur le client. Cela a aidé à améliorer les performances. J'ai également utilisé des workers pour tout code client qui doit manipuler des chaînes de caractères. Cela m'a permis de réduire la taille du bundle à environ 500 ko.

J'ai choisi Textalytic pour le nom et j'ai sécurisé le [site web](https://www.textalytic.com/).

### Oh, vous pensiez que ce serait simple ?

J'ai supposé que tout cela serait assez simple avec mon expérience précédente de travail sur des boîtes à outils liées au NLP avec le QCL Lab. Mais il y a toujours ces moments de "gotcha".

Je voulais que les utilisateurs puissent voir les entités nommées mises en évidence dans leur corpus. J'ai d'abord dû obtenir une bibliothèque compatible JavaScript rapide pour extraire les entités nommées.

Au début, j'ai utilisé [compromise.js](https://github.com/spencermountain/compromise). Cela fonctionnait assez bien dans une certaine mesure, mais la vitesse sur des textes relativement longs laissait à désirer.

J'ai ensuite opté pour [SpaCy](https://spacy.io/), mais cela était en Python. Je n'avais jamais eu à intégrer deux langues différentes auparavant, alors je suis allé sur Stack Overflow pour apprendre.

Après avoir fait fonctionner SpaCy avec JavaScript, j'ai rencontré deux problèmes avec SpaCy. Le premier était que SpaCy ne retournait pas des comptes précis.

Les utilisateurs pouvaient voir la fréquence des noms, adjectifs, verbes, etc. SpaCy retournait 31 instances de "voiture" mais lorsque je faisais un compte manuel, j'en obtenais 44.

Au début, j'avais fait gérer par Python le retour de la fréquence des noms :

J'ai fini par opter pour simplement retourner le tableau brut des noms et faire retourner par JavaScript les 10 noms les plus fréquents.

Cela a conduit à des comptes précis pour les noms :

Le deuxième problème concernait les entités nommées. La plupart des modèles d'analyse de texte, sinon tous, n'obtiendront pas une précision de 100 % sur les entités nommées. Pour compléter SpaCy, j'ai importé une grande liste d'entités nommées prise de [WikiData](https://www.wikidata.org/wiki/Wikidata:Main_Page) dans MongoDB.

Le texte est passé à travers SpaCy qui retourne un tableau d'entités trouvées. MongoDB produit ensuite un grand tableau d'environ 150k entités, qui est envoyé avec le texte à une fonction qui effectue une correspondance contre les limites de mots. Les expressions régulières tenant compte de la ponctuation et des limites causeront beaucoup de maux de tête.

Ces deux tableaux sont filtrés et les entrées en double sont supprimées pour produire un tableau final d'entités. Cette méthode semblait être la plus rapide, retournant des résultats en ~5 secondes.

Cette méthode a fourni une meilleure couverture en obtenant une plus grande précision que les 85,85 % de SpaCy.

### Peut-on simplifier, s'il vous plaît ?

De nombreux tutoriels pour les tâches NLP demandent aux utilisateurs de pré-traiter le texte avant l'analyse. Je voulais que les utilisateurs aient une approche plus simple.

Avec le Corpus Builder, les utilisateurs peuvent taper ou copier et coller du texte ou sélectionner un fichier depuis leur ordinateur ou Dropbox.

#### Pré-traitement

Je devais maintenant tenir compte de l'analyse de différents types de fichiers, de la désinfection des entrées utilisateur et de l'offre d'options de point et clic pour le pré-traitement.

Pour le pré-traitement, les utilisateurs peuvent supprimer les lignes vides, les mots vides, les lignes en double, la ponctuation, les espaces supplémentaires, les sauts de ligne et les lignes contenant un mot sélectionné par l'utilisateur.

Pour rester dans l'esprit de faciliter l'analyse de texte, l'utilisateur n'a pas à faire tout cela. Selon la fonctionnalité sélectionnée au moment de l'exécution, le back-end décide de la meilleure façon de gérer le texte.

#### Transformation de texte

Lorsque je suivais le cours d'analyse de texte, il semblait que nous faisions beaucoup de transformations de texte avant de commencer à tester divers modèles.

J'ai d'abord essayé d'intégrer l'API Dropbox dans l'application. J'avais supposé que c'était la seule façon d'obtenir cette fonctionnalité. J'avais tort, car Dropbox a un composant appelé Chooser qui permet à l'utilisateur d'importer ses documents dans l'application sans que je doive passer plus de temps à ajouter des appels d'API.

Pendant le cours d'analyse de texte, les utilisateurs devaient télécharger des fichiers texte depuis le Google Drive de quelqu'un ou télécharger des corpus prêts à l'emploi depuis NLTK. Cela prenait beaucoup de temps en attendant que tout le monde ait les fichiers téléchargés et importés.

Pour les utilisateurs qui veulent simplement tester des fonctionnalités ou comprendre comment fonctionne l'analyse de texte, j'ai opté pour inclure une bibliothèque d'œuvres littéraires du domaine public qu'ils pourraient ajouter à leur [corpus](https://en.wikipedia.org/wiki/Text_corpus) pour choisir. J'espère que cela fournira une barrière d'entrée plus relaxée pour les utilisateurs débutants.

Pour les utilisateurs avancés, je voulais qu'ils aient des options et ne soient pas liés à une configuration par défaut. J'ai implémenté des mots vides personnalisés, des listes de mots les plus fréquents personnalisées, et plus encore. Certains utilisateurs peuvent vouloir rechercher la fréquence des mots qui se terminent par "-ing", alors j'ai ajouté cela aussi.

En ajoutant ces options, j'ai dû tenir compte de ces espaces supplémentaires, transformer leur entrée en un tableau utilisable, fixer des limites à la taille de leur liste personnalisée, etc.

### Ne bloquez pas la boucle !

Je ne voulais pas que les utilisateurs puissent seulement voir la fréquence normalisée des noms et des verbes. J'ai donc fini par ajouter des clauses relatives et subordonnées.

Je teste actuellement des cas plus complexes tels que les modificateurs pendants, les objets directs et les structures parallèles.

#### Performance

J'étais excité d'avoir cela en place et que les résultats revenaient assez rapidement. Ensuite, j'ai commencé à penser à la performance. J'ai ouvert le site sur mon ordinateur portable et mon bureau, puis j'ai procédé à une analyse sur certains corpus très grands. Comme vous pouvez vous y attendre, mes résultats ne revenaient pas aussi vite lorsque je faisais des recherches avec seulement moi.

Le problème était que mes fonctions de longue durée bloquaient la boucle d'événements principale. Je devais déporter ces tâches vers un processus séparé pour garder Node réactif. J'ai essayé pendant des heures de faire fonctionner les fonctions sur un autre processus.

Enfin, j'ai trouvé [Napa.js](https://github.com/Microsoft/napajs) de Microsoft. C'était vraiment simple à intégrer et je n'ai pas eu à changer aucune de mes fonctions.

L'application fonctionnait maintenant sans problème avec de grands corpus analysés par plusieurs utilisateurs. Cependant, il y a toujours un "mais" !

Lorsque j'effectuais des recherches avec des corpus composés d'un très grand corps d'environ 500k mots, Python lançait une `ValueError`. SpaCy a une limite fixée à 1 000 000 de caractères dans une seule chaîne, ce qui est modifiable. Naturellement, j'ai divisé le corpus en morceaux.

Puisque cette application est gratuite et soutenue par moi-même — et que les ressources du serveur pourraient devenir coûteuses — j'ai opté pour fixer des limites strictes pour les comptes de 1 000 000 de mots de corpus par compte et de 50 000 mots par corpus. Un utilisateur peut exécuter une analyse sur un groupe de corpus, mais chaque corpus est analysé individuellement. Cela devrait aider à prévenir la surcharge du serveur sur les fonctions intensives en calcul.

#### Étiquetage POS

L'étiquetage des parties du discours visualisé de manière significative était quelque chose que je savais devoir avoir dans l'application. SpaCy retournait les étiquettes POS pour chaque mot dans un grand tableau d'objets sans problème, mais cela n'était pas utile pour l'utilisateur. J'ai dû réussir à transformer ce tableau en un format visuellement agréable pour l'utilisateur.

Compromise.js a un joli format pour faire cela, ce qui m'a inspiré.

J'ai placé ce tableau dans une boucle qui ajoutait des balises de couleur en fonction du POS et transformé le nouveau tableau en une chaîne de caractères et mis à jour la page avec ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*guZQY6nRijbY2OROxI2RPQ.png)

### Conclusion

En l'espace d'un mois, l'application était en bon état pour être publiée. J'ai depuis apporté diverses modifications pour l'optimisation et d'autres ajustements. J'essaie d'éviter d'ajouter des modules npm sauf si je dois le faire. Tout a été écrit en JavaScript vanilla à l'exception des bibliothèques de visualisation et des notifications [toastr](https://github.com/CodeSeven/toastr). En faisant cela, la base de code est plus légère et je n'ai pas à m'inquiéter de savoir quand le mainteneur dudit projet va faire `x`.

Vers la fin de ce projet, j'ai commencé à penser :

« Qui utiliserait cela ? »

« Cette application est-elle vraiment assez bonne ? »

« Ai-je fait une erreur quelque part et elle sera à jamais ternie ? »

J'ai supprimé ces pensées et je me suis dit que si cela échoue, j'aurai appris beaucoup, ce que je n'aurais probablement pas appris en faisant autre chose.

Vous pouvez perdre beaucoup de temps à essayer d'optimiser chaque fonction. J'ai rapidement appris à abandonner l'idée d'essayer d'écrire des fonctions dans la dernière syntaxe ES. J'ai cependant mis l'accent sur la performance de diverses fonctions, surtout pour l'expérience utilisateur.

L'une des meilleures stratégies pour gagner du temps a été d'utiliser le pipeline CI/CD de Gitlab — et c'est gratuit !

Au lieu de construire manuellement le bundle, d'arrêter le service, de télécharger, etc., je n'ai fait qu'un seul commit dans [GitKraken](https://www.gitkraken.com/). [GitLab](https://about.gitlab.com/) gère tout le reste sur le serveur.

Il y avait une courbe d'apprentissage pour configurer [NGINX](https://www.nginx.com/) avec plusieurs instances, l'équilibrage de charge et les sessions persistantes. Mais il y a tellement de ressources pour vous aider en cours de route, comme [freeCodeCamp](https://www.freecodecamp.org/), [Stack Overflow](https://stackoverflow.com/), et la section [blog](https://blog.digitalocean.com/) de Digital Ocean.

Je pense constamment à de nouvelles fonctionnalités à ajouter qui pourraient être utiles aux utilisateurs. La synthèse de documents, les modèles personnalisés de machine learning et la détection d'arguments/postures sont quelques fonctionnalités que je prévois d'ajouter cet été. Si vous êtes intéressé par une fonctionnalité NLP qui pourrait être utile, faites-le moi savoir dans la section des commentaires. Merci d'avoir lu !