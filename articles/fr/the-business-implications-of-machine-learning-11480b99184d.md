---
title: Les implications commerciales de l'apprentissage automatique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-23T01:23:29.000Z'
originalURL: https://freecodecamp.org/news/the-business-implications-of-machine-learning-11480b99184d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gIhT3qj9QU3G7YjaphRxdQ.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: business
  slug: business
- name: Machine Learning
  slug: machine-learning
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Les implications commerciales de l'apprentissage automatique
seo_desc: 'By Drew Breunig

  It’s not about what it can do, but the effects of its prioritization

  As buzzwords become ubiquitous they become easier to tune out.

  We’ve finely honed this defense mechanism, for good purpose. It’s better to focus
  on what’s in front o...'
---

Par Drew Breunig

#### Ce n'est pas ce qu'il peut faire, mais les effets de sa priorisation

À mesure que les mots à la mode deviennent omniprésents, ils deviennent plus faciles à ignorer.

Nous avons affiné ce mécanisme de défense, à juste titre. Il est préférable de se concentrer sur ce qui est devant nous plutôt que sur la tendance du moment. [CRISPR pourrait changer nos vies](http://www.bbc.com/news/health-36439260), mais savoir comment cela fonctionne ne vous aide pas. La VR pourrait engloutir tous les médias, mais ses [exigences matérielles la maintiennent éloignée](http://www.engadget.com/2016/05/31/amds-radeon-rx480-gpu-is-vr-ready-for-just-199/) de l'usage courant pendant de nombreuses années.

Mais s'il vous plaît : **ne ignorez pas l'apprentissage automatique**.

Oui, l'apprentissage automatique nous aidera à construire des applications merveilleuses. Mais ce n'est pas pour cela que je pense que vous devriez y prêter attention.

Vous devriez prêter attention à l'apprentissage automatique parce qu'il a été priorisé par les entreprises qui pilotent l'industrie technologique, à savoir Google, Facebook et Amazon. La nature de l'apprentissage automatique — comment il fonctionne, ce qui le rend efficace, et comment il est livré — garantit que cette priorisation stratégique changera significativement l'industrie technologique avant même qu'une fraction de la valeur de l'apprentissage automatique ne soit libérée.

Pour comprendre l'impact de l'apprentissage automatique, explorons d'abord sa nature.

(Je vais utiliser les termes "deep learning" et "machine learning" de manière interchangeable. Pardonnez-moi, les geeks.)

#### L'apprentissage automatique rend tout programmatique

Le but de l'apprentissage automatique, ou du deep learning, est de rendre tout programmatique. [Comme je l'ai écrit en janvier](https://medium.com/@dbreunig/discussions-we-will-have-in-2016-abc1e1d1c4e6#.owe1fdwzn) :

> En résumé, le deep learning est la reconnaissance humaine à l'échelle de l'ordinateur. La première étape pour créer un algorithme est de fournir à un programme une grande quantité de données organisées par des humains, comme des photos étiquetées. Le programme analyse ensuite les éléments des données brutes et note les motifs qui corréleront avec les données organisées par les humains. Le programme recherche ensuite ces motifs connus dans la nature. C'est ainsi que Facebook suggère des amis à étiqueter dans les photos et que Google Photos recherche des personnes.

> Jusqu'à présent, la plupart des applications de deep learning que les gens utilisent sont essentiellement des jouets : [des albums photo plus intelligents](http://www.theverge.com/a/sundars-google/google-photos-google-io-2015) et [une meilleure reconnaissance vocale](http://www.androidheadlines.com/2015/08/google-turns-to-deep-learning-to-fix-speech-recognition.html). Ces premières applications sont indulgentes. Si un algorithme d'apprentissage manque un visage ou vous force à éditer un mot délicat, ce n'est pas grave ([habituellement](http://mashable.com/2015/07/01/google-photos-black-people-gorillas/#Ghnc81lHCGql)). Mais à mesure que notre investissement continue et que ces algorithmes deviennent plus fiables, nous les verrons déployés dans des environnements plus intéressants, avec des cas d'utilisation plus intéressants.

Le point à retenir ici est que l'apprentissage automatique permet aux entreprises de construire de meilleures applications qui interagissent avec les choses que les gens créent : des images, de la parole, du texte et d'autres _choses désordonnées_. Cela permet aux entreprises de créer des logiciels qui nous comprennent. Le potentiel est là pour résoudre les problèmes d'interface utilisateur qui ont empêché les gens de calculer depuis [l'Eniac](https://en.wikipedia.org/wiki/ENIAC). Et les avancées majeures en matière d'UI tendent à lancer de grandes ères de l'informatique.

La souris et les interfaces graphiques ont rendu les ordinateurs accessibles, des objets domestiques.

Les interfaces tactiles ont rendu les ordinateurs normaux, des outils du quotidien.

Les interfaces alimentées par l'apprentissage automatique rendront l'informatique omniprésente. (Éventuellement)

Mais il y a un hic :

![Image](https://cdn-media-1.freecodecamp.org/images/V7SQGItxe3GLH3a58Ftw3tr3PS3rpTLvTQ22)
_Quelqu'un a dû classer tout cela._

#### L'apprentissage automatique n'est aussi bon que ses données d'entraînement

Pour créer un modèle d'apprentissage automatique, vous avez besoin de trois choses, par ordre d'importance :

1. **Données d'entraînement** : Des données qui ont été étiquetées, catégorisées ou autrement triées par des humains.
2. **Logiciel** : La bibliothèque logicielle qui construit les modèles d'apprentissage automatique en évaluant les données d'entraînement.
3. **Matériel** : Les CPU et GPU qui exécutent les calculs du logiciel.

Le matériel est assez facile à acquérir. [Louez-le](https://aws.amazon.com), [achetez-le](https://azure.microsoft.com/en-us/), peu importe.

Le logiciel est encore plus facile à acquérir ! Si vous avez loué, vous avez peut-être accidentellement [déjà fait](https://aws.amazon.com/machine-learning/) [cela](https://azure.microsoft.com/en-us/services/machine-learning/). Sinon, [presque tout est disponible gratuitement](https://en.wikipedia.org/wiki/Comparison_of_deep_learning_software).

Maintenant, tout ce dont vous avez besoin, ce sont des données d'entraînement. Et beaucoup !

**Bonne chance**.

Avant d'aborder à quel point vous êtes coincé, comprenons d'abord pourquoi vous avez besoin de tant de données d'entraînement.

Notre logiciel de deep learning et d'apprentissage automatique est bon. Mieux qu'avant ! Mais pour bien fonctionner, il nécessite _des tonnes_ de données d'entraînement pour produire de bons résultats. Cela ne peut pas être assez souligné : la qualité des modèles que vous créez est directement corrélée à la quantité et à la qualité des données d'entraînement que le logiciel ingère. Jusqu'à ce que nous ayons de meilleurs logiciels, nous sommes incapables de construire de bons modèles à partir de petits ensembles de données. (Et quand je dis "petits", je veux dire, pas _énormes_.)

Malheureusement, un meilleur logiciel n'arrivera pas du jour au lendemain. Alors que la plupart des logiciels s'améliorent progressivement, à mesure que les développeurs corrigent les bugs semaine après semaine, l'apprentissage automatique progressera probablement de manière [ponctuée](https://en.wikipedia.org/wiki/Punctuated_equilibrium) : en quelques grands bonds, difficiles à obtenir.

La raison en est que le logiciel de deep learning est presque impossible à déboguer parce que _nous ne comprenons pas pleinement comment il fonctionne_. Pour moi, c'est la chose la plus étrange à propos de l'apprentissage automatique. Nous ne savons pas vraiment ce qui le fait fonctionner. Nous ne pouvons pas le déboguer systématiquement, nous ne pouvons que deviner et vérifier.

Pete Warden, évangéliste de l'apprentissage automatique extraordinaire, [explique](https://petewarden.com/2014/06/10/why-is-everyone-so-excited-about-deep-learning/) :

> Même si l'approche de Krizhevsky a remporté le concours Imagenet 2012, personne ne peut prétendre comprendre pleinement pourquoi elle fonctionne si bien, quelles décisions de conception et quels paramètres sont les plus importants. C'est une solution fantastique par essai et erreur qui fonctionne en pratique, mais nous sommes encore loin de comprendre comment elle fonctionne en théorie. Cela signifie que nous pouvons nous attendre à des améliorations de vitesse et de résultats à mesure que les chercheurs acquièrent une meilleure compréhension de pourquoi elle est efficace, et comment elle peut être optimisée. Comme l'a dit l'un de mes amis, [toute une génération d'étudiants diplômés est sacrifiée à cet effort](https://twitter.com/dfarmer/status/474609077671034880), mais ils le font parce que le gain potentiel est si grand.

Jusqu'à ce que nous comprenions comment fonctionne le deep learning, nous devons compenser ses insuffisances avec de grandes quantités de données d'entraînement.

Les données d'entraînement sont le sang vital de l'apprentissage automatique.

Alors, comment les obtenons-nous ?

![Image](https://cdn-media-1.freecodecamp.org/images/JdrPABD0RKprta26zdPYKnBeTqslelrU9AWR)
_Les entreprises de plateformes n'ont pas encore utilisé leurs utilisateurs de manière si efficace._

#### Apprendre à utiliser chaque partie du buffle (ou de l'utilisateur)

Si les ordinateurs doivent comprendre les choses humaines et désordonnées, ils doivent être enseignés par des humains désordonnés. Cela a du sens. Mais lorsque nous nous souvenons de la quantité de données dont nous aurons besoin pour créer nos modèles, nous sommes confrontés à un défi : _où allons-nous trouver des tonnes de personnes prêtes à passer leur temps libre à créer nos données d'entraînement ?_

Si vous avez dit : "Je vais les embaucher", j'ai de mauvaises nouvelles. À cette échelle, les payer est pratiquement hors de question.

Si vous avez dit : "Je vais les tromper", vous vous rapprochez.

Un refrain fréquent parmi les personnes qui écrivent sur Internet est : "si vous ne payez pas, vous êtes le produit." Ces écrivains commentent les produits soutenus par la publicité — comme Facebook, Google, Tumblr, SnapChat et presque tout le reste en ligne — qui emballent votre attention et la vendent aux annonceurs. Mais leur refrain fonctionne tout aussi bien pour l'apprentissage automatique.

_Les utilisateurs de services gratuits sont les humains qui entraîneront les ordinateurs afin de construire de meilleurs produits et services._ La partie "gratuite" est cruciale car elle permet d'avoir les masses d'utilisateurs dont nos besoins en données ont besoin.

Tout cela me fait penser à l'ancienne ligne sur les Amérindiens utilisant chaque partie du buffle. Les services en ligne apprennent à utiliser plus de parties de leurs utilisateurs. Notre attention crée leur publicité et notre connaissance alimente leurs modèles de deep learning.

Le truc pour obtenir des données d'entraînement suffisantes est donc double. Vous devez :

1. Attirer un tas de gens.
2. Les convaincre de créer vos données d'entraînement.

C'est Tom Sawyer et les clôtures en picket, juste multiplié par plusieurs centaines de millions.

![Image](https://cdn-media-1.freecodecamp.org/images/BKnjbKELMSzZc6Mnb9FFlQMPgTyL2z8JqU4c)
_Aidez-nous à vous aider._

#### **L'essor des applications de données réciproques (RDA)**

Une nouvelle catégorie d'application, ou de fonctionnalité d'application, a émergé pour faciliter votre peinture de clôture. Ces applications sont conçues pour stimuler la création de données d'entraînement ainsi que pour livrer les produits alimentés par les données capturées. Les gens obtiennent de meilleures applications et les entreprises obtiennent de meilleures données.

L'exemple le plus clair d'une telle application de données réciproques (ou RDA, en abrégé) est Facebook Photos.

Facebook Photos a été conçu pour inciter les spectateurs à étiqueter les personnes dans les photos, facilement et rapidement. Un appel clair à l'action encadre les visages de vos amis et de votre famille après avoir téléchargé une image. L'étiquetage offre des avantages clairs pour vous, à la fois pour la recherche ultérieure et l'alerte de ceux qui sont étiquetés dans les photos. L'étiquetage attire l'attention et commence une conversation, ce qui (non-coïncidemment) sont deux des principales raisons pour lesquelles les gens utilisent Facebook.

Pendant ce temps, tout cet étiquetage crée un énorme bassin de données d'entraînement qui peut être utilisé pour entraîner des modèles d'apprentissage automatique. Avec de meilleurs modèles, viennent de meilleures suggestions d'étiquetage et d'autres fonctionnalités. Grâce à cette RDA, [Facebook possède probablement l'un des meilleurs modèles de reconnaissance d'images humaines au monde](http://www.wired.com/2015/06/facebook-can-recognize-even-dont-show-face/).

Google Search est une autre RDA. Vos recherches et sélections fournissent des données d'entraînement à Google, ce qui aide à rendre sa recherche encore meilleure.

Comme leurs autres produits, Google Search et Facebook Photos démontrent comment les RDA génèrent des [effets de réseau](https://en.wikipedia.org/wiki/Network_effect) significatifs. Plus les gens utilisent une application, plus de données sont générées, meilleure devient l'application, plus les gens utilisent l'application...

Les effets de réseau sont _le_ moteur nécessaire pour les entreprises soutenues par des capitaux-risqueurs dans des marchés où le gagnant rafle tout. Auparavant, les méthodes par défaut d'effet de réseau dans la Silicon Valley étaient sociales/chat (vous allez où sont vos amis) ou les places de marché (les vendeurs vont où sont les acheteurs). C'est pourquoi presque toutes les applications ou services soutenus par des capitaux-risqueurs, non-marchands, intègrent des fonctionnalités de partage ou de communication — même si cela n'avait pas de sens dans l'application.

Les RDA sont une nouvelle méthode pour créer des effets de réseau qui commence tout juste à être comprise. À mesure que la prise de conscience de sa valeur commerciale grandit, attendez-vous à ce que les RDA se propagent dans le paysage.

Cette propagation des RDA sera le premier impact commercial majeur de l'apprentissage automatique. Non seulement parce qu'elles détourneront des ressources, mais parce que les qualités et exigences des RDA influenceront le matériel et le logiciel qui les déploient.

Voici les qualités d'une application de données réciproques :

1. **Les applications doivent être en réseau, de préférence toujours.** Sinon, elles ne peuvent pas envoyer les données capturées à la maison.
2. **Presque tout le calcul se fait hors de l'appareil.** La majeure partie du calcul est la création des modèles, ce qui nécessite l'accès à l'énorme ensemble de données créé par tous les utilisateurs. Par conséquent, la construction de modèles ne peut pas se faire sur l'appareil. Comparer les nouvelles données aux modèles calculés (par exemple, identifier un objet ou une personne dans une image ou reconnaître une phrase parlée) est peu coûteux en calcul.
3. **Les bonnes applications ont besoin de grands publics.** Plus de personnes égalent plus de travailleurs créant des données d'entraînement.
4. **Les bonnes applications ont besoin de beaucoup d'utilisation.** Plus de temps passé à utiliser l'application signifie que chaque utilisateur a plus d'opportunités de créer des données d'entraînement.
5. **Les bonnes applications encouragent la création de données précises.** Si une application est conçue de manière à ce que des erreurs de codage se produisent souvent, les données seront plus faibles. La conception de l'application doit rendre facile pour les utilisateurs d'entrer des données précises, rapidement.

Alors, comment construire une bonne application ?

#### Chemins vers la construction d'une RDA précieuse

La valeur des données d'une RDA peut être exprimée comme un produit des trois derniers points ci-dessus.

Par exemple, vous pouvez avoir une base d'installation relativement modeste si ces utilisateurs passent des heures par jour à coder des données de manière fiable (voir : Tinder, qui possède un ensemble de données d'entraînement incroyable pour déterminer l'attractivité des photos). Ou, vous pourriez avoir une base d'installation géante qui ne code des données que de temps en temps (Facebook, dont les utilisateurs étiquetent des photos généralement lorsqu'ils les téléchargent).

Le défi ici est que les qualités #3 et #4 sont un jeu à somme nulle (comme la publicité, l'autre partie du buffle). Si 50 % du monde passe 20 % de son temps sur Facebook, il ne reste pas beaucoup d'oxygène pour vous. Même si vous grattez quelques centaines de millions d'utilisateurs et empruntez 2 minutes de leur temps quotidien, la collecte de données de Facebook dépassera de nombreux facteurs les gains que vous réalisez. Parce que les données sont collectées en continu, la valeur des RDA ne doit pas être pensée en termes absolus mais comme une _vitesse_.

_Mais_, si dans le scénario ci-dessus vous êtes capable de collecter des données d'entraînement de vos utilisateurs que Facebook ne peut pas collecter par conception, vous ne pouvez pas être dépassé, malgré votre taille plus petite. Les petites entreprises et autres nouveaux venus doivent poursuivre des ensembles de données uniques s'ils veulent rivaliser.

Nous pouvons voir trois chemins vers la construction d'une application de données réciproques précieuse :

1. **Obtenir beaucoup de gens** : Créez une application convaincante qui attire des tonnes d'utilisateurs. C'est le modèle que la Silicon Valley connaît et aime. Construisez quelque chose de disruptif, gagnez en traction et investissez comme un fou pour devenir grand. D'une certaine manière, ce chemin est le chemin RDA accidentel. Une fois grand, ajuster votre application pour mieux collecter des données d'entraînement est simplement une façon de diversifier la valeur que vous tirez de vos utilisateurs. Ce chemin est ridiculement difficile et nécessite une tonne de chance, puis une tonne d'argent. De plus, c'est un peu un cercle vicieux. Une fois que vous êtes aussi grand, la publicité est probablement le fruit le plus facile à cueillir. Vous ne devriez probablement pas choisir ce chemin.
2. **Obtenir beaucoup de temps** : Créez une application qui convainc un nombre raisonnable de personnes de passer un temps extraordinaire à l'utiliser. Dans de nombreux cas, ces types d'applications ou de services seront utilisés passivement. Pensez à une application de navigation qui capture les entrées du conducteur ou à un assistant numérique toujours actif. Les applications ambiantes sont toujours disponibles pour observer ou inciter les utilisateurs, augmentant la vitesse des données qu'elles produisent.
3. **Collecter des données uniques** : Créez une application qui collecte des données d'entraînement que les autres ne peuvent pas collecter. Ici, votre application n'a pas besoin d'être massive au lancement, mais une vision doit exister pour la manière dont les données uniques que vous collectez seront ensuite utilisées pour construire des fonctions complètement uniques. Ces nouvelles fonctions doivent être suffisamment convaincantes pour stimuler les installations et l'utilisation afin de maintenir la vitesse de votre RDA suffisamment élevée avant qu'un grand concurrent ne change la conception de ses applications et n'entre sur le marché. C'est ainsi que vous pourriez distancer Google et Facebook.

Vous avez peut-être remarqué que le chemin #2 a suggéré des exemples qui pourraient ne pas fonctionner sur les smartphones. Bon œil ! En apportant l'informatique dans de nouveaux contextes, nous pouvons créer des RDA qui sont plus persistantes, augmentant le temps passé avec elles. Mieux encore, ces nouveaux contextes apportent l'accès à de nouveaux types de données, ce qui fusionne souvent le chemin #2 dans le chemin #3.

Heureusement, puisque presque toute la valeur fonctionnelle des RDA est produite par des serveurs lointains traitant des ensembles de données massifs, les appareils individuels ont très peu à faire. Leurs cerveaux sont ailleurs, donc ils peuvent s'adapter à plus d'endroits.

![Image](https://cdn-media-1.freecodecamp.org/images/Rj2cQkbH7B4RnEceIZqqKJ4ej8D0N3AWeHmY)
_Il y a une raison pour laquelle ils ne mentionnent pas la vitesse du CPU de la Pebble. Elle fait la plupart de sa réflexion ailleurs._

#### Comment l'apprentissage automatique impacte le matériel

Avec la plupart de la réflexion ayant lieu dans des fermes de serveurs, les appareils qui livrent des RDA peuvent être peu puissants. Leurs CPU peuvent être lents, puisque la comparaison des entrées aux modèles pré-calculés nécessite peu de calcul. Les CPU plus lents peuvent être petits, puisque ils nécessitent moins de transistors et moins de dissipation de chaleur. Et les CPU plus lents nécessitent moins de puissance, ce qui signifie que les batteries peuvent être plus petites (ou rester de la même taille et dépenser leur capacité ailleurs, comme sur la connectivité cellulaire). En plus : ils sont bon marché !

Tout cela signifie que les appareils capables de livrer des RDA se propageront follement. Si nous pouvons intégrer un ordinateur bon marché avec du WiFi dans un produit et capturer de bonnes données de ce contexte, nous le construirons probablement. Les ordinateurs capables de RDA seront injectés partout : dans votre voiture, à votre poignet, dans votre navigateur, à travers vos haut-parleurs portables, dans votre TV, et plus encore.

L'exemple le plus pur de cela est le [Pebble Core](https://blog.getpebble.com/2016/06/02/ks3u03/). Positionné comme un appareil pour le suivi de course et la musique, le Core est vraiment plus une clé de calcul générique. Il est bon marché, à partir de 69 $. Il a un CPU peu puissant, du WiFi, de la connectivité cellulaire, du Bluetooth, un peu de stockage, une prise casque, deux boutons et une batterie. C'est tout. Son interface est contrôlée par la voix et — ce qui est le plus important pour notre discussion — Alexa d'Amazon est intégré. Alexa est une RDA.

En déplaçant le calcul requis pour Alexa vers le côté serveur, Amazon peut déployer Alexa presque partout. Alexa est maintenant livré via des haut-parleurs Bluetooth, des [clés HDMI](http://www.theverge.com/2016/2/3/10904996/amazon-alexa-original-fire-tv-announcement), et par ce que le Core est. L'intégration automobile est inévitable.

Amazon et d'autres sont incités à diversifier leur distribution pour augmenter leur ubiquité et le temps que vous passez avec votre application. De plus, de nouvelles intégrations apportent de nouvelles données, permettant de meilleurs modèles.

Importamment, les entreprises priorisant l'apprentissage automatique ne sont _pas_ incitées à développer pour les appareils les plus puissants. La distribution d'appareils puissants et grand public est limitée en raison de leur coût et de leur nouveauté, limitant leur valeur pour les RDA qui nécessitent des bassins massifs d'utilisateurs. Attendez-vous à ce que la puissance de calcul des appareils stagne à mesure que l'industrie se concentre sur des appareils divers, omniprésents et bon marché plutôt que puissants.

#### Les implications commerciales de l'apprentissage automatique

Pour résumer, voici comment l'investissement dans l'apprentissage automatique et le deep learning affectera probablement l'industrie technologique :

1. **Les gagnants gagneront davantage** : Les grands acteurs existants comme Facebook et Google ont un avantage massif. Ils ont des tonnes d'utilisateurs, des tonnes de leur temps, et des coffres de guerre remplis à la fois de données d'entraînement et d'argent. Concurrencer ces entreprises de front, en créant les mêmes données d'entraînement qu'elles génèrent, est futile.
2. **Les startups réussies créeront des données d'entraînement uniques** : Les challengers peuvent annuler une grande partie des avantages de Google et Facebook en poursuivant de nouvelles frontières de données d'entraînement. Cela peut impliquer des applications mobiles, mais impliquera souvent du nouveau matériel pour amener les RDA dans de nouveaux contextes. Les challengers réussis pourraient construire une telle tête de pont et être acquis pour cela avant même de développer des modèles (voir : Nest). La partie difficile pour ces entreprises sera de passer du développement d'un produit qui génère beaucoup de données d'entraînement uniques et de bonne qualité à la construction de RDA uniques pour générer et maintenir la vitesse.
3. **Les RDA sont un nouveau modèle d'effet de réseau** : À mesure que les RDA émergent et mûrissent, les entreprises et les investisseurs comprendront mieux comment les RDA peuvent construire des modèles commerciaux avec des effets de réseau. Une fois qu'il y aura un exemple clair, la même explosion d'entreprises de marché ("Uber pour X") et d'entreprises sociales ("Facebook pour X") se produira pour les startups d'apprentissage automatique.
4. **L'apprentissage automatique accélérera l'Internet des objets** : Les capacités matérielles stagneront, mais les facteurs de forme se diversifieront. Les ordinateurs coloniseront chaque contexte qui peut accueillir des capteurs et une connectivité réseau à la recherche de données d'entraînement.