const logoutButton = document.getElementById('logout-button');

logoutButton.addEventListener('click', logout);

function logout() {
  // Выход из аккаунта и перенаправление на страницу регистрации
  window.location.href = 'reg.html';
}








