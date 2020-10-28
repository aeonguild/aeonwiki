 Wallet RPC

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

get
set
create
delete
import

### get_balance

  {
    struct request
    {
      uint32_t account_index;
      std::set<uint32_t> address_indices;
      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(account_index)
        KV_SERIALIZE(address_indices)
      END_KV_SERIALIZE_MAP()
    };

    struct per_subaddress_info
    {
      uint32_t address_index;
      std::string address;
      uint64_t balance;
      uint64_t unlocked_balance;
      std::string label;
      uint64_t num_unspent_outputs;
      uint64_t blocks_to_unlock;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(address_index)
        KV_SERIALIZE(address)
        KV_SERIALIZE(balance)
        KV_SERIALIZE(unlocked_balance)
        KV_SERIALIZE(label)
        KV_SERIALIZE(num_unspent_outputs)
        KV_SERIALIZE(blocks_to_unlock)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      uint64_t 	 balance;
      uint64_t 	 unlocked_balance;
      bool       multisig_import_needed;
      std::vector<per_subaddress_info> per_subaddress;
      uint64_t   blocks_to_unlock;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(balance)
        KV_SERIALIZE(unlocked_balance)
        KV_SERIALIZE(multisig_import_needed)
        KV_SERIALIZE(per_subaddress)
        KV_SERIALIZE(blocks_to_unlock)
      END_KV_SERIALIZE_MAP()
    };
  };

### get_address

  {
    struct request
    {
      uint32_t account_index;
      std::vector<uint32_t> address_index;
      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(account_index)
        KV_SERIALIZE(address_index)
      END_KV_SERIALIZE_MAP()
    };

    struct address_info
    {
      std::string address;
      std::string label;
      uint32_t address_index;
      bool used;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(address)
        KV_SERIALIZE(label)
        KV_SERIALIZE(address_index)
        KV_SERIALIZE(used)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string address;                  // to remain compatible with older RPC format
      std::vector<address_info> addresses;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(address)
        KV_SERIALIZE(addresses)
      END_KV_SERIALIZE_MAP()
    };
  };

### create_address
  {
    struct request
    {
      uint32_t account_index;
      std::string label;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(account_index)
        KV_SERIALIZE(label)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string   address;
      uint32_t      address_index;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(address)
        KV_SERIALIZE(address_index)
      END_KV_SERIALIZE_MAP()
    };
  };

