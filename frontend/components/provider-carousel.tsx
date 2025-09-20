"use client"

import { useEffect, useState } from "react"

interface NewsProvider {
  id: number
  name: string
  brandClass: string // Added brand-specific CSS class
}

const newspaperProviders: NewsProvider[] = [
  { id: 1, name: "The New York Times", brandClass: "nyt-brand" },
  { id: 2, name: "The Wall Street Journal", brandClass: "wsj-brand" },
  { id: 3, name: "The Washington Post", brandClass: "wapo-brand" },
  { id: 4, name: "USA Today", brandClass: "usa-brand" },
  { id: 5, name: "The Guardian", brandClass: "guardian-brand" },
  { id: 6, name: "Financial Times", brandClass: "ft-brand" },
  { id: 7, name: "Reuters", brandClass: "reuters-brand" },
  { id: 8, name: "Associated Press", brandClass: "ap-brand" },
  { id: 9, name: "Bloomberg", brandClass: "bloomberg-brand" },
  { id: 10, name: "CNN", brandClass: "cnn-brand" },
]

export default function ProviderCarousel() {
  const [currentIndex, setCurrentIndex] = useState(0)
  const [isHovered, setIsHovered] = useState(false)

  // Auto-rotate carousel
  useEffect(() => {
    if (!isHovered) {
      const interval = setInterval(() => {
        setCurrentIndex((prevIndex) => (prevIndex + 1) % newspaperProviders.length)
      }, 2000) // Slightly slower for smoother feel

      return () => clearInterval(interval)
    }
  }, [isHovered])

  const getVisibleProviders = () => {
    const providers = []
    for (let i = 0; i < 4; i++) {
      const index = (currentIndex + i) % newspaperProviders.length
      providers.push(newspaperProviders[index])
    }
    return providers
  }

  return (
    <div className="w-full max-w-6xl mx-auto px-4 py-8 bg-beigebackground">
      <div className="text-center mb-8">
        <h2 className="text-3xl font-serif font-bold text-foreground mb-2 text-balance">Featured News Sources</h2>
        <p className="text-muted-foreground text-lg">Articles from trusted news providers</p>
      </div>

      <div
        className="relative overflow-hidden rounded-lg py-6"
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
      >
        <div className="flex items-center justify-center">
          <div className="flex gap-8 transition-all duration-500 ease-out transform-gpu will-change-transform">
            {getVisibleProviders().map((provider, index) => (
              <div
                key={`${provider.id}-${currentIndex}-${index}`}
                className="text-center px-6 py-2 transition-opacity duration-500 ease-out"
              >
                <h3
                  className={`text-xl font-semibold whitespace-nowrap ${provider.brandClass} transition-all duration-300`}
                >
                  {provider.name}
                </h3>
              </div>
            ))}
          </div>
        </div>

        <div className="flex justify-center mt-4 gap-1">
          {newspaperProviders.map((_, index) => (
            <div
              key={index}
              className={`w-1.5 h-1.5 rounded-full transition-all duration-300 ease-out transform-gpu ${
                index === currentIndex ? "bg-primary scale-110" : "bg-muted-foreground/30 scale-100"
              }`}
            />
          ))}
        </div>
      </div>
    </div>
  )
}