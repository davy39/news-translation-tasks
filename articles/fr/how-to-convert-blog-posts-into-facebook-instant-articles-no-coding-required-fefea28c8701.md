---
title: Comment convertir des articles de blog en articles instantanés Facebook — aucun
  codage requis
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-29T14:20:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-blog-posts-into-facebook-instant-articles-no-coding-required-fefea28c8701
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KILZRpvD0Ew9jU3NuZ_FnQ.png
tags:
- name: Facebook
  slug: facebook
- name: social media
  slug: social-media
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: writing
  slug: writing
seo_title: Comment convertir des articles de blog en articles instantanés Facebook
  — aucun codage requis
seo_desc: 'By Nicholas Walsh

  A friend of mine asked me to help convert articles that were previously posted to
  their site into Facebook Instant Articles. Afterwards, I decided to compile a guide
  to help nontechnical people convert their old articles, blog posts...'
---

Par Nicholas Walsh

Un ami m'a demandé de l'aider à convertir des articles précédemment publiés sur leur site en articles instantanés Facebook. Ensuite, j'ai décidé de compiler un guide pour aider les personnes non techniques à convertir leurs anciens articles, publications de blog ou contenu en ligne.

Même si vous ne savez pas ce que sont les articles instantanés Facebook, vous les utilisez peut-être déjà. Selon la page [FAQ](https://developers.facebook.com/docs/instant-articles/faq#FAQ-basics) de Facebook IA :

> « Les articles instantanés sont un format de publication mobile qui permet aux éditeurs de nouvelles de distribuer des articles à l'application Facebook qui se chargent et s'affichent jusqu'à 10 fois plus rapidement que le web mobile standard. »

Les IA dictent une norme de publication de contenu qui résulte à la fois en un design agréable et en une performance optimisée pour les articles ouverts depuis l'application mobile Facebook. Vous pouvez en savoir plus sur les [avantages](https://contently.com/strategist/2015/05/13/7-things-you-need-to-know-about-facebook-instant-articles/) des IA.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6YgOYg7b5kWoEAHSlmxT1Q.jpeg)

Facebook offre une multitude de moyens pour accélérer la production et la conversion des IA. Pourtant, il semble que les guides actuels soient destinés aux développeurs ou aux grandes entreprises qui disposent d'un écosystème de publication plus complexe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SNzwqk3Mi1jyvycLcKutUA.jpeg)

Il est difficile de trouver des guides pour convertir des articles précédemment publiés qui n'impliquent pas l'utilisation de l'API Facebook IA, du SDK PHP ou du plugin [WordPress](https://media.fb.com/2016/03/07/instant-articles-wordpress-plugin/). Pour les non-développeurs, la plupart de ces outils nécessitent trop d'expérience technique. Même lorsque l'on essaie de trouver le tutoriel du plugin WordPress, il faut creuser dans la documentation du portail des développeurs de Facebook. Ce n'est pas idéal pour les non-développeurs qui se découragent avant de pouvoir trouver cette page.

Travaillons ensemble pour convertir n'importe quel article déjà publié sur le web en un article instantané Facebook ! Pour notre tutoriel, nous utiliserons l'article sur un chien célèbre du film « [Anchorman](https://www.theatlantic.com/entertainment/archive/2013/12/15-minutes-life-celebrity-dog-baxter-anchorman/356235/) ».

### C'est parti !

**Étape 0 : Préparation**

Nous n'aurons pas besoin d'installer de plugins ou d'intégrations, mais nous aurons besoin d'un éditeur de texte pour travailler avec le code source HTML. Il existe de nombreux éditeurs de texte orientés code, mais pour simplifier cet exemple, je recommande [**Sublime**](https://www.sublimetext.com/). Il possède toutes les fonctionnalités dont nous aurons besoin et est facile à utiliser dès l'installation.

Une fois que vous avez installé Sublime, nous allons vouloir télécharger le modèle de code [template](https://gist.github.com/nmwalsh/e67c8474b038a5286c95d15e2ad82285#file-template-html) que nous utiliserons depuis GitHubGist.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dv4DscHL7Tj7lPseAyHTAQ.png)

```
Sur le côté droit de l'écran : 1. Cliquez avec le bouton droit sur le bouton "Raw"2. Cliquez sur "Enregistrer le lien sous..." Par défaut, il devrait s'enregistrer en tant que fichier HTML avec le nom "template".
```

Maintenant, nous avons l'éditeur de code et le modèle de code que nous allons modifier !

```
Pour la dernière étape de la configuration :1. Lancez Sublime2. Ouvrez le fichier modèle que nous avons téléchargé
```

#### Étape 1 : Obtenir l'image de la bannière

Retournez à votre navigateur internet et trouvez l'article que vous souhaitez convertir sur son site en direct. Nous allons d'abord récupérer l'**image de la bannière**, que nous utiliserons en haut de l'article instantané Facebook.

Pour ce faire, cliquez avec le bouton droit sur l'image et sélectionnez _"Copier l'adresse de l'image"_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*28BtD-UWNCtTxNGvtjnoTw.png)

Revenez au modèle que nous avons ouvert dans Sublime. Recherchez la balise <figure> dans le code, située à la ligne 35 (le numéro de ligne est visible sur le bord gauche).

```
Surlignez l'URL originale située entre les guillemets à la ligne 36, et remplacez-la en collant l'adresse de l'image que nous avons copiée depuis l'image de la bannière. Assurez-vous qu'il y a des guillemets doubles de chaque côté de l'URL pour préserver le format. Et assurez-vous de ne pas supprimer le " />" à la fin de la ligne.
```

```
Modifiez le texte à l'intérieur de <figcaption> </figcaption> avec la légende que vous souhaitez voir apparaître sous l'image. C'est souvent là que va l'attribution de l'image.
```

Remarquez comment nous sommes prudents de ne pas changer le formatage du code. Jouer avec les balises elles-mêmes causera des erreurs plus tard lorsque nous essaierons de rendre le site web. Sublime colorise notre code, ce qui nous aide à reconnaître les erreurs ou les balises HTML non correspondantes.

Faites très attention à la façon dont nous avons remplacé le texte pour la légende de la figure. Nous allons modifier beaucoup d'autres valeurs de la même manière.

#### Étape 2 : Récupération des métadonnées

Il y a quelques informations que nous devons collecter maintenant. Comme la plupart de ces données devraient être récupérables sans creuser dans le code source, copier manuellement ces informations fonctionne bien. Cependant, nous aurons besoin de ce code source plus tard, donc il n'y a aucun mal à l'ouvrir maintenant.

* URL de l'article original
* Titre de l'article
* Sous-titre de l'article
* Auteur(s) de l'article
* Date et heure de la publication originale de l'article
* Date et heure de la dernière mise à jour de l'article

Si c'est difficile d'obtenir ces informations, nous pouvons utiliser le code source du site web. La façon dont vous accédez à ces données dépendra du navigateur que vous utilisez.

```
Chrome : CTRL + U, ou Clic droit → Afficher le code source de la pageFirefox : Clic droit → Afficher le code source de la pageSafari : Menu Safari → Préférences → Avancé, Activer "Afficher le menu Développeur dans la barre de menus", puis Menu Développeur → Afficher le code source de la page
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*mgIdjQwtEYQTFGYMCXwApQ.png)
_Le code source devrait ressembler à ceci_

Maintenant que nous avons le code source et le site web original ouvert, commençons à chercher nos informations.

**Titre :** Copiez le titre de l'article et utilisez-le pour remplacer « Article Title » dans les balises <h1> </h1> à la ligne 14 du modèle. Dans le code source, cela se trouve généralement dans les balises <title> </title>. Par exemple,

```
<h1>Article Title</h1>
```

```
devient
```

```
<h1>15 Minutes in the Life of Celebrity Dog Baxter from 'Anchorman'</h1>
```

**Sous-titre :** Même chose que ci-dessus, mais avec le sous-titre. Utilisez-le pour remplacer « Article Subtitle » dans les balises <h2> </h2> à la ligne 15 du modèle.

**URL :** Copiez l'URL de l'article du site web en direct. Utilisez-le pour remplacer l'URL qui apparaît à la ligne 7 du modèle. Par exemple :

```
<link rel="canonical" href="http://example.com/article.html">
```

```
devient...
```

```
<link rel="canonical" href="https://www.theatlantic.com/entertainment/archive/2013/12/15-minutes-life-celebrity-dog-baxter-anchorman/356235/">
```

**Heure de publication :** À la ligne 18 du modèle, vous pouvez indiquer la date et l'heure de la publication originale de l'article. Soyez attentif au fait que le paramètre « datetime » prend un format très spécifique. Les données à l'intérieur de **datetime=""** déterminent les métadonnées (non affichées), tandis que le texte entre les balises **> </time>** dictera quelle date est affichée (peut être dans n'importe quel format ici).

```
Par exemple, <time class="op-published" datetime="2014-11-11T04:44:16Z">November 11th, 4:44 PM</time>
```

```
S'affiche comme : November 11th, 4:44 PMChangeons-le en : July 24th, 2017. 6:30 PM
```

```
<time class="op-published" datetime="2017-7-24T06:30:16Z">July 24th, 2017. 6:30 PM</time>
```

```
Heure de la dernière mise à jour : Même plan que ci-dessus, mais à la ligne 21 du modèle.
```

**Auteur(s) :** Les lignes 24-27 du modèle représentent un auteur dont le nom est lié à un site web. Les lignes 28-31 représentent un auteur dont le nom n'est pas lié. Vous pouvez copier l'ensemble du bloc de code pour cet auteur respectif et le coller consécutivement au bloc précédent, puis le modifier si nécessaire. Vous pouvez également faire cela pour plusieurs auteurs. Voir l'exemple ci-dessous pour plusieurs auteurs avec des noms simples + légendes.

#### Étape 3 : Copier le contenu du corps

Maintenant, nous allons récupérer le contenu de l'article que nous voulons convertir. Il existe une large gamme de types de contenu, tels que les médias mixtes, le JavaScript avancé, le contenu intégré. Avec un contenu plus compliqué, le risque est plus élevé que les choses ne fonctionnent pas sans dépannage, donc votre expérience peut varier.

Je vais expliquer comment travailler avec du texte, des images (statiques ou gifs) et des vidéos, car ce sont les bases de la plupart des articles instantanés que j'ai vus.

Le code source est probablement de centaines (voire de milliers) de lignes. Une astuce facile pour trouver le début du contenu du corps est de faire une recherche des premiers mots du texte du corps de l'article. Nous voulons copier à partir de la balise <p> au début de notre texte de corps jusqu'à (et y compris) la balise </p> qui suit les mots de clôture de l'article.

Ensuite, nous allons devoir coller cela dans notre modèle. Près de la ligne 58 dans le modèle, il devrait y avoir une ligne avec ce qui suit :

```
<p> Article content </p>
```

Surlignez cette ligne entière et collez le contenu du corps que nous avons copié depuis le code source de l'article en direct. Remarque : nous avons copié les balises d'ouverture <p> et de fermeture </p> depuis le code source, c'est pourquoi nous les collons ici dans le modèle. Il y a du code à l'intérieur d'un autre ensemble de balises <p></p> suivant le texte du corps, mais c'est du style — faites attention à ne pas copier cela avec votre texte de corps.

*Avez-vous une vidéo que vous aimeriez incorporer dans votre IA ? Changez l'URL entre les balises <video> et </video> commençant autour de la ligne 64, comme nous l'avons fait avec l'URL de l'image de la bannière à l'étape 1.

**Notes légales :** Ligne 84. Ce texte sera très petit et à la toute fin de votre article.

#### Étape 4 : Clochettes et sifflets (Publicités, Suiveurs d'analyse, et plus)

**Je recommande de sauter cette étape pour l'instant.** Si vous souhaitez confirmer que ce que nous avons fait jusqu'à présent fonctionne, ou si vous n'avez pas de publicités ou de suiveurs personnalisés, passez à l'étape 5.

L'une des meilleures choses à propos des articles instantanés Facebook, par rapport à d'autres outils de conversion d'articles propriétaires, est que vous pouvez conserver les suiveurs d'analyse personnalisés et les publicités que vous utilisez déjà sur votre propre site.

Chaque intégration personnalisée sera différente et variera probablement en difficulté. Pour cet exemple, nous utiliserons [ChartBeat](https://chartbeat.com/), un outil d'analyse et de suivi du trafic. Nous pouvons utiliser une recherche rapide sur Google pour « ChartBeat Documentation », afin de trouver le [Guide de démarrage](http://support.chartbeat.com/docs/).

Les pages de documentation de certaines entreprises peuvent être destinées aux développeurs. Si cela ne fonctionne pas pour vous, recherchez un tutoriel à la place.

ChartBeat nous donne tout le code et les instructions pour ajouter leur intégration.

Dans le guide, il nous dit ce qui suit, donc c'est ce que nous ferons :

```
Insérez ce script juste avant la balise de fermeture </body> :
```

Maintenant que nous avons ajouté notre suiveur ChartBeat, nous devons apporter quelques modifications rapides pour que le suiveur sache comment se synchroniser avec notre compte ChartBeat.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Il0_cROfPT6hQZtBbdmkdQ.png)
_Code du snippet ChartBeat que nous devons personnaliser_

Chaque ligne surlignée (sauf la ligne « .useCanonical ») devra être modifiée pour qu'elle puisse enregistrer les données.

```
MODIFICATIONS (à droite du "=").uid - L'ID unique de votre compte ChartBeat.domain - Le domaine complet de l'article original.sections - Le nom de la 'section/genre/étiquettes' à laquelle votre article appartient.authors - Le nom de l'auteur à associer à cet article
```

Bingo ! Vous avez ajouté le suiveur et il associera les données qu'il envoie à votre compte ChartBeat unique. Enregistrez votre fichier de modèle modifié et préparons-nous à publier.

#### Étape 5 : Déployer votre article instantané

Sur Facebook, allez au tableau de bord de la page que vous gérez et depuis laquelle vous souhaitez publier. Accédez aux outils de publication, puis à la liste des articles. Cliquez sur le bouton bleu "+Créer" en haut à droite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2b43jAg0QkdNaoyRMMqwwA.png)
_Tableau de bord IA_

Vous devriez maintenant être invité à coller le code de votre nouvel article.

Sélectionnez tout le code du modèle que nous avons modifié et collez-le ici. Cliquez sur enregistrer ! Vous pouvez publier ce brouillon lorsque vous le souhaitez, ou le programmer pour qu'il soit publié à une heure prédéterminée en utilisant le tableau de bord.

#### Félicitations, vous avez terminé ! Je suis impatient de lire les articles géniaux que vous allez publier.

![Image](https://cdn-media-1.freecodecamp.org/images/0*0dsNUILlWp9u8hCF.gif)

Hey, je suis [**Nick Walsh**](http://twitter.com/thenickwalsh).

Je suis un évangéliste technique pour [Wolfram Research](http://wolfram.com) et un entraîneur de hackathon pour [Major League Hacking](http://mlh.io), avec une passion pour la technologie, les eSports et l'autonomisation des développeurs étudiants.