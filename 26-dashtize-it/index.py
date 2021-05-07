def dashatize(nums):

    if nums == None:
        return 'None'
    if nums < 0:
        nums = abs(nums)

    dashtize_nums = ""

    digits = list(str(nums))

    for digit in digits:
        if int(digit) % 2 == 1:
            dashtize_nums += "-" + digit + "-"
        else:
            dashtize_nums += digit
    if dashtize_nums[0] == "-":
        dashtize_nums = dashtize_nums[1:]
    if dashtize_nums[-1] == "-":
        dashtize_nums = dashtize_nums[:-1]
    
    dashtize_nums = dashtize_nums.replace("--", "-")

    
    return dashtize_nums


print(dashatize(274))
print(dashatize(5311))
print(dashatize(86320))
print(dashatize(974302))