---
layout: post
title:  "첫 번째 실습 예제입니다."
---

# -*- coding: utf-8 -*-
"""tensorflow_basic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/sleeptiger/cd042ae94539e95fac868f914bfc17bb/tensorflow_basic.ipynb
"""

import tensorflow as tf

키 = 170
신발 = 260

# 신발 = 키 * a + b

a = tf.Variable(0.1)
b = tf.Variable(0.2)

def 손실함수():
  예측값 = 키 * a + b
  return tf.square(260 - 예측값)       #return = 손실값 = 실제값 - 예측값(오차)


opt = tf.keras.optimizers.Adam(learning_rate=0.1)

for i in range(300):
  opt.minimize(손실함수, var_list=[a,b])
  print(a.numpy(),b.numpy())


