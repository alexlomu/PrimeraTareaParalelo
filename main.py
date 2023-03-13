import threading
import queue
import time

# Se crea una cola de productos con una capacidad máxima de 5
queue_size = 5
product_queue = queue.Queue(maxsize=queue_size)

# Función que produce productos y los añade a la cola
def producer():
    while True:
        if not product_queue.full():
            product = time.time()
            product_queue.put(product)
            print(f"Productor: {product} producido y añadido a la cola")
        time.sleep(1)

# Función que consume productos de la cola
def consumer():
    while True:
        if not product_queue.empty():
            product = product_queue.get()
            print(f"Consumidor: {product} consumido de la cola")
        time.sleep(2)

# Se crean dos hilos, uno para el productor y otro para el consumidor
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Se inician los hilos
producer_thread.start()
consumer_thread.start()
