# Wallet CLI

## Usage

  `./aeon-wallet-cli [options] [commands]`

## Description
This is the command line Aeon wallet. It is a tool to manage aeon
transfers and addresses. It needs to connect to an Aeon daemon to 
work correctly.

## Options

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--config-file`

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

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--help`

Produce a help message with a list of these available options.

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--log-file`

The path to be used for the log file.

Default argument: `aeon-wallet-cli.log`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--max-log-file-size`

Maximum log file size in bytes.

Default argument: `104850000`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--max-log-files`

Maximum number of rotated log files to be saved (no limit by setting to 0).  

Default argument: `50`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }


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

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--daemon-address`

Use aeon daemon at ip-address:port. 
```
--daemon-address=192.168.0.1:9149
```
---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }



### `--daemon-host`

Use daemon instance at specific IP address instead of localhost.
```
--daemon-host=192.168.0.1
``` 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }


### `--daemon-login`

`username:password` or `username` credentials for daemon RPC client. 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--do-not-relay`

Newly created transactions received by this daemon will not be relayed to the Aeon network.

Default argument: `0`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }


### `--daemon-port`

Use daemon instance at specified port. 

Default argument: `11181`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }


### `--trusted-daemon`

Enable the following commands which rely on a trusted daemon:

+ `rescan_spent`
+ `import_key_images`
+ `hw_key_images_sync`
+ `start_mining`


A local connection is trusted by default whereas a remote connection is untrusted by default.

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }


### `--untrusted-daemon`

Disable the following commands which rely on a trusted daemon:

+ `rescan_spent`
+ `import_key_images`
+ `hw_key_images_sync`
+ `start_mining`

A local connection is trusted by default whereas a remote connection is untrusted by default.

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }


### `--allow-mismatched-daemon-version`

Allow communicating with a daemon that uses a different RPC version. 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--restore-deterministic-wallet`

Recover wallet using mnemonic seed. 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--restore-multisig-wallet`

Recover multisig wallet using mnemonic seed.

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--generate-new-wallet`

Generate new wallet and save it to a file set by the argument. 
```
./aeon-wallet-cli --generate-new-wallet=/path/to/file/mynewwallet
```
This will create two new files: mynewwallet and mynewwallet.keys

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--create-address-file`

Create an address file for new wallets. 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--wallet-file`

Use wallet 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--generate-from-json`

Generate wallet from JSON format file. 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--generate-from-keys`

Generate wallet from private keys 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--electrum-seed`

Specify Electrum seed for wallet recovery/creation. 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--generate-from-spend-key`

Generate deterministic wallet from spend key. 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--generate-from-view-key`

Generate incoming-only wallet from view key. 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--restore-height`

Restore from specific blockchain height. 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--mnemonic-language`

Language for mnemonic.  

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--wallet-non-deterministic`

Generate non-deterministic view and spend keys

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--generate-from-multisig-keys`

Generate a master wallet from multisig wallet keys 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--password`

Wallet password (escape/quote as needed). 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--password-file`

Wallet password file. 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--shared-ringdb-dir`

Set shared ring database path. 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--use-english-language-names`

Display English language names. 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--kdf-rounds`

Number of rounds for the key derivation function.  

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--max-concurrency`

Max number of threads to use for a parallel job.  

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--tx-notify`                 

Run a program for each new incoming transaction, '%s' will be replaced by the transaction hash. 

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--stagenet`

For stagenet. Daemon must also be launched with --stagenet flag

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--subaddress-lookahead`

Set subaddress lookahead sizes to major:minor

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--testnet`

For testnet. Daemon must also be launched with --testnet flag

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `--version`

Output version information ###Aeon 'Chronos' (v0.14.0.0-release)###

---