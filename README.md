# jpeg-hash-spoofing
#python3 jpeg-hash-spoofing.py <target_hash> <original_image_path> <altered_image_path>

This program helps you manipulate a jpeg image SHA-512 to match a target hash. By modifying the least significant bytes of an image like metadata to ensure the image face remains the same. The program works by adding modyfying comments section of jpeg image. This tool should be used for learning purposes only.

Initializing Program:
Environment:
This is program is written using Python3 as the programming languange. It requires Python3 environmet to run which can be installed from official webpage (https://www.python.org/downloads/).
Required libraries: sys, hashlib and struct which come bundled with Python and does not require installation.
For the case of a library error install: pip get-install sys hashlib struct

Running:
Arguments must be parsed in the commandline for the program to run successfully.
First argument is the target hash, e.g. 2af673s
Second argument is the original image path, e.g. /home/pictures/original.jpg
Third argument is the path\ to save the new altered image. eg /home/pictures/altered.jpg

python3 jpeg-hash-spoofing.py <target_hash> <original_image_path> <altered_image_path>
Example: python3 jpeg-hashspoofing.py 2448a6 /home/pictures/original.jpg /home/pictures/altered.jpg

Flexible-Progressive Approach:
This solution uses two apporaches, Flexible approach and Progressive locking approach. Whenever a partial match for any character at any position is found, whether it is the first character or any other part of the target hash, that part of the hash match is locked and then focus on finding the remaining unmatched characters. Progressively we only modify the remaining unmatched parts of the hash to avoid unnecessary modifications to already matched parts of the hash.

Faster Convergence:
By locking each segment of the hash independently, reduces the number of trials/loops needed to match the entire target hash, especially when larger sections are martched early on. A list "matched_positions", keeps track of parts of the hash we've already matched.

Steps for the Approach:
  1. Start with the Full Hash: We match any part of the target hash.

  2. Partial Hash Matching: If you match any character of the target hash, then you lock that position and focus on the remaining unmatched characters.

  3. Iterate: Keep iterating through possible changes to the metadata, and each match to a part of the hash, it's locked in and move on to the next part.

  4. Stop When Full Match is Achieved.

Advantages of This Approach:
  1. Flexibility: No need to match the target hash sequentially. As soon as any part of the hash matches, it is locked and focus on the rest.

  2. Potential Faster Convergence: By locking individual matches we minimizing unnecessary modifications and narrowing the search space dynamically.

  3. Smarter Progression: The search is not locked to sequential parts. Matching the 5th character first, it is locked and search continues for other characters.

  4. Time Efficiency:
     (i) Faster Convergence: This method could drastically reduce the total time needed, especially if matches for the target hash are found early on or if the match is dispersed across the hash.

      (ii) Reduced Redundancy: The approach minimizes redundant attempts by locking parts of the hash progressively, allowing the search to converge on the desired target more quickly.
