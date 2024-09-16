from kafka import KafkaConsumer

def main():
    consumer = KafkaConsumer(
            'test', 
            bootstrap_servers=['{Docker HostのIPアドレス}:{Port}'])

    for message in consumer:
        print("x = " + message.value.decode())

if __name__ == '__main__':
    main()
