import sys
import os
import hashlib

_, in_file, out_file  = sys.argv

# open file, read contents in binary, chonk it up into 1MB chunks
def chonker(in_file, out_file):
    old_hash_file = out_file + ".hashes"
    new_hash_file = out_file + ".hashes.temp"
    # check if exists else create out_file and old_hashes
    if not os.path.exists(old_hash_file):
        with open(old_hash_file, 'wb') as f:
            pass
    if not os.path.exists(out_file):
        with open(out_file, 'wb') as f:
            pass


    # opening all them files
    with open(in_file, 'rb') as f_in:
        with open(out_file, 'r+b') as f_out:
            with open(old_hash_file, 'rb') as g_old:
                with open(new_hash_file, 'wb') as g_new:
                    while True:
                        digest_old = g_old.read(32)

                        chunk_start = f_in.tell()
                        # current chunk size is: 1 MB
                        chunk = f_in.read(10**6)
                        # if no more in_file
                        if not chunk:
                            # ensure files are of the same size
                            f_in_end = f_in.tell()    
                            f_out.truncate(f_in_end)
                            break

                        # creating a hash for chunk
                        digest = hashlib.sha256(chunk).digest()
                        # writing into new has file
                        g_new.write(digest)

                        if digest != digest_old:
                            f_out.seek(chunk_start)
                            f_out.write(chunk)

    os.rename(new_hash_file, old_hash_file)

if __name__ == '__main__':
    chonker(in_file, out_file)