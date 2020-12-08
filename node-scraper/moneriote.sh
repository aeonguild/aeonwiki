#!/bin/bash
#Gingeropolous Open node checker

# This is the directory where files are written to.
# If you run as a cronjob, you have to use the full path
DIR=/root/aeonwiki/node-scraper

# This is the path for your monerod binary.
aeond=/root/aeon/build/release/bin/aeond

# This is the ip of your local daemon. If you're not running an open node, 127.0.0.1 is fine.
daemon=0.0.0.0

#Where you're going to dump the file that will be published
html_dir=/root/aeonwiki/node-scraper

# Bound rpc port
bport=32405

#Port to sniff for
port=11181

echo $aeond
echo $daemon

###

cd $DIR
rm open-nodes.md

echo "# Open Nodes" >> open-nodes.md
echo "" >> open-nodes.md
echo "##" >> open-nodes.md
echo "" >> open-nodes.md
echo "##############"
echo "Check network white nodes for domains to add"

#launch a local daemon instance which will connect to another running daemon and request the current peer list
#note that if the other daemon is running with the "restricted-rpc option", it will ignore "print_pl"
white=$($aeond --rpc-bind-ip $daemon --rpc-bind-port $bport print_pl | grep white | awk '{print $3}' | cut -f 1 -d ":")


white_a=($white)
echo ${white_a[@]}
echo "################"
echo ${#white_a[@]}

echo "#############"
echo "Starting loop"

ctr=0

echo "Number of nodes: "${#white_a[@]} >> moneriote.log


#Comment out to check within the loop, and uncomment the one below
l_hit="$(curl -X POST http://$daemon:$bport/getheight -H 'Content-Type: application/json' | grep height | cut -f 2 -d : | cut -f 1 -d ,)"

for i in "${white_a[@]}"
do
   : 
	echo "Checking ip: "$i
	#Uncomment the below to check within the loop
	#l_hit="$(curl -X POST http://$daemon:$bport/getheight -H 'Content-Type: application/json' | grep height | cut -f 2 -d : | cut -f 1 -d ,)"
    #attempt to connect to each node, allowing 0.5 seconds for connection
	r_hit="$(curl -m 0.5 -X POST http://$i:$port/getheight -H 'Content-Type: application/json' | grep height | cut -f 2 -d : | cut -f 1 -d ,)"
	echo "Local Height: "$l_hit
	echo "Remote Height: "$r_hit
        mini=$(( $l_hit-10 ))
        echo "minimum is " $mini
        maxi=$(( $l_hit+10 ))
        echo "max is " $maxi
        if [[ "$r_hit" ==  "$l_hit" ]] || [[ "$r_hit" > "$mini" && "$r_hit" < "$maxi" ]] && [[ -n $r_hit ]] && [[ -n $l_hit ]]
        then
        echo "################################# Daemon $i is good" 
        if [[ $i == 142.93.155.14 ]]
        then
        echo "* [$i](http://www.aeon.wiki)"  >> open-nodes.md
        elif [[ $i != 0.0.0.0 ]] 
        then
        HOST=$(host $i | awk '{print substr($NF, 1, length($NF)-1)}')
        echo "* [$i](http://www.${HOST})"  >> open-nodes.md
        fi
	elif [[ $r_hit ]] || [[ $l_hit ]]; then
	echo "Either the local or remote is dead"
	else
	echo "$i is closed"
	fi
done
echo "" >> open-nodes.md
echo "Each machine that runs the AEON daemon software is considered a node. Public nodes, or open nodes, are nodes ran by unknown operators who allow you to use their node to broadcast your transaction. There are risks to using public nodes, such as IP+time logging, in which operators of the node can tell when your IP started a transaction. Due to the natural privacy of AEON, your destinations are unknown to that node!. 

To see that your node on is added to this list, launch your daemon with the options \`--rpc-bind-ip 0.0.0.0 --rpc-bind-port 11181 --restricted-rpc --confirm-external-bind.\`" >> open-nodes.md
echo "" >> open-nodes.md
echo "To use with aeon-wallet-cli, use these commands">>open-nodes.md
echo "" >> open-nodes.md
echo "* Windows : \`aeon-wallet-cli.exe --daemon-address ADDRESS.OF.HOST:11181\`">>open-nodes.md
echo "" >> open-nodes.md
echo "* Unix-type (ubuntu, MacOS) : \`./aeon-wallet-cli --daemon-address ADDRESS.OF.HOST:11181\`">> open-nodes.md