### set_address_label
label_address
  {
    struct request
    {
      cryptonote::subaddress_index index;
      std::string label;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(index)
        KV_SERIALIZE(label)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### get_address_is_valid
validate_address
  {
    struct request
    {
      std::string address;
      bool any_net_type;
      bool allow_openalias;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(address)
        KV_SERIALIZE_OPT(any_net_type, false)
        KV_SERIALIZE_OPT(allow_openalias, false)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      bool valid;
      bool integrated;
      bool subaddress;
      std::string nettype;
      std::string openalias_address;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(valid)
        KV_SERIALIZE(integrated)
        KV_SERIALIZE(subaddress)
        KV_SERIALIZE(nettype)
        KV_SERIALIZE(openalias_address)
      END_KV_SERIALIZE_MAP()
    };
  };

### get_address_index
  {
    struct request
    {
      std::string address;
      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(address)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      cryptonote::subaddress_index index;
      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(index)
      END_KV_SERIALIZE_MAP()
    };
  };

### get_account
get_accounts
  {
    struct request
    {
      std::string tag;      // all accounts if empty, otherwise those accounts with this tag

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tag)
      END_KV_SERIALIZE_MAP()
    };

    struct subaddress_account_info
    {
      uint32_t account_index;
      std::string base_address;
      uint64_t balance;
      uint64_t unlocked_balance;
      std::string label;
      std::string tag;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(account_index)
        KV_SERIALIZE(base_address)
        KV_SERIALIZE(balance)
        KV_SERIALIZE(unlocked_balance)
        KV_SERIALIZE(label)
        KV_SERIALIZE(tag)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      uint64_t total_balance;
      uint64_t total_unlocked_balance;
      std::vector<subaddress_account_info> subaddress_accounts;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(total_balance)
        KV_SERIALIZE(total_unlocked_balance)
        KV_SERIALIZE(subaddress_accounts)
      END_KV_SERIALIZE_MAP()
    };
  };

### create_account
post_
create_account
  {
    struct request
    {
      std::string label;
      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(label)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      uint32_t account_index;
      std::string address;      // the 0-th address for convenience
      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(account_index)
        KV_SERIALIZE(address)
      END_KV_SERIALIZE_MAP()
    };
  };

### set_account_label
post_
label_account
  {
    struct request
    {
      uint32_t account_index;
      std::string label;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(account_index)
        KV_SERIALIZE(label)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### get_account_tag
get_
get_account_tags
  {
    struct request
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };

    struct account_tag_info
    {
      std::string tag;
      std::string label;
      std::vector<uint32_t> accounts;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tag);
        KV_SERIALIZE(label);
        KV_SERIALIZE(accounts);
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::vector<account_tag_info> account_tags;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(account_tags)
      END_KV_SERIALIZE_MAP()
    };
  };

### set_account_tag
post_
tag_accounts
  {
    struct request
    {
      std::string tag;
      std::set<uint32_t> accounts;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tag)
        KV_SERIALIZE(accounts)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### delete_account_tag
delete_
untag_accounts

  {
    struct request
    {
      std::set<uint32_t> accounts;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(accounts)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### set_account_tag_description
set_account_tag_description
  {
    struct request
    {
      std::string tag;
      std::string description;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tag)
        KV_SERIALIZE(description)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### create_wallet
create_wallet
  {
    struct request
    {
      std::string filename;
      std::string password;
      std::string language;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(filename)
        KV_SERIALIZE(password)
        KV_SERIALIZE(language)
      END_KV_SERIALIZE_MAP()
    };
    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### create_wallet_from_file
open_wallet
  {
    struct request
    {
      std::string filename;
      std::string password;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(filename)
        KV_SERIALIZE(password)
      END_KV_SERIALIZE_MAP()
    };
    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### close_wallet
close_wallet
  {
    struct request
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### stop_wallet
stop_wallet
  {
    struct request
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### create_wallet_password
change_wallet_password
  {
    struct request
    {
      std::string old_password;
      std::string new_password;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(old_password)
        KV_SERIALIZE(new_password)
      END_KV_SERIALIZE_MAP()
    };
    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### create_wallet_from_keys
generate_from_keys
  {
    struct request
    {
      uint64_t restore_height;
      std::string filename;
      std::string address;
      std::string spendkey;
      std::string viewkey;
      std::string password;

      BEGIN_KV_SERIALIZE_MAP()
      KV_SERIALIZE_OPT(restore_height, (uint64_t)0)
      KV_SERIALIZE(filename)
      KV_SERIALIZE(address)
      KV_SERIALIZE(spendkey)
      KV_SERIALIZE(viewkey)
      KV_SERIALIZE(password)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string address;
      std::string info;

      BEGIN_KV_SERIALIZE_MAP()
      KV_SERIALIZE(address)
      KV_SERIALIZE(info)
      END_KV_SERIALIZE_MAP()
    };
  };

### create_wallet_from_seed
restore_deterministic_wallet
  {
    struct request
    {
      uint64_t restore_height;
      std::string filename;
      std::string seed;
      std::string seed_offset;
      std::string password;
      std::string language;

      BEGIN_KV_SERIALIZE_MAP()
      KV_SERIALIZE_OPT(restore_height, (uint64_t)0)
      KV_SERIALIZE(filename)
      KV_SERIALIZE(seed)
      KV_SERIALIZE(seed_offset)
      KV_SERIALIZE(password)
      KV_SERIALIZE(language)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string address;
      std::string seed;
      std::string info;
      bool was_deprecated;

      BEGIN_KV_SERIALIZE_MAP()
      KV_SERIALIZE(address)
      KV_SERIALIZE(seed)
      KV_SERIALIZE(info)
      KV_SERIALIZE(was_deprecated)
      END_KV_SERIALIZE_MAP()
    };
  };
### get_multisig_is_valid
is_multisig
  {
    struct request
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      bool multisig;
      bool ready;
      uint32_t threshold;
      uint32_t total;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(multisig)
        KV_SERIALIZE(ready)
        KV_SERIALIZE(threshold)
        KV_SERIALIZE(total)
      END_KV_SERIALIZE_MAP()
    };
  };

### start_multisig
prepare_multisig
  {
    struct request
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string multisig_info;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(multisig_info)
      END_KV_SERIALIZE_MAP()
    };
  };

### create_multisig
make_multisig
  {
    struct request
    {
      std::vector<std::string> multisig_info;
      uint32_t threshold;
      std::string password;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(multisig_info)
        KV_SERIALIZE(threshold)
        KV_SERIALIZE(password)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string address;
      std::string multisig_info;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(address)
        KV_SERIALIZE(multisig_info)
      END_KV_SERIALIZE_MAP()
    };
  };

### get_multisig_info
export_multisig_info
  {
    struct request
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string info;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(info)
      END_KV_SERIALIZE_MAP()
    };
  };

### import_multisig_info
import_multisig_info
  {
    struct request
    {
      std::vector<std::string> info;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(info)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      uint64_t n_outputs;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(n_outputs)
      END_KV_SERIALIZE_MAP()
    };
  };

### close_multisig
  {
    struct request
    {
      std::string password;
      std::vector<std::string> multisig_info;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(password)
        KV_SERIALIZE(multisig_info)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string address;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(address)
      END_KV_SERIALIZE_MAP()
    };
  };

### create_multisig_keys_exchange
exchange_multisig_keys
  {
    struct request
    {
      std::string password;
      std::vector<std::string> multisig_info;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(password)
        KV_SERIALIZE(multisig_info)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string address;
      std::string multisig_info;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(address)
        KV_SERIALIZE(multisig_info)
      END_KV_SERIALIZE_MAP()
    };
  };

### set_tx_sign_multisig
sign_multisig
  {
    struct request
    {
      std::string tx_data_hex;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tx_data_hex)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string tx_data_hex;
      std::list<std::string> tx_hash_list;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tx_data_hex)
        KV_SERIALIZE(tx_hash_list)
      END_KV_SERIALIZE_MAP()
    };
  };

### create_contact
add_address_book
  {
    struct request
    {
      std::string address;
      std::string payment_id;
      std::string description;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(address)
        KV_SERIALIZE(payment_id)
        KV_SERIALIZE(description)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      uint64_t index;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(index);
      END_KV_SERIALIZE_MAP()
    };
  };

### get_contact
get_address_book
  {
    struct request
    {
      std::list<uint64_t> entries;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(entries)
      END_KV_SERIALIZE_MAP()
    };

    struct entry
    {
      uint64_t index;
      std::string address;
      std::string payment_id;
      std::string description;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(index)
        KV_SERIALIZE(address)
        KV_SERIALIZE(payment_id)
        KV_SERIALIZE(description)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::vector<entry> entries;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(entries)
      END_KV_SERIALIZE_MAP()
    };
  };

### delete_contact
delete_address_book
  {
    struct request
    {
      uint64_t index;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(index);
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### create_transfer
transfer
  {
    struct request
    {
      std::list<transfer_destination> destinations;
      uint32_t account_index;
      std::set<uint32_t> subaddr_indices;
      uint32_t priority;
      uint64_t mixin;
      uint64_t ring_size;
      uint64_t unlock_time;
      std::string payment_id;
      bool get_tx_key;
      bool do_not_relay;
      bool get_tx_hex;
      bool get_tx_metadata;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(destinations)
        KV_SERIALIZE(account_index)
        KV_SERIALIZE(subaddr_indices)
        KV_SERIALIZE(priority)
        KV_SERIALIZE_OPT(mixin, (uint64_t)0)
        KV_SERIALIZE_OPT(ring_size, (uint64_t)0)
        KV_SERIALIZE(unlock_time)
        KV_SERIALIZE(payment_id)
        KV_SERIALIZE(get_tx_key)
        KV_SERIALIZE_OPT(do_not_relay, false)
        KV_SERIALIZE_OPT(get_tx_hex, false)
        KV_SERIALIZE_OPT(get_tx_metadata, false)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string tx_hash;
      std::string tx_key;
      uint64_t amount;
      uint64_t fee;
      std::string tx_blob;
      std::string tx_metadata;
      std::string multisig_txset;
      std::string unsigned_txset;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tx_hash)
        KV_SERIALIZE(tx_key)
        KV_SERIALIZE(amount)
        KV_SERIALIZE(fee)
        KV_SERIALIZE(tx_blob)
        KV_SERIALIZE(tx_metadata)
        KV_SERIALIZE(multisig_txset)
        KV_SERIALIZE(unsigned_txset)
      END_KV_SERIALIZE_MAP()
    };
  };
### create_transfer_from_hex
submit_transfer
  {
    struct request
    {
      std::string tx_data_hex;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tx_data_hex)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::list<std::string> tx_hash_list;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tx_hash_list)
      END_KV_SERIALIZE_MAP()
    };
  };
  
### create_transfer_from_hex
relay_tx
  {
    struct request
    {
      std::string hex;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(hex)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string tx_hash;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tx_hash)
      END_KV_SERIALIZE_MAP()
    };
  };

### create_transfer_from_hex_multisig
submit_multisig
  {
    struct request
    {
      std::string tx_data_hex;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tx_data_hex)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::list<std::string> tx_hash_list;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tx_hash_list)
      END_KV_SERIALIZE_MAP()
    };
  };
### create_transfer_split
transfer_split
  {
    struct request
    {
      std::list<transfer_destination> destinations;
      uint32_t account_index;
      std::set<uint32_t> subaddr_indices;
      uint32_t priority;
      uint64_t mixin;
      uint64_t ring_size;
      uint64_t unlock_time;
      std::string payment_id;
      bool get_tx_keys;
      bool do_not_relay;
      bool get_tx_hex;
      bool get_tx_metadata;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(destinations)
        KV_SERIALIZE(account_index)
        KV_SERIALIZE(subaddr_indices)
        KV_SERIALIZE(priority)
        KV_SERIALIZE_OPT(mixin, (uint64_t)0)
        KV_SERIALIZE_OPT(ring_size, (uint64_t)0)
        KV_SERIALIZE(unlock_time)
        KV_SERIALIZE(payment_id)
        KV_SERIALIZE(get_tx_keys)
        KV_SERIALIZE_OPT(do_not_relay, false)
        KV_SERIALIZE_OPT(get_tx_hex, false)
        KV_SERIALIZE_OPT(get_tx_metadata, false)
      END_KV_SERIALIZE_MAP()
    };

    struct key_list
    {
      std::list<std::string> keys;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(keys)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::list<std::string> tx_hash_list;
      std::list<std::string> tx_key_list;
      std::list<uint64_t> amount_list;
      std::list<uint64_t> fee_list;
      std::list<std::string> tx_blob_list;
      std::list<std::string> tx_metadata_list;
      std::string multisig_txset;
      std::string unsigned_txset;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tx_hash_list)
        KV_SERIALIZE(tx_key_list)
        KV_SERIALIZE(amount_list)
        KV_SERIALIZE(fee_list)
        KV_SERIALIZE(tx_blob_list)
        KV_SERIALIZE(tx_metadata_list)
        KV_SERIALIZE(multisig_txset)
        KV_SERIALIZE(unsigned_txset)
      END_KV_SERIALIZE_MAP()
    };
  };

