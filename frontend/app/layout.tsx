import type { Metadata } from "next";
import "./globals.css";
import Navbar from "@/components/navbar";
import { Brain } from "lucide-react";


export const metadata: Metadata = {
  title: "Next.js + MongoDB",
  description: "Use MongoDB with Next.js",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="bg-beigebackground text-[#0C0D0D]">
        <Navbar/>
        <main className="min-h-screen">{children}</main>
        <footer className="mt-20 mb-12 w-full flex justify-center">
        <div className="flex flex-row items-center gap-4 text-center">
          <div className="text-xl">Made with</div>
          <Brain size={36} />
        </div>
      </footer>
      </body>
    </html>
  );
}
