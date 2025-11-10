Feature: Operações básicas e avançadas da calculadora
  Para realizar cálculos simples e complexos
  Como um usuário
  Eu quero usar a calculadora para somar, subtrair, multiplicar, dividir, calcular raiz quadrada e média.

  # SOMA
  Scenario: Somar dois números 1
    Given que iniciei a calculadora
    When somo 2 e 8
    Then o resultado deve ser 10

  Scenario: Somar dois números 2
    Given que iniciei a calculadora
    When somo 15 e 5
    Then o resultado deve ser 20

  Scenario: Somar dois números 3
    Given que iniciei a calculadora
    When somo 100 e 250
    Then o resultado deve ser 350

  Scenario: Somar dois números 4
    Given que iniciei a calculadora
    When somo -3 e 7
    Then o resultado deve ser 4

  Scenario: Somar dois números 5
    Given que iniciei a calculadora
    When somo -10 e -5
    Then o resultado deve ser -15


  # SUBTRAÇÃO
  Scenario: Subtrair dois números 1
    Given que iniciei a calculadora
    When subtraio 7 de 20
    Then o resultado deve ser 13

  Scenario: Subtrair dois números 2
    Given que iniciei a calculadora
    When subtraio 50 de 100
    Then o resultado deve ser 50

  Scenario: Subtrair dois números 3
    Given que iniciei a calculadora
    When subtraio -5 de 10
    Then o resultado deve ser 15

  Scenario: Subtrair dois números 4
    Given que iniciei a calculadora
    When subtraio 8 de 3
    Then o resultado deve ser -5

  Scenario: Subtrair dois números 5
    Given que iniciei a calculadora
    When subtraio -10 de -4
    Then o resultado deve ser 6


  # MULTIPLICAÇÃO
  Scenario: Multiplicar dois números 1
    Given que iniciei a calculadora
    When multiplico 4 por 6
    Then o resultado deve ser 24

  Scenario: Multiplicar dois números 2
    Given que iniciei a calculadora
    When multiplico 3 por -5
    Then o resultado deve ser -15

  Scenario: Multiplicar dois números 3
    Given que iniciei a calculadora
    When multiplico -8 por -2
    Then o resultado deve ser 16

  Scenario: Multiplicar dois números 4
    Given que iniciei a calculadora
    When multiplico 0 por 10
    Then o resultado deve ser 0

  Scenario: Multiplicar dois números 5
    Given que iniciei a calculadora
    When multiplico 12 por 12
    Then o resultado deve ser 144


  # DIVISÃO
  Scenario: Dividir dois números 1
    Given que iniciei a calculadora
    When divido 20 por 5
    Then o resultado deve ser 4

  Scenario: Dividir dois números 2
    Given que iniciei a calculadora
    When divido 9 por 3
    Then o resultado deve ser 3

  Scenario: Dividir dois números 3
    Given que iniciei a calculadora
    When divido -12 por 3
    Then o resultado deve ser -4

  Scenario: Dividir dois números 4
    Given que iniciei a calculadora
    When divido 50 por -10
    Then o resultado deve ser -5

  Scenario: Dividir dois números 5
    Given que iniciei a calculadora
    When divido -21 por -7
    Then o resultado deve ser 3

  # Divisão por zero
  Scenario: Lidar com divisão por zero 1
    Given que iniciei a calculadora
    When tento dividir 10 por 0
    Then devo receber um erro com a mensagem "Divisão por zero não permitida"


  # RAIZ QUADRADA
  Scenario: Raiz quadrada 1
    Given que iniciei a calculadora
    When calculo a raiz quadrada de 16
    Then o resultado deve ser 4

  Scenario: Raiz quadrada 2
    Given que iniciei a calculadora
    When calculo a raiz quadrada de 25
    Then o resultado deve ser 5

  Scenario: Raiz quadrada 3
    Given que iniciei a calculadora
    When calculo a raiz quadrada de 1
    Then o resultado deve ser 1

  Scenario: Raiz quadrada 4
    Given que iniciei a calculadora
    When calculo a raiz quadrada de 36
    Then o resultado deve ser 6

  Scenario: Raiz quadrada 5
    Given que iniciei a calculadora
    When calculo a raiz quadrada de 0
    Then o resultado deve ser 0


  # Raiz quadrada negativa
  Scenario: Raiz quadrada negativa
    Given que iniciei a calculadora
    When tento calcular a raiz quadrada de -9
    Then devo receber um erro com a mensagem "Número inválido"


  # MÉDIA
  Scenario: Calcular média 1
    Given que iniciei a calculadora
    When calculo a media dos numeros "10, 20, 30"
    Then o resultado deve ser 20

  Scenario: Calcular média 2
    Given que iniciei a calculadora
    When calculo a media dos numeros "5, 7"
    Then o resultado deve ser 6

  Scenario: Calcular média 3
    Given que iniciei a calculadora
    When calculo a media dos numeros "100, 200, 300, 400"
    Then o resultado deve ser 250

  Scenario: Calcular média 4
    Given que iniciei a calculadora
    When calculo a media dos numeros "-2, -4, -6"
    Then o resultado deve ser -4

  Scenario: Calcular média 5
    Given que iniciei a calculadora
    When calculo a media dos numeros "1"
    Then o resultado deve ser 1
