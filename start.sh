cd
tmux new -d -s aeond './aeon/build/release/bin/aeond --rpc-bind-ip=0.0.0.0 --rpc-restricted-bind-port=11181 --rpc-bind-port=32405 --confirm-external-bind'
cd aeonwiki/onion-monero-blockchain-explorer/build 
tmux new -d -s aeonblocks './aeonblocks'
