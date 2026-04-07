import os

problemas = []
pos = 0
for key, value in os.environ.items():
    entry = f"{key}={value}\n"
    try:
        entry.encode('utf-8')
    except UnicodeEncodeError:
        problemas.append(key)
    pos += len(entry.encode('latin-1'))

print("Variables con caracteres problemáticos:")
for k in problemas:
    print(f"  {k} = {os.environ[k]}")

# También mostrar todas las variables cerca de posición 85
print("\nVariables en posición 85:")
pos = 0
for key, value in os.environ.items():
    entry = f"{key}={value}\n"
    entry_bytes = entry.encode('latin-1')
    if pos <= 85 < pos + len(entry_bytes):
        print(f"  {key} = {value}")
    pos += len(entry_bytes)