### create_transfer_from_small_outputs
post_
sweep_dust sweep_unmixable
  {
    struct request
    {
      bool get_tx_keys;
      bool do_not_relay;
      bool get_tx_hex;
      bool get_tx_metadata;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(get_tx_keys)
        KV_SERIALIZE_OPT(do_not_relay, false)
        KV_SERIALIZE_OPT(get_tx_hex, false)
        KV_SERIALIZE_OPT(get_tx_metadata, false)
      END_KV_SERIALIZE_MAP()
    };

    struct key_list
    {
      std::list<std::string> keys;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(keys)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::list<std::string> tx_hash_list;
      std::list<std::string> tx_key_list;
      std::list<uint64_t> amount_list;
      std::list<uint64_t> fee_list;
      std::list<std::string> tx_blob_list;
      std::list<std::string> tx_metadata_list;
      std::string multisig_txset;
      std::string unsigned_txset;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tx_hash_list)
        KV_SERIALIZE(tx_key_list)
        KV_SERIALIZE(amount_list)
        KV_SERIALIZE(fee_list)
        KV_SERIALIZE(tx_blob_list)
        KV_SERIALIZE(tx_metadata_list)
        KV_SERIALIZE(multisig_txset)
        KV_SERIALIZE(unsigned_txset)
      END_KV_SERIALIZE_MAP()
    };
  };

