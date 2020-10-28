# Wallet CLI

## Usage

  `./aeon-wallet-cli [options] [commands]`

## Description
This is the command line Aeon wallet. It is a tool to manage aeon
transfers and addresses. It needs to connect to an Aeon daemon to 
work correctly.

## Commands

### `account`
### `account new`
` <label text with white spaces allowed>`
### `account switch `
`<index>`
### `account label `
`<index> <label text with white spaces allowed>`
### `account tag `
`<tag_name> <account_index_1> [<account_index_2> ...]`
### `account untag `
`<account_index_1> [<account_index_2> ...]`
### `account tag_description `
`<tag_name> <description>`
### `address `
`[ new <label text with white spaces allowed> | all | <index_min> [<index_max>] | label <index> <label text with white spaces allowed>]`
### `address_book `
`[(add ((<address> [pid <id>])|<integrated address>) [<description possibly with whitespaces>])|(delete <index>)]`
### `balance`
`[detail]`
### `bc_height`
### `check_reserve_proof`
`<address> <signature_file> [<message>]`
### `check_spend_proof `
`<txid> <signature_file> [<message>]`
### `check_tx_key `
`<txid> <txkey> <address>`
### `check_tx_proof `
`<txid> <address> <signature_file> [<message>]`
### `donate `
`[index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] <amount> [<payment_id>]`
### `encrypted_seed`
### `exchange_multisig_keys `
`<string> [<string>...]`
### `export_key_images`
` <file>`
### `export_multisig_info `
`<filename>`
### `export_outputs`
` <file>`
### `export_raw_multisig_tx `
`<filename>`
### `export_transfers`
` [in|out|all|pending|failed|coinbase] [index=<N1>[,<N2>,...]] [<min_height> [<max_height>]] [output=<filepath>]`
### `finalize_multisig`
`<string> [<string>...]`
### `get_description`
### `get_reserve_proof `
`(all|<amount>) [<message>]`
### `get_spend_proof`
` <txid> [<message>]`
### `get_tx_key `
`<txid>`
### `get_tx_note `
`<txid>`
### `get_tx_proof `
`<txid> <address> [<message>]`
### `help `
`[<command>]`
### `import_key_images`
` <file>`
### `import_multisig_info`
` <filename> [<filename>...]`
### `import_outputs`
` <file>`
### `incoming_transfers`
` [available|unavailable] [verbose] [index=<N1>[,<N2>[,...]]]`
### `integrated_address`
` [<payment_id> | <address>]`
### `is_output_spent`
` <amount>/<offset>`
### `locked_sweep_all`
` [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] <address> <lockblocks> [<payment_id>]`
### `locked_transfer`
` [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] (<URI> | <addr> <amount>) <lockblocks> [<payment_id>]`
### `make_multisig`
` <threshold> <string1> [<string>...]`
### `mark_output_spent`
` <amount>/<offset> | <filename> [add]`
### `mark_output_unspent`
` <amount>/<offset>`
### `password`
### `payment_id`
### `payments`
` <PID_1> [<PID_2> ... <PID_N>]`
### `prepare_multisig`
### `print_ring`
` <key_image> | <txid>`
### `refresh`
### `rescan_bc`
### `rescan_spent`
### `save`
### `save_bc`
### `save_known_rings`
### `save_watch_only`
### `seed`
### `set`
` <option> [<value>]`
### `set_daemon`
` <host>[:<port>] [trusted|untrusted]`
### `set_description`
` [free text note]`
### `set_log`
` <level>|{+,-,}<categories>`
### `set_ring`
` <filename> | ( <key_image> absolute|relative <index> [<index>...] )`
### `set_tx_key`
` <txid> <tx_key>`
### `set_tx_note`
` <txid> [free text note]`
### `show_transfer`
` <txid>`
### `show_transfers`
` [in|out|pending|failed|pool|coinbase] [index=<N1>[,<N2>,...]] [<min_height> [<max_height>]]`
### `sign`
` <file>`
### `sign_multisig`
` <filename>`
### `sign_transfer`
` [export_raw]`
### `spendkey`
### `start_mining`
` [<number_of_threads>] [bg_mining] [ignore_battery]`
### `status`
### `stop_mining`
### `submit_multisig`
` <filename>`
### `submit_transfer`
### `sweep_all`
` [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] <address> [<payment_id>]`
### `sweep_below `
`<amount_threshold> [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] <address> [<payment_id>]`
### `sweep_single`
` [<priority>] [<ring_size>] <key_image> <address> [<payment_id>]`
### `sweep_unmixable`
### `transfer`
` [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] (<URI> | <address> <amount>) [<payment_id>]`
### `unspent_outputs`
` [index=<N1>[,<N2>,...]] [<min_amount> [<max_amount>]]`
### `verify`
` <filename> <address> <signature>`
### `version`
### `viewkey`
### `wallet_info`


