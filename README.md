# Python IMC Calculator
![Python](https://img.shields.io/badge/Python-323330?style=for-the-badge&logo=python&logoColor=356A99)

Calculadora de IMC, indíce de massa corporal (ou BMI - Body Mass Index, sigla em inglês) feito com Python. 

## O que é o IMC?
O IMC é reconhecido como o padrão internacional para calcular o grau de sobrepeso de uma pessoa, o cálculo é feito da seguinte forma: 

```
IMC = peso / (altura * altura)
```
ou
```
IMC = peso / (altura²)
```
Ambas as formas são válidas de calcular o IMC de uma pessoa.

Portanto, se uma pessoa pesa 80kg com 1.80m de altura - o cálculo ficaria da seguinte forma:

```
IMC = 80kg / (1.80m²) = 24,69kg/m2
```

## O que significa o resultado? Neste caso, 24,69?

De acordo com a tabela abaixo, o valor ~24,7 indica que a pessoa está no peso normal.

| **IMC** | **Classificações** |
| --- | -------------- |
| Menor do que 18,5 | Abaixo do peso normal |
| 18,5 até 24,9 | Peso normal |
| 25,0 até 29,99 | Excesso de peso |
| 30,0 - 34,9 | Obsedidade classe I |
| 35,0 - 39,9 | Obsedidade classe II |
| Maior ou igual a 40,00 | Obsedidade classe III |