### create_transfer_from_all_outputs
post_
sweep_all
  {
    struct request
    {
      std::string address;
      uint32_t account_index;
      std::set<uint32_t> subaddr_indices;
      uint32_t priority;
      uint64_t mixin;
      uint64_t ring_size;
      uint64_t unlock_time;
      std::string payment_id;
      bool get_tx_keys;
      uint64_t below_amount;
      bool do_not_relay;
      bool get_tx_hex;
      bool get_tx_metadata;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(address)
        KV_SERIALIZE(account_index)
        KV_SERIALIZE(subaddr_indices)
        KV_SERIALIZE(priority)
        KV_SERIALIZE_OPT(mixin, (uint64_t)0)
        KV_SERIALIZE_OPT(ring_size, (uint64_t)0)
        KV_SERIALIZE(unlock_time)
        KV_SERIALIZE(payment_id)
        KV_SERIALIZE(get_tx_keys)
        KV_SERIALIZE(below_amount)
        KV_SERIALIZE_OPT(do_not_relay, false)
        KV_SERIALIZE_OPT(get_tx_hex, false)
        KV_SERIALIZE_OPT(get_tx_metadata, false)
      END_KV_SERIALIZE_MAP()
    };

    struct key_list
    {
      std::list<std::string> keys;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(keys)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::list<std::string> tx_hash_list;
      std::list<std::string> tx_key_list;
      std::list<uint64_t> amount_list;
      std::list<uint64_t> fee_list;
      std::list<std::string> tx_blob_list;
      std::list<std::string> tx_metadata_list;
      std::string multisig_txset;
      std::string unsigned_txset;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tx_hash_list)
        KV_SERIALIZE(tx_key_list)
        KV_SERIALIZE(amount_list)
        KV_SERIALIZE(fee_list)
        KV_SERIALIZE(tx_blob_list)
        KV_SERIALIZE(tx_metadata_list)
        KV_SERIALIZE(multisig_txset)
        KV_SERIALIZE(unsigned_txset)
      END_KV_SERIALIZE_MAP()
    };
  };

