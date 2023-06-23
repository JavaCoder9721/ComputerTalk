class ComputerTalk:
    def __init__(self):
        self.vars = {}

    def run(self, source):
        code = source.split("\n")
        for line in code:
            if line.startswith("write "):
                text = line[6:]
                print(text,end="")
                if text in self.vars:
                    os.system("clear")
                    print(self.vars[text])
            elif line.startswith("type with a new line "):
                text = line.replace("type with a new line ","")
                print(text)
            elif line.startswith("take and write a input with "):
                msg = line[28:]
                inp = input(msg)
                print(inp)
            elif line.startswith("sum of "):
                try:
                    num1 = int(line[7:9])
                    num2 = int(line[10:])
                    print(num1 + num2)
                except ValueError:
                    print(f"please try 0{line[9:10]}")
            elif line.startswith("diff of "):
                try:
                    num1 = int(line[8:10])
                    num2 = int(line[11:])
                    print(num1 - num2)
                except ValueError:
                    print(f"please try 0{line[9:10]}")
            elif line.startswith("product of "):
                try:
                    num1 = int(line[11:13])
                    num2 = int(line[14:])
                    print(num1 * num2)
                except ValueError:
                    print(f"please try 0{line[9:10]}")
            elif line.startswith("div "):
                try:
                    num1 = int(line[4:6])
                    num2 = int(line[7:])
                    print(num1 / num2)
                except ValueError:
                    print(f"please try 0{line[6:7]}")
            elif line.startswith("define var "):
                var_name = line[9:11]
                var_value = line[12:]
                self.vars[var_name] = var_value
                # do something else
            elif line.startswith("convert into a integer "):
               try:
                   number = float(line[23:])
                   print(int(number))
               except ValueError:
                   print(f"Couldn't convert {line[25:]} into integer")
            elif line.startswith("take input and convert it into integer with msg "):
                text = line[48:]
                inp = float(input(text))
                print(f"num before: {inp}")
                print(f"num after: {int(inp)}")
            elif line.startswith("if this happend "):
                condition = line[17:]
                if condition:
                    print(True)
                else:
                    print(False)
            elif line.startswith("generate code for "):
                forwhat = line.replace("generate code for ","")
                if forwhat == "printing":
                    print("print('Content')\n\n")
                elif forwhat == "input":
                    print("input_name = input('Message')")
                    print("print(input_name)\n\n")
                elif forwhat == "convert into int":
                    print("var_name = 1.8 #you can add any value")
                    print("integername = int(name)")
                    print("print(integername)\n\n")
                elif forwhat == "use of in":
                    print("nums = [1,8,7,3] # you can add more content")
                    print("userInput = int(input('content'))")
                    print("if userInput in nums:")
                    print("   print('Content')")
                    print("else:")
                    print("   print('Content')\n\n")
                elif forwhat == "arithmetic operations":
                    print("a = 1 + 1 # sum of 1 and 1")
                    print("b = 4 - 2 # diff of 4 and 2")
                    print("c = 2 * 2 # product of 2 by 2")
                    print("d = 7 / 1 # division of 7 by 1")
                    print("print(f'{a} {b} {c} {d}') # output : 2 2 4 7\n\n")
                else:
                    raise TypeError(f"Couldnt generate code for {forwhat}")
            else:
                raise NameError(f"No token for {line}")
comp = ComputerTalk()
code = """generate code for printing
generate code for input
generate code for use of in
generate code for arithmetic operations"""
comp.run(code)