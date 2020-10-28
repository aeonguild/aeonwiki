# Node

## Usage
  `./aeond [options] [commands]`

## Description
This is the command line Aeon peer-to-peer node. 
It is a tool to manage network connections. 

## Options


### `--config`

Specify configuration file. Previously `--config-file`

### `--help`                                

Produce help message

### `--bootstrap-address`

URL of a 'bootstrap' remote daemon that the connected wallets can use 
while this daemon is still not fully synced.  Previously `--bootstrap-daemon-address`.

### `--bootstrap-login`

Specify username:password for the bootstrap daemon login. Previously `--bootstrap-daemon-login`.

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

### `--limit-mempool`

Set maximum txpool weight in bytes. Previously `--max-txpool-weight`.

### `--limit-peers-in`

set max number of in peers. Previously `--in-peers`.

### `--limit-peers-out`

set max number of out peers. Previously `--out-peers`.

### `--limit-rate`

set limit-rate [kB/s]

### `--limit-rate-up`

set limit-rate-up [kB/s]

### `--limit-rate-down`

set limit-rate-down [kB/s]

### `--limit-threads`

Max number of threads to use for a parallel job. Previously `--max-concurrency`.

### `--limit-threads-blocks`

Max number of threads to use when preparing block hashes in groups. 
Previously `--prep-blocks-threads`.

### `--log-file` 

Specify log file

### `--log-file-size`

Specify maximum log file size [B]. Previously `--max-log-file-size`.

### `--log-file-count`

Specify maximum number of rotated log files to be saved 
(no limit by setting to 0). Previously `--max-log-files`.

### `--log-level` 

Specify log level 0-4.

### `--notify-block`                    

Run a program for each new block, '%s' will be replaced by the block hash. 
Previously `--block-notify`.

### `--notify-block-rate`               

Run a program when the block rate undergoes large fluctuations. 
This might be a sign of large amounts of hash rate going on and 
off the Aeon network, and thus be of potential interest in predicting 
attacks. %t will be replaced by the number of minutes for the 
observation window, %b by the number of blocks observed within 
that window, and %e by the number of blocks that was expected 
in that window. It issuggested that this notification is used 
to automatically increase the number of confirmations required 
before a payment is acted upon. Previously `--block-rate-notify`.

### `--notify-reorg`                    

Run a program for each reorg, '%s' will be replaced by the split height, 
'%h' will be replaced by the new blockchain height, '%n' will be replaced 
by the  number of new blocks in the new chain, and '%d' will be replaced 
by the number of blocks discarded from the old chain. 
Previously `--reorg-notify`.

### `--node-ip`

Interface for p2p network protocol. Previously `--p2p-bind-ip`.
 
### `--node-offline`

Do not listen for peers, nor connect to any. Previously `--offline`.

### `--node-port` 

Port for p2p network protocol. Previously `--p2p-bind-port`.

### `--node-port-hide`

Do not announce yourself as peerlist candidate.  Previously `--hide-my-port`.

### `--node-port-external`

External port for p2p network protocol (if port forwarding used with NAT).   
Previously `--p2p-external-port`.

### `--node-port-external-confirm`

Confirm ip value is NOT a loopback (local) IP. Previously `--confirm-external-bind`.

### `--peer`

Manually add peer to local peerlist. Previously `--add-peer`.

### `--peer-exclusive`

Specify list of peers to connect to only. If this option is given the options 
add-priority-node and seed-node are ignored. Previously `--add-exclusive-node`

### `--peer-priority`

Specify list of peers to connect to and attempt to keep the connection open

### `--rpc-ip`

Specify IP to bind RPC server. Previously `--rpc-bind-ip`.

### `--rpc-login`

Specify `username[:password]` required for RPC server.

### `--rpc-origins`
Specify a comma separated list of origins to allow cross origin resource sharing. Previously `--rpc-access-control-origins`.

### `--rpc-port`

Specify IP to bind RPC server. Previously `--rpc-bind-port`.

### `--rpc-safe-mode`

Restrict RPC to view only commands and do not return privacy sensitive data in RPC calls. Previously `--restricted-rpc`.

### `--rpc-safe-mode-port`

