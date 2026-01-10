---
title: Apprendre Vue 3, un Framework JavaScript Front-End
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-09-07T15:37:36.000Z'
originalURL: https://freecodecamp.org/news/vue-3-full-course
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/vue.png
tags:
- name: vue
  slug: vue
- name: youtube
  slug: youtube
seo_title: Apprendre Vue 3, un Framework JavaScript Front-End
seo_desc: 'Vue is one of the more popular front-end JavaScript frameworks. It makes
  it simpler to create powerful websites.

  We just released a Vue course on the freeCodeCamp.org YouTube channel that will
  teach you the latest version of this progressive JavaScri...'
---

Vue est l'un des frameworks JavaScript front-end les plus populaires. Il simplifie la création de sites web puissants.

Nous venons de publier un cours Vue sur la chaîne YouTube freeCodeCamp.org qui vous enseignera la dernière version de ce framework JavaScript progressif.

Gwendolyn Faraday a développé ce cours. Elle a précédemment créé l'un des cours Vue les plus populaires sur tout l'internet et elle est de retour avec ce cours mis à jour.

Dans le cours, vous apprendrez les fondamentaux de VUE et appliquerez ce que vous apprenez pour construire un site web de commerce électronique.

Voici les sections de ce cours :

* Qu'est-ce que Vue.js ?
* Installation de Vue 3
* Directives Vue JS
* Événements et Méthodes
* Composants
* Props des Composants
* Hooks de Cycle de Vie
* Démo de l'Application
* Ajout d'Articles au Panier
* Composants Réutilisables
* Vue CLI
* Structure des Dossiers Vue
* Barre de Navigation Supérieure
* Stylisation avec SASS
* Barre Latérale
* Ajout d'Articles au Panier

Regardez le cours complet ci-dessous ou sur la chaîne YouTube freeCodeCamp.org (4 heures de visionnage).

