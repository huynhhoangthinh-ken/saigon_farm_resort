// ---- GLOBAL IMAGE FALLBACK & SELF-HEALING ----
window.addEventListener('error', function(e) {
  if (e.target && e.target.tagName === 'IMG') {
    const img = e.target;
    if (!img.dataset.hasHandledError) {
      img.dataset.hasHandledError = 'true';
      img.src = 'assets/Index_asset/hero_slide_new/SGFR_H01.webp';
    }
  }
}, true);

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

// // Global Tab Activation Function (Backward Compatibility & Anchor Scroll)
window.activateTab = function(tabId) {
  const map = {
    'tab-villas-market': 'biet-phu',
    'tab-heritage': 'ban-sac',
    'tab-amenities': 'tien-ich',
    'tab-masterplan': 'quy-hoach',
    'tab-editorial': 'tap-chi'
  };
  const targetId = map[tabId] || tabId;
  const targetElem = document.getElementById(targetId);
  if (targetElem) {
    const headerOffset = 75;
    const elementPosition = targetElem.getBoundingClientRect().top;
    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
    window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
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

  // Sub-tabs Switching Logic (Cho 48 Chuyên Đề Phân Tích & Sub-sections)
  const subTabBtns = document.querySelectorAll('.sub-tab-btn');
  const subTabContents = document.querySelectorAll('.sub-tab-content');

  subTabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const parentContainer = btn.closest('.story-section') || btn.closest('.tab-content') || document;
      const btnsInParent = parentContainer.querySelectorAll('.sub-tab-btn');
      const contentsInParent = parentContainer.querySelectorAll('.sub-tab-content');
      
      btnsInParent.forEach(b => b.classList.remove('active'));
      contentsInParent.forEach(c => c.classList.remove('active'));
      
      btn.classList.add('active');
      const targetId = btn.getAttribute('data-subtab');
      const targetElem = document.getElementById(targetId);
      if (targetElem) {
        targetElem.classList.add('active');
      }
    });
  });

  // Smooth Scroll with Header Offset for Navigation & In-page Anchors
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href === '#' || href === '#!') return;
      const targetElem = document.querySelector(href);
      if (targetElem) {
        e.preventDefault();
        const headerOffset = 75;
        const elementPosition = targetElem.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
        window.scrollTo({ top: offsetPosition, behavior: 'smooth' });

        if (typeof closeMobileMenu === 'function') {
          closeMobileMenu();
        }
      }
    });
  });

  // Scrollspy: Highlight Active Nav Link on Scroll
  const spySections = document.querySelectorAll('.story-section[id], .location-section[id]');
  const mainNavLinks = document.querySelectorAll('.nav-menu-links .nav-link');

  function updateActiveNavOnScroll() {
    const scrollY = window.pageYOffset;
    spySections.forEach(current => {
      const sectionHeight = current.offsetHeight;
      const sectionTop = current.offsetTop - 120;
      const sectionId = current.getAttribute('id');
      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        mainNavLinks.forEach(link => {
          if (link.getAttribute('href') === `#${sectionId}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }
  window.addEventListener('scroll', updateActiveNavOnScroll, { passive: true });

  // Fetch JSON and render Editorial Posts
  const editorialGrid = document.getElementById('editorial-grid');
  if (editorialGrid) {
    function toSlug(str) {
      return (str || '').normalize('NFD')
        .replace(/[\u0300-\u036f]/g, '')
        .replace(/đ/g, 'd').replace(/Đ/g, 'd')
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-+|-+$/g, '');
    }

    function createPostHTML(post) {
      const slug = toSlug(post.title);
      return `
        <div class="grid-card">
          <a href="bai-viet/${slug}.html" style="display: block; text-decoration: none; color: inherit;">
            <div class="grid-img">
               <img src="${post.image}" alt="${post.title}" loading="lazy">
               <span class="minh-hoa-tag">* Hình ảnh minh họa</span>
            </div>
          </a>
          <div class="grid-card-info">
            <a href="bai-viet/${slug}.html" style="text-decoration: none; color: inherit;">
              <h5 style="margin-bottom: 8px; line-height: 1.4;">${post.title}</h5>
            </a>
            <p style="font-weight: 400; font-size: 0.85rem; color: #555; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; margin-bottom: 14px;">
              ${post.excerpt}
            </p>
            <div style="display: flex; gap: 8px; margin-top: auto; flex-wrap: wrap;">
              <a href="bai-viet/${slug}.html" class="editorial-btn" style="margin-top:0;">Đọc tiếp</a>
            </div>
          </div>
        </div>
      `;
    }

    let editorialOffset = editorialGrid.children.length; // Already pre-rendered 12
    const loadMoreWrap = document.getElementById('load-more-editorial-wrap');

    window.loadMoreEditorialPosts = function() {
      function appendBatch(posts) {
        const nextBatch = posts.slice(editorialOffset, editorialOffset + 12);
        nextBatch.forEach(post => {
          editorialGrid.insertAdjacentHTML('beforeend', createPostHTML(post));
        });
        editorialOffset += nextBatch.length;
        if (editorialOffset >= posts.length && loadMoreWrap) {
          loadMoreWrap.style.display = 'none';
        }
      }

      if (window.SAIGON_POSTS && Array.isArray(window.SAIGON_POSTS) && window.SAIGON_POSTS.length > 0) {
        appendBatch(window.SAIGON_POSTS);
      } else {
        fetch('data/posts.json?v=' + Date.now())
          .then(response => response.json())
          .then(posts => {
            window.SAIGON_POSTS = posts;
            appendBatch(posts);
          })
          .catch(err => console.error("Error fetching posts:", err));
      }
    };

    // If no posts were pre-rendered, load the first batch
    if (editorialGrid.children.length === 0) {
      window.loadMoreEditorialPosts();
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

  // Sticky header on scroll for desktop (Nền trong, chữ đen nhã nhặn sang trọng)
  var header = document.querySelector('.main-header');
  function updateHeaderScroll() {
    if (!header) return;
    // Clear any inline styles that might have been injected
    header.style.background = '';
    header.style.backgroundColor = '';
    if (window.innerWidth > 768) {
      if (window.scrollY > 50) {
        header.classList.add('scrolled-light');
      } else {
        header.classList.remove('scrolled-light');
      }
    } else {
      header.classList.remove('scrolled-light');
    }
  }
  window.addEventListener('scroll', updateHeaderScroll, {passive: true});
  window.addEventListener('resize', updateHeaderScroll, {passive: true});
  updateHeaderScroll();

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

  // Global Image Fallback Safety Net: Prevents any broken image icon from displaying
  window.addEventListener('error', function(e) {
    if (e.target && e.target.tagName === 'IMG') {
      var img = e.target;
      if (!img.dataset.fallbackTried) {
        img.dataset.fallbackTried = 'true';
        img.src = 'assets/Index_asset/Phoicanh/S01_Final_Fix.jpg';
      }
    }
  }, true);

  // Amenities Directory Zone Switcher & Search
  window.switchAmenityZone = function(zone) {
    var btns = document.querySelectorAll('.amenity-zone-btn');
    btns.forEach(function(b) {
      if (b.dataset.zone === zone) b.classList.add('active');
      else b.classList.remove('active');
    });

    var panelCentral = document.getElementById('zone-central-panel');
    var panelLake = document.getElementById('zone-lake-panel');
    if (panelCentral && panelLake) {
      if (zone === 'central') {
        panelCentral.style.display = 'grid';
        panelLake.style.display = 'none';
      } else {
        panelCentral.style.display = 'none';
        panelLake.style.display = 'grid';
      }
    }
    // Re-apply filter if search box has value
    var searchInput = document.getElementById('amenitySearchInput');
    if (searchInput && searchInput.value.trim() !== '') {
      window.filterAmenities(searchInput.value);
    }
  };

  window.filterAmenities = function(query) {
    var q = (query || '').toLowerCase().trim();
    var activeZone = document.querySelector('.amenity-zone-btn.active');
    var currentZone = activeZone ? activeZone.dataset.zone : 'central';
    var targetPanel = currentZone === 'central' ? document.getElementById('zone-central-panel') : document.getElementById('zone-lake-panel');
    if (!targetPanel) return;

    var items = targetPanel.querySelectorAll('.amenity-pill-item');
    items.forEach(function(item) {
      var text = item.textContent.toLowerCase();
      if (!q || text.indexOf(q) !== -1) {
        item.style.display = 'flex';
      } else {
        item.style.display = 'none';
      }
    });
  };
});

