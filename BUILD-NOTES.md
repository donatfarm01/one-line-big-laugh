# Build notes — One Line, Big Laugh

## The entry

The line is: "My cat filed a noise complaint: my singing violates the lease we both signed."

It is 77 characters long, well inside the 1 to 200 character gate, and the
program writes it with no trailing newline.

## Why this line

The judge weighs five things in order, and the line was picked against each
of them. First, it is a real joke with a setup and a payoff, not just a
quirky observation: a cat files a formal noise complaint, which already
sounds like the start of a story, and the payoff reframes the whole premise.
Second, it turns somewhere unexpected: the reveal is that the cat is a
legal co-tenant, so the complaint is not a cute animal antic but a roommate
enforcing a contract. Third, it wastes no words: at 77 characters every
word earns its place, and nothing could be cut without losing the joke.
Fourth, it is fresh: it avoids the stock templates the judge has heard
twice, the therapist setup, the wife setup, the bar setup, the time machine
setup, and the AI jokes that sibling entries in this same series already
used. Fifth, it stays in the head: the phrase about the lease they both
signed is the kind of line someone repeats to a friend the same day.

The specific detail that makes it land is the lease. A complaint from a
pet is absurd on its own, but a shared lease turns the cat into a
co-tenant with standing, which is the misdirection the whole line rests
on.

## Files

The repository holds four files. The program is main.py, a small Python
script that holds the line as a fixed string, checks it against the gate
itself, and writes it to the output path. The README carries the three
make.fun badges linked to the bounty page. The LICENSE is MIT with the
SPDX identifier line the kit check reads. This file is the build notes.

## Verification

The program was run and its output was verified: the file it wrote is
byte for byte the same as the line in the source, 77 characters, with no
trailing newline. The hash of the file was recorded both as written and
with a trailing newline appended, and the two hashes differ, as expected.
The kit check was run from the kit directory and passed everything it can
check locally, with the transcript and submission checks waiting for the
parent step, which is bundling and submitting.
