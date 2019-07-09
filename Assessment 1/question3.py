meters = 640
meters_to_inch = meters / 0.0254
meters_to_foot = meters_to_inch / 12
meters_to_yard = meters_to_foot / 3
meters_to_miles = meters_to_yard / 1760

print("{}m is equivalent to {}\"".format(meters, round(meters_to_inch, 2)))
print("{}m is equivalent to {}'".format(meters, round(meters_to_foot, 2)))
print("{}m is equivalent to {}yd".format(meters, round(meters_to_yard, 2)))
print("{}m is equivalent to {} miles".format(meters, round(meters_to_miles, 2)))
    