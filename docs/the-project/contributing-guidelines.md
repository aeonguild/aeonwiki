# Contributing to Aeon

Being a fork of Monero, Aeon shares most of its codebase with Monero while making a few critical modifications such
that it can offer a unique alternative to Monero. The codebase is intentionally kept close to Monero's in order to
benefit from the higher code reliability due to the larger source of peer reviewing available in Monero.

## Merging upstream patches

The above goal is achieved through the continuous effort of merging upstream improvements. Anyone with sufficient
knowledge are encouraged to contribute in this effort. In order to ensure the consistency of the changes (which greatly
helps new developers easily navigate through the commit log and cross-reference between the two repositories) as well
as to properly credit the original author, please use the `git cherry-pick` command.

It is also highly recommended to postfix the first line of the commit message with the corresponding pull request
number so that one can easily reference the original Monero PR. For example, if you are to merge the upstream PR 4356
which has two commits with the following commit messages:

    Docker android: use common prefix
    Docker android: add libsodium

then, make the corresponding commit messages as follows:

    Docker android: use common prefix /monero#4356
    Docker android: add libsodium /monero#4356

Note that the postfix is added to the first line of each commit message. Also, please make some reasonable effort to
keep the ordering of merging patches consistent with the original so that potential issues like merge conflicts etc.
are prevented, although this is not a strict requirement.

## Proposing changes

The above effort is faciliated by avoiding the creation of unnecessary differences in the repository. This implies that
**any proposed changes which also apply to Monero should be submitted to Monero.** Specifically, please send a pull
request to Monero first, then send a corresponding PR to Aeon by cherry-picking, as described above. If your Monero PR
is merged, your corresponding Aeon PR will then be merged subsequently.

If you are to propose some changes that are specific to Aeon and distinct from Monero, submit a pull request directly
to Aeon and justify your changes by laying out how they are *more* or *uniquely* applicable to Aeon. With a good
justification the burden of increased maintenance cost as described above can be overcome.


# Contributing to Monero

A good way to help is to test, and report bugs. See
[How to Report Bugs Effectively (by Simon Tatham)](https://www.chiark.greenend.org.uk/~sgtatham/bugs.html)
if you want to help that way. Testing is invaluable in making a piece
of software solid and usable.


## General guidelines

* Comments are encouraged.
* If modifying code for which Doxygen headers exist, that header must be modified to match.
* Tests would be nice to have if you're adding functionality.

Patches are preferably to be sent via a Github pull request. If that
can't be done, patches in "git format-patch" format can be sent
(eg, posted to fpaste.org with a long enough timeout and a link
posted to #monero-dev on irc.freenode.net).

Patches should be self contained. A good rule of thumb is to have
one patch per separate issue, feature, or logical change. Also, no
other changes, such as random whitespace changes or reindentation.
Following the code style of the particular chunk of code you're
modifying is encouraged. Proper squashing should be done (eg, if
you're making a buggy patch, then a later patch to fix the bug,
both patches should be merged).

If you've made random unrelated changes (either because your editor
is annoying or you made them for other reasons), you can select
what changes go into the coming commit using git add -p, which
walks you through all the changes and asks whether or not to
include this particular change. This helps create clean patches
without any irrelevant changes. git diff will show you the changes
in your tree. git diff --cached will show what is currently staged
for commit. As you add hunks with git add -p, those hunks will
"move" from the git diff output to the git diff --cached output,
so you can see clearly what your commit is going to look like.

## Commits and pull requests

Commit messages should be sensible. That means a subject line that
describes the patch, with an optional longer body that gives details,
documentation, etc.

When submitting a pull request on Github, make sure your branch is
rebased. No merge commits nor stray commits from other people in
your submitted branch, please. You may be asked to rebase if there
are conflicts (even trivially resolvable ones).

PGP signing commits is strongly encouraged. That should explain why
the previous paragraph is here.
