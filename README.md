## **COMMANDS TO SSH IN AWS EC2 CABROOZ**

### **Add ssh key to OS**

`chmod 400 carbooz-keys.pem`


### **Connect to your instance using its public DNS**

`ec2-3-14-146-25.us-east-2.compute.amazonaws.com`


### **SSH into VM**

`ssh -i carbooz-keys.pem ubuntu@ec2-3-14-146-25.us-east-2.compute.amazonaws.com`

`ssh -i carbooz-keys.pem ubuntu@3.14.146.25`
