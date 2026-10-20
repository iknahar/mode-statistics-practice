from scipy import stats
#
data = [12, 10, 12, 15, 10, 8]
result = stats.mode(data)
try:
    print(result[0][0])          # the way old tutorials wrote it
except IndexError as e:
    print("IndexError:", e)
print(result.mode, result.count) # the way that works now
