import type { Metadata } from "next";
import { Cinzel, Montserrat } from "next/font/google";
import "./globals.css";

const cinzel = Cinzel({
  variable: "--font-cinzel",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700", "800"],
});

const montserrat = Montserrat({
  variable: "--font-montserrat",
  subsets: ["latin", "vietnamese"],
  weight: ["300", "400", "500", "600"],
});

export const metadata: Metadata = {
  title: "Saigon Farm Resort - Tuyệt Tác Điền Trang Nghỉ Dưỡng Sinh Thái",
  description: "Một miền sống được dệt từ đất, nước và ký ức Việt.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="vi" className={`${cinzel.variable} ${montserrat.variable}`}>
      <body className="bg-black text-[#f4ede4] antialiased selection:bg-[#d4af37]/30 selection:text-white">
        {children}
      </body>
    </html>
  );
}
