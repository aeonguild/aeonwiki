# Open Nodes

##

* [144.76.113.157](http://www.hashvault.pro)
* [95.111.247.164](http://www.vmi390948.contaboserver.net)
* [95.216.145.71](http://www.defusion.de)
* [5.9.16.30](http://www.static.30.16.9.5.clients.your-server.de)
* [142.93.155.14](http://www.aeon.wiki)

Each machine that runs the AEON daemon software is considered a node. Public nodes, or open nodes, are nodes ran by unknown operators who allow you to use their node to broadcast your transaction. There are risks to using public nodes, such as IP+time logging, in which operators of the node can tell when your IP started a transaction. Due to the natural privacy of AEON, your destinations are unknown to that node!. 

To see that your node on is added to this list, launch your daemon with the options `--rpc-bind-ip 0.0.0.0 --rpc-bind-port 11181 --restricted-rpc --confirm-external-bind.`

To use with aeon-wallet-cli, use these commands

* Windows : `aeon-wallet-cli.exe --daemon-address ADDRESS.OF.HOST:11181`

* Unix-type (ubuntu, MacOS) : `./aeon-wallet-cli --daemon-address ADDRESS.OF.HOST:11181`
