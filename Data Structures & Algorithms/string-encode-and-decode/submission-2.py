class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f'{len(s)}#'+s
        
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        cursor = 0

        while cursor < len(s):
            # Step 1: read the number before '#'
            length_end = cursor

            while s[length_end] != '#':
                length_end += 1
            
            string_length = int(s[cursor:length_end])

            # Step 2: skip '#'
            start = length_end + 1

            # Step 3: read exactly `length` characters
            decoded_word = s[start:start + string_length]
            decoded.append(decoded_word)

            # Step 4: move cursor to next encoded item
            cursor = start + string_length

        return decoded

"""
1. Input / return?
encode() takes List[str] and returns one string.
decode() takes that string and must return the original List[str].
Goal: decode(encode(strs)) == strs.

2. Constraints / complexity?
<100 strings, each <200 chars, any ASCII char.
Total size T is small, about <20,000 chars.
O(T) time and O(T) space are fine and optimal.

3. Simplest brute force?
Join with a delimiter, then split on that delimiter.
Example: "#".join(strs), then s.split("#").

4. What is wrong with brute force?
It loses information.
If a string contains "#", decode cannot tell separator vs real data.

5. What pattern does that suggest?
Lossless serialization / cursor parsing.
Use length-prefix encoding: "<length>#<string>".

6. Edge cases?
[], [""], ["", ""], strings containing "#", digits, spaces, newlines, arbitrary ASCII, multi-digit lengths.
"""