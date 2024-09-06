function isFibonacci(num) {
  if (num < 0) return false;

  // Função para verificar se um número é um número de Fibonacci
  function isPerfectSquare(n) {
    let sqrt = Math.sqrt(n);
    return sqrt === Math.floor(sqrt);
  }

  function checkFibonacci(n) {
    let x1 = 5 * n * n + 4;
    let x2 = 5 * n * n - 4;
    return isPerfectSquare(x1) || isPerfectSquare(x2);
  }

  return checkFibonacci(num);
}

// Função para calcular e exibir a sequência de Fibonacci até o número informado
function fibonacciSequence(num) {
  let sequence = [0, 1];
  while (sequence[sequence.length - 1] < num) {
    let next = sequence[sequence.length - 1] + sequence[sequence.length - 2];
    sequence.push(next);
  }
  return sequence;
}

function main() {
  let number = 98;

  if (isNaN(number)) {
    console.log("Por favor, insira um número válido.");
    return;
  }

  let sequence = fibonacciSequence(number);

  console.log(`Sequência de Fibonacci até ${number}: ${sequence.join(", ")}`);

  if (isFibonacci(number)) {
    console.log(`${number} pertence à sequência de Fibonacci.`);
  } else {
    console.log(`${number} não pertence à sequência de Fibonacci.`);
  }
}

// Executar o programa
main();
