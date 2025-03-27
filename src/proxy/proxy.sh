
ssh -v -R 0.0.0.0:9092:localhost:9090 root@182.92.3.33 -p 22

ps aux | grep "ssh -fN -R 9092"

curl http://127.0.0.1:9092
