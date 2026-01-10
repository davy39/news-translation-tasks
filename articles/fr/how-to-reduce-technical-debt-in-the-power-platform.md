---
title: Comment réduire la dette technique dans la Power Platform
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2025-06-06T10:37:39.795Z'
originalURL: https://freecodecamp.org/news/how-to-reduce-technical-debt-in-the-power-platform
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748957101508/ffb9fc9d-3d35-477b-841f-280d8c6a6793.png
tags:
- name: Power Platform
  slug: power-platform
- name: powerapps
  slug: powerapps
- name: engineering
  slug: engineering
seo_title: Comment réduire la dette technique dans la Power Platform
seo_desc: 'Technical debt refers to the future cost – measured in terms of time, money,
  effort, or opportunity – of choosing expedient solutions today instead of more deliberate
  and scalable ones. And it''s not just a pro-code concept.

  It might be easier to unde...'
---

**Dette technique** fait référence au coût futur  mesuré en termes de temps, d'argent, d'efforts ou d'opportunités  de choisir des solutions expéditives aujourd'hui plutôt que des solutions plus réfléchies et évolutives. Et ce n'est pas seulement un concept propre au code traditionnel.

Il peut être plus facile à comprendre si nous le comparons à la dette financière.

Howard G. Cunningham  le créateur du premier wiki  a décrit la dette technique de cette manière :

> *Livrer du code pour la première fois, c'est comme contracter une dette. Une petite dette accélère le développement tant qu'elle est remboursée rapidement avec une réécriture. Les objets rendent le coût de cette transaction tolérable.*  
>   
> *Le danger survient lorsque la dette n'est pas remboursée. Chaque minute passée sur un code pas tout à fait correct compte comme un intérêt sur cette dette. Des organisations d'ingénierie entières peuvent être paralysées sous le poids de la dette d'une implémentation non consolidée, orientée objet ou non.*

Dans cet article, vous apprendrez pourquoi la dette technique est tout aussi préoccupante dans les projets low-code que dans le développement traditionnel  et pourquoi, à certains égards, elle peut être encore plus marquée. Nous passerons en revue huit contributeurs courants à la dette technique dans les projets Power Platform qui, s'ils ne sont pas contrôlés, peuvent entraîner des maux de tête futurs.

### Table des matières

