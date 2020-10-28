# Wallet CLI

## Usage

  `./aeon-wallet-cli [options] [commands]`

## Description
This is the command line Aeon wallet. It is a tool to manage aeon
transfers and addresses. It needs to connect to an Aeon daemon to 
work correctly.

## Options

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

`./aeon-wallet-cli --config-file=/path/to/file/aeon-wallet-cli.conf`

Default argument: 


### `--help`

Produce a help message with a list of these available options.

### `--log-file`

The path to be used for the log file.

Default argument: `aeon-wallet-cli.log`

### `--max-log-file-size`

Maximum log file size in bytes.

Default argument: `104850000` (100 MB - 7600 bytes.)

### `--max-log-files`

Maximum number of rotated log files to be saved (no limit by setting to 0).  

Default argument: `50`

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

### `--daemon-address`

Use aeon daemon at ip-address:port. 
```
--daemon-address=192.168.0.1:9149
```

### `--daemon-host`

Use daemon instance at host arg instead of localhost. 

### `--daemon-login`

Specify `username[:password]` for daemon RPC client. 

### `--do-not-relay`

The newly created transaction will not be relayed to the Aeon network.

### `--daemon-port`

Use daemon instance at port arg instead of 11181. 

### `--trusted-daemon`

Enable commands which rely on a trusted daemon. 

### `--untrusted-daemon`

Disable commands which rely on a trusted daemon. 

### `--allow-mismatched-daemon-version`

Allow communicating with a daemon that uses a different RPC version. 

### `--restore-deterministic-wallet`

Recover wallet using Electrum-style mnemonic seed. 

### `--restore-multisig-wallet`

Recover multisig wallet using Electrum-style mnemonic seed.

### `--generate-new-wallet`

Generate new wallet and save it to arg. 

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

### Other

#### `--use-english-language-names`

Display English language names. 

#### `--kdf-rounds`

Number of rounds for the key derivation function.  

#### `--max-concurrency`

Max number of threads to use for a parallel job.  

#### `--tx-notify`                 

Run a program for each new incoming transaction, '%s' will be replaced by the transaction hash. 

#### `--stagenet`

For stagenet. Daemon must also be launched with --stagenet flag

#### `--subaddress-lookahead`

Set subaddress lookahead sizes to major:minor

#### `--testnet`

For testnet. Daemon must also be launched with --testnet flag

#### `--version`

Output version information ###Aeon 'Chronos' (v0.14.0.0-release)###

## Commands
## Commands
#### `account`
#### `account new`
` <label text with white spaces allowed>`
#### `account switch `
`<index>`
#### `account label `
`<index> <label text with white spaces allowed>`
#### `account tag `
`<tag_name> <account_index_1> [<account_index_2> ...]`
#### `account untag `
`<account_index_1> [<account_index_2> ...]`
#### `account tag_description `
`<tag_name> <description>`
#### `address `
`[ new <label text with white spaces allowed> | all | <index_min> [<index_max>] | label <index> <label text with white spaces allowed>]`
#### `address_book `
`[(add ((<address> [pid <id>])|<integrated address>) [<description possibly with whitespaces>])|(delete <index>)]`
#### `balance`
`[detail]`
#### `bc_height`
#### `check_reserve_proof`
`<address> <signature_file> [<message>]`
#### `check_spend_proof `
`<txid> <signature_file> [<message>]`
#### `check_tx_key `
`<txid> <txkey> <address>`
#### `check_tx_proof `
`<txid> <address> <signature_file> [<message>]`
#### `donate `
`[index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] <amount> [<payment_id>]`
#### `encrypted_seed`
#### `exchange_multisig_keys `
`<string> [<string>...]`
#### `export_key_images`
` <file>`
#### `export_multisig_info `
`<filename>`
#### `export_outputs`
` <file>`
#### `export_raw_multisig_tx `
`<filename>`
#### `export_transfers`
` [in|out|all|pending|failed|coinbase] [index=<N1>[,<N2>,...]] [<min_height> [<max_height>]] [output=<filepath>]`
#### `finalize_multisig`
`<string> [<string>...]`
#### `get_description`
#### `get_reserve_proof `
`(all|<amount>) [<message>]`
#### `get_spend_proof`
` <txid> [<message>]`
#### `get_tx_key `
`<txid>`
#### `get_tx_note `
`<txid>`
#### `get_tx_proof `
`<txid> <address> [<message>]`
#### `help `
`[<command>]`
#### `import_key_images`
` <file>`
#### `import_multisig_info`
` <filename> [<filename>...]`
#### `import_outputs`
` <file>`
#### `incoming_transfers`
` [available|unavailable] [verbose] [index=<N1>[,<N2>[,...]]]`
#### `integrated_address`
` [<payment_id> | <address>]`
#### `is_output_spent`
` <amount>/<offset>`
#### `locked_sweep_all`
` [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] <address> <lockblocks> [<payment_id>]`
#### `locked_transfer`
` [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] (<URI> | <addr> <amount>) <lockblocks> [<payment_id>]`
#### `make_multisig`
` <threshold> <string1> [<string>...]`
#### `mark_output_spent`
` <amount>/<offset> | <filename> [add]`
#### `mark_output_unspent`
` <amount>/<offset>`
#### `password`
#### `payment_id`
#### `payments`
` <PID_1> [<PID_2> ... <PID_N>]`
#### `prepare_multisig`
#### `print_ring`
` <key_image> | <txid>`
#### `refresh`
#### `rescan_bc`
#### `rescan_spent`
#### `save`
#### `save_bc`
#### `save_known_rings`
#### `save_watch_only`
#### `seed`
#### `set`
` <option> [<value>]`
#### `set_daemon`
` <host>[:<port>] [trusted|untrusted]`
#### `set_description`
` [free text note]`
#### `set_log`
` <level>|{+,-,}<categories>`
#### `set_ring`
` <filename> | ( <key_image> absolute|relative <index> [<index>...] )`
#### `set_tx_key`
` <txid> <tx_key>`
#### `set_tx_note`
` <txid> [free text note]`
#### `show_transfer`
` <txid>`
#### `show_transfers`
` [in|out|pending|failed|pool|coinbase] [index=<N1>[,<N2>,...]] [<min_height> [<max_height>]]`
#### `sign`
` <file>`
#### `sign_multisig`
` <filename>`
#### `sign_transfer`
` [export_raw]`
#### `spendkey`
#### `start_mining`
` [<number_of_threads>] [bg_mining] [ignore_battery]`
#### `status`
#### `stop_mining`
#### `submit_multisig`
` <filename>`
#### `submit_transfer`
#### `sweep_all`
` [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] <address> [<payment_id>]`
#### `sweep_below `
`<amount_threshold> [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] <address> [<payment_id>]`
#### `sweep_single`
` [<priority>] [<ring_size>] <key_image> <address> [<payment_id>]`
#### `sweep_unmixable`
#### `transfer`
` [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] (<URI> | <address> <amount>) [<payment_id>]`
#### `unspent_outputs`
` [index=<N1>[,<N2>,...]] [<min_amount> [<max_amount>]]`
#### `verify`
` <filename> <address> <signature>`
#### `version`
#### `viewkey`
#### `wallet_info`


