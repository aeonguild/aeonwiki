aeond
=========

Usage
-------------
  `./aeond [options] [commands]`

Description
-------------
These are the options for the Aeon peer-to-peer node. They will configure how the node operates.

Options
-------------

---
[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `config-file` 

`config-file=<path>`

Specify a config file to load options from.

An example config file is shown below.

```
# /path/to/file/aeond.conf

daemon-address=192.168.0.1:9149
daemon-login=user:rpcpassword
trusted-daemon=1
password=walletpassword
```

Then launch wallet-cli with the following command:

```
./aeond --config-file=/path/to/file/aeond.conf
```

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `help`

`help`

Produce a help message with this list available options.

--- 
[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `bootstrap-daemon-address`

`bootstrap-daemon-address=<ip_address>:<port>`

URL of a 'bootstrap' remote daemon that the connected wallets can use 
while this daemon is still not fully synced.  

```
./aeond --bootstrap-daemon-address=127.0.0.1:11180
```

--- 

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `bootstrap-daemon-login`

`bootstrap-daemon-login=<username>:<password>`

Specify `username:password` for the bootstrap daemon login. 

```
./aeond --bootstrap-daemon-address=127.0.0.1:11180 --bootstrap-daemon-login=someuser:theirpassword
```
---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `data-dir`

`data-dir=<path>`

Specify data directory to store the blockchain data base information.

```
./aeond --data-dir=/path/to/some/directory
```

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `db-salvage`

`db-salvage[=<1|0>]`

Try to salvage a blockchain database if it seems corrupted.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `db-sync-mode` 

`db-sync-mode=[safe|fast|fastest]:[sync|async]:[<blocks_per_sync>[blocks]|<bytes_per_sync>[bytes]]`

Specify sync option.

```
./aeond --db-sync-mode=fast:async:250000000bytes
```

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `db-type`

`db-type=<type>`

Specify database type, available: `lmdb`.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `fast-block-sync`

`fsat-block-sync[=<1|0>]`

Sync up most of the way by using block hashes stored in source code.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `limit-blocks`

`limit-blocks=<number_of_blocks>`

Limit how many blocks to sync at once during chain synchronization. 0 is an adaptive setting which will change dynamically. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `max-txpool-weight`

`max-txpool-weight=<number_of_bytes>`

Set maximum pending transaction pool size in bytes.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `in-peers`

`in-peers=<number_of_peers>`

Set the maximum number of incoming peers connecting to your node. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `out-peers`

`out-peers=<number_of_peers>`

Set the maximum number of outgoing peers you are connecting to.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `limit`

`limit=<kB/s>`

Set both the download and upload limit.

```
>>> limit
limit-down is 8192 kB/s
limit-up is 2048 kB/s
>>> limit 8192
Set limit-down to 8192 kB/s
Set limit-up to 8192 kB/s
```

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `limit-rate-down`

`limit-rate-down=<kB/s>`

Set the download limit.

```
>>> limit_down
limit-down is 8192 kB/s
>>> limit_down 2048
Set limit-down to 2048 kB/s
```

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `limit-rate-up`

`limit-rate-up=<kB/s>`

Set the upload limit.

```
>>> limit_up
limit_up is 8192 kB/s
>>> limit_up 2048
Set limit_up to 2048 kB/s
```

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `max-concurrency`

`max-concurrency=<number_of_cpu_threads>`

Set maximum number of CPU threads used by the daemon process for syncronizing blocks and processing transactions.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

`prep-blocks-threads=<number_of_cpu_threads>`

### `prep-blocks-threads`

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `log-file`

`log-file=<path>`

The path to be used for the log file.

Default argument: `aeon-wallet-cli.log`

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `max-log-file-size`

`max-log-file-size=<bytes>`

Maximum log file size in bytes.

Default argument: `104850000`

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `max-log-files`

`max-log-files=<number>`

Maximum number of rotated log files to be saved (no limit by setting to 0).  

Default argument: `50`

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `log-level`

`log-level=<level|category>`

Aeon source code has five log levels: 0 ERROR, 1 WARN, 2 INFO, 3 DEBUG, 4 TRACE. Each of the higher log levels contains the log levels below them. So for example

```
--log-level=3
``` 

will display levels 0, 1, 2, and 3. To restrict the log to a specific category, you can use the following example

```
--log-level=net.p2p:INFO
```

This will log all ERROR, WARN, and INFO only for net.p2p. To view all net.p2p logs use `net.p2p:TRACE` as that will log all lower levels.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }


### `block-notify`      

`block-notify=<path>`

Run a program for each new block, '%s' will be replaced by the block hash. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `block-rate-notify`               

`block-rate-notify=<path>`

Run a program when the block rate undergoes large fluctuations. 
This might be a sign of large amounts of hash rate going on and 
off the Aeon network, and thus be of potential interest in predicting 
attacks. %t will be replaced by the number of minutes for the 
observation window, %b by the number of blocks observed within 
that window, and %e by the number of blocks that was expected 
in that window. It is suggested that this notification is used 
to automatically increase the number of confirmations required 
before a payment is acted upon. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `reorg-notify`                    

`reorg-notify=<path>`

Run a program for each reorg, '%s' will be replaced by the split height, 
'%h' will be replaced by the new blockchain height, '%n' will be replaced 
by the  number of new blocks in the new chain, and '%d' will be replaced 
by the number of blocks discarded from the old chain. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `p2p-bind-ip`

`p2p-bind-ip=<ip_address>`

Interface for p2p network protocol. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `offline`

`offline[=<1|0>]`

Do not listen for peers, nor connect to any.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `p2p-bind-port` 

`p2p-bind-port=<port>`

Port for p2p network protocol. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `hide-my-port`

`hide-my-port[=<1|0>]`

Do not announce yourself as peerlist candidate.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `p2p-external-port`

`p2p-external-port=<port>`

External port for p2p network protocol (if port forwarding used with NAT).   

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `confirm-external-bind`

`confirm-external-bind[=<1|0>]`

Confirm ip value is NOT a loopback (local) IP.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `add-peer`

`add-peer=<ip_address>:<port>`

Manually add peer to local peerlist. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `add-exclusive-node`

`add-exclusive-node=<ip_address>:<port>`

Specify list of peers to connect to only. If this option is given the options 
add-priority-node and seed-node are ignored. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `peer-priority`
`peer-priority=<ip_address>:<port>`

Specify list of peers to connect to and attempt to keep the connection open.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `rpc-bind-ip`

`rpc-bind-ip=<ip_address>`

Specify IP to bind RPC server.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `rpc-login`

`rpc-login=<username>[:<password>]`

Specify `username[:password]` required for RPC server.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `rpc-access-control-origins`

Specify a comma separated list of origins to allow cross origin resource sharing.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `rpc-bind-port`

`rpc-bind-port=<port>`

Specify IP to bind RPC server.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `restricted-rpc`

`restricted-rpc[=<1|0>]`

Restrict RPC to view only commands and do not return privacy sensitive data in RPC calls.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `rpc-restricted-port`

`rpc-restricted-port=<port>`

Port for restricted RPC server. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `zmq-rpc-bind-ip`

`zmq-rpc-bind-ip=<ip_address>`

IP for ZMQ RPC server to listen on. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `zmq-rpc-bind-port`

`zmq-rpc-bind-port=<port>`

Port for ZMQ RPC server to listen on. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `test-dbg-lock-sleep`

`test-dbg-lock-sleep[=<1|0>]`

 Sleep time in ms, defaults to 0 (off), used to debug before/after locking mutex. Values 100 to 1000 are good for tests.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `test-drop-download`

`test-drop-download[=<1|0>]`

For net tests: in download, discard ALL blocks instead checking/saving them (very fast).

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `test-drop-download-height`

`test-drop-download-height[=<1|0>]`

Like test-drop-download but discards only after around certain height.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `fixed-difficulty`

`fixed-difficulty=<difficulty>`

Fixed difficulty used for testing. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `fluffy-blocks`

`fluffy-blocks[=<1|0>]`

Relay blocks as fluffy blocks (obsolete, now default).



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `no-fluffy-blocks`

`no-fluffy-blocks[=<1|0>]`

Relay blocks as normal blocks. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `allow-local-ip`

`allow-local-ip[=<1|0>]`

Allow local ip add to peer list, mostly in debug purposes.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `bg-mining-enable`

`bg-mining-enable[=<1|0>]`

Enable/disable background mining.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `bg-mining-ignore-battery`

`bg-mining-ignore-battery[=<1|0>]`

If true, assumes plugged in when unable to query system power status.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `bg-mining-min-idle-interval`

`bg-mining-min-idle-interval=<seconds>`

Specify min lookback interval in seconds for determining idle state.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `bg-mining-idle-threshold`

`bg-mining-min-idle-interval=<percentage>`

Specify minimum avg idle percentage over lookback interval.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `bg-mining-miner-target`

`bg-mining-miner-target=<percentage>`

Specify maximum percentage cpu use by miner(s).


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `start-mining`

`start-mining=<address>`

Specify wallet address to mining for.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `mining-threads`

`mining-threads=<number>`

Specify mining threads count. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `regtest`

`regtest[=<1|0>]`

Run in a regression testing mode. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `coinbase-message` 

`coinbase-message=<message>`

Specify file for extra messages to include into transactions.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `detach`

`detach[=<1|0>]`

Run as background process.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `enforce-dns-checkpoints`

`enforce-dns-checkpoints[=<1|0>]`

checkpoints from DNS server will be enforced.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `disable-dns-checkpoints`     

`disable-dns-checkpoints[=<1|0>]`   

Do not retrieve checkpoints from DNS.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `non-interactive`

`non-interactive[=<1|0>]`

Run non-interactive.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `pidfile`

`pidfile=<path>`

File path to write the daemon's PID to a file. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `stagenet`

`stagenet[=<1|0>]`

Run on stagenet. The daemon must be launched with --stagenet flag.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `testnet`

`testnet[=<1|0>]`

Run on testnet. The wallet must be launched with --testnet flag.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `show-time-stats`

`show-time-stats[=<1|0>]`

Show time-stats when processing blocks/txs and disk synchronization.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `tos-flag`

`tos-flag[=<1|0>]`

Set terms of service flag.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `check-update` 

`check-update[=<1|0>]`

Check for new versions of Aeon.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `no-idg`

`no-idg[=<1|0>]`

Disable UPnP port mapping. 



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `version`                            

`version`

Output version information.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `os-version`                             

`os-version`
             
OS for which this executable was compiled.


---


