[<span class="label_source"></span>](#){: .md-button }
# Wallet CLI

## Usage

  `./aeon-wallet-cli [options] [commands]`

## Description
This is the command line Aeon wallet. It is a tool to manage aeon
transfers and addresses. It needs to connect to an Aeon daemon to 
work correctly.

## Commands

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `account`

`account`

Shows all the existing accounts along with their balances.

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `account new`

`account new <label text with white spaces allowed>`

Creates a new account with its label initialized by the provided label text (which can be empty).

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }

### `account switch`
`account switch <index>`

Switches to the account specified by `<index>`.
  
---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `account label`
`account label <index> <label text with white spaces allowed>`

Sets the label of the account specified by <index> to the provided label text.
  
---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `account tag`
`account tag <tag_name> <account_index_1> [<account_index_2> ...]`

A tag `<tag_name>` is assigned to the specified accounts `<account_index_1>`, `<account_index_2>`, ....

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `account untag`
`account untag <account_index_1> [<account_index_2> ...]`

The tags assigned to the specified accounts `<account_index_1>`, `<account_index_2>` ..., are removed.

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `account tag_description`
`account tag_description <tag_name> <description>`

The tag `<tag_name>` is assigned an arbitrary text `<description>`.


---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `address`
`address (<index_min> [<index_max>]|all)`

  Shows the default or specified address.

