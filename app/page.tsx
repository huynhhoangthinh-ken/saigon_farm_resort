import CinematicHero from "@/components/sfr/CinematicHero";

export default function Home() {
  return (
    <main className="relative min-h-screen bg-black">
      {/* 1. Cinematic Scroll Hero Section */}
      <CinematicHero />

      {/* 2. Placeholder Section After Hero */}
      <section className="relative z-10 min-h-screen bg-[#07130f] border-t border-[#d4af37]/20 flex flex-col items-center justify-center text-center px-6 py-24">
        <div className="max-w-2xl mx-auto flex flex-col items-center">
          <div className="w-12 h-1 bg-gradient-to-r from-transparent via-[#d4af37] to-transparent mb-8" />
          <span className="text-xs md:text-sm tracking-[0.3em] uppercase text-[#d4af37] font-medium mb-3">
            Khám Phá Tiếp Theo
          </span>
          <h2 className="font-['Cinzel',serif] text-3xl md:text-5xl tracking-[0.15em] font-semibold text-white uppercase mb-6">
            SAIGON FARM RESORT — NEXT CHAPTER
          </h2>
          <p className="font-['Montserrat',sans-serif] text-sm md:text-base text-[#9ca3af] font-light leading-relaxed max-w-lg mb-8">
            Không gian này sẽ tiếp nối dòng chảy câu chuyện kiến trúc, văn hóa và hệ sinh thái điền trang ven hồ 100ha.
          </p>
          <div className="px-6 py-2.5 rounded-full border border-white/10 bg-white/5 text-xs text-white/60 tracking-wider">
            Cuộn ngược lên trên để tương tác lại với thước phim cinematic
          </div>
        </div>
      </section>
    </main>
  );
}
