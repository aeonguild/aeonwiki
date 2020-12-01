# Features

<ul class="banner-list">
  <li><i class="fa fa-check"></i><em>PoW algorithm:</em> KangarooTwelve</li>
  <li><i class="fa fa-check"></i><em>Max supply:</em> ~18.4 million</li>
  <li><i class="fa fa-check"></i><em>Block reward:</em> smoothly decreasing</li>
  <li><i class="fa fa-check"></i><em>Block time:</em> 240 seconds</li>
  <li><i class="fa fa-check"></i><em>Difficulty:</em> retargets at every block</li>
</ul>
<ul class="steps-list">
  <li>
    <h4>ASIC-friendly proof-of-work</h4>
    <p>We believe ASIC resistance is ultimately futile while imposing various forms of undesirable cost. Our ASIC-friendly PoW (KangarooTwelve) allows for faster verification of the blockchain. This also helps stabilize the protocol as the need for PoW-change hard forks is eliminated.</p>
  </li>
  <li>
    <h4>No use of RingCT</h4>
    <p>Monero's RingCT for encrypting transaction amounts comes with a theoretical risk of catastrophic collapse of the monetary system due to hidden inflation if the discrete log of the second generator is discovered. Favoring supply soundness over privacy, we choose not to use RingCT until cryptographers invent an efficient commitment scheme with unconditional soundness. We believe practical level of privacy can still be achieved without RingCT. Not using RingCT also contributes to faster syncing.</p>
  </li>
  <li>
    <h4>Smaller Blockchain</h4>
    <p>AEON's block time is 4 minutes. This halves the number of blocks produced each day compared to Monero, further reducing the cost of running a node.</p>
  </li>
  <li>
    <h4>Smaller ring size</h4>
    <p>AEON's ring size is fixed to 3 which is the bare minimum needed to prevent chain reactions (<a href="https://lab.getmonero.org/pubs/MRL-0001.pdf">link</a>). Monero's higher ring size means more degree of obfuscation for each transaction, but it also comes at the cost of increased blockchain size and longer verification time. We choose to stick with ring size 3 until a convincing evidence against it is found.</p>
  </li>
</ul>
##