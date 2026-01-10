---
title: Comment prévenir la perte d'un compte lors de l'utilisation de l'authentification
  à deux facteurs
subtitle: ''
author: Obum
co_authors: []
series: null
date: '2023-03-22T16:28:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-prevent-account-loss-when-using-two-factor-authentication
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-karolina-grabowska-4467737.jpg
tags:
- name: Security
  slug: security
- name: Two-factor authentication
  slug: two-factor-authentication
seo_title: Comment prévenir la perte d'un compte lors de l'utilisation de l'authentification
  à deux facteurs
seo_desc: "If someone gains unauthorized access to your passwords, two-factor authentication\
  \ (2FA) can prevent them from accessing your account. \nBut if you ever lose access\
  \ to all your 2FA methods, you have lost your account. How do you prevent such loss?\n\
  In t..."
---

Si quelqu'un obtient un accès non autorisé à vos mots de passe, l'authentification à deux facteurs (A2F) peut l'empêcher d'accéder à votre compte. 

Mais si jamais vous perdez l'accès à toutes vos méthodes A2F, vous avez perdu votre compte. Comment prévenir une telle perte ?

Dans cet article, nous examinerons l'authentification à deux facteurs (A2F), ses méthodes et comment prévenir la perte d'un compte liée à son utilisation.

## Table des matières