---
[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `address new`
`address new <label text with white spaces allowed>`

Creates a new address with the provided label text (which can be empty).

---
[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `address label`
`address label <index> <label text with white spaces allowed>`

Sets the label of the address specified by `<index>` to the provided label text.

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `address_book`

`address_book`

Print all saved addresses in local storage.

```
>>> address_book
address_book
Index: 0
Address: WmsBWTyNwnbDwjkU1LDTNRaeYK2XNASvHFfHxxxxxxxxxS74f8q3CVwL3RigWN7WTFaFQg6k3SWUFdn2SSaZuidZ2UAyQ9yVo
Payment ID: <0000000000000000000000000000000000000000000000000000000000000000>
Description: test

Index: 1
Address: WmsBWTyNwnbDwjkU1LDTNRaeYK2XNASvHFfHxxxxxxxxxS74f8q3CVwL3RigWN7WTFaFQg6k3SWUFdn2SSaZuidZ2UAyQ9yVo
Payment ID: <0000000000000000000000000000000000000000000000000000000000000000>
Description: test
```

---
[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `address_book add`

`address_book add ((<address> [pid <id>])|<integrated address>) [<description possibly with whitespaces>]`

Add an address to the local address book.

```
>>> address_book add WmsBWTyNwnbDwjkU1LDTNRaeYK2XNASvHFfHxxxxxxxxxS74f8q3CVwL3RigWN7WTFaFQg6k3SWUFdn2SSaZuidZ2UAyQ9yVo test
Index: 0
Address: WmsBWTyNwnbDwjkU1LDTNRaeYK2XNASvHFfHcYcQgVsqPS74f8q3CVwL3RigWN7WTFaFQg6k3SWUFdn2SSaZuidZ2UAyQ9yVo
Payment ID: <0000000000000000000000000000000000000000000000000000000000000000>
Description: test
```
---
[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `address_book delete`
`address_book delete <index>`

Delete address at `<index>`.

```
>>>  address_book delete 1
```
---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `balance`
`balance [detail]`

Show the wallet's balance of the currently selected account.

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `bc_height`

`bc_height`

Prints the connected daemon's height.

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `check_reserve_proof`

`check_reserve_proof <address> <signature_file> [<message>]`

Check a signature proving that the owner of `<address>` holds at least this much, optionally with a challenge string `<message>`.
  
---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `check_spend_proof`
`check_spend_proof <txid> <signature_file> [<message>]`

Check a signature proving that the signer generated `<txid>`, optionally with a challenge string `<message>`.

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `check_tx_key`
`check_tx_key <txid> <txkey> <address>`

Check the amount going to `<address>` in `<txid>`.

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `check_tx_proof`
`check_tx_proof <txid> <address> <signature_file> [<message>]`

Check the proof for funds going to `<address>` in `<txid>` with the challenge string `<message>` if any.


---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `donate`
`donate [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] <amount> [<payment_id>]`

Donate `<amount>` to the development team (`donate.aeon.cash`).
  
---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `encrypted_seed`

`encrypted_seed`

Display the encrypted Electrum-style mnemonic seed.

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `exchange_multisig_keys `

`exchange_multisig_keys <string> [<string>...]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `export_key_images`
` <file>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `export_multisig_info `
`<filename>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `export_outputs`
` <file>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `export_raw_multisig_tx `
`<filename>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `export_transfers`
` [in|out|all|pending|failed|coinbase] [index=<N1>[,<N2>,...]] [<min_height> [<max_height>]] [output=<filepath>]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `finalize_multisig`
`<string> [<string>...]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `get_description`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `get_reserve_proof `
`(all|<amount>) [<message>]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `get_spend_proof`
` <txid> [<message>]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `get_tx_key `
`<txid>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `get_tx_note `
`<txid>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `get_tx_proof `
`<txid> <address> [<message>]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `help `
`[<command>]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `import_key_images`
` <file>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `import_multisig_info`
` <filename> [<filename>...]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `import_outputs`
` <file>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `incoming_transfers`
` [available|unavailable] [verbose] [index=<N1>[,<N2>[,...]]]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `integrated_address`
` [<payment_id> | <address>]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `is_output_spent`
` <amount>/<offset>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `locked_sweep_all`
` [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] <address> <lockblocks> [<payment_id>]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `locked_transfer`
` [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] (<URI> | <addr> <amount>) <lockblocks> [<payment_id>]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `make_multisig`
` <threshold> <string1> [<string>...]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `mark_output_spent`
` <amount>/<offset> | <filename> [add]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `mark_output_unspent`
` <amount>/<offset>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `password`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `payment_id`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `payments`
` <PID_1> [<PID_2> ... <PID_N>]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `prepare_multisig`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `print_ring`
` <key_image> | <txid>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `refresh`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `rescan_bc`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `rescan_spent`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `save`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `save_bc`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `save_known_rings`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `save_watch_only`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `seed`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `set`
` <option> [<value>]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `set_daemon`
` <host>[:<port>] [trusted|untrusted]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `set_description`
` [free text note]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `set_log`
` <level>|{+,-,}<categories>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `set_ring`
` <filename> | ( <key_image> absolute|relative <index> [<index>...] )`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `set_tx_key`
` <txid> <tx_key>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `set_tx_note`
` <txid> [free text note]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `show_transfer`
` <txid>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `show_transfers`
` [in|out|pending|failed|pool|coinbase] [index=<N1>[,<N2>,...]] [<min_height> [<max_height>]]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `sign`
` <file>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `sign_multisig`
` <filename>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `sign_transfer`
` [export_raw]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `spendkey`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `start_mining`
` [<number_of_threads>] [bg_mining] [ignore_battery]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `status`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `stop_mining`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `submit_multisig`
` <filename>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `submit_transfer`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `sweep_all`
` [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] <address> [<payment_id>]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `sweep_below `
`<amount_threshold> [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] <address> [<payment_id>]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `sweep_single`
` [<priority>] [<ring_size>] <key_image> <address> [<payment_id>]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `sweep_unmixable`
### `transfer`
` [index=<N1>[,<N2>,...]] [<priority>] [<ring_size>] (<URI> | <address> <amount>) [<payment_id>]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `unspent_outputs`
` [index=<N1>[,<N2>,...]] [<min_amount> [<max_amount>]]`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `verify`
` <filename> <address> <signature>`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `version`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `viewkey`

---

[<span class="label"></span>](https://github.com/ivoryguru/aeondocs/issues/new?labels=question){: .md-button }
### `wallet_info`

---


