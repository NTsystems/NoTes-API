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
            apt-get install -y python-dev python-pip python-virtualenv libpq-dev
            pip install fabric

            # install docker
            apt-get install -y lxc-docker
            gpasswd -a vagrant docker

            # install docker-compose
            curl -L https://github.com/docker/compose/releases/download/1.1.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
            chmod +x /usr/local/bin/docker-compose

            # start postgresql instance
            docker run --name notes-db -p 5432:5432 -e POSTGRES_PASSWORD=ntsystems -e POSTGRES_USER=ntsystems -d postgres:9.3
        SCRIPT
    end
end
