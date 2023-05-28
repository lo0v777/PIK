// Дождемся полной загрузки страницы перед назначением обработчика событий
document.addEventListener('DOMContentLoaded', function() {
    // Найдем форму по ее идентификатору и назначим обработчик отправки формы
    var form = document.getElementById('myForm');
    form.addEventListener('submit', function(event) {
      event.preventDefault(); // Предотвратим отправку формы
  
      // Выполним необходимые действия по обработке данных формы
      // Например, можно получить значения полей формы:
      var wallWidth = document.getElementById('wallWidth').value;
      var wallHeight = document.getElementById('wallHeight').value;
      var standX = document.getElementById('standX').value;
      var standY = document.getElementById('standY').value;
      var standZ = document.getElementById('standZ').value;
  
      // Далее можно выполнить необходимые расчеты или передать данные на сервер
      // ...
  
      // Перейдем на другую страницу после обработки данных
      window.location.href = '3d.html';
    });
  });
  