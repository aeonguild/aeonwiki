# Software upgrades

Aeon uses a software upgrade (hard fork) mechanism to implement new features. This means that users of Aeon (end users and service providers) should run current versions and upgrade their software as needed. The required software for these upgrades will be available prior to the scheduled date. Please check the repository prior to this date for the proper Aeon software version. Below is the historical schedule and the projected schedule for the next upgrade.

Dates are provided in the format YYYY-MM-DD. 


| Software upgrade block height | Date       | Fork version | Minimum Aeon version | Recommended Aeon version | Details                                                                            |  
| ------------------------------ | -----------| ----------------- | ---------------------- | -------------------------- | ---------------------------------------------------------------------------------- |
| 592000                        | 2015-08-04 | v1 (exceptional, version not bumped)      | v0.9.0.0                 | v0.9.14.0                     | blocktime = 240 seconds, CryptoNight-Lite, lower mining priority for ringsize < 3       |
| 963500                        | 2018-06-03 | v7                | v0.12.0.0                 | v0.12.9.0-aeon                    | Rebase to Monero's latest codebase with RingCT disabled, CryptoNight-Lite variant 1, limited use of ringsize 1, ban ringsize 2   |
| 1146200                       | 2019-10-25 | v8                | v0.13.0.0-aeon            | v0.13.1.0-aeon                    | Switch to K12 PoW, reduced tx size with Borromean sigs, fixed ringsize 3, long-term block size, enforced 10 block age   |
| 1280000                       | 2020-11-11 | v9                | v0.14.1.0-aeon            | v0.14.1.0-aeon                    | Difficulty algorithm variant 9 (cut/sort removed, lag reduced to 8), change to the block median used to calculate penalty, deterministic unlock times   |


##