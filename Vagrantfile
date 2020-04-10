# -*- mode: ruby -*-
# vi: set ft=ruby :
SERIAL = false

Vagrant.configure(2) do |config|

  config.ssh.insert_key = true
    config.vm.box = "generic/fedora27"
    config.vm.hostname = "dauction2.server"

    config.vm.network "forwarded_port", guest: 8000, host: 8000
    config.vm.network "forwarded_port", guest: 8080, host: 8080

    config.vm.network "private_network", type: "dhcp" # you need this when running on linux

       # config.vm.network "public_network", ip:"192.168.1.100"
       # config.vm.network "public_network", ip:"192.168.56.1"
       #config.vm.network "public_network", ip:"192.168.99.250"
       #config.vm.network "public_network",
       #use_dhcp_assigned_default_route: true

  # This port goes to Nginx webserver
  config.vm.network "forwarded_port", guest: 80, host: 5000

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.name = "dAuction2staging"
    vb.customize ["modifyvm", :id, "--cpuexecutioncap", "60"]
    vb.memory = "6000"
    vb.cpus = 2
  end

  config.vm.provision "DB setup file", type: "file", source: "deployment/create_db2.sql", destination: "/tmp/create_db2.sql"

  config.vm.synced_folder ".", "/vagrant", type: "nfs"  # you may need to install nfs, see for example https://forums.linuxmint.com/viewtopic.php?t=277719


  config.vm.provision "SW layer", type: "shell", inline: <<-SHELL
    sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config && setenforce 0
    echo "net.ipv6.conf.all.disable_ipv6 = 1" >> /etc/sysctl.conf && sysctl -p
    # dnf install -y pypy
    dnf install -y python3-virtualenv python-pip postgresql-server postgresql-contrib postgresql-devel nginx

    ############################################
    # Added by us (not Robert)
    # for pyomo - not really needed here.
        dnf install -y glpk glpk-utils
    # maybe for deployment - not sure.
    #    dnf install -y uwsgi uwsgi-plugin-python3 uwsgi-logger-file
    # for printing capacity
    #     dnf install redhat-rpm-config python-devel python-lxml python-cffi cairo pango gdk-pixbuf2
    # dnf install -y libffi-devel libffi
    # dnf install -y libxml2-devel
    # dnf install -y libxslt-devel
    ############################################
    dnf -y -v groupinstall "C Development Tools and Libraries"
    systemctl enable postgresql &&  postgresql-setup --initdb --unit postgresql
    echo -e "local all all peer\nhost all all 0.0.0.0/0 md5" > /var/lib/pgsql/data/pg_hba.conf
    echo -e "127.0.0.1\tlocalhost" >> /etc/hosts
    systemctl start postgresql
    cd /tmp && sudo -H -u postgres bash -c 'psql -f /tmp/create_db2.sql -v passwd=dauction -v user=dauction'
    dd if=/dev/zero of=/swapfile bs=1024 count=524288
    chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile
    cp /vagrant/deployment/nginx.conf /etc/nginx/
    cp /vagrant/deployment/dauction-nginx.conf /etc/nginx/conf.d/
    cp /vagrant/deployment/systemd/app.service /etc/systemd/system/
  SHELL



  config.vm.provision "requirements0.txt", type: "shell", privileged: false, inline: <<-SHELL
    # exeption for the firewall (new in fedora27)
    sudo firewall-cmd --zone=public --add-port=8000/tcp --permanent
    sudo firewall-cmd --zone=public --add-port=8080/tcp --permanent
    sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
    sudo firewall-cmd --reload
    sudo pip install virtualenv
    python --version
    echo "PIP install from requirements0.txt, will take some time (like 5mins)"
    # virtualenv venv && source venv/bin/activate
   echo "start virtualenv-3.4 venv && source venv/bin/activate"
   virtualenv-3.6 venv && source venv/bin/activate
   echo "end virtualenv venv && source venv/bin/activate"
   echo "delete all folders with migrations in vagrant"
     find /vagrant/ -type d -name migrations -exec rm -r  "{}" \\;
    # added requirements 0
    pip  install -r /vagrant/requirements0.txt
    #pip  install -r /vagrant/requirements1.txt
    pip  install -r /vagrant/requirements.txt
  SHELL


  #config.vm.provision "requirements.txt", type: "shell", privileged: false, inline: #<<-SHELL
   # echo "PIP install from requirements.txt, will take some time (like 5mins)"
    # virtualenv venv && source venv/bin/activate
   # virtualenv-3.4 venv && source venv/bin/activate
   # pip  install -r /vagrant/requirements.txt
  #SHELL

  config.vm.provision "App layer", type: "shell", privileged: false, inline: <<-SHELL
    source venv/bin/activate
    mkdir -p /vagrant/staticfiles
    cd /vagrant
    ~/venv/bin/python manage.py makemigrations auth dAuction2 forward_and_spot instructions distribution master testing
    ~/venv/bin/python manage.py migrate
    ~/venv/bin/python manage.py createcachetable && ~/venv/bin/python manage.py collectstatic -c --noinput



# && ~/venv/bin/python create_users.py - is now done in the program
    echo -e "source ~/venv/bin/activate\ncd /vagrant/" >> ~/.bashrc
  SHELL

  config.vm.provision "Services", type: "shell", inline: <<-SHELL
    setsebool httpd_can_network_connect 1 -P
    systemctl enable app.service nginx.service
    systemctl start app.service nginx.service
  SHELL


  config.vm.provision "shell", inline: <<-SHELL
    echo "Please, install memcached"
    dnf -y install memcached
    #dnf -y install libmemcached-dev
    memcached -h
    systemctl restart memcached
    systemctl status memcached
   SHELL

   #config.vm.provision "shell", inline: <<-SHELL
    #sudo dnf -y install wget
    #sudo wget https://www.rabbitmq.com/releases/erlang/erlang-18.1-1.el7.centos.x86_64.rpm
    #rpm -Uvh erlang-18.1-1.el7.centos.x86_64.rpm
    #sudo dnf -y install erlang
    #sudo wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.2.2/rabbitmq-server-3.2.2-1.noarch.rpm
    #rpm --import http://www.rabbitmq.com/rabbitmq-signing-key-public.asc
    #sudo dnf -y install rabbitmq-server-3.2.2-1.noarch.rpm
    #sudo rabbitmq-server on
    #sudo celery -A dAuction2 beat -l info
    #sudo celery -A dAuction2 worker -l info
   #SHELL

  # Install Memcached
  #config.vm.provision "shell", path: "#{github_url}/scripts/memcached.sh"

end