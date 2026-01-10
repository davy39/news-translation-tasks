---
title: Comment j'ai construit une application mobile pour le shopping en ligne pendant
  le confinement COVID-19
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-08T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-mobile-app-for-online-shopping-amid-covid-19-lock-down
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/ecommerce-blog-1.jpg
tags:
- name: android app development
  slug: android-app-development
- name: ecommerce
  slug: ecommerce
- name: Java
  slug: java
- name: mobile app development
  slug: mobile-app-development
seo_title: Comment j'ai construit une application mobile pour le shopping en ligne
  pendant le confinement COVID-19
seo_desc: 'By Ogbeta Ovokerie

  When many stores that sell nonessential items were ordered to close in March by
  government decrees, consumers moved their shopping online. U.S. online sales increased
  49% in April over the prior year, according to Adobe Analytics. ...'
---

Par Ogbeta Ovokerie

Lorsque de nombreux magasins vendant des articles non essentiels ont été contraints de fermer en mars par décret gouvernemental, les consommateurs ont transféré leurs achats en ligne. Les ventes en ligne aux États-Unis ont augmenté de 49 % en avril par rapport à l'année précédente, selon [Adobe Analytics](https://www.adobe.com/analytics/abobe-analytics.html). 

L'augmentation des ventes n'a pas été particulièrement significative sur ordinateur. Mais les applications mobiles de shopping comme Instacart [ont vu une augmentation d'environ 650 % (wow !)](https://www.visualcapitalist.com/covid-19-impact-on-popularity/) de nouveaux utilisateurs d'applications mobiles (aux États-Unis seulement) entre mars et avril. 

Ainsi, pour que les boutiques e-Commerce tirent pleinement parti de l'augmentation des acheteurs en ligne pendant la pandémie de coronavirus, elles devraient avoir une application mobile native. 

Dans ce tutoriel, je vais développer une application mobile native Android en utilisant le thème Woocommerce. Je vais également expliquer pourquoi j'ai opté pour une application mobile native (au lieu d'une application hybride ou d'une application web progressive) et le thème Woocommerce. Mieux encore, je vais commencer par quelques données de recherche pour montrer à quel point il est important pour une boutique e-Commerce d'avoir une application mobile.

## Le trafic vers les magasins physiques a presque disparu

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Is-there-anybody-out-there.jpg)
_Y a-t-il quelqu'un là-bas ?_

