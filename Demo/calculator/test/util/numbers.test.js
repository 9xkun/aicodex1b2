const { expect } = require('chai');
const { parseOperands } = require('../../api/util/number');

// api/util/number.test.js

describe('parseOperands', function () {
  it('should parse valid numeric string operands', function () {
    const result = parseOperands('3', '4');
    expect(result).to.eql({ numA: 3, numB: 4 });
  });

  it('should parse valid number operands', function () {
    const result = parseOperands(3, 4);
    expect(result).to.eql({ numA: 3, numB: 4 });
  });

  it('should throw an error if operands are undefined', function () {
    expect(() => parseOperands(undefined, 4)).to.throw('Operands must not be undefined');
    expect(() => parseOperands(3, undefined)).to.throw('Operands must not be undefined');
  });

  it('should throw an error if operands are not numbers', function () {
    expect(() => parseOperands('foo', 4)).to.throw('Operands must be numbers');
    expect(() => parseOperands(3, 'bar')).to.throw('Operands must be numbers');
  });

  it('should parse valid numeric string with exponent', function () {
    const result = parseOperands('1.2e-5', '-1.2e-5');
    expect(result).to.eql({ numA: 1.2e-5, numB: -1.2e-5 });
  });
});