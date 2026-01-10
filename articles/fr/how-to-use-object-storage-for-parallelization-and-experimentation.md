---
title: Comment utiliser le stockage objet pour la parallélisation et l'expérimentation
  des données
subtitle: ''
author: Ry Vee
co_authors: []
series: null
date: '2021-09-27T14:09:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-object-storage-for-parallelization-and-experimentation
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/article-cover-pic.png
tags:
- name: big data
  slug: big-data
- name: data analysis
  slug: data-analysis
- name: data analytics
  slug: data-analytics
- name: storage
  slug: storage
seo_title: Comment utiliser le stockage objet pour la parallélisation et l'expérimentation
  des données
seo_desc: "By using big data, companies can learn a lot about how their businesses\
  \ are performing. Analytics on sales, churn rates, and other basic metrics are available\
  \ in almost real time as data comes in. \nThen there are more complex analyses that\
  \ you'll nee..."
---

En utilisant le big data, les entreprises peuvent en apprendre beaucoup sur la performance de leurs activités. Des analyses sur les ventes, les taux d'attrition (churn) et d'autres indicateurs de base sont disponibles presque en temps réel au fur et à mesure que les données arrivent.

Il existe ensuite des analyses plus complexes que vous devrez effectuer. Parfois, les relations entre deux ensembles de données apparemment sans rapport peuvent fournir des informations surprenantes et dévoiler des opportunités importantes pour l'organisation.

Les data scientists et les ingénieurs continuent d'améliorer la façon dont ils décomposent et travaillent sur les données. L'expérimentation implique de découvrir les bonnes corrélations entre les points de données.

Cela signifie qu'ils doivent également effectuer une sorte de parallélisation de ces données et des modèles qui en résultent. La parallélisation signifie simplement que le même ensemble de données est exploité de nombreuses manières différentes sans compromettre l'intégrité des données d'origine.

Dans cet article, nous allons voir comment vous pouvez vous assurer que vous effectuez cette expérimentation et ce traitement parallèle de manière efficace et qu'ils fournissent un maximum d'informations. Nous aborderons différents concepts liés au stockage des données et au versionnage des données.

# Stockage bloc vs Stockage objet

Pour les non-initiés, nous devons d'abord comprendre la différence entre le stockage bloc et le stockage objet, et pourquoi ce dernier est la meilleure option lorsqu'on traite de l'expérimentation de données.