Port for restricted RPC server. Previously `--rpc-restricted-port`.

### `--rpc-zmq-ip`

IP for ZMQ RPC server to listen on. Previously `--zmq-rpc-bind-ip`.

### `--rpc-zmq-port`

Port for ZMQ RPC server to listen on. Previously `--zmq-rpc-bind-port`.

### `--test-dbg-lock-sleep`

 Sleep time in ms, defaults to 0 (off), used to debug before/after locking mutex. Values 100 to 1000 are good for tests.

### `--test-drop-download`

For net tests: in download, discard ALL blocks instead checking/saving them (very fast).

### `--test-drop-download-height`

Like test-drop-download but discards only after around certain height.

### `--test-fixed-diff`

Fixed difficulty used for testing. Previously `--fixed-difficulty`.

### `--test-blocks-fluffy`

Relay blocks as fluffy blocks (obsolete, now default)Previously `--fluffy-blocks`.

### `--test-blocks-no-fluffy`

Relay blocks as normal blocks. Previously `--no-fluffy-blocks`.

### `--test-local-ip`

Allow local ip add to peer list, mostly in debug purposes. Previously `--allow-local-ip`.

### `--test-pow-enable-bg`

enable/disable background mining. Previously `--bg-mining-enable`.

### `--test-pow-ignore-battery`

if true, assumes plugged in when unable to query system power status. Previously `--bg-mining-ignore-battery`.

### `--test-pow-idle-interval`

Specify min lookback interval in seconds for determining idle state. Previously `--bg-mining-min-idle-interval`.

### `--test-pow-idle-threshold`

Specify minimum avg idle percentage over lookback interval. Previously `--bg-mining-idle-threshold`.

### `--test-pow-cpu-limit`

Specify maximum percentage cpu use by miner(s). Previously `--bg-mining-miner-target`.

### `--test-pow-address`

Specify wallet address to mining for. Previously `--start-mining`.

### `--test-pow-threads`

Specify mining threads count. Previously `--mining-threads`.

### `--test-reg`

Run in a regression testing mode. Previously `--regtest`.

### Other

#### `--coinbase-message` 

Specify file for extra messages to include into ransactions

#### `--daemon`

Run as background process. Previously `--detach`.

#### `--dns-checkpoint`

checkpoints from DNS server will be enforced. Previously `--enforce-dns-checkpoints`.

#### `--dns-checkpoint-disable`             

Do not retrieve checkpoints from DNS. Previously `--disable-dns-checkpoints`.

#### `--non-interactive`

Run non-interactive

#### `--pid`

File path to write the daemon's PID to a file. Previously `--pidfile`.

#### `--stagenet`

Run on stagenet. The wallet must be launched with --stagenet flag.

#### `--testnet`

Run on testnet. The wallet must be launched with --testnet flag.

#### `--time-stats`

Show time-stats when processing blocks/txs and disk synchronization. Previously `--show-time-stats`.

#### `--tos-flag`

set terms of service flag

#### `--update` 

Check for new versions of Aeon. Previously `--check-update`.

#### `--upnp-disable`

Disable UPnP port mapping. Previously `--no-idg`.

#### `--version`                            

Output version information

#### `--version-compile`                          

OS for which this executable was compiled. Previously `--os-version`.


## Commands

### `alt_chain_info`

### `ban`

### `bans`

### `bc_dyn_stats`

### `diff`

### `exit`

### `flush_txpool`

### `hard_fork_info`

### `help`

### `hide_hr`

### `in_peers`

### `is_key_image_spent`

### `limit`

### `limit_down`

### `limit_up`

### `out_peers`

### `output_histogram`

### `print_bc`

### `print_block`

### `print_cn`

### `print_coinbase_tx_sum`

### `print_height`

### `print_pl`

### `print_pl_stats`

### `print_pool`

### `print_pool_sh`

### `print_pool_stats`

### `print_status`

### `print_tx`

### `relay_tx`

### `save`

### `set_log`

### `show_hr`

### `start_mining`

### `start_save_graph`

### `status`

### `stop_daemon`

### `stop_mining`

### `stop_save_graph`

### `sync_info`

### `unban`

### `update`

### `version`
