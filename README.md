# Projeto de Controle de Dados de Funcionários e Envio de Mensagens via WhatsApp

Bem-vindo ao projeto de controle de dados de funcionários e envio de mensagens via WhatsApp com Python! Este projeto permite que você leia uma tabela de dados de funcionários de uma empresa, manipule esses dados e envie mensagens via WhatsApp.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

1. `faker_planilha.py`: Gera uma planilha fictícia de dados de funcionários.
2. `envia_whatsapp.py`: Conecta-se ao WhatsApp Web para enviar mensagens.
3. `empresa.py`: Classe que representa a empresa e seus funcionários.
4. `funcionario.py`: Classe que representa um funcionário.
5. `playbook.ipynb`: Jupyter Notebook para manipulação interativa dos dados.

## Dependências

Para executar este projeto, você precisará das seguintes bibliotecas:

- `Faker`
- `openpyxl`
- `pandas`
- `selenium`
- `jupyter`

Você pode instalar essas dependências utilizando o seguinte comando:

```bash
pip install -r requirements.txt
```

## Como Utilizar

1.Gerar a Planilha de Dados de Funcionários
Execute o arquivo faker_planilha.py para gerar uma planilha fictícia com dados de 100 funcionários. O arquivo será salvo como funcionarios.xlsx.

```bash
python faker_planilha.py
```

2.Conectar ao WhatsApp Web
Execute o arquivo envia_whatsapp.py para abrir o WhatsApp Web. Siga as instruções na tela para escanear o código QR com seu celular e conectar-se ao WhatsApp Web.

```bash
python envia_whatsapp.py
```

3.Manipular Dados de Funcionários
Use o Jupyter Notebook playbook.ipynb para manipular interativamente os dados dos funcionários. Você pode abrir o notebook com o seguinte comando:

```bash
jupyter notebook playbook.ipynb
```

4.Trabalhar com a Classe Empresa
No arquivo empresa.py, a classe Empresa permite que você leia a planilha de funcionários e crie instâncias da classe Funcionario. Você pode manipular os dados dos funcionários diretamente através da classe Funcionario e salvar as alterações de volta na planilha.

```python
from empresa import Empresa
```

## Criar uma instância da empresa

```python
empresa = Empresa('Minha Empresa', planilha='funcionarios.xlsx')
```

## Acessar um funcionário

```python

funcionario = empresa.funcionarios[0]

# Modificar o nome do funcionário
funcionario.nome = 'Novo Nome'

# Salvar alterações
empresa.salvar_alteracoes()
```
