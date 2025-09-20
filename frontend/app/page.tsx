
import { ArrowRight, FileText, LogIn } from "lucide-react";
import { dbConnectionStatus } from "@/db/connection-status";
import { Card, CardContent, CardDescription, CardHeader, CardTitle} from '@/components/ui/card';
import { Button } from "@/components/ui/button";
import {CardCell, CardImage } from "@/components/ui/cardCell";
import Image from "next/image";

export default async function Home() {
  const result = await dbConnectionStatus();
  return (
    <div className="flex min-h-screen flex-col">
      <div className="mx-auto flex w-full max-w-lg flex-1 flex-col px-5 lg:max-w-5xl gap-12">
        <div className="flex justify-center mt-20 text-4xl font-bold">
          Brand Name
        </div>
        <div className="flex justify-center text-xl">
          Description of the website
        </div> 
        <CardCell> 
          <CardImage>
            <Image
              src="/talking.png"
              alt="Some alt text"
              width={400}
              height={250}
              className="w-full h-48 object-cover"
            />
          </CardImage>
          <CardHeader>
            <CardTitle>Title</CardTitle>
            <CardDescription>Description of article</CardDescription>
          </CardHeader>
        </CardCell>
      </div>
    </div>
  );
}
