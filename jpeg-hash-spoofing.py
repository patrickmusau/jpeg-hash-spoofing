import sys
import hashlib
import struct

def calculate_sha512(file_path):
    #Calculate the SHA-512 hash of a file
    sha_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha_hash.update(chunk)
    return sha_hash.hexdigest()


def add_comment_to_jpeg(jpeg_data, comment):
    #Add a comment to the JPEG file (using APP0 or APP1 marker)."""
    # Create the comment segment (JPEG format)
    comment_bytes = comment.encode('ascii')
    length = len(comment_bytes) + 2  
    marker = b'\xFF\xFE'                # marker for comment
    app0_segment = struct.pack('>H', length) + marker + comment_bytes

    # Append the comment to the original JPEG data
    return jpeg_data + app0_segment

def alt_hash(target_hash, original_image_path, altered_image_path):
    #Modifying the JPEG image hash to match the target_hash
    with open(original_image_path, 'rb') as f:
        original_data = f.read()

    # Add to the file data until the hash matches the target hash
    attempt_data = bytearray(original_data)
    target_hash_lower = target_hash.lower()

    # Track matched positions in the target hash
    matched_positions = [False] * len(target_hash)

    iteration = 0
    while True:
        # Try modifying the metadata and checking the hash
        comment = f"spoof_comment_{iteration}"
        
        # Add/modify the comment in the JPEG file
        altered_data = add_comment_to_jpeg(attempt_data, comment)

        # Write the modified data to the altered image path
        with open(altered_image_path, 'wb') as f:
            f.write(altered_data)

        # Calculate the hash of the altered image
        altered_hash = calculate_sha512(altered_image_path)

        # Check for matches at any position
        for i in range(len(target_hash)):
            if not matched_positions[i] and altered_hash.startswith(target_hash_lower[:i+1]):
                matched_positions[i] = True
                print(f"Matched {target_hash[i]} at position {i} in {altered_hash}")
        
        # If all positions are matched, we're done
        if all(matched_positions):
            print(f"Final matched hash: {altered_hash}")
            print(f"Altered image saved as {altered_image_path}")

            break

        iteration += 1

def main():
    #Read command line arguments
    target_hash = sys.argv[1]               #"2448a6512f"
    original_image_path = sys.argv[2]       #"original.jpg"
    altered_image_path = sys.argv[3]        #"altered.jpg"
    
    alt_hash(target_hash, original_image_path, altered_image_path)

if __name__ == "__main__":
    main()      #Initializing the program using OOP approach