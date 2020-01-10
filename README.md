# chonker
Use `chonker` for optimizing the backup of large files. 
`chonker` disects large file objects into 1MB chunks and it hashes each chunk.
Each hash is then compared to a hash for the respective chunk in the previous version of the file. 
The chunk gets copied into the old file and backed up *iff* hashes differ.

## usage
```bash
./chonker input_file output_file
```
This will create `output_file` and `output_file.hashes`
