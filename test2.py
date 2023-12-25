import redis
import time
import json
redis_host = 'localhost'  # Replace with your Redis server host
redis_port = 6379         # Replace with your Redis server port
redis_db = 0              # Replace with your Redis database number
queue_name = 'my_queue'
# Create a connection to Redis
redis_conn = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

def process_queue_item(item): 
    print(f"Popped message as dict: {item}")
    
    
def process_queue(redis_conn, queue_name):
    while True:
        # Lấy một mục từ hàng đợi
        popped_message = redis_conn.lpop(queue_name)

        # Nếu có mục trong hàng đợi
        if popped_message:
            # item là một tuple (queue_name, data)
            popped_dict = json.loads(popped_message.decode('utf-8'))
            process_queue_item(popped_dict)
        else:
            # Đợi 30 giây nếu hàng đợi rỗng
            print("hàng đợi rỗng")
            time.sleep(30)
            

process_queue(redis_conn, queue_name)