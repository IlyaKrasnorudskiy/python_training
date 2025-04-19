# tensorflow_test_suite.py
import os
import sys
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split


print("\n=== ТЕСТ 1: ПРОВЕРКА УСТАНОВКИ ===")

try:
    assert sys.version_info >= (3, 8)
    print(f"✓ Python {sys.version.split()[0]} - OK")
except AssertionError:
    raise SystemExit("❌ Требуется Python 3.8+")

try:
    print("\nПроверка TensorFlow...")
    print(f"Версия TensorFlow: {tf.__version__}")
    print("Доступные устройства:")
    print("CPU:", tf.config.list_physical_devices('CPU'))
    print("GPU:", tf.config.list_physical_devices('GPU'))
except ImportError:
    raise SystemExit("❌ TensorFlow не установлен")


print("\n=== ТЕСТ 2: МАТРИЧНЫЕ ОПЕРАЦИИ ===")


def test_matrix_operations():
    # Создание матриц
    a = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
    b = tf.constant([[5, 6], [7, 8]], dtype=tf.float32)

    # Операции
    sum_result = tf.add(a, b)
    product_result = tf.matmul(a, b)

    # Дополнительные метрики
    metrics = {
        'det_a': tf.linalg.det(a).numpy(),
        'det_b': tf.linalg.det(b).numpy(),
        'trace_sum': tf.linalg.trace(sum_result).numpy()
    }

    print("\nРезультат сложения:")
    print(sum_result.numpy())

    print("\nРезультат умножения:")
    print(product_result.numpy())

    print("\nДополнительные метрики:")
    print(f"Детерминант A: {metrics['det_a']:.2f}")
    print(f"Детерминант B: {metrics['det_b']:.2f}")
    print(f"След суммы: {metrics['trace_sum']:.2f}")

    return a, b, sum_result



matrix_a, matrix_b, matrix_sum = test_matrix_operations()


print("\n=== ТЕСТ 3: ПРОВЕРКА GPU ===")


def check_gpu(matrix1, matrix2):
    gpus = tf.config.list_physical_devices('GPU')

    if not gpus:
        print("\nИнформация: GPU не обнаружены. Используется CPU")
        device = '/CPU:0'
    else:
        print(f"\nНайдено GPU: {len(gpus)} устройств")
        device = '/GPU:0'


    with tf.device(device):
        print(f"\nВычисления на устройстве: {device}")
        result = tf.add(matrix1, matrix2)
        print("Результат сложения матриц (те же данные из Блока 2):")
        print(result.numpy())

        print("\nБенчмарк (1000 операций):")
        for _ in range(1000):
            _ = tf.matmul(matrix1, matrix2)
        print("Вычисления завершены")


# Используем матрицы из Блока 2
check_gpu(matrix_a, matrix_b)


print("\n=== ТЕСТ 4: МОДЕЛЬ KERAS ===")


def build_and_test_model():
    # Генерация данных
    X = np.random.normal(size=(1000, 5))
    y = (X.sum(axis=1) > 0).astype(int)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Построение модели
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(32, activation='relu', input_shape=(5,)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(16, activation='tanh'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['AUC', 'Precision']
    )


    print("\nОбучение модели...")
    history = model.fit(
        X_train, y_train,
        validation_data=(X_test, y_test),
        epochs=5,
        batch_size=32,
        verbose=1
    )


    print("\nОценка модели на тестовых данных:")
    results = model.evaluate(X_test, y_test, verbose=0)
    print(f"Loss: {results[0]:.4f}")
    print(f"AUC: {results[1]:.4f}")
    print(f"Precision: {results[2]:.4f}")


build_and_test_model()

print("\n=== ТЕСТИРОВАНИЕ ЗАВЕРШЕНО ===")
print("Все основные тесты выполнены успешно!")
