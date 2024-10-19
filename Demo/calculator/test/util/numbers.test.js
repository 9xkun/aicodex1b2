const { expect } = require('chai');
const { parseOperands } = require('../../api/util/number');

// api/util/number.test.js

describe('parseOperands', function () {
  // api/util/number.test.js

  describe('parseOperands', function () {
    const successTestCases = [
      { input: ['3', '4'], expected: { numA: 3, numB: 4 } },
      { input: [3, 4], expected: { numA: 3, numB: 4 } },
      { input: ['1.2e-5', '-1.2e-5'], expected: { numA: 1.2e-5, numB: -1.2e-5 } },
      { input: ['0', '0'], expected: { numA: 0, numB: 0 } },
      { input: ['-10', '20'], expected: { numA: -10, numB: 20 } },
      { input: ['3.14', '2.71'], expected: { numA: 3.14, numB: 2.71 } },
    ];

    successTestCases.forEach(({ input, expected }) => {
      it(`should parse operands ${input} correctly`, function () {
        const result = parseOperands(...input);
        expect(result).to.eql(expected);
      });
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

  it('should throw an error if operands are undefined', function () {
    expect(() => parseOperands(undefined, 4)).to.throw('Operands must not be undefined');
    expect(() => parseOperands(3, undefined)).to.throw('Operands must not be undefined');
  });

  it('should throw an error if operands are not numbers', function () {
    expect(() => parseOperands('foo', 4)).to.throw('Operands must be numbers');
    expect(() => parseOperands(3, 'bar')).to.throw('Operands must be numbers');
  });

});