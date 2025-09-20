"use client"

import { useEffect, useState } from "react"
import { Card } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { ChevronLeft, ChevronRight, Star, MapPin } from "lucide-react"

interface Provider {
  id: number
  name: string
  category: string
  rating: number
  location: string
  description: string
  isNew: boolean
  joinedDate: string
}

const dailyProviders: Provider[] = [
  {
    id: 1,
    name: "TechFlow Solutions",
    category: "Software Development",
    rating: 4.9,
    location: "San Francisco, CA",
    description: "Full-stack development and cloud solutions for modern businesses",
    isNew: true,
    joinedDate: "Today",
  },
  {
    id: 2,
    name: "Creative Design Studio",
    category: "UI/UX Design",
    rating: 4.8,
    location: "New York, NY",
    description: "Award-winning design team specializing in user experience",
    isNew: true,
    joinedDate: "Today",
  },
  {
    id: 3,
    name: "DataViz Analytics",
    category: "Data Science",
    rating: 4.7,
    location: "Austin, TX",
    description: "Advanced analytics and machine learning solutions",
    isNew: true,
    joinedDate: "Today",
  },
  {
    id: 4,
    name: "CloudSecure Pro",
    category: "Cybersecurity",
    rating: 4.9,
    location: "Seattle, WA",
    description: "Enterprise-grade security solutions and consulting",
    isNew: true,
    joinedDate: "Today",
  },
  {
    id: 5,
    name: "Mobile First Labs",
    category: "Mobile Development",
    rating: 4.6,
    location: "Los Angeles, CA",
    description: "Native and cross-platform mobile app development",
    isNew: true,
    joinedDate: "Today",
  },
  {
    id: 6,
    name: "AI Innovation Hub",
    category: "Artificial Intelligence",
    rating: 4.8,
    location: "Boston, MA",
    description: "Cutting-edge AI solutions and automation services",
    isNew: true,
    joinedDate: "Today",
  },
]

export default function ProviderCarousel() {
  const [currentIndex, setCurrentIndex] = useState(0)
  const [isHovered, setIsHovered] = useState(false)
  const [visibleCards, setVisibleCards] = useState(3)

  // Adjust visible cards based on screen size
  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth < 768) {
        setVisibleCards(1)
      } else if (window.innerWidth < 1024) {
        setVisibleCards(2)
      } else {
        setVisibleCards(3)
      }
    }

    handleResize()
    window.addEventListener("resize", handleResize)
    return () => window.removeEventListener("resize", handleResize)
  }, [])

  // Auto-rotate carousel
  useEffect(() => {
    if (!isHovered) {
      const interval = setInterval(() => {
        setCurrentIndex((prevIndex) => (prevIndex + 1) % dailyProviders.length)
      }, 3000)

      return () => clearInterval(interval)
    }
  }, [isHovered])

  const nextSlide = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % dailyProviders.length)
  }

  const prevSlide = () => {
    setCurrentIndex((prevIndex) => (prevIndex === 0 ? dailyProviders.length - 1 : prevIndex - 1))
  }

  const getVisibleProviders = () => {
    const providers = []
    for (let i = 0; i < visibleCards; i++) {
      const index = (currentIndex + i) % dailyProviders.length
      providers.push(dailyProviders[index])
    }
    return providers
  }

  return (
    <div className="w-full max-w-7xl mx-auto px-4 py-8">
      <div className="text-center mb-8">
        <h2 className="text-3xl font-bold text-foreground mb-2 text-balance">Daily New Providers</h2>
        <p className="text-muted-foreground text-lg">Discover the latest professionals who joined our platform today</p>
      </div>

      <div className="relative" onMouseEnter={() => setIsHovered(true)} onMouseLeave={() => setIsHovered(false)}>
        {/* Navigation Arrows */}
        <button
          onClick={prevSlide}
          className="absolute left-0 top-1/2 -translate-y-1/2 z-10 bg-muted hover:bg-primary text-muted-foreground hover:text-primary-foreground rounded-full p-2 shadow-lg transition-all duration-200 hover:scale-110"
          aria-label="Previous providers"
        >
          <ChevronLeft className="w-5 h-5" />
        </button>

        <button
          onClick={nextSlide}
          className="absolute right-0 top-1/2 -translate-y-1/2 z-10 bg-muted hover:bg-primary text-muted-foreground hover:text-primary-foreground rounded-full p-2 shadow-lg transition-all duration-200 hover:scale-110"
          aria-label="Next providers"
        >
          <ChevronRight className="w-5 h-5" />
        </button>

        {/* Carousel Container */}
        <div className="overflow-hidden mx-12">
          <div
            className="flex transition-transform duration-500 ease-in-out gap-6"
            style={{
              transform: `translateX(-${currentIndex * (100 / visibleCards)}%)`,
            }}
          >
            {dailyProviders.map((provider) => (
              <div key={provider.id} className="flex-shrink-0" style={{ width: `${100 / visibleCards}%` }}>
                <Card className="h-full bg-card border-border hover:shadow-lg transition-all duration-300 hover:scale-105 p-6">
                  <div className="flex items-start justify-between mb-4">
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-2">
                        <h3 className="font-semibold text-card-foreground text-lg">{provider.name}</h3>
                        {provider.isNew && (
                          <Badge variant="secondary" className="bg-primary text-primary-foreground text-xs">
                            NEW
                          </Badge>
                        )}
                      </div>
                      <p className="text-primary font-medium text-sm mb-1">{provider.category}</p>
                      <div className="flex items-center gap-4 text-sm text-muted-foreground mb-3">
                        <div className="flex items-center gap-1">
                          <Star className="w-4 h-4 fill-yellow-400 text-yellow-400" />
                          <span>{provider.rating}</span>
                        </div>
                        <div className="flex items-center gap-1">
                          <MapPin className="w-4 h-4" />
                          <span>{provider.location}</span>
                        </div>
                      </div>
                    </div>
                  </div>

                  <p className="text-muted-foreground text-sm leading-relaxed mb-4">{provider.description}</p>

                  <div className="flex items-center justify-between">
                    <span className="text-xs text-muted-foreground">Joined {provider.joinedDate}</span>
                    <button className="text-primary hover:text-primary/80 text-sm font-medium transition-colors">
                      View Profile →
                    </button>
                  </div>
                </Card>
              </div>
            ))}
          </div>
        </div>

        {/* Dots Indicator */}
        <div className="flex justify-center mt-6 gap-2">
          {dailyProviders.map((_, index) => (
            <button
              key={index}
              onClick={() => setCurrentIndex(index)}
              className={`w-2 h-2 rounded-full transition-all duration-200 ${
                index === currentIndex ? "bg-primary w-6" : "bg-muted-foreground/30 hover:bg-muted-foreground/50"
              }`}
              aria-label={`Go to slide ${index + 1}`}
            />
          ))}
        </div>
      </div>
    </div>
  )
}
