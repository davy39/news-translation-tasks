---
title: Découverte d'ingénieures formidables dans la communauté GraphQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-02T20:48:08.000Z'
originalURL: https://freecodecamp.org/news/discovering-awesome-female-engineers-in-the-graphql-community-88ddf45e4ce1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U1Vc4FYB7Bs4n_kT00Q_YQ.png
tags:
- name: community
  slug: community
- name: GraphQL
  slug: graphql
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: women in tech
  slug: women-in-tech
seo_title: Découverte d'ingénieures formidables dans la communauté GraphQL
seo_desc: 'By Michael Hunger

  An interesting use of our community-graph project and gender-API

  A while back, I came across Peggy’s Twitter request:

  Which got a really cool response from Bonnie that warmed my heart:

  And triggered an idea …

  Developer Community Act...'
---

Par Michael Hunger

#### Une utilisation intéressante de notre projet community-graph et de gender-API

Il y a quelque temps, je suis tombé sur la demande de Peggy sur Twitter :

Qui a reçu une réponse vraiment cool de Bonnie qui m'a réchauffé le cœur :

Et qui a déclenché une idée…

### Données d'activité de la communauté des développeurs

Comme vous le savez peut-être, nous nous amusons beaucoup à montrer l'engagement impressionnant des développeurs dans leurs communautés (par exemple GraphQL, Neo4j, …) en un seul endroit en les important dans un « Community Graph ». Habituellement, il est vraiment difficile de suivre le flot d'activité sur Twitter, Slack, StackOverflow, GitHub, et ainsi de suite pour rester au courant de ce qui se passe. Surtout si votre communauté grandit rapidement.

Nous avons donc gratté une démangeaison et importons en continu (via AWS Lambda) l'activité de la communauté Neo4j dans un seul graphe, qui peut ensuite être interrogé et visualisé — et qui est [accessible ici](https://github.com/community-graph/documentation).

