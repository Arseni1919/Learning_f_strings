text = 'Hello!'
print(f"{text:-^20}")

x = 55
print(f'number {x:x}')

total = 123456.99

# Formatting values
width = 30
align = ">"
fill = "."
precision = 2
sep = ","

print(f"Total{total:{fill}{align}{width}{sep}.{precision}f}")