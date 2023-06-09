# Alura Challenge Back-end - AluraFlix API

Este repositório guarda a minha versão do back-end do site AluraFlix, desenvolvido no Alura Challenge Back-End 5.
| :placard: Vitrine.Dev |     |
| -------------  | --- |
| :sparkles: Nome        | **Alura Challenge Back-end - AluraFlix**
| :label: Tecnologias | Django, Docker, AWS e Terraform
| :rocket: URL         | 

<!-- Inserir imagem com a #vitrinedev ao final do link -->

## Detalhes do Projeto
O projeto tem o objetivo de construir um back-end para o front do site Aluraflix. Resolvi utilizar as tecnologias Django.

### Semana 1 ✅
Iniciar o banco de dados e criar requisições CRUD básicas.

<table>
    <tr>
        <th>Listar todos os Vídeos</th>
        <th>Listar um vídeo</th>
    </tr>
    <tr>
        <td><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/116848225/243177298-aff8880c-a204-457f-9ce4-8fae78dc22f6.gif" alt="listar todos os vídeos"></td>
        <td><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/116848225/243177705-dbb15c16-6fa0-413b-b232-3726a39ef57b.gif" alt="listar um vídeo"></td>
    </tr>
    <tr>
        <th>Adicionar um vídeo</th>
        <th>Alterar um vídeo</th>
    </tr>
    <tr>
        <td><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/116848225/243177733-c214d59a-54f1-419f-bbfa-6c107fac6f56.gif" alt="adicionar um vídeo"></td>
        <td><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/116848225/243177752-cbfe93fb-0479-4300-9c66-bd067cd6a996.gif" alt="alterar um vídeo"></td>
    </tr>
    <tr>
        <th>Deletar um Vídeo</th>
    </tr>
    <tr>
        <td><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/116848225/243177774-470774a8-fa5c-4524-9ffb-102d7ef8dc61.gif" alt="deletar um vídeo"></td>
    </tr>
</table>

### Semana 2 ✅
Criar nova tabela para categorias com relação de categoria 1:n vídeos; fazer rotas CRUD para as categorias; criar rota para listar vídeos por categoria; e criar rota com parâmetros de busca para os vídeos.

<table>
    <tr>
        <th>Listar todas as Categorias</th>
        <th>Listar uma categoria</th>
    </tr>
    <tr>
        <td><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/116848225/243185426-f34f9125-7fac-4f6e-9c90-b49eed384c2c.gif" alt="listar todas as categoria"></td>
        <td><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/116848225/243185473-168c7b92-1c2f-40b1-a1aa-b0e43dd531e3.gif" alt="listar uma categoria"></td>
    </tr>
    <tr>
        <th>Adicionar uma categoria</th>
        <th>Alterar uma categoria</th>
    </tr>
    <tr>
        <td><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/116848225/243185523-6e6fcb65-ceba-4774-88dc-8cd3c0eed40a.gif" alt="adicionar uma categoria"></td>
        <td><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/116848225/243185566-e1c95396-1e0e-4e91-b061-e80e9f3bf555.gif" alt="alterar uma categoria"></td>
    </tr>
    <tr>
        <th>Deletar uma categoria</th>
        <th>Listar vídeos por categoria</th>
    </tr>
    <tr>
        <td><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/116848225/243185604-7652821e-fb35-4b4c-a9f0-2f9ee120d08a.gif" alt="deletar uma categoria"></td>
        <td><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/116848225/243185954-db72e1a0-548e-4541-9fa2-b7ba1f23a338.gif" alt="listar videos por categoria"></td>
    </tr>
    <tr>
        <th>Procurar um vídeo</th>
    </tr>
    <tr>
        <td><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/116848225/243185629-5bea1625-462e-4d48-baa8-1dceee1f1c52.gif" alt="procurar um vídeo"></td>
    </tr>
</table>

### Semana 3/4 ✅
Criar funcionalidades de paginação, autenticação e fazer o deploy da API.
Para a autenticação, resolvi usar o Basic Auth, criado com login de um usuário. Para testar usar o `"username": "matheus"` e a `"password":"toor"`. Entendo que seria melhor uma criptografia da senha, mas escolhi pela simplicidade.

<table>
    <tr>
        <th>Paginação</th>
        <th>Autenticação</th>
    </tr>
    <tr>
        <td><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/116848225/244812122-36446dd5-5938-473b-85e6-1a3febae2369.gif" alt="paginação"></td>
        <td><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/116848225/244811987-6334a1bb-ef94-4880-aed7-072615f32155.gif" alt="autenticação"></td>
    </tr>
</table>


