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

Essa versão agora conectando no MySQL. Certifique-se que você está com o container do MySQL rodando e que no banco tenha um schema chamado `pi`.
