// fill these before the pitch; an empty link shows its button as "pronto"
const LINKS = {
  app: '',
  demo: '',
};

for (const el of document.querySelectorAll('[data-link]')) {
  const url = LINKS[el.dataset.link];
  if (url) {
    el.href = url;
    el.target = '_blank';
    el.rel = 'noopener';
  } else {
    el.setAttribute('aria-disabled', 'true');
    el.removeAttribute('href');
  }
}

const menu = document.getElementById('menu');
document.querySelector('.menu-button').addEventListener('click', () => menu.showModal());
menu.querySelector('.menu-close').addEventListener('click', () => menu.close());
menu.addEventListener('click', (event) => {
  if (event.target.closest('a')) menu.close();
});

const revealed = document.querySelectorAll('.reveal, .reveal-art, .levels');
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      // items that enter together cascade instead of appearing at once
      entries
        .filter((entry) => entry.isIntersecting)
        .forEach((entry, i) => {
          const el = entry.target;
          observer.unobserve(el);
          el.style.transitionDelay = `${Math.min(i, 5) * 60}ms`;
          const img = el.matches('.reveal-art') && el.querySelector('img');
          if (!img) return (el.dataset.visible = '');
          // open the curtain only once the painting can be shown
          img.loading = 'eager';
          img.decode().catch(() => {}).then(() => (el.dataset.visible = ''));
        });
    },
    { rootMargin: '0px 0px -12% 0px' },
  );
  revealed.forEach((el) => observer.observe(el));
} else {
  revealed.forEach((el) => (el.dataset.visible = ''));
}
