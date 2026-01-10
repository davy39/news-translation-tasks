---
title: Comment protéger votre application Web Laravel contre les 10 principaux risques
  de sécurité OWASP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-18T21:50:07.000Z'
originalURL: https://freecodecamp.org/news/protect-your-laravel-app-against-the-owasp-top-10-security-risks
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c992d740569d1a4ca1e3d.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: Laravel
  slug: laravel
- name: Web Security
  slug: web-security
seo_title: Comment protéger votre application Web Laravel contre les 10 principaux
  risques de sécurité OWASP
seo_desc: 'By Darren Chowles

  I remember the first time one of my sites got hacked.

  The client emailed saying their website was taking ages to load. I jumped online
  as soon as I got home from college and noticed somebody had used SQL injection to
  inject a <scrip...'
---

Par Darren Chowles

Je me souviens de la première fois où l'un de mes sites a été piraté.

Le client m'a envoyé un e-mail disant que leur site web mettait des âges à se charger. Je me suis connecté dès que je suis rentré de l'université et j'ai remarqué que quelqu'un avait utilisé une injection SQL pour injecter une balise `<script>` dans tous les titres des produits. 

Le script tentait de rediriger les visiteurs vers un site web malveillant. J'étais dévasté.

C'était en 2004, et je venais d'apprendre ASP et SQL Server par moi-même. Ce fut un moment de lucidité et l'un de ceux qui m'ont fait réaliser que n'importe quel site web pouvait être une cible, peu importe sa taille. 

Cela m'a également appris l'importance de la sécurité web, et elle a été au premier plan de mon processus de développement depuis lors.

Aucun site ne peut jamais être complètement sûr — le nombre élevé de violations de haute visibilité en témoigne. Mais vous pouvez suivre certaines meilleures pratiques pour rendre votre site moins cible pour un acteur malveillant occasionnel ou un script automatisé.

## OWASP & Laravel

Le projet Open Web Application Security Project (OWASP) est une organisation internationale à but non lucratif dédiée à la création de sensibilisation sur la sécurité des applications web. 

Le Top Ten de l'OWASP est un guide de sensibilisation standard sur la sécurité des applications web et se compose des risques de sécurité les plus critiques pour les applications web.

Laravel est l'un de mes frameworks PHP préférés. Je l'ai utilisé extensivement au fil des ans pour tout, des sites de petites entreprises aux grandes applications fintech et e-commerce exigeant une sécurité au cœur. 

La grande chose est que Laravel prend en charge de nombreuses fonctionnalités de sécurité dès la sortie de la boîte.

Je vais passer en revue le Top Ten de l'OWASP et noter comment vous pouvez renforcer vos applications web Laravel avec quelques meilleures pratiques de sécurité de base.

## 1. Injection

