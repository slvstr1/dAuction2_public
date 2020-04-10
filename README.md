# README: dAuction2 application installation and common issues

About: Aplication to simulate double auction market. We are using Markdown for this
file. We will carry the steps for setting up a Windows environment first, for Linux
jump to chapter 5.

## 1. Install prerequisites to set up a Windows development environment.

### Mandatory

#### 1.0 Install PowerShell when using windows.
If using Windows, make sure you have PowerShell v5+ (https://docs.microsoft.com/en-us/powershell/scripting/setup/installing-windows-powershell?view=powershell-6#upgrading-existing-windows-powershell)


#### 1.1 Install VirtualBox
VirtualBox is used for provisioning and running virtual machines.
Install from the [website](https://www.virtualbox.org).
Use VirtualBox 5.2.6 (presently, 2018.02.20)

#### 1.2 Install Vagrant

Vagrant is a technology to simplify bootstraping the workflow with virtual environments.
Use Vagrant 2.0.2 (presently, 2018.02.20)

#### 1.3 Install GIT

GIT is a version control system (VCS) we use for managing development of our code.
Obtain it from the [GIT Website](https://git-scm.com/download/win).

During installation select "Use GIT and optional Unix tools from the Windows Command
Prompt" option.

#### 1.4 Install Python

At this moment it is recommended to use Python 2.7 branch (as some of the libraries can
 use that as dependency). Obtain Windows installer from [Python](https://www.python
.org/downloads/release/python-2710/).

During installation select `Add python.exe to Path` last option, this will make it
easier to work with Python. Also make sure `PIP` is selected, this is a package manager
for Python.

### Optional

#### 1.5 Install ConEmu

ConEmu is a powerful Windows terminal, replacing standard cmd command.
Download from [ConEmu website](https://conemu.github.io/)

## 2. Main installation: PyCharm

PyCharm comes to be very useful integrated development environment (IDE) for Python. It
 is recommended to use it for development. All is tested on the professional edition,
it is free for students and teachers who have university e-mail.

Simply install it from the provider using the regular settings during installation.

## 3. Setting it all up

### 3.1 Connect to VCS
When in PyCharm intro window: Click  `Checkout from VCS system`.

Login to GitHub, use the [repository](https://github.com/ECON3/dAuction2_interactive3
.git) for code checkout. *(In PyCharm lower right corner, switch to *code_cleanup* branch)

BTW: if you plan to commit changes to code, check with the `GitHub repository` owner
if you have the WRITE permissions instead of READ ONLY.

### 3.2 Set up Vagrant

**First:** In PyCharm select `Tools` then  `Vagrant->Up`, it will take up to 50 (??? 2-8, I would say ???) minutes to
setup the project, this only happens the very first time.

**Then:** You need to configure Vagrant to work with PyCharm correctly.

Go to: `File->Settings->Project:dAuction2_...->Project interpreter`

Now in the upper right corner, click the `settings wheel`, then select `Add
remote->Vagrant`

In the Vagrant tab change the Python interpreter path to
**/home/vagrant/venv/bin/python**
instead of default /usr/bin/python

*(Similar instructions also available at: [PyCharm + Vagrant Remote
Interpreted](https://www.jetbrains.com/pycharm/quickstart/configuring_for_vm.html))*

### 3.3 Set up Django runserver

**First:** You need to enable Django as a language in PyCharm before using a Django
 server. Go: `File->Settings->Languages and Frameworks`. Select `Django`, check the
 `Enable Django support`. Then `Django project root:` must be your project directory on
 your disk and `Settings:` must be `setting\base.py`, base.py is a configuration file!

**Then:** You need to add the Django runserver, in the PyCharm user window, go:
`Run->Edit configurations`, in the top left click the `+` button and select `Django
server`.

Change the host to be `Host: 0.0.0.0 Port: 8000`. Name the server to be 'Django server'
 or something like that.

Now you can go `Run->Run 'Django server'`

After successful server run, you find the app on your localhost. So start your internet
 browser and go 127.0.0.1 .

*(Some instructions also available at: [Configuring PyCharm, Django and Vagrant]
(http://reactuatesoftware.com/configuring-pycharm-django-and-vagrant/))*

### 3.4 Final check: port mapping

After the successful completion of steps 1.0 to 3.3, by default this mapping is
established:

| Host Port | Application        | Guest port |
|-----------|--------------------|------------|
| 5000      | nginx              | 80         |
| 8080      | gunicorn           | 8080       |
| 8000      | development server | 8000       |

Nginx is configured to start by default and listens on port 80, to reach it, go
to [http://127.0.0.1:5000]. It is configured to fetch from proxy served by
`app.service` and is powered by `gunicorn`. This is good for final setup.

For development, either start Django runserver from PyCharm or directly from
the console of the Vagrant box:

    $ vagrant ssh
    $ (venv)[vagrant@dauction2 vagrant] 
    sudo systemctl enable app.service nginx.service
    
    $ ./manage.py runserver 0.0.0.0:8000

#### Regarding the configuration of nginx. There is are two conf files in dAuction2\deployment\nginx.conf and dAuction2\deployment\dauction-nginx.conf
For self-education, you can compare our settings to some settings on https://github.com/h5bp/server-configs-nginx/blob/master/nginx.conf#L67-L109

You can restart nginx by shh (into 127.0.0.1) and then giving the command:

    $ sudo systemctl restart app.service nginx.service


You can start nginx by shh and then giving the command:

    $ sudo
    $ sudo systemctl start app.service nginx.service






## 4. Common issues and solutions

### 4.1 Updating `virtualenv` packages
If you need to upgrade or install new package, login to Vagrant and issue:

    $ pip install <library>
    $ pip freeze > /vagrant/requirements.txt

Then save the changes via GIT.

If you need to update packages, login to the box and issue:

    $ pip install -r /vagrant/requirements.txt

### 4.2 Unapplied migrations

**First option:** Destroy your Vagrant box, then Up Vagrant again.

**Second option:** Go to your project directory and DELETE all folders named "migrations"
(they are under dAuction2 dir and testing dir)

Go `Tools->Run manage.py task`, in the command window send the following
commands:

    makemigrations dAuction2
    migrate dAuction2

    makemigrations testing
    migrate testing

    or

    makemigrations
    migrate

### 4.3 Unable to log in as admin / create new users

In the first run of application, you need to create users and admin using the Python file.

Go `Tools->Start SSH session...`, select `Remote Python Vagrant VM at 'your project dir'`.

In the command line, send this: `python create_users.py`.

After this, you can log in as admin using credentials `admin:admin`.

## 5. Development in Linux

This workflow can be used on from command-line/terminal. This is alternative to PyCharm
 development.

### 5.1 Checkout the code from `GitHub`

    $ git clone https://github.com/ECON3/dAuction2_interactive3.git dAuction2

### 5.2 Create and activate virtual environment

This is used to store all Python related 3rd party libraries (django,postgresql..). The
 folder is taken out from GIT revision using .gitignore file.

 **Initialize it as:**

    $ cd dAuction2
    $ virtualenv venv

**Activate the environment with:**

    $ source venv/bin/activate

It can change the prompt of your shell. Activate the environment every time you
are going to hack on the project.

### 5.3 Install Python requirements

With isolated project environment one can install all python dependencies.

    (venv)~/C/w/dauction2 (code_cleanup) $ pip install -r requirements.txt

####postgresql
postgresql is initialized from the vagrant file. Settings are in ...


### Branching
There are different versions of the program:
1. a stable version for the experiment: "Experiment_Stable"
2. a developing version for education: "Educational"
3. the master branch, having the common elements of both: "master"



