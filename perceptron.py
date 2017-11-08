#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Perceptron(object):
    def __init__(self, input_num, activator):
        '''
        ³õÊ¼»¯¸ĞÖªÆ÷£¬ÉèÖÃÊäÈë²ÎÊıµÄ¸öÊı£¬ÒÔ¼°¼¤»îº¯Êı¡£
        ¼¤»îº¯ÊıµÄÀàĞÍÎªdouble -> double
        '''
        self.activator = activator
        # È¨ÖØÏòÁ¿³õÊ¼»¯Îª0
        self.weights = [0.0 for _ in range(input_num)]
        # Æ«ÖÃÏî³õÊ¼»¯Îª0
        self.bias = 0.0

    def __str__(self):
        '''
        ´òÓ¡Ñ§Ï°µ½µÄÈ¨ÖØ¡¢Æ«ÖÃÏî
        '''
        return 'weights\t:%s\nbias\t:%f\n' % (self.weights, self.bias)

    
    def predict(self, input_vec):
        '''
        ÊäÈëÏòÁ¿£¬Êä³ö¸ĞÖªÆ÷µÄ¼ÆËã½á¹û
        '''
        # °Ñinput_vec[x1,x2,x3...]ºÍweights[w1,w2,w3,...]´ò°üÔÚÒ»Æğ
        # ±ä³É[(x1,w1),(x2,w2),(x3,w3),...]
        # È»ºóÀûÓÃmapº¯Êı¼ÆËã[x1*w1, x2*w2, x3*w3]
        # ×îºóÀûÓÃreduceÇóºÍ
        return self.activator(
            reduce(lambda a, b: a + b,
                   map(lambda (x, w): x * w,  
                       zip(input_vec, self.weights))
                , 0.0) + self.bias)
 
    def train(self, input_vecs, labels, iteration, rate):
        '''
        ÊäÈëÑµÁ·Êı¾İ£ºÒ»×éÏòÁ¿¡¢ÓëÃ¿¸öÏòÁ¿¶ÔÓ¦µÄlabel£»ÒÔ¼°ÑµÁ·ÂÖÊı¡¢Ñ§Ï°ÂÊ
        '''
        for i in range(iteration):
            self._one_iteration(input_vecs, labels, rate)

    def _one_iteration(self, input_vecs, labels, rate):
        '''
        Ò»´Îµü´ú£¬°ÑËùÓĞµÄÑµÁ·Êı¾İ¹ıÒ»±é
        '''
        # °ÑÊäÈëºÍÊä³ö´ò°üÔÚÒ»Æğ£¬³ÉÎªÑù±¾µÄÁĞ±í[(input_vec, label), ...]
        # ¶øÃ¿¸öÑµÁ·Ñù±¾ÊÇ(input_vec, label)
        samples = zip(input_vecs, labels)
        # ¶ÔÃ¿¸öÑù±¾£¬°´ÕÕ¸ĞÖªÆ÷¹æÔò¸üĞÂÈ¨ÖØ
        for (input_vec, label) in samples:
            # ¼ÆËã¸ĞÖªÆ÷ÔÚµ±Ç°È¨ÖØÏÂµÄÊä³ö
            output = self.predict(input_vec)
            # ¸üĞÂÈ¨ÖØ
            self._update_weights(input_vec, output, label, rate)

    def _update_weights(self, input_vec, output, label, rate):
        '''
        °´ÕÕ¸ĞÖªÆ÷¹æÔò¸üĞÂÈ¨ÖØ
        '''
        # °Ñinput_vec[x1,x2,x3,...]ºÍweights[w1,w2,w3,...]´ò°üÔÚÒ»Æğ
        # ±ä³É[(x1,w1),(x2,w2),(x3,w3),...]
        # È»ºóÀûÓÃ¸ĞÖªÆ÷¹æÔò¸üĞÂÈ¨ÖØ
        delta = label - output
        self.weights = map(
            lambda (x, w): w + rate * delta * x,
            zip(input_vec, self.weights))
        # ¸üĞÂbias
        self.bias += rate * delta


def f(x):
    '''
    ¶¨Òå¼¤»îº¯Êıf
    '''
    return 1 if x > 0 else 0


def get_training_dataset():
    '''
    »ùÓÚandÕæÖµ±í¹¹½¨ÑµÁ·Êı¾İ
    '''
    # ¹¹½¨ÑµÁ·Êı¾İ
    # ÊäÈëÏòÁ¿ÁĞ±
    input_vecs = [[1,1,1], [1,0,0], [1,0,1], [0,0,1], [0,1,0], [0,1,1], [1,1,0]]
    # ÆÚÍûµÄÊä³öÁĞ±í£¬×¢ÒâÒªÓëÊäÈëÒ»Ò»¶ÔÓ¦
    # [1,1] -> 1, [0,0] -> 0, [1,0] -> 0, [0,1] -> 0
    labels = [1, 0, 0, 0, 0, 0, 0]
    return input_vecs, labels    


def train_and_perceptron():
    '''
    Ê¹ÓÃandÕæÖµ±íÑµÁ·¸ĞÖªÆ÷
    '''
    # ´´½¨¸ĞÖªÆ÷£¬ÊäÈë²ÎÊı¸öÊıÎª2£¨ÒòÎªandÊÇ¶şÔªº¯Êı£©£¬¼¤»îº¯ÊıÎªf
    p = Perceptron(3, f)
    # ÑµÁ·£¬µü´ú10ÂÖ, Ñ§Ï°ËÙÂÊÎª0.1
    input_vecs, labels = get_training_dataset()
    p.train(input_vecs, labels, 100, 0.1)
    #·µ»ØÑµÁ·ºÃµÄ¸ĞÖªÆ÷
    return p


if __name__ == '__main__': 
    # ÑµÁ·and¸ĞÖªÆ÷
    and_perception = train_and_perceptron()
    # ´òÓ¡ÑµÁ·»ñµÃµÄÈ¨ÖØ
    print and_perception
    # ²âÊÔ
    print '1 and 1 and 1 = %d' % and_perception.predict([1, 1, 1])
    print '0 and 0 and 0 = %d' % and_perception.predict([0, 0, 0])
    print '1 and 0 and 1 = %d' % and_perception.predict([1, 0, 1])
    print '0 and 1 and 1 = %d' % and_perception.predict([0, 1, 1])
    print '1 and 1 and 0 = %d' % and_perception.predict([1, 1, 0])
