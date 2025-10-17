# Sistema de Segurança Simples

## 📋 Descrição

Um sistema de segurança básico em Python que monitora tentativas de acesso e gerencia usuários autorizados.

## 🚀 Funcionalidades

- **Cadastro de Usuários**: Adicione usuários com senha
- **Autenticação**: Sistema de login com validação de credenciais
- **Registro de Tentativas**: Monitora e registra tentativas de acesso (sucesso e falha)
- **Bloqueio Automático**: Bloqueia usuário após 3 tentativas falhas
- **Histórico de Acessos**: Visualize o log de todas as tentativas

## 📦 Requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa necessária (usa apenas bibliotecas padrão)

## 🔧 Como Usar

1. Execute o programa:
```bash
python sistema_seguranca.py
```

2. Menu principal:
   - **Opção 1**: Cadastrar novo usuário
   - **Opção 2**: Fazer login
   - **Opção 3**: Ver histórico de acessos
   - **Opção 4**: Sair do sistema

## 💡 Exemplo de Uso

### Cadastrar Usuário
```
Escolha uma opção: 1
Digite o nome de usuário: joao
Digite a senha: senha123
✓ Usuário cadastrado com sucesso!
```

### Fazer Login
```
Escolha uma opção: 2
Usuário: joao
Senha: senha123
✓ Acesso autorizado! Bem-vindo, joao!
```

## 🔒 Recursos de Segurança

- Senhas armazenadas com hash (não são salvas em texto puro)
- Bloqueio automático após 3 tentativas falhas consecutivas
- Registro de data/hora de todas as tentativas de acesso
- Sistema de permissões básico

## ⚠️ Avisos

Este é um sistema de segurança **educacional e simplificado**. Para aplicações reais, considere:
- Usar banco de dados seguro
- Implementar criptografia mais robusta
- Adicionar autenticação de dois fatores
- Usar bibliotecas especializadas como `bcrypt` ou `argon2`

## 📝 Estrutura dos Arquivos

- `sistema_seguranca.py`: Código principal do sistema
- `usuarios.json`: Banco de dados de usuários (criado automaticamente)
- `log_acessos.txt`: Histórico de tentativas de acesso

## 🤝 Contribuições

Sinta-se à vontade para melhorar este código! Algumas ideias:
- Adicionar níveis de permissão (admin, usuário comum)
- Implementar recuperação de senha
- Criar interface gráfica
- Adicionar notificações por email

## 📄 Licença

Este projeto é livre para uso educacional.