Les enquêtes auprès des consommateurs suggèrent que le passage au shopping en ligne se poursuivra tant que le COVID-19 représentera une menace. Une [enquête auprès de 1 200 consommateurs fin mars](https://www.rsrresearch.com/research) 2020 a révélé que 90 % des acheteurs hésitaient à faire leurs achats en magasin en raison de la pandémie de coronavirus. Et 45 % s'attendaient à ce que le shopping en ligne soit une nécessité pour eux pendant la crise. 

Une [enquête séparée en avril](https://bizrateinsights.com/) a révélé que 55 % des consommateurs en ligne ont déclaré qu'ils commandaient plus en ligne qu'avant l'arrivée du virus, contre 26 % en mars. Et 22 % ont déclaré en avril qu'ils commandaient beaucoup plus en ligne, contre seulement 6 % en mars. 

Si la pandémie continue de persister, il pourrait y avoir un grand changement vers le shopping en ligne pendant les deux plus grandes saisons de l'année pour les détaillants – la rentrée des classes et les achats de vacances. 23 % des détaillants [interrogés en mars](https://go.forrester.com/research/) prévoyaient de réorienter leurs ressources en raison de l'épidémie de coronavirus.

Le commerce de détail a été contraint d'effectuer certains changements majeurs. Alors que toutes les entreprises non essentielles étaient incitées à fermer, et le trafic piéton dans les magasins de détail physiques [a presque entièrement disparu](https://qz.com/1829531/covid-19-has-caused-us-retail-traffic-to-almost-entirely-vanish/). Même avec des réouvertures échelonnées, l'importance d'avoir une fonctionnalité e-Commerce est plus claire que jamais. 

La pandémie a prouvé le besoin pour les entreprises de tous types d'être flexibles et prêtes à tout, et le besoin pour elles de faire le saut numérique. L'e-Commerce sera au premier plan pour la nouvelle normalité.

## Mais mon client a un site web responsive !

Un certain nombre de tendances convergent pour inciter les propriétaires de sites web à vouloir une application mobile native. L'objectif principal de chaque propriétaire de site web est d'ajouter de la valeur à l'entreprise en atteignant plus d'utilisateurs. Je pense qu'il ne sera pas surprenant d'apprendre que l'utilisation des téléphones mobiles est en hausse et que plus de personnes interagissent avec leurs téléphones mobiles qu'avec les ordinateurs de bureau. 

Afin de toucher ce marché d'utilisateurs de téléphones mobiles, nous devons savoir quels types d'applications ces utilisateurs de téléphones mobiles utilisent le plus (applications web progressives, applications hybrides, sites web mobiles responsives ou applications natives). Heureusement pour nous, les gens de [Go-Globe](https://www.go-globe.com/mobile-apps-usage) ont fait une analyse : un impressionnant 85 % des utilisateurs mobiles interagissent le plus avec les applications mobiles natives.

Il existe un certain nombre d'autres raisons pour lesquelles les entreprises devraient avoir une application mobile native pour répondre aux besoins du nombre croissant d'acheteurs en ligne pendant la pandémie de coronavirus. Explorons-les maintenant un peu plus.

### Elles offrent une meilleure expérience aux visiteurs fidèles du site web

Les sites mobiles sont excellents pour la découverte. Mais les utilisateurs fidèles – ceux qui reviennent plus souvent – veulent avoir une application. Les gens utilisent les applications plus qu'ils n'utilisent la recherche sur les appareils mobiles. Une marque (c'est-à-dire une application) sur l'écran d'accueil d'un utilisateur est un rappel constant d'un site et de son contenu.

### Elles se connectent directement avec les visiteurs du site web

Une marque peut être présente sur tous les canaux sociaux, mais seulement une fraction des utilisateurs verra jamais son message. Des e-mails peuvent également être envoyés, mais avec un taux d'ouverture de 25 %, seulement une fraction du public sera atteinte.

Une application mobile de marque donne une ligne directe aux utilisateurs, retenant finalement les utilisateurs et transformant les visiteurs occasionnels en utilisateurs fidèles.

### Elles utilisent les fonctionnalités des appareils mobiles

Les applications mobiles natives ont l'avantage d'utiliser les fonctionnalités d'un téléphone mobile comme l'appareil photo, la liste de contacts, le GPS, les appels téléphoniques, l'accéléromètre, la boussole, etc. De telles fonctionnalités de l'appareil, lorsqu'elles sont utilisées dans une application, peuvent rendre l'expérience utilisateur interactive et amusante. 

De plus, ces fonctionnalités peuvent également réduire les efforts que les utilisateurs devraient faire autrement. Par exemple, les utilisateurs qui souhaitent connaître l'emplacement d'une entreprise peuvent utiliser le GPS/navigation pour le trouver facilement (particulièrement utile dans les applications de nourriture). 

Ces fonctionnalités peuvent également réduire considérablement le temps que les utilisateurs mettent pour effectuer une certaine tâche dans une application, et peuvent même stimuler les conversions. 

Les sites web mobiles, les PWA et les applications hybrides peuvent également utiliser certaines des fonctionnalités de l'appareil. Cependant, il existe des contraintes ou des limites technologiques dans l'utilisation de toutes les fonctionnalités d'un appareil que les applications mobiles natives peuvent utiliser facilement.

### Elles vous donnent la possibilité de travailler hors ligne

C'est probablement la différence la plus fondamentale entre un site web mobile et une application. Bien que les applications mobiles natives puissent nécessiter une connectivité Internet pour effectuer la plupart de leurs tâches, elles peuvent encore offrir un contenu et une fonctionnalité de base aux utilisateurs en mode hors ligne. 

Prenons l'exemple d'un site web e-Commerce – l'application peut fournir des fonctionnalités comme le calcul des taxes et des versements, et déterminer la limite de dépenses d'un utilisateur. Ces fonctionnalités peuvent fonctionner même sans l'aide d'une connexion Internet.

Même si les sites web mobiles, les PWA et les applications mobiles hybrides peuvent utiliser la mise en cache pour charger des pages web sans connexion Internet, ils ne peuvent offrir que des fonctions limitées.

### Elles aident à augmenter la présence de la marque

Les utilisateurs passent une partie substantielle de leur temps sur les appareils mobiles. Il est sûr de dire que de nombreux utilisateurs voient les applications qu'ils ont installées sur leurs appareils presque tous les jours.

Cette rencontre régulière peut être vue comme une opportunité de marque pour les applications. Même lorsque les utilisateurs n'utilisent pas activement une application mobile, ils sont toujours rappelés de la marque associée à l'application. L'icône de l'application agit comme une mini-publicité pour la marque.  


La présence d'une application sur l'appareil d'un utilisateur aide à influencer leur perception d'une marque de manière subconsciente. Ce comportement peut être lié à la Théorie de la Détection du Signal, qui suggère que les utilisateurs traitent encore les publicités qu'ils ont ignorées à un certain niveau de manière subconsciente.

### Les applications peuvent fonctionner plus rapidement que les sites web

Une application mobile bien conçue peut effectuer des actions beaucoup plus rapidement qu'un site web mobile.  
Les applications stockent généralement leurs données localement sur les appareils mobiles, contrairement aux sites web qui utilisent généralement des serveurs web. Pour cette raison, la récupération des données se fait rapidement dans les applications mobiles. 

Les applications peuvent également économiser le temps des utilisateurs en stockant leurs préférences et en les utilisant pour prendre des actions proactives en leur nom.

Il existe également une justification technique quant à la raison pour laquelle les applications mobiles peuvent fonctionner plus rapidement. Les sites web mobiles utilisent le code JavaScript pour effectuer la plupart de leurs fonctions. Et certains des frameworks que les applications mobiles utilisent peuvent fonctionner presque cinq fois plus rapidement que JavaScript ! 

Pendant que tout cela se passe en arrière-plan, les utilisateurs peuvent accomplir des actions plus rapidement sur l'interface frontale des applications mobiles, contribuant à nouveau à une expérience utilisateur agréable.

### Elles augmentent le potentiel SEO pour un site web

Les applications mobiles peuvent être avantageuses de deux manières – pour le contenu dans l'application et le contenu du site web, car des mots synonymes seront utilisés dans le contenu pour les produits et services. Google classe également le contenu dans les applications et vous pouvez modifier votre contenu dans votre application pour vous aider avec le SEO de votre site web.

### Les dépenses pour les applications mobiles devraient doubler d'ici 2024, malgré les impacts économiques du COVID-19

[Selon une prévision de marché révisée 2020-2024](https://sensortower.com/blog/sensor-tower-app-market-forecast-2024), les dépenses mondiales des consommateurs dans les applications mobiles devraient atteindre 171 milliards de dollars d'ici 2024. Cela représente plus du double des 85 milliards de dollars de 2019. 

Ce total, cependant, est d'environ 3 milliards de dollars (ou 2 %) de moins que la prévision que la firme avait publiée avant l'épidémie de COVID-19.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/mobile-app-spending.png)
_Dépenses pour les applications mobiles_

Néanmoins, il est notable que même les régions à la croissance la plus lente sur l'App Store d'Apple et Google Play verront des revenus supérieurs de plus de 80 % à leurs niveaux de 2019 d'ici l'année 2024. Les magasins d'applications atteindront également plusieurs jalons au cours des cinq prochaines années. 

Pour commencer, les dépenses mondiales dans les applications mobiles dépasseront 100 milliards de dollars pour la première fois en 2020, avec une croissance d'environ 20 % d'une année sur l'autre pour atteindre 102 milliards de dollars. Cela indique que les propriétaires de sites web n'obtiennent pas seulement plus de clients, mais plus de clients payants prêts à dépenser.

### Elles atteignent un public plus jeune

Les statistiques indiquent que les 18-24 ans sont les utilisateurs les plus actifs d'applications mobiles.

Toujours pas convaincu ? Laissez ces statistiques parler :

1. 77 % des Américains possèdent un smartphone.
2. Plus de 230 millions de consommateurs américains possèdent des smartphones.
3. Environ 100 millions de consommateurs américains possèdent des tablettes.
4. 79 % des utilisateurs de smartphones ont effectué un achat en ligne en utilisant leur appareil mobile au cours des 6 derniers mois.
5. Les dollars du e-Commerce représentent désormais 10 % de _tous_ les revenus de détail.
6. 80 % des acheteurs ont utilisé un téléphone mobile à l'intérieur d'un magasin physique pour soit consulter des avis sur les produits, comparer les prix, ou trouver des emplacements de magasins alternatifs.
7. On estime que 10 milliards d'appareils connectés mobiles sont actuellement en utilisation.
8. Les utilisateurs d'applications mobiles passent en moyenne 201,8 minutes par mois à faire du shopping, contre 10,9 minutes/mois pour les utilisateurs de sites web.
9. 58 % des millennials ont mentionné qu'ils préféraient acheter via des applications.

Ignorer ces tendances dans l'évolution du e-Commerce mobile (appelé m-Commerce dans l'industrie) signifie potentiellement manquer de plus en plus de profits à mesure que ces tendances se poursuivent.

## Assez parlé ! Écrivons du code

Toutes les applications mobiles natives ne sont qu'un ensemble de code écrit en Java, Kotlin, Objective-C ou Swift qui manipule des données et des ressources (.png, fichiers .xml). Les données manipulées peuvent être récupérées à partir des capteurs de l'appareil mobile tels que l'écran, la caméra, la mémoire de stockage, le GPS, les haut-parleurs, l'accéléromètre, la boussole, ou à partir d'un serveur. 

Dans ce tutoriel, nous utiliserons les outils suivants :

* **JSoup (une bibliothèque Java) :** JSoup est un analyseur HTML qui peut analyser directement une URL, le contenu texte HTML, et fournit un ensemble d'API très pratiques pour manipuler les données.
* **Android Studio :** C'est l'outil officiel pour écrire et compiler des applications Android en Java ou Kotlin et produit des fichiers .apk prêts à être installés. Tout le code de ce tutoriel sera écrit en Java.
* **Plugin Woocommerce :** C'est [le plugin e-Commerce le plus populaire pour WordPress](https://trends.builtwith.com/shop/WooCommerce). Donc, construire une application mobile pour le plugin e-Commerce le plus populaire semble être une bonne idée.

## Obtenir et manipuler les données du serveur

Les données seront obtenues à partir du serveur en utilisant une [API RESTful](https://medium.com/extend/what-is-rest-a-simple-explanation-for-beginners-part-1-introduction-b4a072f8740f). WooCommerce (version 2.6+) est entièrement intégré avec l'API REST de WordPress. Cela permet de créer, lire, mettre à jour et supprimer des données en utilisant des requêtes au format JSON. Il utilise les méthodes d'authentification de l'API REST de WordPress et les verbes HTTP standard qui sont compris par la plupart des clients HTTP. 

J'utiliserai la version 2 de l'API, v2 qui est disponible pour Woocommerce version 3.0.x ou ultérieure et WordPress version 4.4 ou ultérieure.

Le format de réponse par défaut est JSON. Les requêtes réussies retourneront un statut HTTP `200 OK`. Certaines informations clés sur les réponses sont :

* Les dates sont retournées au format ISO8601 : `YYYY-MM-DDTHH:MM:SS`
* Les identifiants de ressource sont retournés sous forme d'entiers.
* Tout montant monétaire décimal, tel que les prix ou les totaux, sera retourné sous forme de chaînes avec deux décimales.
* Les autres montants, tels que les comptes d'articles, sont retournés sous forme d'entiers.
* Les champs vides sont généralement inclus comme `null` ou chaîne vide au lieu d'être omis.

La plupart des requêtes faites à l'API REST de Woocommerce doivent être authentifiées en utilisant des clés pré-générées (clé de consommateur et secret de consommateur). De nouvelles clés sont générées via l'interface d'administration de WordPress. Il suffit d'aller dans WooCommerce > Paramètres > API > Clés/Apps.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/woocommerce-api-keys-settings.png)

Cliquez sur le bouton "Ajouter une clé". Dans l'écran suivant, ajoutez une description et sélectionnez l'utilisateur WordPress pour lequel vous souhaitez générer la clé. Ensuite, cliquez sur le bouton "Générer une clé API" et WooCommerce générera des clés API REST pour l'utilisateur sélectionné.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/woocommerce-creating-api-keys.png)

Maintenant que les clés ont été générées, vous devriez voir deux nouvelles clés. Ces deux clés sont votre Clé de Consommateur et Secret de Consommateur.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/woocommerce-api-key-generated.png)

Nous créons ensuite une URL qui inclura le site web de l'entreprise et le point de terminaison de l'API à partir duquel les données au format JSON seront retournées. 

En utilisant la bibliothèque Jsoup, nous nous connectons à l'URL (site web + point de terminaison de l'API) et ajoutons les clés API (clé de consommateur et secret de consommateur) avec d'autres paramètres du point de terminaison de l'API. Presque tous les points de terminaison acceptent des paramètres optionnels qui peuvent être passés comme un paramètre de chaîne de requête HTTP :

```java
public static final int JSOUP_CONNECTION_TIMEOUT = 100000;

String websiteUrl = "www.freecodecamp.shop"; // exemple de site web qui n'existe pas
// Cette API vous permet de récupérer toutes les catégories de produits
String apiExtension = "/wp-json/wc/v2/products/categories";
// Map pour stocker nos paramètres dans un format clé-valeur
HashMap<String, String> data = new HashMap<>();
data.put("page", String.valueOf(page)); // Paramètre de l'API pour obtenir la page actuelle de la collection. Par défaut, c'est 1.
// ajouter les clés API pour l'authentification
data.put("consumer_key", getKey());
data.put("consumer_secret", getSecret());

// concaténer websiteUrl et apiExtension pour former requestUrl
String requestUrl = websiteUrl + apiExtension

try {
    Connection.Response response = Jsoup.connect(requestUrl).timeout(JSOUP_CONNECTION_TIMEOUT).followRedirects(true)
        .ignoreContentType(true)
        .data(data)
        .execute();
		
    String json = response.body();
	// analyser la chaîne json pour obtenir les données nécessaires.

} catch (Exception e){
    // capturer JSONException et IOException
}
```

Les méthodes `getKey()` et `getSecret()` retournent simplement les clés API :

```java

    public static String getKey() {
        return "ck_a89d59d7441f027df0d91f01c9e2dcaxxxxxxxxx";
    }

    public static String getSecret() {
        return "cs_c3f8fe620bd5b1cb3567712eb843609xxxxxxxxx";
    }
```

Mais attendez... pour certains sites web, lorsque j'exécute ce code, il me donne l'erreur `401 Unauthorized`. Il s'agit d'une erreur d'authentification ou de permission, due à des clés API incorrectes... alors, qu'est-ce qui se passe ?

Bien sûr, le code ci-dessus ne fonctionne que pour les sites web sécurisés avec le protocole HTTPS, tandis que les sites web non sécurisés qui utilisent le protocole HTTP devront chiffrer les clés API avant de les envoyer. 

Que signifie cela exactement ? HTTPS est HTTP avec chiffrement, car HTTPS utilise TLS (SSL) pour chiffrer les requêtes et réponses HTTP normales. Cela rend HTTPS bien plus sécurisé que HTTP. Un site web qui utilise HTTP a http:// dans son URL, tandis qu'un site web qui utilise HTTPS a https://.

Vous devez utiliser l'authentification OAuth 1.0a "one-legged" pour vous assurer que vos identifiants d'API REST ne peuvent pas être interceptés par un attaquant. Les paramètres requis sont _oauth_consumer_key, oauth_timestamp, oauth_nonce, oauth_signature_ et _oauth_signature_method._

Nous allons créer une méthode qui obtiendra ces paramètres chiffrés sous forme de HashMap. La méthode, `getAuthenticationPrams(String url, HashMap<String, String> mData)` acceptera une URL de requête (URL du site web + extension de l'API) et tous les paramètres que nous pourrions vouloir ajouter à l'extension de l'API. 

Ici, nous collectons et normalisons nos paramètres, qui incluent tous les paramètres _oauth_*_ à l'exception de la _oauth_signature_ elle-même.

```java
public static HashMap<String, String> getAuthenticationParams(String url, @Nullable HashMap<String, String> mData){
    HashMap<String, String> data = new HashMap<>();
    if(url.startsWith("http://")){
        String nonce = new TimestampService().getNonce();
        String timestamp = new TimestampService().getTimestampInSeconds();

        data.put("oauth_consumer_key", getKey());
        data.put("oauth_signature_method", "HMAC-SHA1");
        data.put("oauth_version", "1.0");
        data.put("oauth_nonce", nonce);
        data.put("oauth_timestamp", timestamp);

        if(mData != null)
            data.putAll(mData);

        String firstBaseString = "GET&" + urlEncoded(url);
        String generatedBaseString = formatQuery(data);

        ParametersList result = new ParametersList();
        result.addQuerystring(generatedBaseString);
        generatedBaseString = result.sort().asOauthBaseString();
        String secondBaseString = "&" + generatedBaseString;

        if (firstBaseString.contains("%3F")) {
            secondBaseString = "%26" + urlEncoded(generatedBaseString);
        }
        String baseString = firstBaseString + secondBaseString;
        String signature = new HmacSha1SignatureService().getSignature(baseString, getSecret(), "");
        data.put("oauth_signature", signature);

    } else{
        data.put("consumer_key", getKey());
        data.put("consumer_secret", getSecret());

        data.putAll(mData);
    }

    return data;
}

```

La classe `TimestampService` génère un timestamp et un nonce pour les paramètres _oauth_nonce_ et _oauth_timestamp_.

```java
import java.util.Random;

public class TimestampService {
    private Timer timer;

    /**
     * Constructeur par défaut.
     */
    public TimestampService() {
        timer = new Timer();
    }

    public String getNonce() {
        Long ts = getTs();
        return String.valueOf(ts + timer.getRandomInteger());
    }

    public String getTimestampInSeconds() {
        return String.valueOf(getTs());
    }

    private Long getTs() {
        return timer.getMilis() / 1000;
    }

    void setTimer(Timer timer) {
        this.timer = timer;
    }

    /**
     * Classe interne qui utilise {@link System} pour générer les timestamps.
     *
     */
    static class Timer {
        private final Random rand = new Random();
        Long getMilis() {
            return System.currentTimeMillis();
        }

        Integer getRandomInteger() {
            return rand.nextInt();
        }
    }

}
```

La méthode `formatQuery(HashMap<String, String> mData)` formate les paramètres en paramètres de requête qui sont un ensemble de paramètres attachés à la fin d'une URL. La méthode `urlEncoded(String url)` traduit la chaîne donnée dans un format application/x-www-form-urlencoded en utilisant un schéma d'encodage spécifique. Cette méthode utilise le schéma d'encodage fourni pour obtenir les octets des caractères non sécurisés.

```java
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;

    private static String formatQuery(HashMap<String, String> mData){
        int i = 0;
        StringBuilder param = new StringBuilder();
        for(String key : mData.keySet()){
            if(i > 0){
                param.append("&");
            }
            param.append(key);
            param.append("=");
            param.append(mData.get(key));
            i++;
        }

        return param.toString();
    }

    private static String urlEncoded(String url) {
        String encodedurl = "";
        try {
            encodedurl = URLEncoder.encode(url, "UTF-8");
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }

        return encodedurl;
    }
```

La classe `ParametersList` prend la requête formatée et l'encode ensuite en utilisant la classe `OAuthEncoder`. Les valeurs qui commencent par _oauth_*_ doivent être encodées dans une chaîne qui sera utilisée plus tard. Le processus de construction de la chaîne est très spécifique :

1. Encoder en pourcentage chaque clé et valeur qui sera signée.
2. Trier la liste des paramètres par ordre alphabétique par clé encodée.
3. Pour chaque paire clé/valeur : 

* Ajouter la clé encodée à la chaîne de sortie
* Ajouter le caractère `=` à la chaîne de sortie
* Ajouter la valeur encodée à la chaîne de sortie
* Si d'autres paires clé/valeur restent, ajouter un caractère `&` à la chaîne de sortie.

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;


public class ParametersList {
    private static final char QUERY_STRING_SEPARATOR = '?';
    private static final String PARAM_SEPARATOR = "&";
    private static final String PAIR_SEPARATOR = "=";
    private static final String EMPTY_STRING = "";

    private final List<Parameter> params;

    public ParametersList() {
        params = new ArrayList<Parameter>();
    }

    ParametersList(List<Parameter> params) {
        this.params = new ArrayList<Parameter>(params);
    }

    public void add(String key, String value) {
        params.add(new Parameter(key, value));
    }

    public String asOauthBaseString() {
        return OAuthEncoder.encode(asFormUrlEncodedString());
    }

    public String asFormUrlEncodedString() {
        if (params.size() == 0) return EMPTY_STRING;

        StringBuilder builder = new StringBuilder();
        for(Parameter p : params) {
            builder.append('&').append(p.asUrlEncodedPair());
        }
        return builder.toString().substring(1);
    }

    public void addAll(ParametersList other) {
        params.addAll(other.params);
    }

    public void addQuerystring(String queryString) {
        if (queryString != null && queryString.length() > 0) {
            for (String param : queryString.split(PARAM_SEPARATOR)) {
                String pair[] = param.split(PAIR_SEPARATOR);
                String key = OAuthEncoder.decode(pair[0]);
                String value = pair.length > 1 ? OAuthEncoder.decode(pair[1]) : EMPTY_STRING;
                params.add(new Parameter(key, value));
            }
        }
    }

    public boolean contains(Parameter param) {
        return params.contains(param);
    }

    public int size() {
        return params.size();
    }

    public ParametersList sort() {
        ParametersList sorted = new ParametersList(params);

        Collections.sort(sorted.params);
        return sorted;
    }
}

```

```java
public class Parameter implements Comparable<Parameter> {
    private final String key;
    private final String value;

    public Parameter(String key, String value) {
        this.key = key;
        this.value = value;
    }

    public String asUrlEncodedPair() {
        return OAuthEncoder.encode(key).concat("=").concat(OAuthEncoder.encode(value));
    }

    public boolean equals(Object other) {
        if(other == null) return false;
        if(other == this) return true;
        if(!(other instanceof Parameter)) return false;

        Parameter otherParam = (Parameter) other;
        return otherParam.key.equals(key) && otherParam.value.equals(value);
    }

    public int hashCode() {
        return key.hashCode() + value.hashCode();
    }

    public int compareTo(Parameter parameter) {
        int keyDiff = key.compareTo(parameter.key);

        return keyDiff != 0 ? keyDiff : value.compareTo(parameter.value);
    }
}

```

```java
import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.net.URLEncoder;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Pattern;


public class OAuthEncoder {
    private static String CHARSET = "UTF-8";
    private static final Map<String, String> ENCODING_RULES;

    static {
        Map<String, String> rules = new HashMap<String, String>();
        rules.put("*", "%2A");
        rules.put("+", "%20");
        rules.put("%7E", "~");
        ENCODING_RULES = Collections.unmodifiableMap(rules);
    }

    private OAuthEncoder(){}

    public static String encode(String plain) {
        String encoded = "";
        try {
            encoded = URLEncoder.encode(plain, CHARSET);
        }
        catch (UnsupportedEncodingException uee) {
            throw new OAuthException("Charset not found while encoding string: " + CHARSET, uee);
        }
        for(Map.Entry<String, String> rule : ENCODING_RULES.entrySet()) {
            encoded = applyRule(encoded, rule.getKey(), rule.getValue());
        }
        return encoded;
    }

    private static String applyRule(String encoded, String toReplace, String replacement) {
        return encoded.replaceAll(Pattern.quote(toReplace), replacement);
    }

    public static String decode(String encoded) {
        try {
            return URLDecoder.decode(encoded, CHARSET);
        }
        catch(UnsupportedEncodingException uee) {
            throw new OAuthException("Charset not found while decoding string: " + CHARSET, uee);
        }
    }
}


```

```java
public class OAuthConstants {
    private OAuthConstants(){}

    public static final String OUT_OF_BAND = "oob";
}
```

```java
public class OAuthException extends RuntimeException {

    /**
     * Constructeur par défaut
     * @param message message expliquant ce qui n'a pas fonctionné
     * @param e exception originale
     */
    public OAuthException(String message, Exception e) {
        super(message, e);
    }

    /**
     * Constructeur sans exception. Utilisé lorsqu'il n'y a pas d'exception originale
     *
     * @param message message expliquant ce qui n'a pas fonctionné
     */
    public OAuthException(String message) {
        super(message, null);
    }

    private static final long serialVersionUID = 1L;
}

```

Les valeurs collectées (paramètres _oauth_*_ + paramètres d'extension de l'API) doivent être jointes pour former une seule chaîne, à partir de laquelle la signature sera générée. Cela s'appelle la chaîne de base de signature dans la spécification OAuth. 

Pour encoder la méthode HTTP, l'URL de la requête et la chaîne de paramètres en une seule chaîne :

1. Définir la chaîne de sortie égale à la méthode HTTP en majuscules (GET dans cet exemple).
2. Ajouter le caractère `&` à la chaîne de sortie.
3. Encoder en pourcentage l'URL et l'ajouter à la chaîne de sortie.
4. Ajouter le caractère `&` à la chaîne de sortie
5. Encoder en pourcentage la chaîne de paramètres et l'ajouter à la chaîne de sortie.

La classe `HmacSha1SignatureService` génère la signature en utilisant la chaîne de base de signature et votre clé secrète de consommateur avec un caractère `&` avec l'algorithme de hachage HMAC-SHA1.

```java
import android.util.Base64;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;


public class HmacSha1SignatureService {
    private static final String EMPTY_STRING = "";
    private static final String CARRIAGE_RETURN = "\r\n";
    private static final String UTF8 = "UTF-8";
    private static final String HMAC_SHA1 = "HmacSHA1";
    private static final String METHOD = "HMAC-SHA1";

    public String getSignature(String baseString, String apiSecret, String tokenSecret) {
        try {
            return doSign(baseString, OAuthEncoder.encode(apiSecret) + '&' + OAuthEncoder.encode(tokenSecret));
        }
        catch (Exception e) {
            throw new OAuthSignatureException(baseString, e);
        }
    }

    private String doSign(String toSign, String keyString) throws Exception {

        SecretKeySpec key = new SecretKeySpec((keyString).getBytes(UTF8), HMAC_SHA1);
        Mac mac = Mac.getInstance(HMAC_SHA1);
        mac.init(key);
        byte[] bytes = mac.doFinal(toSign.getBytes(UTF8));
        return bytesToBase64String(bytes).replace(CARRIAGE_RETURN, EMPTY_STRING);
    }

    private String bytesToBase64String(byte[] bytes) {
        return Base64.encodeToString(bytes,Base64.NO_WRAP);
    }

    public String getSignatureMethod() {
        return METHOD;
    }
}
```

```java
/**
 * Exception spécialisée qui représente un problème dans la signature
  */
public class OAuthSignatureException extends OAuthException {
    private static final long serialVersionUID = 1L;
    private static final String MSG = "Error while signing string: %s";

    /**
     * Constructeur par défaut
     *
     * @param stringToSign chaîne simple qui est signée (HMAC-SHA, etc)
     * @param e exception originale
     */
    public OAuthSignatureException(String stringToSign, Exception e) {
        super(String.format(MSG, stringToSign), e);
    }

}

```

C'est tout ! Maintenant, vous pouvez vous connecter à n'importe quel site e-Commerce qui utilise le plugin Woocommerce sans installer d'autre plugin. En utilisant l'API REST de WordPress, vous pouvez obtenir/manipuler les données que vous voulez en utilisant ses points de terminaison d'API. Les points de terminaison que j'ai utilisés sont :

1. `/wp-json/wc/v2/customers` - vous permet de créer un nouveau client après l'avoir vérifié via l'écran de connexion/connexion de l'application.
2. `/wp-json/wc/v2/payment_gateways` - vous permet de récupérer et de voir toutes les passerelles de paiement disponibles
3. `/wp-json/wc/v2/products` - vous aide à voir tous les produits qui ont été vendus sur le site web
4. `/wp-json/wc/v2/shipping/zones` - vous aide à créer une nouvelle zone de livraison
5. `/wp-json/wc/v2/settings/general/woocommerce_currency` - obtient la devise utilisée
6. `/wp-json/wc/v2/orders` - vous aide à créer une nouvelle commande
7. `/wp-json/wc/v2/products/categories` - vous permet de récupérer toutes les catégories de produits
8. `/wp-json/wc/v2/coupons` - vous aide à lister tous les coupons qui ont été créés par l'administrateur du site web

Voici mon application mobile finale :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Woostroid_Optimized.gif)
_Mon produit final_

## Ressources qui rendent l'application belle

Pour finaliser la création de votre application mobile native, vous aurez besoin d'une interface utilisateur/expérience utilisateur avec laquelle l'utilisateur interagira pour manipuler les données obtenues du serveur WordPress. Heureusement, les gens de [Wsdesign](https://wsdesign.in/freebies/) ont des modèles gratuits et prêts à l'emploi que vous pouvez télécharger.

J'espère que vous avez trouvé cet article utile et qu'il vous a aidé à apprendre et à construire une application géniale aujourd'hui. Si vous l'avez vraiment aimé, n'hésitez pas à le partager sur toutes les plateformes de médias sociaux.