prompt = input("Expression: ").lower().strip()
x, y, z = prompt.split(" ")
x = float(x)
z = float(z)
def calculate(x,y,z):
    match y:
        case "/":
            return x / z
        case "*":
            return x * z
        case "+":
            return x + z
        case "-":
            return x - z
        case _:
            return None
result = calculate(x,y,z)
print(f"{result:.1f}")
