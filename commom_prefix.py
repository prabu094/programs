def longestCommonPrefix(strs):
    # generate column-wise slicing
    column_slices, common_prefix = zip(*strs), ''

    for current_column in column_slices:

        if len(set(current_column)) == 1:
            common_prefix += current_column[0]

        else:
            break

    return common_prefix


a = ["flower", "flow", "flight"]
print(longestCommonPrefix(a))
