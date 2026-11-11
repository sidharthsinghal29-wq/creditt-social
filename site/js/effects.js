// Creditt. — visual effects (all optional; the site works without them)
(function () {
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var calm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  // Confetti in brand colours (used when a form sends)
  window.creditConfetti = function () {
    if (calm) return;
    var cols = ['#F19B70', '#FFD15D', '#D0B7EF', '#FFC2A3', '#4B1F68'];
    var box = document.createElement('div');
    box.setAttribute('aria-hidden', 'true');
    box.style.cssText = 'position:fixed;inset:0;pointer-events:none;z-index:400;overflow:hidden';
    document.body.appendChild(box);
    for (var i = 0; i < 46; i++) {
      var d = document.createElement('i'), s = 6 + Math.random() * 10;
      d.style.cssText = 'position:absolute;left:50%;top:55%;width:' + s + 'px;height:' + s + 'px;border-radius:50%;background:' + cols[i % 5];
      box.appendChild(d);
      var a = Math.random() * Math.PI * 2, v = 160 + Math.random() * 420;
      d.animate([
        { transform: 'translate(0,0) scale(1)', opacity: 1 },
        { transform: 'translate(' + Math.cos(a) * v + 'px,' + (Math.sin(a) * v - 160) + 'px) scale(1)', opacity: 1, offset: .55 },
        { transform: 'translate(' + Math.cos(a) * v * 1.1 + 'px,' + (Math.sin(a) * v + 320) + 'px) scale(.6)', opacity: 0 }
      ], { duration: 1500 + Math.random() * 600, easing: 'cubic-bezier(.2,.7,.3,1)', fill: 'forwards' });
    }
    setTimeout(function () { box.remove(); }, 2400);
  };

  document.addEventListener('DOMContentLoaded', function () {
    // Scroll progress bar
    var bar = document.createElement('div');
    bar.className = 'progress'; bar.setAttribute('aria-hidden', 'true');
    document.body.appendChild(bar);
    var fab = $('.cb-fab');
    function onScroll() {
      var h = document.documentElement.scrollHeight - innerHeight;
      bar.style.transform = 'scaleX(' + (h > 0 ? scrollY / h : 0) + ')';
      if (fab) fab.classList.toggle('show', scrollY > 500);
    }
    onScroll(); addEventListener('scroll', onScroll, { passive: true });

    // Call-back dialog
    var dlg = $('#cb');
    if (dlg && dlg.showModal) {
      $$('[data-callback]').forEach(function (b) {
        b.addEventListener('click', function () {
          $('.form-success', dlg).style.display = 'none'; $('.form-error', dlg).style.display = 'none';
          dlg.showModal(); var f = $('input[name=full_name]', dlg); if (f) f.focus();
        });
      });
      dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
    } else {
      $$('[data-callback]').forEach(function (b) { b.addEventListener('click', function () { location.href = 'contact.html'; }); });
    }

    // Hero: cursor glow + layered parallax
    var hero = $('#hero');
    if (hero && fine && !calm) {
      var raf = 0, tx = 0, ty = 0, mx = .7, my = .3;
      hero.addEventListener('pointermove', function (e) {
        var r = hero.getBoundingClientRect();
        mx = (e.clientX - r.left) / r.width; my = (e.clientY - r.top) / r.height;
        if (!raf) raf = requestAnimationFrame(function () {
          raf = 0;
          hero.style.setProperty('--mx', (mx * 100) + '%'); hero.style.setProperty('--my', (my * 100) + '%');
          hero.style.setProperty('--px', (mx - .5).toFixed(3)); hero.style.setProperty('--py', (my - .5).toFixed(3));
        });
      });
    }

    // Tilt on tiles
    if (fine && !calm) {
      $$('[data-tilt]').forEach(function (t) {
        t.addEventListener('pointermove', function (e) {
          var r = t.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
          t.style.transform = 'perspective(900px) rotateX(' + (-y * 5) + 'deg) rotateY(' + (x * 6) + 'deg) translateY(-4px)';
        });
        t.addEventListener('pointerleave', function () { t.style.transform = ''; });
      });
    }

    // Story: the house builds as each step scrolls into view
    var grid = $('.story-grid');
    if (grid) {
      var lis = $$('.story-steps li');
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (e.isIntersecting) {
            var n = +e.target.getAttribute('data-s');
            grid.setAttribute('data-step', n);
            lis.forEach(function (l) { l.classList.toggle('active', l === e.target); });
          }
        });
      }, { rootMargin: window.matchMedia('(max-width: 1020px)').matches ? '-60% 0px -30% 0px' : '-45% 0px -45% 0px' });
      lis.forEach(function (l) { io.observe(l); });
    }

    // Video: play when visible, manual pause control
    var v = $('#hv');
    if (v) {
      var btn = $('.vid-toggle'), manual = false;
      var sync = function () { btn.setAttribute('aria-pressed', v.paused ? 'true' : 'false'); btn.setAttribute('aria-label', v.paused ? 'Play video' : 'Pause video'); };
      if (!calm) {
        new IntersectionObserver(function (es) {
          es.forEach(function (e) {
            if (e.isIntersecting && !manual) v.play().catch(function () {}); else v.pause();
            sync();
          });
        }, { threshold: .35 }).observe(v);
      }
      btn.addEventListener('click', function () { manual = true; if (v.paused) { v.play(); manual = false; } else v.pause(); sync(); });
      v.addEventListener('play', sync); v.addEventListener('pause', sync); sync();
    }
  });
})();
