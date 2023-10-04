// Abertura dos modals
document.addEventListener("DOMContentLoaded", function () {
    const modal = new bootstrap.Modal(document.getElementById("modal"));

    htmx.on("htmx:afterSwap", function (e) {
        modal.show();
    });

    htmx.on("htmx:afterRequest", function (e) {
        modal.hide();
    });
});
// Abertura dos modals

// Validação das senhas
    function validatePasswords() {
        var senha1 = document.getElementById('id_password1').value;
        var senha2 = document.getElementById('id_password2').value;
        var errorSpan = document.getElementById('senha-2-error');

        if (senha1 !== senha2) {
            document.getElementById('id_password2').classList.add('is-invalid'); // Adiciona classe de erro ao campo
            document.getElementById('salvar').classList.add('disabled'); // Desativa o botão de salvar
        } else {
            document.getElementById('id_password2').classList.remove('is-invalid'); // Remove a classe de erro do campo
            document.getElementById('salvar').classList.remove('disabled'); // Ativa o botão de salvar
        }
    }

    document.getElementById('id_password1').addEventListener('input', validatePasswords);
    document.getElementById('id_password2').addEventListener('input', validatePasswords);
// Validação das senhas


fetch('http://127.0.0.1:8000/qualquer_requisicao')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Erro:', error));


fetch('https://viacep.com.br/ws/01001000/json/')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Erro:', error));
