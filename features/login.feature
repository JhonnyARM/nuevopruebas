Feature: Inicio de sesión en la aplicación móvil

  Scenario: Inicio de sesión con Microsoft
    Given la aplicación está abierta
    When presiono el botón "Iniciar sesión con Microsoft"
    And ingreso mi correo electrónico "jhorivera@upt.pe"
    And presiono el botón "Next"
    And ingreso mi contraseña "dfhgdvh123456jN"
    And presiono el botón "Sign in"
    Then debo iniciar sesión con éxito y ver la pantalla de bienvenida
