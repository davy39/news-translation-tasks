---
title: Qui a le plus contribué à l'open source en 2017 et 2018 ? Analysons les données
  de GitHub pour le découvrir.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-24T21:01:28.000Z'
originalURL: https://freecodecamp.org/news/the-top-contributors-to-github-2017-be98ab854e87
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/1_Qgsj8DRAKucO4yMpUiwHvw-1.png
tags:
- name: bigquery
  slug: bigquery
- name: Data Science
  slug: data-science
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Qui a le plus contribué à l'open source en 2017 et 2018 ? Analysons les
  données de GitHub pour le découvrir.
seo_desc: 'By Felipe Hoffa

  For this analysis we’ll look at all the PushEvents published by GitHub during 2017.
  For each GitHub user we’ll have to make our best guess to determine to which organization
  they belong. We’ll only look at repositories that have recei...'
---

Par Felipe Hoffa

Pour cette analyse, nous examinerons tous les `PushEvents` publiés par GitHub en 2017. Pour chaque utilisateur GitHub, nous devrons faire notre meilleure estimation pour déterminer à quelle organisation il appartient. Nous ne regarderons que les dépôts qui ont reçu au moins 20 étoiles cette année.

Voici les résultats que j'ai obtenus, que vous pouvez [explorer dans mon rapport interactif Data Studio](https://datastudio.google.com/open/0ByGAKP3QmCjLU1JzUGtJdTlNOG8).

### Comparaison des principaux fournisseurs de cloud

En examinant GitHub en 2017 :

* Microsoft semble avoir ~1 300 employés qui poussent activement du code vers 825 dépôts populaires sur GitHub.
* Google affiche ~900 employés actifs sur GitHub, qui poussent du code vers ~1 100 dépôts populaires.
* Amazon semble n'avoir que 134 employés actifs sur GitHub, poussant du code vers seulement 158 projets populaires.
* Tous les projets ne sont pas égaux : Bien que les Googlers contribuent à 25 % de dépôts en plus que Microsoft, ces dépôts ont accumulé beaucoup plus d'étoiles (530 000 contre 260 000). Le total des étoiles pour les dépôts Amazon en 2017 ? 27 000.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EfhT-K6feRjyifX_K49AFg.png)

### RedHat, IBM, Pivotal, Intel et Facebook

Si Amazon semble si loin derrière Microsoft et Google — quelles sont les entreprises entre les deux ? Selon ce classement, RedHat, Pivotal et Intel apportent d'excellentes contributions à GitHub :

Notez que le tableau suivant combine tous les domaines régionaux d'IBM — tandis que les régions individuelles apparaissent toujours dans les tableaux suivants.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KnaOtVpdmPFabCtk-saYUw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dy08nNIdjxBQRqQ6zXTThg.png)

Facebook et IBM (US) ont un nombre similaire d'utilisateurs GitHub à Amazon, mais les projets auxquels ils contribuent ont accumulé plus d'étoiles (surtout Facebook) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZJP36ojAFyo7BcZnJ-PT3Q.png)

Suivis par Alibaba, Uber et Wix :

![Image](https://cdn-media-1.freecodecamp.org/images/1*yG3X8Sq35S8Z9mNLv9pliA.png)

GitHub lui-même, Apache, Tencent :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ij2hSTZiQndHdFRsFNwb-g.png)

Baidu, Apple, Mozilla :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZRjQ0fNe39-qox3cy6OGUQ.png)

Oracle, Stanford, Mit, Shopify, MongoDb, Berkeley, VmWare, Netflix, Salesforce, Gsa.gov :

