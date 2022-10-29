import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#이미지 가져오는 곳
fashion_mnist = tf.keras.datasets.fashion_mnist

#이미지 가져오기
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

#최종결과물 LABEL
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#가져온 이미지 0~1 사이로 변환
train_images = train_images / 255.0
test_images = test_images / 255.0

#모델 만들기
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

#모델 컴파일
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


#이제부터 모델 훈련함

#훈련 데이터로 훈련함
model.fit(train_images, train_labels, epochs=10)

#테스트 데이터로 정확도 테스트
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)

#데이터 예측하기
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_images)

predictions[0]

np.argmax(predictions[0])