* [Qu'est-ce que l'authentification à deux facteurs (A2F) ?](#heading-quest-ce-que-lauthentification-a-deux-facteurs-a2f)
* [Méthodes d'authentification à deux facteurs](#heading-methodes-dauthentification-a-deux-facteurs)
* [Le problème avec l'authentification à deux facteurs](#heading-le-probleme-avec-lauthentification-a-deux-facteurs)
* [Comment se protéger contre la perte d'accès à vos comptes](#heading-comment-se-proteger-contre-la-perte-dacces-a-vos-comptes)  
1. [Sauvegarder et noter le(s) code(s) de récupération](#heading-1-sauvegarder-et-noter-les-codes-de-recuperation)  
2. [Sauvegarder et noter la clé secrète (seed) de l'application d'authentification](#heading-2-sauvegarder-et-noter-la-cle-secrete-seed-de-lapplication-dauthentification)  
3. [Configurer plus d'une méthode A2F](#heading-3-configurer-plus-dune-methode-a2f)  
4. [Toujours mettre à jour les méthodes A2F](#heading-4-toujours-mettre-a-jour-les-methodes-a2f)  
5. [Configurer un e-mail et un téléphone de récupération](#heading-5-configurer-un-e-mail-et-un-telephone-de-recuperation) 
* [Résumé](#heading-resume)

## Qu'est-ce que l'authentification à deux facteurs (A2F) ?

L'authentification à deux facteurs est un paramètre de sécurité supplémentaire pour votre compte que de nombreuses plateformes ont activé. 

Il s'agit d'un paramètre de sécurité supplémentaire car vous disposez déjà d'un "premier" moyen de vous authentifier. Ce "premier" moyen peut être la connexion par mot de passe ou la connexion par identité fédérée. L'identité fédérée signifie se connecter avec un autre fournisseur, comme Apple, Facebook, Google, etc.

L'authentification à deux facteurs aide à réduire l'accès non autorisé à vos données ou à votre compte. C'est une deuxième étape de connexion pour vérifier que vous êtes bien le propriétaire du compte. Ainsi, en plus de votre première méthode de connexion, vous devrez effectuer cette seconde étape (d'où le terme "deux facteurs") pour accéder à votre compte.

L'authentification à deux facteurs ne concerne pas l'utilisation et la sécurisation de vos mots de passe. Cela relève de la sécurité de base du compte. Nous parlons ici d'une étape de sécurité avancée où, après avoir saisi votre mot de passe, vous devez encore saisir un code ou effectuer une action avant d'accéder à votre compte. 

Dans cet article, le terme "plateforme" désigne tout endroit où vous pouvez vous connecter et vous déconnecter. freeCodeCamp, LinkedIn et Twitter sont des exemples de plateformes. Dans cet article, une plateforme est un endroit où vous possédez un compte.

Certaines plateformes ne proposent pas l'A2F. Il se peut que vous n'ayez que peu de données chez elles. L'A2F y serait donc superflue. En revanche, les plateformes majeures et grand public proposent l'A2F. Ce sont des plateformes où le compte d'un utilisateur présente un intérêt pour le piratage. 

Sur la plupart des plateformes, l'A2F est facultative. Sur quelques-unes, cependant, vous êtes tenu de configurer l'A2F dès le premier accès au compte et vous ne pouvez pas la désactiver. En d'autres termes, l'A2F est obligatoire sur certaines plateformes.

Vous devriez configurer l'A2F partout où elle est disponible. Pour ce faire, rendez-vous dans les paramètres de sécurité de votre compte sur une plateforme compatible. Configurez l'A2F en utilisant au moins l'une des méthodes spécifiées et le tour est joué. Lors des connexions suivantes, vous devrez compléter l'A2F pour accéder au compte.

## Méthodes d'authentification à deux facteurs

Les méthodes d'A2F désignent les différentes manières de configurer l'A2F. Elles sont les suivantes :

1. Clé de sécurité A2F
2. Numéro de téléphone A2F
3. Application d'authentification A2F
4. Invite de connexion (Sign-In prompt)
5. Code(s) de récupération

Les clés de sécurité sont des clés USB ou Bluetooth que vous pouvez connecter à votre appareil. Ce sont des dispositifs A2F physiques et ils semblent être les plus sécurisés. C'est parce qu'il est hautement improbable qu'un pirate vienne voler la clé chez vous. 

Pour configurer l'A2F à l'aide de clés, branchez la clé ou connectez-vous via Bluetooth et suivez les étapes. Vous pourrez ensuite utiliser la clé lors des connexions suivantes. Vous devez acheter ces clés dans le commerce ou en ligne pour les utiliser. 

L'A2F par numéro de téléphone consiste à recevoir un code de mot de passe à usage unique (OTP) soit par appel, soit par SMS. Fournissez un numéro de téléphone et la plateforme y envoie un OTP. Parfois, vous pourriez recevoir un appel automatisé avec le code. Dans les deux cas, saisissez le code sur la plateforme et vous aurez configuré avec succès l'A2F par téléphone. 

Lors des connexions ultérieures pour accéder à votre compte, après avoir saisi votre mot de passe, vous recevrez un code OTP sur ce téléphone. Saisissez le code pour accéder à votre compte.

Les applications d'authentification génèrent un code à 6 chiffres chaque minute. [Il existe de nombreuses applications d'authentification](https://www.google.com/search?q=authenticator+apps), comme Google Authenticator, Microsoft Authenticator et d'autres. 

Pour configurer une application d'authentification, vous scannez un code QR ou vous saisissez une clé secrète (seed). La plateforme où réside votre compte vous fournira l'un des deux. Scannez ou saisissez la phrase et vous obtiendrez un code unique à 6 chiffres chaque minute. 

Lors des prochaines connexions, après avoir saisi votre mot de passe, collez le dernier code à 6 chiffres de l'application d'authentification et vous serez connecté.

Les invites de connexion (Sign-in prompts) ne sont pas aussi courantes que les autres méthodes A2F. Toutes les plateformes ne disposent pas de cette fonctionnalité. Elle consiste à autoriser votre connexion depuis une application ou un site Web de cette plateforme où vous êtes déjà connecté. 

GitHub et Google disposent de ces fonctionnalités. Avec l'application GitHub, vous pouvez compléter l'A2F en saisissant un chiffre sur l'écran de l'application/du site Web sur lequel vous vous connectez. Google le fait via votre appareil Android et votre compte Google.

En dehors des méthodes A2F ci-dessus, nous avons également les codes de récupération. Les codes de récupération sont des codes à usage unique que vous pouvez utiliser pour compléter l'A2F. Vous pouvez y accéder dans les paramètres A2F de votre compte.

En fait, une fois que vous avez configuré au moins une méthode A2F sur votre compte, la plateforme génère automatiquement ces codes de récupération pour vous. Ces codes sont comme une option de secours pour l'A2F. Ils sont destinés à être utilisés lorsque vous n'avez pas accès aux autres méthodes A2F.

## Le problème avec l'authentification à deux facteurs

Le problème avec l'A2F est que si vous perdez l'accès à toutes les méthodes que vous avez configurées, **vous avez définitivement perdu l'accès** à ce compte. Laissez-moi vous expliquer.

L'A2F garantit que c'est bien l'utilisateur légitime qui accède au compte. C'est pourquoi nous avons ces méthodes secondaires en plus de votre mot de passe. L'A2F ne peut être activée ou désactivée que lorsque vous êtes connecté. 

Mais à part les codes de récupération, il n'existe aucun autre mécanisme de secours. Si vous perdez les clés de sécurité, le numéro de téléphone, les appareils contenant les applications d'authentification et les connexions précédentes, ainsi que les codes de récupération, votre compte est perdu. Même le support technique de la plateforme ne pourra pas vous aider. 

Il ne s'agit pas de la fonction classique "Mot de passe oublié", où la plateforme envoie un lien ou un code unique à votre e-mail ou téléphone pour réinitialiser votre mot de passe. C'est de l'A2F. Une fois que vous avez perdu toutes les méthodes A2F configurées, votre compte est perdu. Le support ne peut pas vous donner les codes de récupération car il ne les connaît pas. Ces codes sont chiffrés avec l'accès à votre compte (vous seul pouvez y accéder lorsque vous êtes connecté).

Cela signifie-t-il que vous ne devriez pas configurer l'A2F ? 

Non. Cela signifie qu'en plus de configurer l'A2F, vous devez protéger vos méthodes A2F. N'oubliez pas que c'est la sécurité qui nous a menés à l'A2F. Eh bien, l'A2F elle-même a aussi besoin de sécurité. Vous devez donc la sécuriser.

À partir de là, nous allons examiner les différentes choses que vous pouvez faire pour prévenir la perte de compte due à l'authentification à deux facteurs.

## Comment se protéger contre la perte d'accès à vos comptes

### 1. Sauvegarder et noter le(s) code(s) de récupération

Toutes les plateformes qui accordent l'A2F donnent également un ou des codes de récupération. Sauvegardez-les toujours. Copiez et enregistrez les codes de récupération en lieu sûr, à l'endroit de votre choix. Cachez-les discrètement en ligne. Chiffrez-les dans un stockage sécurisé (vault). 

Plus important encore, **notez-les**. Utilisez votre main et écrivez avec un stylo dans un journal ou un livre que vous ne perdrez pas. Vous pouvez également les imprimer et les conserver avec vos documents et certificats. Protégez simplement chaque code de récupération par plateforme de la manière la plus sûre possible.

De plus, ne stockez pas le code de récupération d'un compte dans ce même compte. Personne ne garde de clés de rechange à l'intérieur de sa maison. Vous donnez vos clés de rechange à des personnes de confiance ou vous les gardez dans d'autres endroits où vous pouvez aller les récupérer en cas de besoin. C'est parce que si votre clé principale disparaît pendant que vous êtes dehors, vous pouvez aller chercher les doubles. Vous ne pouvez pas récupérer les clés de rechange lorsqu'elles sont à l'intérieur de la maison et que vous êtes enfermé dehors.

De la même manière, cela n'a aucun sens de garder les codes de récupération de l'A2F de votre compte Google dans le Google Drive de ce compte ou dans un Google Doc privé appartenant à ce même compte. Au moment où vous en aurez besoin, vous ne pourrez pas y accéder.

Les codes de récupération sont des codes **à usage unique**. Vous ne pouvez pas réutiliser le même code de récupération pour une autre session A2F. Vous ne devriez pas vraiment utiliser vos codes de récupération. Si vous commencez à les utiliser, c'est le signe que vous devez soit mettre à jour vos méthodes A2F, désactiver temporairement l'A2F, ou régénérer un nouveau jeu de codes de récupération (pour remplacer ceux utilisés).

Vous pouvez toujours copier vos codes de récupération. De plus, vous pouvez toujours générer un nouveau jeu de codes de récupération sur chaque plateforme. Chaque plateforme le permet. N'oubliez pas que vous devez être connecté pour faire tout cela. 

De même, chaque fois que vous désactivez ou éteignez l'authentification à deux facteurs dans les paramètres de votre compte, les codes de récupération précédents deviennent invalides. Si vous réactivez l'A2F, vous devrez sauvegarder et noter à nouveau les nouveaux codes de récupération.  

Assurez-vous de stocker le(s) code(s) de récupération de chaque plateforme dans des endroits multiples et différents.

### 2. Sauvegarder et noter la clé secrète (seed) de l'application d'authentification

Lors de la configuration de l'A2F par application d'authentification, n'utilisez pas l'option du code QR. Choisissez l'option de la clé secrète (seed). La seed pour les applications d'authentification se présente sous la forme d'une série d'environ 20 à 40 caractères alphanumériques. Lorsque la plateforme vous montre cette seed, commencez par la **noter**. 

Notez la seed de l'application d'authentification dans votre journal ou dans un carnet que vous avez réservé aux sauvegardes. Si possible, copiez-la et imprimez-la. Sauvegardez également la seed de chaque plateforme sur un autre support en ligne où vous pourrez la récupérer. Vous voulez minimiser vos chances de perdre ces seeds. 

Chaque minute, les applications d'authentification génèrent des codes à 6 chiffres **basés sur la seed** et non sur l'application elle-même ou sur la plateforme. Si vous collez cette même seed dans une autre application d'authentification, les deux applications généreront exactement les mêmes 6 chiffres, chaque minute. En fait, si vous réutilisez cette même phrase exacte pour recréer une autre entrée A2F dans la même application d'authentification, les deux entrées généreront le même code à 6 chiffres par minute.

C'est pourquoi la seed de l'application d'authentification est aussi importante que les codes de récupération A2F. Si vous perdez l'accès à l'appareil sur lequel se trouve votre application d'authentification A2F, vous pouvez mettre vos seeds dans une autre application et récupérer les codes à 6 chiffres pour l'A2F. Protégez également ces seeds. Car si quelqu'un possède à la fois vos mots de passe et vos seeds, il a accès à vos comptes.  

Sauvegarder et noter les seeds des applications d'authentification est nécessaire et c'est un point souvent négligé. Beaucoup de gens ne réalisent pas que la perte d'un appareil signifie la perte d'un compte si l'application d'authentification était leur seule méthode A2F et s'ils n'ont pas enregistré la seed et les codes de récupération quelque part. 

Une panne d'appareil peut arriver. Le système d'exploitation peut planter et vous pouvez perdre des applications et des données. L'application d'authentification peut être désinstallée par erreur. La sauvegarde et l'écriture des seeds empêchent ces circonstances d'affecter vos configurations A2F. 

Vous pouvez réinstaller l'application d'authentification et reconfigurer les entrées de chaque compte à partir de votre seed enregistrée, sans avoir besoin d'aller dans les paramètres de compte de chaque plateforme. De plus, vous serez capable de continuer à utiliser vos méthodes d'authentification à deux facteurs, sans avoir besoin de sauvegarder ou de noter à nouveau un nouveau jeu de codes de récupération.

Si vous avez déjà configuré l'A2F par application d'authentification et que vous n'avez pas enregistré la seed originale que la plateforme de votre compte vous a fournie, s'il vous plaît, s'il vous plaît, s'il vous plaît, allez reconfigurer l'A2F par application d'authentification dans vos paramètres de sécurité. Il vous suffira peut-être de désactiver uniquement l'application d'authentification et de la réactiver. Lors de la réactivation, assurez-vous de sauvegarder et de noter la seed. Vous ne voulez pas vivre l'expérience d'être enfermé hors de votre compte.

### 3. Configurer plus d'une méthode A2F

Configurer plus d'une méthode pour l'authentification à deux facteurs réduit vos risques de perte de compte. L'idée est de s'assurer que vous avez toujours accès à au moins une (sinon toutes) les méthodes A2F. Vous pouvez configurer toutes les méthodes A2F disponibles par compte de plateforme. 

Pour la clé de sécurité USB/Bluetooth, vous pouvez utiliser la même clé pour tous vos comptes sur diverses plateformes. Pour votre numéro de téléphone, vous pouvez utiliser le même numéro de téléphone pour chaque compte sur chaque plateforme. (Mais certaines plateformes ne vous permettent pas d'avoir plusieurs comptes avec le même numéro de téléphone. Gardez cela à l'esprit si vous êtes dans ce cas).

La seed de l'application d'authentification pour chaque compte par plateforme est différente. Mais vous pouvez utiliser la même application d'authentification pour tous les comptes dans lesquels vous avez configuré l'A2F. N'oubliez pas de sauvegarder et de noter les seeds comme mentionné dans la section précédente.

Ainsi, pour chaque plateforme, vous voulez vous assurer d'avoir configuré plus d'une méthode A2F. Vous pouvez recevoir un SMS avec un numéro de téléphone. Vous avez une application d'authentification fonctionnelle. Vous avez sauvegardé et noté la seed de l'application d'authentification et les codes de récupération A2F. Et là où vous le pouvez, vous avez également configuré la clé de sécurité USB/Bluetooth.

### 4. Toujours mettre à jour les méthodes A2F

Des événements peuvent survenir qui justifient la mise à jour de vos méthodes A2F. La mise à jour des méthodes A2F comprend la suppression ou l'ajout de certaines méthodes. Vous pouvez également modifier les paramètres d'une même méthode. 

Par exemple, supposons que vous n'ayez jamais eu de clé de sécurité sur votre compte, mais que vous aviez configuré l'A2F avec un numéro de téléphone et une application d'authentification. Ensuite, vous venez d'acheter une nouvelle clé de sécurité. Vous pouvez aller ajouter la clé de sécurité dans vos paramètres A2F en tant que nouvelle méthode. D'un autre côté, si vous perdez votre clé de sécurité USB/Bluetooth, vous pouvez désactiver l'option clé de sécurité. Puis, lorsque vous en achetez une nouvelle, vous pouvez la remettre dans vos paramètres. 

Si vous avez perdu toutes vos sauvegardes et versions écrites de vos seeds d'application d'authentification et de vos codes de récupération A2F, vous pouvez en régénérer de nouveaux et les sauvegarder/noter à nouveau. Vous ne devriez vraiment pas tout perdre. Une telle perte n'est pas bonne. Eh bien, tout est possible. La prévention est le seul remède car il n'existe aucune solution miracle au monde pour une perte complète d'A2F. 

De plus, il est possible de désactiver l'A2F si vous en avez besoin. L'A2F est recommandée et nécessaire. Mais si vous en voyez la nécessité, désactivez-la pour le moment. Ensuite, configurez-la à nouveau un peu plus tard. 

### 5. Configurer un e-mail et un téléphone de récupération 

L'e-mail et le téléphone de secours ne sont pas vraiment des éléments de l'A2F. La raison en est qu'ils sont toujours là, que vous configuriez le deuxième facteur ou non. La plupart des grandes plateformes vous permettent de définir un e-mail de récupération et/ou un numéro de téléphone de récupération pour votre compte. Ces ressources de récupération sont utiles lorsque vous oubliez votre mot de passe et non lorsque vous perdez l'A2F.

Cependant, puisque nous parlons de sécurité, il convient de mentionner que vous devriez avoir un e-mail et un téléphone de récupération correctement configurés là où c'est possible. 

Sur certaines plateformes, votre compte ou votre numéro de téléphone de récupération peut être différent de votre numéro de téléphone A2F. Votre numéro de téléphone A2F doit toujours être celui sur lequel vous pouvez recevoir un OTP (par appel ou SMS) et l'utiliser pour compléter l'étape A2F.

## Résumé

Vous voulez bloquer tout accès malveillant à votre compte. Mais vous ne voulez pas vous bloquer vous-même.  

Dans ce guide, nous avons examiné comment utiliser au mieux la fonctionnalité d'authentification à deux facteurs sur divers comptes. En même temps, nous avons également vu comment vous pouvez vous assurer de ne pas perdre l'accès à votre compte parce que vous avez essayé de le sécuriser en premier lieu.

Sauvegardez et notez les codes de récupération et les seeds des applications d'authentification. Configurez plusieurs méthodes A2F. Révisez et mettez à jour régulièrement vos paramètres A2F. Faites cela et soyez assuré de bénéficier de la meilleure sécurité en ligne.

Santé !