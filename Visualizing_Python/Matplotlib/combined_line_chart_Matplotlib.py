import matplotlib.pyplot as plt


# y value series
variance     = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]

# zip() combines two data series to tuples
total_error  = [x + y for x, y in zip(variance, bias_squared)]

# x values
xs = range(len(variance))

# we can make multiple calls to plt.plot
# to show multiple series on the same chart
# green solid line, red dot-dashed line, blue dotted line
plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias_squared, 'r-.', label='bias^2')
plt.plot(xs, total_error, 'b:', label='total error')

# because we've assigned labels to each series
# we can get a legend for free
# loc=9 means "top center"
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()