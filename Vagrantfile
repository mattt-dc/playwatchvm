Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/bionic64" # or any other Ubuntu version you prefer
    config.vm.network "private_network", type: "dhcp"
  
    config.vm.provision "shell", path: "setup.sh"
    config.vm.provision "shell", path: "autologin.sh"
    config.vm.provision "file", source: "./automation.py", destination: "/home/vagrant/automation.py"
    config.vm.provision "file", source: "./minetest-compile.sh", destination: "/home/vagrant/minetest-compile.sh"
    config.vm.provision "shell", inline: "chmod +x /home/vagrant/automation.py"
    config.vm.provision "shell", inline: "chmod +x /home/vagrant/minetest-compile.sh"
    config.vm.provision "shell", inline: "pip3 install pyautogui"
  
    # Optional: Adjust VM resources
    config.vm.provider "virtualbox" do |vb|
      vb.memory = "2048" # Set the amount of RAM
      vb.cpus = 2        # Set the number of CPU cores
      vb.gui = true      # Set GUI mode
      vb.customize ["modifyvm", :id, "--vram", "256"]
    end
  end
  