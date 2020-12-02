From https://aeon.herominers.com/#how-to-mine-aeon.

<div class="tab-content">


<div role="tabpanel" class="tab-pane" id="SRBMiner">
<h3><a href="https://github.com/doktor83/SRBMiner-Multi/releases" target="_blank" title="SRBMiner" rel="nofollow noopener noreferrer">SRBminer-Multi v0.5.4+ (Windows, Linux, CPU, AMD)</a></h3>

<div class="card padding-15">
<p><strong>Method 1:</strong> Run <span class="newspublished">guided_setup.bat</span> file and answer questions:</p>
<div class="stats">
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
</div>
</div>

<div class="card padding-15">
<p><strong>Method 2:</strong> Create <span class="newspublished">aeon-herominers.bat</span> file and copy / paste example below.</p>
<div class="stats">
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
</div>
</div>
</div>


<div role="tabpanel" class="tab-pane" id="XMRig-KangarooTwelve">
<h3><a href="https://github.com/stoffu/xmrig/releases" target="_blank" title="XMRig-KangarooTwelve" rel="nofollow noopener noreferrer">XMRig KangarooTwelve v1.0.0+ (Windows, Linux, CPU)</a></h3>

<div class="card padding-15">
<p>Create <span class="newspublished">aeon-herominers.cmd</span> file and copy / paste example below.</p>
<div class="stats">
<pre><code>
<strong>@echo off</strong>
<strong>xmrig.exe --donate-level 1 -o <span class="miningserver">aeon.herominers.com:10651</span> -u <span class="yourwalletaddress">YOUR_AEON_WALLET_ADDRESS</span> -p <span class="yourworkername">YOUR_WORKER_NAME</span> -a <span class="newspublished">k12</span> -k </strong>
<strong>pause</strong>
</code>
</pre>
</div>
</div>
</div>


<div role="tabpanel" class="tab-pane" id="Vulkan">
<h3><a href="https://github.com/enerc/VulkanXMRMiner/releases" target="_blank" title="Vulkan" rel="nofollow noopener noreferrer">Vulkan XMR Miner v0.4.1+ (Windows, Linux, CPU, GPU)</a></h3>

<div class="card padding-15">
<p>Create <span class="newspublished">aeon-herominers.cmd</span> file and copy / paste example below.</p>
<div class="stats">
<pre><code>
<strong>Your crypto:</strong> <span class="newspublished">2 (Aeon v7/v8)</span>
<strong>Mining pool address (hostname/IP):</strong> <span class="miningserver">aeon.herominers.com</span>
<strong>Mining pool port:</strong> <span class="miningserver">10651</span>
<strong>Your address (with optional .something at the end):</strong> <span class="yourwalletaddress">YOUR_AEON_WALLET_ADDRESS</span>
<strong>Password (or x if none):</strong> <span class="yourworkername">YOUR_WORKER_NAME</span>
<strong>Monitoring listen port (0 if no JSON/graphic console):</strong> <span class="newspublished">0</span>
</code>
</pre>
<p>Answer other questions regarding your GPU cards and mining will start.</p>
</div>
</div>
</div>



<div role="tabpanel" class="tab-pane active" id="xmr-node-proxy">
<h3><a href="https://github.com/MoneroOcean/xmr-node-proxy" target="_blank" title="xmr-node-proxy" rel="nofollow noopener noreferrer">xmr-node-proxy</a></h3>
<div class="card padding-15">
<p>Example <span class="newspublished">config.json</span></p>

<div class="stats">
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
</div>
</div>
</div>


</div>