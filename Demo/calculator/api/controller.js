'use strict';

const { parseOperands, validateOperand } = require("./util/number");

// TODO: Define or import the operations object
const operations = {
  add: (a, b) => {
    const { numA, numB } = parseOperands(a, b);
    return numA + numB;
  },
  subtract: (a, b) => {
    const { numA, numB } = parseOperands(a, b);
    return numA - numB;
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

  validateOperand(req.query.operand1, "operand1");
  validateOperand(req.query.operand2, "operand2");

  console.log("Operand1: " + req.query.operand1);
  console.log("Operand2: " + req.query.operand2);
  res.json({ result: operation(req.query.operand1, req.query.operand2) });
};
