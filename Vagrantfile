# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::configure("2") do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "wheezy64"
   
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", 2048]
  end
  config.vm.provision :shell, inline: $servicemix_script

  config.vm.define "servicemix1", primary: true do |servicemix|
    servicemix.vm.network "private_network", ip: "192.168.1.2"
    servicemix.vm.host_name = "servicemix1"
  end
  config.vm.define "servicemix2", primary: true do |servicemix|
    servicemix.vm.network "private_network", ip: "192.168.1.3"
    servicemix.vm.host_name = "servicemix2"
  end
  config.vm.define "servicemix3", primary: true do |servicemix|
    servicemix.vm.network "private_network", ip: "192.168.1.4"
    servicemix.vm.host_name = "servicemix3"
  end
  config.vm.define "servicemix4", primary: true do |servicemix|
    servicemix.vm.network "private_network", ip: "192.168.1.5"
    servicemix.vm.host_name = "servicemix4"
  end
end

$servicemix_script = <<END
  sudo apt-get update
  sudo apt-get -y --force-yes install oracle-java7-jdk
  
  if [ servicemix1 = `hostname` ]; then
    sudo apt-get -y --force-yes install postgresql
    sudo su postgres -c "psql -f /vagrant/servicemix/create_db.sql"

    sudo cp /vagrant/postgres/pg_hba.conf /etc/postgresql/9.1/main/
    sudo cp /vagrant/postgres/postgresql.conf /etc/postgresql/9.1/main/

    sudo invoke-rc.d postgresql restart
  fi

  wget http://repo.fusesource.com/nexus/content/repositories/releases/org/apache/servicemix/apache-servicemix/4.4.1-fuse-07-11/apache-servicemix-4.4.1-fuse-07-11.tar.gz
  tar xvfz apache-servicemix-4.4.1-fuse-07-11.tar.gz
  cp /vagrant/servicemix/etc/* apache-servicemix-4.4.1-fuse-07-11/etc
  cp /vagrant/servicemix/deploy/* apache-servicemix-4.4.1-fuse-07-11/deploy
  cp /vagrant/servicemix/bin/* apache-servicemix-4.4.1-fuse-07-11/bin
  sudo cp -r /vagrant/servicemix/ewafermapping /etc

  sudo chown -R vagrant apache-servicemix-4.4.1-fuse-07-11
  sudo cp /vagrant/servicemix/servicemix.init /etc/init.d/servicemix
  sudo chmod +x /etc/init.d/servicemix
  sudo update-rc.d servicemix defaults 99
  sudo /etc/init.d/servicemix start

  cp /vagrant/servicemix/masterslave.xml-`hostname` apache-servicemix-4.4.1-fuse-07-11/deploy/masterslave.xml
END
