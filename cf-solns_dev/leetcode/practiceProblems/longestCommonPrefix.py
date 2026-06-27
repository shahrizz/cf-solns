strs = ["flower", "flow", "flight"]
common = strs[0]
i = 0

while i < (len(strs)):
    if strs[i].startswith(common):
        i += 1
    else:
        common = common[:-1]

return common
