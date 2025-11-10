import { Calculadora } from '../src/calculadora';

describe('Calculadora', () => {
  let calculadora: Calculadora;

  beforeEach(() => {
    calculadora = new Calculadora();
  });

  test('deve somar dois números corretamente', () => {
    expect(calculadora.soma(2, 3)).toBe(5);
  });

  test('deve subtrair dois números corretamente', () => {
    expect(calculadora.subtracao(10, 4)).toBe(6);
  });

  test('deve multiplicar dois números corretamente', () => {
    expect(calculadora.multiplicacao(3, 5)).toBe(15);
  });

  test('deve dividir dois números corretamente', () => {
    expect(calculadora.divisao(10, 2)).toBe(5);
  });

  test('deve lançar erro ao tentar dividir por zero', () => {
    expect(() => calculadora.divisao(10, 0)).toThrow('Divisão por zero não permitida');
  });

  test('deve calcular a raiz quadrada corretamente', () => {
    expect(calculadora.raizQuadrada(9)).toBe(3);
  });

  test('deve lançar erro ao calcular raiz de número negativo', () => {
    expect(() => calculadora.raizQuadrada(-4)).toThrow('Número inválido');
  });

  test('deve calcular a média corretamente', () => {
    expect(calculadora.media([2, 4, 6])).toBe(4);
  });

  test('deve retornar 0 caso a lista esteja vazia', () => {
    expect(calculadora.media([])).toBe(0);
  });
});