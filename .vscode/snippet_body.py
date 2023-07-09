lines = []

while True:
    try:
        s = input()
        lines.append(f"\"{s}\"")
    except KeyboardInterrupt:
        break

print()
print("-" * 20)
print(",\n".join(lines))
