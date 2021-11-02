# webapp
Esse repositório contém a aplicação web para o controle de presença dos alunos.

A aplicação está agora empacotada como um pacote python, por isso a estrutura de diretórios nova.

Para executar pela primeira vez, clone o repositório, via CMD entre no diretório `webapp` e execute:

```
set PYTHONPATH=C:\Users\lamas\univesp\webapp\sisdiconpra\:.
set FLASK_APP=sisdiconpra.webapp.app
set FLASK_ENV=development
flask run
```

Atente que `C:\Users\lamas\univesp\webapp\sisdiconpra\` precisa ser o mesmo caminho na sua máquina local, esse é o caminho no meu PC :)

Acesse http://127.0.0.1:5000/webapp/

Essa versão ainda não está conectando no MySQL, estamos usando o SQLite como banco. Você vai notar que no diretório `sisdiconpra\webapp` vai ser criado um arquivo chamado db.sqlite. Mudar para o MySQL é uma questão de configuração, por enquanto vamos seguir assim para todo mundo entender o código que é mais próximo da arquitetura final.
