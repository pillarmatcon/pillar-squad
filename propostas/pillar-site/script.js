// ==========================================================================
// Pillar — script.js
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {
  // Ano dinâmico no rodapé
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Número da ficha de pedido (hero) — gerado a cada carregamento
  const orderNoEl = document.getElementById('orderNo');
  if (orderNoEl) {
    const numero = Math.floor(100000 + Math.random() * 899999);
    orderNoEl.textContent = String(numero);
  }

  // Menu mobile
  const hamburger = document.getElementById('hamburger');
  const nav = document.getElementById('nav');

  if (hamburger && nav) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      nav.classList.toggle('active');
    });

    nav.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        nav.classList.remove('active');
      });
    });
  }

  // Header com sombra ao rolar
  const header = document.getElementById('header');
  const onScroll = () => {
    if (window.scrollY > 10) {
      header.style.boxShadow = '0 8px 24px rgba(0,0,0,0.25)';
    } else {
      header.style.boxShadow = 'none';
    }
  };
  window.addEventListener('scroll', onScroll);
  onScroll();

  // Máscara simples de telefone
  const telefoneInput = document.getElementById('telefone');
  if (telefoneInput) {
    telefoneInput.addEventListener('input', (e) => {
      let digits = e.target.value.replace(/\D/g, '').slice(0, 11);
      if (digits.length > 10) {
        digits = digits.replace(/(\d{2})(\d{5})(\d{0,4})/, '($1) $2-$3');
      } else if (digits.length > 6) {
        digits = digits.replace(/(\d{2})(\d{4})(\d{0,4})/, '($1) $2-$3');
      } else if (digits.length > 2) {
        digits = digits.replace(/(\d{2})(\d{0,5})/, '($1) $2');
      } else if (digits.length > 0) {
        digits = digits.replace(/(\d{0,2})/, '($1');
      }
      e.target.value = digits;
    });
  }

  // Envio do formulário de lead (placeholder — sem back-end)
  const leadForm = document.getElementById('leadForm');
  const formSuccess = document.getElementById('formSuccess');

  if (leadForm) {
    leadForm.addEventListener('submit', (e) => {
      e.preventDefault();

      if (!leadForm.checkValidity()) {
        leadForm.reportValidity();
        return;
      }

      const dados = {
        nome: leadForm.nome.value.trim(),
        telefone: leadForm.telefone.value.trim(),
        investimento: leadForm.investimento.value,
      };

      // TODO: substituir por chamada real a um endpoint / CRM
      console.log('Novo lead capturado:', dados);

      formSuccess.classList.add('show');
      leadForm.reset();

      setTimeout(() => formSuccess.classList.remove('show'), 6000);
    });
  }

  // Fade-in ao rolar para seções e cards
  const revealTargets = document.querySelectorAll(
    '.card, .step, .stat, .comparison__col, .mini-card, .testimonial__card'
  );

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  revealTargets.forEach((el) => {
    el.classList.add('reveal');
    observer.observe(el);
  });
});
