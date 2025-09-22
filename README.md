# Projeto-UGTSIC-Django

Sistema desenvolvido em Django para **envio de currículos**, oferecendo uma solução prática e intuitiva para empresas que buscam captar talentos.

---

## 📘 Finalidade

O **SkillUp** foi criado para simplificar o processo de aplicação em vagas de emprego e visualização delas pela empresa — em um único lugar, organizado, categorizado e fácil de acessar.

A plataforma é ideal para:

* Profissionais que buscam uma nova oportunidade;
* Empresas que necessitam de um profissional;
* Estudantes em busca de estágios;

---

## ✅ Funcionalidades

* 📎 Autenticação de usuários;
* 🔍 Painel administrativo com todos os currículos da plataforma para o superusuário credenciado;
* 🧩 Formulário para criar currículo;
* 🌐 Envio automático dos dados dos candidatos para o email da empresa;
* 📥 Upload de comprovante de matrícula da sua candidatura;
* 📱 Interface totalmente **responsiva com Bulma CSS**;
* 🐳 **Containerização com Docker** para fácil execução em qualquer ambiente.

---

## 🛠 Stack Utilizada

| Tecnologia         | Finalidade                                                                                                   |
| ------------------ | ------------------------------------------------------------------------------------------------------------ |
| **Django**        | Framework monólito para construção do sistema de ponta a ponta.                                                  |
| **PostgrsSQL**     | SGBD relacional para persistência de dados. |
| **Docker**         | Containerização da aplicação.                                                                                |
| **Docker Compose** | Orquestração dos serviços.                                                                                   |
| **Bulma CSS**   | Estilização rápida, responsiva e intuitiva.                                                                    |

---

## ⚙️ Como Rodar o Projeto

Antes de iniciar, você precisa ter instalado:

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

### 1. Clonar o Repositório

```bash
git clone https://github.com/bernardommedeiros/Projeto-UGTSIC-Django.git
cd src
```

### 2. Construção dos Containers
```bash
docker compose build
```

### 3. Chaves de ambiente
```bash
crie um arquivo .env
copie e cole o arquivo .env_example adicionando as varíaveis necessárias
```

### 3. Subir os serviços
```bash
docker compose up
```


## 🛠️ Dicas e comandos relevantes para testes no sistemas

### 1. Criar superusuário para visualização do painel administrativo
<p> Após subir os serviços, execute em uma nova linha de comando </p>

```bash
docker exec -it web python manage.py createsuperuser
```

### 2. Teste envio de Email
<p> Acesse esse caminho dentro do sistemas e adicione outros emails em "TO=[]" nas classes <b>CVCreateView</b> e <b>CVUpdateView</b> -> linhas 28 e 57 do arquivo respectivamente, para as informações do formulário chegarem em seu e-mail</p>

```bash
cd src/ugtsic_project/cv_hub/cvform.py
```

## 📝 Licença

Este projeto está licenciado sob a **MIT License**.
Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
