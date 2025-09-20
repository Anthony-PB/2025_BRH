import type { Metadata } from "next";
import "./globals.css";
import Navbar from "@/components/navbar";

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
      <body className="bg-white text-[#0C0D0D]">
        <Navbar />
        <main className="min-h-screen">{children}</main>
      </body>
    </html>
  );
}
