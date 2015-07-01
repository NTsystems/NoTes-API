# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.define :api do |api|
        api.vm.box = "ubuntu/trusty64"

        # networking
        api.vm.network :private_network, ip: "192.168.85.5"

        # box
        api.vm.provider :virtualbox do |vb|
            vb.name = "notes-api"
            vb.memory = "1024"
        end

        # provisioning
        api.vm.provision :shell, :inline => <<-SCRIPT
            # add docker repo
            apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
            sh -c "echo deb https://get.docker.com/ubuntu docker main > /etc/apt/sources.list.d/docker.list"

            # update system
            apt-get update
            apt-get upgrade -y

            # install dev tools
            apt-get install -y python-dev python-pip libpq-dev lxc-docker
            gpasswd -a vagrant docker

            # install docker-compose
            curl -L https://github.com/docker/compose/releases/download/1.3.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
            chmod +x /usr/local/bin/docker-compose

            # start containers
            cd /vagrant
            pip install -r ./requirements/dev.txt
            docker-compose up -d postgres
            docker-compose up -d celery
        SCRIPT
    end
end
