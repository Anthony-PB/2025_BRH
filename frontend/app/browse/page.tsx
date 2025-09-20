import { Card, CardContent, CardDescription, CardHeader, CardTitle} from '@/components/ui/card';
import FilterSideBar from "@/components/filtersidebar";
import Searchbar from "@/components/searchbar"

export default async function Browse() {
  return (
    <div className="flex min-h-screen flex-col gap-8">
      <div className="flex justify-center text-4xl font-bold mt-16">Browse</div>
      <div className='flex justify-center'><Searchbar/></div>
      <div className="flex flex-row w-full h-[calc(100vh-100px)] mt-6 px-5 gap-8">
        {/* Sidebar */}
        <div className="w-64 shrink-0">
          <FilterSideBar />
        </div>

        {/* Cards grid */}
        <div className="flex-1 overflow-y-auto">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 auto-rows-[300px] gap-8 pr-2">
            {Array.from({ length: 18 }).map((_, i) => (
              <Card key={i} className="max-h-full" />
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}