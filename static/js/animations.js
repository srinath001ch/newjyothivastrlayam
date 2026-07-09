/* =========================================================
   NEW JYOTHI VASTRALAYAM — Site Animations
   GSAP + AOS + custom interactions
   ========================================================= */

document.addEventListener('DOMContentLoaded', function () {

  /* ---------------- Site Loader ---------------- */
  const loader = document.getElementById('site-loader');
  if (loader) {
    window.addEventListener('load', () => {
      gsap.to(loader, {
        opacity: 0,
        duration: 0.8,
        delay: 0.3,
        onComplete: () => loader.style.display = 'none',
      });
    });
    // Fallback in case load event already fired
    setTimeout(() => {
      if (loader && loader.style.display !== 'none') {
        gsap.to(loader, { opacity: 0, duration: 0.8, onComplete: () => loader.style.display = 'none' });
      }
    }, 2500);
  }

  /* ---------------- AOS Init ---------------- */
  if (window.AOS) {
    AOS.init({
      duration: 900,
      easing: 'ease-out-cubic',
      once: true,
      offset: 80,
    });
  }

  /* ---------------- GSAP Register ---------------- */
  if (window.gsap && window.ScrollTrigger) {
    gsap.registerPlugin(ScrollTrigger);
  }

  /* ---------------- Navbar scroll state ---------------- */
  const navbar = document.getElementById('navbar');
  const onScroll = () => {
    if (!navbar) return;
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  };
  window.addEventListener('scroll', onScroll);
  onScroll();

  /* ---------------- Mobile Menu ---------------- */
  const menuBtn = document.getElementById('menu-btn');
  const closeMenuBtn = document.getElementById('close-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', () => mobileMenu.classList.add('open'));
  }
  if (closeMenuBtn && mobileMenu) {
    closeMenuBtn.addEventListener('click', () => mobileMenu.classList.remove('open'));
  }
  document.querySelectorAll('#mobile-menu a').forEach(link => {
    link.addEventListener('click', () => mobileMenu.classList.remove('open'));
  });

  /* ---------------- Hero title character animation ---------------- */
  document.querySelectorAll('.hero-title').forEach((titleEl) => {
    const text = titleEl.textContent;
    titleEl.textContent = '';
    text.split('').forEach((ch) => {
      const span = document.createElement('span');
      span.className = 'char';
      span.textContent = ch === ' ' ? '\u00A0' : ch;
      titleEl.appendChild(span);
    });
    if (window.gsap) {
      gsap.fromTo(titleEl.querySelectorAll('.char'),
        { y: 80, opacity: 0, rotateX: -40 },
        { y: 0, opacity: 1, rotateX: 0, duration: 1, ease: 'power4.out', stagger: 0.025, delay: 0.3 }
      );
    }
  });

  /* ---------------- Hero fade-ins ---------------- */
  if (window.gsap) {
    gsap.from('.hero-fade', {
      opacity: 0,
      y: 30,
      duration: 1,
      stagger: 0.2,
      delay: 1,
      ease: 'power3.out',
    });

    /* ---------------- Parallax hero background ---------------- */
    gsap.utils.toArray('.parallax-layer').forEach((layer) => {
      const speed = layer.dataset.speed || 0.4;
      gsap.to(layer, {
        yPercent: 30 * speed,
        ease: 'none',
        scrollTrigger: {
          trigger: layer.closest('section') || layer.parentElement,
          start: 'top bottom',
          end: 'bottom top',
          scrub: true,
        },
      });
    });

    /* ---------------- Section reveal-up (fallback for elements without AOS) ---------------- */
    gsap.utils.toArray('.gsap-reveal').forEach((el) => {
      gsap.fromTo(el,
        { opacity: 0, y: 60 },
        {
          opacity: 1, y: 0, duration: 1, ease: 'power3.out',
          scrollTrigger: { trigger: el, start: 'top 85%' },
        }
      );
    });

    /* ---------------- Stagger cards ---------------- */
    gsap.utils.toArray('.gsap-stagger-group').forEach((group) => {
      const items = group.querySelectorAll('.gsap-stagger-item');
      gsap.fromTo(items,
        { opacity: 0, y: 70 },
        {
          opacity: 1, y: 0, duration: 0.9, ease: 'power3.out', stagger: 0.12,
          scrollTrigger: { trigger: group, start: 'top 85%' },
        }
      );
    });

    /* ---------------- Image reveal masks ---------------- */
    gsap.utils.toArray('.reveal-wrap').forEach((wrap) => {
      const mask = wrap.querySelector('.reveal-mask');
      if (!mask) return;
      gsap.timeline({
        scrollTrigger: { trigger: wrap, start: 'top 80%' },
      })
      .to(mask, { scaleX: 1, transformOrigin: 'left', duration: 0.001 })
      .to(mask, { scaleX: 0, transformOrigin: 'right', duration: 0.9, ease: 'power4.inOut' })
      .from(wrap.querySelector('img'), { scale: 1.3, duration: 1.1, ease: 'power4.out' }, '-=0.9');
    });

    /* ---------------- Counter numbers ---------------- */
    gsap.utils.toArray('.counter-number').forEach((el) => {
      const target = parseFloat(el.dataset.target || el.textContent);
      const obj = { val: 0 };
      gsap.to(obj, {
        val: target,
        duration: 2,
        ease: 'power2.out',
        scrollTrigger: { trigger: el, start: 'top 90%' },
        onUpdate: () => {
          el.textContent = Math.floor(obj.val).toLocaleString('en-IN');
        },
      });
    });

    /* ---------------- Marquee pause on hover ---------------- */
    document.querySelectorAll('.marquee-wrap').forEach((wrap) => {
      const track = wrap.querySelector('.marquee-track');
      if (!track) return;
      wrap.addEventListener('mouseenter', () => track.style.animationPlayState = 'paused');
      wrap.addEventListener('mouseleave', () => track.style.animationPlayState = 'running');
    });
  }

  /* ---------------- Tilt effect on cards ---------------- */
  document.querySelectorAll('.tilt-card').forEach((card) => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const rotateX = ((y / rect.height) - 0.5) * -10;
      const rotateY = ((x / rect.width) - 0.5) * 10;
      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale(1)';
    });
  });

  /* ---------------- Product Swiper (product detail gallery) ---------------- */
  const productThumbs = document.querySelector('.product-thumbs');
  let thumbsSwiper = null;
  if (productThumbs && window.Swiper) {
    thumbsSwiper = new Swiper('.product-thumbs', {
      spaceBetween: 12,
      slidesPerView: 4,
      freeMode: true,
      watchSlidesProgress: true,
    });
  }
  const productMain = document.querySelector('.product-main-swiper');
  if (productMain && window.Swiper) {
    new Swiper('.product-main-swiper', {
      spaceBetween: 0,
      effect: 'fade',
      fadeEffect: { crossFade: true },
      navigation: {
        nextEl: '.product-next',
        prevEl: '.product-prev',
      },
      thumbs: thumbsSwiper ? { swiper: thumbsSwiper } : undefined,
    });
  }

  /* ---------------- Featured / Latest saree swiper (home) ---------------- */
  document.querySelectorAll('.saree-swiper').forEach((el, idx) => {
    if (!window.Swiper) return;
    if (!el.classList.contains('swiper-init-' + idx)) {
      el.classList.add('swiper-init-' + idx);
      new Swiper(el, {
        slidesPerView: 1.15,
        spaceBetween: 20,
        navigation: {
          nextEl: el.parentElement.querySelector('.swiper-next-btn'),
          prevEl: el.parentElement.querySelector('.swiper-prev-btn'),
        },
        breakpoints: {
          640: { slidesPerView: 2.2, spaceBetween: 24 },
          1024: { slidesPerView: 3.3, spaceBetween: 28 },
          1280: { slidesPerView: 4, spaceBetween: 30 },
        },
      });
    }
  });

  /* ---------------- Testimonial / Category Swiper ---------------- */
  document.querySelectorAll('.category-swiper').forEach((el) => {
    if (!window.Swiper) return;
    new Swiper(el, {
      slidesPerView: 1.3,
      spaceBetween: 18,
      centeredSlides: false,
      breakpoints: {
        640: { slidesPerView: 2.3 },
        1024: { slidesPerView: 4 },
      },
    });
  });

  /* ---------------- Smooth anchor scrolling ---------------- */
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId.length > 1) {
        const target = document.querySelector(targetId);
        if (target) {
          e.preventDefault();
          window.scrollTo({
            top: target.offsetTop - 90,
            behavior: 'smooth',
          });
        }
      }
    });
  });

});
