# SINGLE LAYER PERCEPTRON :

The perceptron is a single processing unit of any neural network. Frank Rosenblatt first proposed in 1958 is a simple neuron which is used to classify its input into one or two categories. Perceptron is a linear classifier, and is used in supervised learning. It helps to organize the given input data.

A perceptron is a neural network unit that does a precise computation to detect features in the input data. Perceptron is mainly used to classify the data into two parts. Therefore, it is also known as Linear Binary Classifier.

The perceptron consists of 4 parts.
* Input value or One input layer: The input layer of the perceptron is made of artificial input neurons and takes the initial data into the system for further processing.
* Weights and Bias:
Weight: It represents the dimension or strength of the connection between units. If the weight to node 1 to node 2 has a higher quantity, then neuron 1 has a more considerable influence on the neuron.
* Bias: It is the same as the intercept added in a linear equation. It is an additional parameter which task is to modify the output along with the weighted sum of the input to the other neuron.
Net sum: It calculates the total sum.
* Activation Function: A neuron can be activated or not, is determined by an activation function. The activation function calculates a weighted sum and further adding bias with it to give the result.

# how to use this Package :

## Import these libraries :
```python
from oneNeuron.perceptron import Perceptron
from oneNeuron.allutils import prepare_data
from oneNeuron.allutils import save_model
```

# how to call Perceptron class :
```python
model = Perceptron(eta, epochs)
model.fit(X, y)
```
# A glance of the code :

```python
class Perceptron:
  def __init__(self, eta, epochs):
    self.weights = np.random.randn(3) * 1e-4 # SMALL WEIGHT INIT
    logging.info(f"initial weights before training: \n{self.weights}")
    self.eta = eta # LEARNING RATE
    self.epochs = epochs 


  def activationFunction(self, inputs, weights):
    z = np.dot(inputs, weights) # z = W * X
    return np.where(z > 0, 1, 0) # CONDITION, IF TRUE, ELSE

  def fit(self, X, y):
    self.X = X
    self.y = y

    X_with_bias = np.c_[self.X, -np.ones((len(self.X), 1))] # CONCATINATION
    logging.info(f"X with bias: \n{X_with_bias}")

    for epoch in tqdm(range(self.epochs), total=self.epochs, desc="Training the Model"):
      logging.info("--"*10)
      logging.info(f"for epoch: {epoch}")
      logging.info("--"*10)

      y_hat = self.activationFunction(X_with_bias, self.weights) # foward propagation
      logging.info(f"predicted value after forward pass: \n{y_hat}")
      self.error = self.y - y_hat
      logging.info(f"error: \n{self.error}")
      self.weights = self.weights + self.eta * np.dot(X_with_bias.T, self.error) # backward propagation
      logging.info(f"updated weights after epoch:\n{epoch}/{self.epochs} : \n{self.weights}")
      logging.info("#####"*10)


  def predict(self, X):
    X_with_bias = np.c_[X, -np.ones((len(X), 1))]
    return self.activationFunction(X_with_bias, self.weights)

  def total_loss(self):
    total_loss = np.sum(self.error)
    logging.info(f"total loss: {total_loss}")
    return total_loss

```
