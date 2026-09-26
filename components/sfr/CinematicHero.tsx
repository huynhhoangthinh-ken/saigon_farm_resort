'use client';

import React, { useEffect, useRef, useState } from 'react';

// Toggle debug overlay
const DEBUG = true;

export default function CinematicHero() {
  const containerRef = useRef<HTMLDivElement>(null);
  const videoRef = useRef<HTMLVideoElement>(null);

  // Animation & Scrub Refs (using refs to avoid 60fps React re-renders)
  const targetProgressRef = useRef<number>(0);
  const currentProgressRef = useRef<number>(0);
  const targetTimeRef = useRef<number>(0);
  const currentTimeRef = useRef<number>(0);
  const rafIdRef = useRef<number | null>(null);
  const durationRef = useRef<number>(0);

  // Overlay DOM element refs for direct 60fps DOM updates without React re-rendering
  const introOverlayRef = useRef<HTMLDivElement>(null);
  const endOverlayRef = useRef<HTMLDivElement>(null);
  const darkBackdropRef = useRef<HTMLDivElement>(null);
  const progressBarRef = useRef<HTMLDivElement>(null);

  // Debug HUD refs
  const debugProgressRef = useRef<HTMLSpanElement>(null);
  const debugTimeRef = useRef<HTMLSpanElement>(null);
  const debugDurationRef = useRef<HTMLSpanElement>(null);

  // Component state for initial load only
  const [isReady, setIsReady] = useState(false);
  const [duration, setDuration] = useState<number>(0);

  useEffect(() => {
    const video = videoRef.current;
    const container = containerRef.current;
    if (!video || !container) return;

    // Check prefers-reduced-motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const lerpFactor = prefersReducedMotion ? 0.4 : 0.16;

    // 1. Video Metadata Loaded
    const handleLoadedMetadata = () => {
      const vidDuration = video.duration || 10.07;
      durationRef.current = vidDuration;
      setDuration(vidDuration);
      setIsReady(true);
      // Ensure video is paused at start frame
      video.pause();
      video.currentTime = 0;
    };

    if (video.readyState >= 1) {
      handleLoadedMetadata();
    } else {
      video.addEventListener('loadedmetadata', handleLoadedMetadata);
    }

    // 2. Passive Scroll Listener
    const handleScroll = () => {
      if (!container) return;
      const rect = container.getBoundingClientRect();
      const viewportHeight = window.innerHeight;
      const totalScrollableDistance = rect.height - viewportHeight;

      if (totalScrollableDistance <= 0) return;

      // Distance scrolled within the hero container
      const scrolled = -rect.top;
      const progress = Math.min(Math.max(scrolled / totalScrollableDistance, 0), 1);

      targetProgressRef.current = progress;
      if (durationRef.current > 0) {
        targetTimeRef.current = progress * durationRef.current;
      }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    window.addEventListener('resize', handleScroll, { passive: true });
    handleScroll();

    // 3. Smooth rAF Scrub Loop
    const updateScrub = () => {
      const current = currentTimeRef.current;
      const target = targetTimeRef.current;
      const progress = currentProgressRef.current;
      const targetProg = targetProgressRef.current;

      // Smooth interpolation (LERP)
      const newTime = current + (target - current) * lerpFactor;
      currentTimeRef.current = newTime;

      const newProgress = progress + (targetProg - progress) * lerpFactor;
      currentProgressRef.current = newProgress;

      // Scrub the video frame if difference is meaningful
      if (video && video.readyState >= 2) {
        const delta = Math.abs(video.currentTime - newTime);
        if (delta > 0.008) {
          // Keep video paused, assign exact frame
          video.currentTime = Math.min(Math.max(newTime, 0), durationRef.current || 10);
        }
      }

      // Update Intro Overlay (fades out from progress 0.0 to 0.20)
      if (introOverlayRef.current) {
        // Fade starts immediately and finishes by 20% scroll
        const introOpacity = Math.max(0, Math.min(1, 1 - newProgress / 0.18));
        const introTranslate = -newProgress * 120;
        introOverlayRef.current.style.opacity = introOpacity.toFixed(3);
        introOverlayRef.current.style.transform = `translate3d(0, ${introTranslate.toFixed(1)}px, 0)`;
        introOverlayRef.current.style.pointerEvents = introOpacity <= 0.05 ? 'none' : 'auto';
      }

      // Update End Overlay (fades in from progress 0.88 to 1.0)
      if (endOverlayRef.current && darkBackdropRef.current) {
        // Dark backdrop appears gently between 80% and 100%
        const backdropOpacity = Math.max(0, Math.min(0.55, (newProgress - 0.78) / 0.18 * 0.55));
        darkBackdropRef.current.style.opacity = backdropOpacity.toFixed(3);

        // Content appears between 88% and 98%
        const endOpacity = Math.max(0, Math.min(1, (newProgress - 0.86) / 0.10));
        const endTranslate = (1 - endOpacity) * 40;
        endOverlayRef.current.style.opacity = endOpacity.toFixed(3);
        endOverlayRef.current.style.transform = `translate3d(0, ${endTranslate.toFixed(1)}px, 0)`;
        endOverlayRef.current.style.pointerEvents = endOpacity <= 0.05 ? 'none' : 'auto';
      }

      // Update Hairline Progress Bar
      if (progressBarRef.current) {
        progressBarRef.current.style.width = `${(newProgress * 100).toFixed(2)}%`;
      }

      // Update Debug HUD directly without React re-render
      if (DEBUG) {
        if (debugProgressRef.current) {
          debugProgressRef.current.textContent = `${(newProgress * 100).toFixed(1)}%`;
        }
        if (debugTimeRef.current) {
          debugTimeRef.current.textContent = `${(video ? video.currentTime : newTime).toFixed(2)}s`;
        }
        if (debugDurationRef.current) {
          debugDurationRef.current.textContent = `${durationRef.current.toFixed(2)}s`;
        }
      }

      rafIdRef.current = requestAnimationFrame(updateScrub);
    };

    rafIdRef.current = requestAnimationFrame(updateScrub);

    // Cleanup on unmount
    return () => {
      window.removeEventListener('scroll', handleScroll);
      window.removeEventListener('resize', handleScroll);
      video.removeEventListener('loadedmetadata', handleLoadedMetadata);
      if (rafIdRef.current) {
        cancelAnimationFrame(rafIdRef.current);
      }
    };
  }, []);

  return (
    <div
      ref={containerRef}
      className="relative w-full bg-black h-[380vh] md:h-[500vh]"
    >
      {/* Sticky Full-Screen Viewport */}
      <div className="sticky top-0 h-screen w-full overflow-hidden bg-black flex items-center justify-center">
        {/* Video Element */}
        <video
          ref={videoRef}
          src="/videos/saigon-farm-cinematic.mp4"
          muted
          playsInline
          preload="auto"
          controls={false}
          loop={false}
          autoPlay={false}
          className="absolute inset-0 w-full h-full object-cover select-none pointer-events-none"
        />

        {/* Subtle Ambient Vignette Overlay */}
        <div className="absolute inset-0 bg-radial-[circle_at_center,transparent_40%,rgba(0,0,0,0.65)_100%] pointer-events-none" />

        {/* Dynamic Dark Backdrop for Video Ending */}
        <div
          ref={darkBackdropRef}
          className="absolute inset-0 bg-black/60 opacity-0 pointer-events-none transition-opacity duration-75"
        />

        {/* Top/Bottom Cinematic Letterbox Gradients */}
        <div className="absolute top-0 inset-x-0 h-32 bg-gradient-to-b from-black/80 via-black/30 to-transparent pointer-events-none" />
        <div className="absolute bottom-0 inset-x-0 h-40 bg-gradient-to-t from-black/90 via-black/40 to-transparent pointer-events-none" />

        {/* INTRODUCTORY OVERLAY (0% - 20% scroll) */}
        <div
          ref={introOverlayRef}
          className="relative z-10 flex flex-col items-center justify-center text-center px-6 max-w-4xl mx-auto will-change-transform"
        >
          {/* Subtle Tagline Badge */}
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full border border-[#d4af37]/30 bg-black/40 backdrop-blur-md mb-6 md:mb-8">
            <span className="w-1.5 h-1.5 rounded-full bg-[#d4af37] animate-pulse" />
            <span className="text-[11px] md:text-xs tracking-[0.25em] text-[#e8c872] uppercase font-medium">
              Tuyệt Tác Điền Trang Nghỉ Dưỡng Sinh Thái
            </span>
          </div>

          {/* Main Title */}
          <h1 className="font-['Cinzel',serif] text-4xl sm:text-6xl md:text-7xl lg:text-8xl tracking-[0.18em] font-medium text-white uppercase drop-shadow-[0_4px_24px_rgba(0,0,0,0.8)] mb-4 md:mb-6">
            SAIGON FARM RESORT
          </h1>

          {/* Elegant Subtitle */}
          <p className="font-['Montserrat',sans-serif] text-sm sm:text-base md:text-xl text-[#f3ece2]/90 font-light tracking-wide max-w-2xl leading-relaxed drop-shadow-[0_2px_12px_rgba(0,0,0,0.9)] mb-10 md:mb-14">
            Một miền sống được dệt từ đất, nước và ký ức Việt.
          </p>

          {/* Scroll to Enter Indicator */}
          <div className="flex flex-col items-center gap-3">
            <span className="text-[10px] md:text-xs tracking-[0.35em] text-[#d4af37] uppercase font-medium">
              SCROLL TO ENTER
            </span>
            <div className="w-[1px] h-10 md:h-14 bg-gradient-to-b from-[#d4af37] to-transparent animate-pulse" />
          </div>
        </div>

        {/* ENDING OVERLAY (88% - 100% scroll) */}
        <div
          ref={endOverlayRef}
          className="absolute z-20 inset-0 flex flex-col items-center justify-center text-center px-6 opacity-0 pointer-events-none will-change-transform"
        >
          <div className="max-w-4xl mx-auto flex flex-col items-center">
            {/* Primary Headline */}
            <h2 className="font-['Cinzel',serif] text-2xl sm:text-4xl md:text-5xl lg:text-6xl tracking-[0.2em] font-semibold text-white uppercase drop-shadow-[0_4px_30px_rgba(0,0,0,0.9)] mb-8 md:mb-12">
              <span className="text-[#f7e7a9]">VEN HỒ</span> — <span className="text-white">KỀ BIỂN</span> — <span className="text-[#d4af37]">CẬN PHỐ</span>
            </h2>

            {/* Key Pillars Grid */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-8 w-full max-w-3xl">
              <div className="p-4 md:p-6 rounded-xl border border-[#d4af37]/20 bg-black/50 backdrop-blur-md flex flex-col items-center">
                <span className="font-['Cinzel',serif] text-xl md:text-3xl font-bold text-[#f7e7a9] mb-1">
                  100 HA
                </span>
                <span className="text-[11px] md:text-xs tracking-[0.15em] text-white/80 uppercase font-light">
                  HỒ TỰ NHIÊN
                </span>
              </div>

              <div className="p-4 md:p-6 rounded-xl border border-[#d4af37]/20 bg-black/50 backdrop-blur-md flex flex-col items-center">
                <span className="font-['Cinzel',serif] text-xl md:text-3xl font-bold text-[#f7e7a9] mb-1">
                  3 MẶT
                </span>
                <span className="text-[11px] md:text-xs tracking-[0.15em] text-white/80 uppercase font-light">
                  ĐỒNG LÚA
                </span>
              </div>

              <div className="p-4 md:p-6 rounded-xl border border-[#d4af37]/20 bg-black/50 backdrop-blur-md flex flex-col items-center">
                <span className="font-['Cinzel',serif] text-xl md:text-3xl font-bold text-[#f7e7a9] mb-1">
                  15 PHÚT
                </span>
                <span className="text-[11px] md:text-xs tracking-[0.15em] text-white/80 uppercase font-light">
                  HỒ TRÀM
                </span>
              </div>

              <div className="p-4 md:p-6 rounded-xl border border-[#d4af37]/20 bg-black/50 backdrop-blur-md flex flex-col items-center">
                <span className="font-['Cinzel',serif] text-xl md:text-3xl font-bold text-[#f7e7a9] mb-1">
                  60–75P
                </span>
                <span className="text-[11px] md:text-xs tracking-[0.15em] text-white/80 uppercase font-light">
                  TP. HỒ CHÍ MINH
                </span>
              </div>
            </div>

            {/* Subtle Down Indicator */}
            <div className="mt-10 md:mt-14 flex items-center gap-2 text-white/60 text-xs tracking-[0.2em] uppercase font-light">
              <span>Cuộn tiếp để khám phá chương mới</span>
              <svg className="w-4 h-4 animate-bounce text-[#d4af37]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
              </svg>
            </div>
          </div>
        </div>

        {/* Minimal Bottom Hairline Progress Indicator */}
        <div className="absolute bottom-0 inset-x-0 h-[2px] bg-white/10 z-30">
          <div
            ref={progressBarRef}
            className="h-full bg-gradient-to-r from-[#d4af37] via-[#f7e7a9] to-[#d4af37] w-0 transition-[width] duration-75 ease-out"
          />
        </div>

        {/* Initial Loading State */}
        {!isReady && (
          <div className="absolute inset-0 bg-black z-40 flex flex-col items-center justify-center gap-4 transition-opacity duration-500">
            <div className="w-8 h-8 rounded-full border-2 border-[#d4af37]/20 border-t-[#d4af37] animate-spin" />
            <span className="text-xs tracking-[0.3em] uppercase text-[#d4af37]/70 font-light">
              Đang chuẩn bị thước phim...
            </span>
          </div>
        )}

        {/* DEBUG HUD (Top-Left) */}
        {DEBUG && (
          <div className="absolute top-4 left-4 z-50 bg-black/80 backdrop-blur-md border border-white/15 px-3 py-2.5 rounded-lg font-mono text-[11px] text-white/90 shadow-xl pointer-events-none select-none flex flex-col gap-1">
            <div className="flex items-center gap-2 border-b border-white/10 pb-1 text-[#d4af37] font-semibold">
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
              HERO SCROLL DEBUG
            </div>
            <div className="flex justify-between gap-4">
              <span className="text-white/50">Scroll Progress:</span>
              <span ref={debugProgressRef} className="font-bold text-[#f7e7a9]">0.0%</span>
            </div>
            <div className="flex justify-between gap-4">
              <span className="text-white/50">Current Time:</span>
              <span ref={debugTimeRef} className="font-bold text-white">0.00s</span>
            </div>
            <div className="flex justify-between gap-4">
              <span className="text-white/50">Video Duration:</span>
              <span ref={debugDurationRef} className="text-white/70">{duration ? `${duration.toFixed(2)}s` : 'loading...'}</span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
