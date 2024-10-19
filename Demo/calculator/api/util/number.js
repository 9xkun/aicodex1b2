'use strict';

/**
 * Parses and validates the given operands.
 *
 * @param {string|number} a : required - The first operand to be parsed and validated.
 * @param {string|number} b : required - The second operand to be parsed and validated.
 *
 * @returns {{numA: number, numB: number}} An object containing the parsed numbers.
 * @throws {Error} Throws an error if either operand is not a valid number.
 *
 * @example
 * const result1 = parseOperands(21, 21); // { numA: 21, numB: 21 }
 * const result6 = parseOperands(1.2e-5, -1.2e-5); { numA: 1.2e-5, numB: -1.2e-5 }
 *
 */
const parseOperands = (a, b) => {
  // Defensive code: Check if operands are undefined
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


/**
 * Validates the given operand.
 *
 * @param {string} operand - The operand to be validated.
 * @param {string} operandName - The name of the operand for error messages.
 * @throws {Error} Throws an error if the operand is invalid.
 */
function validateOperand(operand, operandName) {
  if (!operand ||
      !operand.match(/^(-)?[0-9\.]+(e(-)?[0-9]+)?$/) ||
      operand.replace(/[-0-9e]/g, '').length > 1) {
    throw new Error("Invalid " + operandName + ": " + operand);
  }
}

exports.validateOperand = validateOperand;
