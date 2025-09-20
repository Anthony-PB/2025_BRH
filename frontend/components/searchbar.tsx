"use client"

import { Search } from "lucide-react"

export default function Searchbar() {
  return (
    <div className="flex flex-row gap-2 relative w-full max-w-lg lg:max-w-5xl">
        <Search className="ml-3 mt-4 text-black"/>
        <input
        type="text"
        placeholder="Search..."
        className="w-full border-1 rounded-lg max-w-lg lg:max-w-5xl border-black focus:border-blue-600 rounded-t-2xl text-xl px-4 py-3 outline-none"
        />
    </div>
  )
}