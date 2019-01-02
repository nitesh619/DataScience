from sklearn.linear_model import LinearRegression

x = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [10]]

model = LinearRegression()
model.fit(x, y)

print(model.predict(5))
