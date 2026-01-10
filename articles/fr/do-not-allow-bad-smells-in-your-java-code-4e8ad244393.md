---
title: Rendez votre code Java agréable et frais
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-01-25T08:48:11.000Z'
originalURL: https://freecodecamp.org/news/do-not-allow-bad-smells-in-your-java-code-4e8ad244393
coverImage: https://cdn-media-1.freecodecamp.org/images/1*u7DN2oqc-6e0SGBq05sBbw.jpeg
tags:
- name: Design
  slug: design
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: Testing
  slug: testing
- name: Web Development
  slug: web-development
seo_title: Rendez votre code Java agréable et frais
seo_desc: 'By Marco Massenzio

  A few years ago I joined a startup working on a cloud enterprise service that was
  originally built by an offshore team.

  The chosen technologies (REST, Java, MongoDB) were actually valid technical choices
  for the problem at hand. To...'
---

Par Marco Massenzio

Il y a quelques années, j'ai rejoint une startup travaillant sur un service d'entreprise cloud qui avait été initialement construit par une équipe offshore.

Les technologies choisies (REST, Java, MongoDB) étaient en fait des choix techniques valides pour le problème en question. Dommage qu'ils aient ensuite procéder à se tromper spectaculairement avec un schéma de données gonflé (et ingérable) et une implémentation Java encore pire.

La partie la plus amusante était qu'ils croyaient sincèrement que la revendication de MongoDB "sans schéma" signifiait qu'il n'était pas nécessaire de concevoir soigneusement le modèle de données, de réfléchir aux index et de considérer comment les données seraient accessibles.

Dans cet article, j'aimerais disséquer les nombreux "odeurs" (voir le livre de Martin Fowler [book](http://amzn.to/2a717N4)) qu'une classe Java particulière émettait, comment cela aurait pu être évité, et les nombreux anti-modèles rencontrés.

Mon espoir est que, en lisant cet article, vous éviterez de faire les mêmes erreurs, et que les gens comme moi ne seront pas obligés de venir corriger _votre code puant!_

