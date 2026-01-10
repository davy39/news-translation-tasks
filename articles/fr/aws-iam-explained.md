---
title: AWS Identity and Access Management (IAM) – Expliqué avec une analogie
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2022-11-16T18:51:48.000Z'
originalURL: https://freecodecamp.org/news/aws-iam-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Slide1.JPG
tags:
- name: authentication
  slug: authentication
- name: authorization
  slug: authorization
- name: AWS
  slug: aws
- name: IAM
  slug: iam
seo_title: AWS Identity and Access Management (IAM) – Expliqué avec une analogie
seo_desc: 'AWS IAM (Identity and Access Management) gives you control over who can
  access your AWS services and resources based on some predefined permissions.

  The two keywords here are “who” and “permissions”. “Who” refers to a specific identity,
  which can be ...'
---

AWS IAM (Identity and Access Management) vous donne le contrôle sur **qui** peut accéder à vos services et ressources AWS en fonction de certaines **permissions** prédéfinies.

Les deux mots clés ici sont « qui » et « permissions ». « Qui » fait référence à une identité spécifique, qui peut être un **utilisateur**, un **groupe** ou un **rôle**. « Permissions » fait référence aux **stratégies** qui sont attachées à une identité. Ces permissions permettent ou refusent l'accès à une ressource.

IAM est la méthode AWS pour authentifier et autoriser les identités. L'authentification n'est cependant pas la même chose que l'autorisation. L'authentification concerne le « **qui** » tandis que l'autorisation concerne les « **permissions** ».

## La différence entre l'authentification et l'autorisation

L'authentification est lorsque qu'une identité prouve qu'elle est ce/qui elle dit être. L'autorisation, en revanche, consiste à prouver que vous avez les permissions pour accéder à une ressource.

Pour bien comprendre la différence, considérez l'analogie suivante. Vous devez être à la fois authentifié et autorisé pour pouvoir monter à bord d'un vol. L'authentification est faite avec votre passeport ou votre pièce d'identité, où il est vérifié que la photo de votre passeport correspond à votre visage. Cela prouve que vous êtes bien qui vous dites être.

Après avoir été authentifié, vous devez prouver que vous avez la permission de prendre un vol spécifique. Cela se fait avec votre carte d'embarquement.

L'authentification et l'autorisation doivent être effectuées avant de pouvoir monter à bord d'un vol. De même, les deux doivent être effectuées avant de pouvoir accéder aux ressources AWS.

Vous pouvez [en savoir plus sur l'autorisation vs l'authentification ici](https://www.freecodecamp.org/news/whats-the-difference-between-authentication-and-authorisation/).

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-70.png align="left")

*L'authentification et l'autorisation ne sont pas la même chose*

Les utilisateurs, groupes et rôles IAM concernent l'authentification – c'est-à-dire prouver que vous êtes qui vous dites être. Ils sont comme des passeports qui vous permettent de passer la sécurité dans un aéroport.

Sans une carte d'embarquement cependant, vous ne pouvez pas monter à bord d'un avion. La stratégie IAM est comme une carte d'embarquement, en ce sens qu'elle accorde ou refuse l'accès à des ressources spécifiques.

## Qu'est-ce que les utilisateurs IAM ?

Il s'agit de toute identité (humains ou une application) qui nécessite un accès à long terme aux ressources AWS. Ces entités font des demandes à IAM pour être authentifiées avant toute interaction avec les ressources AWS.

L'authentification est effectuée à l'aide d'une combinaison nom d'utilisateur/mot de passe pour les humains accédant à AWS via la console, ou via des clés d'accès pour une application ou un humain accédant à AWS via l'interface de ligne de commande.

## Qu'est-ce que les groupes IAM ?

Les utilisateurs IAM peuvent être placés dans un groupe IAM. Les groupes IAM facilitent l'organisation d'un grand nombre d'utilisateurs IAM et l'application de permissions au niveau du groupe plutôt qu'au niveau individuel. Cela est dû au fait que ce dernier ne s'adapte pas à un grand nombre d'utilisateurs.

Imaginez que vous avez une équipe composée de développeurs, d'architectes, de personnel administratif, d'ingénieurs DevOps, de support en direct et de testeurs. Chacune de ces équipes compte 10 personnes, soit un total de 60 personnes.

Au lieu de définir des stratégies de permission pour 60 personnes individuellement, vous pouvez placer les utilisateurs IAM dans leurs groupes respectifs et appliquer des permissions au niveau du groupe. Cela facilite l'organisation des permissions et permet également de mieux évoluer à mesure que votre équipe grandit.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-72.png align="left")

*Les groupes IAM peuvent être créés pour des équipes séparées*

Il n'y a pas d'identifiants de connexion pour les groupes IAM. De plus, un utilisateur peut appartenir à plusieurs groupes, donc par exemple, un utilisateur IAM qui est dans le groupe DevOps peut également être dans le groupe de support en direct. Cela correspond bien au monde réel où un ingénieur DevOps peut également être dans le support en direct.

## Qu'est-ce que les rôles IAM ?