Nous avons fait de même pour la **communauté GraphQL**, car leurs données sont également [accessibles via GraphiQL](http://graphql.communitygraph.org/) et [documentées ici](https://github.com/neo4j-graphql/graphql-community).

![Image](https://cdn-media-1.freecodecamp.org/images/1*U1Vc4FYB7Bs4n_kT00Q_YQ.png)
_GraphQL Community Graph_

Ainsi, comme nous avions toutes les activités de GraphQL des derniers mois dans notre base de données de graphes, j'ai pensé qu'il serait cool de l'utiliser pour répondre à la demande de Peggy.

Vous pouvez accéder aux données **en lecture seule** ici : [http://107.170.69.23:7474/browser/](http://107.170.69.23:7474/browser/) en utilisant « **graphql** » comme nom d'utilisateur et mot de passe.

Voyons si nous pouvons trouver l'une des femmes (Bonnie Brennan) actives dans le fil Twitter de Peggy, qui tweete sur GraphQL, et montrer ses tweets et leurs tags.

_Nous utilisons ici le langage de requête de Neo4j [Cypher](http://neo4j.com/developer/cypher), en **correspondant** au motif ASCII-art de « un utilisateur publiant des tweets tagués avec ces tags » puis en liant le screen_name de l'utilisateur à 'bonnster75' et en **retournant** tout ce que nous avons trouvé._

```
MATCH (user:Twitter:User)-[:POSTED]->(t:Tweet)-[:TAGGED]->(tag:Tag)WHERE user.screen_name = 'bonnster75'RETURN *
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*BjgoRjLaNRwOPid0xY3LOQ.jpeg)

### Détermination du genre

Une façon simple de prédire le genre est de regarder le prénom. Je sais que ce n'est pas très fiable, mais nous cherchons seulement des suggestions que nous vérifierons manuellement plus tard. Ensuite, le pouvoir du réseau peut révéler d'autres candidats.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ePvswvSScnydMJsRBMGaOg.png)

J'ai googlé « gender api » et trouvé [ce site](https://gender-api.com/), qui semblait vraiment bien et offrait 500 requêtes mensuelles gratuites et une API HTTP simple. Parfait pour mon objectif de fin de nuit (3h du matin).

J'ai testé quelques-uns des noms qui sont revenus à la demande de Peggy :
Peggy, Bonnie, Belén, Robin, Danielle, et Morgan.
Malheureusement, seulement quelques-uns lui ont été recommandés, alors j'espérais pouvoir faire mieux.

J'ai utilisé la vérification interactive du prénom sur la page d'accueil de gender-API, ce qui a donné ces résultats. _J'ai dû changer le pays en « US » car mon pays par défaut (« DE ») n'avait pas le bon mapping pour Robin et Morgan._

![Image](https://cdn-media-1.freecodecamp.org/images/1*UGAdqdOTIBtmrmi9Tzh0sA.jpeg)

```
Peggy{"name":"peggy","country":"US","gender":"female","samples":3015,"accuracy":99,"duration":"51ms"}Bonnie{"name":"bonnie","country":"US","gender":"female","samples":3984,"accuracy":98,"duration":"25ms"}Morgan{"name":"morgan","country":"US","gender":"female","samples":5956,"accuracy":76,"duration":"33ms"}Belén{"name":"belén","country":"US","gender":"female","samples":35,"accuracy":97,"duration":"64ms"}Danielle {"name":"danielle","country":"US","gender":"female","samples":12284,"accuracy":99,"duration":"47ms"}Robin{"name":"robin","country":"US","gender":"female","samples":8088,"accuracy":83,"duration":"31ms"}
```

Sur la base de ces données, je pense qu'il est judicieux de ne regarder que les résultats avec **une précision de plus de 75 et au moins 10 échantillons**.

Vous pouvez utiliser l'API HTTP comme ceci :
 `https://gender-api.com/get?key=<key>&country=US&name`=peggy

### Détection de genre pour les utilisateurs Twitter de Community Graph

Essayons la même chose pour notre community-graph :

1. Nous **correspondons** aux utilisateurs Twitter par une liste de screen-names, et
2. **divisons** leur nom par espace et prenons le **premier mot** comme prénom.
3. Que nous **envoyons** ensuite à l'API « gender-api » (en appelant une procédure définie par l'utilisateur) et
4. obtenons le résultat sous forme de map-**valeur**.
5. Nous ne voulons **retourner que quelques attributs** de notre nœud utilisateur.

```
MATCH (user:Twitter:User) WHERE user.screen_name IN ['bonnster75','peggyrayzis','okbel','morgancodes', 'robin_heinze','danimman']
```

```
WITH user, head(split(user.name," ")) as firstname
```

```
CALL apoc.load.json("https://gender-api.com/get?key=<key>&country=US&name="+firstname) YIELD value
```

```
RETURN user { .screen_name, .name, .followers, .statuses} as user_data, firstname, value;
```

Cela a bien fonctionné. Bien que Morgan ait été recommandée à Peggy, elle n'avait pas encore tweeté et ne serait probablement pas dans notre liste des « plus actifs ».

```
user:  {"name":"Bonnie Brennan","screen_name":"bonnster75",        "followers":"467","statuses":"2831"}value: {"name":"bonnie","accuracy":"98","samples":"3984",        "country":"US","gender":"female"}user:  {"name":"Belén Curcio","screen_name":"okbel",        "followers":"3821","statuses":"35721"}value: {"name":"belén","accuracy":"97","samples":"35",        "country":"US","gender":"female"}user:  {"name":"Morgan Laco","screen_name":"morgancodes",        "followers":null,"statuses":null}value: {"name":"morgan","accuracy":"76","samples":"5956",        "country":"US","gender":"female"}
```

Maintenant, nous voulons trouver les femmes **les plus actives** qui tweetent sur GraphQL. Un **score** pourrait contenir le **nombre de tweets**, et la fréquence à laquelle ces tweets ont été **favorisés, retweetés ou répondus**. C'est ce que nous faisons ici, nous trouvons les utilisateurs qui ont posté des tweets, calculons ce score par utilisateur, et retournons les 500 premiers triés par score.

```
MATCH (u:Twitter:User)-[:POSTED]->(t:Tweet)WITH u, count(*) as tweets,      sum(t.favorites+size((t)<-[:RETWEETED|REPLIED_TO]-())) as scoreWHERE tweets > 5 AND tweets * score > 100RETURN u.name, u.screen_name, tweets, scoreORDER BY tweets * score DESC LIMIT 500
```

En regardant les résultats, cela a du sens :

```
┌──────────────────────┬────────────────┬────────┬────────┐
│"u.name"             │"u.screen_name" │"tweets"│"score" │
├──────────────────────┼────────────────┼────────┼────────┤
│"Sashko Stubailo"    │"stubailo"     │"538"  │"1567" │
├──────────────────────┼────────────────┼────────┼────────┤
│"Apollo"             │"apollographql"│"150"  │"1389" │
├──────────────────────┼────────────────┼────────┼────────┤
│"ReactDOM"           │"ReactDOM"     │"221"  │"596"  │
├──────────────────────┼────────────────┼────────┼────────┤
│"KOYCHEV.DE"         │"K0YCHEV"      │"309"  │"341"  │
├──────────────────────┼────────────────┼────────┼────────┤
│"Graphcool"          │"graphcool"    │"84"   │"859"  │
├──────────────────────┼────────────────┼────────┼────────┤
│"adeeb"              │"_adeeb"       │"179"  │"328"  │
├──────────────────────┼────────────────┼────────┼────────┤
│"ReactJS News"       │"ReactJS_News" │"93"   │"517"  │
├──────────────────────┼────────────────┼────────┼────────┤
│"Max Stoiber"        │"mxstbr"       │"102"  │"450"  │
├──────────────────────┼────────────────┼────────┼────────┤
│"Caleb Meredith"     │"calebmer"     │"135"  │"273"  │
├──────────────────────┼────────────────┼────────┼────────┤
│"Lee Byron"          │"leeb"         │"53"   │"652"  │
└──────────────────────┴────────────────┴────────┴────────┘
```

Cool, maintenant nous pouvons combiner nos deux déclarations. Pour économiser quelques appels d'API répétés, je **stocke simplement les informations de genre** sur l'entité utilisateur (également la précision et les échantillons) afin que nous puissions les réutiliser plus tard.

```
MATCH (u:Twitter:User)-[:POSTED]->(t:Tweet)// name has have at least 2 parts, and gender not yet retrievedWHERE u.name contains " " AND NOT exists(u.gender)
```

```
// compute the scoreWITH u, count(*) AS tweets,      sum(t.favorites+size((t)<-[:RETWEETED|REPLIED_TO]-())) AS scoreWHERE tweets > 5 AND tweets * score > 100
```

```
// top 500 usersWITH u, tweets, score, head(split(u.name," ")) as firstnameORDER BY tweets * score DESC LIMIT 500
```

```
// call gender apiCALL apoc.load.json("https://gender-api.com/get?key=<key>&name="+firstname) YIELD value
```

```
// set result values as propertiesSET u.gender = value.gender,     u.gender_meta = [value.accuracy,value.samples]
```

```
RETURN count(*)
```

Ainsi, pour les 500 meilleurs comptes avec un espace dans leur nom, nous avons obtenu la prédiction de genre via l'API. Maintenant, nous pouvons examiner nos données résultantes, et espérons trouver quelques femmes que nous pouvons _recommander à Peggy_.

```
MATCH (u:Twitter:User)-[:POSTED]->(t:Tweet)WHERE u.gender = "female"   AND u.gender_meta[0] > 75 and u.gender_meta[1] > 10
```

```
WITH u, count(*) AS tweets,      sum(t.favorites+size((t)<-[:RETWEETED|REPLIED_TO]-())) AS scoreORDER BY tweets * score DESC LIMIT 50
```

```
RETURN u { .screen_name, .name, .followers, .following, .statuses} as user, tweets, score;
```

En plus des résultats amusants (Ruby Inside, Else if), et des mal classés (Jess, Brooke), nous obtenons un certain nombre de femmes actives dans la communauté GraphQL qui n'avaient pas été recommandées auparavant :
**ladyleet, _KarimaTounsya, thekamahele, lauralindal, thelamkin, eveporcello** et plusieurs autres.

J'ai manuellement passé en revue les screen-names, regardé ces profils Twitter, et mis une coche **✓** pour les comptes féminins et un **!** pour les nouveaux noms.

Nous avons trouvé **22 femmes au total** — ce qui n'est bien sûr pas beaucoup si l'on regarde le nombre absolu de personnes tweetant sur GraphQL, mais c'est un début et espérons-le en croissance rapide.

Maintenant que nous avons notre liste, utilisons-la à bon escient ! Assurez-vous de vérifier le travail de ces femmes talentueuses et actives et suivez-les sur Twitter si vous ne le faites pas déjà. En reconnaissant leurs contributions, nous pouvons **espérer inspirer plus de femmes à être des membres actifs de la communauté GraphQL** et découvrir plus de noms pour notre liste à l'avenir.

**PS :** Nous avons entendu de Nikolas, le curateur de [@graphqlweekly](http://twitter.com/graphqlweekly), que notre [page de vue d'ensemble « cette semaine dans GraphQL »](http://s3-eu-west-1.amazonaws.com/twigraphql/twigraphql.html) les a beaucoup aidés dans la compilation de la newsletter hebdomadaire. Elle propose également un onglet « Twitter Active », qui devrait vous aider à trouver des personnes à suivre, également.

Nous sommes également heureux de **proposer le service de graphe communautaire à d'autres communautés**, alors n'hésitez pas à nous contacter via [devrel@neo4j.com](mailto:devrel@neo4j.com), si vous êtes intéressé.

**PPS :** Un grand merci à Peggy Rayzis qui a lancé cette activité engageante, fourni des commentaires très précieux pour cet article, et donné son autorisation pour la publication. Assurez-vous de la suivre sur [Twitter](https://twitter.com/peggyrayzis) et ici sur [Medium](https://medium.com/@peggyrayzis).