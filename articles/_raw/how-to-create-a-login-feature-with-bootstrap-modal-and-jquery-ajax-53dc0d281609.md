---
title: How to create a login feature with Bootstrap Modal and jQuery AJAX
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-03T21:44:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-login-feature-with-bootstrap-modal-and-jquery-ajax-53dc0d281609
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QQsDn3sXpsL06kzzS7a_oA.jpeg
tags:
- name: Bootstrap
  slug: bootstrap
- name: coding
  slug: coding
- name: jQuery
  slug: jquery
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Yogi

  Bootstrap Modal is an excellent way to create a Login form on your website. In this
  tutorial, you will learn how to create a login feature using Bootstrap for an ASP.NET
  website. The login Check feature will be created using jQuery AJAX.

  I wi...'
---

By Yogi

**Bootstrap Modal** is an excellent way to create a **Login form** on your website. In this tutorial, you will learn how to create a login feature using Bootstrap for an ASP.NET website. The login Check feature will be created using jQuery AJAX.

**I will create the following features Step by Step:**

1. A Bootstrap Modal that will contain a login form.

2. The Login Form will contain 2 fields, ‘Username’ & ‘Password’. The user has to enter their values in these fields.

3. On clicking the submit button on the form, the user’s input (username and password) will be sent to the C# function.

4. This C# function will check whether the username and password are correct or not.

5. If they are correct then the user is redirected to the profile page.

#### [You can check out the working DEMO here](http://www.demo.yogihosting.com/e/bootstrap-modal-login-form/).

#### **Creating a Bootstrap Modal with a Login Form**

Add the reference of “bootstrap CSS, jQuery and bootstrap js” files on the page head.

```
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
```

```
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
```

```
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
```

Next Create a Bootstrap Modal that contains the login form:

```
<div class="container"><div class="validCredential">
```

```
<h3>Try any one of the following three:</h3><div><p>  1. Username: Ram</p><p>  Password: admin</p></div>
```

```
<div><p>  2. Username: Shiv</p><p>  Password: admin</p></div>
```

```
<div><p>  3. Username: Krishna</p>
```

```
<p>  Password: admin</p></div>
```

```
</div>
```

```
<!-- The button that triggers the Modal --><button type="button" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal">Open Modal</button>
```

```
<!-- Bootstrap Modal --><div id="myModal" class="modal fade" role="dialog">  <div class="modal-dialog">
```

```
    <!-- Modal content-->    <div class="modal-content">      <div class="modal-header">        <button type="button" class="close" data-dismiss="modal">×</button>        <h4 class="modal-title">Log in with your Username</h4>      </div>
```

```
      <div class="modal-body">        <table>          <tbody>            <tr>              <td>                <input type="text" id="userNameTextBox" placeholder="Username" />              </td>            </tr>            <tr>              <td>                <span id="userNamSpan"></span>              </td>            </tr>            <tr>              <td>                <input type="text" id="passwordTextBox" placeholder="Password" />              </td>            </tr>            <tr>              <td>                <span id="passwordSpan"></span>              </td>            </tr>            <tr>              <td>                <input type="button" id="submitButton" value="Login" />              </td>            </tr>            <tr>              <td>                <span id="messageSpan"></span>              </td>            </tr>            <tr>              <td>                <img id="loadingImg" src="loading.gif" />              </td>            </tr>          </tbody>        </table>      </div>
```

```
    <div class="modal-footer">      <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>    </div>  </div><!-- END Modal content--></div>
```

```
</div>
```

```
<!-- END Bootstrap Modal --></div>
```

This is how the bootstrap modal login form will look.

