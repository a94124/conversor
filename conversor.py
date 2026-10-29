
#!/usr/bin/env python3

if __name__ == "__main__":
    print("Converter\n")
    print("(1) Unidades métricas")
    print("(2) Unidades volumétricas")

    op1 = int(input("> "))

    if op1 == 1:
        print("(1) m -> km")
        print("(2) km -> m")
        op2 = int(input("> "))

        if op2 == 1:
            x = float(input("m = "))
            print(f"km = {x / 1000}")

        elif op2 == 2:
            x = float(input("km = "))
            print(f"m = {x * 1000}")

        else:
            print("Opção incorreta")

    elif op1 == 2:
        print("Por implementar")

    else:
        print("Opção incorreta")
#comentario 2 
