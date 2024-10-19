'use strict';

/**
 * Parses and validates the given operands.
 *
 * @param {string|number} a - The first operand to be parsed and validated.
 * @param {string|number} b - The second operand to be parsed and validated.
 * @returns {{numA: number, numB: number}} An object containing the parsed numbers.
 * @throws {Error} Throws an error if either operand is not a valid number.
 */
const parseOperands = (a, b) => {
  if (a === undefined || b === undefined) {
    throw new Error('Operands must not be undefined');
  }

  const numA = Number(a);
  const numB = Number(b);

  if (isNaN(numA) || isNaN(numB)) {
    throw new Error('Operands must be numbers');
  }

  return { numA, numB };
};

exports.parseOperands = parseOperands;


function validateOperand(operand, operandName) {
  if (!operand ||
      !operand.match(/^(-)?[0-9\.]+(e(-)?[0-9]+)?$/) ||
      operand.replace(/[-0-9e]/g, '').length > 1) {
    throw new Error("Invalid " + operandName + ": " + operand);
  }
}

exports.validateOperand = validateOperand;
