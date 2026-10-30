(function () {
  // Mobile menu
  var btn = document.querySelector('.menu-btn');
  var nav = document.querySelector('nav.main');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // ZIP checker
  document.querySelectorAll('form[data-zipcheck]').forEach(function (form) {
    var input = form.querySelector('input');
    var out = form.parentNode.querySelector('.zip-result');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var z = (input.value || '').replace(/\D/g, '').slice(0, 5);
      out.className = 'zip-result';
      if (z.length !== 5) {
        out.textContent = 'Please enter a 5-digit ZIP code.';
        out.classList.add('no');
        return;
      }
      var nc = window.NC_ZIPS || {};
      var all = window.COVERED_ZIPS || '';
      var phone = document.body.getAttribute('data-phone');
      var tel = document.body.getAttribute('data-tel');
      if (nc[z]) {
        var parts = nc[z].split('|');
        out.innerHTML = 'Good news - ZIP ' + z + ' (' + parts[1] + ', NC) is in our service area. ' +
          '<a href="/north-carolina/' + parts[0] + '/">See ' + parts[1] + ' page</a> or call <a href="tel:' + tel + '">' + phone + '</a>.';
        out.classList.add('ok');
      } else if (all.indexOf(',' + z + ',') !== -1) {
        out.innerHTML = 'ZIP ' + z + ' is covered. Call <a href="tel:' + tel + '">' + phone + '</a> to be connected with a local provider.';
        out.classList.add('ok');
      } else {
        out.textContent = 'Sorry, ZIP ' + z + ' is not in our service area yet.';
        out.classList.add('no');
      }
    });
  });

  // City filter on state hub
  var filter = document.querySelector('[data-cityfilter]');
  if (filter) {
    filter.addEventListener('input', function () {
      var q = filter.value.trim().toLowerCase();
      document.querySelectorAll('.county-block').forEach(function (block) {
        var any = false;
        block.querySelectorAll('li').forEach(function (li) {
          var hit = !q || li.textContent.toLowerCase().indexOf(q) !== -1 ||
            block.getAttribute('data-county').indexOf(q) !== -1;
          li.style.display = hit ? '' : 'none';
          if (hit) any = true;
        });
        block.style.display = any ? '' : 'none';
      });
    });
  }
})();
