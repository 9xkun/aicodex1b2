'use strict';

/**
 * Checks if the input is a string of 4 or more incremental digits.
 *
 * @param {string} input - The input string to be checked.
 * @returns {boolean} - Returns true if the input is a string of 4 or more incremental digits, otherwise false.
 */
function isIncremental(input) {
  // Check if input is a string of 4 or more digits
  if (!/^\d{4,}$/.test(input)) {
    return false;
  }

  // Convert the string to an array of digits
  const digits = Array.from(input, Number);

  // Check if the digits are incremental
  for (let i = 1; i < digits.length; i++) {
    if (digits[i] !== digits[i - 1] + 1) {
      return false;
    }
  }

  return true;
}

exports.isIncremental = isIncremental;

// TODO: Define or import the operations object
const parseAndValidateOperands = (a, b) => {
    const intA = parseInt(a, 10);
    const intB = parseInt(b, 10);

    if (isNaN(intA) || isNaN(intB)) {
        throw new Error('Operands must be integers');
    }

    return { intA, intB };
};

const operations = {
  add: (a, b) => {
    const { intA, intB } = parseAndValidateOperands(a, b);
    return intA + intB;
  },
  subtract: (a, b) => {
    const { intA, intB } = parseAndValidateOperands(a, b);
    return intA - intB;
  },
};

exports.calculate = function(req, res) {
  req.app.use(function(err, _req, res, next) {
    if (res.headersSent) {
      return next(err);
    }

    res.status(400);
    res.json({ error: err.message });
  });

  if (!req.query.operation) {
    throw new Error("Unspecified operation");
  }

  var operation = operations[req.query.operation];
  if (!operation) {
    throw new Error("Invalid operation: " + req.query.operation);
  }

  if (!req.query.operand1 ||
      !req.query.operand1.match(/^(-)?[0-9\.]+(e(-)?[0-9]+)?$/) ||
      req.query.operand1.replace(/[-0-9e]/g, '').length > 1) {
    throw new Error("Invalid operand1: " + req.query.operand1);
  }

  if (!req.query.operand2 ||
      !req.query.operand2.match(/^(-)?[0-9\.]+(e(-)?[0-9]+)?$/) ||
      req.query.operand2.replace(/[-0-9e]/g, '').length > 1) {
    throw new Error("Invalid operand2: " + req.query.operand2);
  }

  console.log("Operand1: " + req.query.operand1);
  console.log("Operand2: " + req.query.operand2);
  res.json({ result: operation(req.query.operand1, req.query.operand2) });
};
