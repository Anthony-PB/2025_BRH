import { dbConnectionStatus } from "@/db/connection-status";
import { CardDescription, CardHeader, CardTitle} from '@/components/ui/card';
import {CardCell, CardImage } from "@/components/ui/cardCell";
import Image from "next/image";
import ProviderCarousel from "@/components/provider-carousel"

export default async function Home() {
  const result = await dbConnectionStatus();
  return (
    <div className="flex min-h-screen flex-col">
      <div className="mx-auto flex w-full max-w-lg flex-1 flex-col px-5 lg:max-w-7xl gap-12">
        <div className="flex justify-center mt-20 text-4xl font-bold">
          Brand Name
        </div>
        <div className="flex justify-center text-xl">
          Description of the website
        </div> 
        <CardCell> 
          <CardImage>
            <Image
              src="/browse.png"
              alt="Some alt text"
              width={400}
              height={800}
              className="w-full h-100 object-cover rounded-t-lg border-2"
            />
          </CardImage>
        </CardCell>
        <ProviderCarousel/>
        <div className="max-w-full flex gap-12 overflow-y-none mt-16 mb-4">          
          <Image
            src="/reading_newspaper.png"
            alt="Some alt text"
            width={640}
            height={480}
            className="border-highlight border-2 rounded-lg shadow-xl w-1/2"
          />
          <div className="flex flex-col justify-center gap-12 w-1/2">
            <div className="flex flex-col gap-4">
              <h2 className="text-5xl font-semibold whitespace-pre-line">Get All In One </h2>
              <p className="text-xl">Stay up to date with all your favorite news sites.</p>
            </div>
          </div>
        </div>
        <div className="max-w-full flex gap-12 overflow-y-none mt-20">          
          <div className="flex flex-col justify-center gap-12 w-1/2">
            <div className="flex flex-col gap-4">
              <h2 className="text-5xl font-semibold whitespace-pre-line">Get All In One </h2>
              <p className="text-xl">Stay up to date with all your favorite news sites.</p>
            </div>
          </div>
          <Image
            src="/mult.png"
            alt="Some alt text"
            width={640}
            height={480}
            className="border-highlight border-2 rounded-lg shadow-xl w-1/2"
          />
        </div>
      </div>
    </div>
    
  );
}
