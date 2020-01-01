# chonker
Use for optimizing backup of large files. Disect large file into 1MB chunks and hash each chunk. Each hash is then compared to a hash for the respective chunk in the previous version of the file. Chunk gets copied into the old file and backed up iff hashes differ.
