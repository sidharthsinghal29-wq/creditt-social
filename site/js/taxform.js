// Creditt. — multi-step personal tax form
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelector('.tax-form'); if (!form) return;
    var all = [].slice.call(form.querySelectorAll('.step'));
    var back = document.getElementById('wiz-back'), next = document.getElementById('wiz-next'), send = document.getElementById('wiz-send');
    var count = document.getElementById('wiz-count'), fill = document.getElementById('wiz-fill');
    var cur = 0;
    function active() {
      var picked = [].slice.call(form.querySelectorAll('input[name="applies[]"]:checked')).map(function (i) { return i.value; });
      return all.filter(function (s) { var k = s.getAttribute('data-key'); return k === 'about' || k === 'auth' || picked.indexOf(k) > -1; });
    }
    function show(i) {
      var list = active(); cur = Math.max(0, Math.min(i, list.length - 1));
      all.forEach(function (s) { s.hidden = list[cur] !== s; });
      count.textContent = 'Step ' + (cur + 1) + ' of ' + list.length + ': ' + list[cur].querySelector('legend').textContent;
      fill.style.width = ((cur + 1) / list.length * 100) + '%';
      back.hidden = cur === 0; next.hidden = cur === list.length - 1; send.hidden = cur !== list.length - 1;
    }
    function valid() {
      var s = active()[cur], fs = s.querySelectorAll('input,select,textarea');
      for (var i = 0; i < fs.length; i++) { if (!fs[i].checkValidity()) { fs[i].reportValidity(); return false; } }
      return true;
    }
    function top() { var c = document.getElementById('form'); if (c) window.scrollTo({ top: c.getBoundingClientRect().top + scrollY - 100, behavior: 'smooth' }); }
    next.addEventListener('click', function () { if (valid()) { show(cur + 1); top(); } });
    back.addEventListener('click', function () { show(cur - 1); top(); });
    form.addEventListener('change', function (e) { if (e.target.name === 'applies[]') show(cur); });
    form.addEventListener('keydown', function (e) { if (e.key === 'Enter' && e.target.tagName !== 'TEXTAREA' && e.target.tagName !== 'BUTTON') { e.preventDefault(); if (!send.hidden) { send.click(); } else { next.click(); } } });
    // Block sending until the last step is valid (runs before the shared form handler)
    document.addEventListener('submit', function (e) {
      if (e.target !== form) return;
      if (!send.hidden && valid()) return;
      e.preventDefault(); e.stopImmediatePropagation();
    }, true);
    form.addEventListener('reset', function () { setTimeout(function () { show(0); top(); }, 0); });
    show(0);
  });
})();
