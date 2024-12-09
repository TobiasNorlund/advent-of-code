from dataclasses import dataclass

with open("sample.txt") as f:
    inp = f.read().strip()


@dataclass
class File:
    id: int
    length: int

@dataclass
class Free:
    length: int

print(inp)

fs = []

# Convert to long format
for i, c in enumerate(inp):
    if i % 2 == 0:
        # id
        fs.append(File(id=i//2, length=int(c)))
    else:
        # free space
        if (length := int(c)) > 0:
            fs.append(Free(length=length))

print(fs)

def find_first_free_space(min_length: int):
    for i, seg in enumerate(fs):
        if isinstance(seg, Free) and seg.length >= min_length:
            return i, seg
    return None

def free_file(index):
    assert isinstance(fs[index], File)

    fs.insert(index, Free(length=fs[index].length))
    del fs[index+1]
    return 0
        

# loop through all files, back to front
i = len(fs) - 1
while i > 0:
    if not isinstance(fs[i], File):
        i -= 1
        continue
    
    file = fs[i]
    
    # Find the first free space that could fit file
    res = find_first_free_space(min_length=file.length)
    if res is not None:
        first_free_idx, first_free = res
        if first_free_idx >= i:
            i -= 1
            continue

        # move file and update free space if avail
        
        #  replace free
        if first_free.length > file.length:
            i += free_file(i)
            del fs[first_free_idx]
            fs.insert(first_free_idx, file)
            fs.insert(first_free_idx+1, Free(length=first_free.length - file.length))
            i += 1
        elif first_free.length == file.length:
            i += free_file(i)
            del fs[first_free_idx]
            fs.insert(first_free_idx, file)
        else:
            # Shouldn't happen?
            raise RuntimeError("too small, shouldn't happen")
        
    i -= 1
        
print(fs)

# Convert to long format
long = []
for seg in fs:
    if isinstance(seg, File):
        long += [seg.id] * seg.length
    else:
        # free space
        long += ["."] * seg.length

print(long)

# checksum
s = 0
for i, c in enumerate(long):
    if c == ".":
        continue
    s += i * int(c)

print(s)