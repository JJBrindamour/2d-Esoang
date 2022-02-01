def parse(file):
  lines = []
  currLine = []
  with open(file, 'r') as f:
    for char in f.read():
      if char != '\n': 
        currLine.append(char)
      else:
        lines.append(currLine)
        currLine = []
  if currLine != []: lines.append(currLine)
  return lines

def fmt(lines):
  longestLineLen = 0
  for line in lines:
    if len(line) > longestLineLen: longestLineLen = len(line)

  for line in lines:
    while len(line) < longestLineLen:
      line.append(" ")
  return lines

def exe(lines):
  def doStack(v, stack):
    if v == "+": # Add top 2 nums
      n = stack[-2] + stack[-1]
      stack.pop(-1)
      stack.pop(-1)
      stack.append(n)
    elif v == "-": # Subtract top 2 nums
      n = stack[-2] - stack[-1]
      stack.pop(-1)
      stack.pop(-1)
      stack.append(n)
    elif v == "*": # Multiply top 2 nums
      n = stack[-2] * stack[-1]
      stack.pop(-1)
      stack.pop(-1)
      stack.append(n)
    elif v == "/": # Divide top 2 nums
      n = stack[-2] / stack[-1]
      stack.pop(-1)
      stack.pop(-1)
      stack.append(n)
    elif v == "%": # Mod top 2 nums
      n = stack[-2] % stack[-1]
      stack.pop(-1)
      stack.pop(-1)
      stack.append(n)
    elif v == "c": # Print ASCII Char of top num
      print(chr(stack[-1]))
    elif v == "n": # Print top num
      print(stack[-1])
    elif v == ",": # Add ASCII Code of input onto the Stack
      stack.append(ord(input()[0]))
    elif v == ":": # Duplicate the top number onto the Stack
      stack.append(stack[-1])
    elif v in "1234567890": # Add typed number onto the Stack
      stack.append(int(v))
    elif v == "&": # Int of the String Concatenation of the top 2 nums
      n = int(str(stack[-2]) + str(stack[-1]))
      stack.pop(-1)
      stack.pop(-1)
      stack.append(n)
    elif v == "\\": # Switch the data stored at the index of the top 2 nums and remove the top 2 nums
      stack[stack[-2]], stack[stack[-1]] = stack[stack[-1]], stack[stack[-2]]
      stack.pop(-1)
      stack.pop(-1)
    elif v == "|": # Switch the data stored at the index of the top 2 nums
      stack[stack[-2]], stack[stack[-1]] = stack[stack[-1]], stack[stack[-2]]

    return stack

  def doDir(v):
    if v == "<": return "-x"
    elif v == ">": return "+x"
    elif v == "^": return "+y"
    elif v == "v": return "-y"
    else: print(v)

  stack = []
  moveDir = "+x"
  coord = [0, 0]
  loop = True
  while loop:
    try:
      val = lines[coord[0]][coord[1]]
      if val != "!" or val != "!" and val != "?" and stack[-1] != 0:
        if val not in "<>^v": stack = doStack(val, stack)
        else: moveDir = doDir(val)

        if moveDir == "+x": coord[1] += 1
        elif moveDir == "-x": coord[1] -= 1
        elif moveDir == "+y": coord[0] -= 1
        elif moveDir == "-y": coord[0] += 1
      elif val == "?":
        if moveDir == "+x": coord[1] += 2
        elif moveDir == "-x": coord[1] -= 2
        elif moveDir == "+y": coord[0] -= 2
        elif moveDir == "-y": coord[0] += 2
      elif coord[0] != abs(coord[0]) or coord[1] != abs(coord[1]): loop = False
      else: loop = False
    except IndexError:
      print("Index Error")
      loop = False

exe(fmt(parse("ex.td")))
