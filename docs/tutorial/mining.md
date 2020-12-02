[<span class="label_source"></span>](#){: .md-button }
# Mining
From [Aeon HeroMiners pool](https://aeon.herominers.com/#how-to-mine-aeon).

### [SRBminer-Multi v0.5.4+ (Windows, Linux, CPU, AMD)](https://github.com/doktor83/SRBMiner-Multi/releases)


Method 1: Run `guided_setup.bat` file and answer questions:

<pre><code>
<strong>Configuration name:</strong> <span class="newspublished">aeon-herominers</span>
<strong>Do you want to use multi algorithm mining?</strong> <span class="newspublished">n</span> or y (optional)
<strong>Enter algorithm 0 name:</strong> <span class="newspublished">k12</span>
<strong>Address and port of mining pool:</strong> <span class="miningserver">aeon.herominers.com:10651</span>
<strong>Wallet address:</strong> <span class="yourwalletaddress">YOUR_AEON_WALLET_ADDRESS</span>
<strong>Password:</strong> <span class="yourworkername">YOUR_WORKER_NAME</span>
<strong>Do you want to use your CPU for mining algorithm 0 ?</strong> <span class="newspublished">n</span> or y (optional)
<strong>Do you want to enable logging?</strong> <span class="newspublished">n</span> or y (optional)
<strong>Do you want to enable compute mode?</strong> <span class="newspublished">y</span> or n (optional)
</code>
</pre>

Method 2: Create `aeon-herominers.bat` file and copy / paste example below.
<pre><code>
<strong>setx GPU_MAX_HEAP_SIZE 100</strong>	
<strong>setx GPU_MAX_USE_SYNC_OBJECTS 1</strong>	
<strong>setx GPU_SINGLE_ALLOC_PERCENT 100</strong>	
<strong>setx GPU_MAX_ALLOC_PERCENT 100</strong>	
<strong>setx GPU_MAX_SINGLE_ALLOC_PERCENT 100</strong>	
<strong>setx GPU_ENABLE_LARGE_ALLOCATION 100</strong>
<strong>setx GPU_MAX_WORKGROUP_SIZE 1024</strong>

<strong>@echo off</strong>
<strong>cd %~dp0</strong>
<strong>cls</strong>

<strong>SRBMiner-MULTI.exe --algorithm <span class="newspublished">k12</span> --pool <span class="miningserver">aeon.herominers.com:10651</span> --wallet <span class="yourwalletaddress">YOUR_AEON_WALLET_ADDRESS</span> --password <span class="yourworkername">YOUR_WORKER_NAME</span></strong>
<strong>pause</strong>
</code>
</pre>


### [XMRig KangarooTwelve v1.0.0+ (Windows, Linux, CPU)](https://github.com/stoffu/xmrig/releases)

Create  `aeon-herominers.cmd` file and copy / paste example below.
<pre><code>
<strong>@echo off</strong>
<strong>xmrig.exe --donate-level 1 -o <span class="miningserver">aeon.herominers.com:10651</span> -u <span class="yourwalletaddress">YOUR_AEON_WALLET_ADDRESS</span> -p <span class="yourworkername">YOUR_WORKER_NAME</span> -a <span class="newspublished">k12</span> -k </strong>
<strong>pause</strong>
</code>
</pre>
  


### [Vulkan XMR Miner v0.4.1+ (Windows, Linux, CPU, GPU)](https://github.com/enerc/VulkanXMRMiner/releases)

Create `aeon-herominers.cmd` file and copy / paste example below.
<pre><code>
<strong>Your crypto:</strong> <span class="newspublished">2 (Aeon v7/v8)</span>
<strong>Mining pool address (hostname/IP):</strong> <span class="miningserver">aeon.herominers.com</span>
<strong>Mining pool port:</strong> <span class="miningserver">10651</span>
<strong>Your address (with optional .something at the end):</strong> <span class="yourwalletaddress">YOUR_AEON_WALLET_ADDRESS</span>
<strong>Password (or x if none):</strong> <span class="yourworkername">YOUR_WORKER_NAME</span>
<strong>Monitoring listen port (0 if no JSON/graphic console):</strong> <span class="newspublished">0</span>
</code>
</pre>
Answer other questions regarding your GPU cards and mining will start.


### [xmr-node-proxy](https://github.com/MoneroOcean/xmr-node-proxy)

Example `config.json`.

<pre><code>	
"pools": [
{
"hostname": "<span class="miningserver">aeon.herominers.com</span>",
"port":<span class="miningserver">10651,</span>
"ssl": false,
"allowSelfSignedSSL": false,
"share": 100,
"username": "<span class="yourwalletaddress">YOUR_AEON_WALLET_ADDRESS</span>",
"password": "<span class="yourworkername">YOUR_WORKER_NAME</span>",
"keepAlive": true,
"algo": "<span class="newspublished">k12</span>",
"blob_type": "<span class="newspublished">aeon</span>",
"default": true
}
],
</code>
</pre>
