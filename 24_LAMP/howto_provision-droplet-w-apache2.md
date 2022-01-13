# how-to :: CREATE A DIGITAL OCEAN DROPLET WITH UBUNTU AND APACHE
---
## Overview
Guide to creating an ubuntu 20.04 virtual machine ("droplet") and installing Apache2 web server on it.

### Estimated Time Cost: _

### Prerequisites:
1. Log in as root with `ssh root@server_ip`
2. Create a new user with `adduser user_name`
3. Give admin priveleges with `usermod -aG sudo user_name`
4. Set up a firewall with 
	```
	ufw allow OpenSSH
	ufw enable
	```
5. SSH into the user with `ssh user_name@server_ip`
6. Run the following to install Apache:
	```
	sudo apt update
	sudo apt install apache2
	```
7. Allow traffic on port 80 with `sudo ufw allow in "Apache"`
8. Run `sudo apt install mysql-server` to install MySQL
9. 

### Resources
* https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh
* https://www.digitalocean.com/community/questions/secure-ubuntu-server-for-non-root-user-using-only-ssh-keys?answer=22286
* https://www.digitalocean.com/community/tutorials/how-to-create-a-new-sudo-enabled-user-on-ubuntu-18-04-quickstart
* https://www.digitalocean.com/docs/droplets/how-to/
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh?answer=44730
* https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/putty/
* https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/create-with-openssh/
* https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/openssh/

(please verify ; some of these are old links)

---

Accurate as of (last update): 2022-01-11

### Additional Notes
- You can use "sudo" before commands when logged in as a regular user to get superuser priveleges
- Run `curl http://icanhazip.com` to get your public IP

#### Contributors:  
Clyde "Thluffy" Sinclair  
Topher Mykolyk, pd0  

_Note: the two spaces after each name are important! ( <--burn after reading)  _
