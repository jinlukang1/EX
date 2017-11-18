
# coding: utf-8

# In[93]:


from functools import reduce

class Perceptron(object):
    def __init__(self, input_num, activator):
        self.weights = [0.0 for _ in range(input_num)]
        self.bias = 0.0
        self.activator = activator

    def __str__(self):
        return 'weights:%s\nbias:%s' % (self.weights, self.bias)
    
    def predict(self, input_vec):
        a = list(map(lambda x, y: x * y, self.weights, input_vec))
        return self.activator(sum(a, self.bias))
    
    def train(self, input_vecs, labels, rate, times):
        for i in range(times):
            self.train_one(input_vecs, labels, rate)
            
    def train_one(self, input_vecs, labels, rate):
        samples = zip(input_vecs, labels)
        for (input_vec, label) in samples:
            output = self.predict(input_vec)
            self.bp(input_vec, label, rate, output)
    
    def bp(self, input_vec, label, rate, output):
        delta = label - output
        self.weights = list(map(lambda x, y: y + rate * delta * x, input_vec, self.weights))
        self.bias += rate * delta
        
def f(x):
    if(x > 0):
        return 1
    else:
        return 0
    
def get_date():
    input_vecs = [[1,1], [1,0], [0,1], [0,0]]
    labels = [1, 0, 0, 0]
    return input_vecs, labels

def train_date():
    p = Perceptron(2, f)
    input_vecs, labels = get_date()
    p.train(input_vecs, labels, 0.01, 100)
    return p
    
if __name__ == '__main__':
    a = train_date()
    print(a)
    print('1 and 1 = %s' % a.predict([1, 1]))
    print('0 and 0 = %s' % a.predict([0, 0]))
    print('1 and 0 = %s' % a.predict([1, 0]))
    print('0 and 1 = %s' % a.predict([0, 1]))

