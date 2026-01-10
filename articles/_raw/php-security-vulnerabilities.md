---
title: 'PHP Security Vulnerabilities: Session Hijacking, Cross-Site Scripting, SQL
  Injection, and How to Fix Them'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T19:30:00.000Z'
originalURL: https://freecodecamp.org/news/php-security-vulnerabilities
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d68740569d1a4ca3799.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: PHP
  slug: php
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Security in PHP

  When writing PHP code it is very important to keep the following security vulnerabilities
  in mind to avoid writing insecure code.

  Types Of Vulnerabilities

  These are the common vulnerabilities you''ll encounter when writing PHP code. We...'
---

## **Security in PHP**

When writing PHP code it is very important to keep the following security vulnerabilities in mind to avoid writing insecure code.

### **Types Of Vulnerabilities**

These are the common vulnerabilities you'll encounter when writing PHP code. We'll discuss a few in further depth below.

* [Cross Site Request Forgery](https://guide.freecodecamp.org/php/security/cross-site-request-forgery) A vulnerability in the application caused by the programmer not checking where a request was sent from - this attack is sent to a high privilege level user to gain higher level access to the application.
* [Cross Site Scripting](https://guide.freecodecamp.org/php/security/cross-site-scripting) A vulnerability in the application caused by the programmer not sanitizing input before outputting the input to the browser (for example a comment on a blog). It is commonly used to run malicious javascript in the browser to do attacks such as stealing session cookies among other malicious actions to gain higher level privileges in the application.
* [Local File Inclusion](https://guide.freecodecamp.org/php/security/local-file-inclusion) A vulnerability in the application caused by the programmer requiring a file input provided by the user and not sanitizing the input before accessing the requested file. This results in a file being included where it should not of been.
* [Remote File Inclusion](https://guide.freecodecamp.org/php/security/remote-file-inclusion) A vulnerability in the application caused by the programmer requiring a file input provided by the user and not sanitizing the input before accessing the requested file. This results in a file being pulled from a remote server and included where it should not of been.
* [Session Hijacking](https://guide.freecodecamp.org/php/security/session-hijacking) A vulnerability caused by an attacker gaining access to a user’s session identifier and being able to use another user’s account impersonating them. This is often used to gain access to an administrative user’s account.
* [Session Identifier Acquirement](https://guide.freecodecamp.org/php/security/session-identifier-acquirement) Session Identifier Acquirement is a vulnerability caused by an attacker being able to either guess the session identifier of a user or exploit vulnerabilities in the application itself or the user’s browser to obtain a session identifier.
* [SQL Injection](https://guide.freecodecamp.org/php/security/sql-injection) A vulnerability in the application caused by the programmer not sanitizing input before including it into a query into the database. This leads to the attacker having full read and more often than not write access to the database. With this type of access an attacker can do very bad things.

Now let's look at some common vulnerabilities in more detail.

## **Session Hijacking**

Session Hijacking is a vulnerability caused by an attacker gaining access to a user’s session identifier and being able to use another user’s account impersonating them. This is often used to gain access to an administrative user’s account.

### **Defending against Session Hijacking attacks in PHP**

To defend against Session Hijacking attacks you need to check the current user’s browser and location information against information stored about the session. Below is an example implementation that can help mitigate the effects of a session hijacking attack. It checks the IP Address, User Agent, and if the Session Expired removing a session before it’s resumed.

```php
<?php
session_start();

// Does IP Address match?
if ($_SERVER['REMOTE_ADDR'] != $_SESSION['ipaddress'])
{
session_unset();
session_destroy();
}

// Does user agent match?
if ($_SERVER['HTTP_USER_AGENT'] != $_SESSION['useragent'])
{
  session_unset();
  session_destroy();
}

// Is the last access over an hour ago?
if (time() > ($_SESSION['lastaccess'] + 3600))
{
  session_unset();
  session_destroy();
}
else
{
  $_SESSION['lastaccess'] = time();
}
```

## **Cross Site Scripting**

Cross Site Scripting is a type of vulnerability in a web application caused by the programmer not sanitizing input before outputting the input to the web browser (for example a comment on a blog). It is commonly used to run malicious javascript in the web browser to do attacks such as stealing session cookies among other malicious actions to gain higher level privileges in the web application.

### **Example Cross Site Scripting Attack**

A blog allows users to style their comments with HTML tags, however the script powering the blog does not strip out `<script>` tags allowing any user to run javascript on the page. An attacker can use this to their advantage to run malicious javascript in the browser. They could infect users with malware, steal session cookies, and more.

```html
<script>
  alert('Cross Site Scripting!');
</script>
```

### **Defending your website from cross site scripting attacks in PHP**

In PHP there are two primary functions, `htmlspecialchars()` and `strip_tags()`, built in to protect yourself from cross site scripting attacks.

The `htmlspecialchars($string)` function will prevent an HTML string from rendering as HTML and display it as plain text to the web browser. **htmlspecialchars() code example**

```php
<?php
$usercomment = "<string>alert('Cross Site Scripting!');</script>";
echo htmlspecialchars($usercomment);
```

The other approach is the `strip_tags($string, $allowedtags)` function which removes all HTML tags except for the HTML tags that you’ve whitelisted. It’s important to note that with the `strip_tags()` function you have to be more careful, this function does not prevent the user from including javascript as a link, you’ll have to sanitize that on our own.

**strip_tags() code example**

```php
<?php
$usercomment = "<string>alert('Cross Site Scripting!');</script>";
$allowedtags = "<p><a><h1><h2><h3>";
echo strip_tags($usercomment, $allowedtags);
```

**Setting the X-XSS-Protection Header:**

In PHP you can send the `X-XSS-Protection` Header which will tell browsers to check for a reflected Cross Site Scripting attack and block the page from loading. This does not prevent all cross site scripting attacks only reflected ones and should be used in combination with other methods.

```php
<?php
header("X-XSS-Protection: 1; mode=block");
```

**Writing your own sanitization function** Another option, if you would like more control over how the sanitization works, is to write your own HTML Sanitization function, this is not recommended for PHP Beginners as a mistake would make your website vulnerable.

### **Defending your website from cross site scripting attacks with a Content Security Policy**

An effective approach to preventing cross site scripting attacks, which may require a lot of adjustments to your web application’s design and code base, is to use a content security policy.

#### **Set a Content Security Policy as an HTTP Header**

The most common way of setting a Content Security Policy is by setting it directly in the HTTP Header. This can be done by the web server by editing it’s configuration or by sending it through PHP.

**Example of a Content Security Policy set in a HTTP Header**

```php
<?php
header("content-security-policy: default-src 'self'; img-src https://*; child-src 'none';");
```

#### **Set a Content Security Policy as a Meta tags**

You can include your Content Security Policy in the page’s HTML and set on a page by page basis. This method requires you to set on every page or you lose the benefit of the policy.

**Example of a Content Security Policy set in a HTML Meta Tag**

```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src https://*; child-s
```

## **SQL Injection**

SQL injection is a vulnerability in the application caused by the programmer not sanitizing input before including it into a query into the database. This leads to the attacker having full read and more often than not write access to the database. With this type of access an attacker can do very bad things.

### **Example SQL Injection attack**

The below PHP Script runs an SQL Statement to get a user’s email by ID. However the input is not sanitized making it vulnerable to SQL Injection

```php
<?php
$input = $_GET['id'];
$dbserver = "localhost";
$dbuser = "camper";
$dbpass = "supersecretcampsitepassword";
$dbname = "freecodecamp";

$conn = new mysqli($dbserver, $dbuser, $dbpass, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT email FROM users WHERE id =" . $input;

$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo $row["email"];
    }
} else {
    echo "no results";
}

$conn->close();
```

```sql
SELECT email FROM users WHERE id = `$input`;
```

So with the above the input is not type casted (I.e. casting the input with (int) so only a number is allowed) nor escaped allowing someone to perform an SQL Injection attack - for example the URL `getemailbyuserid.php?id=1'; My Query Here-- -` would allow you to run arbitrary SQL queries with little effort.

### **Defending your website from sql injection attacks in PHP**

There are a few approaches to defend your website from SQL Injection Attacks. These approaches are Whitelisting, Type Casting, and Character Escaping

**Whitelisting:** The whitelisting approach is used in cases where only a few inputs are expected. You can list each expected input in a PHP Switch and then have a default for invalid input. You do not have to worry about a type casting issue or a character escape bypass but the allowed input is extreamly limited. It remains an option, see the example below.

```php
<?php
switch ($input) {
  case "1":
    //db query 1
    break;
  case "2":
    //db query 2
    break;
  default:
    // invalid input return error
}
```

**Type Casting:** The type casting approach is commonly used for an application using numeric input. Simply cast the input with `(int) $input` and only a numeric value will be allowed.

**Character Escaping:** The character escaping approach will escape characters such as quotes and slashes provided by the user to prevent an attack. If you are using MySQL Server and the MySQLi library to access your database, the `mysqli_real_escape_string($conn, $string)` function will take two arguments, the MySQLi connection, and the string and will properly escape the user’s input to block an sql injection attack. The exact function you use depends on the database type and php library you are using check the php library’s documentation for more information on escaping user input.

## More on PHP:

* [PHP best practices](https://www.freecodecamp.org/news/p/9a508d2b-fa35-4ac1-a15b-8bab8acc356d/)
* [Best PHP code examples](https://www.freecodecamp.org/news/the-best-php-examples/)
* [How to prevent a slow loris attack on a PHP server](https://www.freecodecamp.org/news/slow-loris-attack-using-javascript-on-php-server/)
* [How to set up a local debugging environment in PHP](https://www.freecodecamp.org/news/set-up-xdebug-phpstorm-in-php5-7-6a8386304fc6/)


