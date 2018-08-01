def calPoints(self, ops):
    nums = []
    for op in ops:
        if op.strip('-').isdigit():
            nums.append(int(op))
        elif op == "+":
            last = nums.pop()
            last_sec = nums[-1]
            nums.append(last)
            nums.append(last + last_sec)
        elif op == "D":
            nums.append(2 * nums[-1])
        elif op == "C":
            nums.pop()
    return sum(nums)