![Image](https://cdn-media-1.freecodecamp.org/images/1*axmvm_999hjITKu4debMZQ.gif)

#### Première odeur : pas de style

J'ai [précédemment](https://codetrips.com/2014/02/07/from-null-to-a-hundred-in-six-months-2/) râlé sur la nécessité de suivre des styles de code adéquats (et largement acceptés). En bref:

* Les nouveaux développeurs rejoignant l'équipe auront une courbe d'apprentissage moins raide.
* Les outils automatisés seront mieux à même de fournir des insights.
* Les bugs triviaux et évitables seront faciles à repérer.

Et, oui, votre code sera plus agréable à regarder et votre estime de soi s'améliorera aussi. Il est difficile de convaincre les gens de vos brillantes idées lorsque votre code ressemble à quelque chose que vous avez écrit en frappant un club de caveman contre votre clavier.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nMh07KOPxty6E2sG10uHCw.jpeg)
_Les grands développeurs de logiciels sont comme des artisans talentueux._

Voici quelques-unes des caractéristiques du "caveman du clavier":

* utilisation incohérente des espaces (parfois avant, parfois après les parenthèses et autour des opérateurs, ou pas du tout)
* utilisation incohérente des lignes vides: parfois une au hasard, parfois deux ou plus, puis aucune
* aucun égard pour la longueur de ligne (de nombreuses lignes plus longues que 100 colonnes, plusieurs plus longues que 200, et une ligne record de 257 colonnes)
* pas d'utilisation du "diamond pattern" de Java 7 et quelques utilisations aléatoires de collections _raw_
* des noms de variables qui ont peu à voir avec leur véritable signification
* utilisation incohérente des constantes et des chaînes de caractères codées en dur — parfois **la même** chaîne de caractères codée en dur répétée plusieurs fois dans quelques lignes de code — clairement le résultat d'un copier-coller

et ainsi de suite...

Voici quelques conseils pour corriger les odeurs de style de votre code:

* Choisissez un bon guide de style [style guide](https://google.github.io/styleguide/javaguide.html) largement connu et respectez-le. Mieux encore, faites en sorte que votre IDE applique automatiquement le style de codage (à la fois Eclipse et IntelliJ sont très bons dans ce domaine).
* Si votre langage de programmation de choix le permet, envisagez d'utiliser un outil automatisé pour détecter les infractions de style de code (comme pylint, jslint). Mieux encore, **intégrez les vérifications de style dans vos builds CI automatisés** (et empêchez les commits jusqu'à ce qu'ils passent).
* Soyez **cohérent** dans l'utilisation des espaces, des lignes vides et de la longueur des lignes. On ne sait jamais quand une recherche et un remplacement pilotés par regex à l'échelle du projet seront nécessaires.
* N'utilisez jamais les collections _raw_. Les génériques Java sont là pour une raison. Ce point seul mériterait un article à lui seul. Je m'y attellerai en temps voulu. En attendant, veuillez lire [l'excellent Effective Java de Bloch](http://amzn.to/2a70WkJ).
* Pensez à la pauvre âme qui devra corriger votre code puant. Cela pourrait même être **vous** dans quelques mois!

#### Deuxième odeur : code non testable

Je ne peux pas vous dire combien de fois j'ai juré que mon code était exempt de bugs, mais j'ai quand même écrit des tests unitaires. Cela m'a sauvé la mise tellement de fois que ce n'est même pas drôle.

Les gens, testez vos codes unitaires. Faites-le simplement.

Pour commencer, si vous voulez que votre code soit testé, votre code devrait être, bien, testable.

Voici un exemple de ce qu'il ne faut pas faire: une classe a été implémentée pour servir un appel d'API particulier qui, en réponse à une requête client, servirait un objet très complexe, avec des sous-objets profondément imbriqués, tous couchés dans un mélange de logique métier et de données liées à l'interface utilisateur.

Lors de la fourniture d'un objet aussi complexe, vous voudriez le tester dans plusieurs scénarios différents et vous assurer que l'objet retourné conforme aux spécifications de l'API _documentées_.

Sauf que dans ce cas particulier de la vie réelle, il n'y avait virtuellement **aucune API documentée**. En fait, non seulement il n'y avait **aucun test unitaire**, mais la classe était (et reste probablement) intestable.

Que veux-je dire par là? Eh bien, regardez cette méthode:

```
public static Map<String, Object> getSomeView(    Map<String, Object> queryParams) {  List<Map<String,Object>> results = SomeSearch.find(queryParams);  ...}
```

Comme vous pouvez le voir, cette méthode (qui retourne une Map dont les valeurs sont des Objects — juste un cran au-dessus d'être non typée) est **statique** — tout comme la _première méthode_ appelée, qui exécutera éventuellement la requête contre MongoDB.

Cela rend très difficile le fait de simuler l'appel, ou la requête de base de données, ou de construire un ensemble de tests pilotés par les données, ce qui nous aurait permis de tester la transformation des données et la logique de génération de vue dans la méthode sous plusieurs scénarios différents.

Il existe aujourd'hui [PowerMockito](https://github.com/jayway/powermock/wiki/MockitoUsage) qui peut résoudre certains de ces problèmes, mais le faire est extrêmement laborieux et sujet aux erreurs. Selon mon expérience, la simulation de méthodes statiques nécessite un ratio de 10:1 lignes de code de simulation par rapport au code de test réel.

Il est également à noter que _queryParams_ pourrait être à peu près n'importe quoi. Dans ce cas, il s'agit d'un ensemble d'options de pagination/tri. La seule façon de le découvrir, cependant, aurait été de faire tourner le serveur réel en mode débogage, puis d'exécuter l'appel API à partir d'un client et de voir ce qui arrive à l'autre bout.

Parce que, oui, vous l'avez deviné: il n'y avait absolument **aucun javadoc** pour expliquer ce que fait la méthode.

Considérez plutôt si vous aviez un code similaire à ceci:

```
@InjectQueryAdapter query;...public Map<String, ?> getSomeView(boolean sort, int skip, int limit) {    List<Map<String,?>> results = query.find(sort, skip, limit);    ...
```

Pour commencer, vous pouvez simuler l'objet _query_ et retourner ce que vous voulez pendant une exécution de test. Deuxièmement, il est clair ce que sont les différents paramètres d'après leurs noms. Cela limite également les permutations possibles qui doivent être testées. Par exemple: si _sort_ est _true_, les résultats retournés sont-ils triés? Si _limit_ est 1, obtenez-vous vraiment seulement **un** résultat? Et ainsi de suite.

Mais surtout, parce qu'aucune des méthodes appelées n'est statique, il est beaucoup plus facile de construire un contexte de test qui est facile à comprendre.

Enfin, si _QueryAdapter_ était une interface Java, vous pouvez échanger différentes implémentations à l'exécution (peut-être pilotées par la configuration), et le code qui l'utilise et le teste reste parfaitement valide.

#### Points à retenir

* utilisez [l'injection de dépendances](http://docs.spring.io/spring/docs/current/spring-framework-reference/html/beans.html) (DI) partout où c'est possible. [Spring](http://docs.spring.io/spring/docs/current/spring-framework-reference/html/beans.html) ou Guice sont des frameworks vraiment valides, et sont cruciaux pour garder votre code propre, réactif aux changements et testable.
* **évitez, dans la mesure du possible, les méthodes statiques**, sauf si vous **devez absolument le faire**. Elles rendent votre code difficile à tester, et vraiment difficile à simuler. Elles rendent également vos clients (le code qui utilisera vos classes/méthodes) extrêmement fragiles, et tout aussi intestables.
* Java est un langage fortement typé. Il y a une bonne raison à cela. Laissez le compilateur et la JVM faire le travail, et attrapez vos (et les) erreurs.
* **Évitez d'utiliser String et Object partout** comme un _poor man's_ langage dynamique. Si vous ne pouvez vraiment pas concevoir un modèle de données pour vos entités métier, vous devriez effectivement envisager un **vrai langage dynamique** (Python étant un excellent choix).
* **Documentez votre code.** Assurez-vous que toutes les méthodes publiques ont une documentation javadoc adéquate pour que les autres puissent comprendre et utiliser. Assurez-vous également que la documentation javadoc de vos classes explique clairement ce que fait la classe, comment l'utiliser, et aussi des exemples d'utilisation correcte (et, potentiellement, incorrecte aussi). Et, surtout, documentez vos APIs, ce que la méthode s'attend à recevoir, et ce qu'elles sont censées retourner.

Ce dernier point est particulièrement important: utilisez vos tests unitaires également comme un moyen de démontrer comment l'API de votre code devrait être utilisée (et comment elle ne devrait pas être utilisée).

#### Troisième odeur : code confus

Il m'a fallu le meilleur d'une heure pour inverser l'ingénierie de la méthode suivante. Ensuite, je l'ai passée à mes collègues comme un "Java Puzzler" et leurs devinettes étaient également largement confuses.

J'ai "obfusqué" une partie du code pour préserver la confidentialité et éviter l'embarras, mais faites-moi confiance, l'_obfuscation_ rend cette version **moins** obscure que l'original:

```
// Même si cela me fait mal, j'ai laissé le style de code (ou son absence) intact// PLEASE DON'T DO THIS AT HOMEprivate static String getSomething(boolean isOnRoute,         List<Map<String,Object>> trip,        String primarySomething, String id){    boolean somethingKnown = isOnRoute;    if(!somethingKnown && trip!=null){        for(Map<String,Object> segment: trip){            Map<String,Object> line = (Map<String, Object>) thisLeg.get(Constants.LINE);            if(line!=null){                String something = (String) carrierLane.get(Constants.SOMETHING);                LOG.debug("Line something: "+something);                if(primarySomething.equals(something)){                    somethingKnown = true;                    break;                }            }        }    }    if(somethingKnown){        return primarySomething;    }    LOG.debug("Unknown something:: isOnRoute:'" + isOnRoute + "' ; primarySomething:'" +            primarySomething + "' ; id:'" + id + "'");    return null;}
```

Pour vous sortir de votre misère, tout ce que fait cette méthode est de retourner la valeur (_primarySomething_) qui lui a été initialement donnée si le voyage _isOnRoute._ Si ce n'est pas le cas, elle vous le dira, puis retournera null — et laissons-nous passer un moment sur le fait qu'elle nécessite que l'appelant passe l'_id_ uniquement pour l'utiliser dans une déclaration de débogage.

De plus, notez l'utilisation inutile d'une variable booléenne (_somethingKnown_) uniquement pour l'utiliser dans le cas de la rupture, puis tomber dans une déclaration de retour. Et il y a tant d'autres problèmes ici. Par exemple, pourquoi assigner la valeur d'un drapeau qui indique si le voyage est "en route" à un drapeau qui indique si cet _something_ insaisissable a été trouvé?

Finalement, nous avons compris que cette méthode était entièrement inutile, et nous l'avons supprimée entièrement.

Triste à dire, appuyer sur la touche _DEL_ sur ce tas de merde a été le point culminant de ma journée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-rsB9AczUL4nA122DHiiYg.jpeg)

Voici quelques conseils pour éviter le code confus:

* Essayez de rendre l'intention de votre ou de vos méthodes évidemment claire pour les lecteurs de votre code. Suivez les conventions de nommage convenues, les listes d'arguments claires, les implémentations d'algorithmes claires, et aidez vos collègues à faire de même.
* Même en faisant cela, **ajoutez toujours une Javadoc** pour expliquer quelle est l'intention, ce que les arguments sont censés être, et quel devrait être le résultat attendu (y compris les effets secondaires possibles).
* Évitez les raccourcis qui rendront la logique de votre code obscure pour les autres développeurs.
* Et, pour l'amour de Dieu, évitez de concaténer des chaînes de caractères. Le _String.format()_ et le motif de composition de chaînes [_slf4j_](http://www.slf4j.org/) sont là pour une raison:

```
// Log4J:LOG.debug(String.format("Le résultat est: %d", result));
```

```
// logback ou slf4j: ceci est plus souhaitable, car vous n'aurez pas// le coût de la construction de la chaîne, sauf si le niveau de log// provoquera effectivement l'émission du message de logLOG.error("Le gizmo [{}] était dans {}, mais alors il a grillé à {}, {}",   gizmoId, state, foo, bar)
```

#### Quatrième odeur : Code copié-collé

Vous vous souvenez quand vous étiez enfant et qu'on vous demandait de "repérer la différence" entre deux images qui semblaient identiques? Jouons au jeu opposé. Pouvez-vous repérer les similitudes?

```
// Encore une fois, j'ai laissé le style de code (ou son absence) intact// PLEASE DON'T DO THIS AT HOMEList<Map<String, Object>> originSiteEvents = null;List<Map<String, Object>> destinationSiteEvents = null;List<Map<String, Object>> inventoryEvents = null;try{    originSiteEvents = (List<Map<String, Object>>) ((Map<String, Object>) ((Map)entry.get(ModelConstants.INVENTORY)).get(ModelConstants.ORIGIN)).get(ModelConstants.EVENTS);} catch (Exception e){    //No origin events availabl}try{    inventoryEvents = (List<Map<String, Object>>)  ((Map)entry.get(ModelConstants.INVENTORY)).get(ModelConstants.EVENTS);} catch (Exception e){    //No inventory events available}try{    destinationSiteEvents = (List<Map<String, Object>>) ((Map<String, Object>) ((Map)entry.get(ModelConstants.INVENTORY)).get(ModelConstants.DESTINATION)).get(ModelConstants.EVENTS);} catch (Exception e){    //No destination events available}if(events != null){    List<Map<String, Object>> eventListForLeg = (List<Map<String, Object>>) events;    for(int j=eventListForLeg.size()-1; j>=0; j--){        Map<String, Object> event = eventListForLeg.get(j);        if(event.get("category")!=null && event.get("category").equals("GPS")){            event.put("isLastGPSEvent", true);            break;        }    }}if(destinationSiteEvents != null){    for(int j=destinationSiteEvents.size()-1; j>=0; j--){        Map<String, Object> event = destinationSiteEvents.get(j);        if(event.get("category")!=null && event.get("category").equals("GPS")){            event.put("isLastGPSEvent", true);            return;        }    }}if(inventoryEvents != null){    for(int j=inventoryEvents.size()-1; j>=0; j--){        Map<String, Object> event = inventoryEvents.get(j);        if(event.get("category")!=null && event.get("category").equals("GPS")){            event.put("isLastGPSEvent", true);            return;        }    }}if(originSiteEvents != null){    for(int j=originSiteEvents.size()-1; j>=0; j--){        Map<String, Object> event = originSiteEvents.get(j);        if(event.get("category")!=null && event.get("category").equals("GPS")){            event.put("isLastGPSEvent", true);            return;        }    }}
```

Comme vous le savez probablement, copier-coller du code est une violation flagrante du principe DRY ("Don't Repeat Yourself"). Sans parler du fait que c'est assez horrible à regarder. Cela vous fera également passer pour un paresseux aux yeux de quiconque connaît les bases du développement logiciel.

Il est bon de mentionner que le même motif exact (naviguer dans des cartes imbriquées selon une séquence de chaînes) était dispersé partout dans les 600+ lignes de code de cette classe. Donc, vous seriez pardonnés d'avoir une méthode utilitaire comme celle que j'ai bricolée en moins de 10 minutes pour remplacer l'abomination ci-dessus:

```
/** * Navigue dans le {@literal path} dans la carte donnée et essaie * de récupérer la valeur sous forme de liste d'objets. * * <p>Ceci est sûr à utiliser, que le chemin existe ou non,  * et relativement sûr contre les erreurs de {@link java.lang.ClassCastException} * (dans la mesure où ce type de code peut l'être). * * @param map l'arbre JSON * @param path le chemin vers l'objet souhaité * @return la liste d'objets, ou {@literal null} si l'un des *     segments n'existe pas */@SuppressWarnings("unchecked")public static List<Map<String, ?>> tryPath(        Map<String, ?> map, List<String> path) {    List<Map<String, ?>> result = null;    Map<String, ?> intermediateNode = map;    String tail = path.remove(path.size() - 1);    for (String node : path) {        if (intermediateNode.containsKey(node)) {            Object o =  intermediateNode.get(node);            if (o instanceof Map) {                intermediateNode = (Map<String, ?>) o;            } else {                LOG.error("Le nœud intermédiaire {} ne peut pas être " +                    "converti en une Map ({})", node, o);                return null;            }        } else {            return null;        }    }    if (intermediateNode.containsKey(tail)) {        Object maybeList = intermediateNode.get(tail);        if (maybeList instanceof List) {            return (List<Map<String, ?>>) maybeList;        }    }    return null;}
```

Le résultat est que la séquence de recherches (qui, encore une fois, lorsqu'elles ont été rencontrées pour la première fois, ressemblaient à une énigme enveloppée dans un mystère) ressemble maintenant à ceci:

```
List<List<String>> paths = Lists.newArrayList();paths.add(Lists.newArrayList(Lists.asList(                ModelConstants.INVENTORY, new String[] {                ModelConstants.EVENTS})));paths.add(Lists.newArrayList(Lists.asList(                ModelConstants.INVENTORY, new String[] {                ModelConstants.ORIGIN,                ModelConstants.EVENTS})));paths.add(Lists.newArrayList(Lists.asList(                ModelConstants.INVENTORY, new String[] {                ModelConstants.DESTINATION,                ModelConstants.EVENTS})));List<Map<String, ?>> events = null;for (List<String> path : paths) {    events = tryPath(entry, path);    if (events != null) {        break;    }}if (events != null) {    for (int j = events.size() - 1; j >= 0; --j) {        Map<String, Object> event = (Map<String, Object>) events.get(j);        if (event.contains("category") && Constants.GPS.equals(event.get("category"))) {            event.put(Constants.isLastGPSEvent, true);            return;        }    }}
```

Cela n'est toujours pas aussi propre que je le voudrais, mais je blame principalement Java pour le manque d'une classe de fabrique similaire à _Lists_ de Scala:

```
val paths = List(List(ModelConstants.INVENTORY,                       ModelConstants.EVENTS,                 List(ModelConstants.INVENTORY,                      ModelConstants.ORIGIN,                      ModelConstants.EVENTS),                 List(ModelConstants.INVENTORY,                       ModelConstants.DESTINATION,                      ModelConstants.EVENTS))
```

De plus, une note rapide sur l'anti-modèle consistant à utiliser un bloc _try-catch_ pour filtrer les chemins de code potentiellement valides, et éviter d'écrire des vérifications de null et d'existence de clés.

En factorisant les vérifications et les conversions de classe (avec des vérifications de type appropriées) en un seul endroit, vous évitez d'avoir à choisir entre deux mauvaises options, qui sont: disperser les mêmes vérifications répétitives et fastidieuses partout, ou masquer les codes d'erreur possibles en jetant un filet très large.

Si vous laissez passer des conditions potentiellement erronées, vous rendrez extrêmement difficile la découverte des causes profondes des bugs inattendus.

Il y a tout un article de blog à écrire sur "l'avalement" des exceptions et des conditions d'erreur.

![Image](https://cdn-media-1.freecodecamp.org/images/0*1iciOILG0-OWerBy.)

Donc:

* **ne copiez pas et ne collez pas le code**: si vous voyez une similitude, factorisez les parties communes et réutilisez-les (dans une classe utilitaire ou une méthode auxiliaire);
* ne contournez pas les vérifications de sécurité dans votre code en avalant de manière indiscriminée les exceptions: les blocs _try-catch_ doivent être là pour une raison, et la raison devrait être (le signe révélateur étant dans le nom) _exceptionnelle_.

**Le code reste largement un artisanat**. Une compréhension approfondie des problèmes liés à l'informatique distribuée, une capacité de raisonnement critique et de pensée abstraite, et une compréhension des problèmes opérationnels liés aux systèmes évolutifs — tout cela est crucial de nos jours pour devenir un grand développeur de logiciels. Pourtant, la maîtrise de l'artisanat est aussi importante qu'elle l'était en Italie à la Renaissance.

Écrivez un code bien conçu, clairement structuré et correctement documenté — et soyez fier de votre artisanat!

Et si vous voulez vous moquer de **mon** code, allez simplement sur [mes dépôts github](https://github.com/massenz), je suis sûr qu'il y a encore beaucoup d'odeurs là-bas (mais, espérons-le, aussi quelques pépites de bon code qui vous inspireront!)

_Initialement publié sur [codetrips.com](https://codetrips.com/2015/01/25/do-not-allow-bad-smells-in-your-code/) le 25 janvier 2015._