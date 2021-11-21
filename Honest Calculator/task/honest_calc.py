# write your code here
def right(value):
    return value.replace(".", "").isdigit()


def is_one_digit(value: float):
    if int(value) == value:
        if -10 < int(value) < 10:
            return True
    return False


msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
M = 0

while True:
    msg = ""
    result = None
    print(msg_0)
    content = input()
    content = content.replace("M", str(M))
    content_list = content.split()

    if right(content_list[0]) and right(content_list[2]):
        if content_list[1] in ["+", "-", "*", "/"]:
            x = content_list[1]
            a = float(content_list[0])
            b = float(content_list[-1])
            if is_one_digit(a) and is_one_digit(b):
                msg += msg_6
            if a == 1 or b == 1 and x == '*':
                msg += msg_7
            if a == 0 or b == 0:
                if x in ["+", "-", "*"]:
                    msg += msg_8

            if x == '+':
                result = a + b
            elif x == '-':
                if a == 0 or b == 0:
                    print(msg_9 + msg_8)
                result = a - b
            elif x == '*':
                result = a * b
            elif x == "/":
                if content_list[2] != '0':
                    result = a / b
                else:
                    print(msg_9 + msg_6)
                    print(msg_3)
                    continue
            if result is not None:
                if msg:
                    print(msg_9 + msg)
                print(result)
                print(msg_4)
                if input() == "y":
                    if is_one_digit(result):
                        msg_index = 10
                        while msg_index < 13:
                            print(eval(f"msg_{msg_index}"))
                            if input() == "y":
                                msg_index += 1
                            else:
                                break
                        else:
                            M = result
                    else:
                        M = result
            print(msg_5)
            if input() == "y":
                continue
            else:
                break

        else:
            print(msg_2)
    else:
        print(msg_1)