### create_transfer_from_output
sweep_single
  {
    struct request
    {
      std::string address;
      uint32_t priority;
      uint64_t mixin;
      uint64_t ring_size;
      uint64_t unlock_time;
      std::string payment_id;
      bool get_tx_key;
      std::string key_image;
      bool do_not_relay;
      bool get_tx_hex;
      bool get_tx_metadata;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(address)
        KV_SERIALIZE(priority)
        KV_SERIALIZE_OPT(mixin, (uint64_t)0)
        KV_SERIALIZE_OPT(ring_size, (uint64_t)0)
        KV_SERIALIZE(unlock_time)
        KV_SERIALIZE(payment_id)
        KV_SERIALIZE(get_tx_key)
        KV_SERIALIZE(key_image)
        KV_SERIALIZE_OPT(do_not_relay, false)
        KV_SERIALIZE_OPT(get_tx_hex, false)
        KV_SERIALIZE_OPT(get_tx_metadata, false)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string tx_hash;
      std::string tx_key;
      uint64_t amount;
      uint64_t fee;
      std::string tx_blob;
      std::string tx_metadata;
      std::string multisig_txset;
      std::string unsigned_txset;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tx_hash)
        KV_SERIALIZE(tx_key)
        KV_SERIALIZE(amount)
        KV_SERIALIZE(fee)
        KV_SERIALIZE(tx_blob)
        KV_SERIALIZE(tx_metadata)
        KV_SERIALIZE(multisig_txset)
        KV_SERIALIZE(unsigned_txset)
      END_KV_SERIALIZE_MAP()
    };
  };


### get_transfer_signature
sign_transfer
  {
    struct request
    {
      std::string unsigned_txset;
      bool export_raw;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(unsigned_txset)
        KV_SERIALIZE_OPT(export_raw, false)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string signed_txset;
      std::list<std::string> tx_hash_list;
      std::list<std::string> tx_raw_list;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(signed_txset)
        KV_SERIALIZE(tx_hash_list)
        KV_SERIALIZE(tx_raw_list)
      END_KV_SERIALIZE_MAP()
    };
  };

