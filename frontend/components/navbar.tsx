'use client';
import Link from "next/link";
import Image from "next/image";
import { Button } from "./ui/button";
import { useAuth } from "@/api/authContext";
import { AddSourceDialog } from "./add-source-dialog";

export default function Navbar() {
    const { user, token, logout } = useAuth();

    const handleSourceAdded = () => {
        // A simple way to see the result is to reload the page.
        // A more advanced implementation might re-fetch data without a full reload.
        window.location.reload();
    };

    return ( 
        <div className="w-full py-6 px-24 flex justify-between border-underline border-b">
            <Link href="/" className="flex gap-4 items-center">
                <Image
                    src="/feedstream.png"
                    alt="The FeedStream logo"
                    width={40}
                    height={40}
                />
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
                        
                        <AddSourceDialog onSourceAdded={handleSourceAdded}>
                            <Button variant="outline" className="text-lg font-bold">Add Source</Button>
                        </AddSourceDialog>

                        <div className="text-black dark:text-white sm:flex hidden items-center">
                            <Button variant="default" className="text-lg font-bold hover:bg-gray-600" onClick={logout}>
                                Logout
                            </Button>
                        </div>
                    </>
                ) : (
                    <>
                    <div className="text-black dark:text-white sm:flex hidden items-center">
                        <Link href="/sign-in">
                            <Button variant="default" className="text-lg font-bold hover:bg-gray-600">Sign Up</Button>
                        </Link>
                    </div>
                </>
                )}
            </div>
        </div>
    )

}