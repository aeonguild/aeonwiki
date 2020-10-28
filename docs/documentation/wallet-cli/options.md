# Wallet CLI

## Usage

  `./aeon-wallet-cli [options] [commands]`

## Description
This is the command line Aeon wallet. It is a tool to manage aeon
transfers and addresses. It needs to connect to an Aeon daemon to 
work correctly.

## Options

---

### `--config-file`

Specify a config file to load options from.

An example config file is shown below.

```
# /aeon-wallet-cli.conf

daemon-port=18080
daemon-address=192.168.0.1:9149
daemon-login=user:rpcpassword
trusted-daemon=1
password=walletpassword
```

Then launch wallet-cli with the following command:

```
./aeon-wallet-cli --config-file=/path/to/file/aeon-wallet-cli.conf
```

Default argument: 

---


### `--help`

Produce a help message with a list of these available options.

---

### `--log-file`

The path to be used for the log file.

Default argument: `aeon-wallet-cli.log`

---

### `--max-log-file-size`

Maximum log file size in bytes.

Default argument: `104850000B`

---

### `--max-log-files`

Maximum number of rotated log files to be saved (no limit by setting to 0).  

Default argument: `50`

---

### `--log-level`

Accepts arugments of `<level|category>`. Aeon code has five log levels: 0 ERROR, 1 WARN, 2 INFO, 3 DEBUG, 4 TRACE. Each of the higher log levels contains the log levels below them. So for example

```
--log-level=3
``` 

will display levels 0, 1, 2, and 3. To restrict the log to a specific category, you can use the following example

```
--log-level=net.p2p:INFO
```

This will log all ERROR, WARN, and INFO only for net.p2p. To view all net.p2p logs use TRACE as that will log all lower levels.

---

### `--daemon-address`

Use aeon daemon at ip-address:port. 
```
--daemon-address=192.168.0.1:9149
```

---


### `--daemon-host`

Use daemon instance at specific IP address instead of localhost.
```
--daemon-host=192.168.0.1
``` 

---

### `--daemon-login`

`username:password` or `username` credentials for daemon RPC client. 

---

### `--do-not-relay`

Newly created transactions received by this daemon will not be relayed to the Aeon network.

Default argument: `0`

---

### `--daemon-port`

Use daemon instance at specified port. 

Default argument: `11181`

---

### `--trusted-daemon`

Enable the following commands which rely on a trusted daemon:

+ `rescan_spent`
+ `import_key_images`
+ `hw_key_images_sync`
+ `start_mining`


A local connection is trusted by default whereas a remote connection is untrusted by default.

---

### `--untrusted-daemon`

Disable the following commands which rely on a trusted daemon:

+ `rescan_spent`
+ `import_key_images`
+ `hw_key_images_sync`
+ `start_mining`

A local connection is trusted by default whereas a remote connection is untrusted by default.

---

### `--allow-mismatched-daemon-version`

Allow communicating with a daemon that uses a different RPC version. 

### `--restore-deterministic-wallet`

Recover wallet using mnemonic seed. 

### `--restore-multisig-wallet`

Recover multisig wallet using mnemonic seed.

### `--generate-new-wallet`

Generate new wallet and save it to a file set by the argument. 
```
./aeon-wallet-cli --generate-new-wallet=/path/to/file/mynewwallet
```
This will create two new files: mynewwallet and mynewwallet.keys

### `--create-address-file`

Create an address file for new wallets. 

### `--wallet-file`

Use wallet 

### `--generate-from-json`

Generate wallet from JSON format file. 

### `--generate-from-keys`

Generate wallet from private keys 

### `--electrum-seed`

Specify Electrum seed for wallet recovery/creation. 

### `--generate-from-spend-key`

Generate deterministic wallet from spend key. 

### `--generate-from-view-key`

Generate incoming-only wallet from view key. 

### `--restore-height`

Restore from specific blockchain height. 

### `--mnemonic-language`

Language for mnemonic.  

### `--wallet-non-deterministic`

Generate non-deterministic view and spend keys

### `--generate-from-multisig-keys`

Generate a master wallet from multisig wallet keys 

### `--password`

Wallet password (escape/quote as needed). 

### `--password-file`

Wallet password file. 

### `--shared-ringdb-dir`

Set shared ring database path. 

### `--use-english-language-names`

Display English language names. 

### `--kdf-rounds`

Number of rounds for the key derivation function.  

### `--max-concurrency`

Max number of threads to use for a parallel job.  

### `--tx-notify`                 

Run a program for each new incoming transaction, '%s' will be replaced by the transaction hash. 

### `--stagenet`

For stagenet. Daemon must also be launched with --stagenet flag

### `--subaddress-lookahead`

Set subaddress lookahead sizes to major:minor

### `--testnet`

For testnet. Daemon must also be launched with --testnet flag

### `--version`

Output version information ###Aeon 'Chronos' (v0.14.0.0-release)###
