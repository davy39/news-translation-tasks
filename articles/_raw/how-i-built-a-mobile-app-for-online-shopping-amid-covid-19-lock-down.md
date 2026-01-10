---
title: How I Built a Mobile App for Online Shopping Amid the COVID-19 Lockdown
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
seo_title: null
seo_desc: 'By Ogbeta Ovokerie

  When many stores that sell nonessential items were ordered to close in March by
  government decrees, consumers moved their shopping online. U.S. online sales increased
  49% in April over the prior year, according to Adobe Analytics. ...'
---

By Ogbeta Ovokerie

When many stores that sell nonessential items were ordered to close in March by government decrees, consumers moved their shopping online. U.S. online sales increased 49% in April over the prior year, according to [Adobe Analytics](https://www.adobe.com/analytics/abobe-analytics.html). 

The increase in sales was not particularly significant on desktop. But mobile shopping apps such as Instacart [saw an increase of about 650% (wow!)](https://www.visualcapitalist.com/covid-19-impact-on-popularity/) in new mobile app users (in the U.S alone) between March and April. 

So, in order for e-Commerce stores to take full advantage of the increase in online shoppers during the Coronavirus pandemic, they should have a native mobile app. 

In this tutorial, I will be developing a native mobile Android app using the Woocommerce theme. I will also explain why I went for a native mobile app (instead of a hybrid app or a progressive web app) and the Woocommerce theme. Even better, I will start with some research data to show just how important it is for an e-Commerce store to have a mobile app.

## Traffic to brick-and-mortar stores has almost vanished

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Is-there-anybody-out-there.jpg)
_Is there anybody out there?_

Consumer surveys suggest that the shift to online shopping will continue as long as COVID-19 remains a threat. A [survey of 1,200 consumers in late March](https://www.rsrresearch.com/research) 2020 found that 90% of shoppers were hesitant to shop in stores because of the Coronavirus pandemic. And 45% expected online shopping would be a necessity for them during the crisis. 

A [separate survey in April](https://bizrateinsights.com/) found that 55% of online consumers said they were ordering more online than they were before the virus hit, up from 26% in March. And 22% said in April they were ordering a lot more online, as opposed to only 6% in March. 

If the pandemic continues to linger, there could be a big shift to online shopping during retailers’ two biggest seasons of the year – back-to-school and holiday shopping. 23% of retailers [surveyed in March](https://go.forrester.com/research/) planned to shift resources as a result of the Coronavirus outbreak.

Retail has been forced to make some major changes. As all non-essential businesses were urged to shut down, and foot traffic into brick-and-mortar retail stores [all but vanished](https://qz.com/1829531/covid-19-has-caused-us-retail-traffic-to-almost-entirely-vanish/). Even with staggered re-openings, the importance of having e-Commerce functionality is clearer than ever. 

The pandemic proved the need for businesses of all types to be flexible and ready for anything, and the need for them to take the digital leap. e-Commerce will be front and center for the new normal.

## But my client has a responsive website!

A number of trends are converging that make website owners want a native mobile app. The main goal of every website owner is to add value to the business by reaching more users. I think it will come as no surprise that mobile phone usage is on the rise and more people interact with their mobile phones than with desktops. 

In order to tap into this market of mobile phone users, we need to know which types of apps these mobile phone users interact with the most (progressive web apps, hybrid apps, responsive mobile websites, or native apps). Luckily for us the people at [Go-Globe](https://www.go-globe.com/mobile-apps-usage) did an analysis: a whopping 85% of mobile users interact with native mobile apps the most.

There are a number of other reasons why companies should have a native mobile app to meet the needs of the growing number of online shoppers amid the coronavirus pandemic. Let's explore them now a bit more.

### They offer a better experience to loyal website visitors

Mobile sites are great for discovery. But loyal users – those that come back more often – want to have an app. People use apps more than they use search on mobile devices. A brand (that is, an app) on a user’s home screen is a constant reminder of a site and its content.

### They connect directly with website visitors

A brand can be on all social channels, but only a fraction of users will ever see its message. Emails can also be sent, but with a 25% open rate, only a fraction of the audience will be reached.

A branded mobile app gives a direct line to users, ultimately retaining users and turning casual visitors into loyal users.

### They make use of mobile device features

Native mobile apps have the advantage of utilizing features of a mobile phone like the camera, contact list, GPS, phone calls, accelerometer, compass, and etc. Such device features, when used within an app, can make the user experience interactive and fun. 

Moreover, these features can also reduce the efforts users would have to make otherwise. For instance, users that would like to know the location of a business can use the GPS/navigation to easily find it (especially useful in food apps). 

These features can also significantly shorten the time users take to perform a certain task in an app, and can even boost conversions. 

Mobile websites, PWAs, and hybrid apps can also use some of the device's features. Still, there are technological constraints or limits in utilizing all the features of a device which native mobile apps can use easily.

### They give you the ability to work offline

This is probably the most fundamental difference between a mobile website and an app. Although native mobile apps might require internet connectivity to perform most of their tasks, they can still offer basic content and functionality to users in offline mode. 

Let’s take the example of an e-Commerce website – the app can provide features like tax and installment calculation, and determine a user's spending limit. These features can work even without the help of an internet connection.

Even though mobile websites, PWAs, and hybrid mobile apps can use caching to load web pages without an internet connection, they can only offer limited functions.

### They help increase brand presence

Users spend a substantial amount of their time on mobile devices. It’s safe to say that many users see the apps they’ve installed on their devices almost every day.

This regular encounter can be viewed as a branding opportunity for the apps. Even when users are not actively using a mobile app, they are still reminded of the brand associated with the app. The app's icon acts like a mini-advertisement for the brand.  


The presence of an app on a user’s device helps influence their perception about a brand subconsciously. This behavior can be linked to the Signal Detection Theory, which suggests that users still process ads they’ve ignored at some level subconsciously.

### Apps can work faster than websites

A well-designed mobile app can perform actions much quicker than a mobile website.  
Apps usually store their data locally on mobile devices, in contrast to websites that generally use web servers. For this reason, data retrieval happens swiftly in mobile apps. 

Apps can further save users’ time by storing their preferences and using them to take proactive actions on their behalf.

There is also a technical justification as to why mobile apps can work faster. Mobile websites use JavaScript code to perform most of their functions. And some of the frameworks that mobile apps use can run almost five times faster than JavaScript! 

While all this is happening in the background, users get to complete actions more quickly on the front end of mobile apps, again contributing to a delightful user experience.

### They increase SEO potential for a website

Mobile apps can be advantageous in two ways – for in-app content and website content as synonymous words will be used in the content for products and services. Google these days rank in-app content too and you can modify your content in your application to help you with your website SEO.

### Mobile app spending is expected to double by 2024, despite the economic impacts of COVID-19

[According to a revised 2020-2024 market forecast](https://sensortower.com/blog/sensor-tower-app-market-forecast-2024), worldwide consumer spending in mobile apps is projected to reach $171 billion by 2024. This is more than double the $85 billion from 2019. 

This total, however, is about $3 billion (or 2%) less than the forecast the firm had released prior to the COVID-19 outbreak.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/mobile-app-spending.png)
_Mobile App Spending_

Still, it's notable that even the slowest-growing regions on both Apple's App Store and Google Play will see revenue that's over 80% higher than their 2019 levels by the year 2024. The app stores will also hit several milestones during the next five years. 

For starters, global spending in mobile apps will surpass $100 billion for the first time in 2020, growing at approximately 20% year-over-year to hit $102 billion. This indicates that website owners do not just get more customers, but more paying customers that are willing to spend.

### They reach out to a younger audience

The stats indicate that 18-24 years olds are the most active mobile app users.

Still not convinced? Let these statistics do the talking:

1. 77% of Americans own a smartphone.
2. Over 230 million U.S. consumers own smartphones.
3. Around 100 million U.S. consumers own tablets.
4. 79% of smartphone users have made a purchase online using their mobile device in the last 6 months.
5. e-Commerce dollars now comprise 10% of _all_ retail revenue.
6. 80% of shoppers used a mobile phone inside of a physical store to either look up product reviews, compare prices, or find alternative store locations.
7. An estimated 10 billion mobile connected devices are currently in use.
8. Mobile app users spend an average 201.8 minutes per month shopping, compared to 10.9 minutes/month for website users.
9. 58% of millennials mentioned that they preferred purchasing through apps.

Ignoring these trends in mobile e-Commerce (referred to as m-Commerce in the industry) evolution means potentially missing out on more and more profit as these trends continue.

## Enough talk! Let’s write some code

All native mobile apps are just a bundle of code written in Java, Kotlin, Objective-C, or Swift that manipulate data and resources (.png, .xml files). The manipulated data can be retrieved from the mobile device’s sensors such as the screen, camera, storage memory, GPS, speakers, accelerometer, compass, or from a server. 

In this tutorial we will be using the following tools:

* **JSoup (a** J**ava library):** JSoup is an HTML parser which can directly parse a URL, HTML text content, and provides a set of very convenient API interfaces to manipulate data.
* **Android Studio:** This is the official tool for writing and compiling Android apps in Java or Kotlin and produces ready to install .apk files. All code in this tutorial will be written in Java.
* **Woocommerce Plugin:** This [is the most popular e-Commerce plugin for WordPress](https://trends.builtwith.com/shop/WooCommerce). So building a mobile app for the most popular e-Commerce plugin seems like a good idea.

## Getting and Manipulating Data from the Server

Data will be gotten from the server using a [RESTful API](https://medium.com/extend/what-is-rest-a-simple-explanation-for-beginners-part-1-introduction-b4a072f8740f). WooCommerce (version 2.6+) is fully integrated with the WordPress REST API. This allows data to be created, read, updated, and deleted using requests in JSON format. It uses WordPress REST API Authentication methods and standard HTTP verbs which are understood by most HTTP clients. 

I will be using the API version 2, v2 which is available for Woocommerce version 3.0.x or later and WordPress version 4.4 or later.

The default response format is JSON. Successful requests will return a `200 OK` HTTP status. Some key information about responses are:

* Dates are returned in ISO8601 format: `YYYY-MM-DDTHH:MM:SS`
* Resource IDs are returned as integers.
* Any decimal monetary amount, such as prices or totals, will be returned as strings with two decimal places.
* Other amounts, such as item counts, are returned as integers.
* Blank fields are generally included as `null` or empty string instead of being omitted.

Most requests made to the Woocommerce REST API have to be authenticated using pre-generated keys (consumer key and consumer secret). New keys are generated through the WordPress admin interface. Just go to WooCommerce > Settings > API > Keys/Apps.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/woocommerce-api-keys-settings.png)

Click the "Add Key" button. In the next screen, add a description and select the WordPress user you would like to generate the key for. Then click the "Generate API Key" button and WooCommerce will generate REST API keys for the selected user.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/woocommerce-creating-api-keys.png)

Now that keys have been generated, you should see two new keys. These two keys are your Consumer Key and Consumer Secret.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/woocommerce-api-key-generated.png)

We then create a URL which will include the business website and the API endpoint from which the data in JSON format will be returned. 

Using the Jsoup library, we connect to the URL (website + API endpoint) and add the API keys (consumer key and consumer secret) with other parameters of the API endpoint. Almost all endpoints accept optional parameters which can be passed as a HTTP query string parameter:

```java
public static final int JSOUP_CONNECTION_TIMEOUT = 100000;

String websiteUrl = "www.freecodecamp.shop"; //example website doesn't exist
//This API lets you retrieve all product categories
String apiExtension = "/wp-json/wc/v2/products/categories";
//Map to store our parameters in a key value format
HashMap<String, String> data = new HashMap<>();
data.put("page", String.valueOf(page)); // API parameter to get the current page of the collection. Default is 1.
//add API keys for authentication
data.put("consumer_key", getKey());
data.put("consumer_secret", getSecret());

//concatenate both websiteUrl and apiExtension to form the requestUrl
String requestUrl = websiteUrl + apiExtension

try {
    Connection.Response response = Jsoup.connect(requestUrl).timeout(JSOUP_CONNECTION_TIMEOUT).followRedirects(true)
        .ignoreContentType(true)
        .data(data)
        .execute();
		
    String json = response.body();
	//parse json string to get needed data.

} catch (Exception e){
    //catch both JSONException and IOException
}
```

The  `getKey()` and `getSecret()` methods just return the API keys:

```java

    public static String getKey() {
        return "ck_a89d59d7441f027df0d91f01c9e2dcaxxxxxxxxx";
    }

    public static String getSecret() {
        return "cs_c3f8fe620bd5b1cb3567712eb843609xxxxxxxxx";
    }
```

But wait...for some websites, when I run this code it gives me the error `401 Unauthorized`. This is an authentication or permission error, due to incorrect API keys...so what gives?

Sure, the above code only works for secured websites with the HTTPS protocol, whereas unsecured websites which use the HTTP protocol will need to encrypt the API keys before sending them. 

What does that mean, exactly? HTTPS is HTTP with encryption, as HTTPS uses TLS (SSL) to encrypt normal HTTP requests and responses. This makes HTTPS far more secure than HTTP. A website that uses HTTP has http:// in its URL, while a website that uses HTTPS has https://.

You must use OAuth 1.0a "one-legged" authentication to ensure your REST API credentials cannot be intercepted by an attacker. The required parameters are _oauth_consumer_key, oauth_timestamp, oauth_nonce, oauth_signature_ and _oauth_signature_method._

We will create a method that will get these encrypted parameters as a HashMap. The method, `getAuthenticationPrams(String url, HashMap<String, String> mData)` will accept a request URL (website URL + API extension) and any parameters that we might want to add to the API extension. 

Here we collect and normalize our parameters, which includes all _oauth_*_ parameters except for the _oauth_signature_ itself.

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

The `TimestampService` class generates a timestamp and nonce for the _oauth_nonce_ and _oauth_timestamp_ parameters.

```java
import java.util.Random;

public class TimestampService {
    private Timer timer;

    /**
     * Default constructor.
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
     * Inner class that uses {@link System} for generating the timestamps.
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

The  `formatQuery(HashMap<String, String> mData)` method formats the parameters into query parameters which are a set of parameters attached to the end of a url. The `urlEncoded(String url)` method translates the given string into an application/x-www-form-urlencoded format using a specific encoding scheme. This method uses the supplied encoding scheme to obtain the bytes for unsafe characters.

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

The `ParametersList` class takes the formatted query and then encodes it using the `OAuthEncoder` class. The values that start with _oauth_*_ need to be encoded into a string which will be used later on. The process to build the string is very specific:

1. Percent encode every key and value that will be signed.
2. Sort the list of parameters alphabetically by encoded key.
3. For each key/value pair: 

* Append the encoded key to the output string
* Append the `=` character to the output string
* Append the encoded value to the output string
* If there are more key/value pairs remaining, append an `&` character to the output string.

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
     * Default constructor
     * @param message message explaining what went wrong
     * @param e original exception
     */
    public OAuthException(String message, Exception e) {
        super(message, e);
    }

    /**
     * No-exception constructor. Used when there is no original exception
     *
     * @param message message explaining what went wrong
     */
    public OAuthException(String message) {
        super(message, null);
    }

    private static final long serialVersionUID = 1L;
}

```

The collected values (_oauth_*_ parameters + API extension parameters) must be joined to make a single string, from which the signature will be generated. This is called the signature base string in the OAuth specification. 

To encode the HTTP method, request URL, and parameter string into a single string:

1. Set the output string equal to the uppercase HTTP Method (GET in this example).
2. Append the `&` character to the output string.
3. Percent encode the URL and append it to the output string.
4. Append the `&` character to the output string
5. Percent encode the parameter strng and append it to the output string.

The `HmacSha1SignatureService` class generates the signature using the signature base string and your consumer secret key with an `&` character with the HMAC-SHA1 hashing algorithm.

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
 * Specialized exception that represents a problem in the signature
  */
public class OAuthSignatureException extends OAuthException {
    private static final long serialVersionUID = 1L;
    private static final String MSG = "Error while signing string: %s";

    /**
     * Default constructor
     *
     * @param stringToSign plain string that gets signed (HMAC-SHA, etc)
     * @param e original exception
     */
    public OAuthSignatureException(String stringToSign, Exception e) {
        super(String.format(MSG, stringToSign), e);
    }

}

```

That's it! Now you can connect to any e-Commerce website that uses the Woocommerce plugin without installing any other plugin. Using the WordPress REST API you can get/manipulate the data you want using its API endpoints. The endpoints I used are:

1. `/wp-json/wc/v2/customers` - lets you create a new customer after you have verified them through the signin/login screen of the app.
2. `/wp-json/wc/v2/payment_gateways` - lets you retrieve and view all the available payment gateways
3. `/wp-json/wc/v2/products` - helps you view all the products that have been sold on the website
4. `/wp-json/wc/v2/shipping/zones` - helps you create a new shipping zone
5. `/wp-json/wc/v2/settings/general/woocommerce_currency` - gets the currency used
6. `/wp-json/wc/v2/orders` - helps you create a new order
7. `/wp-json/wc/v2/products/categories` - lets you retrieve all product categories
8. `/wp-json/wc/v2/coupons` - helps you list all the coupons that have been created by the website administrator

Here's my final mobile app:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Woostroid_Optimized.gif)
_My Final Product_

## Resources that Makes the App Look Pretty

In finalizing your native mobile app creation, you will need a UI/UX which the user will interact with to manipulate the data gotten from the WordPress server. Luckily, the people at [Wsdesign](https://wsdesign.in/freebies/) have some free and ready to use templates that you can download.

I hope that you found this article useful and it was able to help you learn and build an awesome app today. If you really liked it, please do share it on all social media platforms.

