def read_in_chunks(total_size, chunk_size=1024):
    read_bytes = 0
    while read_bytes < total_size:
        current_chunk = min(chunk_size, total_size - read_bytes)
        yield 'A' * current_chunk
        read_bytes += current_chunk
print([len(chunk) for chunk in read_in_chunks(2500, 1000)])