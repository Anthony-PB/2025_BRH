'use client'; // Step 1: Mark as a client component
import { useState, useEffect } from 'react'; 
import { CardCell, CardHeader, CardTitle, CardContent, CardImage } from '@/components/ui/cardCell';
import FilterSideBar from "@/components/filtersidebar";
import Searchbar from "@/components/searchbar";
import { getSourceArticles } from '@/api/sources';

interface Article {
  title: string;
  link: string;
  date_published: string;
  aggregated_at: string;
  image_url: string | null;
}

interface ApiResponse {
  results: Article[];
}

export default function Browse() {

  const [sourceData, setSourceData] = useState<ApiResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await getSourceArticles("68cfa96ea07e358109b0dccd");
        setSourceData(data);
      } catch (err) {
        setError("Failed to load articles.");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []); // The empty [] means this runs once when the component loads

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div className="flex min-h-screen flex-col gap-8">
      <div className="flex justify-center text-4xl font-bold mt-16">Browse</div>
      <div className='flex justify-center'><Searchbar/></div>
      <div className="flex flex-row w-full h-[calc(100vh-100px)] mt-6 px-5 gap-8">
        {/* Sidebar */}
        <div className="w-64 shrink-0">
          <FilterSideBar />
        </div>

        <div className="flex-1 overflow-y-auto">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 auto-rows-[300px] gap-8 pr-2">
            {sourceData.results?.map((article, i) => (
              <CardCell key={i} className="max-h-full flex flex-col">
                <CardImage>
                  <img 
                    src={article.image_url ?? "/talking.png"} 
                    alt={article.title} 
                    className="w-full h-48 object-cover rounded-t-lg"
                  />
                </CardImage>
                <CardHeader className="flex-shrink-0">
                  <CardTitle className="text-lg font-semibold line-clamp-3 leading-tight mb-0">
                    {article.title}
                  </CardTitle>
                </CardHeader>
                <CardContent className="flex-1 flex flex-col justify-between">
                  <div className="text-sm text-gray-600 mb-2">
                    Published: {formatDate(article.date_published)}
                  </div>
                  <a 
                    href={article.link} 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="mt-auto bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors text-center"
                  >
                    Read Article
                  </a>
                </CardContent>
              </CardCell>
            )) || []}
          </div>
        </div>
      </div>
    </div>
  );
}