1. [Pourquoi la dette technique est aussi un problème en low-code](#heading-pourquoi-la-dette-technique-est-aussi-un-probleme-en-low-code)
    
2. [Huit exemples de dette technique dans un projet low-code](#heading-huit-exemples-de-dette-technique-dans-un-projet-low-code)
    
    * [Valeurs codées en dur ou statiques dans votre code](#heading-valeurs-codees-en-dur-ou-statiques-dans-votre-code)
        
    * [Code dupliqué](#heading-code-duplique)
        
    * [Mauvais nommage des contrôles et des variables](#heading-mauvais-nommage-des-controles-et-des-variables)
        
    * [Écrans et applications surchargés](#heading-ecrans-et-applications-surcharges)
        
    * [Aucune note de version](#heading-aucune-note-de-version)
        
    * [Logique invisible](#heading-logique-invisible)
        
    * [Modèles de données dénormalisés](#heading-modeles-de-donnees-denormalises)
        
    * [Commencer par la mise en page avant la logique](#heading-commencer-par-la-mise-en-page-avant-la-logique)
        
3. [Conclusion](#heading-conclusion)
    

## Pourquoi la dette technique est aussi un problème en low-code

La dette technique s'accumule lorsque des décisions à court terme ignorent les conséquences à long terme. Bien qu'elle existe dans tout type de développement, les plateformes low-code augmentent le risque pour une raison simple : elles éliminent une grande partie des frictions traditionnelles qui obligent les équipes à ralentir.

Avec moins de barrières à l'entrée, il est plus facile pour les développeurs citoyens  et même pour les développeurs professionnels nouveaux sur la plateforme  de commencer à construire sans tenir compte de la maintenabilité, de l'évolutivité et de la sécurité.

Les plateformes low-code permettent la rapidité  mais si vous n'êtes pas intentionnel, cette rapidité peut créer un environnement qui favorise l'accumulation de la dette technique.

## Huit exemples de dette technique dans un projet low-code

### Valeurs codées en dur ou statiques dans votre code

Nous avons tous vu du code comme ceci :

```plaintext
Office365Outlook.SendEmailV2(
  gblAuthenticatedUser.Email, 
  "Demande d'inscription reçue !", 
  "Un membre de l'équipe vous contactera bientôt avec plus d'informations."
)
```

À première vue, cela semble correct. Mais que se passe-t-il si le sujet ou le corps de l'email doit changer ?

Les valeurs codées en dur sont fragiles. Une meilleure approche consiste à stocker vos modèles d'email dans une source de données, même si elle ne contient qu'un seul enregistrement.

```plaintext
With({
  wthEmailTemplate: LookUp(EmailTemplates, TemplateType="new_signup")},
  Office365Outlook.SendEmailV2(
    gblAuthenticatedUser, 
    wthEmailTemplate.Subject, 
    wthEmailTemplate.Message
  )
)
```

Maintenant, si l'email doit être modifié, vous mettez à jour la source de données, et non la logique de l'application.

### Code dupliqué

Bien qu'il puisse être plus difficile à éviter que dans le code traditionnel, la logique dupliquée est un casse-tête pour la maintenance future.

Imaginez deux façons différentes de créer des commentaires dans une application :

```plaintext
// Boîte de dialogue principale dans un flux de commentaires
With(
    {
        wthNewlyCreatedComment: Patch(
            Comments,
            Defaults(Comments),
            {Comment: txt_hs_comment.Value}
        )
    },
    Collect(
        colComments,
        wthNewlyCreatedComment
    );
    Set(
        gblCommentCount,
        CountRows(colComments)
    )
)

// Une autre boîte de dialogue lors de la réponse à un commentaire
With(
    {
        wthNewlyCreatedComment: Patch(
            Comments,
            Defaults(Comments),
            {Comment: txt_hs_dialogComment.Value}
        )
    },
    Collect(
        colComments,
        wthNewlyCreatedComment
    );
    Set(
        gblCommentCount,
        CountRows(colComments)
    )
)
```

Ces deux blocs font la même chose. Si la logique change un jour, vous devez vous souvenir de la mettre à jour aux deux endroits.

Une approche plus propre consiste à utiliser une **fonction définie par l'utilisateur (UDF)** pour encapsuler la logique qui est réutilisée dans votre application.

```plaintext
// App.Formulas
UpdateComments(comment: Text):Void = 
{
	With(
        {
            wthNewlyCreatedComment: Patch(
                Comments,
                Defaults(Comments),
                {Comment: comment}
            )
        },
        Collect(
            colComments,
            wthNewlyCreatedComment
        );
        Set(
            gblCommentCount,
            CountRows(colComments)
        )
    )
};
```

Et ensuite dans chacun des emplacements qui nécessitent cette formule :

```plaintext
// Boîte de dialogue principale dans un flux de commentaires
UpdateComments(txt_hs_comment.Value)

// Une autre boîte de dialogue lors de la réponse à un commentaire
UpdateComments(txt_hs_dialogComment.Value)
```

À l'heure actuelle, **les fonctions définies par l'utilisateur dans les applications Canvas prennent en charge les effets secondaires** (tels que la modification des collections ou la définition de variables), mais la fonctionnalité globale est toujours **en version préliminaire**.

Si les UDF ne sont pas une option pour votre cas d'utilisation actuel, une solution de contournement courante consiste à utiliser un bouton caché qui encapsule la logique et à l'appeler avec `Select(ButtonName)`. Gardez simplement à l'esprit : le contrôle doit se trouver sur le même écran où il est invoqué.

### Mauvais nommage des contrôles et des variables

```plaintext
Écran d'accueil
  ButtonCanvas4
  TextCanvas2
  ButtonCanvas1
```

Qu'est-ce qui ne va pas dans le scénario ci-dessus ? Il est impossible de savoir à quoi chaque contrôle est responsable.

Un bon nommage n'est pas seulement un plus  c'est l'une des meilleures façons de réduire la confusion et d'améliorer la maintenabilité, surtout dans les environnements collaboratifs.

Voici une version améliorée qui permet à tout développeur de comprendre ce que font ces contrôles :

```plaintext
Écran d'accueil
  txt_hs_userName
  btn_hs_submitForm
  btn_hs_cancelSubmission
```

Dans cet exemple, nous suivons le modèle suivant :

`[type_de_contrôle]_[écran]_[responsabilité_du_contrôle]`

Cela aide à faciliter la recherche d'éléments rapidement ainsi qu'à identifier ce qu'ils font.

Un autre aspect qui se prête naturellement aux conventions de nommage est l'utilisation de variables. Les applications Canvas ont diverses méthodes pour stocker des données localement. Elles incluent :

1. Collections (ClearCollect/Collect)
    
2. Variables globales (Set)
    
3. Variables locales (UpdateContext)
    
4. Variables contextuelles (fonctions With)
    

Chaque type de variable a une portée différente qui lui est associée. Les collections sont des tables et sont disponibles dans toute votre application. Les variables globales sont également disponibles dans toute l'application. Les variables définies à l'aide de `UpdateContext` sont limitées à l'écran sur lequel elles sont déclarées. Et les variables contenues dans une fonction `With` ne sont disponibles que dans cette fonction.

Il est bon de s'assurer que le nom de la variable reflète avec précision le type de variable qu'elle représente. Par exemple :

```plaintext
// préfixé avec "wth" pour une variable dont la portée est limitée à une fonction with
With({wthNewlyCreatedUser: Patch(AppUsers,...)},...)

// préfixé avec "ctx" pour une variable contextuelle dont la portée est limitée à l'écran
UpdateContext({ctxCurrentPostVotes: LookUp(colPostVotes, ....)})

// préfixé avec "gbl" pour une variable globale
Set(gblAuthenticatedUser, LookUp(AppUsers,....))

// préfixé avec "col" pour une collection
ClearCollect(colUserRoles, LookUp(AppRoles, ...))
```

Chaque type de stockage de données est désigné par un préfixe qui indique son type, ce qui facilite le débogage d'une application.

### Écrans et applications surchargés

Il peut être tentant de tout garder sur un seul écran pour les applications simples. Mais les applications canvas peuvent rapidement devenir non performantes si trop de contrôles ou trop de logique se trouvent sur un seul écran. La limite recommandée est de ne pas dépasser 500 contrôles par application et 300 contrôles par écran. L'utilisation et l'édition de l'application peuvent ralentir considérablement si ces limites sont dépassées.

Une façon de prévenir ce problème est de penser de manière plus modulaire. Par exemple, vous pouvez avoir à la fois des tâches administratives et non administratives au sein d'une seule application. Au lieu de cela, vous pouvez créer deux applications, une pour les utilisateurs administrateurs et l'autre pour les utilisateurs généraux.

Une autre façon d'éviter ces problèmes dans la même application est de construire en utilisant des composants. Les contrôles qui composent un composant ne comptent pas individuellement vers les limites de l'écran et sont également un moyen naturel de réduire la duplication au sein et entre vos applications. Les composants peuvent être créés au sein d'une application ou sous forme de bibliothèque de composants (si votre composant doit être utilisé dans plusieurs applications  par exemple, des chargeurs/spinners et des boîtes de dialogue de confirmation).

Pour plus d'informations sur les composants, consultez [cet article que j'ai écrit sur la création de composants réutilisables.](https://www.scriptedbytes.com/posts/power-apps-reusable-components)

### Aucune note de version

À mesure que l'écosystème Power Platform grandit, des techniques de versionnage avancées sont introduites, y compris l'intégration de solutions avec Git. Mais même si vous n'avez pas cette intégration git, il y a quelque chose de simple que vous pouvez faire.

Lorsque vous enregistrez une application après toute modification non triviale, utilisez les notes de version intégrées.

![Image de la façon d'enregistrer avec des notes de version dans une application canvas](https://scripted-bytes.ghost.io/content/images/2025/05/Snag_29bdb959.png align="left")

Cette simple habitude rendra deux choses beaucoup plus faciles :

1. Si vous devez un jour revenir en arrière sur des modifications, il devient beaucoup plus facile d'identifier la version correcte à laquelle revenir.
    
2. Lorsque vous utilisez plusieurs environnements (par exemple, Dev, Test et Prod), cela peut vous aider à identifier quelle version se trouve actuellement dans chaque environnement, car les numéros de version intégrés peuvent ne pas nécessairement correspondre.
    

Pour afficher les notes de version d'une application canvas, sélectionnez 'Afficher les détails' pour l'application, puis sélectionnez l'onglet des versions.

![Image des versions d'application canvas et des notes de version](https://scripted-bytes.ghost.io/content/images/2025/05/Snag_29bde376.png align="left")

### Logique invisible

La logique invisible est une logique qui supporte un produit, mais qui n'est pas immédiatement reconnaissable. Par exemple, les API personnalisées et les flux cloud peuvent rapidement être oubliés s'il n'y a pas de documentation rappelant aux développeurs que ces composants critiques existent  et ce qu'ils font réellement.

L'une des meilleures façons de documenter un projet est d'utiliser des solutions. Les solutions incluront généralement la majorité des actifs d'un projet  souvent plus de 90 %  mais il existe des exceptions notables, telles que les listes SharePoint, les rapports Power BI et certaines intégrations externes.

Certaines choses qu'une solution n'inclura souvent pas ou ne pourra pas inclure sont les actifs appartenant à des solutions de base ou de cœur  par exemple, des flux cloud génériques qui servent plusieurs projets ou produits. Selon votre stratégie de solution, vous ne voudrez peut-être pas ajouter ceux-ci à chaque solution, et ils n'existeront que dans une solution de base ou de cœur.

D'autres choses qui relèvent de la logique invisible incluent les actifs Power BI et les Dataflows, ainsi que leurs architectures d'automatisation respectives (par exemple, comment et quand un Dataflow est déclenché).

En tant que meilleure pratique, utilisez la nature auto-documentée des solutions pour fournir des références à tous les actifs, la logique et les dépendances qu'un projet utilise. Envisagez également d'adopter une pratique de documentation basée sur les fonctionnalités, où chaque fonctionnalité ou histoire utilisateur implémentée inclut une documentation de base, y compris des détails de mise en œuvre de haut niveau et toute logique sous-jacente. Cela pourrait être un document de type wiki qui permet aux développeurs, qui peuvent être en train de résoudre des problèmes ou d'étendre une fonctionnalité, de s'orienter simplement avant de plonger dans un projet inconnu.

### Modèles de données dénormalisés

La normalisation des données est un sujet à part entière, mais vous n'avez pas besoin d'être un expert pour commencer à construire des modèles de données robustes et *évolutifs*. En termes simples, la normalisation des données implique de regrouper des éléments de données similaires et d'éliminer la duplication.

Jetez un coup d'œil à l'exemple suivant de la table des employés.

```plaintext
Table des employés (Dénormalisée)

| ID de l'employé | Nom   | Nom du département | Emplacement du département |
|-----------------|--------|--------------------|----------------------------|
| 1               | Alice  | RH                  | Bâtiment A                 |
| 2               | Bob    | IT                  | Bâtiment B                 |
| 3               | Carol  | RH                  | Bâtiment A                 |
| 4               | Dan    | IT                  | Bâtiment B                 |
| 5               | Eve    | Finance             | Bâtiment C                 |
```

Dans la table ci-dessus, nous pouvons voir que les enregistrements de la table EMPLOYÉ contiennent des informations sur le département. Conceptuellement, cela est correct, mais le principal problème est que les attributs de chaque enregistrement décrivent non seulement l'employé, mais fournissent également des détails sur le département.

Ce type de données est appelé données dénormalisées. Les données dénormalisées rendent le modèle de données plus difficile à faire évoluer et à maintenir. Par exemple, si le `Nom du département` change, nous devons localiser chaque enregistrement avec ce nom de département et le mettre à jour en conséquence.

Au lieu de cela, examinons un modèle de données plus normalisé qui consiste maintenant en deux tables.

```plaintext
Table des employés (Normalisée)

| ID de l'employé | Nom   | ID du département |
|-----------------|--------|-------------------|
| 1               | Alice  | 1                 |
| 2               | Bob    | 2                 |
| 3               | Carol  | 1                 |
| 4               | Dan    | 2                 |
| 5               | Eve    | 3                 |


Table des départements

| ID du département | Nom du département | Emplacement du département |
|-------------------|--------------------|----------------------------|
| 1                 | RH                  | Bâtiment A                 |
| 2                 | IT                  | Bâtiment B                 |
| 3                 | Finance             | Bâtiment C                 |
```

Ce modèle de données élimine la duplication et simplifie les mises à jour des attributs du département, ne nécessitant qu'une seule mise à jour d'enregistrement. Et parce que chaque attribut des tables EMPLOYÉS et DÉPARTEMENTS décrit uniquement la clé primaire de la table respective, il s'agit d'un modèle de données normalisé.

Une idée fausse courante parmi les nouveaux développeurs est que plus de tables sont une mauvaise chose. Beaucoup pensent que moins de sources de données sont plus faciles à maintenir, mais ce n'est pas toujours vrai.

En développement, ce qui rend les choses plus faciles à maintenir n'est pas moins de quelque chose, mais plutôt à quel point c'est atomique, modulaire et sans dépendance. Par exemple, quelques petites fonctions pures qui ne font qu'une seule chose seront plus faciles à maintenir qu'une seule fonction produisant des effets secondaires qui fait beaucoup de choses.

Ne vous éloignez pas des données normalisées simplement parce qu'elles créent plus de tables. Éloignez-vous des modèles de données qui ne peuvent pas évoluer.

**Une dernière note :** Les données dénormalisées ont aussi leur place et ce n'est pas une mauvaise chose. Par exemple, les données de reporting sont souvent dénormalisées et sont beaucoup plus préférées car elles rendent la logique de reporting beaucoup plus facile.

### Commencer par la mise en page avant la logique

Le low-code rend facile de se lancer et de commencer à construire, ce qui est un avantage significatif. Mais ce modèle peut aussi rendre très facile de sauter des aspects importants du développement, tels que la collecte des exigences, la conception de l'interface utilisateur et la modélisation des données.

Il est parfaitement acceptable de prototyper des idées. C'est idéal pour déterminer rapidement si quelque chose peut être réalisable ou non. Mais vous devez avoir la discipline de vous arrêter avant d'aller trop loin et de prendre le temps de planifier correctement.

Par exemple, envisagez d'adopter une approche basée sur la logique métier en premier. Cela signifie que les exigences et la logique métier principale sont décidées (et souvent implémentées) avant même de commencer à construire l'interface utilisateur.

Le principe de base de ce type de développement est que, quel que soit l'interface qu'un utilisateur choisit pour interagir avec nos données  et rappelez-vous, une application web n'est rien de plus qu'une interface pour vos données  la logique métier principale doit fonctionner correctement. Dans cette optique, une application Canvas devient simplement une enveloppe esthétique qui complète ce qui est, espérons-le, une logique métier bien conçue.

## Conclusion

La dette technique existe à la fois dans le développement traditionnel et low-code. La reconnaître tôt, avant qu'elle ne commence à s'accumuler, est crucial. Voici quelques conseils qui peuvent réduire et maintenir la dette technique à des niveaux gérables :

1. Évitez les données codées en dur ou statiques dans votre logique d'application
    
2. Éliminez la logique dupliquée avec des fonctions définies par l'utilisateur (UDF)
    
3. Utilisez des conventions de nommage cohérentes pour les contrôles et les variables
    
4. Divisez les applications surchargées en plusieurs écrans ou plusieurs applications
    
5. Ajoutez des notes de version pour suivre les modifications significatives
    
6. Documentez la logique invisible telle que les flux et les API
    
7. Normalisez vos données pour réduire la duplication
    
8. Commencez par la logique métier  et non par la mise en page ou les visuels
    

> **Vous avez trouvé cela utile ?** Je travaille à l'intersection du développement low-code et pro-code, en me concentrant sur la création d'applications performantes et en vous aidant à récupérer votre temps grâce à une automatisation réfléchie. Explorez plus sur [scriptedbytes.com.](https://scriptedbytes.com)