![Image](https://cdn-media-1.freecodecamp.org/images/DNem9yh40WOT2fNUPM33t9YynO7yWzqoiFsC)
_**Bootstrap Modal Login Form**_

#### **Adding the jQuery Code on the button click event**

In the button click, I will force users to enter some value to the username and password fields, before they submit the form.

When both the textboxes contain some value, only then I will be calling the C# function using the [jQuery AJAX method](http://www.yogihosting.com/jquery-ajax/). With this method, I will be able to pass the values of the 2 text boxes (username and password) to my C# function.

Add the below jQuery code to your page:

```
$("#submitButton").click(function (e) {
```

```
if ($("#userNameTextBox").val() == "")
```

```
$("#userNamSpan").text("Enter Username");
```

```
else
```

```
$("#userNamSpan").text("");
```

```
if ($("#passwordTextBox").val() == "")
```

```
$("#passwordSpan").text("Enter Password");
```

```
else
```

```
$("#passwordSpan").text("");
```

```
if (($("#userNameTextBox").val() != "") && ($("#passwordTextBox").val() != ""))
```

```
$.ajax({  type: "POST",  url: "index.aspx/login",  contentType: "application/json; charset=utf-8",  data: '{"username":"' + $("#userNameTextBox").val() + '","password":"' + $("#passwordTextBox").val() + '"}',  dataType: "json",  success: function (result, status, xhr) {    if (result.d == "Success") {      $("#messageSpan").text("Login Successful, Redireting to your profile page.");      setTimeout(function () { window.location = "profile.aspx"; }, 2000);    }    else      $("#messageSpan").text("Login failed, Please try again.");    },   error: function (xhr, status, error) {     $("#dbData").html("Result: " + status + " " + error + " " + xhr.status + " " + xhr.statusText)   }});
```

```
});
```

```
$(document).ajaxStart(function () {  $("#loadingImg").show();});
```

```
$(document).ajaxStop(function () {  $("#loadingImg").hide();});
```

In the success callback method, you can see that I am redirecting the user to the **profile.aspx** page if-and-only-if I receive the “**Success**” message.

The **setTimeout()** is a JavaScript function that will redirect to the profile page in 2 seconds.

**The following 2 images will explain the login feature:**

> _1. When login fails._

![Image](https://cdn-media-1.freecodecamp.org/images/pEzx51hKTGLE3OTi76TdDiLQQKCiHN4VS8EZ)
_**Login Failed for wrong Username and Password**_

> _2. When login is successful._

![Image](https://cdn-media-1.freecodecamp.org/images/bttqLY1d9BT7-UNRPN-lrYCIxgXHCqVmVV0H)
_**Login Successful when Username and Password are correct**_

#### **The C# code:**

Now in your **.aspx.cs** page, add the following code:

```
[System.Web.Services.WebMethod]
```

```
public static string login(string username, string password)
```

```
{
```

```
var cred = LoadCredential();
```

```
var count = (from t in cred
```

```
where t.username == username && t.password == password
```

```
select t).Count();
```

```
if (count == 1)
```

```
{
```

```
HttpContext.Current.Session["User"] = username;
```

```
return "Success";
```

```
}
```

```
else
```

```
return "Failed";
```

```
}
```

```
class Credential
```

```
{
```

```
public string username { get; set; }
```

```
public string password { get; set; }
```

```
}
```

```
static List<Credential> LoadCredential()
```

```
{
```

```
List<Credential> credList = new List<Credential>();
```

```
Credential cred = new Credential();
```

```
cred.username = "Ram";
```

```
cred.password = "admin";
```

```
credList.Add(cred);
```

```
cred = new Credential();
```

```
cred.username = "Shiv";
```

```
cred.password = "admin";
```

```
credList.Add(cred);
```

```
cred = new Credential();
```

```
cred.username = "Krishna";
```

```
cred.password = "admin";
```

```
credList.Add(cred);
```

```
return credList;
```

```
}
```

The login() function is the one that is called by the **jQuery** method. It checks if the _username and passwords are correct_ and then returns the appropriate message.

#### **CSS**

To style the login form and the bootstrap modal so that they look perfect, add the following CSS to your page:

```
.btn {
```

```
margin: 15px 0;
```

```
}
```

```
#loadingImg {
```

```
display: none;
```

```
position: absolute;
```

```
margin: auto;
```

```
top: 0;
```

```
left: 0;
```

```
right: 0;
```

```
bottom: 0;
```

```
}
```

```
.validCredential h3 {
```

```
float: left;
```

```
text-decoration: underline;
```

```
}
```

```
.validCredential div {
```

```
clear: both;
```

```
}
```

```
.validCredential p {
```

```
float: left;
```

```
padding-right: 10px;
```

```
}
```

```
::-webkit-input-placeholder {
```

```
color: #ccc;
```

```
}
```

```
#myModal {
```

```
color: #1fa67b;
```

```
}
```

```
#myModal table {
```

```
position: relative;
```

```
margin: auto;
```

```
}
```

```
#myModal table input {
```

```
border-radius: 5px;
```

```
border: solid 1px #CCC;
```

```
margin: 10px;
```

```
padding: 3px 10px;
```

```
color: #000;
```

```
}
```

```
#myModal table input[type="button"] {
```

```
width: 94%;
```

```
background: #1fa67b;
```

```
color: #FFF;
```

```
}
```

```
#myModal table span {
```

```
float: left;
```

```
font-size: 12px;
```

```
color: #f00;
```

```
padding-left: 23px;
```

```
}
```

#### **Profile Page**

![Image](https://cdn-media-1.freecodecamp.org/images/DnAL6MlCl08x4PU4NDj9YKcfGhsYAoJnnsra)
_**Welcome Message on the Profile Page**_

On the profile page, the user will get the welcome message. The code of the profile page is the following:

```
<h1 id="welcomeMessage" runat="server"></h1>
```

```
if (!IsPostBack){  welcomeMessage.InnerHtml = "Welcome " + Session["User"] + " to the profile page.";}
```

> **_Check out the working demo by clicking the below link:_**

#### [Working DEMO](http://www.demo.yogihosting.com/e/bootstrap-modal-login-form/)

### **Conclusion**

I hope you liked this tutorial. Feel free to contact me for any questions. I will be there to help if you need it. If you liked this tutorial, then kindly share it on your social accounts.

**I have also published another tutorial on freeCodeCamp, you would like to see it too — [Master the art of looping in JavaScript with these incredible tricks](https://medium.freecodecamp.org/master-the-art-of-looping-in-javascript-with-these-incredible-tricks-a5da1aa1d6c5)**

