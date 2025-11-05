'use client';
import Link from "next/link";
import Image from "next/image";
import { Button } from "./ui/button";
import { useAuth } from "@/api/authContext";
import { AddSourceDialog } from "./add-source-dialog";
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuTrigger,
    DropdownMenuSeparator,
} from "@/components/ui/dropdown-menu";
import { CircleUserRound } from "lucide-react";
import { DropdownMenuLabel } from "@radix-ui/react-dropdown-menu";
import { useState } from "react";

export default function Navbar() {
    const { user, token, logout } = useAuth();
    const [isAddSourceDialogOpen, setIsAddSourceDialogOpen] = useState(false);

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
                {token ? (
                    <> 
                        <Link  href="/browse" className="text-black font-bold text-xl hover:text-gray-600">Browse</Link>
                        <Link href="/bookmark" className="text-black font-bold text-xl hover:text-gray-600">Bookmarks</Link>

                        <AddSourceDialog 
                            open={isAddSourceDialogOpen} 
                            onOpenChange={setIsAddSourceDialogOpen} 
                            onSourceAdded={handleSourceAdded} 
                        />
                        <DropdownMenu>
                            <DropdownMenuTrigger asChild>
                                <Button variant="ghost" className="relative h-15 w-15 rounded-full">
                                    <CircleUserRound size="20" strokeWidth="2"/>
                                </Button>
                            </DropdownMenuTrigger>
                            <DropdownMenuContent className="w-56" align="end" forceMount>
                                <DropdownMenuLabel>
                                    {user && (
                                        <p className="px-1 text-black font-bold text-l">Hello, {user.display_name}!</p>
                                    )}
                                </DropdownMenuLabel>
                                <DropdownMenuSeparator />
                                <DropdownMenuItem onSelect={() => setIsAddSourceDialogOpen(true)}>
                                    Add Source
                                </DropdownMenuItem>
                                <DropdownMenuItem onClick={logout}>
                                    Log out
                                </DropdownMenuItem>
                            </DropdownMenuContent>
                        </DropdownMenu>
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