![Image](https://lh4.googleusercontent.com/p8F4n7jqjmQtqquQasDGPEj1eRdxhNIsdMFxX9gIM03w6r6u-VRzU6rn2gMqdF1U3lrGOrjWEPwlBFzR-0cYVHWBWF7tigFiS4m_EtYjw0bU4tPATeWsZNYTFwpZTbyLBAzxqmbX=s0)
_[Source de l'image](https://res.cloudinary.com/practicaldev/image/fetch/s--PYImgKrK--/c_imagga_scale,f_auto,fl_progressive,h_500,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4519hl0nf6aze73pyvsr.png)_

## Qu'est-ce que le stockage bloc ?

On l'appelle « stockage bloc » (également connu sous le nom de [SAN](https://www.snia.org/education/storage_networking_primer/san/what_san)) parce que chaque ensemble de données (sous forme de fichiers) est regroupé en blocs stockés sur des disques.

Un exemple classique de stockage bloc est le système de fichiers de votre ordinateur personnel. Pour les cas d'utilisation en entreprise, il est mis à l'échelle via un réseau de disques durs connectés par des câbles en fibre optique.

L'utilisation du stockage bloc présente quelques inconvénients. Premièrement, si un secteur (ou un bloc) est corrompu, cela peut endommager les fichiers. Un autre problème est le manque d'évolutivité (l'extension du réseau de câbles en fibre optique est coûteuse).

## Qu'est-ce que le stockage objet ?

Dans le stockage objet, les données sont stockées sous forme d'objets. Chaque objet contient les données réelles, appelées le blob, un identifiant unique (UUID) et des métadonnées, qui contiennent des informations sur l'objet (telles que l'horodatage, la version et l'auteur).

Le stockage objet permet de faire évoluer votre stockage de données de manière rentable — vous n'avez pas besoin de matériel complexe pour cela. Il rend également la récupération des données plus rapide car chaque objet peut être récupéré via son UUID.

Cela contraste avec le stockage bloc, où chaque emplacement de données doit être identifié avant que l'information réelle puisse être récupérée.

Un inconvénient du stockage objet est que les données ne peuvent être écrites qu'une seule fois et ne peuvent pas être mises à jour. Mais ce n'est pas vraiment un inconvénient, comme nous le verrons plus loin dans cet article.

## Quels problèmes le stockage objet résout-il ?

Comme nous l'avons déjà vu, la récupération des données peut être incroyablement rapide avec le stockage objet (quelle que soit la taille du stockage). Mais lorsqu'il s'agit d'expérimentation et de parallélisation des données, le stockage objet brille de mille feux.

Comme mentionné précédemment, vous ne pouvez pas écraser des données déjà stockées en tant qu'objet. Cela garantit que le stockage objet est protégé contre la destruction ou la mise à jour non souhaitée (ou non autorisée) des données. C'est une excellente chose à savoir si vous effectuez beaucoup de traitements de données où une corruption accidentelle des informations pourrait se produire.

Un autre problème que le stockage objet peut résoudre est qu'il ne nécessite pas que les données soient structurées. Comme les entreprises produisent et consomment d'énormes quantités d'informations à chaque instant, les données non structurées (telles que les PDF, les vidéos, les images) ne sont souvent pas facilement transformées en formes utiles (comme pour l'analytique ou les tableaux de bord).

Avec le stockage objet, cela est désormais possible. Vous pouvez maintenant utiliser des données non structurées pour développer des modèles de machine learning.

Avec le stockage de données, il est possible d'avoir différentes versions du même blob (avec des métadonnées différentes). Tout comme il existe Git pour le contrôle de version du code, nous pouvons avoir des moyens similaires de gérer différentes versions des mêmes données.

Cela nous amène au concept de lacs de données (data lakes).

## Que sont les lacs de données ?

Les lacs de données sont des dépôts centraux de données qui ne se soucient pas du format de ces données.

Les entreprises produisent et consomment d'énormes quantités de données. Traditionnellement, ces données se trouvent dans des silos parce qu'elles appartiennent à différents départements ou se présentent sous différentes formes (par exemple, les vidéos ne sont pas stockées dans le même répertoire que les données de la base de données MySQL).

Avec les lacs de données, n'importe quel département de l'entreprise peut stocker des informations sans avoir besoin de les prétraiter. De même, n'importe quelle donnée peut être récupérée et analysée par n'importe qui de n'importe quel département.

Les lacs de données sont importants car ils rendent l'analyse des données extrêmement rapide et pratique.

## Comment l'expérimentation et la parallélisation des données fonctionnent avec le stockage objet

Comme pour le développement de logiciels, le travail sur les données nécessite l'utilisation d'outils capables de nous aider dans notre flux de travail. Un outil open source puissant pour expérimenter avec les données et effectuer de la parallélisation (c'est-à-dire travailler sur les mêmes données pour créer différents ensembles de modèles de machine learning) est LakeFS.

LakeFS est une plateforme open source qui offre des fonctionnalités de type Git lors du travail sur les données. Cela signifie que vous pouvez créer des branches (vous permettant d'expérimenter avec les données) et effectuer des Commit de versions de données (et de modèles de données).

### Pourquoi cette fonctionnalité de type Git est-elle importante ?

Tout d'abord, vous devez vous assurer que votre lac de données est conforme à la norme [ACID](https://mariadb.com/resources/blog/acid-compliance-what-it-means-and-why-you-should-care/). Cela signifie que vos modifications de données peuvent se produire de manière isolée (dans des branches). Ainsi, l'intégrité des données est maintenue dans la branche master (jusqu'à ce que ces modifications soient prêtes à être fusionnées).

Une autre caractéristique importante de LakeFS est l'intégration continue des données (encore une fois, tout comme dans le développement de logiciels). Les entreprises doivent incorporer de nouvelles données rapidement et sans interruption. Par conséquent, cette capacité à avoir un flux de travail [CI/CD](https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html) est inestimable.

Voyons donc comment nous pouvons commencer à utiliser LakeFS pour notre expérimentation et notre parallélisation de stockage objet.

### Comment installer LakeFS

Localement, vous pouvez installer LakeFS en exécutant la commande suivante dans votre terminal :*

![Image](https://lh4.googleusercontent.com/pTYRbQlB2_Mp8j_XGxUOvBI0PLf5kuuT1tYV5AxcPmrnq8K5sjLCUBwQqp4klk4rnraQnK9OD5hrudEFUwBLNcvmyNGQqDPkLQ_DkVBoVgCUfITIFdS6d1RxtkTFG_T40ZV0ia0L=s0)
_[Source du code](https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&amp;t=seti&amp;wt=none&amp;l=application%2Fx-sh&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=curl%2520https%253A%252F%252Fcompose.lakefs.io%2520%257C%2520docker-compose%2520-f%2520-%2520up%250A)_

_*Ceci suppose que Docker et Docker-Compose sont installés sur votre système. Si vous n'avez pas Docker et Docker-Compose, vous pouvez essayer d'autres méthodes d'installation [ici](https://docs.lakefs.io/quickstart/more_quickstart_options.html)._

Visitez maintenant [http://127.0.0.1:8000/setup](http://127.0.0.1:8000/setup) dans votre navigateur pour vérifier que vous l'avez installé correctement.

### Comment créer un dépôt dans LakeFS

Une fois que vous avez vérifié que LakeFS est correctement installé, créez un utilisateur administrateur.

![Image](https://lh5.googleusercontent.com/kRpsNjJe60f7fiIEFC0O5ZbY88F9g-F4X-GRtl8L8WiVJ_sDiKcnz-0jmprZc-bVkfq029fYhq4K-jdBXyBQttc012Nv4v6j2vbJvk4jnbs71BF9Wulo_5JwsvmSjRE1nkQ-ltRe=s0)
_[Source de l'image](https://docs.lakefs.io/assets/img/setup.png)_

![Image](https://lh3.googleusercontent.com/oez-1Q1JH6Q_cqUh0tKE1bW-IbEXg92UP4NVkTy_o-vVETELASw8R8CoPS5ogWDZNl4hH8W3cb68_PvEECO1os9U1sgfJFA2PMnc1J57wEjomp9SrN0ZZK-OXoOjJpZcF-LPZlhu=s0)
_[Source de l'image](https://docs.lakefs.io/assets/img/setup_done.png)_

Cliquez sur le lien de connexion et connectez-vous en tant qu'administrateur.

Sur la page vers laquelle vous êtes redirigé, cliquez sur Create Repository (Créer un dépôt). Une fenêtre contextuelle apparaîtra :

![Image](https://lh6.googleusercontent.com/2abxJeRjLk7IRzhohW7jlG3cKQKH4kRCjIyVbQkHe_Fa9qdcGPdrbcTsFRhW7lv3S5LQtfa4xBmnNu0wRqhFSvwi1hp5_ARB_fRJlcLgz1TmDa_a9DQ-apmcIiclMLwsgfuyoD9P=s0)
_[Source de l'image](https://docs.lakefs.io/assets/img/create_repo_local.png)_

Félicitations ! Vous avez maintenant votre premier dépôt. C'est le « bucket » principal dans lequel vous allez stocker vos données.

Ensuite, nous allons commencer à ajouter des données.

### Comment ajouter des données à votre dépôt LakeFS

Visitez [ici](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) pour installer l'AWS CLI.

Avec les identifiants créés lors de la phase de création de l'utilisateur administrateur, configurez un nouveau profil de connexion :

![Image](https://lh5.googleusercontent.com/D9FDuc11VgqsUr5LfN2UE_zTQYSKinNHB_saQxvr0MJj2yurnDCTqEC0cWA-dvOj3TYGMxJq52Una4zpaG6hrImrAaOWA43V1nMsUg0NpI9XIj8lKF6THD3ZoC0BNMqd-uRUsS6p=s0)
_[Source du code](https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&amp;t=seti&amp;wt=none&amp;l=application%2Fx-sh&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=aws%2520configure%2520--profile%2520local%250A%2523%2520output%253A%250A%2523%2520AWS%2520Access%2520Key%2520ID%2520%255BNone%255D%253A%2520AKIAJVHTOKZWGCD2QQYQ%250A%2523%2520AWS%2520Secret%2520Access%2520Key%2520%255BNone%255D%253A%2520****************************************%250A%2523%2520Default%2520region%2520name%2520%255BNone%255D%253A%250A%2523%2520Default%2520output%2520format%2520%255BNone%255D%253A%250A)_

Pour tester si la connexion fonctionne, exécutez ce qui suit :

![Image](https://lh5.googleusercontent.com/oP-iisEz7w9qQM-zQaAUcdhXj_YMRGamhV-AwwNfFsDVm_p4HcKlGsw0sVD0aJS-Q-3rCy3VlhtcvtBxJgFCrHQLXrPB7ZyHVril1iGeWKP_mqPPrxizpw8NNAGWdNc2ZF36mfX4=s0)
_[Source du code](https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&amp;t=seti&amp;wt=none&amp;l=application%2Fx-sh&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=aws%2520--endpoint-url%253Dhttp%253A%252F%252Flocalhost%253A8000%2520--profile%2520local%2520s3%2520ls%250A%2523%2520output%253A%250A%2523%25202021-06-15%252013%253A43%253A03%2520example-repo%250A)_

Maintenant, pour copier des fichiers dans la branche main :

![Image](https://lh5.googleusercontent.com/Z_3sbfX6IMJzPkYeejJ1O9ftjkO3c4kPk_rlCJ1iOP2FgTnJTZ03cB8C8Ml2u4bet4cvBS60rHt7Ns-xgLWix422-w3ZvpGQCyeGKgBDd0Oog-sV-E4XSpV4ARpoYeQhR2INZV_H=s0)
_[Source du code](https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&amp;t=seti&amp;wt=none&amp;l=application%2Fx-sh&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=aws%2520--endpoint-url%253Dhttp%253A%252F%252Flocalhost%253A8000%2520--profile%2520local%2520s3%2520cp%2520.%252Ffoo.txt%2520s3%253A%252F%252Fexample-repo%252Fmain%252F%250A%2523%2520output%253A%250A%2523%2520upload%253A%2520.%252Ffoo.txt%2520to%2520s3%253A%252F%252Fexample-repo%252Fmain%252Ffoo.txt%250A)_

Notez simplement que nous devons préfixer le chemin avec le nom de la branche que nous voulons utiliser.

Maintenant, nous verrons le fichier que nous avons ajouté dans l'interface utilisateur :

![Image](https://lh6.googleusercontent.com/F8UCd8s43wM0y4WgRhHWy04p2rzBQ1ccvUZhppCzl30fE0FJEpMQb7Y1X06x-WDx3J9I5LELQv4FtFKOYWJqU2E9dENB5MMqjsv-MYfLI-oCEXLekhWH9xTcazm1-_Fmo4NxgDb_=s0)
_[Source de l'image](https://docs.lakefs.io/assets/img/object_added.png)_

Ensuite, nous devrons savoir comment effectuer un Commit et créer des branches. Pour ce faire, nous devrons installer le CLI LakeFS.

### Comment installer le CLI LakeFS

Vous devez d'abord télécharger le fichier binaire [ici](https://docs.lakefs.io/#downloads).

Encore une fois, nous devons utiliser les identifiants administrateur créés précédemment :

![Image](https://lh4.googleusercontent.com/KQntIwi6YaOyp2kKvKLxeYs4Il4czCGCv8fj2_PFhg2Bqy2RRGNNQtLsCxS8YT57DEH-Q63obz7emujS5tST4aoPx0qb4XLjJV3AeKEwRwQGATfJd6us3BA5Svo7Lz_i3k_Smy7N=s0)
_[Source du code](https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&amp;t=seti&amp;wt=none&amp;l=application%2Fx-sh&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=lakectl%2520config%250A%2523%2520output%253A%250A%2523%2520Config%2520file%2520%252Fhome%252Fjanedoe%252F.lakectl.yaml%2520will%2520be%2520used%250A%2523%2520Access%2520key%2520ID%253A%2520AKIAJVHTOKZWGCD2QQYQ%250A%2523%2520Secret%2520access%2520key%253A%2520****************************************%250A%2523%2520Server%2520endpoint%2520URL%253A%2520http%253A%252F%252Flocalhost%253A8000%252Fapi%252Fv1%250A)_

Voici quelques-unes des commandes que nous pouvons exécuter pour essayer :

![Image](https://lh4.googleusercontent.com/4HuuBJwfpif6TzMS5spkzhkLQf_TC-rZ6WMjAiOOrsv3z8iF2vaTtKTjzicnm5qDjXmLq_aSGqXvAF7RE43BWd9hGB7gUSb76w1bt6ntyLJgAVFBMLwP7uYRPLFUd-1G27kVER7O=s0)
_[Source du code](https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&amp;t=seti&amp;wt=none&amp;l=application%2Fx-sh&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=lakectl%2520branch%2520list%2520lakefs%253A%252F%252Fexample-repo%250A%2523%2520output%253A%250A%2523%2520%252B----------%252B------------------------------------------------------------------%252B%250A%2523%2520%257C%2520REF%2520NAME%2520%257C%2520COMMIT%2520ID%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%257C%250A%2523%2520%252B----------%252B------------------------------------------------------------------%252B%250A%2523%2520%257C%2520main%2520%2520%2520%2520%2520%257C%2520a91f56a7e11be1348fc405053e5234e4af7d6da01ed02f3d9a8ba7b1f71499c8%2520%257C%250A%2523%2520%252B----------%252B------------------------------------------------------------------%252B%250A%2520%2520%2520%2520%2520%250Alakectl%2520commit%2520lakefs%253A%252F%252Fexample-repo%252Fmain%2520-m%2520%27added%2520our%2520first%2520file%21%27%250A%2523%2520output%253A%250A%2523%2520Commit%2520for%2520branch%2520%2522main%2522%2520done.%250A%2523%2520%250A%2523%2520ID%253A%2520901f7b21e1508e761642b142aea0ccf28451675199655381f65101ea230ebb87%250A%2523%2520Timestamp%253A%25202021-06-15%252013%253A48%253A37%2520%252B0300%2520IDT%250A%2523%2520Parents%253A%2520a91f56a7e11be1348fc405053e5234e4af7d6da01ed02f3d9a8ba7b1f71499c8%250A%2520%2520%250Alakectl%2520log%2520lakefs%253A%252F%252Fexample-repo%252Fmain%250A%2523%2520output%253A%2520%2520%250A%2523%2520commit%2520901f7b21e1508e761642b142aea0ccf28451675199655381f65101ea230ebb87%250A%2523%2520Author%253A%2520Example%2520User%2520%253Cuser%2540example.com%253E%250A%2523%2520Date%253A%25202021-06-15%252013%253A48%253A37%2520%252B0300%2520IDT%250A%2520%2520%2520%2520%2520%2520%2520%250A%2520%2520%2520%2520%2520%2520added%2520our%2520first%2520file%21%250A%2520%2520%2520%2520%2520%2520%2520)_

Vous pouvez trouver toutes les autres commandes, telles que la création de branches, etc., [en ligne](https://docs.lakefs.io/reference/commands.html).

Et voilà ! Vous pouvez maintenant travailler avec vos données comme bon vous semble. Expérimentez sans culpabilité et créez plusieurs versions de vos modèles de données.

## En conclusion

Dans cet article, nous avons couvert pas mal de terrain. Nous avons appris les différents types de mécanismes de stockage de données et pourquoi le stockage objet présente de nombreux avantages pour l'expérimentation et le parallélisme des données.

Ensuite, nous avons exploré les lacs de données et LakeFS, qui est un outil puissant pour travailler avec les données.

Au premier abord, cela peut sembler une tâche ardue. Mais, comme nous l'avons montré ici, avec le bon ensemble d'outils et de connaissances, vous pouvez accomplir énormément de choses.