%[https://youtu.be/FXpIoQ_rT_c]

## Transcription

(autogénérée)

Gwendolyn Farraday a précédemment créé l'un des cours Vue les plus populaires sur l'internet.

Maintenant, elle est de retour avec un tout nouveau cours complet sur Vue pour enseigner la dernière version aux débutants absolus.

Bonjour à tous.

Je m'appelle Gwendolyn Faraday et je serai votre instructrice pour ce cours.

Je suis développeur logiciel professionnel depuis plus de cinq ans maintenant.

Et j'ai eu l'opportunité de travailler dans plusieurs langages et frameworks différents au fil des ans, y compris Angular, React et Vue js.

Je travaille actuellement en tant que consultante logicielle dans diverses technologies, et j'utilise Vue js comme mon framework front-end préféré pour tout type d'application web ou mobile.

Si vous souhaitez me contacter, vous pouvez me trouver partout en ligne à Faraday Academy.

Si vous avez des commentaires spécifiques pour ce cours, veuillez m'envoyer un email à gwenf@protonmail.com.

J'espère que vous apprécierez ce cours.

Vue js est un framework JavaScript pour construire des applications et des sites web.

Comment vous aide-t-il ? Il fournit des outils prêts à l'emploi pour vous aider à rendre vos sites web et applications plus rapides et plus dynamiques.

Et il vous donne également un ensemble de normes pour l'organisation du code et des attentes pour les individus et les équipes qui travaillent sur la même base de code.

Si vous avez déjà entendu parler du DOM virtuel, Vue js est un framework de DOM virtuel.

Si vous ne savez pas ce que c'est, ce n'est pas grave.

Ce n'est pas important pour comprendre ce cours.

Le DOM virtuel rend essentiellement les applications web JavaScript un peu plus rapides et plus efficaces. Vue en lui-même est extrêmement léger, vous pouvez le réduire à environ huit ou dix kilo-octets gzippés.

Bien que dans un sens pratique, votre Vue et JavaScript regroupés ne seront probablement jamais aussi petits dans une application de toute façon.

Bien qu'il soit bon de savoir que Vue n'a pas beaucoup de code supplémentaire prenant plus de place dans votre application.

Pourquoi Vue JS s'appelle-t-il un framework progressif ? Ils utilisent le terme progressif pour signifier que vous pouvez l'utiliser partout, depuis de petites fonctionnalités sur des sites web où vous voulez ajouter un peu d'interactivité et l'utiliser comme une sorte de remplacement pour jQuery et des applications héritées.

Jusqu'à l'utiliser comme un framework plus complet avec des fonctionnalités incluses pour des applications à grande échelle comme Gmail ou Twitter ou quelque chose de similaire.

Vous décidez quelles fonctionnalités vous voulez ajouter depuis l'écosystème Vue au-delà de la bibliothèque principale, et il est extrêmement flexible pour vous permettre de choisir les outils et autres bibliothèques que vous voulez par vous-même.

Ou vous pouvez utiliser ceux que Vue fournit dans son écosystème par défaut, beaucoup de gens et d'entreprises l'utilisent pour sa nature adoptable de manière incrémentielle.

Cela signifie que si elles ont une application héritée, il est assez simple de mettre à jour leur application page par page pour en faire une application Vue, une application plus moderne, au lieu de devoir réécrire toute l'application en une seule fois.

C'est une chose très pratique à propos de Vue j s.

Jetons un coup d'œil rapide à l'histoire de Vue.

Le projet Vue a été lancé en 2013 par son fondateur, Evan You.

En 2014.

La version un a été lancée et a commencé à devenir populaire en Chine où Evan est originaire. Quelques années plus tard, Vue deux a été lancée avec de nombreuses nouvelles mises à jour et améliorations par rapport à Vue version un.

Et avec la sortie de la version deux, c'est vraiment là que nous commençons à voir la croissance massive de Vue j s et sa popularité dans le reste du monde.

Beaucoup de développeurs n'avaient pas entendu parler de VueJs avant 2017.

Mais à partir de 2017, et surtout en 2018 et 2019, Vue s'est vraiment imposé comme l'un des trois principaux frameworks JavaScript.

De nombreuses conférences Vue ont commencé à apparaître, beaucoup de création de contenu autour de l'écosystème Vue a commencé à avoir lieu.

Et de nombreuses entreprises ont commencé à utiliser Vue pour leurs applications également.

En fait, de nombreuses entreprises que vous reconnaissez, qui sont des noms familiers en Occident, utilisent Vue, j s maintenant.

Et maintenant nous pouvons voir que Vue version trois a été publiée à l'automne 2020.

Et au fil des six dernières années, nous voyons de nombreuses bibliothèques différentes qui sont également créées et maintenues par Evan et l'équipe principale de Vue.

Comme le vcli Vue router in Vue x, également régulièrement mis à jour pour correspondre à la version actuelle de Vue.

Même maintenant, avec Vue trois tout juste sorti, nous voyons qu'une nouvelle version de Vue, router et VX ont également été publiées pour être compatibles avec Vue version trois.

Dans ce cours, nous utiliserons la bibliothèque principale de Vue j s ainsi que le vcli.

Pour plus d'informations sur Vue, x Vue router, Vue test utils et certains des autres outils de l'écosystème Vue que je ne couvre pas en profondeur dans ce cours, je ferai des cours futurs sur ceux-ci sur ma chaîne YouTube Faraday Academy.

Alors commençons à apprendre v j, s.

Et gardez à l'esprit, j'utilise v3 ici.

Alors assurez-vous d'être sur le bon site, qui est v3 dot Vue, J s.org.

Et puis cliquez sur getting started ici.

Cela vous amènera à la documentation.

Et par défaut, l'introduction à Vue j s, je vais aller directement au lien d'installation sur la barre latérale ici.

Et si je fais défiler vers le bas, je peux voir l'endroit où il est écrit CDN.

Et vous remarquerez ici qu'il est écrit Vue add next, assurez-vous d'importer la bonne bibliothèque depuis la bonne URL ici, next est nécessaire, car Vue trois n'est pas encore dans le dépôt principal de Vue j s, il est dans ce autre dépôt que vous pouvez référencer avec ce next, qui pointe vers Vue trois, jusqu'à ce que tout l'écosystème et tout le reste finissent d'être mis à jour.

Il y aura une différence entre importer Vue deux et importer Vue at next, qui pointe vers Vue version trois.

Et je vais prendre cette balise de script ici.

Donc je suis dans VS code, et je n'ai qu'un simple fichier HTML.

Et je vais ajouter Vue j s dans cette application pour démontrer les bases de la syntaxe Vue avant de me lancer dans la construction d'une application plus grande avec le Vue COI.

Tout d'abord, je vais utiliser un plugin VS code appelé live server.

Et vous pouvez voir en bas ici qu'il est écrit go live.

Donc si vous allez dans les plugins, qui est cette icône de quatre boîtes sur le côté, vous pouvez taper live server et cliquer sur ce plugin.

Et vous pouvez l'installer si vous ne l'avez pas déjà installé.

Mais je l'ai déjà installé et activé.

Donc je vais revenir à mon code ici.

Et en bas, je vais juste cliquer sur go live.

Et vous pouvez voir qu'il affiche ma page HTML, je vais juste zoomer un peu ici avec le contenu statique.

Maintenant, si vous ne voulez pas utiliser live server, vous pouvez juste venir ici et faire un clic droit et cliquer sur copier le chemin.

Et puis vous pouvez aller dans votre navigateur et coller ce chemin absolu vers le projet ou vers votre fichier index dot HTML.

Et il s'affichera de la même manière dans le navigateur.

Live server rend simplement les choses un peu plus faciles car il rafraîchit automatiquement lorsque vous faites des changements de code.

Et il ouvre également la page du navigateur pour vous.

Mais c'est à vous de voir si vous voulez l'utiliser ou non.

Maintenant, je veux ajouter Vue à cette application.

Donc je vais aller à l'intérieur de la balise body et juste en dessous de cette div, coller la balise de script que je viens de copier.

Donc maintenant, c'est tout ce que j'ai à faire pour importer Vue et commencer à l'utiliser dans mon application.

Je n'ai pas réellement besoin de Babel ou autre chose pour commencer.

Donc pour écrire mon propre code personnalisé, je vais ajouter ma propre balise de script juste en dessous.

Donc il y a essentiellement deux choses que je dois faire ici.

Et la première est d'utiliser cette variable Vue à laquelle j'ai accès depuis l'importation de Vue.

Et cette balise de script et Vue me donne cette méthode appelée create app.

Et cela crée essentiellement mon application Vue.

Et je peux lui passer un objet d'options, ce que je vais faire dans une seconde.

Maintenant, je dois somehow connecter ce JavaScript pour mon application Vue avec le HTML que je vais afficher dans le navigateur.

Et cela se fait par une autre méthode que je peux enchaîner sur cette instance Vue que je crée.

Donc je vais en fait enregistrer cela comme une variable.

Je vais dire let app equals Vue create app.

Et puis je vais utiliser cette autre méthode appelée Mount car je veux lui dire de monter mon application Vue quelque part dans mon HTML ici.

Donc je vais faire ID equals, je vais simplement l'appeler app.

Et je vais en fait lui dire de monter mon application Vue j s à l'intérieur de cette div.

Et cela signifie que l'instance Vue j s que je crée ici pourra se connecter et afficher des données et interagir avec n'importe quel élément DOM à l'intérieur de cette div ici.

Donc cela sera plus clair dans une seconde.

Donc maintenant, laissez-moi changer cela, laissez-moi créer une variable sur mon instance Vue.

Et pour cela, je dois créer une fonction appelée data ici.

Maintenant, cet objet entier ici est appelé l'objet d'options.

Donc toutes les variables ou fonctions que je vais utiliser dans mon application vivront sur cet objet ici.

Donc spécifiquement avec data qui est une fonction, et elle doit retourner un objet.

Et sur cet objet qui est retourné par la fonction data, je peux mettre toutes les variables que je veux.

Donc je vais créer une variable de salutation.

Et je vais dire bonjour, v3, puis point d'exclamation.

Et maintenant je peux aller dans ma div ici, supprimer ce code statique là.

Et je vais utiliser ma variable maintenant.

Donc pour utiliser une variable dans Vue, vous utilisez cette syntaxe de double accolade, elle est appelée syntaxe de double moustache, qui est un peu difficile à prononcer.

Donc vous pouvez simplement l'appeler double accolades.

C'est une syntaxe courante dans les langages de templating.

Et cela signifie essentiellement que tout ce qui se trouve entre ces ensembles de doubles accolades sera analysé comme du JavaScript par Vue.

Donc Vue va d'abord chercher à l'intérieur de cet objet data que nous retournons, et voir s'il y a une variable nommée greeting, puis il va afficher cette variable ou la valeur de cette variable à l'intérieur de ces accolades.

Et vous pouvez voir que maintenant il affiche la variable de salutation de notre instance Vue.

Parlons des directives Vue j.

s. Elles sont essentiellement un moyen de connecter des éléments dans notre HTML ou template ici avec le JavaScript Vue j.

s. Et voyons à quoi cela ressemble à travers un exemple.

Je vais créer une entrée ici.

Dans le navigateur, cela ressemble à ceci.

Maintenant, que se passe-t-il si je veux obtenir la valeur de cette entrée ? Vue a un moyen intégré de le faire à travers une directive appelée v model.

Maintenant, ces directives dans Vue sont utilisées comme un attribut HTML, mais elles sont précédées de v dash pour les différencier des attributs HTML réguliers.

Et Vue, lorsqu'il analyse cette application Vue, verra ce mot-clé v model, et le liera à la variable que nous passons en argument au modèle ici.

Donc ici, entre guillemets, je dois mettre un nom de variable.

Et je vais mettre la variable greeting ici.

Et voyons ce que cela fait.

Donc vous pouvez voir maintenant dans mon entrée, elle commence avec le texte Bonjour Vue.

Et lorsque je la change, elle change également la variable de salutation qui est affichée sur la page.

Cela s'appelle la liaison de données bidirectionnelle et est gérée dans Vue avec cette directive V model.

Regardons une autre directive.

Je vais créer un HR ici.

Et je vais faire une div avec une classe de box.

Et je vais utiliser une autre directive ici appelée v if, qui prend également un argument, qui sera une autre variable.

Donc je vais définir une variable is visible que je dois créer.

Donc je vais faire is visible et le définir à true pour commencer, je vais coller un peu de style que j'ai fait.

C'est juste pour styliser la boîte afin que vous puissiez la voir sur la page.

Génial que vous puissiez voir que je vois cette boîte, car cette directive V if est essentiellement comme une instruction if en JavaScript.

Donc si cette valeur est vraie, alors cet élément sera affiché sur la page.

Mais si c'est faux, cette div ne sera pas rendue dans le DOM du tout.

Donc je vais changer cette variable à false.

Et vous pouvez voir la boîte disparaître.

Et si je vérifie, je peux inspecter l'élément.

Et il n'y a aucune div trouvée dans le DOM.

Maintenant, v If est très similaire à V show, qui est une autre directive vj s, elle prend le même type d'argument, une expression booléenne.

Et je vais le définir à true à nouveau, vous pouvez voir que si c'est vrai, il s'affiche sur la page, tout comme v if.

Cependant, lorsqu'il est faux, vous pouvez voir qu'il y a toujours une div, rendue dans le DOM.

La seule différence est que le style est défini sur display none.

Donc vous ne le verrez pas réellement, mais il est là dans le DOM.

Alors, quand utiliseriez-vous v show ? Eh bien, dans la plupart des cas, vous utiliseriez simplement v if, car vous voulez soit que quelque chose soit rendu, soit non.

Par exemple, si vous avez un spinner de chargement, vous utiliseriez V, si c'est en train de charger, affichez le spinner.

Et ensuite, lorsque la page ou ce que vous voulez a chargé, vous définissez la variable à false et ensuite v if la supprimera du DOM.

Maintenant, v show est utile pour des cas spécifiques, lorsque vous pourriez avoir besoin de basculer quelque chose plus fréquemment.

Et ce serait plus performant que de l'ajouter et de le supprimer constamment du DOM.

Donc, il est déjà là, tout ce que vous faites est de changer le CSS.

Donc, vous le changez de display none à display block.

Donc, en revenant à Vf.

Il y a d'autres directives que vous pouvez enchaîner à Vf.

Il y a v, elsif, et V else.

Et vous pouvez déjà deviner ce que ces directives font.

Donc, je vais simplement vous montrer la syntaxe ici.

Donc, v else if et V else est celui qui ne prend aucun argument.

Et je vais simplement démontrer ceux-ci très rapidement.

Je vais ajouter une autre variable ici.

Donc, is visible est visible deux.

Donc, j'ai ajouté un peu plus de CSS ici pour différencier entre les trois boîtes que j'ai créées ici.

Et cela fonctionne comme une instruction if else régulière.

Donc, si is visible est vrai, cette div sera rendue.

Si ce n'est pas vrai, il va continuer à descendre la chaîne.

Donc, il va regarder tous les v else if que vous avez ici, vous pouvez en avoir autant que vous voulez.

Donc, il va regarder is visible deux pour voir si c'est vrai.

Si ce n'est pas vrai, alors il va automatiquement afficher cette troisième boîte.

Maintenant, la troisième boîte est bleue, la deuxième boîte est rouge, et la première boîte est violette.

Donc, vous pouvez voir la boîte bleue affichée car les deux autres valeurs étaient fausses.

De même, je pourrais changer l'une de ces variables à vrai.

Et alors cette boîte serait rendue dans le DOM ici.

Maintenant, je veux souligner quelque chose ici, si je rafraîchis la page, vous pouvez voir pendant une fraction de seconde, vous avez en fait vu toutes les boîtes se rendre, ainsi que les accolades s'afficher à l'écran ici avant qu'elles ne soient analysées comme une variable Vue.

Je vais rafraîchir la page à nouveau et la ralentir un peu, au cas où vous n'auriez pas pu voir cela.

Donc, comment puis-je empêcher cela de se produire ? Vue a quelque chose appelé v cloak, qui est un utilitaire pratique qui masquera tout ce qui est rendu jusqu'à ce que toute l'application Vue soit prête.

Donc, je vais ajouter un V cloak ici.

Et puis, je dois essentiellement ajouter un style pour cela.

Donc, vous pouvez voir, je définis v cloak ou cet attribut V cloak à display none.

C'est le modèle recommandé dans Vue js.

Et puis, je vais simplement ajouter un V cloak à ma div avec mon app dedans.

Maintenant, si je reviens ici et que je rafraîchis, vous ne voyez plus les accolades ou les autres boîtes se rendre.

Comment cela se produit-il ? Je vais inspecter l'élément.

Et vous pouvez voir sur la div avec l'ID app ici, il n'y a pas d'attribut v cloak.

Mais si je rafraîchis la page, vous ne pouvez pas vraiment le voir car c'est trop rapide.

Mais essentiellement, cet attribut V cloak reste sur cette div jusqu'à ce que l'application soit chargée, puis il est supprimé.

Une fois que tout est rendu dans le DOM.

Je ne rencontre pas souvent de cas où je dois utiliser cela manuellement, mais c'est une fonctionnalité utile à connaître si vous rencontrez ce problème.

Ce n'étaient que quelques directives de base.

Nous couvrirons définitivement plus de directives au fur et à mesure que nous avancerons dans ce cours.

Dans la prochaine vidéo, nous allons passer en revue les événements et les méthodes dans Vue js.

Maintenant que vous avez vu comment utiliser des variables et des directives dans Vue, j s, rendons ce code un peu plus interactif avec un. Vous savez probablement déjà qu'il existe de nombreux événements qui peuvent être capturés dans le navigateur et utilisés dans nos applications.

Par exemple, lorsque l'utilisateur clique sur un élément à l'écran, comme un bouton, ou si l'utilisateur appuie sur une certaine touche du clavier, comme Entrée pour soumettre un formulaire, essayons ces deux cas dans notre petite mini-application ici.

Tout d'abord, je vais me débarrasser des deux boîtes supplémentaires.

Et je vais ajouter un bouton ici.

Que pour l'instant, je vais étiqueter comme showbox.

Donc maintenant, ce V if est défini sur false ou la variable is visible est définie sur false.

Donc cette div ne sera jamais rendue sur la page à moins que nous ne mettons à jour cette variable d'une manière ou d'une autre.

Auparavant, nous codions en dur la valeur de la variable ici comme true ou false.

Mais nous pouvons en fait utiliser ce bouton pour changer la valeur de la variable également.

Et cela se fait avec une autre directive appelée v dash on.

Maintenant, la directive v dash on est spécifique pour les événements.

Vous pouvez l'utiliser pour des événements personnalisés que vous créez vous-même.

Ou vous pouvez l'utiliser pour l'un des événements standard du navigateur, comme, comme je l'ai mentionné précédemment, lorsqu'un utilisateur clique ou appuie sur une touche de son clavier.

Donc ici, spécifiquement, je vais faire v on colon, et puis le type d'événement qui sera un événement de clic.

Donc j'écoute un événement de clic sur ce bouton en ce moment.

Mais maintenant, lorsque quelqu'un clique sur le bouton, je dois vous dire quoi faire avec cet événement de clic.

Donc je dois passer en argument tout le JavaScript que je veux exécuter lorsque ce bouton est cliqué.

Et pour l'instant, je vais garder cela simple.

Et je vais définir la variable is visible à true lorsque ce bouton est cliqué.

Maintenant, vous pouvez voir que j'ai ce bouton show box.

Lorsque vous cliquez dessus, la boîte s'affiche. Que se passe-t-il si je veux masquer la boîte.

Pour l'instant, cela ne fait que montrer la boîte.

Et la seule façon de s'en débarrasser est de rafraîchir.

Je peux mettre en place un basculement pour la boîte, en disant simplement is visible est égal à l'opposé de ce qu'elle est actuellement.

Donc is visible est égal à not as visible.

Donc si c'est vrai, il sera défini à faux.

Si c'est faux, il sera défini à vrai.

Et cela devrait basculer notre boîte, nous étiquetons cela pour basculer la boîte.

Et maintenant, si je continue à cliquer sur les bascules on et off, c'est essentiellement comment les événements fonctionnent.

Il y a aussi un raccourci pour créer des événements.

Donc vous n'avez pas à taper le dash on colon, vous pouvez simplement taper le symbole app, et puis le nom de l'événement.

Et c'est exactement la même chose que lorsque j'ai tapé v dash on colon.

le symbole at remplace tout cela.

Que se passe-t-il si vous voulez faire quelque chose de plus complexe ici, pas seulement définir une variable à True ou false ? Eh bien, vous pouvez en fait utiliser cela pour passer n'importe quelle méthode sur votre objet VJs.

Donc je vais me débarrasser de is visible ici.

Et je vais créer une méthode appelée toggle box.

Et maintenant, je dois créer cette méthode toggle box.

Vous pouvez voir que j'ai déjà des données sur mon objet vj s, cette fonction de données.

Mais maintenant, je dois faire une autre clé, qui s'appelle méthodes et méthodes est un objet de fonctions.

Je peux mettre autant de fonctions que je veux sur cet objet méthodes pour pouvoir utiliser celles-ci dans mon application Vue, j s.

Donc laissez-moi créer cette fonction toggle box.

Je pourrais faire la même chose ici que j'ai fait ci-dessus, mais je vais juste utiliser le raccourci de la fonction et je veux la même logique à nouveau mais à l'intérieur de cette fonction, donc pour me référer à cette variable is visible ici, je dois l'obtenir à partir du contexte this.

Et Vue j s gère la mise de toutes mes méthodes et variables sur le contexte this afin qu'elles soient disponibles pour moi n'importe où dans mon application Vue.

Donc je peux faire this.is visible et ensuite le définir égal à not this.is visible This is not function there.

Et cela devrait fonctionner de la même manière que précédemment.

Donc je peux le tester et basculer la boîte une fois de plus.

Donc c'est les bases de comment les méthodes fonctionnent.

Et vous pouvez voir parce que j'ai appelé ma méthode toggle box, qu'elle est également disponible pour moi n'importe où à l'intérieur de mon template Vue JS ici.

Donc regardons un autre type d'événement.

Et ce sera un événement écoutant l'entrée du clavier.

Donc ici, je veux écouter les pressions de touches.

C'est aussi un événement.

Donc je vais commencer avec le symbole Add.

Et écouter un événement key up.

Je pourrais aussi utiliser key down si je le voulais.

Donc pour les événements du clavier, je dois ajouter un modificateur pour dire quelle entrée du clavier je suis en train d'écouter.

Donc pour l'entrée ici, je veux exécuter une fonction ou un JavaScript, chaque fois que j'appuie sur la touche Entrée.

Donc pour Entrée, j'ai en fait un raccourci parce que c'est une entrée de clavier courante.

Donc je peux dire, Écouter l'événement key up spécifiquement avec la touche Entrée.

Ou je peux toujours utiliser le code clé associé à n'importe quelle touche du clavier.

Donc pour Entrée, ce serait 13.

Peu importe celui que j'utilise, je vais simplement utiliser key up dot enter, parce que c'est un peu plus évident ce que c'est.

Et puis c'est la même syntaxe ici.

Et je vais créer une méthode greet pour cet événement key up.

Donc laissez-moi descendre à mes méthodes, créer une méthode appelée greet.

Utiliser le raccourci de la méthode.

Et je vais simplement faire console dot log, this dot greeting.

Et voyons comment cela fonctionne.

Donc je peux simplement me concentrer sur cette entrée n'importe où et simplement appuyer sur Entrée, peu importe ce qui est déjà dans l'entrée.

Et vous pouvez voir qu'il journalise la salutation.

Si je change l'entrée, il journalise ce que la variable de salutation est actuellement définie.

Maintenant, que se passe-t-il si je veux passer quelque chose dans une fonction lorsque je l'appelle dans l'une de ces méthodes, alors je pourrais le faire, simplement en ajoutant les parenthèses pour appeler la fonction.

Par exemple, greet ici, je peux simplement passer quelque chose.

Donc juste à des fins de démonstration, je vais passer le greeting à travers le template ici.

Je vais accepter cela ici.

Et je l'appellerai toujours greeting.

Et puis me débarrasser de cela parce que je ne cherche plus la variable de salutation.

Sur l'instance vj s ici, je vais en fait utiliser la variable de salutation que je passe ici.

Et juste pour vous montrer que c'est différent, je peux utiliser la variable de salutation et puis la passer avec des points d'exclamation ajoutés.

Et maintenant lorsque je vais ici, et que je clique sur Entrée à nouveau, vous pouvez voir que c'est la variable de salutation que j'ai passée à travers le template.

Si j'efface quelques caractères ici, appuie sur ENTER à nouveau, vous pouvez voir qu'il s'agit toujours de la même variable définie sur la nouvelle valeur.

Ce sont les bases de l'utilisation des événements et des méthodes dans Vue js.

Je veux souligner ici, vous voyez ce point enter, c'est un modificateur d'événement dans Vue js.

Donc vous n'écoutez pas seulement l'événement key up, vous écoutez spécifiquement la touche enter.

Maintenant, il y a de nombreux modificateurs que vous pouvez utiliser.

Par exemple, à cet événement de clic ici, par exemple, j'ai un modificateur ici qui dit que je n'écoute que les clics droits.

Donc un clic gauche normal sur une souris ne déclenchera pas cette bascule de boîte.

Mais seulement si vous faites un clic droit, je peux aussi utiliser des modificateurs pratiques comme prevent.

Donc si je ne veux pas qu'un formulaire soit soumis au lieu d'utiliser le regular event dot prevent default dans ma méthode, je peux simplement ajouter ce modificateur ici dot prevent.

Et je peux faire cela pour stop propagation aussi.

Donc je pourrais ajouter ce stop.

Vous pouvez enchaîner autant de ces modificateurs que vous voulez dans Vue j s, il y a définitivement une chose pratique à savoir lorsque vous construisez des applications Vue.

C'est tout pour cette vidéo, nous approfondirons les événements et les méthodes plus tard dans ce cours et dans les cours futurs.

Dans la prochaine vidéo, nous allons parler des composants personnalisés dans Vue js.

Parlons des composants Vue.

Maintenant, lorsque nous avons créé notre application Vue ici, nous utilisons essentiellement un seul composant standard, vous pourriez l'appeler juste un objet d'options par défaut pour une utilisation dans notre template.

Donc maintenant, nous allons travailler sur la division de parties de notre application en composants séparés afin de nous préparer à apprendre comment construire des applications plus grandes et travailler sur des applications avec le Vue COI en dehors d'un seul fichier HTML.

Prenons une pause du code pendant une seconde et jetons un coup d'œil à ce que nous allons construire avec les composants Vue, nous allons utiliser un exemple simple de formulaire pour travailler sur la division d'une application en composants séparés.

Maintenant, là où vous voyez le contour rouge, chacun d'eux sera un composant séparé.

Donc le contour rouge extérieur autour de tout le formulaire de connexion sera son propre composant de formulaire de connexion.

Et ensuite chaque entrée avec son étiquette sera un composant d'entrée personnalisé que nous allons créer et pouvoir réutiliser pour autant d'entrées que nous avons.

Donc nous allons commencer par ce composant extérieur, puis extraire les composants intérieurs dans leurs propres composants après cela.

Et ensuite nous allons voir comment vous pouvez faire passer des données entre les composants de votre application.

À quoi ressemblerait un composant Vue ? Disons que nous voulons avoir un formulaire ici.

Et je vais me débarrasser de cette salutation très rapidement.

Et mettre un formulaire ici.

Donc je pourrais faire cela directement dans le HTML et créer une balise de formulaire.

Ou je peux créer une balise personnalisée en tant que composant Vue appelé custom form.

Maintenant, c'est la même syntaxe que si c'était une balise HTML.

Sauf, bien sûr, ce n'est pas une balise HTML standard.

Donc je dois la définir comme un composant Vue ici.

Et je dois la définir après avoir défini ma variable app, qui est mon instance Vue.

Et avant de la monter réellement dans le DOM, donc je peux l'enchaîner ici comme app dot component.

C'est une fonction et elle prend deux arguments ici que je vais passer.

Donc le premier est le nom du composant que je vais utiliser.

Et c'est le nom que je vais utiliser dans mon HTML là-haut.

Donc je vais lui donner le même nom custom form.

Et le second est un objet d'options.

Et puisque c'est son propre composant autonome, je peux en fait utiliser n'importe laquelle des mêmes options que j'ai utilisées ici, comme data et methods, etc.

La seule chose supplémentaire dont j'ai besoin pour l'instant est que je dois définir un template pour ce composant.

Et le moyen le plus simple de définir un template est d'utiliser des graves.

Donc je peux faire cela sur plusieurs lignes et passer le HTML ici.

Donc très rapidement, je vais créer une div.

Et je vais juste mettre, disons, deux entrées ici pour l'instant, mais de type email, et ensuite une entrée de type mot de passe.

Et appelons cela un formulaire de connexion.

Puisque nous faisons email et mot de passe, je vais changer cela ici en formulaire de connexion.

Et puisque le template est la seule option requise que je dois passer dans cet objet, cela devrait fonctionner comme c'est maintenant.

Donc laissez-moi voir si cela fonctionne.

Je vais cliquer sur go live.

Et vous pouvez voir ces deux champs de formulaire en haut ici, complètement non stylisés, juste des entrées de navigateur de base.

Donc je vais styliser ces entrées très rapidement, pour qu'elles soient plus faciles à voir.

Après toutes ces boîtes, je vais ajouter une référence à l'entrée ici.

Je vais dire une marge de 10 pixels juste sur tous les côtés, et un affichage de block pour qu'elles ne soient pas en ligne.

Et maintenant elles sont un peu plus faciles à voir ici.

D'accord, laissez-moi recoder les styles à nouveau.

Et maintenant laissez-moi ajouter une méthode de données à ce composant.

Donc vous pouvez voir à quoi cela ressemble.

Donc après cette clé de template que j'ai ici, je vais faire la même chose que j'ai fait ci-dessus.

Avec les données, je vais juste utiliser le raccourci de fonction ici, retourner un objet.

Et ici, je vais lui donner un titre.

Et le titre sera formulaire de connexion.

Et maintenant, je dois faire quelque chose avec ce titre.

Donc là-haut, lorsque j'ai défini des variables, je les utilise à l'intérieur de mon template d'application ici.

Mais puisque mon formulaire de connexion est un composant autonome, toutes les variables que je définis sur les données ici, je vais devoir les utiliser à l'intérieur de son propre template.

Donc je vais juste ajouter une autre ligne ici et lui donner un h1 et au fait, cela n'a pas de coloration syntaxique, et c'est un peu une forme de template bizarre.

Parce que je fais tout cela dans un seul fichier HTML.

C'est juste une pierre d'achoppement pour passer à des moyens plus standard de créer des composants Vue où vous aurez une coloration syntaxique, et une complétion automatique et toutes ces autres grandes fonctionnalités.

Donc ici, je dois utiliser cette variable titre.

Donc je vais l'utiliser de la même manière que je l'ai fait avant en la référençant.

Et maintenant, je devrais voir le titre au-dessus de ces deux champs de saisie.

Et en effet, je le vois ici, je suis assez zoomé.

Donc c'est les bases de la façon dont vous pouvez créer un composant ici, je vais continuer à construire ce formulaire, et puis aussi vous montrer comment composer des composants maintenant.

Donc je vais juste changer cela très rapidement en formulaire.

Et puis je vais ajouter une fonctionnalité de soumission ici.

Donc je vais ajouter un événement pour la soumission, soumission, et puis passer un argument avec la méthode que je veux exécuter ou la fonction que je veux exécuter lorsque je soumets un formulaire.

Donc je vais simplement appeler ma fonction, je suppose handle Submit.

Et puis je dois créer un objet méthodes ici avec cette fonction.

Je l'appellerai handle, submit.

Et je vais juste faire console dot log submitted.

Donc maintenant, lorsque le formulaire est soumis, il exécutera cette fonction, il y a quelques autres choses que je dois faire, je dois ajouter un bouton ici, qui soumettra réellement le formulaire.

Par défaut, les boutons sont de type submit, donc je n'ai pas besoin de l'ajouter ici.

Mais je vais ajouter du texte au bouton.

Maintenant, lorsque le formulaire est soumis, il rafraîchit toute la page.

Bien sûr, c'est le comportement par défaut dans les navigateurs.

Donc vous pouvez simplement cliquer et envoyer des données du formulaire à votre back-end.

Mais puisque nous allons gérer la soumission du formulaire à partir de notre fonction handle submit, nous ne voulons pas ce comportement par défaut avec le rafraîchissement de la page.

Donc, comme nous l'avons vu plus tôt, nous avons des modificateurs d'événements.

Donc nous pouvons faire prevent, pour empêcher le comportement par défaut, ce serait la même chose que de passer un objet événement à notre fonction handle submit, et puis faire e dot prevent default.

Encore une fois, ce n'est qu'un raccourci.

Donc maintenant, si nous regardons notre console, ici, nous voyons qu'il journalise soumis lorsque nous soumettons le formulaire.

Donc maintenant, nous voulons probablement capturer ces entrées.

Donc nous pouvons faire cela.

Encore une fois, en utilisant la directive v model pour lier à la valeur de l'entrée du formulaire à une variable, nous appellerons celle-ci email.

Et nous allons v model celle-ci comme password.

Et puis les ajouter dans les données.

Et maintenant, journalisons ceux-ci.

Donc, journalisons email.

Et password.

Bien sûr, si vous vous souvenez, je dois l'obtenir à partir du contexte this, puisque je le référence à l'intérieur de JavaScript ici.

Et maintenant, je devrais pouvoir taper quelque chose ici, cela doit être un email.

Donc je vais dire gwen@example.com.

Juste un mot de passe, et je vais cliquer sur Connexion.

Et vous pouvez voir qu'il a journalisé mes identifiants ici.

D'accord, donc c'est un composant.

Dans la prochaine vidéo, regardons comment décomposer ce composant et sortir les entrées pour les mettre dans des composants séparés, comme vous l'avez vu dans les maquettes plus tôt dans cette vidéo.

Et nous verrons également comment passer des données entre les composants.

Donc d'un composant parent à un enfant, puis également d'un enfant à un parent.

Que se passe-t-il si nous voulons composer plusieurs composants ensemble ? Démontrons cela en supprimant les entrées et en créant un composant personnalisé juste pour nos entrées de formulaire.

Disons que nous voulons une logique juste contenue dans un composant d'entrée spécial.

Donc laissez-moi plier cela rapidement.

Et je vais créer un autre composant ici.

Je vais faire app dot component à nouveau.

Et je vais appeler cela custom input en passant l'objet options.

Encore une fois, je dois avoir un template ici.

Et dans celui-ci, je vais simplement avoir Label Label lorsque j'affiche une variable label ici, puis je vais avoir cela envelopper l'entrée.

Et je vais utiliser un type, juste le texte par défaut pour l'instant, nous allons le changer dans une seconde.

Et c'est une entrée par défaut.

Donc maintenant, où vais-je utiliser ce composant, donc je vais en fait remplacer mes champs d'entrée dans ce composant par celui-ci que j'ai créé.

Donc ce que je peux faire ici est d'appeler ce Custom input, et custom input.

Et je peux utiliser mes composants à l'intérieur de cet autre composant.

Maintenant, il y a une étape supplémentaire que je dois faire ici.

Et c'est l'enregistrement du composant.

Donc je dois faire savoir à mon composant de formulaire de connexion l'autre composant personnalisé.

Et je peux faire cela ici en créant un tableau de composants, et puis juste lui donner la chaîne du composant que je veux utiliser, qui est custom input.

Maintenant, voyons comment cela fonctionne.

D'accord, donc j'ai ces deux entrées.

Maintenant, cela me donne cet avertissement, que la propriété label a été accédée pendant le rendu, mais elle n'est pas définie sur l'instance.

Cela se produit, car ici, je référence cette variable label, mais elle n'est définie nulle part.

Donc cela me donne cet avertissement.

Maintenant, je pourrais définir une fonction de données ici et créer la variable sur ce composant.

Mais je veux démontrer le passage de données d'un composant à un autre.

Donc au lieu de la définir sur ce composant, je vais en fait définir label sur le composant parent et le passer au composant custom input.

Pour cela, je vais venir ici et ajouter juste un label, laissez-moi ajouter, nous l'appelons email label pour l'instant.

Et je vais l'appeler email.

Et j'aurai aussi un password label et je vais appeler cela password.

Maintenant, je dois faire passer ces deux variables dans ces composants personnalisés ici.

Et donc ce que je vais faire ici, je peux aller de l'avant et me débarrasser du V model juste une seconde.

Et je vais ajouter un label ici que je vais passer.

Et je vais passer le email label.

Maintenant, cela ressemble juste à un attribut HTML.

Mais je vais en fait ajouter un modificateur ici.

C'est une directive Vue appelée v bind.

Ce que v bind fait, c'est essentiellement transformer cet attribut HTML régulier en quelque chose qui peut être analysé comme JavaScript afin que je puisse passer une variable au composant enfant.

Donc je vais v bind ce label, qui est email label, qui fait référence à cette chaîne ici, qui est email, cela sera passé comme une propriété au composant enfant appelé label.

Et maintenant dans ce composant enfant custom input, je dois recevoir cette propriété pour l'accepter ici avec un objet props.

Et la manière la plus simple d'écrire props est de faire un tableau de chaînes, tout comme je l'ai fait pour les composants personnalisés.

Et ces props sont essentiellement juste une liste de tous les noms des informations que je passe du parent à cet enfant.

Donc maintenant, parce que je définis label dans props, j'aurai accès à utiliser la variable label ici à l'intérieur de mon template.

Maintenant, si vous regardez le formulaire de connexion, vous pouvez voir que le champ email, il a un label ici, et vous pouvez dire qu'il s'agit d'un label car lorsque je clique sur le mot email, il se concentre sur le champ auquel il est lié.

Donc laissez-moi donner un label au mot de passe maintenant aussi, je vais passer password ici.

D'ailleurs, v bind, il y a aussi un raccourci pour V bind.

C'est l'une des directives les plus courantes dans toutes les applications Vue.

Donc le raccourci est au lieu d'utiliser v bind colon, vous utilisez simplement colon et puis label.

Donc laissez-moi passer un label ici aussi.

Donc je vais passer un label en tant que password label, puisque nous utilisons ce composant réutilisable, le label s'affichera toujours comme le label que nous passons.

Et maintenant vous pouvez voir que les deux champs de formulaire sont correctement étiquetés ici.

Maintenant, je veux souligner une chose très rapidement.

Et c'est pour les labels email et password, vous ne pourriez pas faire de variables pour ceux-ci et simplement les passer en tant que chaînes ici.

Par exemple, si je me débarrasse de la liaison du raccourci colon, alors je pourrais simplement passer, disons, password.

Et laissez-moi mettre enter email ici.

Donc c'est différent.

Et maintenant je peux simplement passer ce texte comme une chaîne.

Parce qu'il n'y a plus de v bind ici, Vue ne cherche plus une variable.

Donc maintenant dans l'application, vous pouvez voir qu'il passe simplement la chaîne comme un label au composant enfant et affiche cette chaîne, je vais faire ces changements.

Lorsque vous travaillez dans des applications Vue réelles, vous verrez que 95% du temps, vous voulez passer une variable lorsque vous passez une prop à un composant enfant, soit une variable de données, soit une sorte de fonction.

Donc vous utiliserez presque toujours cette syntaxe V bind ici.

Maintenant, il y a un problème car dans le composant enfant, nous avons l'entrée ici, nous n'écoutons pas réellement les changements de texte dans l'entrée, nous ne v modelons pas cela à une variable, donc nous n'avons pas accès à ce qui se trouve à l'intérieur de l'entrée.

Donc nous devons en fait créer un V model ici dans l'enfant, je vais enregistrer le modèle.

Et juste temporairement ici, je veux mapper cela à une variable dans l'enfant.

Et je pourrais juste l'appeler input value.

Et j'ai besoin de créer une fonction de données ici, de retourner un objet avec input value comme une chaîne vide.

Donc maintenant, dans ce cas, vous êtes déjà familier avec le modèle.

Et vous savez que chaque fois que nous tapons un caractère dans cette entrée, cela va mettre à jour cette variable et cette variable, et l'entrée resteront synchronisées.

Mais maintenant, comment puis-je obtenir la valeur de cette variable dans le composant parent ici, car je veux en fait qu'elle reste synchronisée avec ces deux variables sur le composant parent.

De cette façon, lorsque je soumets mon formulaire, je peux y avoir accès dans cette fonction handle submit.

Donc il y a en fait quelques façons différentes de faire cela.

Je vais vous montrer l'approche la plus simple pour commencer avec cela.

Et puis dans les cours futurs, je vais expliquer un peu plus en profondeur comment vous pouvez utiliser des événements personnalisés et d'autres méthodes pour capturer la valeur d'une variable de l'enfant au parent.

Donc pour commencer ici, je vais utiliser ma même variable d'entrée.

Mais je vais utiliser un nouvel objet ici.

Et cet objet s'appelle computed.

Je vais commenter data pour une seconde.

Donc computed est un objet où vous pouvez mettre des noms de variables ici comme clés.

Par exemple, cette variable input value que je veux créer, je peux la mettre ici comme clé.

Et chaque fois que cette valeur change, je peux en fait faire en sorte qu'elle exécute des fonctions getter et setter.

Donc je peux créer une fonction getter, et puis un setter.

Donc lorsque j'obtiens la valeur de la variable ici, elle exécutera cette fonction.

Et puis lorsque je vais définir la valeur de la variable, elle exécutera la fonction set.

Donc maintenant, quelle valeur veux-je mettre dans mon getter ici, je veux obtenir cette valeur à partir du composant parent.

Donc je vais en fait utiliser ces deux variables que j'ai déjà ici.

Et je vais me débarrasser de ces types.

Je ne les utilise pas encore.

Donc je me débarrasse de ceux-là.

Et je vais faire quelque chose de différent.

Je vais créer v model directement sur mon composant personnalisé ici.

Et je vous montrerai pourquoi dans une seconde.

Et je veux modéliser cela à la variable que je vais utiliser.

Donc pour celui-ci, c'est la variable password.

Et pour celui-ci, c'est email et ceux-ci sont sortis de l'ordre.

Donc je vais les échanger.

D'accord, donc maintenant je vais modéliser l'email et le password.

Et maintenant je veux obtenir ces variables dans mon composant enfant ici.

Maintenant, comment faire cela.

Donc dans props, je peux en fait accepter une prop appelée model value.

Et cela vient du parent.

Maintenant, cela ne ressemble pas vraiment à ce que nous passons une autre Prop, car nous ne v bindons aucune variable et ne la passons pas à l'enfant.

Mais en fait, ce que v modeling fait sur un composant enfant est en fait sous le capot, il nous donne une autre prop appelée model value, qui est mappée à email.

Donc v model fait quelques étapes à la fois, c'est une sorte de raccourci ici.

Donc j'ai accès à cette prop model value car j'utilise le model.

Donc je peux accepter cette prop dans l'enfant ici v model.

Et puis dans ma fonction getter, je peux faire this dot model value.

Et je peux retourner cela.

Donc maintenant, chaque fois que j'obtiens la valeur pour cette entrée, elle devrait être la même que la valeur dans le composant parent.

Et je peux vérifier cela en tapant simplement des valeurs ici.

Et vous pouvez voir que les entrées sont pré-remplies avec la valeur du composant parent.

Parce que je suis en train de v modeliser cette entrée à une fonction getter que je définis ici et en disant que la valeur sera this dot model value, qui provient de la variable V model dans le composant parent, qui sont ces variables.

Donc maintenant, comment gérons-nous la définition de la valeur si nous tapons du texte dans cette entrée ici, donc nous devons capturer la valeur d'abord et Vue la passe via un paramètre.

Donc nous pouvons donner à ce paramètre n'importe quel nom que nous voulons, je vais simplement l'appeler value.

Et je vais simplement d'abord journaliser cette valeur.

Et donc ici, je peux essayer de taper.

Et vous pouvez voir qu'il journalise la valeur de l'entrée à partir de ce journal dans la fonction setter.

Mais maintenant, il ne définit aucune variable nulle part.

Donc laissez-moi aller de l'avant et définir la variable.

Maintenant, pour cela, je vais utiliser une nouvelle méthode que vous n'avez pas encore vue.

Et c'est this dot dollar sign emit.

Ce que emit fait, c'est me permettre d'émettre des événements que d'autres composants peuvent écouter.

Et je peux faire passer des données autour de mon application Vue comme cela.

Je peux émettre des événements qui sont intégrés, comme je pourrais émettre un événement on click ou quelque chose comme cela.

Ou je peux émettre un événement personnalisé que je crée.

Pour l'instant, je vais utiliser un événement que Vue me donne et celui-ci s'appelle un événement de mise à jour.

Cette syntaxe est en fait nouvelle, légèrement mise à jour dans Vue trois.

Donc si vous voyez des tutoriels plus anciens, et qu'ils n'utilisent peut-être pas cette syntaxe exacte, ils utiliseront probablement un événement d'entrée ici à la place.

Mais je vais passer une valeur ici.

Oups, j'ai besoin d'une virgule.

Donc ce premier argument est le type d'événement que j'émets.

Et le deuxième argument est la valeur que je passe à travers cet événement, qui est cette valeur que j'obtiens de l'entrée via la fonction set.

Maintenant, comment puis-je écouter un événement dans un autre composant ? Je pourrais le définir manuellement.

Mais comme je l'ai dit avant, V model est un raccourci.

Donc V model écoute en fait cet événement de mise à jour de mon enfant.

Et chaque fois que cet événement de mise à jour est émis, ce V model du composant parent met à jour la valeur de la variable pour nous.

Testons cela.

Je vais commencer à taper ici, à taper ici.

Et je vais appuyer sur login.

Et vous pouvez voir qu'il journalise les valeurs de l'email et du mot de passe.

Donc ce n'est pas très clair.

Donc laissez-moi mettre un vrai email ici, ou un faux email en tout cas.

Et vous pouvez voir qu'il y a l'email et le mot de passe, qui proviennent de cette instruction de journalisation dans handle Submit.

Maintenant, vous vous demandez peut-être, pourquoi devons-nous passer par tous ces problèmes pour modéliser une variable d'un enfant à un parent.

Et la raison est que les props que nous passons aux enfants, elles sont immuables.

Nous ne pouvons pas les modifier dans l'enfant, ces variables sur les données ici ne peuvent être modifiées que dans le même composant.

Donc mon custom input ne peut pas changer quoi que ce soit que nous passons via les props ici.

Par exemple, si j'essayais de modéliser cela à label ici, en obtenant tous ces avertissements en tentant de muter la prop label, les props sont en lecture seule.

Donc je vais annuler cela.

C'est pourquoi j'ai dû créer cette variable supplémentaire dans l'enfant et créer un getter.

Donc je reçois cette prop model value en lecture seule du parent.

Et ensuite ce que je fais pour mettre à jour la valeur de cette prop, c'est que j'émets un événement vers le parent, cet événement de mise à jour de la model value.

Donc le parent, parce que j'ai ce raccourci V model, écoute cet événement.

Et ce composant, ce composant de formulaire de connexion, met en fait à jour ces variables lui-même.

Donc je ne mute pas réellement les props depuis l'enfant.

Maintenant, il existe définitivement d'autres façons de gérer le changement des props dans le composant enfant, je pourrais écouter les changements sur cette entrée.

Et je pourrais appeler une méthode sur un objet méthodes, qui pourrait faire la même chose, soit émettre un événement, je pourrais aussi passer une fonction du parent à l'enfant, et l'enfant peut appeler des fonctions dans le parent.

Et puis je pourrais mettre à jour les variables de cette manière aussi.

Il existe également d'autres solutions de gestion d'état.

Et nous explorerons toutes ces différentes options plus tard, je voulais juste vous donner un premier aperçu de la façon dont cela peut être fait dans Vue js, et spécifiquement dans Vue version trois, maintenant que la syntaxe a un peu changé.

Dans cette vidéo, nous avons passé en revue les composants personnalisés, la composition de composants ensemble, leur importation les uns dans les autres, comme nous le faisons avec ce custom input dans le composant de formulaire de connexion.

Nous avons également parlé de l'utilisation des props, du passage de données du parent à l'enfant, et ensuite de la possibilité de définir des données en émettant un événement que le parent peut écouter et en lui passant une valeur.

Dans la prochaine vidéo, nous allons parler des boucles dans Vue pour simplifier notre syntaxe ici avec plusieurs instances du même composant.

Maintenant, parlons des boucles.

Ici, nous avons deux instances du même composant, ces composants custom input.

Et j'aimerais pouvoir boucler à travers autant de ces composants que je veux.

Pour cela, je dois ajouter un tableau et des données ici.

Et ce tableau contiendra toutes les informations pour chaque entrée ici, y compris la variable à laquelle je veux modéliser le nom de l'étiquette.

Et je vais aussi ajouter un type.

Donc je vais créer un tableau ici appelé inputs.

Et juste pour démontrer rapidement, je vais ajouter quelques chaînes ici, comme email, password.

Et disons name.

Donc, si je voulais afficher toutes ces trois chaînes à l'intérieur du template ici, je vais revenir à la boucle sur le formulaire dans une seconde.

Mais pour l'instant, je vais créer une balise p ici.

Et je veux montrer chacune de ces chaînes à l'intérieur de sa propre balise de paragraphe.

Donc je vais créer une boucle pour celles-ci, je vais dire V four equals, et puis je dois passer le tableau ici, qui s'appelle inputs.

Et cela va boucler sur le tableau inputs.

Maintenant, c'est une boucle for in.

Donc je vais devoir créer une variable que je peux utiliser dans les itérations.

Donc je vais dire pour str, court pour string dans inputs, et maintenant j'ai accès à cette variable string à chaque passage dans la boucle.

Et je peux simplement l'afficher dans une variable maintenant.

Oui, il se plaint que j'ai fait une erreur dans ma syntaxe.

Et bien sûr, c'est parce que je n'ai pas mis de virgule après mon tableau.

Et maintenant vous pouvez voir que ces trois premiers ici sont des chaînes qui sont affichées dans une balise de paragraphe.

Bien sûr, elles sont si grandes parce que je suis zoomé si loin, mais elles s'affichent correctement.

Et c'est essentiellement comment vous utilisez une boucle dans Vue js.

Il me manque une prop ici que je dois ajouter.

Chaque fois que vous faites une boucle, vous devez ajouter une clé prop ici et cette clé doit être unique à chaque itération de la boucle.

Maintenant, les raisons d'utiliser cette clé prop sont un peu plus avancées.

Donc je ne vais pas entrer dans les détails dans cette vidéo.

Mais je veux juste que vous compreniez qu'il est bon de pratique pour vous d'utiliser une clé qui identifiera de manière unique tous les éléments que vous parcourez dans vos templates Vue JS.

Cela peut aider avec les performances et prévenir les bugs dans vos applications.

Et lorsque vous passez à la programmation d'une application Vue plus structurée avec des composants Vue dans leurs propres fichiers, vous verrez que votre linter et votre éditeur de code le détecteront si vous n'avez pas de valeur clé ici.

Et il vous donnera un avertissement et vous demandera d'en ajouter une.

Donc nous devons avoir une clé pour donner une référence unique à chacun de ces paragraphes que nous ajoutons dans le template.

Maintenant, ce que je peux faire puisque les noms sont uniques ici, chaque chaîne est différente.

Donc je peux v bind à la clé, la variable de chaîne str.

C'est une application Vue très simple.

Donc vous ne remarquez essentiellement aucune différence dans le navigateur.

Mais vous pouvez voir qu'il y a des clés attachées à ces éléments.

Maintenant, je veux souligner une autre façon dont vous pouvez créer cette clé unique à chaque itération de la boucle, vous pouvez en fait obtenir un index à chaque itération de la boucle.

Vous pouvez l'obtenir ici et ensuite l'utiliser comme votre clé.

Et si je fais un print de i, vous pouvez voir que i est l'index de chaque itération dans la boucle, je le remets en chaîne.

Donc c'était juste une démonstration, bien sûr.

Donc je vais en fait me débarrasser de toute cette balise p ici.

Et ce que je veux vraiment mettre dans les entrées ici, ce sont des objets pour les informations qui concernent chaque entrée que je veux.

Donc le premier, laissez-moi mettre un label ici.

Et je vais dire que le label est email, je vais créer une valeur ici.

Et c'est ce à quoi je vais V model.

Et puis je vais ajouter un type.

Donc disons que le type est email.

Et je vais faire la même chose pour le mot de passe.

Je peux me débarrasser de ceux-ci maintenant.

D'accord, donc maintenant mon application est cassée, parce que je me suis débarrassé de toutes les données que j'avais passées dans ces entrées personnalisées.

Et en fait, je vais me débarrasser de l'une de ces entrées personnalisées, parce que maintenant je vais boucler sur une seule, et elle en créera une pour chaque itération de la boucle.

Laissez-moi nettoyer cela un peu.

Mais ceux-ci sur des lignes séparées.

Et donc la première chose que je veux faire est créer un V four ici.

Et ce V four va parcourir les inputs, comme je l'ai fait avant, je vais dire four inputs in inputs.

Et je vais en fait obtenir l'index ici assez rapidement aussi.

Et puis utiliser une clé de V bind l'index.

Donc maintenant je ne peux pas v model email, je dois V model basé sur cet objet input, qui est chaque objet dans ce tableau inputs.

Donc je vais devoir V model input dot value ici pour le modéliser à la valeur.

Donc je vais faire input dot value, le label, aussi, je vais devoir faire input dot label.

Et maintenant j'ai un type.

Donc laissez-moi rebind un type aussi.

Et je vais faire input dot type.

Donc c'est une chose que je dois mettre à jour dans ce composant enfant.

Maintenant, j'accepte toujours cette prop model value et la prop label.

Mais je veux aussi accepter une prop type maintenant.

Et au lieu de faire type is text, maintenant j'ai une prop du parent basée sur le composant dans lequel elle se trouve dans la boucle.

Donc maintenant je vais V bind cela pour qu'il puisse prendre une variable, et je vais dire type, qui fera référence à la prop que j'ai passée.

Donc je vais venir à mon formulaire ici.

Et je vais taper et j'ai en fait oublié de changer la journalisation ici pour handle Submit.

Donc je ne veux pas compliquer les choses pour cet exemple.

Donc ce que je vais faire, c'est simplement supprimer cela et journaliser this dot inputs of zero et cette valeur et puis this dot inputs, ont un et puis cette valeur.

Et cela devrait résoudre mon problème ici.

Laissez-moi juste taper quelque chose.

Et il se plaint que je n'ai pas d'adresse email, je vais juste taper un faux email, login.

Et vous pouvez voir qu'il a mes bonnes informations de connexion.

Donc ce sont les bases de la gestion des boucles dans Vue j s, vous pouvez utiliser V for soit sur des éléments HTML réguliers comme un h1 ou sur n'importe quel composant personnalisé que vous faites également.

Cela est très couramment fait avec des composants de carte.

Si vous voyez un site web comme Pinterest, comment il montre toutes ces différentes petites boîtes avec de jolies photos dedans.

Si cela était fait en Vue js, il ferait cette boucle V for sur tous ces objets de données qui composent toutes ces cartes Pinterest sur votre mur Pinterest.

La dernière chose que nous devons examiner avant de passer à l'application de démonstration est les hooks de cycle de vie.

Donc nous les couvrirons dans la prochaine vidéo.

Un autre concept important dans Vue j.

s est les hooks de cycle de vie, également appelés hooks de cycle de vie des composants.

Donc qu'est-ce qu'un hook et qu'est-ce que les cycles de vie des composants.

Pour comprendre cela, j'ai fait une démonstration rapide.

Similaire à la démonstration avec laquelle nous avons commencé dans ce cours, je peux cliquer sur le bouton toggle box et une boîte apparaît.

Maintenant, j'utilise un V if pour prendre cette boîte, vous pouvez voir qu'elle a été ajoutée, vous pouvez voir qu'elle a été ajoutée au DOM.

Maintenant, si je clique à nouveau, elle a été complètement supprimée du DOM ici, tout ce processus d'entrée dans le DOM.

Et puis finalement de quitter le DOM.

C'est le cycle de vie de ce composant de boîte que j'ai.

Maintenant, parfois les choses peuvent quitter le DOM parce que vous naviguez vers une autre page, ou parce que quelque chose entre dans Vue via le défilement, ou parce que vous cachez et montrez quelque chose comme cet exemple.

Dans tous les cas, vous pouvez utiliser quelque chose appelé hooks de cycle de vie.

Un hook est simplement une fonction qui sera déclenchée pour s'exécuter à un point spécifique dans le cycle de vie d'un composant.

Par exemple, c'est une fonction qui sera appelée juste lorsque cette boîte violette apparaît à l'écran, ou juste avant qu'elle ne quitte l'écran.

Si vous regardez la documentation de Vue, j.

s. Maintenant, c'est la documentation de la version deux ici, car ils n'ont pas encore ce que je vais vous montrer dans les docs de la version trois.

Mais c'est la même chose.

Donc je suis sous learn guide.

Et puis si je fais défiler vers le bas sur la barre latérale, je suis à l'instance Vue et à la création d'une instance Vue.

Et je peux en fait cliquer sur le diagramme de cycle de vie ici.

Donc c'est un diagramme comme il est dit du cycle de vie de l'instance de votre instance Vue.

Et comme il est dit, vous n'avez pas besoin de tout comprendre ce qui se passe maintenant.

Mais c'est une référence utile.

Et ce graphique n'est pas seulement utile pour votre instance Vue.

Mais chaque composant Vue aura accès à ces hooks de cycle de vie.

Donc vous pouvez voir ces deux en haut en rouge.

Toutes les boîtes en rouge sont les hooks de cycle de vie, vous pouvez voir before create et created, ces hooks seront exécutés juste avant et juste après que Vue.

js ait initialisé votre composant.

Maintenant, les deux suivants, before mount et mounted, le format est exécuté juste avant que votre composant soit monté dans le DOM.

Et mounted est exécuté dès que votre composant est monté dans le DOM.

Les composants peuvent également subir des mises à jour.

Donc before update et updated, comme il est dit ici, cela se produira.

Ou ces mises à jour seront déclenchées lorsque les données changeront sur votre composant.

Donc toutes ces variables de données que vous créez, si vous incrémentez un nombre ou changez une valeur, alors updated et before update s'exécuteront.

Et lorsque votre composant va quitter le DOM.

Maintenant, il est dit before destroy et destroyed.

Maintenant, cette terminologie a été mise à jour pour Vue trois pour ces deux hooks de cycle de vie.

Donc si nous allons à la documentation Vue trois maintenant et que nous sommes sur les hooks de cycle de vie ici.

Je vais faire défiler vers le bas pour que vous puissiez voir before create created before mount mounted before update et updated.

Je vais sauter quelques-uns de ceux-ci et maintenant vous pouvez voir qu'il s'agit de before unmount et unmounted, qui est à la place de before destroy et destroyed.

Les fonctions des hooks de cycle de vie fonctionnent exactement de la même manière, elles ont simplement été renommées.

J'espère que cela deviendra un peu plus clair lorsque nous examinerons une démonstration.

Donc dans le code, vous pouvez voir que j'ai la même boîte que nous avons utilisée avant, elle apparaît.

Et voici le bouton toggle box à l'intérieur de mon template Vue.

Mais cette fois, j'ai un composant personnalisé test box spécial que j'ai fait, qui est basculé en fonction d'un V, if, donc c'est mon application principale.

Et l'objet d'options avec ma variable is visible pour savoir si la boîte est visible ou non.

Et puis j'ai juste une méthode toggle box, que j'appelle lorsque je clique sur ce bouton.

Donc encore une fois, c'est presque la même chose que ce que nous avons fait avant.

Sauf pour ce nouveau composant ici.

J'ai mis la boîte dans son propre composant.

Maintenant, maintenant que nous avons appris à composer des composants, et je vais simplement ajouter quelques hooks de cycle de vie ici très rapidement pour illustrer quand ceux-ci sont appelés sur le cycle de vie du composant.

Donc je vais simplement en ajouter quelques-uns ici.

Nous allons ajouter created, et puis mounted, et puis unmounted.

Et dans chacun de ceux-ci, je vais mettre un console dot log.

Et voyons quand ces console dot logs s'impriment.

De retour dans mon navigateur, je vais appuyer sur toggle box ici.

Et vous pouvez voir dans le terminal en bas, created, imprimé et puis mounted, imprimé dans le même ordre que nous avons vu dans la documentation VJs.

Donc celui-ci s'est produit avant.

Et puis celui-ci s'est produit après qu'il ait été monté à l'écran au DOM ici.

Maintenant, si je clique sur toggle box, nous pouvons voir unmounted qui s'imprime car cela est exécuté après que la boîte quitte le DOM.

Maintenant, regardons un autre.

Après les méthodes ici, je vais mettre un hook de cycle de vie sur ce composant, ou sur l'instance Vue principale que nous avons ici.

Et je vais essayer updated.

Et je vais cliquer sur toggle box.

Et vous pouvez voir que nous avons created et mounted qui s'impriment tous les deux depuis le composant de boîte lui-même, mais depuis l'instance principale aussi updated s'imprime.

Et c'est parce que nous mettons à jour cette variable de données de is visible false à is visible true.

Et donc la fonction de mise à jour est déclenchée sur ce composant parce que nos données ont été mises à jour pour ce composant.

Et si nous le basculons à nouveau, nous pouvons voir que updated est exécuté à nouveau, parce que cette variable a été changée à false à nouveau.

Donc updated s'exécutera chaque fois que les données changent.

Maintenant, pourquoi pourriez-vous vouloir utiliser un hook de cycle de vie, certains des cas d'utilisation les plus courants sont de vérifier si quelqu'un est autorisé à voir une certaine page ou un certain composant.

Beaucoup de gens utilisent les hooks created et mounted pour extraire des données dans leur application depuis un back-end ou depuis le stockage du navigateur.

Parfois, ils sont également utilisés pour initialiser des événements.

Et lorsque le composant est sur le point de se démonter, vous pouvez nettoyer cet événement.

Ou vous pouvez sauvegarder des données ou exécuter une sorte de vérification sur before unmount ou dans la fonction unmounted.

Ce sont les bases des hooks de cycle de vie, je vous encourage à tester les hooks de cycle de vie sur vos différents composants et à voir ce qui se passe lorsque vous utilisez différents hooks de cycle de vie.

Dans un cours futur, nous pourrons nous pencher sur des exemples plus avancés et quelques-uns des hooks de cycle de vie plus avancés que vous ne verrez pas aussi souvent.

Donc ce sont les bases de Vue js.

Dans la prochaine vidéo, nous allons construire une application Vue trois à partir de zéro, en commençant par le Vue COI cette fois-ci.

C'est une démonstration de l'application que nous allons construire.

C'est une application de boutique simple avec quelques articles.

Maintenant, cela ressemble à la page web déjà terminée.

Mais en fait, ce n'est que du HTML et du CSS statique pour l'instant.

Comme vous pouvez le voir, si je clique sur le bouton Ajouter au Panier, rien ne se passe.

Et si je fais défiler vers le haut, les seules choses qui sont réellement fonctionnelles sur ce site pour l'instant sont ces liens de navigation en haut.

Qui sont juste des liens d'ancrage de navigateur réguliers pour vous amener à une autre page.

Donc celui-ci va à la page Produits.

Et vous pouvez voir que j'ai ce panier, qui n'est pas fonctionnel.

Donc si je clique sur la X, rien ne se passe, il est juste complètement sorti ici pour démontrer comment il apparaîtra.

Et si je clique sur la X, rien ne se passe, il ne supprime pas l'article, je ne peux pas ajouter d'articles au panier.

Et sur cette page, j'ai un tableau des commandes passées, qui est également juste du contenu statique pour l'instant.

Ce projet va être un peu différent des tutoriels auxquels vous êtes habitués, nous ne allons pas commencer à partir de zéro avec quelques maquettes ici.

Au lieu de cela, nous allons commencer avec une application statique avec HTML et CSS déjà codés, puis nous allons déterminer étape par étape comment ajouter Vue JS dans l'application.

Cela aidera à vous donner une compréhension plus approfondie de comment Vue fonctionne et comment construire des applications Vue réelles.

Tout d'abord, je vais vous donner un aperçu de la base de code.

Et puis nous allons voir comment cela se présente dans le navigateur.

Et enfin, nous allons commencer avec la partie Vue JS et implémenter notre propre code Vue dans chaque fonctionnalité une par une, l'objectif est d'atteindre éventuellement un point où il devient difficile de continuer à coder à l'intérieur du HTML.

Et ensuite nous allons déplacer le projet vers un projet de configuration Vue COI où nous aurons Webpack et tout l'écosystème d'outils et de bibliothèques Vue j s comme Vue x et Vue router.

Donc commençons à regarder le code.

Donc je vais commencer ici avec le package dot JSON.

Maintenant, c'est le fichier qui est généré par NPM.

Vous devriez en avoir vu un avant si vous avez travaillé avec JavaScript, et il a quelques métadonnées sur notre projet ici, et puis la section des scripts.

Donc vous n'avez pas besoin de savoir ce que tous ces scripts font.

Ce code sera disponible pour vous.

Donc si vous voulez approfondir chacun d'eux, vous pouvez.

Mais puisque nous nous concentrons sur Vue ici, la partie importante est que nous avons ce start server qui compile nos styles et sert notre application pour nous.

Maintenant, plus tard, je vous montrerai comment démarrer une application avec le vcli.

Mais j'ai dû utiliser un serveur temporaire ici en attendant.

Donc c'est ce que live server fait pour nous, il le servira sur un port, similaire à ce que nous avons fait avec le plugin live server que nous avons utilisé dans VS code pour la dernière application de démonstration.

Donc pour démarrer cette application, je vais aller en haut de mon option terminal ici.

Et je vais choisir nouveau terminal.

Et mon terminal s'ouvre en bas ici à l'intérieur de mon dossier actuel.

Et je vais exécuter la commande start.

Donc NPM start, vous pouvez voir que cela ouvre automatiquement l'application sur le bon port ici.

Et si je fais défiler vers le bas, je peux voir la même page que vous avez déjà vue.

Maintenant, de retour dans le code, regardons dans le répertoire source.

Donc le répertoire source est là où tout notre JavaScript et autre code va vivre.

Et c'est aussi là que nous allons ajouter Vue js.

C'est notre fichier HTML principal pour l'application, qui est la page d'accueil.

Et vous pouvez voir les liens ici vont aux pages Vues à l'intérieur de ce répertoire Vues ici.

Donc les liens vous amèneront à la page des commandes passées et aussi à la page des Produits.

Maintenant, pour commencer à travailler avec Vue j s, je vais commencer avec ces cartes ici.

Pour l'instant, je veux pouvoir mettre à jour et sauvegarder les quantités et pouvoir les ajouter au panier.

Donc dans ce fichier app dot html, je vais ajouter mon lien vers Vue j s, comme je l'avais dans la dernière application de démonstration.

Donc je vais aller en bas ici et coller la balise de script.

Donc j'importe vj s.

Et maintenant, je dois écrire un code vj s personnalisé pour obtenir mon application.

Donc je vais créer une autre balise de script.

Et ici, je vais faire let app equal Vue dot create app up a passer un objet vide pour l'instant.

Et puis ici, je vais faire app dot mount et puis monter dans le même élément DOM qu'avant avec l'ID de app.

Et laissez-moi juste vérifier ici.

Oui, la div wrapper ici.

Si je la plie, vous pouvez voir que tout le contenu est créé à l'intérieur de app.

Donc pour commencer ici, je dois définitivement créer une méthode de données.

Et j'ai besoin de retourner un objet.

Et sur cet objet, je veux suivre mon inventaire.

Donc lorsque quelqu'un clique sur le bouton Ajouter au Panier, je veux incrémenter ou changer la quantité d'inventaire que j'ai.

Donc l'inventaire lui-même sera un objet.

Et vous pouvez voir les différents types de produits que j'ai ici.

Donc carottes, ananas et cerises.

Et donc je vais ajouter ces trois articles à mon inventaire, carottes, et je vais initialiser tous ceux-ci à zéro.

Cela a l'air bien.

Maintenant, je dois trouver ces éléments à l'intérieur de mon application et mettre les variables là.

Donc si je regarde ces cartes, vous pouvez voir ici la section des produits recommandés.

Donc j'ai des carottes ici.

Et j'ai le prix ici est la quantité avec le champ de saisie.

Et ce que je veux faire ici, au lieu de définir la valeur, je veux faire v model.

Et cela devrait être inventory, dot carrots.

Et puis je vais copier la même chose pour les autres champs.

Donc je descends ici aux ananas, et je colle cela.

Et puis les cerises aussi.

D'accord, maintenant laissez-moi jeter un coup d'œil à cela.

Et vous pouvez voir qu'il montre toujours zéro ici.

Juste comme avant, je peux mettre à jour un nombre, nous faisons trois carottes.

Et maintenant le nombre commence à trois.

Donc maintenant, nous voulons faire quelque chose lorsque quelqu'un clique sur ajouter au panier, s'il a une certaine quantité ici, nous voulons l'ajouter à un total de panier, nous changeons cela en zéro.

Donc pour cela, je dois créer une méthode, nous créons mon objet méthodes, je vais créer une méthode Add To Cart.

Et dans cette méthode, je dois prendre le nombre d'articles que quelqu'un veut ajouter à son panier, ainsi que le type d'article.

Donc pour cela, j'aurai besoin d'un autre endroit pour stocker les articles qui sont réellement dans le panier.

Donc je vais créer un panier ici.

Et pour l'instant, je vais simplement copier les mêmes articles.

Et puis lorsque j'appelle la méthode add to cart, je dois passer le type d'article et la quantité, puis je peux accéder à mes variables de panier en faisant this, ce panier et passer une variable que je veux accéder sur mon objet de panier, je dois utiliser les crochets, et puis je peux passer le type.

Donc ce serait la même chose que this cart carrots ou this card, pineapples, ou l'article que nous voulons accéder.

Et puis je vais incrémenter par la quantité.

Donc plus equals quantity.

Maintenant, je n'ai pas besoin de retourner quoi que ce soit de cette fonction.

Parce que c'est vraiment l'action que je veux prendre en appelant cette fonction est de mettre à jour ce que j'ai dans mon panier en ce moment.

Et pour montrer cela, je vais simplement le journaliser dans la console dans le navigateur, afin que vous puissiez le voir lorsque je journalise ce panier.

Et je vais ouvrir ma console ici.

Donc pour les carottes, je vais ajouter trois, vous pouvez voir que rien ne s'est passé.

C'est parce que j'ai oublié de connecter cette méthode à ce bouton.

Donc laissez-moi aller là-haut et ajouter ce bouton.

Donc je vais juste l'ajouter aux carottes pour l'instant, ici.

Donc lorsque quelqu'un clique sur le bouton Ajouter au Panier, je vais appeler la méthode add to cart.

Maintenant, je dois l'appeler en passant quelques arguments ici.

Donc le premier sera le type d'article que je veux ajouter au panier.

Donc celui-ci sera carottes, et je dois aussi passer la quantité.

Pour passer la quantité, je dois utiliser la variable inventory carats.

Donc je peux simplement la passer ici.

Je pourrais aussi simplement l'appeler depuis l'intérieur de ma fonction, ce que je vais en fait faire.

Donc laissez-moi faire défiler vers le bas pour voir ma fonction à nouveau.

Et au lieu de quantity ici, au lieu de passer cette variable supplémentaire, je vais simplement mettre à jour cela en this dot, this dot inventory, et puis obtenir le type de là.

Donc voyons si cela fonctionne.

Laissez-moi ajouter au panier.

Et vous pouvez voir qu'il y a définitivement un problème car la valeur d'entrée est une chaîne, et il essaie de l'ajouter aux nombres zéro, donc il transforme l'expression en une chaîne.

Maintenant, Vue a un moyen très facile de corriger cela.

Et cela se fait par un modificateur, comme nous l'avons appris un peu dans la dernière démonstration que nous avons faite.

Donc laissez-moi aller là-haut au V model.

Et nous ne voulons pas que ce V model soit considéré comme une chaîne, nous voulons aller de l'avant et le caster comme un nombre.

Donc Vue nous donne ce modificateur comme un raccourci.

Donc v model DOT number.

Donc maintenant, si nous regardons dans notre application, je peux ajouter au panier.

Et je peux voir en bas ici que mes carottes ont un article dedans, qui est un nombre, donc je peux ajouter au panier à nouveau.

Et maintenant il y en a deux, et je peux en ajouter plusieurs.

Et maintenant il y a huit carottes dans le panier.

Arrêtons-nous ici pour cette vidéo.

Et n'oubliez pas de télécharger le code lié et d'essayer ces fonctionnalités par vous-même.

Dans la prochaine vidéo, nous travaillerons sur l'affichage des articles dans le panier.

Donc maintenant, nous voulons connecter ce menu de panier ou ce tiroir de panier coulissant.

Et pour l'instant, ce n'est que du contenu statique.

Donc nous ne pouvons le voir que depuis la page Produits.

Et si vous regardez le code, nous allons à products dot html, je vais plier cet en-tête, et aussi le conteneur principal, qui est cette partie principale de la page ici.

Et maintenant je peux juste voir cet aside, qui est cette section de panier sur le côté.

Donc je veux essentiellement prendre tout ce HTML et le rendre disponible sur mes autres pages comme ma page d'application, qui est la page d'accueil, afin que je puisse utiliser Vue j s pour déclencher l'ouverture ou la fermeture du menu.

Et je veux aussi rendre ces articles de panier dynamiques.

Donc lorsque j'ajoute plus d'articles au panier, il peut mettre à jour la quantité et le prix.

Et je peux aussi définir une variable.

Donc s'il n'y a pas d'articles dans le panier, cela s'affichera.

Maintenant, HTML lui-même n'a pas quelque chose comme une importation pour importer un bloc de HTML dans un autre fichier HTML.

Beaucoup de gens utilisent PHP ou un autre outil backend pour cela.

Mais nous pouvons aussi facilement le faire en JavaScript.

Donc nous allons le faire en Vue, j.

s, en fait.

Donc je vais supprimer cette barre latérale de la page sur laquelle elle se trouve actuellement.

Et la déplacer dans notre application Vue.

Bien sûr, notre application Vue est imbriquée à l'intérieur de la page app dot html.

Mais nous pouvons la déplacer à l'extérieur plus tard.

Donc que ce menu sera accessible sur toutes les pages à l'avenir.

Donc je vais plier cette Vue create app.

Et maintenant je vais coller cet aside HTML que j'ai.

Maintenant, il me donne une erreur ou quelques erreurs parce qu'il est à l'intérieur d'une balise de script.

Mais je vais corriger cela.

Si vous vous souvenez, dans les leçons précédentes, nous avons défini les différents composants à l'intérieur de notre application Vue.

Donc c'est un cas d'utilisation parfait pour un composant en ce moment, car c'est ce bloc de HTML réutilisable ou ce template que nous voulons utiliser sur plusieurs pages différentes et aussi interagir avec.

Donc je vais l'enregistrer comme un composant.

Et je vais simplement l'appeler sidebar.

Et maintenant je passe dans l'objet comme avant, et sur cet objet d'options, je peux définir le template et puis utiliser des graves.

Et maintenant je veux attraper cet aside à nouveau.

Et le coller à l'intérieur de celui-ci.

Et donc maintenant j'ai tout cet aside, tout le code à l'intérieur de mon template pour ce composant.

Et maintenant je peux l'ajouter à la page avec le nom sidebar.

Donc je vais aller de l'avant et l'ajouter ici.

Et rappelez-vous que notre div enveloppe toute l'application Vue.

Donc je peux le mettre n'importe où à l'intérieur de cette div avec l'ID de app.

Je vais le mettre ici, en fait entre le main et le footer, je vais mettre le composant personnalisé, sidebar, et Vue va gérer la mise du template que j'ai ici où cet élément sidebar est dans le template.

Donc laissez-moi revenir au HTML ici, vous pouvez voir que la sidebar n'est plus sur la page des Produits.

Mais si je vais à la page d'accueil, maintenant j'ai une sidebar ici.

Donc maintenant que la sidebar est en Vue js, je peux commencer à la rendre interactive.

Et la première chose que je veux faire est de pouvoir cacher et montrer la sidebar.

Donc, essentiellement, lorsque cela est cliqué, je veux la cacher.

Et puis lorsqu'un autre bouton est cliqué, je veux la montrer.

Donc j'ai besoin de créer une variable pour cela.

Et laissez-moi descendre à mon JavaScript ici.

Donc à l'intérieur de mon create app régulier ici, dans mon objet d'options principal, je vais ajouter un élément à data ici.

Et je vais l'appeler show sidebar, false.

Et maintenant je peux venir à ma sidebar, et simplement utiliser un vi F, et le pointer vers la variable show sidebar.

Donc si show sidebar est vrai, alors mon composant personnalisé apparaîtra sur la page.

Si c'est faux, alors je ne devrais pas voir la sidebar du tout.

Et vous pouvez voir qu'il est faux, je ne vois aucune sidebar.

Et lorsque je change cela en vrai, je vois la sidebar.

Maintenant, je dois simplement ajouter un basculement pour cette sidebar et la remettre à false par défaut.

Et maintenant je peux créer une méthode appelée toggle sidebar.

Et je vais dire this dot show sidebar est égal à l'opposé de ce qu'il est car il basculera entre vrai ou faux à chaque fois que cette fonction est exécutée.

Donc je vais dire qu'il est égal à not this dot show sidebar.

Donc s'il est actuellement faux, cela signifie qu'il sera défini égal à vrai et s'il est vrai, il sera alors défini égal à faux.

Maintenant, je dois simplement appeler cette méthode.

Donc le premier endroit où je vais la mettre est sur ce bouton ici, ce bouton de panier devrait ouvrir ce panier de sidebar.

Je vais trouver cela sur la page.

Voici ce bouton de panier.

Et je vais simplement ajouter un clic ici.

Add click equals toggle sidebar, je n'ai pas besoin de passer quoi que ce soit donc je peux simplement le laisser comme cela.

Et Vue cherchera automatiquement dans mes méthodes et trouvera cette méthode.

Donc laissez-moi voir si cela fonctionne.

Revenez à la page, vous devriez pouvoir cliquer sur cela maintenant.

Et oui, cela bascule.

Maintenant, la prochaine chose que je dois pouvoir faire est de le fermer et je dois le fermer en utilisant cette x ici.

Donc je vais devoir descendre à mon template ici.

Et voici le bouton.

C'est cette x qui est dans le coin de l'en-tête de la sidebar.

Donc je dois ajouter un clic sur celui-ci.

Et je vais devoir faire un clic.

Et maintenant je veux utiliser la fonction toggle sidebar.

Mais parce que cela est enveloppé dans son propre composant, je n'ai en fait pas accès à la fonction toggle sidebar depuis ici, je dois en fait la passer dans ce composant pour pouvoir y accéder.

Et je peux faire cela ici.

Donc je vais la passer en tant que toggle equals toggle sidebar, j'utilise ma méthode sur l'objet vj s appelée toggle sidebar en la passant dans le composant sidebar avec le nom toggle.

Donc à l'intérieur de mon composant ici, il sera appelé toggle.

Donc je vais devoir l'accepter en tant que prop et l'accepter en tant que toggle.

Et ce sera le nom de ma fonction.

Donc maintenant je dois renommer cette fonction et l'appeler toggle.

Laissez-moi voir si cela fonctionne.

Aller au panier, cliquer sur x et cela ne fonctionne pas.

Donc j'ai une erreur ici, la taille maximale de la pile de calls dépassée.

Donc laissez-moi voir ce que je fais de mal dans le code.

Donc j'importe la prop toggle, la fonction devrait être appelée à partir d'ici de toggle sidebar qui pointe vers toggle sidebar ici.

Et, oh, j'ai oublié de faire pointer cela vers une variable Vue.

Au lieu de cela, il essayait simplement de l'utiliser comme une chaîne avant, ce qui causait une erreur.

Donc maintenant, cela devrait appeler la fonction toggle sidebar réelle.

Et laissez-moi voir cela dans le code.

D'accord, cela fonctionne comme prévu maintenant.

Donc maintenant sur la sidebar, je veux afficher des articles dynamiques ici.

Pour l'instant, je n'ai qu'un seul article connecté, les carottes.

Et donc je ne vais travailler qu'avec cet article jusqu'à la prochaine vidéo.

Donc connectons cet article.

Lorsque j'ajoute des articles au panier ici, il devrait se mettre à jour dans le panier ici.

Maintenant, pour cela, je dois prendre cet objet panier et le passer dans ma sidebar, afin que ma sidebar y ait accès.

Tout d'abord, laissez-moi faire un peu de nettoyage ici.

Avec cela sur plusieurs lignes pour le rendre un peu plus propre.

Et je vais passer cart comme cart.

Et maintenant, je dois recevoir cette prop dans mon composant ici.

Donc je vais le faire ici et l'appeler cart.

Et maintenant, cart que je reçois dans mon composant est en fait cet objet cart.

Donc puisque je ne travaille qu'avec les carottes pour l'instant, je vais simplement supposer cela et ajouter uniquement le nombre ici pour les carottes.

Donc je vais utiliser ma syntaxe de double moustache.

Et j'ai cette variable cart.

Donc je vais faire cart dot carrots, et ce sera le nombre de carottes que j'ai.

Donc laissez-moi revenir ici et la mise à jour automatique.

Laissez-moi ajouter trois.

Et mon panier contient maintenant une quantité de trois.

Donc si j'ajoute, disons cinq de plus maintenant, cette quantité est de huit dans mon panier.

Donc maintenant mon panier est dynamique.

Bien sûr, le total devrait également être mis à jour en fonction de la quantité, devrait être le prix fois la quantité égale au total pour cet article.

Donc laissez-moi faire cela très rapidement.

C'est le nombre total.

Donc je vais simplement devoir faire cela.

Et disons cart dot carats fois le prix qui est de 1 $.

Mais ici, il est indiqué 482.

Donc je vais utiliser ce prix car 1 $ n'est pas très intéressant.

Donc je vais faire fois 482.

Et puis avant cela, je dois mettre des dollars.

Et voyons si cela fonctionne.

Pour ajouter au panier.

Maintenant, il y a une erreur, voyons quelle est l'erreur, jeton inattendu avec un point.

La raison pour laquelle il se plaint est parce que le signe $1 suivi d'accolades.

En JavaScript, chaque fois que vous mettez cette syntaxe à l'intérieur des backticks que nous avons autour de ce template ici.

C'est appelé une chaîne de template.

Et elle analysera tout ce qui se trouve à l'intérieur de ces accolades extérieures comme du JavaScript.

Donc elle pense que nous essayons de passer un objet JavaScript.

Et elle se plaint parce que cart carrots n'est pas une clé valide.

Donc la seule chose que nous devons faire ici est en fait d'échapper le signe dollar.

Donc JavaScript ne pense pas que vous essayez d'utiliser une chaîne de template et de passer une variable.

Et puis Vue peut simplement analyser la syntaxe des doubles accolades par elle-même.

Cela devrait fonctionner.

Donc laissez-moi aller au panier maintenant, mon panier s'ouvre normalement.

Vous pouvez voir qu'il y a zéro carottes.

Et maintenant si j'ajoute deux carottes au panier, et maintenant cela me donne le total correct de 964.

Maintenant, je veux aussi avoir un total de tous les articles dans le panier.

Je n'ai qu'un seul article maintenant, mais j'aurai plus d'articles bientôt.

Donc je vais ajouter une fonction pour cela.

Et puis nous connecterons le reste des articles dans la prochaine vidéo.

Donc dans le code ici, c'est le total que je veux mettre à jour.

Donc je vais ajouter cela et échapper à ce signe dollar qui vient avec les doubles accolades, maintenant je pourrais créer une formule juste en ligne ici et dire carrot cart carrots, fois le prix des carottes, plus le deuxième article fois ce prix, et ainsi de suite.

Mais cela n'a pas beaucoup de sens.

Et cela ne s'adapte pas à plusieurs articles.

Donc ce que je vais faire ici, c'est en fait ajouter un objet calculé.

Et si vous vous souvenez, computed surveille les changements dans les variables, et mettra à jour le résultat.

Donc je vais appeler cette fonction calculée cart total.

Et sur mon cart, il y a le nombre de chaque article.

Donc pour l'instant, je vais simplement coder en dur le prix ici.

Donc je vais retourner cart dot carats fois le prix, qui est 482.

Et maintenant je peux prendre cette variable calculée que j'ai créée, et la mettre ici.

Et maintenant le total du panier, ce montant devrait être mis à jour à chaque fois.

Voyons si cela fonctionne.

Ajouter au panier, ouvrir mon panier.

Et il y a un bug car il ne s'ouvre pas et passe en revue en essayant de comprendre pourquoi le total du panier ne fonctionne pas.

Et c'est parce que je l'ai accédé incorrectement.

Donc cart dot carrots doit être accédé, cela est à l'intérieur de JavaScript, donc je dois l'accéder sur le contexte this dans mon composant.

Donc je dois l'accéder sur this card carrots, et cela devrait donner mon nombre fois ce nombre.

Donc laissez-moi revenir à ma page.

Et maintenant il s'ouvre.

Et si j'ajoute des articles, je peux voir qu'il est à 24,10 $.

Bien sûr, ce n'est pas très joli.

Parfois, il l'arrondit à un, ou parfois il n'y a qu'une décimale, et parfois il y en a comme 10 ici.

Donc faisons cela très rapidement en utilisant quelque chose de intégré en JavaScript.

Donc nous avons juste deux décimales.

Je vais envelopper cela ici, que deux fixes.

Et puis le nombre deux.

Et revenons au navigateur, je vais ouvrir le panier, ajouter quelques articles.

Et maintenant il est à deux décimales exactement.

Toujours deux.

D'accord, je vais le laisser là dans cette vidéo.

Encore une fois, veuillez essayer d'implémenter ces fonctionnalités par vous-même à partir du code d'exemple, vous devriez pouvoir consulter la branche de départ appelée homepage, one depuis le dépôt et commencer exactement là où je l'ai fait au début de cette vidéo.

Dans la prochaine vidéo, nous couvrirons l'ajout de tous les autres articles au panier en les important dans notre JavaScript.

Donc nous pouvons utiliser des boucles pour rendre notre code plus efficace et ne pas avoir à tout coder en dur.

Dans cette vidéo, nous allons extraire du contenu dynamique pour remplir notre page.

Et cela proviendra de ce fichier food dot JSON.

Donc cela contient en fait une liste d'objets de toutes sortes de produits d'épicerie que nous allons afficher dans notre application.

Il contient certaines informations, comme les noms ainsi que le prix.

Et même si nous voulons ajouter un filtre pour trier par type.

Donc comment pouvons-nous extraire cela dans notre application.

En fait, nous allons utiliser des hooks de cycle de vie dans Vue j s pour cela.

Si nous venons à notre application Vue principale ici, en dessous des méthodes, je vais ajouter le hook mounted comme nous l'avons fait avant.

Et à l'intérieur de celui-ci, je vais extraire ces données JSON.

Et ce sera un appel asynchrone.

Donc je dois d'abord extraire cela depuis le nom de fichier, qui est food dot JSON.

Et je vais appeler cela la réponse.

Et puis je dois appeler la méthode JSON sur cette réponse.

Que je mets sur cette ligne, et cela sera des données.

Et en fait, je dois ajouter un poids à ces appels.

Donc res dot JSON, je peux appeler cette méthode.

Je vais attendre cela aussi.

Et puis parce que j'utilise un poids, je dois ajouter async à cette méthode mounted.

Donc maintenant j'ai créé le hook de cycle de vie mounted, j'obtiens mes données, qui est le tableau de tous les objets alimentaires.

Et maintenant que j'ai mes données, je vais les définir sur l'état ici.

Donc au lieu de l'inventaire ici, je vais remplacer l'inventaire, me débarrasser de toutes ces données factices que j'ai maintenant.

Le définir comme un tableau vide.

Cela va définitivement casser mon application maintenant.

Mais c'est bon car c'est une étape vers la correction.

Donc maintenant je vais définir cet état d'inventaire égal aux données.

Voyons si cela fonctionne.

Et je peux voir ma racine.

Et je peux voir que l'inventaire dans mon élément racine ici que j'ai tous les 15 articles.

Bien.

Donc je sais que mes données fonctionnent.

Maintenant, les deux prochaines choses que je dois faire sont afficher ces données sur cette page ici.

Et donc ce ne sont que trois articles recommandés, en fait, tous les produits s'afficheront sur cette page.

Donc pour la page d'accueil, je vais simplement afficher les trois premiers et découper cette liste lorsque je boucle dessus.

Donc maintenant que j'ai l'inventaire, je vais en fait venir ici à mon conteneur principal.

Et je vais venir à la section recommandée et plier toutes ces cartes et me débarrasser des deux dernières, car je n'aurai besoin que d'une seule pour ma boucle.

Et maintenant avec cette carte initiale, je vais la transformer en une boucle V for et boucler sur chaque article de ce tableau d'inventaire.

Donc equals product in inventory.

Laissez-moi juste voir à quoi cela ressemble très rapidement.

Et oui, il essaie de boucler à travers chaque article dans tout l'inventaire.

Donc je vais le découper à trois articles maintenant.

Et je peux faire cela car à l'intérieur de ma directive Vue, je peux mettre du JavaScript valide.

Donc nous allons faire dot slice de 0 à 3.

Et maintenant nous allons revenir à ma page.

Et vous pouvez voir que je n'ai que trois articles.

Maintenant, bien sûr, il n'affiche que carotte, car c'est tout ce qui est encore codé en dur.

Donc laissez-moi mettre un peu de contenu dynamique ici.

Et d'abord avec le nom, je vais mettre product dot name.

Et puis je crois que c'est product dot type.

Oui.

Donc ici, je vais mettre product dot type.

Et pour le prix, maintenant j'ai des prix en deux devises différentes, je vais utiliser des dollars américains pour l'instant.

Donc je dois accéder à price dot USD.

Et donc ici, je vais y aller et échapper cela.

Et puis faire product dot price, dot u, s, d.

Et en fait, ceci est juste un template HTML.

Ce n'est pas à l'intérieur d'une chaîne de template JavaScript, donc je n'ai pas besoin d'échapper cela du tout.

Et cela devrait être tout le contenu dynamique dont nous avons besoin pour l'instant.

Allons-y et mettons à jour l'icône également.

Donc ce serait product dot icon.

Assurez-vous que c'est le bon.

Un.

Oui, cette icône.

D'accord, donc laissez-moi aller à la page.

D'accord, donc l'icône ne fonctionne pas, mais toutes les autres données s'affichent assez bien.

Donc maintenant nous voulons ajouter une fonctionnalité pour que la quantité se mette à jour correctement et que nous puissions l'ajouter au panier.

Bien sûr, en ce moment, tous ces éléments ont le même v model.

Donc c'est pourquoi ils se marient les uns les autres.

Donc changeons cela.

Maintenant, je vais aller au V model ici qui est inventory carrots, mais j'ai besoin de l'inventaire de l'article correct au lieu de simplement coder en dur carrots ici.

Donc parce que ces nombres sont dans l'ordre ou parce que c'est une liste ordonnée, je vais venir à ma boucle et obtenir l'index.

Bien sûr, je pourrais utiliser l'ID aussi.

Mais je vais juste utiliser l'index dans la boucle ici.

Et en fait, j'ai presque oublié, je dois aussi ajouter une clé ici puisque je suis en train de boucler.

Donc laissez-moi ajouter cette clé.

Et je vais descendre ici, et inventory, je vais passer cet index.

Et puis je vais ajouter un nouvel attribut appelé quantity.

Et donc cela devrait modéliser un attribut appelé quantity, qui n'est pas actuellement sur les objets, mais ce n'est pas grave, je vais simplement le laisser.

Et cela devrait simplement ajouter la clé quantity à l'objet au besoin.

Donc voyons si cela fonctionne.

Laissez-moi revenir ici.

Je vais en ajouter un ici, vous pouvez voir qu'ils ne sont plus tous en miroir les uns des autres, je vais l'ajouter au panier.

Et laissez-moi voir comment cela se représente dans mes données Vue ici, je peux venir à inventory.

Et je peux voir une quantité de un.

Quel que soit le nombre que j'ai mis, ce nombre le reflète.

Mais maintenant j'ai besoin d'un moyen de l'ajouter au panier.

Donc laissez-moi définir le panier.

Et ici à cette fonction add to cart, je dois la changer car je dois passer au lieu d'une chaîne, le nom dynamique de l'article.

Donc je peux faire product dot name.

Et en fait ici, je n'y ai pas pensé, mais au lieu de inventory et d'obtenir l'inventaire à l'index, i, je l'ai déjà vraiment dans cette boucle.

C'est ce que la variable product est.

Donc je vais simplement la remplacer.

Et cela devrait fonctionner très bien.

Maintenant, bien sûr, je n'ai plus vraiment besoin de cet index, car pour la clé, je peux utiliser l'ID du produit.

Donc laissez-moi simplement utiliser cet ID de produit et cela devrait fonctionner correctement.

Et cela devrait également refléter l'objet, laissez-moi voir si cela le fait.

Oui, et la quantité est reflétée.

D'accord, maintenant pour le panier, en passant le nom du produit comme Add To Cart.

Jetons un coup d'œil à la fonction add to cart.

Nous passons le type ici.

Et puis en disant this duck card duck type.

Donc ce serait comme this cart dot radishes plus equals le montant que this that inventory.

Donc nous devons faire une chose de plus ici, nous pourrions soit rechercher et trouver l'article par nom dans l'inventaire, soit la chose la plus facile à faire serait de passer l'index de cet article.

Donc c'est ce que nous allons faire.

Et pendant que je change cela, au lieu de type maintenant, je pense qu'il est plus logique de l'appeler name car c'est le nom de l'article.

Et nous utilisons type pour le type d'article comme légume ou fruit, pas le nom.

Donc maintenant pour y accéder dans l'inventaire, je veux faire index et puis dot quantity.

Et cela devrait fonctionner.

Mais nous devons en fait passer l'index ici.

Et ici, nous allons en fait passer l'index.

Donc nous allons prendre l'index ici.

Et maintenant add to cart.

D'accord, donc nous obtenons pas un nombre pour ces valeurs.

Donc je veux en fait voir ce que nous passons ou ce qui est passé dans la fonction.

Et donc pour déboguer la fonction rapidement, je vais simplement faire console dot log et name et index.

Maintenant, de retour dans le code.

Donc les arguments sont passés dans la fonction très bien.

Donc en revenant à travers cela, je peux voir que mon problème ici est que je fais un plus equals sur cart ou this cart name lorsqu'il n'y a pas de valeur pour ce name dans le cart.

Et en passant, je vais me débarrasser de mes données factices.

Dans le cart, et ici, je vais simplement mettre une vérification simple.

Donc si not this dot cart name, alors je vais définir this cart name et égal à zéro.

Et maintenant cette instruction devrait fonctionner.

D'accord, laissez-moi essayer à nouveau.

Donc ici, je vais faire deux.

Et cela devrait se mettre à jour.

Voyons voir.

D'accord, oui.

Donc cela prend un peu de temps, pour une raison quelconque, acheter, cela montre le nombre correct de chacun dans le panier, plus de pas un nombre.

Maintenant, cela montre dans le panier ici, je veux le montrer dans la barre latérale.

Pour l'instant, dans la barre latérale, il est connecté pour ne chercher que les carottes.

Donc rendons la barre latérale dynamique maintenant.

Si vous vous souvenez, la barre latérale ici est dans ce template.

Donc elle fait partie du composant personnalisé de la barre latérale que nous avons créé.

Et nous passons déjà le panier ici.

Maintenant, nous avons en fait besoin de plus d'informations car le panier ne nous montre que le nombre d'articles dans le panier.

Mais nous voulons aussi plus d'informations sur ces articles, comme le prix.

Donc je vais venir ici à ma barre latérale, et après le panier, je vais passer l'inventaire ainsi que l'inventaire.

Et maintenant je peux le recevoir comme une prop dans mon composant.

Donc, essentiellement, nous devons parcourir tous les articles du panier et afficher leurs informations maintenant.

Et nous avons un tableau ici.

Donc nous avons tous les en-têtes du tableau.

Et puis nous pouvons parcourir ces lignes et essentiellement faire autant de lignes que nous voulons.

Donc je vais ajouter un v4 ici pour parcourir chaque article du panier.

Et ici, j'ai effectivement besoin de l'index, je vais l'utiliser comme clé ici.

D'accord, et maintenant ceux-ci sont parcourus dans la barre latérale.

Donc si je viens à la barre latérale, je ne devrais voir aucun article pour l'instant, bien sûr, le total doit être corrigé.

Et maintenant je peux voir que j'ai cet article.

Et maintenant j'en ai un autre.

Donc maintenant je dois me débarrasser de ces noms codés en dur.

Maintenant, pour cela, je vais prendre la clé de ces articles dans le panier.

Et en fait, parce que le panier est un objet, cet index sera en fait une clé.

Et le troisième est l'index, ou juste I.

Donc maintenant j'ai accès au nom de l'article, qui est la clé, à la quantité de l'article, que je vais changer en nom, quantité.

Et ici, je peux changer cela en cette clé et nous devrions voir les noms de tous les articles dans notre panier.

Testons cela.

Laissez-moi ajouter différents articles au panier, je devrais voir des radis et des artichauts.

Et dans le panier, nous voyons effectivement des radis et des artichauts.

Maintenant, affichons la quantité.

Donc ici, nous pouvons nous débarrasser de cela et dire simplement quantité, que nous extrayons de l'objet dans le panier.

Bien sûr, nous savons déjà que cela devrait fonctionner lorsque nous ajoutons un article ici.

Et la quantité fonctionne.

Maintenant, le prix est un peu plus compliqué.

Parce que nous n'avons pas le prix stocké sur le panier, nous devons en fait rechercher le prix dans l'inventaire.

Donc nous allons faire une méthode d'assistance pour cela.

Tout d'abord, laissez-moi échapper cela.

Et puis nous allons appeler get price Asin le nom de l'article qui est la clé et nous trouverons le prix et le retournerons en fonction du nom.

Donc après computed ici, je vais ajouter des méthodes pour cet objet de méthodes régulier et ajouter ce get price.

Et essentiellement, nous pouvons accéder à this dot inventory et faire un dot find.

Donc nous voulons trouver l'un des articles de l'inventaire.

Donc je vais appeler chaque article produit dans la fonction que je passe, et find va parcourir tous les produits de l'inventaire et essayer de trouver l'article que je veux.

Donc je veux l'article où le nom du produit est égal au nom que je passe dans la fonction.

Et lorsque je trouve ce produit, je vais le définir égal à une variable ici.

Un peu déroutant, si je l'appelle produit à nouveau, donc peut-être que je vais juste l'appeler celui-ci p à la place.

Nous y voilà.

Et maintenant pour la fonction de retour, maintenant que j'ai le produit enregistré dans cette variable, je peux faire produit.

Et il devrait être dot price dot USD à nouveau.

Donc dot price that USD.

Et cela devrait retourner le prix de l'article.

Et voyons si cela fonctionne.

Donc laissez-moi en prendre un ici et Vue le panier.

Et je peux effectivement voir le prix.

Laissez-moi essayer cela pour les artichauts aussi.

Et je peux voir le prix et les quantités de l'article correctement.

Maintenant, laissez-moi mettre à jour la fonction pour le total.

Et donc le total ici doit être dynamique, basé sur tout le panier.

Donc pour cela, je vais en fait utiliser une méthode d'assistance.

Donc ce que je vais faire, c'est sortir cela de computed, et au lieu de cela, utiliser cela comme une méthode.

Donc puisque ce n'est pas computed comme une méthode, je vais l'appeler un verbe.

Donc calculate total.

Et je vais renommer l'appel de méthode ici, bien sûr, je vais en fait l'appeler comme une fonction maintenant.

Et je n'aurai plus besoin de cette ligne de code.

Donc maintenant, nous devons essentiellement calculer le total en fonction de la quantité dans le panier.

Et puis nous devons chercher le prix dans l'inventaire.

Heureusement, nous avons déjà une méthode pour pouvoir chercher le prix.

Donc nous allons simplement utiliser cela.

Et le moyen le plus simple de faire cela est en fait de faire object dot values.

Et donc object dot values peut me donner un tableau facile de valeurs à partir d'un objet.

Et parce que le panier est un objet, je ne vais pas le parcourir directement, je vais simplement prendre toutes les valeurs.

Donc je vais passer cart.

Et maintenant j'ai un tableau de toutes les valeurs ici, qui sont les quantités que je veux.

Donc à partir de ce tableau, je vais le réduire.

Maintenant, la fonction réduite est juste une fonction JavaScript intégrée, où je sauvegarde un accumulateur.

Certaines personnes aiment l'appeler un total, parce que c'est ce qu'ils utilisent sur MDN.

Et essentiellement, je calcule une somme à chaque itération de la boucle.

J'ai aussi mon article actuel qui est en cours de boucle.

Et puis je peux aussi obtenir l'index de cet article dans la fonction.

Et essentiellement, ce que je veux faire, c'est retourner l'accumulateur, la somme totale, peu importe comment vous voulez l'appeler, plus l'article actuel ou la valeur actuelle, parce que je parcours toutes les valeurs du panier ici.

Et j'ai besoin de la valeur fois le prix.

Donc je vais devoir appeler this dot get price.

Et puis je dois passer le nom de l'article pour lequel je veux obtenir le prix.

Donc le moyen le plus simple de faire cela est de faire aussi un tableau de noms.

Donc je vais faire cela en utilisant cette fois-ci object keys.

Et je vais faire this cart, obtenir toutes les clés cette fois-ci de cart.

Et en fait, j'ai oublié de mettre cela ici.

Et donc je vais faire la valeur actuelle fois this dot get price.

Et maintenant que j'ai les noms ici, je vais simplement chercher par l'index.

Donc je peux passer un noms index à cette fonction this dot get price, et cela devrait fonctionner.

Pour la fonction.

J'ai oublié de mettre une flèche ici.

Et maintenant pour la variable total.

Je l'ai simplement stockée dans une variable pour la nommer explicitement.

Tout ce que je dois faire maintenant est de retourner le total maintenant, cette fois la fonction fonctionne, il pourrait y avoir un moyen plus optimisé de faire cela.

C'est juste pour démontrer comment calculer un total en utilisant une méthode VJs pour cette application.

Et c'est essentiellement juste en utilisant du JavaScript régulier.

Donc laissez-moi ajouter des articles au panier ici.

Et bien sûr, bien sûr, ce total, nous ne l'avons pas encore fait.

Mais nous avons deux radis, et le total dit 2 $.

Donc laissez-moi ajouter quelques artichauts.

Et maintenant nous avons un total de 30,32 $.

Comme vous pouvez le voir, ce sont les valeurs correctes, ce que je crois qui se passe, c'est parce que les objets sont non ordonnés, et les tableaux sont ordonnés, que les noms et les valeurs de l'objet, ils ne sont pas listés dans le tableau dans le même ordre.

Donc je vais devoir au lieu de faire deux tableaux séparés ici, je vais me débarrasser de celui-ci.

Et ici, je vais devoir changer cela en entrées.

Et maintenant ma valeur actuelle ici sera essentiellement dans un tableau, qui sera la clé et la valeur, chaque fois en parcourant ce tableau plus grand.

Donc pour la valeur, maintenant, je vais devoir y accéder à la première index.

Et au lieu des noms ici, je peux accéder au nom à l'article actuel à la zéroième index, tout cela a l'air bien.

La dernière chose que je vais faire est ajouter une valeur initiale ici.

Et cela signifie que l'accumulateur commencera à zéro.

Et aussi, s'il n'y a pas d'articles dans ce tableau, ce qui n'est pas le cas au début, cela signifie que le nombre sera simplement zéro total.

Et pour ici pour le total, en fait, je vais utiliser cette méthode à nouveau, que nous avons utilisée avant, qui était too fixed.

Donc je pourrais le faire à deux décimales, ce que je veux dans mon panier.

Laissez-moi voir si cela fonctionne.

Et c'est exactement ce que je veux ici.

Donc laissez-moi ajouter des articles.

Oui.

Et le prix est exactement correct.

Un artichaut, et le prix fonctionne toujours là.

Maintenant, qu'en est-il du total ici, cela devrait être assez facile à faire avec notre méthode get price.

Donc descendons au total.

Pour l'instant, il est codé en dur comme carottes, ce qui n'existe pas.

Donc maintenant je peux simplement faire la quantité, qui est la quantité de l'article dans le panier.

Et puis j'appellerai la méthode get price.

Et je vais passer la clé, qui est le nom de l'article.

Et donc cela devrait multiplier par le total.

Voyons si cela fonctionne.

Ajouter un article et vérifier le panier.

Et nous voyons effectivement le total ici.

Maintenant, il indique toujours aucun article dans le panier, allons-y et corrigeons cela.

Cela ne devrait s'afficher que s'il n'y a en fait aucun article.

Donc je vais ajouter un V if ici.

Et juste pour accélérer cela, nous allons faire object that keys et puis vérifier l'objet cart.

Donc s'il n'y a pas de clés sur l'objet cart, cela sera zéro, ce qui est une valeur fausse.

Et voyons si cela fonctionne.

Allons en bas ici aux radis, ajoutons-en un dans le panier, nous voyons toujours ce message aucun article dans le panier.

Donc je crois que je dois faire length ici.

Voyons si cela fonctionne.

D'accord, cela fonctionne, mais je l'ai à l'envers.

Donc je dois en fait faire si ce n'est pas, parce que si la longueur est zéro, je veux montrer cela.

Et si ce n'est pas zéro, alors je ne veux pas montrer ce message aucun article dans le panier car il y aura des articles dans le panier.

Donc voyons si cela fonctionne.

D'abord, allons ici, cela montre aucun article dans le panier.

Et maintenant, laissez-moi aller ici.

Et maintenant cela change pour l'article dans le panier.

Et tous les totaux sont affichés correctement et les quantités sont mises à jour et tout cela.

La seule autre chose que je veux faire est de fournir des opérations CRUD complètes, et cette suppression ne fonctionne pas.

Donc je vais connecter la suppression maintenant.

Donc vous pouvez voir que la suppression est ici sur ce bouton pour supprimer.

Et donc je vais ajouter une fonction ici et en fait cette fonction devra ne pas être à l'intérieur de ce composant.

Mais à l'intérieur du composant parent, qui est mon application Vue principale dans ce cas, donc je vais faire un clic.

Donc lorsque ce bouton est cliqué, je vais dire remove item pour supprimer l'article du panier, et puis je dois passer le nom de l'article, qui est la clé.

Maintenant, cette fonction remove item devra être une fonction passée en tant que prop ici.

Parce que je ne peux pas muter les props, je ne pourrais pas changer l'inventaire, ou le panier en fait directement depuis ce composant, je dois le changer depuis le composant parent d'où il provient.

Donc je vais prendre une fonction remove item, laissez-moi aller de l'avant et passer cela.

Remove item equals remove item.

Et maintenant je dois créer cette fonction ici comme l'une de ces méthodes.

Donc laissez-moi ajouter cette fonction remove item, cela prendra le nom de l'article.

Et je vais le supprimer du panier.

Donc je peux simplement supprimer JavaScript, delete this cart name.

Voyons si cela fonctionne.

Laissez-moi ajouter quelques légumes à mon panier.

Et maintenant je vais les supprimer.

Et cela ne les supprime pas, voyons si j'ai une erreur.

Remove item n'est pas une fonction.

Donc voyons pourquoi ce n'est pas considéré comme une fonction.

Je l'ai dans les méthodes ici, remove item.

Allons ici.

C'est remove item que je passe dans ma sidebar.

Je l'accepte également comme une prop dans la sidebar ici.

Laissez-moi me débarrasser de computed.

Donc il ne reconnaît pas cela comme une fonction.

Donc ce que je vais faire est de le renommer dans le composant enfant.

Maintenant, c'est un contournement uniquement pour le CDN, vous n'auriez pas ce problème si vous utilisiez Vue JS depuis NPM.

Mais je renomme simplement la fonction dans le composant app ici.

Nous y voilà.

Et bien sûr, je dois la passer en tant que nom remove.

Donc j'ai essentiellement donné un nom différent à la fonction pour le composant enfant et pour le composant parent.

Et voyons si cela reconnaît cela comme une fonction.

Maintenant, je vais venir ici.

Et je peux le supprimer du panier.

Génial.

Bien sûr, lorsque j'ajoute des choses au panier, je veux que le nombre revienne à zéro ici.

Donc laissez-moi m'en occuper très rapidement.

Dans Add To Cart ici, très rapidement, je vais le définir à zéro.

Voyons si cela fonctionne.

Et de retour à zéro, et il est dans le panier maintenant.

Génial.

La seule autre chose est que le panier montre zéro articles, même lorsqu'il y a des articles dedans.

C'est parce que le nombre n'est pas dynamique.

Donc laissez-moi changer cela très rapidement.

Ici, à l'intérieur des parenthèses, je vais changer cela pour être dynamique.

Et je vais simplement appeler la variable total quantity.

D'accord, et maintenant je dois faire cette variable.

Donc ce que je vais faire, c'est créer un objet computed ici.

Et je vais dire total quantity est essentiellement la somme de toutes les quantités dans le panier.

Et pour cela, je vais utiliser une autre méthode reduce, je vais dire object, that values passe dans this cart.

Et puis je vais réduire ceux-ci pour additionner tous les nombres.

Donc j'ai mon accumulateur et ma valeur actuelle.

Et puis tout ce que je dois faire est d'additionner l'accumulateur et la valeur actuelle.

Bien sûr, je vais définir une valeur par défaut de zéro ici comme point de départ ou valeur initiale.

Et je vais simplement retourner cela directement cette fois.

Laissez-moi voir si cela a fonctionné.

Pour l'instant, il dit zéro, mais laissez-moi ajouter des articles, des notes trois, laissez-moi en ajouter un de plus.

Et maintenant il y en a quatre.

Donc la quantité fonctionne.

Si j'en enlève un, maintenant il n'y en a plus qu'un.

Donc c'est une valeur dynamique maintenant.

Et c'est essentiellement tout pour la page d'accueil ici.

Dans la prochaine vidéo, nous allons déplacer le code Vue JS en dehors du fichier app dot html.

Donc nous pouvons voir comment il peut fonctionner sur plusieurs pages différentes.

Et aussi quelques difficultés que nous pourrions rencontrer en essayant de construire un site multi-pages via le CDN Vue et en essayant de faire des choses comme partager des données entre les pages et autres.

Si vous voulez voir le code de départ pour cette vidéo, assurez-vous de vérifier la branche et le dépôt appelés homepage, numéro deux, ou homepage, deux.

Bonjour à tous, bienvenue.

Tout d'abord, je veux réexaminer ce que nous avons fait dans la dernière vidéo, nous avons connecté le menu de panier coulissant sur la droite ici et l'avons rendu entièrement fonctionnel.

Et puis nous avons ajouté une boucle réelle, ainsi qu'une fonctionnalité pour pouvoir ajouter des articles à notre panier ici.

Maintenant, ce n'est qu'une seule page, bien sûr.

Donc nous avons aussi la page des Produits ici.

Donc si je vais à la page des Produits, vous pouvez voir que l'URL change pour aller à la page products dot html.

Maintenant, si je regarde cela dans mon code, donc laissez-moi ouvrir la source.

Et ce fichier app dot html.

Encore une fois, vous pouvez voir ici l'en-tête avec tous les liens dessus.

Je vais le plier rapidement.

Et puis vous pouvez voir les différentes sections de la page, y compris cette sidebar qui glisse que nous voulons en fait sur chaque page.

Mais maintenant, elle est un peu juste codée en dur dans cette page d'accueil.

Je peux aussi aller dans Vues ici.

Donc vous pouvez voir dans l'en-tête en fait.

Donc lorsque je clique sur produits, il va à Vues slash produits, ce HTML.

Donc il me navigue en fait vers cette page products dot html.

Et si vous regardez l'en-tête ici, voici toute la page, y compris une div complètement séparée avec l'ID de app où nous devrions injecter notre code Vue JS.

Vous pouvez voir que nous l'avons déjà fait sur cette page, car notre Vue j s est dans le script en bas.

Et nous le rendons ou le montons à l'intérieur de cette div.

Mais si je vais à produits, nous n'avons pas de JavaScript, pas d'interaction, tout est codé en dur.

Nous avons aussi un en-tête dupliqué.

Donc c'est exactement la même chose que l'en-tête sur cette page est juste copié-collé dans le HTML sur cette page.

Bien sûr, nous ne voulons pas faire cela partout.

Nous ne voulons pas avoir un en-tête copié-collé pour toutes nos différentes pages.

Non seulement cela, nous devrions aussi copier-coller toute la sidebar du panier.

Donc pour rendre ce code réutilisable ici, nous devons extraire ces éléments dans d'autres fichiers.

Maintenant, ce n'est pas facile à faire pour du HTML simple.

Mais nous pouvons utiliser un composant Vue comme nous l'avons fait auparavant avec la sidebar.

Donc je vais en fait extraire tout cela dans un fichier JavaScript séparé.

Et maintenant importer ce fichier dans mon HTML.

Et vous pouvez voir que ma page fonctionne toujours.

Mon panier est toujours entièrement fonctionnel.

Et ce que cela me permet de faire maintenant, c'est de prendre ce fichier, ce fichier JavaScript que j'ai séparé et de l'importer également dans mon fichier products dot html.

Et je vais en fait prendre les deux balises de script pour que je puisse aussi avoir mon Vue et je vais les mettre en bas ici, sauf que je vais devoir remonter d'un répertoire ici car mon fichier app.js vit en dehors de mes Vues, voici products.

Et j'ai besoin d'obtenir le dossier parent à app.

Donc je dois faire dot dot.

Et cela devrait référencer le bon fichier app.js.

Laissez-moi voir si cela fonctionne pour aller aux produits.

Et vous pouvez voir que la page du panier ne s'ouvre pas.

Mais c'est parce que je n'ai pas encore connecté le bouton du panier.

Donc je vais devoir copier cela depuis le fichier app dot html pour l'instant.

Donc si je vais ici, je peux simplement prendre le même code.

Et maintenant cela devrait référencer la même fonction toggle sidebar, et aussi afficher correctement la quantité totale, car j'importe le même code Vue j s dans la balise de script ici.

Maintenant, vous pouvez voir que la variable du panier s'affiche parfaitement sur la page des Produits.

Mais si je clique ici, bien sûr, le panier ne s'ouvre pas.

Parce que le panier n'est disponible que sur cette page, je n'ai le composant sidebar que ici.

Et le composant sidebar, vous savez, est en fait un composant personnalisé que nous avons fait dans vj s.

Donc nous pouvons le mettre sur n'importe quelle page où nous importons le vj s.

Donc je vais simplement le mettre ici en dessous de cette balise main.

Et avec toutes les mêmes variables, cela devrait être correct, car nous partageons le même script Vue JS.

Laissez-moi sauvegarder cela.

Maintenant, vous pouvez voir que je peux basculer le panier ici.

Et tout cela est à peu près la même chose que ce que nous avons fait sur la page d'accueil, ici en bas où nous avons fait une boucle sur les différents types de nourriture, nous ferions la même chose ici sur la page des Produits, faire une boucle sur eux, connecter chaque nombre individuel, puis connecter le bouton Ajouter au Panier pour qu'il s'affiche réellement dans le panier ici.

Maintenant, si j'ajoute des articles ici, je peux en ajouter quelques au panier, je peux voir que j'en ai trois dans mon panier ici.

Si je vais aux produits, vous pouvez voir que la page a été rafraîchie.

Et maintenant, il n'y a plus d'articles dans mon panier.

Donc, bien qu'il y ait une certaine fonctionnalité à cette application.

Jusqu'à présent, il y a quelques problèmes que nous avons rencontrés en utilisant simplement un CDN pour importer Vue j s.

Et c'est comment partager des données entre les pages et les rafraîchissements de page.

Donc ici, à la page d'accueil, lorsque j'ajoute quelque chose au panier ici, il quitte le panier dès que la page est rafraîchie.

Donc dès que je navigue vers une autre page, il a disparu.

Maintenant, comment pourrais-je résoudre ce problème.

Généralement, dans les applications front-end, nous voudrions faire quelque chose comme persister nos données ou sauvegarder nos données quelque part.

Un moyen facile de le faire dans le navigateur.

Et un moyen très courant est d'aller ici dans l'application.

Et vous pouvez voir qu'il y a différents types de stockage.

C'est le stockage dans le navigateur.

Et le stockage local persistera même si la page est rafraîchie.

Donc nous pouvons en fait sauvegarder les données comme nos données actuelles dans le stockage local ici.

Et puis si nous rafraîchissons ou autre chose, nous allons simplement essayer automatiquement de récupérer tout ce qui est sauvegardé dans le stockage local pour la façon dont notre application est configurée maintenant.

Cela serait chaque fois que nous naviguons vers une nouvelle page, nous devrions vérifier le stockage local, voir s'il y a quelque chose là et puis le récupérer dans notre application.

C'est un peu un contournement pour notre configuration.

Donc un moyen de corriger cela serait en fait de créer une application monopage avec Vue où le front-end ferait en fait le routage.

Au lieu de notre serveur.

Dans ce cas, nous utilisons simplement un serveur live dans VS code.

Mais notre serveur sert des pages chaque fois que nous allons à une nouvelle URL ici.

Et c'est pourquoi il doit rafraîchir car il provient du serveur.

Alors que si nous faisons une application monopage, il n'y aura pas de rafraîchissements de page, nous irons de manière transparente de page en page car notre front-end, en d'autres termes, Vue j S, nous routera vers différentes pages.

Le deuxième problème, comme vous pouvez le voir, est le partage de code.

Nous avons un peu de code dupliqué entre les pages.

Bien sûr, nous réutilisons le même template de sidebar ici, ce template de sidebar.

Nous l'avons simplement enregistré comme un template Vue, un composant Vue appelé sidebar et nous pouvons l'utiliser sur n'importe quelle page.

Maintenant.

Nous pourrions faire la même chose avec l'en-tête aussi.

Et nous le ferions probablement si nous devions construire une application en utilisant le CDN.

Nous devons extraire cela dans un template aussi.

Et puis nous devrions faire la même chose pour la page des commandes passées.

Bien sûr, rien de tout cela n'est dynamique ou configuré pour l'instant.

Mais la chose la plus facile à faire est en fait de configurer notre projet avec quelque chose appelé le Vue COI.

À mesure que notre base de code grandit, il sera très difficile de gérer de nombreux composants différents, si nous les gérons simplement en important différents fichiers dans tous nos différents fichiers HTML.

Mais il existe un moyen beaucoup plus facile.

Et c'est avec le Vue COI. C'est pourquoi il a été créé.

Le vcli nous donne essentiellement une commande, Vue create, et le nom de notre projet, puis il crée un projet entier pour nous.

Il nous guide à travers un assistant de configuration, nous demande quelles fonctionnalités nous voulons.

Et puis il créera tous les fichiers, dossiers et outils de construction nécessaires pour une application front-end monopage robuste.

Donc dans la prochaine vidéo, nous allons prendre tout notre code actuellement dans des fichiers HTML et notre fichier JavaScript et le convertir en une application Vue COI.

Je vous verrai dans la prochaine vidéo.

Commençons avec le Vue COI, je suis à sea ally dot Vue j s.org.

Et je vais simplement cliquer sur getting started.

Et si je vais sur le côté, cliquez sur installation, je peux voir qu'il me demande d'installer globalement ce package Vue COI package at Vue slash c li afin que, depuis ma ligne de commande ou terminal, je pourrai utiliser une commande Vue pour créer des projets.

Maintenant, vous pourriez voir certains endroits sur l'internet qui installent un package différent sans le signe at slash dist Vue dash c li ou quelque chose comme ça.

C'est une ancienne version du package Vue qui a essentiellement son propre espace de noms et puis chacun de ses packages sont après la barre oblique.

Donc pour installer vcli, vous pouvez copier cette commande ici.

Je vais aller à mon terminal.

Maintenant, j'ai le Vue COI installé, je peux vérifier et m'assurer qu'il est installé en vérifiant la version.

Maintenant, j'ai la version 4.5 point 11.

Et maintenant, je veux l'utiliser pour créer un projet Vue réel.

Et je peux faire cela via la commande Vue, create, et puis lui donner le nom du projet que je vais créer.

Si vous voulez voir la documentation pour cette commande, vous pouvez venir ici sous les bases pour créer un projet et lire comment Vue create fonctionne ici.

Je vais aller de l'avant et dire Vue create product and cart comme nom de mon projet et cliquer sur Entrée.

Maintenant, si vous avez utilisé certains outils comme create react app, vous remarquerez que ici, c'est un peu différent.

Il ne démarre pas tout le projet pour vous tout de suite, vous obtenez en fait à choisir vos propres options, et les packages que vous voulez installer et utiliser.

Ces quatre options en haut ici sont en fait des options personnalisées que j'ai créées moi-même.

Vue nous donne ces deux options par défaut pour l'instant, une pour la version deux de vous, et une pour la version trois.

Et puis il nous donne également l'option en bas de sélectionner manuellement les fonctionnalités.

Donc je vais aller de l'avant et faire cela juste pour vous montrer comment cela fonctionne.

Maintenant, vous remarquerez que cette liste ici est multi-sélection.

Et si j'appuie sur la barre d'espace, je peux sélectionner ou désélectionner un élément.

Bien sûr, je veux choisir ma version Vue car je veux utiliser la version trois.

J'ai définitivement besoin d'avoir Babel configuré pour moi pour transpiler mon code Vue, j'aurai besoin de routage dans cette application.

Je vais également utiliser la gestion d'état avec Vue x.

Mais je vais l'ajouter plus tard pour vous montrer comment ajouter un package Vue COI après avoir déjà configuré votre application, les préprocesseurs CSS ou des choses comme sass, si vous pensez que vous voudrez utiliser sass à l'avenir, c'est une bonne idée de le configurer.

Maintenant, je crois que cela fonctionne également avec less et stylus.

Et puis j'ai définitivement besoin de linting et de formatting dans ce projet.

Et je peux optionnellement sélectionner les tests si je veux, mais je ne vais pas le faire cette fois-ci.

Donc une fois que je suis prêt, je vais appuyer sur Entrée, cela m'amène à l'étape suivante, je peux choisir la version de uJs, descendre avec la flèche.

Et je vais choisir la version trois, utiliser le mode history pour le routeur.

C'est un changement de code assez petit.

Mais c'est généralement ce que vous voulez dans un projet.

Cela affecte essentiellement seulement l'URL de votre projet d'un point de vue utilisateur.

Donc si vous voulez que vos routes soient après un hashtag, il utilisera le routeur hash.

Si vous voulez que vos annonces soient après une simple barre oblique, comme n'importe quel site web, vous naviguez dans votre navigateur, alors vous pouvez simplement utiliser le routeur history.

Et je vais utiliser le routeur history.

Maintenant, il me demande de choisir un linter, et un formatter, donc je vais choisir es lint plus la config standard qu'il a pour VJs.

Cliquez sur Entrée, lint les fichiers lorsqu'ils sont sauvegardés, je vais choisir de mettre ma configuration dans le package dot JSON cette fois-ci, juste pour ne pas avoir un tas de fichiers de config supplémentaires.

Généralement, lorsque vous avez des projets plus grands, vous voulez des fichiers de config dédiés.

Donc cela n'encombre pas votre package dot JSON.

Est-ce que je veux sauvegarder cela comme un preset ? Non, je ne le veux pas cette fois-ci.

Mais si vous vous souvenez au début de ce tutoriel, les quatre options en haut, c'étaient des presets que j'avais sauvegardés dans le passé, mais ici je vais simplement dire non.

Ici, il configure essentiellement tout mon projet avec la structure de fichiers et tout.

Et il exécute également une installation npm, vous pouvez voir qu'il a créé mon projet avec succès.

Si je liste les dossiers à l'intérieur maintenant, j'ai ce nouveau dossier qui a été créé pour moi par Vue JS appelé product and cart.

Je vais entrer dans ce dossier.

Et vous pouvez voir lorsque vous avez démarré le projet pour moi, il a également initialisé un dépôt git pour moi, et sauvegardé tous les changements qu'il a faits initialement comme un commit.

Donc laissez-moi l'ouvrir dans VS code.

Et j'ai mon projet complet créé pour moi par Vue.

Dans la prochaine vidéo, nous allons parcourir tous ces fichiers et dossiers et vous donner un petit tour de la façon dont votre projet Vue est organisé.

En regardant cela, cela ressemble à peu près au dernier projet sur lequel nous avons travaillé avec des fichiers HTML, CSS et JavaScript statiques.

Et c'était par conception, pour vous donner le même style de codage et de structure de fichiers que vous utiliseriez dans une application Vue réelle.

Cela, cependant, est beaucoup plus agréable.

En commençant avec le Vue, see ally nous donne beaucoup plus de fonctionnalités dès le départ que nous pouvons voir dans le package dot JSON, nous avons trois scripts ici par défaut, il y en aurait plus si vous choisissez d'installer les packages de test également, car nous avons installé un linter, le vcli nous donne cette commande link.

Et puis il nous donne également nos deux commandes principales pour l'application Vue pour le développement local, il nous donne cette commande serve, qui appelle essentiellement ce package vcli service.

Cela provient de Vue, j s lui donne la commande serve et il exécutera un serveur de développement pour nous.

Donc il n'y a plus de l'ancienne configuration de serveur compliquée que nous avions dans la dernière version de celle-ci dans la dernière application.

La commande build est vraiment pour lorsque nous voulons héberger notre projet en direct.

Cela générera des fichiers prêts pour la production pour vous comme votre HTML, CSS, et JavaScript.

Donc vous pouvez les déployer et avoir un site web en direct quelque part.

Nous allons juste parler de cette commande dans cette vidéo.

Et pour vous donner une idée de ce qu'elle fait, allons-y et exécutons-la.

Je peux utiliser NPM pour exécuter la commande.

Donc NPM run serve.

Et maintenant mon app est en cours d'exécution au Port 8080.

Si je surligne quelque chose sur le terminal, il copie automatiquement lorsque je viens à mon navigateur, ouvre un nouvel onglet et je peux voir qu'il me donne une app déjà configurée dès le départ.

Et parce que nous avons choisi d'installer un routeur aussi, il a installé le routeur Vue par défaut, qui est aussi appelé Vue router.

Et vous pouvez voir que je peux aller à différentes routes de page.

Maintenant, ce n'est pas la même chose que notre dernière application, car il n'y a pas de rafraîchissement de page entre les routes de page.

Ce ne sont pas des liens HTML.

C'est juste un routeur JavaScript, rendant, cachant ou montrant différentes pages de cette application.

Vous remarquez également depuis la page d'accueil, c'est juste le Port 8080.

Lorsque vous allez à la page about à ad slash about, si nous regardons dans le dossier public ici, vous pouvez voir ici notre page HTML.

Et nous avons une div d'ID app.

Et c'est là que notre app sera injectée.

Mais aussi lorsque notre application est construite.

Sous le capot, cette commande Vue COI service exécute Webpack, et regroupe tous nos fichiers ensemble, et gère également l'exécution de Babel pour transpiler nos fichiers, et ainsi tout le JavaScript et tout sera injecté en tant que balises de script également ici.

Mais nous n'avons généralement pas à nous soucier de ce fichier index dot HTML dans un projet Vue.

Parce que encore une fois, la plupart de ce que nous allons faire est dans le dossier source juste ici.

Donc nous avons un fichier main dot j.

s qui est toujours créé pour nous.

Donc c'est essentiellement la même chose que ce que nous avons fait dans l'application précédente.

Si vous faites c Vue to code, ce fichier aura un aspect un peu différent.

Mais vous pourrez toujours voir les différentes parties, juste l'organisation et la syntaxe sont un peu différentes.

Tout comme avant, nous devons passer dans un composant racine, nous enchaînons tous les packages que nous voulons utiliser, dans ce cas, le routeur, et puis nous montons cela dans le DOM.

Donc à l'intérieur de la div avec l'ID de app.

Et vous pourriez aussi réécrire cela comme const app.

Et puis app dot use router, et puis app dot mount.

C'est un peu plus facile à analyser lorsque vous ajoutez plus de packages.

Maintenant, lorsque nous regardons cette page initiale, d'où vient tout cela ? Jetons un coup d'œil.

Donc nous avons notre composant principal app.

Mais vous remarquerez dans app, il n'y a pas de vrai contenu ici.

Tout ce que c'est, c'est une div.

C'est essentiellement la navigation supérieure.

Maintenant, d'où vient ce router link ? C'est en fait un composant personnalisé.

Et si vous regardez notre main j s, lorsque nous utilisons App dot use router, nous recevons en fait certains composants comme router link, ainsi que router Vue.

Maintenant, router link est en fait une substitution pour utiliser la balise d'ancrage pour lier à une autre page.

Sauf que router link est fait par Vue router, spécifiquement pour le routage d'application monopage, où notre JavaScript gère le routage.

Au lieu de lier à une page HTML séparée.

Bien sûr, nous n'avons qu'une seule page HTML.

Et tout notre contenu statique est injecté dans cette seule page.

Et le routeur gère l'interception de la route et fait apparaître comme si vous aviez navigué vers une autre page.

Alors qu'en réalité, il montre et cache simplement différents éléments sur le DOM.

Donc nous avons ces deux router links.

Et puis que fait router Vue ? Donc router Vue, est en fait notre contenu de page.

Et notre routeur gérera le remplacement de cette balise router Vue par le composant que nous lui disons dans notre fichier de routes que nous allons regarder.

Donc router Vue est juste un espace réservé temporaire pour ce que nous mettons sur la page.

Et vous verrez que nous naviguons vers différentes pages, ces liens home et about en haut de ce fichier.

Ceux-ci resteront peu importe la page vers laquelle nous naviguons.

Mais tout le contenu en dessous changera car ce sont les composants qui sont injectés dans cette zone router Vue ici.

Si nous regardons dans notre fichier router index.js ici, nous pouvons voir que nous utilisons l'API Vue router pour créer un routeur et lorsque nous créons un routeur ici, nous passons deux choses.

Donc les routes, qui est un tableau de toutes nos routes que nous avons dans l'application, et puis le mode history, il l'a configuré pour nous parce que nous avons choisi d'utiliser le mode history.

Et Vue gère tout cela en coulisses.

Mais parlons des routes ici.

Donc nous avons la route home par défaut, qui est cette page.

Et puis nous avons aussi la page about, qui se trouve à cette route.

Maintenant, vous n'avez pas à vous soucier du code splitting, et du lazy loading et de toutes ces autres choses.

Ce sont des concepts de routage plus avancés.

Donc je vais me débarrasser de cette ligne.

Et puis simplement importer le composant about.

Tout comme le composant home.

Maintenant, vous définissez essentiellement des routes ici.

Et au lieu d'importer les composants que vous voulez afficher sur une page dans votre app dot Vue, vous utilisez simplement une balise router Vue ici.

Et puis vous importez l'un de vos composants Vue, comme home et about dans ce fichier, vous définissez le chemin où ce composant peut être trouvé, le nom de ce composant, maintenant le nom est principalement utilisé pour le routage, et puis vous lui dites quel composant sera trouvé à ce chemin.

Donc à la route home, nous allons trouver le composant home.

Maintenant, où est le composant home, vous pouvez voir qu'il est dans Vues slash home.

Donc allons-y.

Et nous pouvons voir que c'est le composant, il a une image, qui est le logo Vue en haut.

Et puis il importe également un autre composant en lui-même.

Maintenant, ce composant n'est pas dans le dossier Vues, il est dans le répertoire des composants.

Maintenant, pourquoi est-il dans le répertoire des composants, au lieu d'un seul dossier pour tous les fichiers Vue, essentiellement, dans les applications front-end, les fichiers sont généralement divisés entre Vues, ou pages.

Donc, essentiellement, tout ce qui se trouve dans ce dossier Vues sera connecté au routeur.

Donc ils auront leurs propres routes, ils seront leurs propres pages.

Tout ce qui se trouve dans le dossier des composants sont des choses qui sont importées dans d'autres composants.

Ils sont censés être des parties de pages ou des composants réutilisables que vous utilisez dans toute votre application.

Essentiellement, tout ce qui se trouve dans le dossier Vues est connecté au routeur.

Et si ce n'est pas connecté au routeur, et simplement importé dans un autre composant, alors mettez-le dans le dossier des composants.

Et vous pouvez voir à la route home, il y a une image Vue en haut.

Et puis il y a tous ces liens ici.

Et c'est exactement ce que nous voyons dans la route home.

Maintenant, si nous allons à la page about, elle n'importe aucun autre composant ou ne fait rien de fantaisiste.

Il n'y a que ce h1.

Donc un en-tête avec ce texte, qui est ce que nous voyons lorsque nous allons à la page about.

Les assets, bien sûr, sont un endroit pour que le CSS, les images, tout ce genre de choses vivent.

Parfois, vous verrez d'autres dossiers créés ici dans les projets Vue.

Mais ce sont les bases.

Le seul que nous allons ajouter plus tard est le dossier store.

Et nous en parlerons dans quelques vidéos.

Dans la prochaine vidéo, nous allons commencer à transférer notre contenu de notre ancienne application statique vers notre application Vue.

Commençons à déplacer les choses une par une en commençant par la page d'accueil.

Je vais aller dans mon code original ici dans source et puis aller dans mon app dot html ici.

La première chose dont j'ai besoin est de prendre cet en-tête.

Maintenant, j'ai un peu de JavaScript ici et je vais m'occuper de le connecter dans une minute.

Mais laissez-moi simplement copier-coller pour l'instant.

Et déplacer cela vers un nouveau fichier.

Maintenant, je vais en avoir besoin sur cette page d'accueil ici.

Mais puisque cet en-tête est en fait ma navigation à travers l'application, je vais en fait vouloir remplacer la navigation ici.

Donc que je puisse l'utiliser et la voir sur n'importe quelle page.

Pour l'instant, je vais me débarrasser de ceux-ci.

Maintenant, il y a un peu de nettoyage que je dois faire ici.

Parce que ces balises d'ancrage doivent être changées en balises de lien de routeur Vue.

Et maintenant j'ai besoin d'une vraie route.

Donc au lieu de pointer vers un fichier HTML, je vais lui donner une route qui sera dans mon routeur ici liée à un composant.

Donc j'ai ce products dot html ici, ce que je vais faire est de le changer en slash products.

Bien sûr, cela ne peut pas être un H ref, cela sera deux, puisque c'est attendu par le router link, il faut aussi changer cela de h ref à deux.

Et je peux simplement appeler cette route past orders, me débarrasser du dot html.

Et ici aussi, changer cela en deux.

Et cela devrait être juste une barre oblique.

Je ne vais pas m'inquiéter de cela pour l'instant.

Ce dernier router link en bas, je vais simplement le commenter pour l'instant.

Et essentiellement, je dois créer ces trois composants qui sont liés aux routes.

Maintenant, j'ai déjà la route home ici qui est liée au composant home, je vais en fait me débarrasser de about et je vais changer cela en products.

Je vais devoir créer un nouveau composant.

Maintenant, laissez-moi supprimer about d'ici.

Et laissez-moi créer un nouveau fichier.

Je vais l'appeler products dot Vue.

Maintenant, c'est un peu différent.

Au lieu d'appeler cela simplement un fichier JavaScript régulier, avec l'extension j s Vue a une extension de fichier personnalisée, qui est dot Vue.

Tous ces fichiers dot Vue sont analysés par la configuration Vue et webpack, que le Vue COI configure pour nous.

Donc en utilisant ces fichiers dot Vue, nous pouvons mettre notre template HTML, notre JavaScript, et même notre CSS tous dans le même fichier qui est analysé et tout est mis ensemble et regroupé par les outils que vcli configure pour nous.

Maintenant, j'ai un nouveau fichier, je vais simplement créer un template ici.

Et j'ai quatre espaces, je vais passer à l'utilisation de deux espaces pour l'espacement des tabulations.

Et je vais simplement mettre h1 products pour l'instant.

D'accord, avant d'aller trop loin, voyons à quoi cela ressemble.

Et nous avons une page Produits et une page d'accueil maintenant.

Mais bien sûr, cela est complètement non stylisé.

Faisons une pause ici et commençons à apporter certains des styles dans la prochaine vidéo.

Commençons à déplacer nos styles.

Maintenant, nos styles vont vivre à l'intérieur de ce dossier assets.

Et je peux aller de l'avant et créer un dossier à l'intérieur de celui-ci appelé styles.

Maintenant, comment utiliser les styles dans mon projet.

Si vous venez à ce composant app ici, vous remarquerez qu'il y a une balise de style en bas du composant.

Et ce sont ceux qui fournissent des styles personnalisés pour l'application.

Si je regarde dans mon navigateur, c'est ce qui style et centre les éléments.

Si je me débarrasse de ces styles, voici à quoi cela ressemble sans aucun de ces styles personnalisés.

Dans n'importe quel composant Vue, vous pouvez ajouter des styles directement à l'intérieur de ce composant.

Donc si je voulais faire quelque chose, je pourrais changer toutes les balises h1 en couleur bleue.

Et vous remarquerez que c'est juste du CSS simple ici que vous pouvez écrire à l'intérieur de ces fichiers Vue.

Maintenant, si je vais ici, vous pouvez voir que c'est une balise h1, et elle a changé pour être bleue.

Aussi sur la balise products qui est bleue également, car c'est une autre h1.

Maintenant, si je regarde cela, cependant, ces éléments h1 ne sont nulle part dans ce composant.

Ceux-ci sont en fait dans d'autres composants.

Mais par défaut, la balise de style affecte globalement tout ce qui se trouve dans l'application.

Donc si je mets une balise de style ici, même si elle est dans le fichier app dot Vue, n'importe où dans mon application qui a une balise h1 peut être affectée par cela.

Maintenant, ce n'est généralement pas une bonne pratique.

Parce que si vous voulez changer globalement un style, vous devriez le mettre dans une feuille de style séparée.

Donc dans un autre fichier dot CSS, ici, si je mets des styles à l'intérieur de mon fichier app dot Vue, généralement, ce que je veux faire est de ne le laisser affecter que le fichier app dot Vue.

Donc il ne changera pas les styles dans d'autres composants.

Exact, il n'affectera que ce qui se trouve dans mon template dans ce fichier.

Et c'est pourquoi j'utilise le mot-clé scope ici.

Maintenant, maintenant que j'ai ajouté le mot-clé scope, vous pouvez voir que le texte est revenu à noir.

Parce que maintenant que je l'ai scopé, il n'affecte que les styles à l'intérieur de ce composant Vue, pas dans d'autres composants à travers l'application.

Maintenant, si je voulais ajouter une feuille de style externe, laissez-moi simplement en créer une temporaire ici.

Je vais l'appeler main dot CSS.

Et laissez-moi coller mon dernier style.

Et je vais changer la couleur.

Cela n'affectera pas mon application pour l'instant, car je dois importer le fichier CSS.

Maintenant, au lieu d'importer cela dans l'un de mes fichiers HTML, ce que Vue fait, c'est me permettre de l'importer directement dans mon JavaScript.

Donc généralement, ce serait ce fichier main.js, ce que je peux faire est importer depuis les assets, styles.

Et puis ce main dot CSS, et la configuration Vue, see ally a configuré Webpack pour moi de telle sorte que je puisse importer des styles directement dans mon JavaScript.

Et tout est géré par les outils.

Donc maintenant, si je reviens à mon navigateur, il est un peu plus sombre.

Mais vous pouvez dire que cela est violet maintenant.

Parce que je l'importe globalement, dans mon projet depuis ce fichier main dot CSS.

Ce sont les bases de la façon dont vous importez des styles dans une application.

Maintenant, si je reviens à mon application statique originale avec nos fichiers HTML que nous utilisions, si je viens aux styles ici, vous pouvez voir que ceux-ci ne sont pas simplement des fichiers CSS.

Ce sont des fichiers sass, pour la plupart.

Donc comment puis-je les intégrer dans mon projet s'ils ne sont pas des fichiers CSS standard.

Donc Vue a également des moyens intégrés de gérer cela, laissez-moi copier ces styles.

Et je vais supprimer ce dossier de styles ici.

Et je vais coller.

Donc j'ai collé ce dossier de styles de mon autre projet.

Et maintenant si je regarde dans ce dossier, il y a un fichier appelé style dot SCSS, qui est un fichier sass.

Et celui-ci importe tous les autres fichiers ici, tous mes autres fichiers sass.

Maintenant, c'est ce fichier que je veux vraiment importer dans mon projet pour obtenir tous mes styles.

Je vais commenter cela.

Et maintenant je vais importer ce fichier sass directement depuis assets slash styles, slash style dot s CSS.

Je vais sauvegarder cela.

Et maintenant vous pouvez voir qu'il me donne une erreur disant ne peut pas résoudre sass loader donc il essaie de charger ces fichiers sass.

Mais comme ils ne sont pas du CSS régulier, nous devons ajouter un autre module pour pouvoir importer ces fichiers.

Et c'est comme il est dit sass loader.

Si nous regardons dans la documentation Vue COI, et allons à travailler avec CSS sous développement, nous pouvons voir qu'il a cette section sur les préprocesseurs.

Maintenant, comme il est mentionné, nous pouvons sélectionner notre préprocesseur lorsque nous créons le projet, ce qui signifie lorsque nous avons exécuté cette première commande Vue, create project name, cette commande nous a fait passer par la configuration de SAS automatiquement.

Maintenant, puisque nous n'avons pas choisi SAS à l'époque, lorsque nous l'avons configuré, il existe des moyens d'ajouter ces packages, que vous pouvez faire via cette commande, npm install, puis installer le sass loader.

Et aussi le package sass.

Maintenant, si je fais défiler un peu vers le bas, il me donne cette note sur Webpack quatre, que j'utilise dans vcli.

Je dois m'assurer que j'ai une version compatible de ces loaders.

Donc je vais aller de l'avant et prendre cette commande npm install où je peux installer sass loader à une version spécifique et aussi sass et installer ces packages pour moi.

Maintenant, je devrais pouvoir exécuter mon serveur une fois de plus.

NPM run serve.

Maintenant, il se plaint que je n'ai pas un module CSS spécifique, parce que je ne l'ai pas installé dans mes modules de nœud.

Mais c'est en fait un bon signe car cela signifie qu'il lit à travers le reste de mon fichier ici, il lit à travers cela, arrive à cette ligne et dit, Hé, je ne peux pas trouver ce fichier.

Donc je vais simplement commenter cela pour l'instant.

Et maintenant nous avons une autre erreur ici.

Et c'est qu'il cherche des images qu'il ne peut pas trouver pour l'instant.

Allons de l'avant et résolvons cela.

Et ils proviennent de ce fichier.

Donc si je vais à splash dot sass, maintenant vous remarquerez que la syntaxe est un peu différente ici.

Vous pouvez essentiellement penser à cela comme une syntaxe indentée sans accolades.

Dans tous les cas, vous pouvez voir que les attributs sont les mêmes ici.

Donc j'ai une image de fond, elle cherche cette image.

Et encore, il y a une image de fond, qui cherche cette image verte.

Donc je vais créer un dossier images ici, un dossier IMG, et mettre ces deux images à l'intérieur du dossier IMG, puis mettre à jour ce chemin.

Donc dans mon ancienne application, elles étaient dans mon répertoire public, j'ai green, et splash.

Je vais les copier et les coller ici.

Et je devrais pouvoir référencer le chemin relatif ici.

Fermer ce fichier.

Et vous pouvez voir que j'ai les styles pour mon application principale ici.

Maintenant, laissez-moi faire une chose de plus et me débarrasser de ce code de démarrage ici.

Donc je peux être prêt à mettre mon propre contenu là.

Donc laissez-moi sortir d'ici.

Et aller à source slash Vues et home, je vais me débarrasser de cette image, aussi me débarrasser de ce composant.

Je vais simplement mettre home ici pour l'instant et me débarrasser du composant partout.

Maintenant, si je reviens à cette page, vous pouvez voir qu'elle est prête à ajouter mon propre contenu personnalisé.

Et je peux voir la page Produits et navigue également.

Une chose de plus que je vais faire est d'ajouter une page de commandes passées au routeur à cette route.

Et tout ce que j'ai à faire est essentiellement de copier la route des produits.

Cela sera les commandes passées.

Je peux l'appeler commandes passées.

Commandes passées.

Maintenant, je dois créer ce composant.

Il est connecté à mon routeur.

Donc je vais le créer dans le dossier Vues.

L'appeler past orders dot Vue et j'ai un raccourci snippet ici.

Je vais vous montrer comment l'utiliser, mais si je clique sur Entrée, il vient de créer la balise de template pour moi.

Et je vais mettre un h1 ici qui dit, commandes passées.

Et maintenant j'ai cette page qui fonctionne.

Donc les trois pages sont là.

Dans la prochaine vidéo, je vais mettre du contenu sur ces pages, puis les connecter à JavaScript pour les rendre fonctionnelles.

Maintenant, travaillons à mettre du contenu réel sur cette page d'accueil.

Je suis dans l'application originale.

Maintenant, laissez-moi aller à source à l'intérieur de Vues ici, j'ai mes pages, en fait, la page principale est toujours dans app dot html.

Donc je vais aller de l'avant et prendre ces deux éléments de conteneur ici, la div et le conteneur principal, copier ceux-ci, aller dans mon nouveau code, mon projet vcli.

Et ici, je peux venir à ma page d'accueil, et simplement coller cela ici.

D'accord, maintenant prenez cela, juste l'indentation, débarrassez-vous de ce vieux mot.

Et maintenant j'ai mon conteneur splash.

Et aussi mon conteneur principal.

Et rien ne s'affiche sur la page.

Donc si je regarde dans les outils de développement, il dit ne peut pas lire la propriété slice de undefined.

Et je peux rechercher où cela est utilisé.

Et inventory dot slice.

Donc bien sûr, il est cassé maintenant parce que je n'ai aucun inventaire.

Donc laissez-moi prendre cela de ma base de code originale.

Si je vais ici, je peux voir dans food dot JSON, ce fichier contient vraiment mes articles d'inventaire.

Donc je vais copier ce fichier, copier, aller ici.

Et à l'intérieur de source, je vais simplement coller ce fichier.

Et maintenant j'ai besoin de l'importer dans mon Vue j s.

Donc si je veux cela maintenant dans mon composant home, je dois l'importer en bas ici.

Donc laissez-moi importer mes données.

Donc importer food de go up a directory food, ce JSON.

Laissez-le égal à une variable de données.

Donc data et puis je peux retourner.

Et puis je peux définir inventory égal à food.

D'accord, essayons cela.

Et maintenant nous voyons que la bannière s'affiche très bien.

Et nous pouvons voir notre section des Produits Recommandés en bas, qui affiche déjà des données réelles.

Parce que nous l'avons déjà configuré.

Et c'est essentiellement la même logique que l'autre app.

Mais nous l'avons seulement réécrite dans une structure de composant.

Maintenant, importons les autres pages très rapidement.

Donc nous avons les commandes passées, et aussi les produits.

Allons aux produits.

Et si je vais à la page Produits, je peux simplement prendre cette section principale ici, revenir à mon code, et puis la coller.

Maintenant, cette page devrait fonctionner telle quelle car si je regarde tout le code ici, nous ne l'avons jamais rendu dynamique.

Donc c'est quelque chose que nous devrons changer plus tard.

Mais tout cela est codé en dur.

Laissez-moi prendre la page des commandes passées rapidement.

Et puis nous pouvons y jeter un coup d'œil dans le navigateur.

Donc si je vais aux commandes passées, laissez-moi plier cette section principale.

Je vais copier cela et aller ici dans mon code.

Coller cela.

Et maintenant, jetons un coup d'œil à ces pages.

D'accord, donc notre page des commandes passées a une erreur.

Et elle se plaint que cette balise i, qui était utilisée pour les icônes généralement, n'a pas de balise de fermeture, ce qui signifie qu'elle n'est pas explicitement auto-fermante et je ne la ferme pas explicitement non plus, comme cette balise TD ici a une balise TD de fermeture là.

Donc je vais devoir corriger cela.

Ce n'est pas grave.

Cela se produit seulement en deux endroits, ce qui est bien.

Tout ce que je dois faire pour corriger cela est soit je pourrais faire une balise de fermeture, des choses comme IMG et I et certaines balises n'ont pas vraiment de balises de fermeture.

Donc tout ce que je dois faire est de les rendre auto-fermantes, puisque vous ne allez jamais imbriquer quoi que ce soit à l'intérieur de cette balise en général.

Donc je ajoute simplement la barre oblique à la fin.

Et je vais faire cela avec ce I aussi.

Et cela a corrigé mon erreur.

Et maintenant voici la page des Produits.

Et la page des commandes passées aussi.

C'est une sorte de tableau des commandes précédentes.

Maintenant, qu'en est-il de la barre latérale ? Ajoutons cette logique dans la prochaine vidéo.

Dans notre application originale, nous avions cette barre latérale à droite pour afficher notre panier.

Dans cette vidéo, nous allons la déplacer vers notre nouvelle application Vue see ally.

Donc je suis dans la base de code originale ici.

Si je vais à l'un de mes fichiers, je peux voir qu'il y a un composant sidebar, qui est un composant Vue personnalisé que je définis dans mon fichier app dot j s, ce composant sidebar que j'enregistre, et je peux essentiellement l'utiliser globalement dans toute mon application.

Maintenant, bien sûr, ceci est juste du code Vue régulier.

Donc je pourrais absolument faire la même chose dans ma nouvelle application.

Mais il y a d'autres façons dont je peux maintenant créer des composants réutilisables.

Donc je vais en fait le mettre dans mon dossier de composants.

à la place.

Je vais copier tout cela.

Laissez-moi aller dans les composants, j'ai ce vieux composant HelloWorld, je vais le supprimer car je n'en ai plus besoin.

Et puis je vais créer un nouveau fichier ici et l'appeler sidebar dot Vue.

Ici, bien sûr, j'ai besoin du template.

Et je vais coller tout ce code.

Et c'est essentiellement toute la logique du panier.

Maintenant, il y a quelques choses que je devrais ajouter, passer un toggle dynamique ici lorsque le bouton est cliqué.

Donc laissez-moi aller de l'avant et configurer cela.

Maintenant, la première chose que je dois faire est d'importer ce composant sidebar dans mon application.

Et il sera disponible globalement sur toutes mes pages.

Donc je vais l'importer dans mon fichier app dot Vue.

Et je vais le faire en dessous.

En fait, je le fais en bas ici.

Je vais mettre sidebar, il doit bien sûr être auto-fermant ici.

Et la convention est de mettre en majuscule les composants personnalisés.

Donc vous pouvez facilement les voir et ils sont même mis en évidence différemment de tout ce qui est en minuscules que j'ai importé d'une bibliothèque ou qui est simplement du HTML standard.

Je vais me débarrasser de ma balise de style ici et ajouter une balise de script.

Et maintenant je peux importer ce composant.

Donc je vais importer sidebar de that slash components slash sidebar dot Vue.

Maintenant, une autre façon d'écrire cela et ce que vous verrez souvent dans les applications Vue.

Ici, vous verrez un signe plus.

Maintenant, c'est un raccourci, une sorte de référence au dossier source.

Donc, de cette façon, n'importe où dans mon application, peu importe combien de fichiers profonds mes composants sont, je n'ai pas à faire quelque chose comme dot dot slash dot, dot slash dot, dot, etc.

Je peux toujours référencer le dossier source avec un symbole at.

Donc ce sera source slash components slash sidebar dot Vue.

Maintenant, tout composant que j'importe dans un autre composant, je dois l'enregistrer et dire à mon application Vue que je vais utiliser ce composant.

Et je peux faire cela en définissant un objet Component sur cet objet d'options par défaut dans Vue.

Et je peux définir le composant sidebar ici, l'enregistrer ici ou l'inclure dans la liste des notes de composant ici signifie simplement que je peux l'utiliser ici dans mon template.

Donc comment cela fonctionne, essentiellement, tout cet objet ici, c'est ce qu'on appelle l'objet d'options.

Et tout type de fonctions JavaScript ou de données sera défini sur cet objet, je veux juste souligner que cela est exactement la même chose que l'objet d'options que vous avez utilisé dans les composants personnalisés comme celui-ci, sauf que le template dans notre fichier dot Vue est simplement inclus en haut ici à l'intérieur de ce template.

Et si nous regardons ce composant principal app ici, tout ce qui se trouve à l'intérieur de cet objet, toutes ces données, computed methods, tout cela est l'objet d'options.

Mais ici, nous l'avons pour être utilisé globalement.

Et lorsque nous créons une application vcli, nous avons essentiellement un template, et un objet d'options par composant que nous utilisons pour définir tout.

Maintenant, le problème avec cela est que chaque composant ne connaît que le JavaScript à l'intérieur de l'objet d'options de ce composant.

Donc si je crée une fonction ici, je ne peux l'utiliser que ici et dans aucun autre composant, à moins que je ne la passe explicitement dans ce composant pour être utilisée.

De la même manière que nous passons les données et les fonctions à différents composants lorsque nous construisions l'application statique.

Et ici, nous allons devoir le faire à nouveau, car la sidebar nécessite certaines choses à passer.

Maintenant, si nous regardons, ici, nous pouvons voir qu'il y a d'abord un V, si booléen, il y a une fonction pour basculer la sidebar, lorsqu'elle est cliquée, ou lorsque le bouton est cliqué pour l'ouvrir ou la fermer.

Il y a aussi un objet cart pour ce qui se trouve actuellement dans le panier.

Il y a tous nos articles d'inventaire, et puis il y a une fonction remove item.

Donc je vais copier toutes ces choses et les coller ici.

Et maintenant je dois définir ces propriétés.

La première chose est Vf, je dois créer une propriété de données show sidebar ici.

Et je vais définir cela par défaut comme true pour l'instant.

Donc je peux voir la sidebar.

Maintenant, j'ai besoin d'une fonction toggle sidebar.

Maintenant, d'où vient cela ? Cela doit venir de mon composant app ici, car je le passe, essentiellement de app à la sidebar.

Donc voici ma fonction toggle sidebar.

Et je vais simplement prendre toutes ces fonctions maintenant.

Et je vais créer cet objet méthodes.

Et j'ai collé toutes mes méthodes ici.

Maintenant, voici une autre partie délicate car je veux référencer l'inventaire ici.

Mais malheureusement, je ne l'ai que dans mon composant home, que je viens de mettre ici pour résoudre mon problème de base de l'inventaire étant undefined.

Donc je vais devoir restructurer mon application.

Donc je n'importe pas l'inventaire séparément dans chaque composant.

Donc laissez-moi en fait prendre cette importation.

Et je vais simplement importer l'inventaire dans mon composant app dot Vue.

Donc je l'importe ici.

Et puis ma logique ici, donc inventory food.

Et je vais l'ajouter à cela aussi.

Donc inventory est food.

Maintenant, j'ai besoin de l'obtenir dans mon composant home.

Mais ce n'est pas vraiment un composant enregistré sur cette page, comme sidebar, je peux facilement passer des éléments dans sidebar comme props, car c'est un composant enregistré ici.

Mais home est un peu différent car le routeur met dynamiquement le composant home là.

Donc comment puis-je passer des props à travers le routeur alors, à n'importe quel composant de routeur Vue, ce que nous allons faire est de passer l'inventaire dans essentiellement n'importe quel composant de routeur Vue.

Donc je vais passer la variable inventory et bien sûr, je dois V bind cela pour qu'elle cherche réellement une variable, et ne la considère pas comme une simple chaîne ici.

Donc maintenant je passe inventory.

Et j'ai besoin de l'accepter dans le composant enfant.

Donc au lieu de data ici, je vais en fait devoir utiliser props comme je l'ai fait avant, et je vais simplement le faire comme un tableau en fait.

Et je dois l'appeler inventory.

Il y a quelques autres éléments cassés que je vais devoir corriger ici que la sidebar attend, j'ai mon inventory et remove item.

Et j'ai vraiment besoin de mon cart à ce stade.

Maintenant, si je regarde dans la version originale, je peux voir que le cart est juste un objet vide.

Et puis les choses peuvent être ajoutées dynamiquement au cart.

Mais nous allons nous soucier d'ajouter des choses dynamiquement dans une minute.

Mais d'abord, je vais simplement le définir comme un objet vide.

Donc laissez-moi aller à data ici et définir cart comme un objet vide.

Très rapidement, allons de l'avant et prenons cette propriété calculée aussi, car nous en aurons besoin.

Donc je vais descendre ici et mettre computed.

Et vérifions cela dans le navigateur.

Donc il se plaint maintenant qu'il ne peut pas trouver ce fichier JSON.

Et c'est parce que nous l'importons du mauvais endroit.

Et oui, l'app est en cours d'exécution, produits, commandes passées, tout semble fonctionner correctement.

Cependant, nous n'avons pas encore la sidebar.

Donc laissez-moi aller de l'avant et décommenter ce code ici.

Donc nous avons toggle sidebar, et aussi l'affichage de la quantité et le bouton ici.

Donc ici, je devrais pouvoir voir le bouton que nous avions avant dans notre application précédente.

D'accord, lorsque je viens ici, et que je rafraîchis, rien ne s'affiche.

Donc nous avons un problème.

Il dit erreur de type non capturé, chemin de undefined.

Donc le chemin, cela fait référence au routeur.

Donc je pense qu'il nous donne une erreur dans le router link, car nous n'utilisons pas correctement le router link.

Donc laissez-moi simplement changer cela en une div, nous ne disons essentiellement pas au routeur d'aller quelque part, nous utilisons simplement cela comme un élément cliquable.

Donc nous pourrions aussi bien utiliser autre chose.

Et maintenant cela fonctionne.

Sauf que je ne peux pas cliquer sur le bouton du panier, cela ne fonctionne pas encore.

Mais tout le reste fonctionne.

Laissez-moi faire défiler vers le haut pour voir mon erreur originale ici.

Donc il dit ne peut pas convertir undefined ou null en objet.

Et cette boucle est essentiellement à l'intérieur de mon composant sidebar.

Donc il se plaint de cette ligne ici, ligne 25.

J'essaie de boucler à travers un objet cart, obtenir la quantité et la clé ainsi que l'index.

Et essentiellement, il dit que cart doit être une valeur undefined.

Donc laissez-moi jeter un coup d'œil dans mon app ici.

Il ne s'ouvre pas.

Donc laissez-moi en fait jeter un coup d'œil au code original.

Et à l'intérieur de mon app dot j s, j'ai tout ce code déplacé sauf ce mounted ici, mais je n'en ai plus besoin, car je peux maintenant importer directement le fichier JSON.

Je n'ai pas besoin de le récupérer.

Donc voici mon composant sidebar.

Et en fait, je n'ai pas copié les méthodes ici et j'oublie aussi d'ajouter les props.

Donc laissez-moi aller de l'avant et faire cela.

Copiez simplement cela.

Revenez ici à sidebar et j'ai effectivement besoin d'une balise de script en bas ici.

Donc je vais ajouter une balise de script, coller les props.

Et puis je veux aussi les méthodes d'ici donc je vais les prendre aussi.

Maintenant, calculate total et get price sont définis, puis j'ai toutes les props ici.

Donc voyons si cela fonctionne.

Hourra.

Et le basculement fonctionne parfaitement.

Bien sûr, il commence par être ouvert.

Si je le rafraîchis, il s'ouvre simplement automatiquement.

Donc laissez-moi changer cela dans app dot Vue.

Je vais venir ici et dire show sidebar est false.

D'accord, laissez-moi voir si nous pouvons utiliser cela.

Donc ce n'est pas encore l'ajout dynamique d'articles au panier.

Donc nous allons corriger cela dans la prochaine vidéo.

Dans cette vidéo, nous allons connecter la fonctionnalité d'ajout au panier afin que lorsque nous ajoutons au panier ici, cela s'affichera dans la barre latérale.

Si je regarde dans le terminal, maintenant, vous pouvez voir que cet ajout au panier, il dit que ce n'est pas une fonction.

Donc j'ai une erreur lorsque je clique sur ce bouton Ajouter au Panier.

Maintenant, je peux voir pourquoi j'ai cette erreur, car cela est dans mon composant de page d'accueil.

Et si je descends ici, je peux voir que cette fonction add to cart que j'appelle lorsque je clique sur ce bouton n'est définie nulle part dans ce composant.

Où est définie cette fonction ? Elle est dans le fichier app dot Vue.

Donc si je vais dans mes méthodes, je peux voir que j'ai une méthode Add To Cart juste ici, je dois essentiellement passer cette fonction dans ma page d'accueil pour que ma page d'accueil puisse l'utiliser.

Donc je vais aussi la passer à travers le routeur, comme je l'ai fait avant.

Et puis dans ma page d'accueil, je peux aussi la recevoir comme une prop.

Ajoutez cela à la liste des props, add to cart.

Donc je devrais avoir accès à la fonction que j'ai passée dans ce composant home maintenant à travers le router Vue.

Et laissez-moi rafraîchir et voir si cela fonctionne.

Ajouter au Panier.

Et vous pouvez voir que la fonction fonctionne car la quantité est passée à zéro.

Le panier dit deux articles.

Et si je l'ouvre, il liste effectivement deux articles ici.

Maintenant, pourquoi y a-t-il des barres obliques ici, nous pouvons en fait voir dans la page d'accueil, qu'en JavaScript régulier, cela est en fait dans le composant de la barre latérale, qu'afin de mettre un signe $1 avant la variable, nous devions l'échapper.

Mais nous n'avons pas à le faire dans une application Vue j s.

Parce que ce n'est plus dans un fichier JavaScript régulier.

C'est dans notre template Vue j s.

Donc je peux me débarrasser de tous ces caractères d'échappement.

Et maintenant cela a l'air beaucoup mieux.

Maintenant, si je veux supprimer cela, cela supprime, je n'ai plus d'articles dans le panier, je peux ajouter quelques articles et j'ai des articles dans le panier.

Si je vais à une autre page, le panier devrait toujours fonctionner.

Parce que c'est un composant partagé que je peux voir sur n'importe quelle page.

Dans les applications simples.

Ce type de partage de données fonctionne assez bien, nous pouvons garder toutes nos variables dans un composant parent.

Donc dans ce cas, dans notre composant app dot Vue, nous passons des fonctions et des variables aux enfants.

Et puis les enfants peuvent appeler des fonctions, comme add to cart qui mettra ensuite à jour l'état du composant parent.

Maintenant, dans des applications plus compliquées, nous aurions besoin de quelque chose d'un peu plus robuste pour la gestion d'état, et être capable de partager toutes ces données dans toute notre application.

Et nous en parlerons dans une série future où nous couvrirons Vue x, qui est la bibliothèque de gestion d'état par défaut de Vue j s.

Mais pour l'instant, nous allons laisser l'application telle quelle et travailler dessus dans des séries et leçons futures.

Donc nous avons la page d'accueil, la barre latérale du panier.

Maintenant, nous devons vraiment connecter certaines des informations sur cette page.

Donc la page Produits et c'est vraiment exactement la même chose que la section des produits.

Ici, sur la page d'accueil, nous avons toutes les mêmes cartes et informations.

Donc puisque nous avons la même chose à peu près à plusieurs endroits de l'application, il est logique de sortir toute cette interface utilisateur qui compose ces cartes dans son propre composant.

Et puis nous pouvons le partager dans toute l'application et sur n'importe quelle page que nous voulons.

Donc allons-y et créons un composant de carte.

Maintenant, dans les composants ici, je vais créer un nouveau fichier.

Et je vais l'appeler product card dot Vue.

Je vais commencer avec un template.

Et maintenant je vais aller à ma page d'accueil.

Et je peux voir qu'il y a une boucle for ici qui boucle et affiche toutes les cartes.

Donc je vais prendre toute cette carte ici et la coller dans mon fichier product card.

Maintenant, ce n'est qu'une seule carte.

Donc je n'ai pas besoin d'une boucle for ici.

Laissez-moi me débarrasser de cette logique.

Et ce sera juste une carte.

Maintenant, j'aurai besoin des informations sur le produit pour que cette carte s'affiche correctement.

Donc je vais devoir l'accepter comme une prop dans mon composant.

Donc laissez-moi créer une balise de script.

Je vais créer des props ici, juste un tableau de props.

Et je vais dire, product.

Donc j'accepte la prop product dans mon composant.

Et maintenant je peux l'utiliser dans mon template.

Maintenant, je peux supprimer toute cette logique d'ici.

Et la seule chose dont j'ai besoin est en fait d'importer ce composant.

Donc j'ai besoin d'importer product card de, je vais utiliser mon raccourci de dossier source slash components, et slash product card dot Vue.

Et maintenant je dois l'enregistrer comme un composant pour pouvoir l'utiliser.

Et maintenant dans mon code ici, je vais utiliser product card.

Je vais nettoyer les lignes un peu ici.

Et je dois rendre cela auto-fermant.

Parce que toutes les balises dans les templates Vue doivent soit être auto-fermantes, soit avoir une balise de fermeture.

Maintenant, je n'utilise plus cet index ici, je vais voir dans mon produit, si j'utilise l'index quelque part.

Et je passe effectivement l'index.

Donc je vais devoir accepter l'index comme une prop aussi.

Laissez-moi changer cela en index, c'est un peu plus clair.

Et je vais le passer ici.

Bien sûr, l'index est une variable, pas une chaîne, donc je dois le V bind.

Et cela devrait fonctionner ici.

Voyons si cela fonctionne.

Et nous obtenons une erreur ici.

Maintenant, c'est parce que le produit est maintenant une prop.

Et bien sûr, nous ne pouvons pas muter les props du composant parent.

Donc nous pouvons en fait corriger cela en ne mappant pas à la prop produit du tout, nous allons en fait créer une variable locale à l'intérieur de ce composant produit.

Donc chaque composant, chaque fois que nous utilisons le composant product card, il aura sa propre variable locale.

Et nous pouvons faire cela en ajoutant une prop de données ici.

Et dans la méthode, nous devons retourner un objet.

Et maintenant nous pouvons simplement mapper la quantité car chaque carte n'a qu'une seule boîte de saisie.

Donc nous allons simplement la mapper en interne dans la carte.

Et nous pouvons vérifier que cela fonctionne.

Je ne suis pas sûr de pourquoi il n'y a que deux cartes maintenant.

Mais essayons cela.

Donc j'ai appuyé sur le nombre deux.

Et je peux regarder dans mes outils de développement Vue j.

s. Et j'obtiens une erreur ici.

Et il dit que je ne peux pas lire la propriété name de undefined.

Donc product name.

Oui, je crois que j'ai oublié de passer les props correctes ici.

Donc laissez-moi les ajouter, j'ai besoin de passer product equals product.

Et puis pendant que j'y suis, laissez-moi aussi ajouter la fonction add to cart equals Add To Cart.

Nous y voilà.

Et maintenant, voyons si cela fonctionne.

La page se charge et la page se charge.

D'accord, donc maintenant nous avons toutes les cartes qui se chargent.

Et laissez-moi juste regarder, dans mes outils de développement Vue, je peux voir tous mes composants product card.

Donc laissez-moi juste jeter un coup d'œil.

Si je change cela en deux, et je peux voir que la quantité est de deux.

Si je la change en 22, elle est maintenant de 22.

D'accord, donc cela se mappe correctement.

Maintenant, j'ai besoin d'obtenir cette quantité, la valeur jusqu'à travers le composant home vers le composant app, où je suis en fait en train d'effectuer la fonction d'ajout au panier.

Donc ce que je vais faire, pour l'instant, je vais simplement passer un troisième paramètre, et je vais passer la quantité.

Et maintenant, jetons un coup d'œil à notre fonction, notre fonction Add To Cart dans le composant app.

Donc nous ajoutons des articles au panier, s'ils ne sont pas déjà là.

Et puis nous incrémentons essentiellement le nombre ici.

Donc maintenant que nous avons ce troisième paramètre qui est passé, qui est la quantité, tout ce que nous avons à faire est de changer cette ligne en B plus equals quantity, qui est maintenant passé.

Et puis bien sûr, nous n'avons plus besoin de cette ligne, car nous ne mappons plus à une quantité imbriquée.

Plutôt, nous avons la variable quantité juste ici.

Cela signifie également que nous n'avons plus besoin de passer l'index.

Donc nous pouvons le supprimer de cette fonction.

Nous avons seulement besoin du nom et de la quantité, essentiellement, afin que nous puissions l'ajouter au panier.

Vérifions si cela fonctionne.

Si je viens ici, le nombre se mappe toujours au composant.

Maintenant, si je clique sur Ajouter au panier, il n'est pas dans mon panier.

Voyons si nous avons eu une erreur.

Add to cart n'est pas une fonction.

Laissez-moi regarder à l'intérieur de mon home dot Vue.

J'ai add to cart que je reçois du composant parent.

Donc du composant app, je le passe dans la product card.

Et je devrais l'avoir, oh oui, je ne l'ai pas accepté comme une prop à l'intérieur de la product card.

Donc maintenant, voyons si cela fonctionne.

Laissez-moi rafraîchir et aller dans mes outils de développement Vue.

Et maintenant je peux voir qu'il fonctionne correctement ici.

Si je veux ajouter 10 artichauts, et j'ai deux radis, et j'ai 12 articles dans le panier.

Maintenant, ma fonctionnalité d'arrondi ne fonctionne pas correctement, comme vous pouvez le voir, mais elle ajoute et affiche correctement la quantité et le total dans le panier.

Mais je ne veux pas seulement cette fonctionnalité sur la page d'accueil.

Je la veux aussi sur la page des Produits.

Donc laissez-moi importer ces composants dans la page des Produits maintenant.

Donc si je viens à mon fichier product stock Vue, j'ai en fait accès à l'inventaire déjà ici.

Parce que si vous vous souvenez dans mon app dot Vue, je passe l'inventaire et la fonction add to cart dans tout ce qui est affiché par le router Vue, qui est essentiellement l'une de nos pages ici, home, past orders ou products.

Elles sont toutes connectées à notre routeur.

Donc laissez-moi accepter ces props dans la page des Produits pour commencer.

Tout d'abord, laissez-moi plier toutes ces cartes, les mettre hors de vue.

Donc laissez-moi faire une balise de script, props.

Et je vais accepter l'inventaire et add to cart.

Une chose de plus que je dois faire est d'importer cette product card.

Donc je vais aller dans le composant home, et simplement copier cette importation et la coller dans la page des Produits.

Et maintenant je dois définir cela comme un composant ici.

Product card.

Et cela devrait être des composants, pas un composant.

Et j'ai aussi une autre erreur ici, qui devrait être une majuscule P.

Et maintenant si je surligne cela, tous ceux-ci se mettent en surbrillance, laissez-moi voir quelle est cette erreur ici.

Le composant product card a été enregistré, mais pas utilisé.

Donc corrigeons cela.

Donc j'ai essentiellement toutes ces cartes ici.

Pour les différents articles qui apparaissent sur la page, je vais en fait supprimer tous ceux-ci maintenant.

Et au lieu de cela, je vais ajouter la product card.

Donc si je vais à home, je peux jeter un coup d'œil à ma product card que j'utilise en fait à l'intérieur du template.

Et je vais simplement copier cela et le coller ici.

Mais au lieu de le découper à trois ici, laissez-moi simplement faire les six premiers éléments.

Maintenant, parce que nous avons déjà l'inventaire qui est passé, ainsi que la fonction add to cart, bien sûr, à l'intérieur de la boucle, nous nous occupons de la variable produit, il n'y a vraiment pas d'autre état que nous avons localement sur le composant des produits.

Donc cela devrait fonctionner presque directement pour nous.

Vérifions ici.

Et nous pouvons voir qu'il boucle effectivement et affiche toutes les cartes sur la page des Produits.

Maintenant, laissez-moi ajouter quelques-uns de ces articles au panier ici.

Et vous pouvez voir que le panier vient de se mettre à jour avec cinq.

Si j'ajoute quelques artichauts, ajoutons quelques cerises, et un peu de chou, des carottes.

Tout est correct, nous avons 17 articles dans le panier maintenant.

Et nous pouvons voir qu'il a ajouté tous ces articles.

Maintenant, si je vais à la page d'accueil, je peux toujours voir 17 articles dans le panier.

Parce que nous sommes passés à une application monopage.

Tout notre routage est géré par le JavaScript Vue.

Et nous partageons en fait l'état entre les composants.

Donc tout l'état de notre panier vit dans le composant app, qui est le composant parent de toutes les autres pages, la page d'accueil, la page des produits.

Et c'est pourquoi tous les articles dans le panier, toutes les données que nous sauvegardons ici, dans notre application, elles restent peu importe la page vers laquelle nous naviguons.

Et même si cela est affiché, ou cette carte est sur plusieurs pages, vous pouvez voir comment Vue a rendu cela très facile pour nous de réutiliser le même code et le même template pour boucler et afficher où nous le voulions dans l'application.

Et c'est essentiellement comment les composants réutilisables fonctionnent dans Vue js.

J'espère que vous avez apprécié ce cours.

Et que vous avez appris beaucoup de choses sur Vue js, en l'apprenant à trois niveaux différents à travers ce cours.

Nous avons commencé par travailler dans un simple fichier index dot HTML.

Et puis nous sommes passés à un site statique en le mettant à niveau un peu avec un peu de Vue js.

Et puis nous sommes passés à l'utilisation du Vue COI et à la création d'une application monopage entièrement dynamique que nous avons ici.

N'hésitez pas à me contacter si vous avez des commentaires, des questions ou des suggestions concernant ce cours.

Vous pouvez me trouver sur Twitter et presque partout en ligne en tant que Gwen Faraday ou à Faraday Academy.

Passez une excellente journée et j'espère vous voir dans le prochain cours.