[<span class="label_source"></span>](#){: .md-button }
# Wallet RPC

Usage
-------------

`./aeon-wallet-rpc [options]`

Description
-------------
This allows one to interact with a wallet through
HTTP requests.

Options
-------------


---
[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
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

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `help`

`help`

Produce a help message with this list available options.

--- 

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `log-file`

`log-file=<path>`

The path to be used for the log file.

Default argument: `aeon-wallet-cli.log`

---


[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `max-log-file-size`

`max-log-file-size=<bytes>`

Maximum log file size in bytes.

Default argument: `104850000`

---
[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `max-log-files`

`max-log-files=<number>`

Maximum number of rotated log files to be saved (no limit by setting to 0).  

Default argument: `50`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
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


[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `daemon-address`

`daemon-address=<ip_address>:<port>`

Use aeon daemon at ip-address:port. 

```
--daemon-address=192.168.0.1:9149
```
---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }



### `daemon-host`

`daemon-host=<ip_address>`


Use daemon instance at specific IP address instead of localhost.

```
--daemon-host=192.168.0.1
``` 

---


[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `confirm-external-bind`

`confirm-external-bind[=<1|0>]`

Confirm ip value is NOT a loopback (local) IP.

---


[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }


### `daemon-login`

`daemon-login=<username>[:<password>]`

`username:password` or `username` credentials for daemon RPC client. 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }


### `daemon-port`

`daemon-port=<port>`

Use daemon instance at specified port. 

Default argument: `11181`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }


### `trusted-daemon`

`trusted-daemon[=<1|0>]`

Enable the following commands which rely on a trusted daemon:

+ `rescan_spent`
+ `import_key_images`
+ `hw_key_images_sync`
+ `start_mining`


A local connection is trusted by default whereas a remote connection is untrusted by default.

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }


### `untrusted-daemon`

`untrusted-daemon[=<1|0>]`

Disable the following commands which rely on a trusted daemon:

+ `rescan_spent`
+ `import_key_images`
+ `hw_key_images_sync`
+ `start_mining`

A local connection is trusted by default whereas a remote connection is untrusted by default.

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `password`

`password=<password>`

Wallet password (escape/quote as needed). 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `password-file`

`password-file=<path>`

Wallet password file. 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `prompt-for-password`

`prompt-for-password[=<1|0>`

Prompts for password when not provided. 


---
[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `rpc-bind-ip`

`rpc-bind-ip=<ip_address>`

Specify IP to bind RPC server.

---


[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `rpc-login`

`rpc-login=<username>[:<password>]`

Specify `username[:password]` required for RPC server.

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `disable-rpc-login`       

`disable-rpc-login[=<1|0>`

Disable HTTP authentication for RPC connections served by this process.  


---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `rpc-access-control-origins`

`rpc-access-control-origins=<list,of,comma,separated,urls>`

Specify a comma separated list of origins to allow cross origin resource sharing. 


---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `rpc-bind-port`

`rpc-bind-port=<port>`

Specify IP to bind RPC server.


---
[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `restricted-rpc`

`restricted-rpc[=<1|0>]`

Restrict RPC to view only commands and do not return privacy sensitive data in RPC calls.


---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `wallet-dir`

`wallet-dir=<path>`

Directory for newly created wallets.


---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `wallet-file`

`wallet-file=<path>`

Use wallet file at `path`.


---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `generate-from-json`  

`generate-from-json=<path_to_json>`

Generate wallet from JSON format file.  



---
[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `shared-ringdb-dir`

`shared-ringdb-dir=<path>`

Set shared ring database path. 


---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `detach`

`detach[=<0|1>]`
Run as daemon. 


---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `kdf-rounds`

`kdf-rounds=<number-of-rounds>`

Number of rounds for the key derivation function.  


---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `max-concurrency`

`max-concurrency=<number_of_cpu_threads>`

Set maximum number of CPU threads used by the daemon process for syncronizing blocks and processing transactions.

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `non-interactive`

`non-interactive[=<0|1>]`

Run non-interactive


---


[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `tx-notify`                 

`tx-notify=<path>`

Run a program for each new incoming transaction, '%s' will be replaced by the transaction hash. 


---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `pidfile`

`pidfile=<path_to_file>`

File path to write the rpc's PID to (optional, requires --detach). 


---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `stagenet`

`stagenet[=<1|0>]`

Run on stagenet. The daemon must be launched with --stagenet flag.


---


[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `testnet`

`testnet[=<1|0>]`

Run on testnet. The daemon must be launched with --testnet flag.


---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `version`                            

`version`

Output version information.
