# Pega-IP
Pega-IP é uma simples aplicação para pegar o endereço de IP do usuário que foi desenvolvida para fins de teste a partir de uma necessidade com relação a norma de LGPD para captura de logs do usuário.

## Como rodar o projeto?

* Clone esse repositório.
* Crie um ambiente virtual com Python 3.
* Ative o ambiente virtual.
* Instale as dependências.


##-Caso Linux
```
terminal
git clone https://github.com/vladetec/Pega-IP.git
cd Pega-IP
python3 -m venv venv
source venv/bin/activate
cd ..
cd ..
python -m pip install -U pip
pip install -U setuptools wheel
pip install -r requirements.txt
export FLASK_APP=pega_ip.py
export FLASK_DEBUG=1   
flask run
```
###-Fechar e Sair
```
ctrl + c  --Interrompe a execuçao
deactivate  --Sai do ambiente virtual

```


##-Caso Windows
```
cmd
git clone https://github.com/vladetec/Pega-IP.git
cd Pega-IP
python -m venv venv
cd venv/Scripts
activate
cd .. 
cd ..
python -m pip install -U pip
pip install -U setuptools wheel
pip install -r requirements.
set FLASK_APP=pega_ip.py
set FLASK_DEBUG=1 
flask run
```
###-Fechar e Sair
```
ctrl + c  -- Interrompe a execuçao
deactivate  -- Sai do ambiente virtual

```
## Links

[PEGA-IP - Usando IPAPI](http://localhost:5000/)

[PEGA-IP - Usando JSON](http://127.0.0.1:5000/pega_ip)



