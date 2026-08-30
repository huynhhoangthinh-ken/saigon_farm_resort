// ---- MOBILE MENU (prepended) ----
function closeMobileMenu() {
  var drawer = document.getElementById('mobileMenuDrawer');
  var overlay = document.getElementById('mobileMenuOverlay');
  if (drawer) drawer.classList.remove('open');
  if (overlay) overlay.classList.remove('open');
  document.body.style.overflow = '';
}
function openMobileMenu() {
  var drawer = document.getElementById('mobileMenuDrawer');
  var overlay = document.getElementById('mobileMenuOverlay');
  if (drawer) drawer.classList.add('open');
  if (overlay) overlay.classList.add('open');
  document.body.style.overflow = 'hidden';
}
// Main Application JS

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Trending Carousel Controls
  const track = document.getElementById('trendingTrack');
  const prevBtn = document.getElementById('trendPrevBtn');
  const nextBtn = document.getElementById('trendNextBtn');

  if (track && prevBtn && nextBtn) {
    const scrollAmount = 270;

    nextBtn.addEventListener('click', () => {
      track.parentElement.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    });

    prevBtn.addEventListener('click', () => {
      track.parentElement.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    });
  }

// Global Tab Activation Function
window.activateTab = function(tabId) {
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');
  const navLinks = document.querySelectorAll('.nav-link');

  tabBtns.forEach(b => b.classList.toggle('active', b.getAttribute('data-tab') === tabId));
  tabContents.forEach(c => c.classList.toggle('active', c.id === tabId));
  navLinks.forEach(l => l.classList.toggle('active', l.getAttribute('data-target') === tabId));

  const tabsSection = document.querySelector('.tabs-section');
  if (tabsSection) {
    tabsSection.scrollIntoView({ behavior: 'smooth' });
  }
};

  // Hero Auto Slider Logic
  const heroSlides = document.querySelectorAll('#heroAutoSlider .hero-slide');
  const heroPrevBtn = document.getElementById('heroPrevBtn');
  const heroNextBtn = document.getElementById('heroNextBtn');
  let currentHeroIdx = 0;
  let heroTimer = null;

  function showHeroSlide(index) {
    if (heroSlides.length === 0) return;
    heroSlides.forEach((slide, idx) => {
      slide.classList.toggle('active', idx === index);
    });
    currentHeroIdx = index;
  }

  function nextHeroSlide() {
    let nextIdx = (currentHeroIdx + 1) % heroSlides.length;
    showHeroSlide(nextIdx);
  }

  function prevHeroSlide() {
    let prevIdx = (currentHeroIdx - 1 + heroSlides.length) % heroSlides.length;
    showHeroSlide(prevIdx);
  }

  function resetHeroTimer() {
    if (heroTimer) clearInterval(heroTimer);
    if (heroSlides.length > 0) {
      heroTimer = setInterval(nextHeroSlide, 8000);
    }
  }

  if (heroSlides.length > 0) {
    resetHeroTimer();
  }

  if (heroNextBtn) {
    heroNextBtn.addEventListener('click', () => {
      nextHeroSlide();
      resetHeroTimer();
    });
  }

  if (heroPrevBtn) {
    heroPrevBtn.addEventListener('click', () => {
      prevHeroSlide();
      resetHeroTimer();
    });
  }

  // Tabs Switching Logic
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      // Remove active classes
      tabBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));
      
      // Add active class to clicked
      btn.classList.add('active');
      const targetId = btn.getAttribute('data-tab');
      document.getElementById(targetId).classList.add('active');
    });
  });

  // Sub-tabs Switching Logic
  const subTabBtns = document.querySelectorAll('.sub-tab-btn');
  const subTabContents = document.querySelectorAll('.sub-tab-content');

  subTabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const parentTab = btn.closest('.tab-content');
      const btnsInParent = parentTab.querySelectorAll('.sub-tab-btn');
      const contentsInParent = parentTab.querySelectorAll('.sub-tab-content');
      
      btnsInParent.forEach(b => b.classList.remove('active'));
      contentsInParent.forEach(c => c.classList.remove('active'));
      
      btn.classList.add('active');
      const targetId = btn.getAttribute('data-subtab');
      document.getElementById(targetId).classList.add('active');
    });
  });

  // Main Navigation Links Logic
  const navLinks = document.querySelectorAll('.nav-link');
  const tabsSection = document.querySelector('.tabs-section');
  
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      
      if (tabsSection) {
        tabsSection.scrollIntoView({ behavior: 'smooth' });
      }

      const targetTabId = link.getAttribute('data-target');
      if(targetTabId) {
        const targetTabBtn = document.querySelector(`.tab-btn[data-tab="${targetTabId}"]`);
        if(targetTabBtn) {
           targetTabBtn.click();
        }
      }
      
      navLinks.forEach(l => l.classList.remove('active'));
      link.classList.add('active');
    });
  });

  // Fetch JSON and render Editorial Posts
  const editorialGrid = document.getElementById('editorial-grid');
  if (editorialGrid) {
    function renderEditorialList(posts) {
      editorialGrid.innerHTML = ''; // clear initial content
      posts.forEach(post => {
        const postHTML = `
          <div class="grid-card">
            <a href="article.html?id=${post.id}" style="display: block; text-decoration: none; color: inherit;">
              <div class="grid-img">
                 <img src="${post.image}" alt="${post.title}" loading="lazy">
                 <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
              </div>
            </a>
            <div class="grid-card-info">
              <a href="article.html?id=${post.id}" style="text-decoration: none; color: inherit;">
                <h5 style="margin-bottom: 8px; line-height: 1.4;">${post.title}</h5>
              </a>
              <p style="font-weight: 400; font-size: 0.85rem; color: #555; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; margin-bottom: 14px;">
                ${post.excerpt}
              </p>
              <div style="display: flex; gap: 8px; margin-top: auto; flex-wrap: wrap;">
                <a href="article.html?id=${post.id}" class="editorial-btn" style="margin-top:0;">Đọc tiếp</a>
                <a href="https://zalo.me/0906060036" target="_blank" class="editorial-btn" style="margin-top:0; background-color: #0068FF; color: white; border-color: #0068FF;">
                  Hotline Zalo
                </a>
              </div>
            </div>
          </div>
        `;
        editorialGrid.insertAdjacentHTML('beforeend', postHTML);
      });
    }

    if (window.SAIGON_POSTS && Array.isArray(window.SAIGON_POSTS) && window.SAIGON_POSTS.length > 0) {
      renderEditorialList(window.SAIGON_POSTS);
    } else {
      fetch('data/posts.json?v=' + Date.now())
        .then(response => response.json())
        .then(posts => {
          window.SAIGON_POSTS = posts;
          renderEditorialList(posts);
        })
        .catch(err => console.error("Error fetching posts:", err));
    }
  }
});

