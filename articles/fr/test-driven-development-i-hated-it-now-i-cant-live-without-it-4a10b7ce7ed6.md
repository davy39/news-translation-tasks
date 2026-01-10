---
title: Comment et pourquoi j'ai décidé que le développement piloté par les tests valait
  mon temps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-12T17:05:53.000Z'
originalURL: https://freecodecamp.org/news/test-driven-development-i-hated-it-now-i-cant-live-without-it-4a10b7ce7ed6
coverImage: https://cdn-media-1.freecodecamp.org/images/0*2x368zcCx_aSL57K.
tags:
- name: Life lessons
  slug: life-lessons
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: TDD (Test-driven development)
  slug: tdd
- name: technology
  slug: technology
seo_title: Comment et pourquoi j'ai décidé que le développement piloté par les tests
  valait mon temps
seo_desc: 'By Ronauli Silva

  I first read about test driven development (TDD) in some technical reviews blog,
  but I barely read it (or thought about it). Why would people write tests first when
  they already knew the logic?

  So what was this all about? Writing tes...'
---

Par Ronauli Silva

J'ai d'abord lu sur le développement piloté par les tests (TDD) dans un blog de revues techniques, mais je l'ai **à peine** lu (ou y ai pensé). Pourquoi les gens écriraient-ils des tests en premier **quand ils connaissent déjà la logique ?**

Alors, de quoi s'agissait-il ? Écrire les tests en premier, construire la logique de manière incrémentielle, et le faire en itérations. Le truc amusant, c'est que si vous donnez deux programmeurs cinq minutes pour coder une simple séquence de Fibonacci et que vous demandez à l'un de faire du TDD, à la fin des 5 minutes, le programmeur faisant du TDD peut dire « J'ai un test pour ça ! » Mais il n'aura pas fini le code. D'un autre côté, l'autre aura fini toute la séquence de Fibonacci et l'aura optimisée.

### **Pourquoi utiliser le TDD ? Les tests unitaires ne suffisent-ils pas ?**

À la fin de l'année dernière, j'ai enfin rencontré le TDD face à face. Lors d'une session de bootcamp de trois mois, nous étions obligés de toujours faire les choses avec le TDD. J'avais déjà assez de mal, et mon cerveau se rebellait toujours quand il était temps d'écrire les tests.

Pourquoi devrions-nous écrire les tests en premier quand je peux directement coder la logique, mon cerveau demandait ? Ne pouvons-nous pas simplement les écrire plus tard ? Après que toutes les fonctionnalités soient terminées ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*G2pGmoV1UXUH1izsziJDSw.png)
_Comment cela se présente quand notre mentor TDD nous convainc_

Permettez-moi de vous donner un aperçu rapide du TDD en quelques mots.

Disons que je crée une fonction fibonacci. Je pourrais demander, quelle est l'**assertion la plus simple** sur une fibonacci ?   
=> Retourne 1 si l'entrée est 1.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uXMbt9iEYwdXCIt7ii6Zkg.png)
_Écrire le test en premier, aucune logique codée !_

Quelle est la **solution la plus simple** pour cette assertion ? La **solution la plus simple**, je veux dire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qajwrX_pTW-3LDFxY_BafQ.png)

Maintenant, le prochain mouvement. Quelle est la prochaine assertion la plus simple pour fibonacci ?  
=> Retourne 2 pour les entrées = 3

![Image](https://cdn-media-1.freecodecamp.org/images/1*vKLIf8aqUSaylG2UZvP9Zg.png)

Encore une fois, corrigeons cela très rapidement. Retournez-le simplement et ajoutez un peu de branchement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zU1Q78Q9v3SD6LVycIrYfQ.png)

Passez à une autre attente. Visez un nombre plus grand. Faites-le de manière itérative, incrémentielle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vANcpoacacpjY-HbkpEIZA.png)

