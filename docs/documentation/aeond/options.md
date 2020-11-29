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
### `--config-file` 

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
### `--help`

Produce a help message with this list available options.

--- 
[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--bootstrap-daemon-address`

URL of a 'bootstrap' remote daemon that the connected wallets can use 
while this daemon is still not fully synced.  

```
./aeond --bootstrap-daemon-address=127.0.0.1:11180
```

--- 

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--bootstrap-daemon-login`

Specify `username:password` for the bootstrap daemon login. 

```
./aeond --bootstrap-daemon-address=127.0.0.1:11180 --bootstrap-daemon-login=someuser:theirpassword
```
---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--data-dir`

Specify data directory to store the blockchain data base information.

```
./aeond --data-dir=/path/to/some/directory
```

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--db-salvage`

Try to salvage a blockchain database if it seems corrupted.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--db-sync-mode` 

Specify sync option, using format `[safe|fast|fastest]:[sync|async]:[<blocks_per_sync>[blocks]|<bytes_per_sync>[bytes]]`.
```
./aeond --db-sync-mode=fast:async:250000000bytes
```

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--db-type`

Specify database type, available: `lmdb`.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--fast-block-sync`

Sync up most of the way by using block hashes stored in source code.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--limit-blocks`

Limit how many blocks to sync at once during chain synchronization. 0 is an adaptive setting which will change dynamically. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--max-txpool-weight`

Set maximum pending transaction pool size in bytes.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--in-peers`

Set the maximum number of incoming peers connecting to your node. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--out-peers`

Set the maximum number of outgoing peers you are connecting to.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--limit-rate`

Set network traffic limit rate in kB/s.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--limit-rate-up`

Set network traffic upload limit rate in kB/s.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--limit-rate-down`

Set network traffic download limit rate in kB/s.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--max-concurrency`

Set maximum number of CPU threads used by the daemon process for syncronizing blocks and processing transactions.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--prep-blocks-threads`

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--log-file`

The path to be used for the log file.

Default argument: `aeon-wallet-cli.log`

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--max-log-file-size`

Maximum log file size in bytes.

Default argument: `104850000`

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--max-log-files`

Maximum number of rotated log files to be saved (no limit by setting to 0).  

Default argument: `50`

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--log-level`

Accepts arugments of `<level|category>`. Aeon source code has five log levels: 0 ERROR, 1 WARN, 2 INFO, 3 DEBUG, 4 TRACE. Each of the higher log levels contains the log levels below them. So for example

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


### `--block-notify`                    

Run a program for each new block, '%s' will be replaced by the block hash. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
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


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--reorg-notify`                    

Run a program for each reorg, '%s' will be replaced by the split height, 
'%h' will be replaced by the new blockchain height, '%n' will be replaced 
by the  number of new blocks in the new chain, and '%d' will be replaced 
by the number of blocks discarded from the old chain. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--p2p-bind-ip`

Interface for p2p network protocol. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--offline`

Do not listen for peers, nor connect to any.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--p2p-bind-port` 

Port for p2p network protocol. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--hide-my-port`

Do not announce yourself as peerlist candidate.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--p2p-external-port`

External port for p2p network protocol (if port forwarding used with NAT).   

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--confirm-external-bind`

Confirm ip value is NOT a loopback (local) IP.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--add-peer`

Manually add peer to local peerlist. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--add-exclusive-node`

Specify list of peers to connect to only. If this option is given the options 
add-priority-node and seed-node are ignored. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--peer-priority`

Specify list of peers to connect to and attempt to keep the connection open.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--rpc-bind-ip`

Specify IP to bind RPC server.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--rpc-login`

Specify `username[:password]` required for RPC server.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--rpc-access-control-origins`

Specify a comma separated list of origins to allow cross origin resource sharing.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--rpc-bind-port`

Specify IP to bind RPC server.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--restricted-rpc`

Restrict RPC to view only commands and do not return privacy sensitive data in RPC calls.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--rpc-restricted-port`

Port for restricted RPC server. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--zmq-rpc-bind-ip`

IP for ZMQ RPC server to listen on. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--zmq-rpc-bind-port`

Port for ZMQ RPC server to listen on. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--test-dbg-lock-sleep`

 Sleep time in ms, defaults to 0 (off), used to debug before/after locking mutex. Values 100 to 1000 are good for tests.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--test-drop-download`

For net tests: in download, discard ALL blocks instead checking/saving them (very fast).

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--test-drop-download-height`

Like test-drop-download but discards only after around certain height.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--fixed-difficulty`

Fixed difficulty used for testing. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--fluffy-blocks`

Relay blocks as fluffy blocks (obsolete, now default).



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--no-fluffy-blocks`

Relay blocks as normal blocks. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--allow-local-ip`

Allow local ip add to peer list, mostly in debug purposes.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--bg-mining-enable`

Enable/disable background mining.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--bg-mining-ignore-battery`

if true, assumes plugged in when unable to query system power status.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--bg-mining-min-idle-interval`

Specify min lookback interval in seconds for determining idle state.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--bg-mining-idle-threshold`

Specify minimum avg idle percentage over lookback interval.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--bg-mining-miner-target`

Specify maximum percentage cpu use by miner(s).


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--start-mining`

Specify wallet address to mining for.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--mining-threads`

Specify mining threads count. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--regtest`

Run in a regression testing mode. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--coinbase-message` 

Specify file for extra messages to include into transactions.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--detach`

Run as background process.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--enforce-dns-checkpoints`

checkpoints from DNS server will be enforced.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--disable-dns-checkpoints`        

Do not retrieve checkpoints from DNS.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--non-interactive`

Run non-interactive.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--pidfile`

File path to write the daemon's PID to a file. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--stagenet`

Run on stagenet. The wallet must be launched with --stagenet flag.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--testnet`

Run on testnet. The wallet must be launched with --testnet flag.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--show-time-stats`

Show time-stats when processing blocks/txs and disk synchronization.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--tos-flag`

Set terms of service flag.



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--check-update` 

Check for new versions of Aeon.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--no-idg`

Disable UPnP port mapping. 



---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `--version`                            

Output version information.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--os-version`                  

OS for which this executable was compiled.


---


