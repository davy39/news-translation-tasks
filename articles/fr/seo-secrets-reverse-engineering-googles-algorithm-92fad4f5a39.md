---
title: 'Les secrets du SEO : L''ingénierie inverse de l''algorithme de Google'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-26T04:01:57.000Z'
originalURL: https://freecodecamp.org/news/seo-secrets-reverse-engineering-googles-algorithm-92fad4f5a39
coverImage: https://cdn-media-1.freecodecamp.org/images/1*534CcgVNnmTtKNiqphMk-w.gif
tags:
- name: Google
  slug: google
- name: marketing
  slug: marketing
- name: SEO
  slug: seo
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: 'Les secrets du SEO : L''ingénierie inverse de l''algorithme de Google'
seo_desc: 'By benjamin bannister

  What have I learned from creating content for the internet? One thing is crystal
  clear: if you want people to discover your work, you need search engine optimization
  (SEO).

  Take this article for example, if you search for “rever...'
---

Par benjamin bannister

Qu'ai-je appris en créant du contenu pour Internet ? Une chose est claire : si vous voulez que les gens découvrent votre travail, vous avez besoin de l'optimisation pour les moteurs de recherche (SEO).

Prenons cet article par exemple, si vous recherchez « [reverse engineer Google](https://www.google.com/search?q=reverse+engineer+Google&oq=reverse+engineer+Google&aqs=chrome..69i57j69i60l3&sourceid=chrome&ie=UTF-8) », « [seo secrets](https://www.google.com/search?q=seo+secrets&oq=seo+secrets&aqs=chrome..69i57j69i60l3&sourceid=chrome&ie=UTF-8) », « [reverse engineering seo](https://www.google.com/search?q=reverse+engineering+seo&oq=reverse+engineering+seo&aqs=chrome..69i57j69i60l3&sourceid=chrome&ie=UTF-8) », cet article est sur la première page pour chacun de ces termes de recherche. Parlons méta.

**Le SEO n'est pas de la magie, c'est savoir ce qu'il faut faire.**

Que vous soyez un novice en SEO ou un praticien expérimenté, je vous encourage à lire cet article en entier pour comprendre comment vous pouvez placer votre contenu en haut des résultats de recherche. Il est conçu comme une base solide pour le SEO. Il y a beaucoup d'essentiels à discuter et à jongler, et je vais distiller les informations en anglais simple.

Rejoignez-moi et plongeons dans l'esprit des programmeurs du moteur de recherche Google et reverse-engineerons comment ils analysent, jugent et classent le contenu. Nous allons faire cela à travers une combinaison d'intuition et de logique, et pas nécessairement d'analyse empirique.

> « L'intuition est une chose très puissante, plus puissante que l'intellect, à mon avis. » — [Steve Jobs](http://www.nytimes.com/2011/10/30/opinion/sunday/steve-jobss-genius.html)

**Tenter de tricher ou de manipuler l'algorithme de Google avec ces informations ne fera que se retourner contre vous**, car en tant qu'ingénieur, c'est ce que je ferais (_moins 30 points pour Serpentard !_).

![Image](https://cdn-media-1.freecodecamp.org/images/E4DqsXYtNeBgkbxyv5KbSnaBvJogvte5F5Ie)
_**Qu'est-ce que le SEO ?** Image : [benjamin bannister](http://www.benjaminbannister.com/" rel="noopener" target="_blank" title=")_

Commençons par une question essentielle : **Qu'est-ce que le SEO ?**

> « Le SEO (Search Engine Optimization) est le processus qui affecte la visibilité d'un site web/page web dans les résultats non payants d'un moteur de recherche. » —[Wikipedia](https://en.wikipedia.org/wiki/Search_engine_optimization)

Traduction : Le SEO est tout ce que vous devez faire pour que votre site web soit bien classé dans les résultats de recherche, sans payer pour cela.

Question suivante : **Quel est l'objectif de Google.com ?**

> **La priorité numéro un de Google est de s'assurer que les résultats d'une recherche sont précis et pertinents.**

> **Plus les utilisateurs sont satisfaits des résultats, plus ils sont susceptibles de revenir et de rester fidèles à** Google**.**

Pensez à Google (Bing, Baidu, Yandex, etc.) comme à des bibliothécaires. Ils catégorisent (indexent) de nombreux livres (sites web) dans des bibliothèques autour du monde (Internet). Leur travail est de trouver le livre exact (pertinent) que vous cherchez. Ils sont très bons dans ce domaine et c'est pourquoi Google est numéro un en matière de recherche.

Pour en arriver là, Google a créé un algorithme complexe (désormais appelé **'L'Algorithme'**), avec des variables top secrètes qui jugent les sites web et les classent en fonction de leur contenu.

Avez-vous déjà recherché quelque chose et trouvé exactement ce que vous vouliez, puis commencé une autre recherche, et avant que vous ne puissiez taper trois lettres, Google a déjà prédit la prochaine chose que vous prévoyiez de rechercher ? C'est le génie de L'Algorithme. Il peut même prédire ce que vous voulez en fonction du contexte que vous avez précédemment recherché !

**Un bon SEO suit les directives _que Google détermine_ comme étant les meilleures pratiques** pour que votre contenu soit classé en haut. À moins que vous ne travailliez chez Google, personne ne sait vraiment quelles sont ces variables. Mais il y a des indices pour extrapoler ce qu'elles pourraient être.

![Image](https://cdn-media-1.freecodecamp.org/images/0WCPAUw2ltMMYS1z8IczhqolWZaCXm-S9GXI)
_**Le contenu de qualité vaut plus que la quantité.** Image : [benjamin bannister](http://www.benjaminbannister.com/" rel="noopener" target="_blank" title=")_

### I. La qualité est reine

On vous a peut-être dit : « Le contenu est roi. » Si vous y réfléchissez, vous pouvez créer autant de contenu que vous voulez, mais cela ne le rend pas automatiquement bon. Non, le vrai mot ici est _qualité_. [La qualité est reine](https://webmasters.googleblog.com/2011/05/more-guidance-on-building-high-quality.html). Ce concept devrait être clair et ancré dans votre esprit, et devrait être la priorité numéro un lors de la création de contenu.

> Que signifie « la qualité est reine » ?

**Le contenu de qualité doit avoir de la _valeur_ pour votre audience.** La valeur peut être beaucoup de choses. Votre contenu fait-il l'une des choses suivantes :

* Informer/enseigner à l'audience (_connaissance_)
* Faire rire/pleurer l'audience (_émotion_)
* Montrer quelque chose de nouveau/différent (_découverte_)

Si votre contenu ne fait pas une ou plusieurs de ces choses, alors pourquoi essayez-vous même ? Commencez par créer quelque chose qui apporte de la valeur, une valeur durable. Pas une page de « déclaration de mission », pas une page « à propos de nous ». Du contenu de qualité. Vous pouvez suivre presque tous les points de cette page à 100 % de précision, mais si la qualité n'y est pas, alors bonne chance à vous.

> Si vous oubliez que le contenu de qualité est une priorité absolue, alors vous pouvez oublier avoir une stratégie SEO.

> _LEÇON D'HISTOIRE : Dans les anciens temps, Internet était jonché de « fermes de contenu ». Ces sites web prenaient du contenu de qualité et les agrégeaient sur leurs propres sites remplis de publicités, dans le but d'obtenir du trafic, de gagner de l'argent et de dominer les classements de recherche (et ils le font encore)._

> _La qualité reste en tête des classements, la seule différence maintenant est que L'Algorithme favorise les créateurs originaux, et leur travail apparaît à juste titre en haut._

**Google aime fournir des résultats de recherche qui ont de la valeur.** Qu'il s'agisse d'une vidéo tutorielle, d'un article drôle ou d'une série de photos incroyable, il est possible de créer quelque chose de qualité qui bénéficie à la ligne de fond de votre marque, et qui bénéficie à votre audience. Gagnant-gagnant.

### IIa. Qui partage ?

Le contenu de qualité mène à la popularité, ce qui mène au partage (également connu sous le nom de lien ou de backlink). **_Qui_ et _combien_ de personnes partagent/lien votre contenu sont des variables SEO :

* _Experts_ : des personnes crédibles et compétentes dans leur domaine
* _Célébrités_ : des célébrités de Hollywood/Musique/Sport (payées ou non)
* _Influenceurs_ : des personnes qui ont un grand nombre de followers
* _Réseaux sociaux_ : les masses de personnes en ligne
* _Pairs_ : vos amis, votre famille et les personnes que vous connaissez

Avoir des personnes qui partagent votre contenu est quelque chose sur lequel vous avez peu de contrôle. Vous pourriez et devriez demander (ou payer) aux personnes ci-dessus de lier/partager, mais la meilleure chose pour L'Algorithme est de le faire partager _organiquement_. Cela signifie **grandir par le bouche-à-oreille**. Et pour cela, vous commencez par du contenu de qualité. (Et un budget marketing aide à répandre la nouvelle.)

> Si Google voit que beaucoup de personnes partagent votre contenu, il le considère comme un QUALITÉ potentielle.

### IIb. Les partageurs sont-ils pertinents pour votre contenu ?

La deuxième partie du partage est : Votre publication est-elle partagée par des sites liés ? Votre vidéo sur « L'avenir du design » est-elle partagée par des designers et des personnes créatives ? Votre article sur « Un remède possible contre le cancer » est-il partagé par des médecins et des institutions établies dans l'industrie médicale ?

> Si Google voit que des sites liés partagent votre contenu, il le considère comme probablement PERTINENT.

> _EXEMPLE : Vous avez un ami connaisseur en nourriture et un ami professeur d'université. Ils recommandent tous les deux le même nouveau restaurant. Vous êtes susceptible d'écouter les deux, mais dont l'avis aura le plus d'impact ? Qui est le plus pertinent ?_

> _LEÇON D'HISTOIRE : Les anciens conseils SEO suggéraient de vous connecter avec des sites web et d'échanger des liens entre vous. Vrai, un grand site légitime qui vous lie peut booster votre classement, mais cela n'aidera pas votre score de pertinence si le contenu lié n'est pas lié au site qui le partage._

Désolé, si votre site parle de chatons et que vous partagez le lien de quelqu'un pour faire du brocoli rôti et vice versa, en tant que Google, je penserais que vous êtes tous les deux en collusion et je déduirais un point de maison pour les deux pour irrelevance.

Évidemment, les personnes et les marques partagent tous types de contenu. Ceux qui ont une véritable identité — qui se connaissent, savent partager des choses qui sont en ligne avec ce qu'ils représentent. **Si vous partagez, gardez-le pertinent.**

![Image](https://cdn-media-1.freecodecamp.org/images/YEgrwoYMAW93hZmp5cjfkYRPNagRosi0WUA8)
_**Liez votre marque à travers les plateformes, mais ne liez pas de contenu vide.** Image : [benjamin bannister](http://www.benjaminbannister.com/" rel="noopener" target="_blank" title=")_

### III. Lier votre marque

Une manière simple de montrer la pertinence _de votre marque_ est par le biais de liens croisés. **Si vous avez des comptes sur plusieurs réseaux et que vous voulez que Google sache qu'ils sont tous liés à vous, liez-les ensemble.**

> _EXEMPLE : Si j'ai un compte YouTube, Twitter et Behance avec le même nom, c'est-à-dire BravoEcho, assurez-vous que votre site principal, BravoEcho.com, a des liens vers vos comptes YouTube, Twitter et Behance. Faites de même pour ces réseaux séparés._

> _Cela permet à Google de savoir que le BravoEcho sur YouTube est le même BravoEcho sur Twitter et Behance. Facilitez la tâche de Google pour qu'il sache que vous êtes la même entité._

J'ai seulement une mise en garde ici : **ne faites pas de liens croisés si vous avez du contenu vide**. Par exemple : Si vous liez votre page Facebook à votre page Twitter, mais que votre profil Twitter n'a aucun tweet, c'est simplement une mauvaise UX (expérience utilisateur). Assurez-vous que vos plateformes ont du contenu si vous les liez.

Le lien croisé est simple et facile à mettre en œuvre. Alors faites-le.

![Image](https://cdn-media-1.freecodecamp.org/images/NsEZTCIII84yJmja8EYG8PSKaQlCFljlUVfc)
_**Choisissez des mots-clés précis dans votre contenu.** Image : [benjamin bannister](http://www.benjaminbannister.com/" rel="noopener" target="_blank" title=")_

### IVa. Les mots-clés sont reine

Les mots-clés, ou termes de recherche, sont ce que Google utilise pour indexer votre site. Bien que les mots-clés n'aient pas le même poids qu'avant, ils sont toujours nécessaires.

Votre choix de mots et de mots-clés sur votre page compte. Chaque. Mot. **Remplir votre page de termes de recherche juste pour le plaisir de la remplir n'est ni impactant ni utile pour Google** (et vous aurez une déduction pour tromperie, et vous savez que je suis pour la déduction de points de maison !).

> _LEÇON D'HISTOIRE : Le « [Keyword stuffing](https://support.google.com/webmasters/answer/66358?hl=en&ref_topic=6001971) » était une pratique où les mots-clés étaient répétés encore et encore ad nauseam sur une page pour tromper les moteurs de recherche en leur faisant croire qu'un site contenant certains mots si souvent devait être sur ces mots-clés. Plus maintenant._

Un ensemble important de mots-clés est **le titre de votre contenu**. Le titre doit accomplir plusieurs objectifs :

* Être concis et _précis_
* Être _intéressant_ pour cliquer dessus
* Avoir des mots qui servent de _termes de recherche_

Ce n'est pas facile d'obtenir cette trifecta. Ne laissez pas ce point vous empêcher d'avoir un bon titre, mais prenez-le en considération. **Utilisez des mots-clés dans votre titre que les gens sont susceptibles de rechercher.**

> _EXEMPLE 1 : J'ai eu une décision difficile pour nommer cet article. J'aurais pu avoir quelque chose de simple et efficace comme « SEO Secrets Everyone Should Know », ou « 9 Powerful and Essential SEO Tips », mais zzzZZZZZ, snooze._

> _J'aurais pu choisir un titre « safe » (clickbait) et être comme tous les autres sites SEO. Mais non, je voulais quelque chose de différent, pas pour être contrariant, mais quelque chose qui représente précisément le contenu. (Et honnêtement, il est vraiment difficile de titrer les choses de nos jours sans sembler clickbaity !)_

En ce qui concerne la longueur, il n'y a pas de règles strictes sur la longueur ou la brièveté d'un titre. **Le titre de votre contenu doit être aussi long qu'il en a besoin** (mais ne le rendez pas trop long).

> _EXEMPLE 2 : Je ne peux pas déduire de points pour un long titre technique s'il a besoin d'un long titre technique. Je ne peux pas déduire de points pour un titre court s'il décrit précisément le contenu._

### IVb. Écrivez une méta description précise

En plus des mots-clés dans votre titre, il y a la balise [**meta _description_**](https://support.google.com/webmasters/answer/79812?hl=en) dans votre code html. Ces balises diffèrent des meta _tags_. Google et la plupart des moteurs de recherche n'utilisent pas les meta tags pour l'indexation (mais ils les utilisent dans certains contextes).

> _LEÇON D'HISTOIRE : Comme le keyword stuffing, les sites web utilisaient pour spammer leur code avec d'innombrables variations des mêmes meta tags encore et encore, par exemple : « iPhone », « best iPhone », « [iPhone X](https://www.youtube.com/watch?v=DgiAHFtvC5I) », etc. Ils faisaient cela même si le contenu n'avait rien à voir avec les iPhones, dans le but que Google pense :_

> « Oh, ce site DOIT être sur les iPhones parce qu'il est mentionné BEAUCOUP dans les tags et le contenu. » Désolé, non. Google a des programmeurs intelligents qui voient cela immédiatement. [Ils n'utilisent pas les meta tags](https://www.youtube.com/watch?v=RBTBEfd7z_Y).

**Écrivez une méta description précise et optimisée.** Cette balise de description permet à Google d'indexer votre page précisément. Elle n'est pas toujours utilisée, mais c'est un facteur. Ne trompez pas ici (_ne le faites pas !_). Si vous tentez de tromper, cela comptera contre vous dans les classements de recherche. Parce que pourquoi ? Parce que c'est ce que je ferais.

![Image](https://cdn-media-1.freecodecamp.org/images/NHz59m94nyCyyJMLTV0vKa9InK9ztCIcYmnW)
_**Utilisez toujours des URLs personnalisées avec des mots-clés.** Image : [benjamin bannister](http://www.benjaminbannister.com/" rel="noopener" target="_blank" title=")_

### IVc. Utilisez des mots-clés dans les URLs personnalisées

L'URL de cet article est : 
https://medium.com/@benjaminbannister/**seo-secrets-and-reverse-engineering-googles-algorithm-92fad4f5a39**

L'URL ci-dessus est parfaitement correcte. Elle utilise les mots-clés principaux du titre pour renforcer le sujet et pour la cohérence. J'ai limité la duplication de cette phrase au titre et à l'URL personnalisée. Plus l'URL est courte, moins elle risque de ressembler à du keyword stuffing, et moins elle risque d'être automatiquement tronquée par certains sites web.

J'aurais un problème si mon lien était : 
https://medium.com/@benjaminbannister/**92fad4f5a39**

Voyez-vous une différence ? Le premier lien décrit clairement le contenu, le second est un lien généré aléatoirement.

> Google ne va pas comprendre ce que sont les chiffres et les lettres incompréhensibles dans votre URL. Rendez cela clair pour eux.

> _ASTUCE : Utilisez un tiret (-) entre les mots lors de la nomination des liens web et des fichiers. Cela aide Google à séparer les mots. Par exemple : website.com/votre-produit-cool.html._

**Pour résumer les mots-clés/meta tags/URLs : Soyez précis, intéressant et recherchable.**

### IVd. Utilisez des mots-clés dans la nomination des images

J'aime inclure des images quand je le peux. La nomination précise et pertinente de vos images renforce votre contenu et devient également indexée dans la recherche d'images de Google.

Chaque fois que je crée des graphiques et que j'enregistre des images, je m'assure que les noms de fichiers font plusieurs choses :

* Identifier la photo
* Avoir un schéma de nomination cohérent
* Avoir des mots-clés

Comme pour la nomination du titre de votre contenu, **deux choses comptent dans les photos : le nom du fichier et la légende que vous lui donnez (ou le texte qui l'entoure).**

> _EXEMPLE : Si je prenais une photo de Diamond Head à Hawaï, je la nommerais probablement « diamond-head-hawaii-benjamin-bannister.jpg ». Je pourrais aussi ajouter les mots « volcanic-tuff-cone » dedans, mais cela pourrait être considéré comme du keyword stuffing. Je peux ajouter cela comme légende à la place._

> _J'inclus personnellement mon nom si je crée un graphique. Cependant, si cela rend le nom du fichier trop long, je l'enlève._

Encore une fois, la pertinence est la clé. **Il est important que le nom du fichier et la légende/le texte environnant représentent précisément l'image.**

> _NOTE : Si vous publiez sur d'autres sites, ils peuvent renommer automatiquement vos images. Ne laissez pas cela vous déranger. Continuez à nommer les fichiers avec cohérence._

### V. La profondeur et la concision de votre contenu comptent

Les jours où vous pouviez écrire un article de 300 mots, y ajouter quelques liens vers d'autres contenus populaires et vous retrouver en haut des classements sont révolus. Google considère cela comme du « **contenu mince** ». Vous les reconnaissez probablement lorsque vous les rencontrez car ils vous laissent en vouloir plus. Maintenant, plus de points sont attribués au contenu qui a de la substance.

> Je veux un morceau de viande épais, juteux et saignant à mâcher, avec très peu de gras. C'était une métaphore.

Cela ne signifie pas que tout doit être épique en longueur. **Google veut des pages qui donnent aux gens exactement ce qu'ils veulent, pas des pages qui sont plus longues que nécessaire ou qui ralentissent l'expérience utilisateur.**

> _EXEMPLE 1 : Si quelqu'un recherche la définition d'un terme technique, ne passez pas trois paragraphes à divaguer avant de le définir. Définissez le mot. Vous pouvez ajouter des mots liés et des exemples de contexte, mais cette définition de mot devrait être la première chose qu'un utilisateur voit._

> _EXEMPLE 2 : Si quelqu'un recherche « comment rempoter une plante », je m'attendrais à ce que les articles classés sur la première page soient tous concis, avec suffisamment de profondeur pour donner les réponses que vous cherchez._

Si vous écrivez des articles, lisez et relisez et apprenez à supprimer les mots et phrases inutiles. Si vous faites des vidéos, coupez les « euh » et les « hum », et _allez droit au but_. Ne perdez pas le temps des gens avec des remplissages inutiles ; personne n'a de temps pour ça. Chaque créateur aime son travail, mais il devrait savoir quand s'éditer.

**Les gens ne veulent pas de restes ou de gras, donnez-leur un délicieux steak maigre ou un dessert riche en une bouchée**, selon ce qui convient le mieux à votre contenu.

### VI. L'UX (expérience utilisateur) est un facteur

Un site bien conçu, intuitif et facile à utiliser, obtiendra des points pour être bien fait. Si vous avez une navigation confuse, des liens qui mènent à des pages cassées/manquantes, une navigation qui nécessite plus de clics que nécessaire, cela signifie que vous ne l'entretenez pas ou que vous n'avez pas engagé un architecte web approprié.

L'UX est un sujet très approfondi en soi. Pour le garder simple, **avoir un site web avec une excellente UX, c'est comme avoir une chaise ergonomique. Assurez-vous que votre chaise est confortable et naturelle à utiliser.** _Je ne devrais pas avoir à réfléchir à la façon d'utiliser votre chaise._

Une UX fantastique sur un ordinateur devrait être similaire : agréable à regarder et intuitive à utiliser. Si vous ne pouvez pas plonger dans un nouveau système et comprendre les choses comme ça (claque des doigts), alors les concepteurs n'ont pas fait un bon travail avec l'UX.

### VII. Limitez les publicités et leurs placements

Une autre partie d'une bonne UX est de _ne pas_ être inondé de publicités sur une page. Oui, les entreprises et les sites web doivent gagner de l'argent, et ils en gagnent une partie avec les publicités. C'est un mal nécessaire.

Cependant, lorsque vous **positionnez** vos publicités entre votre contenu, cela fait deux choses : cela confond l'audience en lui faisant croire que la publicité fait partie du contenu ; et cela les énerve (et la fidélité à la marque commence à s'envoler par la fenêtre).

> _NOTE : On pourrait débattre du placement de publicités qui ressemblent à du contenu pour de bonnes esthétiques de design. C'est bien, dans une certaine mesure. Mais lorsque vous insérez des publicités entre du contenu écrit pour qu'elles semblent en faire partie, ou que vous avez une énorme bannière publicitaire graphique indistincte du contenu réel, vous essayez de tromper. Comment Google saurait-il la différence ? Google sait._

Ensuite, il y a le péché d'avoir **trop** de publicités sur votre site où la question devient : « est-ce une page de contenu, ou une page de publicités ? » **Il y a une ligne fine à marcher entre donner à une audience un bon contenu, tout en gagnant assez d'argent pour faire tourner votre entreprise.**

Et enfin, nous avons le **ratio de publicités par rapport au contenu**. Cinq publicités pour un paragraphe de contenu ? (GTFO, moins 15 points.) Une publicité pour un paragraphe ? Vous allez bien. Envisagez de coder des publicités qui sont _responsives_ (s'ajustent automatiquement) à la quantité de contenu. Gardez votre ratio de publicités sous contrôle.

Et surtout, ne lancez pas automatiquement des publicités vidéo sur une page (_moins 10 points, Serdaigle_). C'est tout.

### VIII. Le premier à publier gagne

Google est devenu intelligent face à [ceux qui copient et collent du contenu populaire](https://support.google.com/webmasters/answer/2721312?hl=en&ref_topic=6001971) (généralement sans permission), sur leurs propres sites dans l'espoir d'obtenir du trafic et des revenus publicitaires (moins cent points dans la vie si vous faites cela). Bien sûr, vous obtiendrez votre argent AdSense, mais vous ne serez pas classé plus haut dans les résultats.

Si vous créez quelque chose qui obtient 1 million de vues, tandis que quelqu'un d'autre le partage et obtient 20 millions de vues (parce qu'ils sont une plateforme plus grande), le vôtre sera toujours classé en premier parce que :

> Google sait qui l'a posté _en premier._

Heureusement pour les horodatages. **La personne qui l'a posté en premier est considérée comme la source originale**, et sera à son tour classée plus haut. Toute autre personne ayant le même contenu est considérée comme quelqu'un qui l'a copié ou partagé, peu importe leurs chiffres. Le fait d'être le premier peut ne pas entrer en vigueur immédiatement, mais L'Algorithme se corrige au fil du temps et à mesure que plus de données sont collectées.

> _EXEMPLE : J'ai écrit « [Why Typography Matters — Especially At The Oscars](https://medium.freecodecamp.com/why-typography-matters-especially-at-the-oscars-f7b00e202f22) », qui a reçu des millions de vues et a été republié sur de grandes plateformes comme [Vox](http://www.vox.com/first-person/2017/3/1/14777110/typography-oscars-2017), [Good](https://www.good.is/articles/oscars-mistake-typography), et même partagé par [George Takei](https://www.facebook.com/georgehtakei/posts/1910923148937129), mais mon article original sur Medium est classé en premier lorsque vous recherchez « [typography oscars](https://www.google.com/search?q=typography+oscars&ie=utf-8&oe=utf-8). » (Premier !)_

Si vous prévoyez de publier le même contenu sur plusieurs plateformes, assurez-vous de publier sur le site principal où vous voulez que votre audience aille, puis publiez sur le reste. Ne vous inquiétez pas trop des gens qui copient votre contenu, L'Algorithme triera la hiérarchie appropriée. (De plus, si les gens ne volent pas votre contenu, il n'est pas assez bon pour être volé.)

> _EXEMPLE : Vous avez une série de photos de personnages Disney en tant que (insérer un nom), et vous la publiez sur Behance, Tumblr et DeviantArt, dans cet ordre. C'est probablement l'ordre dans lequel Google les classera avec le temps._

### IX. Produisez du contenu de manière constante

**Créez continuellement.** Cela n'a pas besoin d'être tous les jours, mais assez pour donner à votre audience un flux régulier de vous et de votre marque. **Google veut du contenu frais en haut.** Pensez à cela comme un supermarché mettant du nouveau lait derrière les anciens. Faites savoir aux gens que vous produisez continuellement du lait et qu'il est frais.

> _EXEMPLE : Si vous avez écrit sur « Les meilleurs ordinateurs portables de 2016 ». Devinez quoi ? « Les meilleurs ordinateurs portables de 2017 » seront classés au-dessus de vous._

Pour moi, j'essaie de créer un contenu riche et de qualité au moins 1 à 2 fois par mois. Pour vous, ce nombre peut être différent.

En tant que perfectionniste en rétablissement, je vous exhorte à simplement publier vos créations. Cela n'a pas besoin d'être parfait, et sur la plupart des plateformes (sauf pour la vidéo), vous pouvez faire un George Lucas et continuer à éditer et à affiner (comme je le fais).

Si vous mettez toujours à jour votre blog ou votre site avec un contenu bien recherché et approfondi, vous devriez vous attendre à des classements améliorés. Les sites qui publient de manière sporadique peuvent s'attendre à la même irrégularité dans leur positionnement.

**Produisez un flux régulier de contenu frais.** Une fois que vous êtes sur un calendrier régulier, il sera plus facile à maintenir.

![Image](https://cdn-media-1.freecodecamp.org/images/bmohd1oupNdkivkd2fC9AB6cVVD202N00ZsI)
_**Analyse des couches de l'algorithme de Google.** Image : [benjamin bannister](http://www.benjaminbannister.com/" rel="noopener" target="_blank" title=")_

### En résumé...

Les principales variables pour un SEO puissant se résument à :

**Qualité et profondeur du contenu**  
**+**  
**Liens/partages de sites liés**  
**+**  
**Popularité**  
**+**  
**Mots-clés précis dans le contenu, les meta tags, l'URL**  
**+**  
**Être la source originale**  
**+**  
**Ratio publicités-contenu**  
**+**  
**Bonne UI et UX du site web**  
**+**  
**Flux régulier de contenu produit**

> Google cherche à fournir un contenu de qualité qui répond aux requêtes des utilisateurs. Un contenu qui est lié et sourcé par de nombreux sites crédibles renforce son autorité sur le sujet. Et un contenu qui est correctement mot-clé dans les bons endroits le rendra indexable pour les moteurs de recherche.

Google n'a pas de temps pour les livres (sites web) qui disent une chose sur la couverture (code), mais finissent par être autre chose (non pertinent). **Ne trompez pas Google.** ([Voici une liste de choses que vous _ne devriez pas_ faire](https://support.google.com/webmasters/topic/6001971?hl=en&ref_topic=6001981).) Vous ne voulez pas être sur leur liste noire, ce qui signifie essentiellement que vous n'existez pas.

Les points ci-dessus sont les variables les plus importantes pour l'optimisation des moteurs de recherche. Certains sont sous votre contrôle, d'autres non. Si vous réussissez sur tous les points, vous n'aurez pas à vous soucier de savoir si votre contenu apparaîtra en haut des listes, il devrait y arriver par lui-même, organiquement (et encore une fois, un budget marketing aide).

Peu importe combien de fois Google ajuste ou fait évoluer L'Algorithme, de [Panda](https://googleblog.blogspot.com/2011/02/finding-more-high-quality-sites-in.html) à [Penguin](https://webmasters.googleblog.com/2016/09/penguin-is-now-part-of-our-core.html) à Polar Bear, ces conseils SEO de base logiques et intuitifs devraient rester intemporels.

Pour en apprendre encore plus sur le SEO, consultez ces trois liens officiels de Google :

[https://www.google.com/webmasters/docs/search-engine-optimization-starter-guide.pdf](https://www.google.com/webmasters/docs/search-engine-optimization-starter-guide.pdf)

[**Comment fonctionne la recherche Google | Algorithmes de recherche**](https://www.google.com/search/howsearchworks/algorithms/)  
[_De l'analyse des mots dans votre terme de recherche à la prise en compte de facteurs comme votre localisation, voyez comment les algorithmes de recherche Google..._www.google.com](https://www.google.com/search/howsearchworks/algorithms/)[**Blog officiel du Google Webmaster Central**](https://webmasters.googleblog.com/)  
[_Blog sur les moteurs de recherche (et le SEO) avec des conseils et des annonces pour connecter votre site web ou votre application avec les utilisateurs de Google Search et..._webmasters.googleblog.com](https://webmasters.googleblog.com/)

Qu'en pensez-vous ? Êtes-vous d'accord ou pas ? Ai-je manqué quelque chose qui devrait être essentiel en matière de SEO ? **Ajoutez votre voix dans les commentaires.**

> Montrez votre soutien en applaudissant cet article, en le tweettant, en le partageant, et suivez-moi pour découvrir de nouvelles choses.

![Image](https://cdn-media-1.freecodecamp.org/images/T0RqMEMTsBOUCB79LXTjp5jrhS51SFVt4LRX)
_[**benjaminbannister.com**](http://www.benjaminbannister.com/" rel="noopener" target="_blank" title=")_

**Aussi par benjamin bannister :**

* [L'avenir de l'iPhone X : Du réaliste à l'absurde](https://medium.com/@benjaminbannister/the-future-of-the-iphone-x-from-the-realistic-to-the-absurd-f33bee3288ea)
* [À quoi ressemblerait un Apple MacPad Pro ?](https://medium.com/@benjaminbannister/macpad-pro-two-worlds-united-a8c6f4c51eb3)
* [Pourquoi la typographie compte — surtout aux Oscars](https://medium.freecodecamp.com/why-typography-matters-especially-at-the-oscars-f7b00e202f22)