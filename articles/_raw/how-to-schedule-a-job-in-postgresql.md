---
title: How to Schedule a Job in PostgreSQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-12T14:04:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-schedule-a-job-in-postgresql
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-mat-brown-552598.jpg
tags:
- name: automation
  slug: automation
- name: database
  slug: database
- name: postgres
  slug: postgres
seo_title: null
seo_desc: 'By Jagruti Tiwari

  Scheduling allows you to automate things so you don''t have to do them in real time.

  In this article we will see how to schedule a job in PostgreSQL. We''ll use pgAgent,
  a job scheduling agent for PostgreSQL.

  How to Install PostgreSQL...'
---

By Jagruti Tiwari

Scheduling allows you to automate things so you don't have to do them in real time.

In this article we will see how to schedule a job in PostgreSQL. We'll use pgAgent, a job scheduling agent for PostgreSQL.
# How to Install PostgreSQL and Stack Builder
You can install pgAgent with Stack Builder.

Install PostreSQL from the [official website](https://www.postgresql.org/download/). This will download Stack Builder along with the installer.

If you have PostgreSQL already installed, you could download the installer and run Stack Builder if you don't have it already. 

Stack Builder runs once PostgreSQL installation is complete. I am using PostgreSQL14 and pgAdmin4. 

# How to Install pgAgent

When you run Stack Builder it will first open a welcome wizard.

![Screenshot-2022-07-10-163841_auto_x2_auto_x2_colored_toned_light_ai](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-163841_auto_x2_auto_x2_colored_toned_light_ai.jpg)

If you have multiple PostgreSQL versions installed you will pick one to use to install pgAgent.

![Screenshot-2022-07-10-163907_auto_x2_colored_toned_light_ai_auto_x2_colored_toned_light_ai](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-163907_auto_x2_colored_toned_light_ai_auto_x2_colored_toned_light_ai.jpg)

Under *Adds-ons, tools and utilities*, you will find pgAgent. Check the checkbox to install it.

![Screenshot-2022-07-10-163926_auto_x2_colored_toned_light_ai--1-_auto_x2_colored_toned_light_ai](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-163926_auto_x2_colored_toned_light_ai--1-_auto_x2_colored_toned_light_ai.jpg)

Next, it will ask you to choose a directory where you want to install pgAgent.

![Screenshot-2022-07-10-163956](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-163956.png)

Stack Builder will then open a pgAgent SetUp Wizard.

![Screenshot-2022-07-10-164018](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-164018.png)

Here you will pick whether you want to install it in an upgrade mode. If you do not want to automatically change scripts while upgrading you can check the box.

![Screenshot-2022-07-10-164038](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-164038.png)

In the *PostgreSQL installation details* wizard, provide the username and password that you entered when you installed PostgreSQL.

![Screenshot-2022-07-10-164125](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-164125.png)

If you enter incorrect details it will throw a connection error. So make sure you remember those details.

> **_NOTE:_** Login to PostgreSQL with the username and password you provided at this stage to view *pgAgent jobs*.

![Screenshot-2022-07-10-164233](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-164233.png)

After adding those details, the setup begins:

![Screenshot-2022-07-10-164250](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-164250.png)

It takes a couple of seconds to finish.

![Screenshot-2022-07-10-164304](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-164304.png)

Click the *finish* button at the end.

![Screenshot-2022-07-10-164320](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-164320.png)

Stack Builder will also display an *installation completed* wizard. It has instructions to install and uninstall utilites. 

Once Stack Builder is installed you simply run it to install other utilites. To uninstall them you need to use the Control Panel.

![Screenshot-2022-07-10-190229](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-190229.png)

*pgAgent jobs* will be visible to you in the browser tree on the left side of the dashboard. 

![Screenshot-2022-07-10-152307-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-152307-1.png)

Above you can see a close up view of the browser tree.
# How to Create a Job in pgAgent

To create a new job, right click on the *pgAgent Jobs* button and click on *create*. 

![Screenshot-2022-07-10-152329-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-152329-1.png)

You will see a menu, and there just click *create* > *pgAgent Job*.

![Screenshot-2022-07-10-191902](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-191902.png)

The *create pgAgent dialog box* has four tabs. 

The first one is *General* tab. Here you enter the name of the job and select a category. 

*Category* is just for internal categorization purposes – this does not affect how your job runs. You can select one based on the function of the job. Since I want to export the data to a CSV, I will pick the *Data Export* category.

![Screenshot-2022-07-10-152531-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-152531-1.png)

Next we click on the *Steps* tab in the *create pgAgent* dialog box. In the top right corner of the box you will see a + sign. Click on it to add a new row.

![Screenshot-2022-07-10-153345-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-153345-1.png)

The *Steps* tab has two sections: *General* and *Code*.

In the *General* tab: 

1) Add the name of the step.
2) Next, you *Enable* or *Disable* the step. Your job will run only if the step is enabled.
3) Depending on whether your job is *local* or *remote*, you can pick the *Connection type*. I will choose a remote connection.
4) A remote connection allows you to manually add the Connection String. The syntax should be like in [libq connection string](https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING). I will add my connection details in the same format: ```host=localhost port=5432 dbname=postgres```
5) In the *On Error* select box, you can pick what should be happen in case an error occurs. I have selected for the job to fail.
6) Finally, you  can comment on the step. Then save the changes.

Next comes the *code* section in *Steps* tab.
![Screenshot-2022-07-10-155158-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-155158-1.png)

Since I want to export the data from a view, I will call the view and ask it to export the file. The code will be:
```COPY (select * from acc_view) TO E'C:\\test-data\\try.csv';```

I will save the changes after adding the code.

![Screenshot-2022-07-10-153614-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-153614-1.png)

We are now ready to schedule a job. In the *Schedules* tab we add the *start date time* and the *end date time* for the job to start and end. 

![Screenshot-2022-07-10-163332-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-163332-1.png)

*SQL* is the last tab. It shows the code generated by the GUI. If you want to schedule a job dynamically you will have to execute the procedure code displayed here.

# How to View Created Jobs in pgAgent

Once a new job is created, it will be displayed under *pgAgent jobs* in the browser tree.

![Screenshot-2022-07-10-163417-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-163417-1.png)

Its *schedules* and *steps* will be displayed when you extend the job.

![Screenshot-2022-07-10-163540-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-163540-1.png)

To see whether the job was executed (whether it failed or succeeded), you select the job by its name and click on the *Statistics* tab in the dashboard. Here you can view the number of times the job was executed, start and end time, its status and id. *s* means success and *f* means failed in the *Status* column.

![Screenshot-2022-07-10-163639-1](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-163639-1.png)

To debug why a job failed, you can simply click on the name of the step under *Steps* in the browser tree and click *Statistics* on the dashboard. In the *output*  column you can see why the job failed. 

In my case it wasn't able to access the directory I was trying to copy the data to. Once I changed the path, my job was successfully executed (note the first row).

# How to Edit Jobs in pgAgent
To edit a job in pgAgent you select the job and click on the *Properties* tab on the dashboard.

![Screenshot-2022-07-10-201542](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-10-201542.png)

Click on the pencil icon in the top left corner, it will open a wizard where you can edit all the details. 
# Conclusion
It is not always feasible to create schedulers in your code, but when it's an option, it can be really helpful. 

Job Scheduling coupled with exporting data in CSV format is a powerful feature of PostgreSQL. I will try to explain how to create a job dynamically in the next tutorial. Happy learning.



