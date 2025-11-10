export class Calculadora {
  soma(a: number, b: number): number {
    return a + b;
  }

  subtracao(a: number, b: number): number {
    return a - b;
  }

  multiplicacao(a: number, b: number): number {
    return a * b;
  }

  divisao(a: number, b: number): number {
    if (b === 0) throw new Error('Divisão por zero não permitida');
    return a / b;
  }

  raizQuadrada(n: number): number {
    if (n < 0) throw new Error('Número inválido');
    return Math.sqrt(n);
  }

  media(numbers: number[]): number {
    if (numbers.length === 0) return 0;
    const total = numbers.reduce((acc, num) => acc + num, 0);
    return total / numbers.length;
  }
}