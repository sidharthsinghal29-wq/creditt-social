// Creditt. — shared site behaviour
(function () {
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var fmt = function (n) { return n.toLocaleString('en-AU', { style: 'currency', currency: 'AUD', maximumFractionDigits: 0 }); };

  document.addEventListener('DOMContentLoaded', function () {
    var header = $('.site-header');

    // Header turns solid once the page scrolls
    function onScroll() { header.classList.toggle('scrolled', window.scrollY > 24); }
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });

    // Mobile menu
    var toggle = $('.nav-toggle');
    if (toggle) {
      toggle.addEventListener('click', function () {
        var open = header.classList.toggle('menu-open');
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
        document.body.style.overflow = open ? 'hidden' : '';
      });
      $$('.mobile-panel a').forEach(function (a) {
        a.addEventListener('click', function () { header.classList.remove('menu-open'); document.body.style.overflow = ''; });
      });
    }

    // Range sliders: paint the filled track
    function paint(el) {
      var min = +el.min || 0, max = +el.max || 100;
      el.style.setProperty('--fill', ((el.value - min) / (max - min) * 100) + '%');
    }
    $$('input[type=range]').forEach(function (el) { paint(el); el.addEventListener('input', function () { paint(el); }); });

    // FAQ accordion
    $$('.faq-item').forEach(function (item) {
      var btn = $('.faq-q', item);
      btn.setAttribute('aria-expanded', 'false');
      btn.addEventListener('click', function () {
        var was = item.classList.contains('open');
        $$('.faq-item.open').forEach(function (o) { o.classList.remove('open'); $('.faq-q', o).setAttribute('aria-expanded', 'false'); });
        if (!was) { item.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); }
      });
    });

    // Home page estimator
    var amt = $('#hx-amount');
    if (amt) {
      var out = $('#hx-monthly'), val = $('#hx-amount-val');
      var calc = function () {
        var P = +amt.value, r = 0.062 / 12, n = 360;
        var M = (P * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
        out.textContent = fmt(M);
        val.textContent = fmt(P);
      };
      amt.addEventListener('input', calc); calc();
    }

    // Process line fills as the steps scroll into view
    var steps = $('.steps');
    if (steps && 'IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { steps.style.setProperty('--p', 1); io.disconnect(); } });
      }, { threshold: .4 });
      io.observe(steps);
    } else if (steps) { steps.style.setProperty('--p', 1); }

    // Enquiry + call-back forms
    $$("#lead-form, #cb-form, .lead-form").forEach(function (form) {
      var scope = form.closest('dialog') || form.closest('.form-card') || document;
      var btn0 = $('button[type="submit"]', form), label = btn0.textContent;
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var ok = $('.form-success', scope), bad = $('.form-error', scope), btn = btn0;
        ok.style.display = 'none'; bad.style.display = 'none';
        btn.disabled = true; btn.textContent = 'Sending…';
        fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } })
          .then(function (res) {
            if (res.ok) { form.reset(); ok.style.display = 'block'; ok.focus(); if (window.creditConfetti) window.creditConfetti();
              if (window.gtag) window.gtag('event', 'generate_lead'); if (window.dataLayer) window.dataLayer.push({ event: 'generate_lead' }); }
            else { bad.style.display = 'block'; }
          })
          .catch(function () { bad.style.display = 'block'; })
          .finally(function () { btn.disabled = false; btn.textContent = label; });
      });
    });

    var y = $('#year'); if (y) y.textContent = new Date().getFullYear();
  });
})();
