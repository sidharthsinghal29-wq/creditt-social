// Creditt — calculators
// Both calculators are simplified estimates for illustration only,
// not a formal loan quote or credit assessment.

function formatAUD(n) {
  return n.toLocaleString('en-AU', { style: 'currency', currency: 'AUD', maximumFractionDigits: 0 });
}

document.addEventListener('DOMContentLoaded', function () {

  /* ---------------- Repayment calculator ---------------- */
  var repayForm = document.querySelector('#repayment-calc');
  if (repayForm) {
    var amountInput = repayForm.querySelector('#loan-amount');
    var rateInput = repayForm.querySelector('#interest-rate');
    var termInput = repayForm.querySelector('#loan-term');
    var amountVal = repayForm.querySelector('#loan-amount-val');
    var rateVal = repayForm.querySelector('#interest-rate-val');
    var termVal = repayForm.querySelector('#loan-term-val');

    var monthlyFigure = document.querySelector('#repay-monthly');
    var totalInterestFigure = document.querySelector('#repay-total-interest');
    var totalPaidFigure = document.querySelector('#repay-total-paid');

    function calcRepayment() {
      var P = parseFloat(amountInput.value);
      var annualRate = parseFloat(rateInput.value);
      var years = parseFloat(termInput.value);
      var r = (annualRate / 100) / 12;
      var n = years * 12;

      var M = r === 0 ? P / n : (P * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
      var totalPaid = M * n;
      var totalInterest = totalPaid - P;

      amountVal.textContent = formatAUD(P);
      rateVal.textContent = annualRate.toFixed(2) + '%';
      termVal.textContent = years + ' yrs';

      monthlyFigure.textContent = formatAUD(M);
      totalInterestFigure.textContent = formatAUD(totalInterest);
      totalPaidFigure.textContent = formatAUD(totalPaid);
    }

    [amountInput, rateInput, termInput].forEach(function (el) {
      el.addEventListener('input', calcRepayment);
    });
    calcRepayment();
  }

  /* ---------------- Borrowing power calculator ---------------- */
  var borrowForm = document.querySelector('#borrowing-calc');
  if (borrowForm) {
    var incomeInput = borrowForm.querySelector('#gross-income');
    var expensesInput = borrowForm.querySelector('#monthly-expenses');
    var debtsInput = borrowForm.querySelector('#monthly-debts');
    var dependentsInput = borrowForm.querySelector('#dependents');

    var estimateFigure = document.querySelector('#borrow-estimate');
    var surplusFigure = document.querySelector('#borrow-surplus');

    function calcBorrowingPower(e) {
      if (e) e.preventDefault();
      var annualIncome = parseFloat(incomeInput.value) || 0;
      var monthlyIncome = annualIncome / 12;
      var monthlyExpenses = parseFloat(expensesInput.value) || 0;
      var monthlyDebts = parseFloat(debtsInput.value) || 0;
      var dependents = parseFloat(dependentsInput.value) || 0;

      // Simplified serviceability model: apply a living-cost buffer per dependent,
      // an assessed (buffered) interest rate, and a conservative income shading.
      var dependentCost = dependents * 450;
      var netMonthly = (monthlyIncome * 0.8) - monthlyExpenses - monthlyDebts - dependentCost;
      netMonthly = Math.max(netMonthly, 0);

      var assessedAnnualRate = 8.5; // buffered rate used for a conservative estimate
      var r = (assessedAnnualRate / 100) / 12;
      var n = 30 * 12;
      var maxLoan = netMonthly * 0.35 * ((Math.pow(1 + r, n) - 1) / (r * Math.pow(1 + r, n)));

      estimateFigure.textContent = formatAUD(Math.max(maxLoan, 0));
      surplusFigure.textContent = formatAUD(netMonthly) + ' / month';
    }

    borrowForm.addEventListener('input', calcBorrowingPower);
    calcBorrowingPower();
  }
});
