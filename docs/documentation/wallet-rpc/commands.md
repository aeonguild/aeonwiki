---
template: base.html
title: "aeon-wallet-rpc Documentation (Commands)"
---
[<span class="label_source"></span>](#){: .md-button }
# Wallet RPC

This page is still under construction. Follow the progress on [github](https://github.com/ivoryguru/aeonwiki).

## Usage

`./aeon-wallet-rpc [options]`

## Description
This allows one to interact with a wallet through
HTTP requests.

## Commands

### `get_balance`
* request 
```
uint32_t account_index;
std::set<uint32_t> address_indices;
```
* per_subaddress_info 
```
uint32_t address_index;
std::string address;
uint64_t balance;
uint64_t unlocked_balance;
std::string label;
uint64_t num_unspent_outputs;
uint64_t blocks_to_unlock;
```
* response 
```
uint64_t 	 balance;
uint64_t 	 unlocked_balance;
bool       multisig_import_needed;
std::vector<per_subaddress_info> per_subaddress;
uint64_t   blocks_to_unlock;
```

### `get_address`
* request 
```
uint32_t account_index;
std::vector<uint32_t> address_index;
```
* address_info 
```
std::string address;
std::string label;
uint32_t address_index;
bool used;
```
* response 
```
std::string address;
std::vector<address_info> addresses;
```


### `get_address_index`
* request 
```
std::string address;
```
* response 
```
cryptonote::subaddress_index index;
```


### `create_address`
* request 
```
uint32_t account_index;
std::string label;
```
* response 
```
std::string   address;
uint32_t      address_index;
```


### `label_address`
* request 
```
cryptonote::subaddress_index index;
std::string label;
```
* response 
```
```


### `get_accounts`
* request
```
std::string tag;      // all accounts if empty, otherwise those accounts with this tag
```
* subaddress_account_info 
```
uint32_t account_index;
std::string base_address;
uint64_t balance;
uint64_t unlocked_balance;
std::string label;
std::string tag;
```

* response 
```
uint64_t total_balance;
uint64_t total_unlocked_balance;
std::vector<subaddress_account_info> subaddress_accounts;
```


### `create_account`
* request 
```
std::string label;
```
* response 
```
uint32_t account_index;
std::string address;      // the 0-th address for convenience
```


### `label_account`
* request 
```
uint32_t account_index;
std::string label;
```
* response 
```
```


### `get_account_tags`
* request 
```
```
* account_tag_info 
```
std::string tag;
std::string label;
std::vector<uint32_t> accounts;
```
* response 
```
std::vector<account_tag_info> account_tags;
```


### `tag_accounts`
* request 
```
std::string tag;
std::set<uint32_t> accounts;
```
* response 
```
```


### `untag_accounts`
* request 
```
std::set<uint32_t> accounts;
```
* response 
```
```


### `set_account_tag_description`
* request 
```
std::string tag;
std::string description;
```
* response 
```
```


### `get_height`
* request 
```
```
* response
```
uint64_t  height;
```

### `transfer`
* transfer_destination
```
uint64_t amount;
std::string address;
```
* request 
```
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
```
* response 
```
std::string tx_hash;
std::string tx_key;
uint64_t amount;
uint64_t fee;
std::string tx_blob;
std::string tx_metadata;
std::string multisig_txset;
std::string unsigned_txset;
```


### `transfer_split`
* request 
```
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
```
* key_list 
```
std::list<std::string> keys;
```
* response 
```
std::list<std::string> tx_hash_list;
std::list<std::string> tx_key_list;
std::list<uint64_t> amount_list;
std::list<uint64_t> fee_list;
std::list<std::string> tx_blob_list;
std::list<std::string> tx_metadata_list;
std::string multisig_txset;
std::string unsigned_txset;
```


### `sign_transfer`
* request 
```
std::string unsigned_txset;
bool export_raw;
```
* response 
```
std::string signed_txset;
std::list<std::string> tx_hash_list;
std::list<std::string> tx_raw_list;
```


### `submit_transfer`
* request 
```
std::string tx_data_hex;
```
* response 
```
std::list<std::string> tx_hash_list;
```


### `sweep_dust`
* request 
```
bool get_tx_keys;
bool do_not_relay;
bool get_tx_hex;
bool get_tx_metadata;
```
* key_list 
```
std::list<std::string> keys;
```
* response 
```
std::list<std::string> tx_hash_list;
std::list<std::string> tx_key_list;
std::list<uint64_t> amount_list;
std::list<uint64_t> fee_list;
std::list<std::string> tx_blob_list;
std::list<std::string> tx_metadata_list;
std::string multisig_txset;
std::string unsigned_txset;
```


### `sweep_all`
* request 
```
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
```
* key_list 
```
std::list<std::string> keys;
```
* response 
```
std::list<std::string> tx_hash_list;
std::list<std::string> tx_key_list;
std::list<uint64_t> amount_list;
std::list<uint64_t> fee_list;
std::list<std::string> tx_blob_list;
std::list<std::string> tx_metadata_list;
std::string multisig_txset;
std::string unsigned_txset;
```


### `sweep_single`
* request 
```
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
```
* response 
```
std::string tx_hash;
std::string tx_key;
uint64_t amount;
uint64_t fee;
std::string tx_blob;
std::string tx_metadata;
std::string multisig_txset;
std::string unsigned_txset;
```


### `relay_tx`
* request 
```
std::string hex;
```
* response 
```
std::string tx_hash;
```


### `store`
* request 
```
```
* response 
```
```
### `get_payments`
* request 
```
std::string payment_id;

```

* payment_details
```
std::string payment_id;
std::string tx_hash;
uint64_t amount;
uint64_t block_height;
uint64_t unlock_time;
cryptonote::subaddress_index subaddr_index;
std::string address;
```
* response 
```
std::list<payment_details> payments;
```


### `get_bulk_payments`
* request 
```
std::vector<std::string> payment_ids;
uint64_t min_block_height;
```
* response 
```
std::list<payment_details> payments;
```
### `incoming_transfers`
* request 
```
std::string transfer_type;
uint32_t account_index;
std::set<uint32_t> subaddr_indices;

```
* transfer_details
```
uint64_t amount;
bool spent;
uint64_t global_index;
std::string tx_hash;
cryptonote::subaddress_index subaddr_index;
std::string key_image;
```
* response 
```
std::list<transfer_details> transfers;

```

### `query_key`
* request 
```
std::string key_type;
```
* response 
```
std::string key;
```

### `make_integrated_address`
* request 
```
std::string standard_address;
std::string payment_id;
```
* response 
```
std::string integrated_address;
std::string payment_id;
```


### `split_integrated_address`
* request 
```
std::string integrated_address;
```
* response 
```
std::string standard_address;
std::string payment_id;
bool is_subaddress;
```


### `stop_wallet`
* request 
```
```
* response 
```
```


### `rescan_blockchain`
* request 
```
```
* response 
```
```


### `set_tx_notes`
* request 
```
std::list<std::string> txids;
std::list<std::string> notes;

```

* response 
```
```


### `get_tx_notes`
* request 
```
std::list<std::string> txids;
```
* response 
```
std::list<std::string> notes;
```


### `set_attribute`
* request 
```
std::string key;
std::string value;
```
* response 
```
```


### `get_attribute`
* request 
```
std::string key;
```
* response 
```
std::string value;
```


### `get_tx_key`
* request 
```
std::string txid;
```
* response 
```
std::string tx_key;
```


### `check_tx_key`
* request 
```
std::string txid;
std::string tx_key;
std::string address;
```
* response 
```
uint64_t received;
bool in_pool;
uint64_t confirmations;
```


### `get_tx_proof`
* request 
```
std::string txid;
std::string address;
std::string message;
```
* response
```
std::string signature;
```


### `check_tx_proof`
* request 
```
std::string txid;
std::string address;
std::string message;
std::string signature;
```
* response 
```
bool good;
uint64_t received;
bool in_pool;
uint64_t confirmations;

```
### `get_spend_proof`
* request 
```
std::string txid;
std::string message;
```
* response 
```
std::string signature;
```


### `check_spend_proof`
* request 
```
std::string txid;
std::string message;
std::string signature;
```
* response 
```
bool good;
```


### `get_reserve_proof`
* request 
```
bool all;
uint32_t account_index;     // ignored when `all` is true
uint64_t amount;            // ignored when `all` is true
std::string message;
```
* response 
```
std::string signature;
```


### `check_reserve_proof`
* request 
```
std::string address;
std::string message;
std::string signature;
```
* response 
```
bool good;
uint64_t total;
uint64_t spent;
```


### `get_transfers`
* request 
```
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
```
* transfer_entry
```
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
```
* response 
```
std::list<transfer_entry> in;
std::list<transfer_entry> out;
std::list<transfer_entry> pending;
std::list<transfer_entry> failed;
std::list<transfer_entry> pool;
```


### `get_transfer_by_txid`
* request 
```
std::string txid;
uint32_t account_index;
```
* response 
```
transfer_entry transfer;
std::list<transfer_entry> transfers;
```


### `sign`
* request 
```
std::string data;
```
* response 
```
std::string signature;
```


### `verify`
* request 
```
std::string data;
std::string address;
std::string signature;
```
* response 
```
bool good;
```


### `export_outputs`
* request 
```
```
* response 
```
std::string outputs_data_hex;
```


### `import_outputs`
* request 
```
std::string outputs_data_hex;
```
* response 
```
uint64_t num_imported;
```


### `export_key_images`
* request 
```
```
* signed_key_image 
```
std::string key_image;
std::string signature;
```
* response 
```
std::vector<signed_key_image> signed_key_images;
```


### `import_key_images`
* signed_key_image 
```
std::string key_image;
std::string signature;
```
* request 
```
std::vector<signed_key_image> signed_key_images;
```
* response 
```
uint64_t height;
uint64_t spent;
uint64_t unspent;
```

### `make_uri`

* uri_spec
```
std::string address;
std::string payment_id;
uint64_t amount;
std::string tx_description;
std::string recipient_name;
```
* request 
```
public uri_spec
```
* response 
```
std::string uri;

```
### `parse_uri`
* request 
```
std::string uri;
```
* response 
```
uri_spec uri;
std::vector<std::string> unknown_parameters;
```


### `add_address_book_entry`
* request 
```
std::string address;
std::string payment_id;
std::string description;
```
* response
```
uint64_t index;
```


### `get_address_book_entry`
* request 
```
std::list<uint64_t> entries;
```
* entry 
```
uint64_t index;
std::string address;
std::string payment_id;
std::string description;
```
* response 
```
std::vector<entry> entries;
```


### `delete_address_book_entry`
* request 
```
uint64_t index;
```
* response 
```
```


### `rescan_spent`
* request 
```
```
* response 
```
```


### `refresh`
* request 
```
uint64_t start_height;
```
* response 
```
uint64_t blocks_fetched;
bool received_money;
```


### `start_mining`
* request 
```
uint64_t    threads_count;
bool        do_background_mining;
bool        ignore_battery;
```
* response 
```
```


### `stop_mining`
* request 
```
```
* response 
```
```


### `get_languages`
* request 
```
```
* response 
```
std::vector<std::string> languages;
```


### `create_wallet`
* request 
```
std::string filename;
std::string password;
std::string language;

```
* response 
```
```


### `open_wallet`
* request 
```
std::string filename;
std::string password;
```
* response 
```
```


### `close_wallet`
* request
```
```
* response 
```
```


### `change_wallet_password`
* request 
```
std::string old_password;
std::string new_password;
```
* response 
```
```


### `generate_from_keys`
* request 
```
uint64_t restore_height;
std::string filename;
std::string address;
std::string spendkey;
std::string viewkey;
std::string password;
```
* response 
```
std::string address;
std::string info;
```


### `restore_deterministic_wallet`
* request 
```
uint64_t restore_height;
std::string filename;
std::string seed;
std::string seed_offset;
std::string password;
std::string language;
```
* response 
```
std::string address;
std::string seed;
std::string info;
bool was_deprecated;
```


### `is_multisig`
* request 
```
```
* response 
```
bool multisig;
bool ready;
uint32_t threshold;
uint32_t total;
```


### `prepare_multisig`
* request 
```
```
* response 
```
std::string multisig_info;
```


### `make_multisig`
* request
```
std::vector<std::string> multisig_info;
uint32_t threshold;
std::string password;
```
* response 
```
std::string address;
std::string multisig_info;
```


### `export_multisig`
* request 
```
```
* response 
```
std::string info;```


### `import_multisig`
* request 
```
std::vector<std::string> info;```
* response 
```
uint64_t n_outputs;
```


### `finalize_multisig`
* request 
```
std::string password;
std::vector<std::string> multisig_info;
```
* response 
```
std::string address;
```


### `exchange_multisig_keys`
* request 
```
std::string password;
std::vector<std::string> multisig_info;
```
* response 
```
std::string address;
std::string multisig_info;
```


### `sign_multisig`
* request 
```
std::string tx_data_hex;
```
* response 
```
std::string tx_data_hex;
std::list<std::string> tx_hash_list;
```


### `submit_multisig`
* request 
```
std::string tx_data_hex;
```
* response 
```
std::list<std::string> tx_hash_list;
```


### `get_version`
* request 
```
```
* response 
```
uint32_t version;
```


### `validate_address`
* request
```
std::string address;
bool any_net_type;
bool allow_openalias;

```
* response 
```
bool valid;
bool integrated;
bool subaddress;
std::string nettype;
std::string openalias_address;
```

### `set_daemon`
* request 
```
std::string address;
bool trusted;
bool ssl;
#if 0 // to be enabled when ssl support is added
std::string ssl_support; // disabled, enabled, autodetect
std::string ssl_private_key_path;
std::string ssl_certificate_path;
std::list<std::string> ssl_allowed_certificates;
std::vector<std::string> ssl_allowed_fingerprints;
bool ssl_allow_any_cert;
#endif
#if 0 // to be enabled when ssl support is added
#endif
```
* response 
```
```

### `set_log_level`
* request 
```
int8_t level;
```
* response 
```
```

### `set_log_categories`
* request 
```
std::string categories;
```
* response 
```
std::string categories;
```