### create_store
store
  {
    struct request
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

  struct payment_details
  {
    std::string payment_id;
    std::string tx_hash;
    uint64_t amount;
    uint64_t block_height;
    uint64_t unlock_time;
    cryptonote::subaddress_index subaddr_index;
    std::string address;

    BEGIN_KV_SERIALIZE_MAP()
      KV_SERIALIZE(payment_id)
      KV_SERIALIZE(tx_hash)
      KV_SERIALIZE(amount)
      KV_SERIALIZE(block_height)
      KV_SERIALIZE(unlock_time)
      KV_SERIALIZE(subaddr_index)
      KV_SERIALIZE(address)
    END_KV_SERIALIZE_MAP()
  };

### get_payments
  {
    struct request
    {
      std::string payment_id;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(payment_id)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::list<payment_details> payments;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(payments)
      END_KV_SERIALIZE_MAP()
    };
  };

### get_payments_bulk
get_bulk_payments
  {
    struct request
    {
      std::vector<std::string> payment_ids;
      uint64_t min_block_height;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(payment_ids)
        KV_SERIALIZE(min_block_height)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::list<payment_details> payments;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(payments)
      END_KV_SERIALIZE_MAP()
    };
  };
  
  struct transfer_details
  {
    uint64_t amount;
    bool spent;
    uint64_t global_index;
    std::string tx_hash;
    cryptonote::subaddress_index subaddr_index;
    std::string key_image;

    BEGIN_KV_SERIALIZE_MAP()
      KV_SERIALIZE(amount)
      KV_SERIALIZE(spent)
      KV_SERIALIZE(global_index)
      KV_SERIALIZE(tx_hash)
      KV_SERIALIZE(subaddr_index)
      KV_SERIALIZE(key_image)
    END_KV_SERIALIZE_MAP()
  };

### get_incoming_transfers
incoming_transfers
  {
    struct request
    {
      std::string transfer_type;
      uint32_t account_index;
      std::set<uint32_t> subaddr_indices;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(transfer_type)
        KV_SERIALIZE(account_index)
        KV_SERIALIZE(subaddr_indices)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::list<transfer_details> transfers;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(transfers)
      END_KV_SERIALIZE_MAP()
    };
  };

  //JSON RPC V2
### get_key_type
query_key
  {
    struct request
    {
      std::string key_type;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(key_type)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string key;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(key)
      END_KV_SERIALIZE_MAP()
    };
  };

### create_integrated_address
make_integrated_address
  {
    struct request
    {
      std::string standard_address;
      std::string payment_id;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(standard_address)
        KV_SERIALIZE(payment_id)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string integrated_address;
      std::string payment_id;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(integrated_address)
        KV_SERIALIZE(payment_id)
      END_KV_SERIALIZE_MAP()
    };
  };

### create_integrated_address_split
split_integrated_address
  {
    struct request
    {
      std::string integrated_address;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(integrated_address)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string standard_address;
      std::string payment_id;
      bool is_subaddress;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(standard_address)
        KV_SERIALIZE(payment_id)
        KV_SERIALIZE(is_subaddress)
      END_KV_SERIALIZE_MAP()
    };
  };

### refresh_blockchain
rescan_blockchain
  {
    struct request
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### set_tx_notes
set_tx_notes
  {
    struct request
    {
      std::list<std::string> txids;
      std::list<std::string> notes;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(txids)
        KV_SERIALIZE(notes)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### get_tx_notes
  {
    struct request
    {
      std::list<std::string> txids;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(txids)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::list<std::string> notes;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(notes)
      END_KV_SERIALIZE_MAP()
    };
  };

### set_attribute
set_attribute
  {
    struct request
    {
      std::string key;
      std::string value;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(key)
        KV_SERIALIZE(value)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### get_attribute
  {
    struct request
    {

      std::string key;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(key)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string value;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(value)
      END_KV_SERIALIZE_MAP()
    };
  };

### get_tx_key
  {
    struct request
    {
      std::string txid;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(txid)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string tx_key;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(tx_key)
      END_KV_SERIALIZE_MAP()
    };
  };

### get_tx_key_info
check_tx_key
  {
    struct request
    {
      std::string txid;
      std::string tx_key;
      std::string address;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(txid)
        KV_SERIALIZE(tx_key)
        KV_SERIALIZE(address)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      uint64_t received;
      bool in_pool;
      uint64_t confirmations;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(received)
        KV_SERIALIZE(in_pool)
        KV_SERIALIZE(confirmations)
      END_KV_SERIALIZE_MAP()
    };
  };

### get_tx_proof
  {
    struct request
    {
      std::string txid;
      std::string address;
      std::string message;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(txid)
        KV_SERIALIZE(address)
        KV_SERIALIZE(message)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string signature;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(signature)
      END_KV_SERIALIZE_MAP()
    };
  };

### get_tx_proof_info
check_tx_proof
  {
    struct request
    {
      std::string txid;
      std::string address;
      std::string message;
      std::string signature;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(txid)
        KV_SERIALIZE(address)
        KV_SERIALIZE(message)
        KV_SERIALIZE(signature)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      bool good;
      uint64_t received;
      bool in_pool;
      uint64_t confirmations;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(good)
        KV_SERIALIZE(received)
        KV_SERIALIZE(in_pool)
        KV_SERIALIZE(confirmations)
      END_KV_SERIALIZE_MAP()
    };
  };

  struct transfer_entry
  {
    std::string txid;
    std::string payment_id;
    uint64_t height;
    uint64_t timestamp;
    uint64_t amount;
    uint64_t fee;
    std::string note;
    std::list<transfer_destination> destinations;
    std::string type;
    uint64_t unlock_time;
    cryptonote::subaddress_index subaddr_index;
    std::vector<cryptonote::subaddress_index> subaddr_indices;
    std::string address;
    bool double_spend_seen;
    uint64_t confirmations;
    uint64_t suggested_confirmations_threshold;

    BEGIN_KV_SERIALIZE_MAP()
      KV_SERIALIZE(txid);
      KV_SERIALIZE(payment_id);
      KV_SERIALIZE(height);
      KV_SERIALIZE(timestamp);
      KV_SERIALIZE(amount);
      KV_SERIALIZE(fee);
      KV_SERIALIZE(note);
      KV_SERIALIZE(destinations);
      KV_SERIALIZE(type);
      KV_SERIALIZE(unlock_time)
      KV_SERIALIZE(subaddr_index);
      KV_SERIALIZE(subaddr_indices);
      KV_SERIALIZE(address);
      KV_SERIALIZE(double_spend_seen)
      KV_SERIALIZE_OPT(confirmations, (uint64_t)0)
      KV_SERIALIZE_OPT(suggested_confirmations_threshold, (uint64_t)0)
    END_KV_SERIALIZE_MAP()
  };

### get_spend_proof
  {
    struct request
    {
      std::string txid;
      std::string message;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(txid)
        KV_SERIALIZE(message)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string signature;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(signature)
      END_KV_SERIALIZE_MAP()
    };
  };

### get_spend_proof_info
check_spend_proof
  {
    struct request
    {
      std::string txid;
      std::string message;
      std::string signature;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(txid)
        KV_SERIALIZE(message)
        KV_SERIALIZE(signature)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      bool good;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(good)
      END_KV_SERIALIZE_MAP()
    };
  };

### get_reserve_proof
  {
    struct request
    {
      bool all;
      uint32_t account_index;     // ignored when `all` is true
      uint64_t amount;            // ignored when `all` is true
      std::string message;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(all)
        KV_SERIALIZE(account_index)
        KV_SERIALIZE(amount)
        KV_SERIALIZE(message)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string signature;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(signature)
      END_KV_SERIALIZE_MAP()
    };
  };

### get_reserve_proof_info
check_reserve_proof
  {
    struct request
    {
      std::string address;
      std::string message;
      std::string signature;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(address)
        KV_SERIALIZE(message)
        KV_SERIALIZE(signature)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      bool good;
      uint64_t total;
      uint64_t spent;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(good)
        KV_SERIALIZE(total)
        KV_SERIALIZE(spent)
      END_KV_SERIALIZE_MAP()
    };
  };

### get_transfers
  {
    struct request
    {
      bool in;
      bool out;
      bool pending;
      bool failed;
      bool pool;

      bool filter_by_height;
      uint64_t min_height;
      uint64_t max_height;
      uint32_t account_index;
      std::set<uint32_t> subaddr_indices;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(in);
        KV_SERIALIZE(out);
        KV_SERIALIZE(pending);
        KV_SERIALIZE(failed);
        KV_SERIALIZE(pool);
        KV_SERIALIZE(filter_by_height);
        KV_SERIALIZE(min_height);
        KV_SERIALIZE_OPT(max_height, (uint64_t)CRYPTONOTE_MAX_BLOCK_NUMBER);
        KV_SERIALIZE(account_index);
        KV_SERIALIZE(subaddr_indices);
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::list<transfer_entry> in;
      std::list<transfer_entry> out;
      std::list<transfer_entry> pending;
      std::list<transfer_entry> failed;
      std::list<transfer_entry> pool;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(in);
        KV_SERIALIZE(out);
        KV_SERIALIZE(pending);
        KV_SERIALIZE(failed);
        KV_SERIALIZE(pool);
      END_KV_SERIALIZE_MAP()
    };
  };

### get_transfer_by_txid
  {
    struct request
    {
      std::string txid;
      uint32_t account_index;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(txid);
        KV_SERIALIZE_OPT(account_index, (uint32_t)0)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      transfer_entry transfer;
      std::list<transfer_entry> transfers;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(transfer);
        KV_SERIALIZE(transfers);
      END_KV_SERIALIZE_MAP()
    };
  };

### get_sign
sign
  {
    struct request
    {
      std::string data;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(data);
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string signature;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(signature);
      END_KV_SERIALIZE_MAP()
    };
  };

### get_verify
verify
  {
    struct request
    {
      std::string data;
      std::string address;
      std::string signature;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(data);
        KV_SERIALIZE(address);
        KV_SERIALIZE(signature);
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      bool good;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(good);
      END_KV_SERIALIZE_MAP()
    };
  };

### get_outputs
export_outputs
  {
    struct request
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string outputs_data_hex;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(outputs_data_hex);
      END_KV_SERIALIZE_MAP()
    };
  };

### import_outputs
import_outputs
  {
    struct request
    {
      std::string outputs_data_hex;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(outputs_data_hex);
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      uint64_t num_imported;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(num_imported);
      END_KV_SERIALIZE_MAP()
    };
  };

### get_key_images
export_key_images
  {
    struct request
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };

    struct signed_key_image
    {
      std::string key_image;
      std::string signature;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(key_image);
        KV_SERIALIZE(signature);
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::vector<signed_key_image> signed_key_images;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(signed_key_images);
      END_KV_SERIALIZE_MAP()
    };
  };

### import_key_images
import_key_images
  {
    struct signed_key_image
    {
      std::string key_image;
      std::string signature;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(key_image);
        KV_SERIALIZE(signature);
      END_KV_SERIALIZE_MAP()
    };

    struct request
    {
      std::vector<signed_key_image> signed_key_images;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(signed_key_images);
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      uint64_t height;
      uint64_t spent;
      uint64_t unspent;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(height)
        KV_SERIALIZE(spent)
        KV_SERIALIZE(unspent)
      END_KV_SERIALIZE_MAP()
    };
  };

  struct uri_spec
  {
    std::string address;
    std::string payment_id;
    uint64_t amount;
    std::string tx_description;
    std::string recipient_name;

    BEGIN_KV_SERIALIZE_MAP()
      KV_SERIALIZE(address);
      KV_SERIALIZE(payment_id);
      KV_SERIALIZE(amount);
      KV_SERIALIZE(tx_description);
      KV_SERIALIZE(recipient_name);
    END_KV_SERIALIZE_MAP()
  };

### get_uri
make_uri
  {
    struct request: public uri_spec
    {
    };

    struct response
    {
      std::string uri;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(uri)
      END_KV_SERIALIZE_MAP()
    };
  };

### get_uri_parse
parse_uri
  {
    struct request
    {
      std::string uri;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(uri)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      uri_spec uri;
      std::vector<std::string> unknown_parameters;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(uri);
        KV_SERIALIZE(unknown_parameters);
      END_KV_SERIALIZE_MAP()
    };
  };

### refresh_spent
rescan_spent
  {
    struct request
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### refresh
refresh
  {
    struct request
    {
      uint64_t start_height;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE_OPT(start_height, (uint64_t) 0)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      uint64_t blocks_fetched;
      bool received_money;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(blocks_fetched);
        KV_SERIALIZE(received_money);
      END_KV_SERIALIZE_MAP()
    };
  };

### get_height 
get_
getheight
    {
      struct request
      {
        BEGIN_KV_SERIALIZE_MAP()
        END_KV_SERIALIZE_MAP()
      };

      struct response
      {
        uint64_t  height;
        BEGIN_KV_SERIALIZE_MAP()
          KV_SERIALIZE(height)
        END_KV_SERIALIZE_MAP()
      };
    };

  struct transfer_destination
  {
    uint64_t amount;
    std::string address;
    BEGIN_KV_SERIALIZE_MAP()
      KV_SERIALIZE(amount)
      KV_SERIALIZE(address)
    END_KV_SERIALIZE_MAP()
  };

### start_mining
start_mining
  {
    struct request
    {
      uint64_t    threads_count;
      bool        do_background_mining;
      bool        ignore_battery;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(threads_count)
        KV_SERIALIZE(do_background_mining)        
        KV_SERIALIZE(ignore_battery)        
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### stop_mining
stop_mining
  {
    struct request
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### get_languages

  {
    struct request
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
    struct response
    {
      std::vector<std::string> languages;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(languages)
      END_KV_SERIALIZE_MAP()
    };
  };

### get_version
  {
    struct request
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      uint32_t version;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(version)
      END_KV_SERIALIZE_MAP()
    };
  };

### set_daemon
set_daemon
  {
    struct request
    {
      std::string address;
      bool trusted;
      bool ssl;
#if 0 // to be enabled when SSL support is added
      std::string ssl_support; // disabled, enabled, autodetect
      std::string ssl_private_key_path;
      std::string ssl_certificate_path;
      std::list<std::string> ssl_allowed_certificates;
      std::vector<std::string> ssl_allowed_fingerprints;
      bool ssl_allow_any_cert;
#endif

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(address)
        KV_SERIALIZE_OPT(trusted, false)
        KV_SERIALIZE_OPT(ssl, false)
#if 0 // to be enabled when SSL support is added
        KV_SERIALIZE_OPT(ssl_support, (std::string)"autodetect")
        KV_SERIALIZE(ssl_private_key_path)
        KV_SERIALIZE(ssl_certificate_path)
        KV_SERIALIZE(ssl_allowed_certificates)
        KV_SERIALIZE(ssl_allowed_fingerprints)
        KV_SERIALIZE_OPT(ssl_allow_any_cert, false)
#endif
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### set_log_level
set_log_level
  {
    struct request
    {
      int8_t level;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(level)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      BEGIN_KV_SERIALIZE_MAP()
      END_KV_SERIALIZE_MAP()
    };
  };

### set_log_categories
set_log_categories
  {
    struct request
    {
      std::string categories;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(categories)
      END_KV_SERIALIZE_MAP()
    };

    struct response
    {
      std::string categories;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(categories)
      END_KV_SERIALIZE_MAP()
    };
  };

}





































