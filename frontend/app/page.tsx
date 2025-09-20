
import { ArrowRight, FileText, LogIn } from "lucide-react";
import { dbConnectionStatus } from "@/db/connection-status";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from "@/components/ui/button";

export default async function Home() {
  const result = await dbConnectionStatus();
  return (
    <div className="flex min-h-screen flex-col">
      <div className="mx-auto flex w-full max-w-lg flex-1 flex-col px-5 lg:max-w-5xl">
        <div className="flex flex-row gap-6">
          <Card className="mt-20 w-full">
            <CardHeader className="flex flex-row items-center justify-between">
              <div>
                <CardTitle>Title</CardTitle>
                <CardDescription>Description of article</CardDescription>
              </div>
            </CardHeader>
            <CardContent className="bg-gray-100">
              <div className="text-2xl font-bold">Image</div>
            </CardContent>
          </Card>
          <Card className="mt-20 w-full">
            <CardHeader className="flex flex-row items-center justify-between">
              <div>
                <CardTitle>Title</CardTitle>
                <CardDescription>Description of article</CardDescription>
              </div>
            </CardHeader>
            <CardContent className="bg-gray-100">
              <div className="text-2xl font-bold">Image</div>
            </CardContent>
          </Card>
          </div>
      </div>
    </div>
  );
}