Les rôles IAM sont utilisés pour accorder un **accès temporaire** à plusieurs identités. Ces identités pourraient être des humains externes à AWS accédant à vos services, des utilisateurs IAM, ou des applications.

Ces identités assument le rôle temporairement, et toute stratégie de permission attachée au rôle est appliquée par procuration à l'identité assumant ce rôle.

Les rôles IAM sont importants car AWS a des limites strictes sur le nombre d'utilisateurs IAM ([actuellement 5000](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html)).

### Stratégies de confiance vs stratégies de permission

Les stratégies IAM qui sont attachées aux rôles se présentent sous deux formes – stratégie de confiance et stratégie de permission.

La stratégie de confiance contrôle quelle identité (par exemple, les utilisateurs IAM, les ressources AWS comme les instances EC2, les entités anonymes) peut assumer ce rôle. Une fois qu'un rôle est assumé par une identité, AWS lui délivre des [Identifiants de Sécurité Temporaires](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html).

Vous pouvez penser à la stratégie de confiance comme la manière dont AWS authentifie un rôle IAM pour s'assurer que seule l'identité autorisée à assumer le rôle peut le faire – c'est-à-dire qu'une identité a prouvé qu'elle est ce/qui elle dit être.

Mais il y a un piège. Avec les stratégies de confiance, cette authentification ne fonctionne que pendant une période de temps. Une fois que ce temps s'est écoulé, l'identité doit se réauthentifier et obtenir de nouveaux Identifiants de Sécurité Temporaires.

La stratégie de permission est relativement simple : elle définit les permissions que le rôle possède, ce qui, par procuration, définit les permissions que l'identité assumant ce rôle aura.

Les rôles IAM sont un concept relativement difficile à saisir, donc si vous ne le comprenez pas tout à fait encore, veuillez continuer à lire et cela deviendra plus clair.

## Comment fonctionnent les stratégies IAM

Les stratégies IAM sont attachées à des identités, donc des utilisateurs, des groupes ou des rôles. Les stratégies IAM peuvent également être attachées à certaines ressources AWS. Ces types de stratégies sont appelées [stratégies basées sur les ressources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html).

Les stratégies IAM sont des documents JSON, constitués d'une ou plusieurs déclarations qui accordent ou refusent l'accès aux ressources AWS.

La stratégie IAM ci-dessous montre comment les permissions sont accordées à une identité pour lire et écrire dans un bucket S3.

```python
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ListObjectsInBucket",
            "Effect": "Allow",
            "Action": ["s3:ListBucket"],
            "Resource": ["arn:aws:s3:::bucket-name"]
        },
        {
            "Sid": "AllObjectActions",
            "Effect": "Allow",
            "Action": "s3:*Object",
            "Resource": ["arn:aws:s3:::bucket-name/*"]
        }
    ]
}
```

* `Sid` signifie identifiant de déclaration, un champ facultatif qui permet au lecteur d'identifier rapidement ce qu'une déclaration fait.

* `Effect` peut être soit allow (autoriser) soit deny (refuser)

* `Action` fait référence à l'action que vous essayez d'effectuer. Le format est **service:opération**.

* `Resource` fait référence à la ressource avec laquelle vous interagissez. Typiquement, vous utiliserez [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) (Amazon Resource Name) qui identifie de manière unique les ressources AWS.

Par défaut, toutes les demandes sont implicitement refusées sauf si une stratégie a explicitement un « allow » comme c'est le cas dans l'exemple ci-dessus.

Ce principe de moindre privilège garantit qu'une identité ne peut pas utiliser une ressource sauf si elle est explicitement autorisée à le faire.

## Tout rassembler – Comment fonctionne IAM

Considérons un restaurant de pizzas. Il aura certains employés à temps plein – comme des chefs, des serveurs et des nettoyeurs. Il peut également avoir certains chefs à temps partiel pour aider pendant les périodes de forte demande en soirée et le week-end. Si le restaurant est bon, il aura également des clients qui peuvent manger sur place ou emporter.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-73.png align="left")

*Analogie du restaurant IAM*

Pour faire une analogie avec AWS IAM, les employés à temps plein sont comme les utilisateurs IAM. Ils nécessitent un accès à long terme aux ressources du restaurant comme montré ci-dessus. Ces utilisateurs appartiendront tous à différents groupes – le groupe des serveurs, des chefs et des nettoyeurs (c'est-à-dire que tous les serveurs, par exemple, auront le même titre de poste de « serveur »).

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-74.png align="left")

*Analogie du restaurant IAM*

Comment les employés du restaurant sont-ils authentifiés ? Comment savons-nous qu'ils sont bien qui ils disent être ? Des badges avec une photo feront l'affaire. Cela peut également montrer leur titre, ce qui est analogue au groupe IAM auquel ils appartiennent.

Les stratégies de permission qui définissent les ressources auxquelles les employés du restaurant peuvent accéder sont appliquées au niveau du groupe, puisque chaque serveur, chef et nettoyeur aura les mêmes permissions. Cela peut ne pas être vrai en réalité, car le chef principal, par exemple, peut avoir un accès privilégié. Mais pour simplifier, supposons que c'est vrai.

