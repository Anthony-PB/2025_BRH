'use client';
import Link from "next/link";
import {Brain} from "lucide-react";
import { Button } from "./ui/button";
import { useAuth } from "@/api/authContext";

export default function Navbar() {
    const { user, token, logout } = useAuth();

    return ( 
        <div className="w-full py-6 px-24 flex justify-between border-underline border-b">
            <Link href="/" className="flex gap-4 items-center">
                <Brain size={36} />
                <p className="text-xl font-bold">FeedStream</p>
            </Link>
            <div className="flex items-center gap-12">
               {user && (
                    <p className="text-black font-bold text-xl">Welcome, {user.display_name}!</p>
                )}
                
                {token ? (
                    <> 
                        <Link  href="/browse" className="text-black font-bold text-xl hover:text-gray-600">Browse</Link>
                        <Link href="/bookmark" className="text-black font-bold text-xl hover:text-gray-600">Bookmarks</Link>
                        <div className="text-black dark:text-white sm:flex hidden items-center">
                            <Button variant="default" className="text-lg font-bold hover:bg-gray-600" onClick={logout}>
                                Logout
                            </Button>
                        </div>
                    </>
                ) : (
                    <>
                    <div className="text-black dark:text-white sm:flex hidden items-center">
                        <a href="/sign-in">
                            <Button variant="default" className="text-lg font-bold hover:bg-gray-600">Sign Up</Button>
                        </a>
                    </div>
                </>
                )}
            </div>
        </div>
    )

}