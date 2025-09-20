import {Card, CardContent, CardFooter} from "@/components/ui/card";

export default async function Browse() {
    return (
        <div className="flex min-h-screen flex-col ">
            <div className="mx-auto flex w-full max-w-lg flex-1 flex-col px-5 lg:max-w-5xl">
                <Card className="mt-20 w-full">
                    <CardContent className="bg-gray-100 flex justify-center items-center ">
                        <div className="text-2xl font-bold">Browse</div>
                    </CardContent>
                    
                </Card>
            </div>
        </div>
        )
    ;
    }