Comment le gérant du restaurant contrôle-t-il qui a accès à quelles ressources ? Des portes avec des serrures feront très bien l'affaire. Les clés agissent comme une stratégie car elles contrôlent l'accès à certaines parties du restaurant.

Un jeu identique sera donné à tous les serveurs, puisque les serveurs auront besoin du même niveau d'accès à la salle de stockage des aliments/boissons, à la cuisine et à la zone de restauration.

La même logique s'appliquera aux autres employés à temps plein, où le jeu de clés approprié est distribué afin qu'ils puissent utiliser les ressources du restaurant selon leurs besoins.

Donner des clés aux employés du restaurant est analogue à l'attachement d'une stratégie à un utilisateur ou à un groupe IAM. Sans les clés, les employés ne peuvent pas accéder à certaines parties du restaurant.

De même, dans AWS, sans des stratégies qui autorisent explicitement une action, les demandes ne peuvent pas être faites aux ressources AWS. L'état par défaut dans AWS et dans notre analogie de restaurant est un refus implicite lors de la tentative d'accès aux ressources.

Les employés à temps partiel, comme un chef temporaire par exemple, et les clients, n'ont pas besoin d'un accès à long terme aux ressources mais auront besoin d'un accès à court terme, analogue aux rôles IAM.

Les employés à temps partiel ne peuvent travailler que pendant une courte période – disons le soir pendant le week-end. En dehors de cette période, ils n'ont pas les permissions d'utiliser les ressources du restaurant.

Ce chef à temps partiel n'a pas besoin d'être la même personne. Cela pourrait être une personne différente chaque semaine, contrairement aux employés à temps plein qui ont des identités spécifiques.

Un chef à temps partiel **assumera** donc le rôle de chef et obtiendra un **badge temporaire** qu'il gardera pendant la durée de son service. Cela est analogue à une entité assumant un rôle IAM qui a une stratégie attachée et obtenant des Identifiants de Sécurité Temporaires qui expireront après un certain temps.

Encore une fois, la stratégie ici est l'ensemble des clés qui accordent la permission d'accéder à certaines parties du restaurant tandis que l'Identifiant de Sécurité Temporaire est le badge temporaire utilisé pour authentifier le chef.

De même, les clients sont analogues aux rôles IAM pour deux raisons. Premièrement, ils ne nécessitent qu'un accès temporaire au restaurant. Deuxièmement, et peut-être plus important encore, un restaurant prospère aura des dizaines de milliers à des centaines de milliers de clients uniques au cours de sa vie.

Avoir un grand nombre d'entités non identifiées est un cas d'utilisation parfait pour les rôles IAM. Rappelez-vous qu'avec AWS, il y a une limite stricte de 5000 pour le nombre d'utilisateurs IAM que vous pouvez avoir. Si un cas d'utilisation nécessite un nombre d'utilisateurs IAM dépassant cette limite de 5000, l'utilisation de rôles IAM est votre seule option.

Tout comme les rôles IAM sont assumés, le client doit d'abord commander quelque chose pour prouver qu'il est un client et peut assumer le rôle de client.

Après que le rôle de client est assumé, la stratégie de permission attachée au rôle de client est alors appliquée au client également. Les clients ont des permissions pour n'utiliser que certaines ressources comme la zone de restauration et les toilettes.

Pour garder l'analogie réaliste, l'accès aux toilettes est contrôlé en entrant un code qui change chaque jour, assurant ainsi que l'accès est temporaire. Ce code est analogue à la stratégie attachée au rôle de client qui accorde un accès temporaire aux toilettes.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-75.png align="left")

## Exemple de cas d'utilisation des rôles IAM

Considérons l'architecture très simple suivante : une instance EC2 exécutant une application qui nécessite un accès complet à un bucket S3.

Comment donneriez-vous à l'instance EC2 la permission de lire et d'écrire des objets depuis un bucket S3 ? Cela est expliqué dans le diagramme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-77.png align="left")

*Attacher une stratégie à un rôle IAM et laisser une instance EC2 assumer ce rôle*

1. Créez un rôle IAM pour votre instance EC2

2. Attachez une stratégie IAM au rôle qui donne un accès complet au bucket S3

3. Laissez l'instance EC2 assumer le rôle

La stratégie IAM pour un accès complet à S3 mentionnée dans l'étape #2 est :

```python
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": "*"
        }
    ]
}
```

Vous pouvez maintenant lire et écrire dans le bucket S3. Remarquez que dans la stratégie ci-dessus, elle ne spécifie aucun ARN, mais dit simplement "\*" pour la ressource. Cela signifie tous les buckets S3. Si c'est ce que vous voulez, alors cette stratégie est correcte. Mais si vous voulez spécifier un seul bucket, alors vous devez donner l'ARN du bucket.

## Conclusion

Comprendre IAM et la différence entre les utilisateurs, les rôles, les groupes et le fonctionnement des stratégies vous donne une base solide sur laquelle vous pouvez architecturer et construire des solutions sécurisées avec AWS.

Merci d'avoir lu !