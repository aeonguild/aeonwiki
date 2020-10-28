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

### Other

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

## Commands

### `GET_BALANCE`
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
### `GET_ADDRESS`
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

### `GET_ADDRESS_INDEX`
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

### `CREATE_ADDRESS`
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

### `LABEL_ADDRESS`
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

### `GET_ACCOUNTS`
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

### `CREATE_ACCOUNT`
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

### `LABEL_ACCOUNT`
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

### `GET_ACCOUNT_TAGS`
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

### `TAG_ACCOUNTS`
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

### `UNTAG_ACCOUNTS`
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

### `SET_ACCOUNT_TAG_DESCRIPTION`
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

### `GET_HEIGHT`
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

### `TRANSFER`
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

### `TRANSFER_SPLIT`
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

### `SIGN_TRANSFER`
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

### `SUBMIT_TRANSFER`
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

### `SWEEP_DUST`
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

### `SWEEP_ALL`
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

### `SWEEP_SINGLE`
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

### `RELAY_TX`
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

### `STORE`
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

### `GET_PAYMENTS`
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

### `GET_BULK_PAYMENTS`
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

### `INCOMING_TRANSFERS`
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
### `QUERY_KEY`
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

### `MAKE_INTEGRATED_ADDRESS`
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

### `SPLIT_INTEGRATED_ADDRESS`
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

### `STOP_WALLET`
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

### `RESCAN_BLOCKCHAIN`
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

### `SET_TX_NOTES`
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

### `GET_TX_NOTES`
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

### `SET_ATTRIBUTE`
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

### `GET_ATTRIBUTE`
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

### `GET_TX_KEY`
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

### `CHECK_TX_KEY`
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

### `GET_TX_PROOF`
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

### `CHECK_TX_PROOF`
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

### `GET_SPEND_PROOF`
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

### `CHECK_SPEND_PROOF`
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

### `GET_RESERVE_PROOF`
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

### `CHECK_RESERVE_PROOF`
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

### `GET_TRANSFERS`
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

### `GET_TRANSFER_BY_TXID`
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

### `SIGN`
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

### `VERIFY`
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

### `EXPORT_OUTPUTS`
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

### `IMPORT_OUTPUTS`
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

### `EXPORT_KEY_IMAGES`
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

### `IMPORT_KEY_IMAGES`
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

### `MAKE_URI`
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

### `PARSE_URI`
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

### `ADD_ADDRESS_BOOK_ENTRY`
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

### `GET_ADDRESS_BOOK_ENTRY`
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

### `DELETE_ADDRESS_BOOK_ENTRY`
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

### `RESCAN_SPENT`
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

### `REFRESH`
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

### `START_MINING`
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

### `STOP_MINING`
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

### `GET_LANGUAGES`
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

### `CREATE_WALLET`
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

### `OPEN_WALLET`
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

### `CLOSE_WALLET`
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

### `CHANGE_WALLET_PASSWORD`
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

### `GENERATE_FROM_KEYS`
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

### `RESTORE_DETERMINISTIC_WALLET`
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
  
### `IS_MULTISIG`
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

### `PREPARE_MULTISIG`
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

### `MAKE_MULTISIG`
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

### `EXPORT_MULTISIG`
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

### `IMPORT_MULTISIG`
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

### `FINALIZE_MULTISIG`
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

### `EXCHANGE_MULTISIG_KEYS`
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

### `SIGN_MULTISIG`
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

### `SUBMIT_MULTISIG`
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

### `GET_VERSION`
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

### `VALIDATE_ADDRESS`
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

### `SET_DAEMON`
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

### `SET_LOG_LEVEL`
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

### `SET_LOG_CATEGORIES`
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