![Image](https://www.freecodecamp.org/news/content/images/2020/08/exploits_of_a_mom.png)
_Source : [https://xkcd.com/327/](https://xkcd.com/327/" rel="noopener)_

> « Les failles d'injection, telles que SQL, NoSQL, OS et LDAP, se produisent lorsque des données non fiables sont envoyées à un interpréteur dans le cadre d'une commande ou d'une requête. Les données hostiles de l'attaquant peuvent tromper l'interpréteur pour qu'il exécute des commandes non intentionnelles ou accède à des données sans autorisation appropriée. » — [OWASP Top 10](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A1-Injection)

Le constructeur de requêtes Laravel utilise la liaison de paramètres PDO pour protéger l'application contre les attaques par injection SQL. Cela signifie que vous n'avez pas à nettoyer les valeurs passées en tant que liaisons.

Sachez que Laravel permet également d'exécuter des requêtes SQL brutes. Vous devriez éviter cela si possible. Restez avec [Eloquent](https://laravel.com/docs/7.x/eloquent) à la place.

Gardez à l'esprit que PDO ne supporte pas la liaison des noms de colonnes. Vous ne devriez jamais utiliser l'entrée des utilisateurs pour dicter le nom de la colonne de la table, y compris les colonnes utilisées dans une instruction `ORDER BY`. 

Si vous avez besoin de flexibilité, assurez-vous de vérifier les noms de colonnes par rapport à une liste blanche.

## 2. Authentification défaillante

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-153.png)
_Photo par [Unsplash](https://unsplash.com/@danny144?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Dan Nelson</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

> « Les fonctions d'application liées à l'authentification et à la gestion des sessions sont souvent mises en œuvre incorrectement, permettant aux attaquants de compromettre les mots de passe, les clés ou les jetons de session, ou d'exploiter d'autres failles de mise en œuvre pour usurper temporairement ou définitivement l'identité d'autres utilisateurs. » — [OWASP Top 10](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A2-Broken_Authentication)

Il existe plusieurs stratégies que vous pouvez utiliser pour protéger votre application contre ce type d'attaque.

* Utilisez CAPTCHA pour tous les points de terminaison qui peuvent être exploités à l'aide de techniques de force brute. Cela inclut les formulaires de connexion, d'inscription et de mot de passe oublié. CAPTCHA stoppera la plupart des attaques automatisées. Optez pour quelque chose comme reCAPTCHA de Google plutôt que de développer votre propre implémentation.
* Limitez le taux de tentatives de connexion. Si utilisé en conjonction avec CAPTCHA, cela permet une excellente stratégie de défense en profondeur. Laravel dispose d'un [middleware](https://laravel.com/docs/7.x/routing#rate-limiting) qui peut être utilisé directement dans vos routes ou contrôleurs pour limiter les requêtes.
* Construisez une authentification multifactorielle pour vos comptes membres et administrateurs. Il existe d'excellents [packages](https://github.com/antonioribeiro/google2fa) disponibles que vous pouvez utiliser pour générer des codes QR et valider les codes de mot de passe à usage unique lors de la connexion. Évitez d'autres moyens de livraison de ce code, tels que l'e-mail ou le SMS. Ce n'est tout simplement [pas assez sécurisé](https://blog.sucuri.net/2020/01/why-2fa-sms-is-a-bad-idea.html).
* Ne commettez jamais de détails de connexion par défaut ou d'identifiants d'API sensibles dans votre dépôt de code. Maintenez ces paramètres dans le fichier `.env` à la racine du projet.
* Configurez les sessions de manière sécurisée : elles doivent être envoyées uniquement via HTTPS et ne jamais s'afficher dans votre application. Le paramètre `secure` peut être activé dans le fichier de configuration `session.php` de votre application Laravel.

## 3. Exposition de données sensibles

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-154.png)
_Photo par [Unsplash](https://unsplash.com/@tjevans?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Tim Evans</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

> « De nombreuses applications web et API ne protègent pas correctement les données sensibles, telles que les données financières, de santé et les informations personnelles identifiables (PII). Les attaquants peuvent voler ou modifier ces données faiblement protégées pour commettre des fraudes par carte de crédit, des vols d'identité ou d'autres crimes. Les données sensibles peuvent être compromises sans protection supplémentaire, telle que le chiffrement au repos ou en transit, et nécessitent des précautions spéciales lors de l'échange avec le navigateur. » — [OWASP Top 10](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A3-Sensitive_Data_Exposure)

Il ne se passe pas une semaine sans qu'on entende parler d'une autre violation de données de haute visibilité. Et le plus préoccupant de tout, c'est que parfois, ces violations révèlent comment l'entreprise a utilisé des pratiques de sécurité faibles. Les hachages de mots de passe faibles et les compartiments S3 non sécurisés sont des occurrences courantes.

Voici quelques moyens de lutter contre cela :

* Assurez-vous de servir l'ensemble de l'application via HTTPS avec un certificat TLS. Si les utilisateurs tentent d'accéder à l'équivalent HTTP, redirigez-les vers la route sécurisée et utilisez les en-têtes [HSTS](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html).
* Hachez tous les mots de passe à l'aide d'une fonction de hachage salée adaptative. Ce sont des fonctions de hachage où le facteur de travail peut être augmenté au fil du temps à mesure que la puissance du processeur augmente. Laravel supporte à la fois Bcrypt et Argon2 par défaut.
* Chiffrez toutes les données sensibles stockées au repos. N'utilisez jamais vos propres fonctions de chiffrement développées. Utilisez plutôt les fonctions de chiffrement [intégrées](https://laravel.com/docs/7.x/encryption) de Laravel qui utilisent OpenSSL pour fournir un chiffrement AES-256 et AES-128.
* Si vous utilisez l'énumération pour les fichiers ou les clés primaires pour identifier les enregistrements, vous pourriez involontairement exposer des informations sur votre système. L'utilisation d'une URL comme `/profil-membre/23` révélera que vous avez (au moins) 23 membres sur votre système. Si vous incluez des fichiers téléchargés comme `/images-utilisateurs/45.jpg`, vous pourriez vous ouvrir à une attaque par énumération où un acteur malveillant pourrait essayer toutes les combinaisons de nombres et extraire toutes les images des utilisateurs de votre site web. Pour lutter contre cela, utilisez un schéma différent comme UUIDv4 pour identifier les enregistrements qui sont publics et pourraient nécessiter une protection. Pour les fichiers, utilisez des noms de fichiers générés automatiquement ou une structure de dossiers hachée pour prévenir l'énumération.

Ne faites jamais confiance aux fichiers téléchargés par les utilisateurs. Si ces fichiers téléchargés ne sont pas validés ou traités correctement, ils peuvent permettre l'accès à l'ensemble de votre système. La page OWASP sur le [téléchargement de fichiers non restreint](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload) inclut plusieurs précautions à prendre. Vous pouvez implémenter la plupart de celles-ci en utilisant la fonctionnalité de validation de Laravel :

* Définir une taille minimale et maximale pour le [téléchargement de fichiers](https://laravel.com/docs/7.x/validation#rule-size).
* Limiter le nombre de téléchargements de fichiers simultanés.
* N'autoriser que des types de fichiers spécifiques en vérifiant leur [MIME](https://laravel.com/docs/7.x/validation#rule-mimes).
* Renommer tous les fichiers lors du téléchargement.
* Télécharger les fichiers dans un répertoire non public ou un stockage d'objets tiers comme AWS S3. Vous ne voulez pas que quelqu'un télécharge un script shell PHP, lui permettant d'exécuter des commandes directement sur votre serveur.

Le mieux de tout, vous pouvez envelopper tout cela dans une [règle](https://laravel.com/docs/7.x/validation#custom-validation-rules) Laravel et simplement appeler cette règle dans votre flux de validation.

## 4. Entités externes XML (XXE)

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-155.png)
_Photo par [Unsplash](https://unsplash.com/@markuswinkler?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Markus Winkler</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

> « De nombreux processeurs XML plus anciens ou mal configurés évaluent les références d'entités externes dans les documents XML. Les entités externes peuvent être utilisées pour divulguer des fichiers internes en utilisant le gestionnaire d'URI de fichiers, des partages de fichiers internes, des analyses de ports internes, l'exécution de code à distance et des attaques par déni de service. » — [OWASP Top 10](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A4-XML_External_Entities_%28XXE%29)

Cette vulnérabilité s'applique à tout système qui analyse le XML. Un chercheur en sécurité a découvert cette vulnérabilité sur Facebook il y a quelques années. Cet [article de SensePost](https://sensepost.com/blog/2014/revisting-xxe-and-abusing-protocols/) explique plus en détail comment cela a été accompli.

Le moyen le plus rapide de prévenir cette attaque est de désactiver la résolution des entités externes lors de l'utilisation de l'analyseur XML [PHP par défaut](https://www.php.net/manual/en/ref.libxml.php). Cela se fait en définissant `libxml_disable_entity_loader` sur `true`.

Si vous ne pouvez pas désactiver cette fonctionnalité, assurez-vous que votre analyseur XML est à jour et que vous utilisez au moins SOAP v1.2 ou supérieur lorsque cela est applicable. Soyez toujours vigilant lorsqu'il s'agit de XML téléchargé par les utilisateurs ou tiers.

## 5. Contrôle d'accès défaillant

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-156.png)
_Photo par [Unsplash](https://unsplash.com/@brazofuerte?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Collin Armstrong</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

> « Les restrictions sur ce que les utilisateurs authentifiés sont autorisés à faire ne sont souvent pas correctement appliquées. Les attaquants peuvent exploiter ces failles pour accéder à des fonctionnalités et/ou des données non autorisées, telles que l'accès aux comptes d'autres utilisateurs, la visualisation de fichiers sensibles, la modification des données d'autres utilisateurs, le changement des droits d'accès, etc. » — [OWASP Top 10](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A5-Broken_Access_Control)

En [2011](https://www.nytimes.com/2011/06/14/technology/14security.html), des attaquants se sont emparés des détails de plus de 200 000 clients de Citigroup après avoir découvert une faille dans la manière dont ils géraient les numéros de compte client. Une fois connectés à un compte, ils n'avaient qu'à changer le numéro de client dans l'URL pour accéder à l'enregistrement d'un autre client. 

Cela leur a permis de créer un processus automatisé qui parcourrait tous les numéros possibles et capturerait toutes les données confidentielles. 

Le système n'avait aucune vérification d'autorisation en place pour s'assurer que le numéro de compte consulté appartenait à l'utilisateur connecté.

* Effectuez toujours des vérifications d'autorisation sur toute opération disponible uniquement pour les utilisateurs connectés. Cela inclut la page (par exemple, vous permettant de mettre à jour les détails), ainsi que la destination de la soumission du formulaire.
* Il existe des packages RBAC (Role-Based Access Control) populaires qui peuvent être utilisés avec Laravel, vous permettant de gérer les permissions et les rôles des utilisateurs. Vous pouvez également utiliser les services d'autorisation [intégrés](https://laravel.com/docs/7.x/authorization) de Laravel.

## 6. Mauvaise configuration de la sécurité

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-157.png)
_Photo par [Unsplash](https://unsplash.com/@fantasyflip?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Philipp Katzenberger</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

> « La mauvaise configuration de la sécurité est le problème le plus couramment observé. Cela est souvent le résultat de configurations par défaut non sécurisées, de configurations incomplètes ou ad hoc, de stockage cloud ouvert, d'en-têtes HTTP mal configurés et de messages d'erreur verbeux contenant des informations sensibles. Non seulement tous les systèmes d'exploitation, frameworks, bibliothèques et applications doivent être configurés de manière sécurisée, mais ils doivent être corrigés/mis à jour en temps opportun. » — [OWASP Top 10](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A6-Security_Misconfiguration)

Lors de la configuration de votre application web, tenez toujours compte du principe de moindre fonctionnalité. Renforcez votre installation en supprimant ou en désactivant tous les services dont vous n'avez pas besoin.

En 2001, le ver Nimda a semé le chaos mondial en exploitant plusieurs vulnérabilités d'IIS (Internet Information Server). 

De nombreux systèmes avaient IIS installé par défaut, même s'ils n'utilisaient pas du tout le serveur web Microsoft. Le résultat a été un taux d'infection élevé qui aurait pu être évité en renforçant le système et en désinstallant tous les services non requis par le système ou le réseau.

* Maintenez à jour tous les logiciels serveurs et les dépendances de votre application web.
* Désactivez la liste des répertoires pour votre serveur web.
* Désactivez le débogage sur les serveurs de production. Même sur les serveurs de staging, le débogage peut révéler des informations sensibles du serveur en affichant toutes vos variables d'environnement. Utilisez l'option de configuration `debug_hide` de l'application [configuration option](https://laravel.com/docs/7.x/configuration#hiding-environment-variables-from-debug) dans Laravel pour éviter cela.

## 7. Cross-Site Scripting (XSS)

![Image](undefined)
_Photo par [Unsplash](https://unsplash.com/@pankajpatel?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Pankaj Patel</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

> « Les failles XSS se produisent chaque fois qu'une application inclut des données non fiables dans une nouvelle page web sans validation ou échappement approprié, ou met à jour une page web existante avec des données fournies par l'utilisateur en utilisant une API de navigateur qui peut créer du HTML ou du JavaScript. XSS permet aux attaquants d'exécuter des scripts dans le navigateur de la victime, ce qui peut détourner les sessions utilisateur, défigurer les sites web ou rediriger l'utilisateur vers des sites malveillants. » — [OWASP Top 10](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A7-Cross-Site_Scripting_%28XSS%29)

N'affichez jamais les entrées fournies par l'utilisateur sans échapper les données. Le moteur de template de Laravel, Blade, échappe automatiquement le contenu rendu en utilisant la syntaxe par défaut `{{ $var }}`. Cela l'envoie via la fonction `htmlspecialchars` de PHP. 

Échapper toutes les sorties de cette manière réduira l'exposition de vos visiteurs à des attaques XSS et CSRF (Cross-Site Request Forgery).

Malheureusement, ce n'est pas toujours aussi simple. Si vous avez déjà inclus des éditeurs HTML WYSIWYG dans votre application comme TinyMCE ou CKEditor, vous savez que cela pose un risque (surtout puisque l'échappement de la sortie entraînerait un tas de balises HTML plutôt que le contenu formaté). 

Dans ces cas, utilisez un package comme [HTMLPurifier](https://github.com/mewebstudio/Purifier) pour supprimer tout code potentiellement malveillant.

## 8. Désérialisation non sécurisée

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-161.png)
_Photo par [Unsplash](https://unsplash.com/@mr_williams_photography?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Micah Williams</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

> « La désérialisation non sécurisée conduit souvent à l'exécution de code à distance. Même si les failles de désérialisation ne conduisent pas à l'exécution de code à distance, elles peuvent être utilisées pour effectuer des attaques, y compris des attaques par relecture, des attaques par injection et des attaques par élévation de privilèges. » — [OWASP Top 10](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A8-Insecure_Deserialization)

Méfiez-vous de la désérialisation de tout ce qui provient de sources non fiables. Cela inclut les cookies que votre application pourrait créer. Un utilisateur malveillant peut modifier ce cookie dans son navigateur et utiliser cela comme vecteur d'attaque contre votre application.

Par défaut, tous les cookies créés par Laravel sont chiffrés et signés. Cela signifie qu'ils seront invalides si un client les manipule.

## 9. Utilisation de composants avec des vulnérabilités connues

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-162.png)
_Photo par [Unsplash](https://unsplash.com/@_nnaro_?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Diego Gennaro</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

> « Les composants, tels que les bibliothèques, les frameworks et autres modules logiciels, s'exécutent avec les mêmes privilèges que l'application. Si un composant vulnérable est exploité, une telle attaque peut faciliter une perte de données sérieuse ou une prise de contrôle du serveur. Les applications et API utilisant des composants avec des vulnérabilités connues peuvent saper les défenses de l'application et permettre diverses attaques et impacts. » — [OWASP Top 10](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A9-Using_Components_with_Known_Vulnerabilities)

Parce que la plupart des dépendances que vous pourriez utiliser dans Laravel sont open source, cela permet aux utilisateurs malveillants d'analyser les packages et de trouver des moyens d'exploiter les vulnérabilités. Voici quelques idées pour atténuer ce problème :

* Assurez-vous de maintenir toutes les dépendances à jour.
* Supprimez toutes les dépendances non utilisées. Cela réduira le nombre potentiel de points d'entrée d'attaque.
* Abonnez-vous aux bulletins de sécurité et incluez un scanner de sécurité (tel que [Snyk](https://snyk.io/)) dans votre pipeline CI/CD.
* Envisagez d'utiliser une version LTS (Long Term Support) de Laravel plutôt que la dernière version. Les versions LTS reçoivent des correctifs de sécurité pendant trois ans plutôt qu'un an pour les versions non-LTS.

## 10. Journalisation et surveillance insuffisantes

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-163.png)
_Photo par [Unsplash](https://unsplash.com/@cspek?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Chris Nguyen</a> sur <a href="https://unsplash.com/@cspek?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)_

> « Une journalisation et une surveillance insuffisantes, couplées à une intégration manquante ou inefficace avec la réponse aux incidents, permettent aux attaquants d'attaquer davantage les systèmes, de maintenir la persistance, de pivoter vers plus de systèmes et de falsifier, extraire ou détruire des données. La plupart des études sur les violations montrent que le temps pour détecter une violation est de plus de 200 jours, généralement détecté par des parties externes plutôt que par des processus ou une surveillance internes. » — [OWASP Top 10](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A10-Insufficient_Logging%252526Monitoring)

En ce qui concerne votre application et votre serveur, journalisez tout, y compris les tentatives de connexion échouées et les réinitialisations de mot de passe. 

Laravel est livré avec [Monolog](https://github.com/Seldaek/monolog) dès la sortie de la boîte. Vous pouvez même l'intégrer avec un service de journalisation tiers comme [Papertrail](https://www.papertrail.com/) et recevoir des alertes pour des événements de journal spécifiques.

## Conclusion

Merci d'avoir lu, j'espère que cela s'est avéré utile ! [Inscrivez-vous à ma newsletter](https://webdev.chowles.com/) ou [visitez mon blog](https://www.chowles.com/) où je partagerai des articles perspicaces sur le développement web pour supercharger vos compétences.

## Ressources

Le site web OWASP est une source brillante d'informations, et ils fournissent plusieurs guides approfondis sur de nombreux problèmes de sécurité mentionnés ci-dessus.

* Consultez le [OWASP Top 10](https://owasp.org/www-project-top-ten/) ([Téléchargement PDF](https://github.com/OWASP/Top10/raw/master/2017/OWASP%20Top%2010-2017%20%28en%29.pdf)).
* Consultez et téléchargez les [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/).
* Dernière [documentation Laravel](https://laravel.com/docs/7.x).