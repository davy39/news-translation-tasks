---
title: Observations sur la culture de test du Développement Piloté par les Tests
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-02T17:42:42.000Z'
originalURL: https://freecodecamp.org/news/8-observations-on-test-driven-development-a9b5144f868
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s1wnrbNeea89uz6GsPe6jw.png
tags:
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Testing
  slug: software-testing
- name: TDD (Test-driven development)
  slug: tdd
- name: 'tech '
  slug: tech
seo_title: Observations sur la culture de test du Développement Piloté par les Tests
seo_desc: 'By Doug Arcuri

  This is not a primer on Test Driven Development. It contains my personal observations
  of re-starting the discipline and the problem of unit testing craft.

  Kent Beck, a software engineering leader, is also the modern day re-inventor of
  ...'
---

Par Doug Arcuri

_Ceci n'est pas une introduction au Développement Piloté par les Tests. Il contient mes observations personnelles sur la reprise de cette discipline et le problème de l'artisanat des tests unitaires._

Kent Beck, un leader en ingénierie logicielle, est également le réinventeur moderne du développement piloté par les tests (TDD). Kent a également coécrit JUnit, un framework de test largement utilisé, avec Erich Gamma.

Dans son livre, [XP Explained](https://www.pearson.com/us/higher-education/program/Beck-Extreme-Programming-Explained-Embrace-Change-2nd-Edition/PGM155384.html) (deuxième édition), Kent décrit que à l'intersection des **valeurs** et des **pratiques** se forment des **principes**. Lorsque nous itérons à partir du concept et que nous intégrons ce en quoi nous croyons comme une formule, nous obtenons une transformation.

```
[KISS, Qualité, YAGNI, ...] + [Tests, Spécifications, ...] == [TDD, ...]
```

J'ai un profond respect pour le travail de la vie de Kent, non seulement pour ses brillantes créations logicielles, mais aussi pour son exploration continue de la **confiance**, du **courage**, du **feedback**, de la **simplicité** et de la **vulnérabilité**. Tous ces attributs sont primordiaux pour l'invention de l'Extreme Programming (XP).

Le TDD est un principe et une **discipline** suivie par la communauté XP. Cette discipline existe depuis dix-neuf ans.

Dans cet article, je vais décrire mon opinion sur l'adoption du TDD. Ensuite, nous explorerons des observations personnelles intrigantes lors de la pratique du TDD. Enfin, nous conclurons en postulant pourquoi le TDD n'a pas décollé comme il le devrait. Commençons.

### TDD, Études et Professionnalisme

Dix-neuf ans plus tard, le TDD est toujours débattu comme une discipline dans la communauté des développeurs.

La première question qu'une personne analytique poserait est : « Combien ou quel pourcentage de professionnels du logiciel utilisent le TDD aujourd'hui ? » Si vous demandiez à un ami de Robert Martin (Uncle Bob), un ami de Kent Beck, la réponse serait cent pour cent. Cela est dû au fait qu'Uncle Bob croit qu'il est irréalisable de se considérer comme un professionnel si le développement piloté par les tests n'est pas pratiqué. [1]

Uncle Bob a été le centre de cette discipline depuis quelques années maintenant, et il est naturel de le mentionner dans cet article. Uncle Bob a défendu le TDD et a repoussé les limites de cette discipline de manière significative. Il va sans dire que je respecte également Uncle Bob et son dogmatisme pragmatique.

Cependant, personne ne pose la question de suivi : « la définition de **pratique** est l'utilisation délibérée de — mais elle ne spécifie pas la quantité ou le pourcentage, n'est-ce pas ? » Mon estimation subjective est qu'une majorité n'a pas pratiqué le TDD même pendant une courte période.

La réalité de la situation est que nous ne savons **pas vraiment**, puisque le pourcentage de pratique n'a pas été largement étudié. La seule mesure concrète que nous avons est une petite collection d'entreprises réunies sur [WeDoTDD](http://www.wedotdd.com/). Ici, il y a un suivi de ces entreprises. Des entretiens sont menés avec ceux qui pratiquent 100% du temps, mais cette liste est courte. Elle est également incomplète, car une simple recherche révèle d'autres grandes entreprises pratiquant — mais peut-être pas à pleine capacité.

Si nous ne savons pas combien pratiquent, la question suivante est : « à quel point le TDD est-il efficace en fonction des bénéfices mesurés ? »

Vous serez ravi de savoir qu'il y a eu des études menées au fil des ans qui ont prouvé l'efficacité du TDD. Cela inclut les rapports bien reconnus de [Microsoft](https://collaboration.csc.ncsu.edu/laurie/Papers/Unit_testing_cameraReady.pdf), [IBM](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.567.3740&rep=rep1&type=pdf), de l'Université de Caroline du Nord et de l'[Université d'Helsinki](http://www.sserg.org/publications/uploads/04b700e040d0cac8681ba3d039be87a56020dd41.pdf).

![Image](https://cdn-media-1.freecodecamp.org/images/SxfOzMZHoqcB8MJ51eU97aeXKATgYWYxG7Ms)
_Une visualisation impactante tirée du rapport d'Helsinki._

Ces rapports prouvent dans une certaine mesure que la densité des défauts est réduite de 40% à 60% en échange d'un effort accru et d'un temps d'exécution de 15% à 35%. Ces chiffres commencent également à se répandre dans les livres et les nouveaux processus industriels tels que la communauté DevOps.

Avec ces questions à moitié répondue, la question finale est : « que devrais-je attendre en commençant à pratiquer le TDD ? » Vous avez de la chance, car j'ai formulé mes propres observations sur le TDD. Passons-les en revue.

### 1. Le TDD Exige de Verbaliser une Approche

En pratiquant le TDD, nous commençons à expérimenter un phénomène d'« annoncer le coup ». En termes simples, les courts actes de création de tests échouant et réussissant vont intellectuellement défier le développeur. Ils diront à voix haute « Je pense que cela va passer » et « Je ne pense pas que cela va passer » ou « Je ne suis pas sûr, laissez-moi réfléchir après avoir essayé cette approche. »

L'IDE du développeur est devenu un canard en plastique demandant une conversation intense. Au minimum, les environnements TDD devraient bourdonner de ce type de conversion.

> _Réfléchissez, puis parlez de votre prochain mouvement immédiat._

Ce type de renforcement est clé pour la communication, non seulement pour prédire votre prochaine action, mais aussi pour renforcer les concepts d'écriture du code le **plus simple** pour faire passer un test unitaire. Bien sûr, si le développeur devient silencieux, il s'égare presque certainement de la boucle et doit revenir sur le chemin.

### 2. Le TDD Exige une Mémoire Musculaire

Alors qu'un développeur avance avec les premiers cycles de TDD, il ressentira une fatigue intense en luttant contre une friction élevée et un flux maladroit. Cela est vrai pour toute activité humaine initiée mais non apprise. Le développeur tentera de trouver des raccourcis pour améliorer le cycle, car le but est de réduire cette maladresse et d'améliorer la mémoire musculaire.

La mémoire musculaire est la clé pour ressentir les bonnes vibrations et devenir fluide. Le TDD l'exige en raison de la répétition de l'exécution.

> _Imprimez une feuille de raccourcis. Apprenez seulement autant de raccourcis dans votre IDE que nécessaire pour rendre vos cycles efficaces. Ensuite, continuez à chercher d'autres raccourcis._

Le développeur deviendra un expert de certains raccourcis en seulement quelques sessions, y compris la construction et l'exécution du banc de test. Avec plus de pratique, la création de nouveaux artefacts, la mise en surbrillance de texte et la navigation dans l'IDE deviendront naturelles. Enfin, nous passons à débloquer tous les raccourcis de refactorisation tels que l'extraction, le renommage, la génération, le pull up, le reformatage et le push down de code.

### 3. Le TDD Exige de Réfléchir au Moins un Peu en Avant

Chaque fois qu'un développeur s'assoit pour commencer le TDD, il doit avoir une carte mentale courte et concrète de ce qui doit être résolu. Dans une approche de codage traditionnelle, cela n'est pas toujours vrai, car la carte mentale de la solution pourrait être macro et exploratoire. Le développeur ne sait pas comment résoudre le problème, mais peut connaître un objectif flou. Pour atteindre cet objectif, les tests unitaires sont négligés dans le processus.

Le début et la fin de la session doivent également être ritualisés. D'abord, réfléchissez et listez. Jouez avec. Listez plus. Ensuite, commencez, faites, puis réfléchissez. Cochez. Répétez quelques fois. Enfin, réfléchissez et arrêtez.

> _Maintenez votre liste de tests comme un faucon. Cochez les éléments au fur et à mesure. Ne conduisez jamais sans une liste. Réfléchissez !_

La liste peut prendre un certain temps à formuler et ne fait pas partie du cycle. Cependant, elle doit être préparée juste avant que les cycles ne commencent. Si vous n'en avez pas, vous ne savez peut-être pas où vous allez. Ayez toujours une carte.

```
// Une Liste de Tests
// "" -> ne valide pas
// "a" -> ne valide pas
// "aa" -> valide
// "racecar" -> valide
// "Racecar" -> valide
// imprimer la validation
// avoir une bière aux myrtilles
```

Le développeur doit commander une **liste de tests**, comme décrit par Kent Beck. La liste de tests permet de diriger la résolution dans les cycles immédiats suivants. Cette liste de tests doit toujours être travaillée et mise à jour juste avant que les cycles ne commencent. Une fois la liste de tests résolue, à l'exception de la dernière étape, le cycle s'arrête sur un test échoué.

### 4. Le TDD Exige une Communication avec les Autres

Alors que la liste de tests ci-dessus est remplie, certaines étapes peuvent devenir bloquées parce que l'engagement de travail n'était pas clair. Le développeur ne peut pas comprendre la liste de tests. Ou l'inverse. Générer une liste de tests présomptueuse qui comporte trop de suppositions sur les exigences manquantes. La suggestion est de s'arrêter là.

Conduire sans TDD entraînera des implémentations de complexité inutile. Conduire avec le TDD dans un esprit sans liste est tout aussi dangereux.

> _Parlez fort si la liste de tests comporte des lacunes._

Dans le TDD, le développeur doit comprendre ce qu'il doit construire en fonction de la vision du propriétaire des exigences et rien de plus. Si l'exigence n'est pas claire dans son contexte, la liste de tests commencera à se décomposer. Cette décomposition nécessitera une conversation. Des conversations franches peuvent rapidement se transformer en confiance et en respect. Les boucles de feedback courtes sont maintenant établies.

### 5. Le TDD Exige une Architecture Itérative

Initialement proposé dans la première édition du livre XP, Kent a proposé que les tests devraient piloter l'architecture. Cependant, au cours de quelques années, il y a eu des histoires sur la façon dont les équipes de sprint se heurtent à des murs après quelques sprints.

Bien sûr, faire en sorte que les tests pilotent toute l'architecture est imprudent. Uncle Bob a convenu avec d'autres experts que l'architecture pilotée par les tests est du « horse sh*t ». [1] Une carte plus large est nécessaire, mais pas trop au-dessus des listes de tests distribuées qui sont travaillées sur le terrain.

Kent a également souligné cela il y a de nombreuses années dans le livre [TDD By Example](https://www.safaribooksonline.com/library/view/test-driven-development/0321146530/). La **concurence** et la **sécurité** sont les deux principaux domaines où le TDD ne peut pas piloter et où le développeur doit s'en préoccuper séparément. Traduit librement, la concurrence via la conception système est à un niveau différent et doit être travaillée de manière itérative et en concert avec le TDD. Cela est très vrai aujourd'hui, car certaines architectures évoluent vers des extensions réactives, le zénith de la construction concurrente.

> _Créez une carte plus large de l'organisation. Une vision qui va juste un peu plus loin. Assurez-vous de diriger avec l'équipe de la même manière._

Cependant, l'idée la plus importante est l'**organisation** du système que le TDD ne peut pas gérer efficacement seul. Cela est dû au fait que les tests unitaires testent à un niveau inférieur. L'architecture itérative et l'orchestration du TDD sont difficiles en pratique et demandent de la confiance parmi tous les membres de l'équipe, de la programmation en binôme et une solide revue de code. Il n'y a pas de moyen clair de faire cela, mais il deviendra apparent que de courtes sessions de conception itérative sont nécessaires en harmonie avec les listes de tests sur le terrain.

### 6: Le TDD Révèle la Fragilité des Tests Unitaires et l'Implémentation Dégénérative

Les tests unitaires ont une propriété amusante et le TDD expose cette propriété. Ils ne peuvent pas prouver la correction. E.W. Dijkstra a travaillé sur cela et a discuté de la possibilité de preuves mathématiques dans notre profession pour combler le fossé.

Par exemple, le code ci-dessous résout tous les tests autour d'un palindrome imparfait hypothétique requis par l'entreprise. Il a été développé avec le TDD.

```
// Ce n'est pas un palindrome imparfait.
```

```
@Test
fun `Étant donné "", alors cela ne valide pas`() {    "".validate().shouldBeFalse()}

@Test
fun `Étant donné "a", alors cela ne valide pas`() {    "a".validate().shouldBeFalse()}

@Test
fun `Étant donné "aa", alors cela valide`() {    "aa".validate().shouldBeTrue()}

@Test
fun `Étant donné "abba", alors cela valide`() {    "abba".validate().shouldBeTrue()}

@Test
fun `Étant donné "racecar", alors cela valide`() {    "racecar".validate().shouldBeTrue()}

@Test
fun `Étant donné "Racecar", alors cela valide`() {    "Racecar".validate().shouldBeTrue()}
```

En effet, ces tests ont des lacunes. Les tests unitaires sont fragiles même pour les demandes les plus triviales. Nous ne pouvons jamais prouver la correction car, si nous devions le faire, cela nécessiterait un effort mental extrême et les entrées requises seraient inimaginables.

```
// Une solution trop générique basée sur les tests fournis
```

```
fun String.validate() = if (isEmpty() || length == 1) false else toLowerCase() == toLowerCase().reversed()
```

```
// La meilleure implémentation et résout tous les tests
```

```
fun String.validate() = length > 1
```

`length >`; 1 pourrait être appelé **implémentation dégénérative**. C'est juste assez d'implémentation pour résoudre le problème en main, mais en soi, cela ne nous dit rien sur le problème que nous essayons de résoudre.

La question est, quand un développeur arrête-t-il d'écrire les tests ? La réponse semble simple. Lorsque **l'entreprise est satisfaite**, et non lorsque l'auteur du code l'est. Cela peut blesser notre **passion de construction** et nous sommes **embarrassés par la simplicité**. Ces sentiments sont équilibrés par les bons sentiments du code propre et la capacité à refactoriser avec confiance plus tard. Les choses semblent simplement propres et ordonnées.

> _Soyez conscient que les tests unitaires sont faillibles mais nécessaires. Comprenez leurs forces et faiblesses. Les [tests de mutation](http://pitest.org/) peuvent aider à combler cette lacune._

Le TDD a des gains, mais il peut empêcher de construire les châteaux de sable dont nous n'avons pas besoin. C'est une **contrainte**, mais il nous permet d'aller plus vite, plus loin et en sécurité. Peut-être que c'est ce qu'Uncle Bob voulait vraiment dire par être un **professionnel**.

Mais ! Peu importe à quel point les tests unitaires peuvent sembler fragiles, ils sont une nécessité fondamentale. Ils sont nécessaires pour permettre à la **peur** de se transformer en **courage**. Les tests permettent de refactoriser le code avec miséricorde et, mieux encore, c'est un guide, une **documentation**, pour tout autre développeur de sauter immédiatement et de commencer à ajouter de la valeur à un projet bien soutenu par des tests unitaires.

### 7: Le TDD Révèle la Boucle de Feedback de Complétion des Assertions

Faisons un pas en arrière. Pour les deux phénomènes suivants, nous visiterons des récurrences étranges. Pour la première occurrence, jetons un rapide coup d'œil à FizzBuzz. Voici notre liste de tests.

```
// Imprimer les nombres de 9 à 15. [OK]
// Pour les nombres divisibles par 3, imprimer Fizz au lieu du nombre.
// ...
```

Nous sommes à quelques étapes. Nous avons maintenant un test échoué.

```
@Test
fun `Étant donné des nombres, remplacer ceux divisibles par 3 par "Fizz"`() {    val machine = FizzBuzz()    assertEquals(machine.print(), "?")}

class FizzBuzz {    fun print(): String {        var output = ""        for (i in 9..15) {            output += if (i % 3 == 0) {                "Fizz "            } else "${i} "        }        return output.trim()    }}
```

```
Attendu <Fizz 10 11 Fizz 13 14 Fizz>, réel <?>.
```

Naturellement, si nous dupliquons les données d'assertion attendues dans `assertEquals`, cela atteint le résultat et le test passe.

> _Alors que nous continuons à interroger le banc de test pendant les étapes d'implémentation, les tests unitaires échouant basés sur des données peuvent correctement répondre à leurs propres assertions. Peut-être pouvons-nous appeler cela du test vaudou._

Parfois, les tests échouant crieront un résultat correct nécessaire pour faire passer le test. Je ne sais pas comment appeler ces événements... peut-être **test vaudou**. Votre expérience peut varier en fonction de votre paresse et de votre étiquette de test, mais j'ai vu cela se produire de nombreuses fois en travaillant pour que l'implémentation atteigne des **ensembles de données** préétablis et attendus.

### 8: Le TDD Révèle le Prémisse de Priorité de Transformation

Dans le TDD, on peut se retrouver piégé. Il existe des situations où le développeur peut être enchevêtré par les transformations qu'il applique pour atteindre l'implémentation. À un moment donné, le code de test devient un goulot d'étranglement pour avancer. Un **impasse** se forme. Le développeur doit reculer et désarmer en supprimant une partie des tests pour sortir du trou. Le développeur devient exposé.

Uncle Bob a probablement rencontré ces impasses dans sa carrière, puis il a probablement réalisé que l'acte de faire passer un test doit nécessiter un ordre préféré afin que le risque d'une impasse soit réduit. En même temps, il a également réalisé un prémisse. **À mesure que les tests deviennent plus spécifiques, le code devient plus générique.**

![Image](https://cdn-media-1.freecodecamp.org/images/ABgDg1ObAdd7zqhYFkN0shypQX89fqaAC9AP)
_L'ordre des transformations. On devrait toujours préférer la plus simple (en haut de la liste)._

Cela s'appelle le [Prémisse de Priorité de Transformation](https://8thlight.com/blog/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html). Il semble y avoir un ordre de risque de refactorisation que l'on peut choisir pour atteindre en faisant passer un test. La transformation choisie en haut (la plus simple) est généralement la meilleure option et entraînera le moins de risques de créer une situation d'impasse.

[TPP](http://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html) ou peut-être **le Calcul des Tests d'Uncle Bob** est l'une des observations les plus intrigantes, techniques et excitantes à ce jour. Utilisez-le comme guide pour garder le code aussi simple que possible.

> _Imprimez la liste TPP et placez-la sur votre bureau. Référez-vous à elle pendant que vous conduisez pour éviter les impasses. Embrassez un ordre de simplicité._

Cela complète toutes les observations initiales. Mais avant de conclure, j'aimerais revenir à ma question initiale sans réponse : « Combien ou quel pourcentage de professionnels du logiciel utilisent le TDD aujourd'hui ? » Ma réponse reste : « Je pense que le groupe est petit. » J'aimerais explorer cette supposition ci-dessous avec des raisons.

### Le TDD a-t-il Décollé ?

Malheureusement, non. Le pourcentage est subjectivement bas et la recherche de données continue. En m'appuyant sur mon expérience en recrutement, en direction d'équipes et en tant que développeur empathique, laissez-moi partager mes observations.

#### Raison 1 : Aucune Exposition à une Vraie Culture de Test

Mon estimation éduquée est qu'une majorité de développeurs logiciels n'ont pas eu l'expérience d'apprendre et de travailler dans une **culture de test**.

La définition d'une culture de test est un endroit où les développeurs pratiquent et s'améliorent délibérément par le test. Ils mentorent continuellement ceux qui ne sont pas compétents dans ce domaine. Chaque binôme et chaque pull request est une boucle de feedback sur la construction d'individus pour devenir excellents en test. Il y a également un soutien et un appui majeurs tout au long de la chaîne d'ingénierie. Tous les managers comprennent et croient en l'importance des tests. Lorsque les délais et les temps deviennent difficiles, la discipline des tests n'est pas abandonnée — elle est maintenue.

Ceux qui ont traversé une culture de test, comme moi, ont de la chance d'avoir ces observations. Nous pouvons appliquer l'expérience à des projets futurs.

#### Raison 2 : Ressources Éducatives Peu Claires

Certains ont tenté d'écrire des livres sur le sujet tels que [xUnit Patterns](http://xunitpatterns.com/) et [Effective Unit Testing](https://www.manning.com/books/effective-unit-testing). Cependant, il semble qu'il n'y ait aucun endroit qui définisse clairement ce qu'il faut tester et pourquoi. La plupart des ressources disponibles ne décrivent pas clairement l'art de l'assertion et de la vérification.

Les projets open source sont également inégaux en matière de bons tests unitaires. Dans ces projets peu familiers, la toute première chose que je fais est de chercher des tests. Ma déception est presque certaine. Je peux également me souvenir des très rares cas d'excitation lorsque des tests sont présents mais aussi... lisibles.

#### Raison 3 : Aucun Focus dans les Universités

Mon observation des candidats fraîchement sortis de l'université au fil des ans révèle une hypothèse bien connue : peu ou pas de discipline dans la rigueur des tests. Chaque développeur que je connais a appris les tests par la suite, certains par eux-mêmes mais la plupart en passant par une expérience précédente de culture de test.

#### Raison 4 : Une Carrière de Haute Passion pour les Tests Requise

Cela prend également de la passion pour s'intéresser aux tests et pour comprendre les détails et les bénéfices sur une longue période. Vous devez être affamé et obsédé par le code propre et faire mieux l'artisanat.

La plupart veulent simplement que les choses fonctionnent, atteignant seulement la moitié de ce que Kent Beck a dit : « D'abord, faites-le fonctionner, puis faites-le correctement. » Je comprends que faire fonctionner les choses est une bataille difficile en soi.

Les tests sont tout aussi difficiles à bien faire, alors concluons sur cette pensée.

### Conclusion

La proposition de Kent dans XP incluait une formulation simple de l'**instinct**, de la **pensée** et de l'**expérience**. Ces trois niveaux sont des pierres d'achoppement pour la qualité d'exécution mesurée par un **seuil**. C'est un excellent modèle pour expliquer un problème avec le TDD.

Le seuil pour une exécution de test propre est élevé, en ce sens qu'il éclipse une base généreuse d'expérience. La majorité ne deviendra jamais au-dessus de l'eau et ceux qui le font sont chanceux — ont une expérience de la culture de test insaisissable.

![Image](https://cdn-media-1.freecodecamp.org/images/I3qtB4KmCS9URHBFHSyqTTyilaoBmrf6-3Lk)
_Tiré de XP Explained. À l'origine sur la qualité de la conception, imaginez une ligne de seuil plus élevée._

Le logiciel est suffisamment difficile à construire et à organiser, mais les tests le portent à un tout nouveau niveau d'illumination.

Au début, j'avais un **instinct** que les tests sont importants, mais mon **expérience** de la culture de test est venue plus tard. Cela a pris des années de **pensée** dans ma carrière, mais sans cette expérience de la culture de test, je ne serais pas sorti au-dessus de ce seuil.

Je crois que de nombreux développeurs ont également cette pensée mais ne peuvent pas voir le vrai bénéfice de la culture de test en raison du manque d'**expérience** spécifique.

> _La discipline du TDD a du mal à décoller en partie à cause de la courbe d'apprentissage élevée des tests. Même armé de connaissances et d'expérience vétérans en test, le TDD nécessite un espace mental qui est unique et difficile. Cependant, tous devraient l'essayer._

Amplifiez cela. Le TDD exige toute cette **pensée** et **expérience** et plus encore. Ce n'est pas facile et c'est une compétence. Je pense que c'est parce qu'il commande le débit des développeurs au maximum, continuellement et sans relâche. Nous sommes tous **vulnérables** dans le processus, et peu de développeurs aiment être dans cette position.

```
@Test
fun `Étant donné un logiciel, lorsque nous construisons, alors nous attendons des tests`() {    build(software) devraitAvoir des tests}
```

Cependant, le TDD est une discipline intrigante et **est un outil sur lequel s'appuyer**. Ses **phénomènes** devraient être étudiés en détail. Si rien d'autre, la discipline fait de meilleurs développeurs car la pratique contient des bénéfices qui peuvent renforcer l'individu et le groupe collectif.

_L'inspiration pour cet article est due en partie à [Danny Preussler](https://www.freecodecamp.org/news/8-observations-on-test-driven-development-a9b5144f868/undefined). Alors que je réexplore la discipline, il a commencé à organiser des ateliers complets sur le TDD Android. [Consultez son récent deck ici](https://speakerdeck.com/dpreussler/tdd-on-android-mobos-2018)._

[1] [Jim Coplien et Bob Martin Débattent du TDD](https://www.youtube.com/watch?v=KtHQGs3zFAM)