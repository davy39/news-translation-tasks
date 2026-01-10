---
title: An in-depth introduction to SQOOP architecture
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-26T17:53:46.000Z'
originalURL: https://freecodecamp.org/news/an-in-depth-introduction-to-sqoop-architecture-ad4ae0532583
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3aWPwVLlbZ8sq4aboE_CQw.png
tags:
- name: architecture
  slug: architecture
- name: big data
  slug: big-data
- name: Data Science
  slug: data-science
- name: hadoop
  slug: hadoop
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Jayvardhan Reddy

  Apache Sqoop is a data ingestion tool designed for efficiently transferring bulk
  data between Apache Hadoop and structured data-stores such as relational databases,
  and vice-versa.


  _Image Credits: [hdfstutorial.com](https://www.h...'
---

By Jayvardhan Reddy

**Apache Sqoop** is a data ingestion tool designed for efficiently transferring bulk data between Apache Hadoop and structured data-stores such as relational databases, and vice-versa.

![Image](https://cdn-media-1.freecodecamp.org/images/yA5Wt8JEHKyIDA-bK2ehlgYGN03XXPgKFmdz)
_Image Credits: [hdfstutorial.com](https://www.hdfstutorial.com/sqoop-architecture/" rel="noopener" target="_blank" title=")_

As part of this blog, I will be explaining how the architecture works on executing a Sqoop command. I’ll cover details such as the jar generation via Codegen, execution of MapReduce job, and the various stages involved in running a Sqoop import/export command.

### **Codegen**

Understanding Codegen is essential, as internally this converts our Sqoop job into a jar which consists of several Java classes such as POJO, ORM, and a class that implements DBWritable, extending SqoopRecord to read and write the data from relational databases to Hadoop & vice-versa.

You can create a Codegen explicitly as shown below to check the classes present as part of the jar.

```
sqoop codegen \   -- connect jdbc:mysql://ms.jayReddy.com:3306/retail_db \   -- username retail_user \   -- password ******* \   -- table products
```

The output jar will be written in your local file system. You will get a Jar file, Java file and java files which are compiled into .class files:

![Image](https://cdn-media-1.freecodecamp.org/images/9584V87MKrbpriG-qjgfkRmU95O4DqMWBMpw)

Let us see a snippet of the code that will be generated.

ORM class for table ‘products’ // Object-relational modal generated for mapping:

![Image](https://cdn-media-1.freecodecamp.org/images/R-YKp7vBHJyG0U9fkHmUrbDnie-O2-3G8PwV)

Setter & Getter methods to get values:

![Image](https://cdn-media-1.freecodecamp.org/images/do50-AIfmsBnWa0UmDElJu8lfJMl0lgATWtk)

Internally it uses JDBC prepared statements to write to Hadoop and ResultSet to read data from Hadoop.

![Image](https://cdn-media-1.freecodecamp.org/images/dp1Oud1aHWZ6zPFRmDhTf5p4KUuPrYIUg4K6)

### **Sqoop Import**

It is used to import data from traditional relational databases into Hadoop.

![Image](https://cdn-media-1.freecodecamp.org/images/1fuDCRMH99ZB3HA496qQycCcGQFzs7c6kdNl)
_Image Credits: [dummies.com](https://www.dummies.com/programming/big-data/hadoop/hadoop-for-dummies-cheat-sheet/" rel="noopener" target="_blank" title=")_

Let’s see a sample snippet for the same.

```
sqoop import \   -- connect jdbc:mysql://ms.jayReddy.com:3306/retail_db \   -- username retail_user \   -- password ******* \   -- table products \   -- warehouse-dir /user/jvanchir/sqoop_prac/import_table_dir \   -- delete-target-dir
```

The following steps take place internally during the execution of sqoop.

**Step 1**: Read data from MySQL in streaming fashion. It does various operations before writing the data into HDFS.

![Image](https://cdn-media-1.freecodecamp.org/images/FSvnl854UDyo8C9QKIOO0aMLNBw5uWed-KEJ)

As part of this process, it will first generate code (typical Map reduce code) which is nothing but Java code. Using this Java code it will try to import.

* Generate the code. (Hadoop MR)
* Compile the code and generate the Jar file.
* Submit the Jar file and perform the import operations

During the import, it has to make certain decisions as to how to divide the data into multiple threads so that Sqoop import can be scaled.

**Step 2**: Understand the structure of the data and perform CodeGen

![Image](https://cdn-media-1.freecodecamp.org/images/iw8VSQhwmd4uvmqwN0MxCG15xrFBPGyRZdXy)

Using the above SQL statement, it will fetch one record along with the column names. Using this information, it will extract the metadata information of the columns, datatype etc.

![Image](https://cdn-media-1.freecodecamp.org/images/rEfjXBnXyMjmyvtcIub-cxby3LS31vpFCFyt)
_Image Credits: [cs.tut.fi](http://www.cs.tut.fi/~aaltone3/kurssit/hadoop/Sqoop_pdf.pdf" rel="noopener" target="_blank" title=")_

**Step 3**: Create the java file, compile it and generate a jar file

As part of code generation, it needs to understand the structure of the data and it has to apply that object on the incoming data internally to make sure the data is correctly copied onto the target database. Each unique table has one Java file talking about the structure of data.

![Image](https://cdn-media-1.freecodecamp.org/images/IVi4qXeQV0wHLso3jw-YSNt4Qdq1jz5WOSSQ)

This jar file will be injected into Sqoop binaries to apply the structure to incoming data.

**Step 4**: Delete the target directory if it already exists.

![Image](https://cdn-media-1.freecodecamp.org/images/PnNCCNdcFYG63ckjOdNQz9sLwHwp-xQhA6mh)

**Step 5**: Import the data

![Image](https://cdn-media-1.freecodecamp.org/images/L0xKeU6eZzzFNXq9GTUizLA9daPHdicLyKcm)

Here, it connects to a resource manager, gets the resource, and starts the application master.

![Image](https://cdn-media-1.freecodecamp.org/images/0k04I6Df7Ox1UGcxyOEqh-WENTYZtboAPfAH)

To perform equal distribution of data among the map tasks, it internally executes a boundary query based on the primary key by default  
 to find the minimum and maximum count of records in the table.  
 Based on the max count, it will divide by the number of mappers and split it amongst each mapper.

![Image](https://cdn-media-1.freecodecamp.org/images/ixpOtqkpYybBmnTLp1o9vsvkG5Z22ybCYWMB)

It uses 4 mappers by default:

![Image](https://cdn-media-1.freecodecamp.org/images/SvulfY8XlKP3-Th9pY7nLI0RBaWZs4spjFWv)

It executes these jobs on different executors as shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/4doX1MPcDsGOirBF0qyTlaEZCUEvZfiCqg1w)

The default number of mappers can be changed by setting the following parameter:

![Image](https://cdn-media-1.freecodecamp.org/images/J4gGRZO4nsjSvBqfH8yopHaCgYyodWutLGLl)

So in our case, it uses 4 threads. Each thread processes mutually exclusive subsets, that is each thread processes different data from the others.

To see the different values, check out the below:

![Image](https://cdn-media-1.freecodecamp.org/images/bRNZNgynB99qUWQVotlG0PCM7UYUYMzatqE1)

Operations that are being performed under each executor nodes:

![Image](https://cdn-media-1.freecodecamp.org/images/Q6V3RYKFJ56mlEPTX5VTPGQqBYWpdlSGBoXW)

In case you perform a Sqooop hive import, one extra step as part of the execution takes place.

**Step 6**: Copy data to hive table

![Image](https://cdn-media-1.freecodecamp.org/images/TRcmgwhHAQy2SutU-R13R53ejFPJ2j2JsB7R)

### **Sqoop Export**

This is used to export data from Hadoop into traditional relational databases.

![Image](https://cdn-media-1.freecodecamp.org/images/s1lKtokuWsuEqmHsb92--czqDaFuQKd8Dvtm)
_Image Credits: [slideshare.net](https://www.slideshare.net/gharriso/from-oracle-to-hadoop-with-sqoop-and-other-tools" rel="noopener" target="_blank" title=")_

Let’s see a sample snippet for the same:

```
sqoop export \  -- connect jdbc:mysql://ms.jayReddy.com:3306/retail_export \  -- username retail_user \  -- password ******* \  -- table product_sqoop_exp \  -- export-dir /user/jvanchir/sqoop_prac/import_table_dir/products
```

On executing the above command, the execution steps (1–4) similar to Sqoop import take place, but the source data is read from the file system (which is nothing but HDFS). Here it will use boundaries upon block size to divide the data and it is internally taken care by Sqoop.

The processing splits are done as shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/pFCifYgZx8KRMRCVxfJdk7HOigxDTZOX5UQz)

After connecting to the respective database to which the records are to be exported, it will issue a JDBC insert command to read data from HDFS and store it into the database as shown below.

![Image](https://cdn-media-1.freecodecamp.org/images/dWB1TZmEH07zlJ3TOKnVZm1dvzVvbEKOIa5c)

Now that we have seen how Sqoop works internally, you can determine the flow of execution from jar generation to execution of a MapReduce task on the submission of a Sqoop job.

**Note_:_** The commands that were executed related to this post are added as part of my [GIT](https://github.com/Jayvardhan-Reddy/BigData-Ecosystem-Architecture) account.

Similarly, you can also read more here:

* [Hive Architecture in Depth](https://medium.com/plumbersofdatascience/hive-architecture-in-depth-ba44e8946cbc) with **code**.
* [HDFS Architecture in Depth](https://medium.com/plumbersofdatascience/hdfs-architecture-in-depth-1edb822b95fa) with **code**.

If you would like too, you can connect with me on LinkedIn - [Jayvardhan Reddy](https://www.linkedin.com/in/jayvardhan-reddy-vanchireddy).

If you enjoyed reading this article, you can click the clap and let others know about it. If you would like me to add anything else, please feel free to leave a response ?

