import React from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle} from '@/components/ui/card';
import { CardCell, CardImage } from "@/components/ui/cardCell";
import Image from "next/image";

export default async function Bookmark() {
    return (
        <div className="flex min-h-screen flex-col">
      <div className="mx-auto flex w-full max-w-lg flex-1 flex-col px-5 lg:max-w-5xl gap-12">
        <div className="flex flex-row gap-6">
          <CardCell className="mt-20 w-full"> 
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
          <CardCell className="mt-20 w-full"> 
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
    </div>
        )   
    ;
    }