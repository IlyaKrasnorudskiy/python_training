import unittest
import tensorflow as tf
import numpy as np


class TestTensorFlowOperations(unittest.TestCase):

    def test_tensor_creation(self):
        tensor = tf.constant([1, 2, 3])
        self.assertEqual(tensor.shape, (3,))
        self.assertEqual(tensor.numpy().tolist(), [1, 2, 3])

    def test_simple_model(self):
        x_train = np.random.random((100, 3))
        y_train = np.random.randint(0, 2, 100)

        model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(3,)),  # Указываем форму входных данных
            tf.keras.layers.Dense(10, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        model.fit(x_train, y_train, epochs=1, batch_size=10)

        # Намеренно вводим ошибку в проверку точности, ожидаем значение больше 1
        self.assertEqual(model.history.history['accuracy'][0] > 1, True)  # Это ошибка

    def test_data_preprocessing(self):
        data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        data = tf.convert_to_tensor(data)

        processed_data = data * 2
        self.assertTrue(np.array_equal(processed_data.numpy(), [2.0, 4.0, 6.0, 8.0, 10.0]))

    def test_gpu_availability(self):
        devices = tf.config.list_physical_devices('GPU')
        if len(devices) == 0:
            print("GPU не доступен, тест пропущен.")
            return
        self.assertGreater(len(devices), 0, "GPU не доступен для использования")

    def test_interoperability_with_numpy(self):
        tensor = tf.constant([1, 2, 3, 4, 5])
        numpy_array = tensor.numpy()
        self.assertTrue(np.array_equal(numpy_array, [1, 2, 3, 4, 5]))

    def test_model_prediction(self):
        x_test = np.random.random((10, 3))
        model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(3,)),  # Указываем форму входных данных
            tf.keras.layers.Dense(10, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        model.fit(x_test, np.random.randint(0, 2, 10), epochs=1, batch_size=10)

        predictions = model.predict(x_test)

        # Намеренно вводим ошибку в проверку формы предсказания
        self.assertEqual(predictions.shape, (20, 1))  # Ошибка! Предсказания имеют форму (10, 1)

if __name__ == '__main__':
    unittest.main()
