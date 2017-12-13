# Crime Ethics and Law

### SQL Injection

  - sql_inject.php
To perform SQL injection we have made a vulnerable webpage which is interacting with database.

To perform a attack  
```sh
$ username : admin
$ password : india' or 'a' = 'a
Click on Submit
```

It will login into admin account

For secure Login
```sh
$ username : admin
$ password : india' or 'a' = 'a
Click on Secure Submit
```

It will generate a error and will not allow to you to perform a sql injection



### Brute Force Attack
  - brute.py
  - log.py
  - testfile.txt
  
Here we have performed brute force attack on a webpage using python script. To demonstrate this attack we need some python libraries as follows
  - itertools - Functions creating iterators for efficient looping
  - mechanize - Automate interaction with HTTP web servers
  - bs4
  

