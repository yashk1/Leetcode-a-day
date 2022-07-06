### Intuition

A palindrome consists of letters with equal partners, plus possibly a unique center (without a partner). The letter i from the left has its partner i from the right. For example in 'abcba', 'aa' and 'bb' are partners, and 'c' is a unique center.

Imagine we built our palindrome. It consists of as many partnered letters as possible, plus a unique center if possible. This motivates a greedy approach.

### Algorithm

For each letter, say it occurs v times. We know we have v // 2 * 2 letters that can be partnered for sure. For example, if we have 'aaaaa', then we could have 'aaaa' partnered, which is 5 // 2 * 2 = 4 letters partnered.

At the end, if there was any v % 2 == 1, then that letter could have been a unique center. Otherwise, every letter was partnered. To perform this check, we will check for v % 2 == 1 and ans % 2 == 0, the latter meaning we haven't yet added a unique center to the answer.