Et ainsi de suite, jusqu'à ce que vous obteniez la belle solution pour votre fonction fibonacci. Si vous voulez pratiquer davantage, essayez d'ajouter la mémoisation pendant le processus (et n'oubliez pas—avec TDD).

Avez-vous remarqué ce que nous avons fait là ? Les petits pas, votre assertion, et comment nous définissons la solution ? Votre processus de pensée s'est séparé en ces cinq points critiques :

**Conception Simple & Incrémentielle** — Vous devez penser à ce que la chose la plus simple qu'une fonction particulière pourrait faire, et à ce qui vient ensuite. L'exemple de fibonacci décrit parfaitement ce point.

**Assertion** — Quelle est votre attente de cette fonction ? Et comment décrivez-vous cette attente ? Les autres personnes la comprendront-elles rapidement ?  
Certaines bibliothèques de test vous fournissent une fonctionnalité de description de test. Cette chaîne est la seule chose verbeuse qui explique ce que votre code fait.

Assurez-vous que c'est une bonne explication, ou vous recevrez un appel pendant vos vacances parce que votre cas de test illisible échoue, et personne ne sait pourquoi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*B7_rBZ57kOtz92rrsWW-KA.png)
_Votre assertion et la manière dont vous la formulez compte._

**Conception Testable** — Comment devriez-vous la concevoir pour qu'elle soit testable ? Jetez un coup d'œil à ces deux extraits ci-dessous.

Le premier :

![Image](https://cdn-media-1.freecodecamp.org/images/1*VYWzFZjaMaZj1EEBZ-TKPg.png)
_Voyez comme c'est désordonné si votre code n'est pas testable._

En faisant du TDD, puisque vous écrivez le test en premier, vous devez vous assurer que votre code est **testable**_. Vous pouvez voir dans l'exemple que vous ne testez même pas votre fonction fibonacci. Au lieu de cela, vous testez l'**effet secondaire** de cette logique fibonacci dans votre code, qui invoque la fonction console.log.

L'autre chose est que vous ne savez jamais lequel échoue, le console.log() ou votre bloc fibonacci lorsque vous le refactorisez. De cette manière, le TDD nous conduit à augmenter la modularité dans notre code.

Maintenant, regardons le deuxième extrait.

![Image](https://cdn-media-1.freecodecamp.org/images/1*I2U7QrcmisWipCcYd_pcUQ.png)

Dans le deuxième exemple, nous pouvons voir que nous testons la fonction fibonacci particulière, et non l'autre fonction qui l'invoque. Nous sommes confiants que la fonction fonctionne parfaitement dans les conditions que nous avons définies. Nous sommes sûrs que si l'autre fonction invoque notre fibonacci et échoue, ce n'est pas à cause de notre code.

**Cas Négatifs et Particuliers** — que devriez-vous attendre lorsque quelque chose ne va pas : est-il invoqué avec null ? Lance-t-il une exception ? Comment devrait-il être géré ? Que pourrait-il se passer dans le code ? Quelle pourrait être la chose la plus étrange et la plus bizarre qui pourrait se produire dans cette boucle ? Quel test peut attraper cela ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*M1cysq3GcCAVSGTSyCT1Bg.png)
_Combien de possibilités y a-t-il ?_

**Limites** — Devriez-vous vous attendre à cela de votre fonction ? Êtes-vous sûr que ce n'est pas la responsabilité d'une autre classe ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*o6kKa-ib3wswzKqe.jpg)

### Mes problèmes avec le TDD

Oui, c'est effectivement lent. Parfois, votre temps est doublé puisque vous écrivez à la fois des tests et de la logique en même temps. Cela rend important la manière dont vous utilisez votre clavier (vitesse de frappe, meilleure utilisation des raccourcis, etc.).

Et pire encore — lorsque les exigences changent — vous devez refactoriser ou supprimer et réécrire le code de test sur lequel vous avez travaillé dur. Ce qui signifie que le code de test est un code que vous écrivez et qui est plus susceptible d'être supprimé à l'avenir. Et vous le faites, de manière itérative. SUPPRESSIONS. CODES. RÉÉCRITURES. ENCORE. EN BOUCLE !

**Réfléchissez-y. Pourquoi écririez-vous du code qui est plus susceptible d'être supprimé ?**

« Non, ça suffit avec ce TDD. Je le ferai quand je trouverai une bonne raison de passer du temps à écrire du code que je suis susceptible de supprimer », me suis-je dit.

**Et c'était juste avant que je ne commence inconsciemment à creuser ma propre tombe.**

### Pourquoi j'ai changé d'avis

L'illumination est venue environ deux mois plus tard, quand j'ai été affecté à un groupe qui n'implémentait pas bien du tout le TDD.

Je veux dire, ils implémentaient le TDD, **mais** ils laissaient les tests cassés. Ils ne se donnaient pas la peine de corriger ces cas de test échoués (qui échouaient souvent parce que les exigences avaient changé). Et cela s'est produit pour la raison la plus clichée du monde : ils n'avaient pas le temps. Ils devaient respecter les délais.

Après avoir examiné la situation, j'ai marmonné « Regardez, voyez ! Ce TDD ne fonctionne pas dans le monde de la production ! » Cela m'a fait remettre en question beaucoup de choses : est-ce que ce TDD vaut la peine de se battre ? Le TDD vaut-il le temps ? Apporte-t-il même une quelconque valeur commerciale ?

Après un certain temps, j'ai réalisé que les problèmes grandissaient de manière exponentielle, les tâches étaient retardées, le chaos régnait, et l'expérience des développeurs devenait vraiment mauvaise — tout cela parce qu'ils avaient mal implémenté le TDD et à moitié. C'était **encore pire que de ne pas écrire de tests du tout.**

Voici quelques-uns des problèmes que cela a causés :

* Lorsque j'ajoutais une nouvelle fonctionnalité ou refactorisais des choses, je ne savais pas si ce code échouait ou non parce que le test échouait déjà.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qL_hflKv-kH7IOjxfnqQqg.png)
_Nous ne savons pas quels tests échouent, car presque tous échouaient déjà avant ! -_-_

* Nous étions obligés d'avoir un seuil élevé de couverture de code. Et ne vous y trompez pas, les programmeurs sont intelligents et **rusés**. Ils écrivent des tests sans attentes, comme des tests de fumée. Et c'était le **seul** test qu'ils avaient sur cette logique particulière. C'était comme si nous savions seulement qu'il échouait après que tout était en feu. Comme c'est dangereux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gq_uwGye0DYRcXA822w1fA.png)
_Toujours en train de passer, de toute façon ! Vive la couverture de code !_

