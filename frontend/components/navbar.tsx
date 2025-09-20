import Link from "next/link";
import {Brain} from "lucide-react";
import Image from "next/image";
import { Button } from "./ui/button";

export default async function Navbar() {
    return ( 
        <div className="w-full py-6 px-24 flex justify-between border-underline border-b">
            <Link href="../(auth-pages)" className="flex gap-4 items-center">
                <Brain size={36} />
                <p className="text-xl font-bold">Name</p>
            </Link>
            <div className="flex items-center gap-8">
                <div className="text-black dark:text-white sm:flex hidden items-center">
                    <Button variant="default" className="text-lg font-bold">Sign Up</Button>
                </div>
            </div>
        </div>
    )

}