// ---- MOBILE MENU INIT (added for responsive) ----
document.addEventListener('DOMContentLoaded', function() {
  // Show/hide hamburger based on viewport
  var mobileMenuBtn = document.getElementById('mobileMenuBtn');
  var mobileMenuClose = document.getElementById('mobileMenuClose');
  var mobileMenuOverlay = document.getElementById('mobileMenuOverlay');

  function updateHamburger() {
    if (mobileMenuBtn) {
      mobileMenuBtn.style.display = window.innerWidth <= 768 ? 'flex' : 'none';
    }
  }
  updateHamburger();
  window.addEventListener('resize', updateHamburger);

  if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', openMobileMenu);
  if (mobileMenuClose) mobileMenuClose.addEventListener('click', closeMobileMenu);
  if (mobileMenuOverlay) mobileMenuOverlay.addEventListener('click', closeMobileMenu);

  // Mobile drawer links: switch tab + close + scroll
  document.querySelectorAll('.mobile-menu-links a[data-tab]').forEach(function(link) {
    link.addEventListener('click', function(e) {
      var tabId = link.getAttribute('data-tab');
      if (tabId) {
        document.querySelectorAll('.tab-btn').forEach(function(btn) {
          btn.classList.toggle('active', btn.getAttribute('data-tab') === tabId);
        });
        document.querySelectorAll('.tab-content').forEach(function(tc) {
          tc.classList.toggle('active', tc.id === tabId);
        });
        var tabsSec = document.querySelector('.tabs-section');
        if (tabsSec) setTimeout(function() { tabsSec.scrollIntoView({behavior: 'smooth'}); }, 280);
      }
      closeMobileMenu();
    });
  });

  // Sticky header on scroll for desktop
  var header = document.querySelector('.main-header');
  window.addEventListener('scroll', function() {
    if (!header) return;
    if (window.innerWidth > 768) {
      if (window.scrollY > 80) {
        header.style.cssText = 'position:fixed;top:0;background:rgba(10,10,10,0.95);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);padding:12px 0;transition:all 0.3s ease;';
      } else {
        header.style.cssText = 'position:absolute;top:38px;background:linear-gradient(180deg,rgba(0,0,0,0.65) 0%,rgba(0,0,0,0) 100%);padding:20px 0;';
      }
    }
  });

  // Swipe gesture for hero slider on mobile
  var hero = document.getElementById('heroAutoSlider');
  if (hero) {
    var touchStartX = 0;
    hero.addEventListener('touchstart', function(e) { touchStartX = e.touches[0].clientX; }, {passive: true});
    hero.addEventListener('touchend', function(e) {
      var diff = touchStartX - e.changedTouches[0].clientX;
      if (Math.abs(diff) > 50) {
        var btn = diff > 0 ? document.getElementById('heroNextBtn') : document.getElementById('heroPrevBtn');
        if (btn) btn.click();
      }
    }, {passive: true});
  }
});
