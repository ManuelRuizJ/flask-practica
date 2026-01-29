"# flask-practica"

App web monolítica en Flask

1. ¿Qué quedó más acoplado en el monolito?
   • El frontend, se vuelve totalmente dependiente del backend, lo que evita que se pueda reutilizar el backend sin reescribir el frontend.
   • La base de datos que está acoplada directamente a la app, SQLite está embebido y las consultas SQL están repartidas por todo “app.py”.
2. ¿Qué separarías primero si lo migraras a API / microservicio?
   • El módulo CRUD de productos para dejar el monolito solo como frontend, ya que si por alguna razón una parte del CRUD o del frontend deja de funcionar.
   • Separar la base de datos en un servicio.
   • Separar la autenticación, dividirlos en servicios aparte una de otra, para así poder realizar cambios sin romper el resto del proyecto.
3. ¿Qué problemas surgen si dos equipos trabajan en paralelo en el mismo monolito?
   • Que al tocar “app.py” se encuentren varios conflictos al realizar el merge, los cambios continuos que cada uno realiza y surgen bugs difíciles de
   rastrear.
   • Realizar cambios rompen cosas que no se tocaron.
   • No se puede desplegar por partes.
   • Las pruebas se realizan más lentas y son más frágiles.