![Image](https://cdn-media-1.freecodecamp.org/images/1*mi1gdgVUYRbTBoBuo14gtA.png)

LinkedIn, Broad Institute, Palantir, Yahoo, MapBox, Unity3d, Automattic, Sandia, Travis-ci, Spotify :

![Image](https://cdn-media-1.freecodecamp.org/images/1*yQzsoab7AFbQ2BTnPCGbXg.png)

Chromium, UMich, Zalando, Esri, IBM (UK), SAP, EPAM, Telerik, UK Cabinet Office, Stripe :

![Image](https://cdn-media-1.freecodecamp.org/images/1*TCbZaq4sgpjFQ9f4yFoWoQ.png)

Cern, Odoo, Kitware, Suse, Yandex, IBM (Canada), Adobe, AirBnB, Chef, The Guardian :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zXxtygHJUi4tdNr1JRNlyg.png)

Arm, Macports, Docker, Nuxeo, NVidia, Yelp, Elastic, NYU, WSO2, Mesosphere, Inria

![Image](https://cdn-media-1.freecodecamp.org/images/1*f6AK5xHrJIAhEn7t9569lQ.png)

Puppet, Stanford (CS), DatadogHQ, Epfl, NTT Data, Lawrence Livermore Lab :

![Image](https://cdn-media-1.freecodecamp.org/images/1*RP5nyYdwn2d2pb05xnMxyA.png)

### Ma méthodologie

#### Comment j'ai lié les utilisateurs GitHub aux entreprises

Déterminer l'organisation à laquelle appartient chaque utilisateur GitHub n'est pas facile — mais nous pouvons utiliser les domaines d'email qui apparaissent dans chaque message de commit contenu dans les PushEvents :

* Le même email peut apparaître pour plus d'un utilisateur, donc je n'ai considéré que les utilisateurs GitHub capables de pousser du code vers des projets GitHub avec plus de 20 étoiles pendant la période.
* Je n'ai compté que les utilisateurs GitHub avec plus de 3 pushes pendant la période.
* Les utilisateurs poussant du code vers GitHub peuvent afficher de nombreux emails différents sur leurs pushes — c'est une partie du fonctionnement de Git. Pour déterminer l'organisation pour chaque utilisateur, j'ai examiné l'email qui apparaît le plus fréquemment dans leurs pushes.
* Tout le monde n'utilise pas son email professionnel sur GitHub. Il y a beaucoup de gmail.com, users.noreply.github.com et d'autres fournisseurs d'hébergement d'email. Parfois, la raison en est l'anonymat et la protection de leurs boîtes mail professionnelles — mais si je ne pouvais pas voir leur domaine d'email, je ne pouvais pas les compter. Désolé.
* Parfois, les employés changent d'organisation. Je les ai assignés à celle qui a obtenu le plus de pushes selon ces règles.

#### Ma requête

```
#standardSQLWITHperiod AS (  SELECT *  FROM `githubarchive.month.2017*` a),repo_stars AS (  SELECT repo.id, COUNT(DISTINCT actor.login) stars, APPROX_TOP_COUNT(repo.name, 1)[OFFSET(0)].value repo_name   FROM period  WHERE type='WatchEvent'  GROUP BY 1  HAVING stars>20), pushers_guess_emails_and_top_projects AS (  SELECT *    # , REGEXP_EXTRACT(email, r'@(.*)') domain    , REGEXP_REPLACE(REGEXP_EXTRACT(email, r'@(.*)'), r'.*.ibm.com', 'ibm.com') domain  FROM (    SELECT actor.id      , APPROX_TOP_COUNT(actor.login,1)[OFFSET(0)].value login      , APPROX_TOP_COUNT(JSON_EXTRACT_SCALAR(payload, '$.commits[0].author.email'),1)[OFFSET(0)].value email      , COUNT(*) c      , ARRAY_AGG(DISTINCT TO_JSON_STRING(STRUCT(b.repo_name,stars))) repos    FROM period a    JOIN repo_stars b    ON a.repo.id=b.id    WHERE type='PushEvent'    GROUP BY  1    HAVING c>3  ))SELECT * FROM (  SELECT domain    , githubers    , (SELECT COUNT(DISTINCT repo) FROM UNNEST(repos) repo) repos_contributed_to    , ARRAY(        SELECT AS STRUCT JSON_EXTRACT_SCALAR(repo, '$.repo_name') repo_name        , CAST(JSON_EXTRACT_SCALAR(repo, '$.stars') AS INT64) stars        , COUNT(*) githubers_from_domain FROM UNNEST(repos) repo         GROUP BY 1, 2         HAVING githubers_from_domain>1         ORDER BY stars DESC LIMIT 3      ) top    , (SELECT SUM(CAST(JSON_EXTRACT_SCALAR(repo, '$.stars') AS INT64)) FROM (SELECT DISTINCT repo FROM UNNEST(repos) repo)) sum_stars_projects_contributed_to  FROM (    SELECT domain, COUNT(*) githubers, ARRAY_CONCAT_AGG(ARRAY(SELECT * FROM UNNEST(repos) repo)) repos    FROM pushers_guess_emails_and_top_projects    #WHERE domain IN UNNEST(SPLIT('google.com|microsoft.com|amazon.com', '|'))    WHERE domain NOT IN UNNEST(SPLIT('gmail.com|users.noreply.github.com|qq.com|hotmail.com|163.com|me.com|googlemail.com|outlook.com|yahoo.com|web.de|iki.fi|foxmail.com|yandex.ru|126.com|protonmail.com', '|')) # email hosters    GROUP BY 1    HAVING githubers > 30  )  WHERE (SELECT MAX(githubers_from_domain) FROM (SELECT repo, COUNT(*) githubers_from_domain FROM UNNEST(repos) repo  GROUP BY repo))>4 # second filter email hosters)ORDER BY githubers DESC
```

### FAQ

#### **Si une organisation a 1 500 dépôts, pourquoi n'en comptez-vous que 200 ? Si un dépôt a 7 000 étoiles, pourquoi n'en affichez-vous que 1 500 ?**

Je filtre pour la pertinence. Je ne compte que les étoiles données en 2017. Par exemple, Apache a >1 500 dépôts sur GitHub, mais seulement 205 ont reçu plus de 20 étoiles cette année.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wf86s1GygY1u283nA6LoYQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*vjycrF8zFYdJIBCV2HEkCg.png)

#### Est-ce l'état de l'open source ?

Notez que l'analyse de GitHub n'inclut pas les principales communautés comme Android, Chromium, GNU, Mozilla, ni les fondations Apache ou Eclipse, et [d'autres](https://developers.google.com/open-source/organizations) projets qui choisissent de mener la plupart de leurs activités en dehors de GitHub.

#### **Vous avez été injuste envers mon organisation.**

Je ne peux compter que ce que je peux voir. Veuillez remettre en question mes hypothèses et me dire comment vous mesureriez les choses de manière meilleure. Des requêtes fonctionnelles seraient le meilleur moyen.

Par exemple, voyez comment leur classement change lorsque je combine les domaines régionaux d'IBM en un seul avec une transformation SQL :

```
SELECT *, REGEXP_REPLACE(REGEXP_EXTRACT(email, r'@(.*)'), r'.*.ibm.com', 'ibm.com') domain
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*sKjuzOO2OYPcKGAzq9jDYw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ywkHH3kMMVdGhXe6LDq7IA.png)
_La position relative d'IBM change significativement lorsque vous combinez leurs domaines d'email régionaux._

#### Réactions

[**Quelques réflexions sur "les principaux contributeurs à GitHub 2017".**](https://redmonk.com/jgovernor/2017/10/25/some-thoughts-on-the-top-contributors-to-github-2017/)  
[_Hier, Felipe Hoffa de l'équipe Google Dev Rel a publié une recherche intéressante sur l'utilisation des entreprises de... redmonk.com](https://redmonk.com/jgovernor/2017/10/25/some-thoughts-on-the-top-contributors-to-github-2017/)

### Prochaines étapes

Je me suis déjà trompé — et cela se reproduira probablement. Veuillez examiner toutes les données brutes disponibles et remettre en question toutes mes hypothèses — ce sera intéressant de voir quels résultats vous obtiendrez.

[Jouez avec le rapport interactif Data Studio](https://datastudio.google.com/open/0ByGAKP3QmCjLU1JzUGtJdTlNOG8).

Merci à [Ilya Grigorik](https://www.freecodecamp.org/news/the-top-contributors-to-github-2017-be98ab854e87/undefined) pour avoir maintenu [GitHub Archive](http://githubarchive.org) bien alimenté et rempli de données GitHub toutes ces années !

Vous voulez plus d'histoires ? Consultez mon [Medium](http://medium.com/@hoffa/), [suivez-moi sur twitter](http://twitter.com/felipehoffa), et abonnez-vous à [reddit.com/r/bigquery](https://reddit.com/r/bigquery). Et [essayez BigQuery](https://www.reddit.com/r/bigquery/comments/3dg9le/analyzing_50_billion_wikipedia_pageviews_in_5/) — chaque mois, vous obtenez un téraoctet complet d'analyse [gratuitement](https://cloud.google.com/blog/big-data/2017/01/how-to-run-a-terabyte-of-google-bigquery-queries-each-month-without-a-credit-card).

[**Mener avec des virgules — laid ou efficace ? Une enquête sur 320 Go de code SQL**](https://hackernoon.com/winning-arguments-with-data-leading-with-commas-in-sql-672b3b81eac9)  
[_Gagner des arguments avec des données : Analysons 320 gigaoctets de code SQL open source pour déterminer si nous devons utiliser des virgules... hackernoon.com](https://hackernoon.com/winning-arguments-with-data-leading-with-commas-in-sql-672b3b81eac9)[**Certains codeurs aiment la chaleur — mais la plupart préfèrent les climats plus froids**](https://hackernoon.com/some-coders-like-it-hot-but-most-prefer-colder-climates-4703c3f02fbb)  
[_Précédemment, nous avons trouvé certaines des principales concentrations de codeurs open source autour d'endroits assez froids (Islande, Suède... hackernoon.com](https://hackernoon.com/some-coders-like-it-hot-but-most-prefer-colder-climates-4703c3f02fbb)