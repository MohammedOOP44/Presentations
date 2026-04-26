def find_high_intensity(readings, threshold):
    # [expression for item in list if condition]
    return [r for r in readings if r > threshold]

# Test the function
readings = [120, 450, 780, 110, 900, 30]
threshold = 500
print(find_high_intensity(readings, threshold))
# Output: [780, 900]