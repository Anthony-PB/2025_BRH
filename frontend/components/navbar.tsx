import Link from "next/link";
import {Brain} from "lucide-react";
import Image from "next/image";
import { Button } from "./ui/button";

export default async function Navbar() {
    return ( 
        <div className="w-full py-6 px-24 flex justify-between border-underline border-b">
            <Link href="/" className="flex gap-4 items-center">
                <Brain size={36} />
                <p className="text-xl font-bold">Name</p>
            </Link>
            <div className="flex items-center gap-12">
                <Link  href="/browse" className="text-black font-bold text-xl hover:text-gray-600">Browse</Link>
                <Link href="/bookmark" className="text-black font-bold text-xl hover:text-gray-600">Bookmark</Link>
                <div className="text-black dark:text-white sm:flex hidden items-center">
                    <a href="/sign-in">
                        <Button variant="default" className="text-lg font-bold hover:bg-gray-600">Sign Up</Button>
                    </a>
                </div>
            </div>
        </div>
    )

}