* Nous utilisions CI/CD pour le déploiement. Et nous déployions toujours même si cela échouait, ce qui était effrayant : Vous ne saviez jamais si votre production elle-même échouait, ou si c'était parce que vous n'aviez pas corrigé les tests.

![Image](https://cdn-media-1.freecodecamp.org/images/1*g_0sJ3rQKpauqi3wuLzD0g.png)
_Le test échoue, déployez quand même !_

![Image](https://cdn-media-1.freecodecamp.org/images/0*8R6C2z00Z6f7F7fC.jpg)

* Après la production, nous avons fini par corriger des bugs étranges et complètement imprévus. Nous n'avions même jamais pensé à ces conditions étranges auparavant. (Vous avez déjà trouvé une situation où quelque chose dans un bloc try-catch échoue mais ne lance pas d'exception ?)

Oh, l'horreur !

Après avoir analysé la situation, l'avoir fait en itérations, et y avoir réfléchi, j'ai réalisé que le TDD est en fait une pépite d'or. Si fait correctement, il peut faire de nous de meilleurs développeurs.

### Pourquoi j'aime maintenant le TDD

#### **Avec le TDD, vous avez moins de bugs**

**Vous ne manquerez presque jamais de choses que vous pouvez attraper avec vos tests**.

Lorsque vous obtenez une exigence, vous écrivez d'abord un test pour celle-ci. Ensuite, vous exécutez le test et voyez s'il échoue d'abord. Lorsque vous ajoutez la logique, vous voyez s'il passe.

**Voir qu'il échoue est important, car vous savez ce qui a cassé votre code**. À long terme, cette pratique garantit que toutes les lignes de votre code sont bien testées.

#### **Le TDD vous fait gagner beaucoup de temps _(dans le futur)_**

Le CI/CD repose fortement sur les tests. Si vous écrivez les mauvais tests (ou trop peu de tests), vous avez déjà gaspillé cinq heures pour trouver les erreurs qu'il n'a pas pu attraper. Si vous écrivez de bons tests, et passez juste cinq minutes de plus à écrire des conditions plus profondes et plus complètes de votre code, vous gagnerez du temps à le déboguer dans le futur.

#### **Le TDD traite des aspects humains du codage**

Les principaux étant la négligence et l'oubli. Si vous écrivez toute la logique directement, à la fin de, disons, la ligne 190, vous pouvez oublier pourquoi vous avez multiplié une variable par 100 à la ligne 19.

Mais, en le faisant de manière incrémentielle et en énonçant l'assertion de notre code, nous construisons progressivement notre compréhension. Cela nous fait mieux comprendre le code et ses comportements.

En bonus, nous avons une sorte de documentation vivante et fonctionnelle de notre code. Vous pouvez voir quel test échoue si vous supprimez la ligne précédente, et vous savez instantanément pourquoi.

#### **Le TDD vous aide à vous concentrer**

Les programmeurs ont tendance à écrire trop de code, ou à écrire du code qui fait trop de choses. Ou ils essaient de planifier des conditions qui n'existent jamais. Souvent, lorsque mon équipe pratiquait le pair pairing, j'ai découvert que le TDD nous permettait d'écrire moins de code par rapport aux autres équipes qui ne faisaient pas de TDD. Pendant le codage, nous étions concentrés sur le passage du cas de test — rien de moins, rien de plus.

#### **Le TDD bénéficie aussi à votre cerveau**

Vous avez la preuve que votre code est prêt pour la production, même avant de le déployer. Vous n'avez pas à vous soucier des choses que vous avez déjà testées auparavant. Vous n'avez pas à vous vanter auprès de votre chef de projet de l'avancement du projet, car vous pouvez leur montrer que les tests passent !

![Image](https://cdn-media-1.freecodecamp.org/images/0*m9IeLR30F2AAtlwu.jpg)

Cependant, le TDD n'est pas **toujours** votre solution miracle. Cela prend du temps. Vous devez configurer le projet — comme l'environnement, les mocks et les stubs — même avant de commencer à faire quoi que ce soit.

Mais rappelez-vous, le temps passé à écrire des tests n'est pas du temps perdu. C'est le temps que vous investissez maintenant pour économiser votre temps plus tard. C'est l'investissement que vous faites sur le système que vous construisez, alors que vous construisez du code sur plus de code. Et vous voulez que ses fondations soient aussi solides que possible. Le TDD vous donne cela.

En fin de compte, cela pourrait vous coûter une fortune si vous **ne faites pas** de TDD. **Cela peut prendre du temps, mais c'est bon pour vous et votre équipe à long terme.**