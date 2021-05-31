with_dots = ["processing..", "...  strings ", " with....", "..map.."]

a=list(map(lambda s: s.strip(". "), with_dots))
print(a)
