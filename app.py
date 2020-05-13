from confluent_kafka import Producer

p = Producer({'bootstrap.servers':'my-cluster-kafka-bootstrap:9092')
p.produce('my-topic',key='message',value='Hello from Python')
p.flush(30)
