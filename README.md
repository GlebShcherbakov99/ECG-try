# Prepare your enviroment
## Linux
1. Open up your terminal (by pressing Ctrl + Alt + T).
2. Update your local system's repository list by entering the following command:

```shell
sudo apt update
```

3. Check your Python version (it is better to use python3.7):

```shell
python3 --version
```

4. Clone repository using git:

```shell
sudo apt install git
```

```shell
cd ~
```
```shell
git clone https://github.com/Konstantin-Lebeda/ECG-core-project.git
```
```shell
cd ECG-core-project
```

5. Install requirement python libraries usin pip3:

```shell
sudo apt install python3-pip
```

```shell
pip3 install -r requirements.txt
```

6. Run simpletest.py to make sure, that everything goes on so far:

```shell
python3 simpletest.py
```
