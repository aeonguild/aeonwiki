# Wallet RPC

## Usage

`./aeon-wallet-rpc [options]`

## Description
This allows one to interact with a wallet through
HTTP requests.

## Options

### `--config-file`
Config file. Previously.

### `--help`                                
Produce help message

### `--log-file`
Specify log file

### `--max-log-file-size`
Specify maximum log file size [B]

### `--max-log-files`
Specify maximum number of rotated log files to be saved (no limit by setting to 0). 

### `--log-level`
0-4 or categories

### `--daemon-address`                  
Use daemon instance at `<host>:<port>`. 

### `--daemon-host`                  
Use daemon instance at host instead of localhost. 

### `--confirm-external-bind`
Confirm rpc-bind-ip value is NOT a loopback (local) IP. 

### `--trusted-daemon`     
Specify username[:password] for daemon RPC client. 

### `--daemon-port`
Use daemon instance at port <> instead of 11181. 

### `--trusted-daemon`                    
Enable commands which rely on a trusted daemon. 

### `--untrusted-daemon`
Disable commands which rely on a trusted daemon. 

### `--password`                         
Wallet password (escape/quote as needed)

### `--password-file`
Wallet password file

### `--prompt-for-password`
Prompts for password when not provided. 

### `--rpc-bind-ip`
Specify IP to bind RPC server. 

### `--rpc-login`
Specify `username[:password]` required for RPC server

### `--disable-rpc-login`       
Disable HTTP authentication for RPC connections served by this process.  

### `--rpc-access-control-origins`
Specify a comma separated list of origins to allow cross origin resource sharing. 

### `--rpc-bind-port`
Sets bind port for server. 

### `--restricted-rpc`
Restricts to view-only commands. 

### `--wallet-dir`
Directory for newly created wallets

### `--wallet-file`
Use wallet <>

### `--generate-from-json`            
Generate wallet from JSON format file.  

### `--shared-ringdb-dir`
Set shared ring database path. 

### `--detach`
Run as daemon. 

### `--kdf-rounds`              
Number of rounds for the key derivation function. 

### `--max-concurrency`
Max number of threads to use for a parallel job. 

### `--non-interactive`
Run non-interactive

### `--tx-notify`                      
Run a program for each new incoming transaction, '%s' will be replaced by the transaction hash. 

### `--pidfile`
File path to write the rpc's PID to (optional, requires --detach). 

### `--stagenet` 
For stagenet. Daemon must also be launched with --stagenet flag

### `--testnet`
For testnet. Daemon must also be launched with --testnet flag

### `--version`                             
Output version information
