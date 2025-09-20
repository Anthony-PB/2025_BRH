"use client"

import { useState } from "react"
import { ChevronDown } from "lucide-react"

interface NewsProvider {
  id: number
  name: string
  brandClass: string
  category: string
  popularity: number
  dateAdded: string
}

const newspaperProviders: NewsProvider[] = [
  {
    id: 1,
    name: "The New York Times",
    brandClass: "nyt-brand",
    category: "General News",
    popularity: 95,
    dateAdded: "2024-01-15",
  },
  {
    id: 2,
    name: "The Wall Street Journal",
    brandClass: "wsj-brand",
    category: "Business",
    popularity: 92,
    dateAdded: "2024-01-20",
  },
  {
    id: 3,
    name: "The Washington Post",
    brandClass: "wapo-brand",
    category: "Politics",
    popularity: 88,
    dateAdded: "2024-01-18",
  },
  {
    id: 4,
    name: "USA Today",
    brandClass: "usa-brand",
    category: "General News",
    popularity: 75,
    dateAdded: "2024-01-22",
  },
  {
    id: 5,
    name: "The Guardian",
    brandClass: "guardian-brand",
    category: "International",
    popularity: 85,
    dateAdded: "2024-01-16",
  },
  {
    id: 6,
    name: "Financial Times",
    brandClass: "ft-brand",
    category: "Business",
    popularity: 90,
    dateAdded: "2024-01-19",
  },
  {
    id: 7,
    name: "Reuters",
    brandClass: "reuters-brand",
    category: "International",
    popularity: 87,
    dateAdded: "2024-01-21",
  },
  {
    id: 8,
    name: "Associated Press",
    brandClass: "ap-brand",
    category: "General News",
    popularity: 82,
    dateAdded: "2024-01-17",
  },
  {
    id: 9,
    name: "Bloomberg",
    brandClass: "bloomberg-brand",
    category: "Business",
    popularity: 89,
    dateAdded: "2024-01-23",
  },
  { id: 10, name: "CNN", brandClass: "cnn-brand", category: "Politics", popularity: 78, dateAdded: "2024-01-24" },
]

type FilterType = "all" | "recent" | "popular"
type CategoryType = "all" | "General News" | "Business" | "Politics" | "International"

export default function FilterSidebar() {
  const [activeFilter, setActiveFilter] = useState<FilterType>("all")
  const [selectedCategory, setSelectedCategory] = useState<CategoryType>("all")
  const [showCategoryDropdown, setShowCategoryDropdown] = useState(false)

  const getFilteredProviders = () => {
    let filtered = [...newspaperProviders]

    // Filter by category
    if (selectedCategory !== "all") {
      filtered = filtered.filter((provider) => provider.category === selectedCategory)
    }

    // Apply sorting based on active filter
    switch (activeFilter) {
      case "recent":
        filtered.sort((a, b) => new Date(b.dateAdded).getTime() - new Date(a.dateAdded).getTime())
        break
      case "popular":
        filtered.sort((a, b) => b.popularity - a.popularity)
        break
      default:
        // Keep original order for "all"
        break
    }

    return filtered
  }

  const filteredProviders = getFilteredProviders()
  const categories: CategoryType[] = ["all", "General News", "Business", "Politics", "International"]

  return (
    <div className="w-64 max-w-sm mx-auto px-4 py-8">
      <div className="bg-card border rounded-lg p-6">
        <h3 className="text-lg font-semibold mb-4 text-foreground">Filters</h3>

        {/* Filter Options */}
        <div className="space-y-3 mb-6">
          <button
            onClick={() => setActiveFilter("all")}
            className={`w-full text-left px-3 py-2 rounded-md transition-colors ${
              activeFilter === "all"
                ? "bg-primary text-primary-foreground"
                : "hover:bg-muted text-muted-foreground hover:text-foreground"
            }`}
          >
            All Sources
          </button>
          <button
            onClick={() => setActiveFilter("recent")}
            className={`w-full text-left px-3 py-2 rounded-md transition-colors ${
              activeFilter === "recent"
                ? "bg-primary text-primary-foreground"
                : "hover:bg-muted text-muted-foreground hover:text-foreground"
            }`}
          >
            Recent
          </button>
          <button
            onClick={() => setActiveFilter("popular")}
            className={`w-full text-left px-3 py-2 rounded-md transition-colors ${
              activeFilter === "popular"
                ? "bg-primary text-primary-foreground"
                : "hover:bg-muted text-muted-foreground hover:text-foreground"
            }`}
          >
            Popular
          </button>
        </div>

        {/* Category Dropdown */}
        <div className="relative">
          <label className="text-sm font-medium text-foreground mb-2 block">Category</label>
          <button
            onClick={() => setShowCategoryDropdown(!showCategoryDropdown)}
            className="w-full flex items-center justify-between px-3 py-2 bg-background border rounded-md hover:bg-muted transition-colors"
          >
            <span className="text-sm">{selectedCategory === "all" ? "All Categories" : selectedCategory}</span>
            <ChevronDown className={`w-4 h-4 transition-transform ${showCategoryDropdown ? "rotate-180" : ""}`} />
          </button>

          {showCategoryDropdown && (
            <div className="absolute top-full left-0 right-0 mt-1 bg-popover border rounded-md shadow-lg z-10">
              {categories.map((category) => (
                <button
                  key={category}
                  onClick={() => {
                    setSelectedCategory(category)
                    setShowCategoryDropdown(false)
                  }}
                  className={`w-full text-left px-3 py-2 text-sm hover:bg-muted transition-colors first:rounded-t-md last:rounded-b-md ${
                    selectedCategory === category ? "bg-muted" : ""
                  }`}
                >
                  {category === "all" ? "All Categories" : category}
                </button>
              ))}
            </div>
          )}
        </div>

        <div className="mt-6 pt-4 border-t">
          <p className="text-sm text-muted-foreground">
            {filteredProviders.length} source{filteredProviders.length !== 1 ? "s" : ""} found
          </p>
        </div>
      </div>
    </div>
  )
}
