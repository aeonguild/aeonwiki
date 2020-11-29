Wallet RPC
=========

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

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `config-file`

Specify a config file to load options from.

An example config file is shown below.

```bash
# /aeon-wallet-cli.conf

daemon-address=192.168.0.1:9149
daemon-login=user:rpcpassword
trusted-daemon=1
password=walletpassword
```

Then launch wallet-cli with the following command:

```
./aeon-wallet-cli --config-file=/path/to/file/aeon-wallet-cli.conf
```


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `help`

Produce a help message with a list of these available options.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `log-file`

The path to be used for the log file.

Default argument: `aeon-wallet-cli.log`

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `max-log-file-size`

Maximum log file size in bytes.

Default argument: `104850000`

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `max-log-files`

Maximum number of rotated log files to be saved (no limit by setting to 0).  

Default argument: `50`

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `log-level`

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

### `daemon-address`

Use aeon daemon at ip-address:port. 
```
--daemon-address=192.168.0.1:9149
```


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `daemon-host`

Use daemon instance at specific IP address instead of localhost.
```
--daemon-host=192.168.0.1
``` 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `confirm-external-bind`
Confirm rpc-bind-ip value is NOT a loopback (local) IP. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `daemon-login`

`username:password` or `username` credentials for daemon RPC client. 

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `daemon-port`

Use daemon instance at specified port. 

Default argument: `11181`


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `trusted-daemon`

Enable the following commands which rely on a trusted daemon:

+ `rescan_spent`
+ `import_key_images`
+ `hw_key_images_sync`
+ `start_mining`


A local connection is trusted by default whereas a remote connection is untrusted by default.


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `untrusted-daemon`

Disable the following commands which rely on a trusted daemon:

+ `rescan_spent`
+ `import_key_images`
+ `hw_key_images_sync`
+ `start_mining`

A local connection is trusted by default whereas a remote connection is untrusted by default.

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `password`                         
Wallet password (escape/quote as needed)

---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `password-file`
Wallet password file


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `prompt-for-password`
Prompts for password when not provided. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `rpc-bind-ip`
Specify IP to bind RPC server. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `rpc-login`
Specify `username[:password]` required for RPC server


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `disable-rpc-login`       
Disable HTTP authentication for RPC connections served by this process.  


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `rpc-access-control-origins`
Specify a comma separated list of origins to allow cross origin resource sharing. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `rpc-bind-port`
Sets bind port for server. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `restricted-rpc`
Restricts to view-only commands. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `wallet-dir`
Directory for newly created wallets


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `wallet-file`
Use wallet <>


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `generate-from-json`            
Generate wallet from JSON format file.  


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `shared-ringdb-dir`
Set shared ring database path. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `detach`
Run as daemon. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `kdf-rounds`              
Number of rounds for the key derivation function. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `max-concurrency`
Max number of threads to use for a parallel job. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `non-interactive`
Run non-interactive


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `tx-notify`                      
Run a program for each new incoming transaction, '%s' will be replaced by the transaction hash. 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `pidfile`
File path to write the rpc's PID to (optional, requires --detach). 


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `stagenet` 
For stagenet. Daemon must also be launched with --stagenet flag


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `testnet`
For testnet. Daemon must also be launched with --testnet flag


---

[<span class="label_source"></span>](#){: .md-button }[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `version`                             
Output version information
