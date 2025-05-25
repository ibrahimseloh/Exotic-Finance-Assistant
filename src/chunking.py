def chunk_by_size(data, max_size: int)-> dict:
    chunks = []
    index = 0
    for i in range(0, len(data), max_size):
        text = data[i: i + max_size]
        chunk = {
        "chunk_id": str(index),
        "text": text,
         }
        chunks.append(chunk)
        index += 1

    return chunks