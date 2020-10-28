# Wallet RPC

## Usage

`./aeon-wallet-rpc [options]`

## Description
This allows one to interact with a wallet through
HTTP requests.

## Options

### `--config`
Config file. Previously `--config-file`.

### `--help`                                
Produce help message

### `--log-file`
Specify log file

### `--log-file-size`
Specify maximum log file size [B] Previously `--max-log-file-size`.

### `--log-file-count`
Specify maximum number of rotated log files to be saved (no limit by setting to 0). Previously `--max-log-files`.

### `--log-level`
0-4 or categories

### `--node-address`                  
Use daemon instance at `<host>:<port>`. Previously `--daemon-address`.

### `--node-ip`                     
Use daemon instance at host instead of localhost. Previously `--daemon-host`.

### `--node-ip-confirm`
Confirm rpc-bind-ip value is NOT a loopback (local) IP. Previously `--confirm-external-bind`.

### `--node-login`     
Specify username[:password] for daemon RPC client. Previously `--trusted-daemon`.

### `--node-port`
Use daemon instance at port <> instead of 11181. Previously `--daemon-port`.

### `--node-trusted`                      
Enable commands which rely on a trusted daemon. Previously `--trusted-daemon`.

### `--node-untrusted` 
Disable commands which rely on a trusted daemon. Previously `--untrusted-daemon`.

### `--password`                         
Wallet password (escape/quote as needed)

### `--password-file`
Wallet password file

### `--password-prompt`
Prompts for password when not provided. Previously `--prompt-for-password`.

### `--rpc-ip`
Specify IP to bind RPC server. Previously `--rpc-bind-ip`.

### `--rpc-login`
Specify `username[:password]` required for RPC server

### `--rpc-disable-login`        
Disable HTTP authentication for RPC connections served by this process.  Previously `--disable-rpc-login`.

### `--rpc-origins`
Specify a comma separated list of origins to allow cross origin resource sharing. Previously `--rpc-access-control-origins`.

### `--rpc-port`
Sets bind port for server. Previously `--rpc-bind-port`.

### `--rpc-safe-mode`
Restricts to view-only commands. Previously `--restricted-rpc`.

### `--wallet-dir`
Directory for newly created wallets

### `--wallet-file`
Use wallet <>

### `--wallet-json`            
Generate wallet from JSON format file.  Previously `--generate-from-json`.

### `--wallet-ringdb-dir`  
Set shared ring database path. Previously `--shared-ringdb-dir`.

### Other

#### `--daemon`
Run as daemon. Previously `--detach`.

#### `--key-rounds`                 
Number of rounds for the key derivation function. Previously `--kdf-rounds`.

#### `--limit-threads`
Max number of threads to use for a parallel job. Previously `--max-concurrency`.

#### `--non-interactive`
Run non-interactive

#### `--notify-tx`                        
Run a program for each new incoming transaction, '%s' will be replaced by the transaction hash. Previously `--tx-notify`.

#### `--pid`
File path to write the rpc's PID to (optional, requires --detach). Previously `--pidfile`.

#### `--stagenet` 
For stagenet. Daemon must also be launched with --stagenet flag

#### `--testnet`
For testnet. Daemon must also be launched with --testnet flag

#### `--version`                             
Output version information

## Commands

### Account
#### `account`
#### `account_balance`
#### `account_balance_proof`
  check reserve proof
#### `account_balance_verify`
  get reserve proof
#### `account_new`
#### `account_label`
#### `account_spendkey`
 spendkey
#### `account_tag`
#### `account_tag_delete`
account untag
#### `account_tag_description`
#### `account_viewkey`
 viewkey
### Address
#### `address`
#### `address_all`
#### `address_integrated`
integrated address
#### `address_label`
integrated address
#### `address_new`
### Contacts
#### `contacts`
address_book
#### `contacts_add`
address_book add
#### `contacts_delete`
address_book delete
### Multisig
#### `multisig_new`
make multisig
#### `multisig_prepare`
prepare multisig
#### `multisig_exchange_keys`
exchange multisig keys
#### `multisig_export`
export multisig info
#### `multisig_finalize`
finalize multisig
#### `multisig_import`
import multisig info
#### `multisig_sign`
sign multisig
#### `multisig_submit`
submit multisig
### Outputs
#### `output_is_spent`
is output spent
#### `output_mark_spent`
mark output spent
#### `output_mark_unspent`
mark output unspent
#### `output_export`
export outputs
#### `output_import`
import outputs
#### `output_unspent`
unspent outputs
### Transfer
#### `transfer`
#### `transfer_locked`
locked transfer
#### `transfer_locked_sweep_all`
locked sweep all
#### `transfer_sweep_all`
sweep all
#### `transfer_sweep_below`
sweep_below
#### `transfer_sweep_single`
sweep single
#### `transfer_sweep_unmixable`
sweep unmixable
### Txs
#### `tx_export`
export transfers
#### `tx_incoming`
incoming transfers
#### `tx_key_export`
export key images
#### `tx_key_import`
import key images
#### `tx_key_set`
set_tx_key
#### `tx_multisig_export_raw`
export raw multisig tx
#### `tx_note`
set_tx_note
#### `tx_payment_id`
payment id
#### `tx_prove_address`
get tx proof
#### `tx_prove_amount`
get spend proof
#### `tx_prove_key`
get tx key
#### `tx_ring_print`
print ring
#### `tx_sign`
sign transfer
#### `tx_verify_address`
check tx proof
#### `tx_verify_amount`
check spend proof
#### `tx_verify_key`
check tx key
#### `tx_view`
show transfer
#### `tx_view_type`
show transfers
### Wallet
#### `wallet`
get description
#### `wallet_info`
#### `wallet_password`
password
#### `wallet_rescan`
rescan_bc
#### `wallet_rescan_spent`
rescan_spent
#### `wallet_seed`
seed
#### `wallet_seed_encrypt`
encrypted seed
#### `wallet_set_account`
account switch
#### `wallet_set_description`
set_description
#### `wallet_sync`
refresh
#### `wallet_watch_only_export`
save_watch_only
### Other
#### `help`
#### `donate`
#### `payments`
set daemon
#### `height`
bc height
#### `save`
#### `save_bc`
#### `save_known_rings`
#### `set`
#### `set log`
#### `set node`
#### `set_ring`
#### `sign`
#### `status`
#### `start_mining`
#### `stop_mining`
#### `verify`
#### `version`




