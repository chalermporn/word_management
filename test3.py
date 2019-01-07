def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

# Remove duplicates from this list.
values = ["bird", "pik", "bird"]
result = remove_duplicates(values)
print(result)