# gpu_check.py
import tensorflow as tf


def check_gpu_and_add_matrices():
    gpus = tf.config.list_physical_devices('GPU')

    if not gpus:
        print("Информация: GPU не обнаружены. Для ускорения вычислений рекомендуется использовать GPU")
        print("Доступные устройства CPU:", tf.config.list_physical_devices('CPU'))

        # Демонстрация сложения матриц на CPU
        matrix1 = tf.constant([[1.0, 2.0], [3.0, 4.0]])
        matrix2 = tf.constant([[5.0, 6.0], [7.0, 8.0]])
        result_cpu = tf.add(matrix1, matrix2)

        print("Результат сложения матриц на CPU:\n", result_cpu.numpy())
        return

    print(f"Найдено GPU: {len(gpus)} устройств")

    for i, gpu in enumerate(gpus):
        details = tf.config.experimental.get_device_details(gpu)
        print(f"GPU {i + 1}:")
        print(f"  Имя: {gpu.name}")

        # Демонстрация сложения матриц на GPU
        with tf.device('/GPU:0'):
            matrix1 = tf.constant([[1.0, 2.0], [3.0, 4.0]])
            matrix2 = tf.constant([[5.0, 6.0], [7.0, 8.0]])
            result_gpu = tf.add(matrix1, matrix2)

        print("Результат сложения матриц на GPU:\n", result_gpu.numpy())


if __name__ == "__main__":
    check_gpu_and_add_matrices()
