# playwatchvm
## Overview

This is a somewhat hacky but working solution designed to automate gameplay in Minetest (and potentially other games in the future). 

This repository leverages Vagrant to deploy a virtual machine (VM) that downloads, runs Minetest, and applies random inputs during gameplay. The key purpose of this setup is to record these gameplay sessions and corresponding inputs, generating the data to be used for training ML models.
## Disclaimer

This project is experimental and developed with a focus on functionality rather than elegance. The methods and code might not follow best practices but serve the intended purpose.
## Prerequisites

Before setting up, ensure you have the following installed:

* Vagrant
* VirtualBox or any compatible VM provider

Installation

1. Clone this repository:

```git clone https://github.com/mattt-dc/playwatchvm.git```

2. Navigate to the cloned directory:

```cd playwatchvm```

## Usage

1. To set up and run the VM, use the following command:

```vagrant up```

2. Once the VM is running, Minetest will start automatically with a script to apply random inputs and record gameplay. On first boot the script is setup on the vm but not run so restart the vm with the following command:

```vagrant reload```

## Output

The outputs are video files of the gameplay and logs of the random inputs applied. These are stored in the shared directory and can be used as data for [Video-MLGenerator](https://github.com/mattt-dc/Video-MLGenerator).
