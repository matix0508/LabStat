# LabStat

## Using:
### Curve Fitting
```
# you have to write your custom function that you want to fit into data
def my_func(x: np.ndarray, a: float) -> np.ndarray:
  return a * x ** 2

# data to feed curve fitting
xdata = np.array([1, 2, 3, 4, 5, 6])
ydata = inverse_square(xdata, 3)

model = CurveFit(xdata, ydata, my_func, ['a'])
model.find_curve()
model.plot()
print(model.output)
```

### LinearRegression
```
linreg = LinReg(xdata, ydata)
print(f"a = {linreg.a}, b = {linreg.b}")
```
