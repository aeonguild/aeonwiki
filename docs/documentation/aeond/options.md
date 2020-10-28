# Node

## Usage
  `./aeond [options] [commands]`

## Description
This is the command line Aeon peer-to-peer node. 
It is a tool to manage network connections. 

## Options


### `--config-file`


### `--help`                                

Produce help message

### `--bootstrap-daemon-address`

URL of a 'bootstrap' remote daemon that the connected wallets can use 
while this daemon is still not fully synced.  

### `--bootstrap-daemon-login`

Specify username:password for the bootstrap daemon login. 

### `--data-dir`

Specify data directory. 

### `--db-salvage`

Try to salvage a blockchain database if it seems corrupted

### `--db-sync-mode` 

Specify sync option

### `--db-type`

Specify database type, available: lmdb

### `--fast-block-sync`

Sync up most of the way by using embedded, known block hashes.s

### `--limit-blocks`

How many blocks to sync at once during chain synchronization (0 = adaptive). 
Previously `--block-sync-size`.

### `--max-txpool-weight`

Set maximum txpool weight in bytes.

### `--in-peers`

set max number of in peers. 

### `--out-peers`

set max number of out peers.

### `--limit-rate`

set limit-rate [kB/s]

### `--limit-rate-up`

set limit-rate-up [kB/s]

### `--limit-rate-down`

set limit-rate-down [kB/s]

### `--max-concurrency`

### `--prep-blocks-threads`

Max number of threads to use when preparing block hashes in groups. 

### `--log-file` 

Specify log file

### `--max-log-file-size`

Specify maximum log file size [B]. 

### `--max-log-files`

Specify maximum number of rotated log files to be saved 
(no limit by setting to 0). 

### `--log-level` 

Specify log level 0-4.

### `--block-notify`                    

Run a program for each new block, '%s' will be replaced by the block hash. 

### `--block-rate-notify`               

Run a program when the block rate undergoes large fluctuations. 
This might be a sign of large amounts of hash rate going on and 
off the Aeon network, and thus be of potential interest in predicting 
attacks. %t will be replaced by the number of minutes for the 
observation window, %b by the number of blocks observed within 
that window, and %e by the number of blocks that was expected 
in that window. It issuggested that this notification is used 
to automatically increase the number of confirmations required 
before a payment is acted upon. 

### `--reorg-notify`                    

Run a program for each reorg, '%s' will be replaced by the split height, 
'%h' will be replaced by the new blockchain height, '%n' will be replaced 
by the  number of new blocks in the new chain, and '%d' will be replaced 
by the number of blocks discarded from the old chain. 
Previously ``.

### `--p2p-bind-ip`

Interface for p2p network protocol. 
 
### `--offline`

Do not listen for peers, nor connect to any.

### `--p2p-bind-port` 

Port for p2p network protocol. Previously ``.

### `--hide-my-port`

Do not announce yourself as peerlist candidate.

### `--p2p-external-port`

External port for p2p network protocol (if port forwarding used with NAT).   

### `--confirm-external-bind`

Confirm ip value is NOT a loopback (local) IP.

### `--add-peer`

Manually add peer to local peerlist. 

### `--add-exclusive-node`

Specify list of peers to connect to only. If this option is given the options 
add-priority-node and seed-node are ignored. 

### `--peer-priority`

Specify list of peers to connect to and attempt to keep the connection open

### `--rpc-bind-ip`

Specify IP to bind RPC server.

### `--rpc-login`

Specify `username[:password]` required for RPC server.

### `--rpc-access-control-origins`
Specify a comma separated list of origins to allow cross origin resource sharing.

### `--rpc-bind-port`

Specify IP to bind RPC server.

### `--restricted-rpc`

Restrict RPC to view only commands and do not return privacy sensitive data in RPC calls. 

### `--rpc-restricted-port`

Port for restricted RPC server. 

### `--zmq-rpc-bind-ip`

IP for ZMQ RPC server to listen on. 

### `--zmq-rpc-bind-port`

Port for ZMQ RPC server to listen on. 

### `--test-dbg-lock-sleep`

 Sleep time in ms, defaults to 0 (off), used to debug before/after locking mutex. Values 100 to 1000 are good for tests.

### `--test-drop-download`

For net tests: in download, discard ALL blocks instead checking/saving them (very fast).

### `--test-drop-download-height`

Like test-drop-download but discards only after around certain height.

### `--fixed-difficulty`

Fixed difficulty used for testing. 

### `--fluffy-blocks`

Relay blocks as fluffy blocks (obsolete, now default)

### `--no-fluffy-blocks`

Relay blocks as normal blocks. 

### `--allow-local-ip`

Allow local ip add to peer list, mostly in debug purposes.

### `--bg-mining-enable`

enable/disable background mining. Previously .

### `--bg-mining-ignore-battery`

if true, assumes plugged in when unable to query system power status.

### `--bg-mining-min-idle-interval`

Specify min lookback interval in seconds for determining idle state.

### `--bg-mining-idle-threshold`

Specify minimum avg idle percentage over lookback interval. 

### `--bg-mining-miner-target`

Specify maximum percentage cpu use by miner(s).

### `--start-mining`

Specify wallet address to mining for.

### `--mining-threads`

Specify mining threads count. 

### `--regtest`

Run in a regression testing mode. 


#### `--coinbase-message` 

Specify file for extra messages to include into ransactions

#### `--detach`

Run as background process.

#### `--enforce-dns-checkpoints`

checkpoints from DNS server will be enforced.

#### `--disable-dns-checkpoints`        

Do not retrieve checkpoints from DNS..

#### `--non-interactive`

Run non-interactive

#### `--pidfile`

File path to write the daemon's PID to a file. .

#### `--stagenet`

Run on stagenet. The wallet must be launched with --stagenet flag.

#### `--testnet`

Run on testnet. The wallet must be launched with --testnet flag.

#### `--show-time-stats`

Show time-stats when processing blocks/txs and disk synchronization.

#### `--tos-flag`

set terms of service flag

#### `--check-update` 

Check for new versions of Aeon.

#### `--no-idg`

Disable UPnP port mapping. 

#### `--version`                            

Output version information

#### `--os-version`                  

OS for which this executable was compiled.

