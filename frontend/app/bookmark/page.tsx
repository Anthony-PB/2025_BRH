'use client';
import React from "react";
import Group from "@/components/group";
import { useAuth } from "@/api/authContext";
import { useRouter } from "next/navigation";
import { useEffect } from "react";

export default function Bookmark() {
    const { token, loading: authLoading } = useAuth();
    const router = useRouter();

    useEffect(() => {
        if (!authLoading && !token) {
            router.push('/');
        }
    }, [token, authLoading, router]);

    // Mock data to show how it would look
    const mockGroups = [
        {
            title: "Tech News",
            description: "Latest technology and startup news",
            memberCount: 1247,
            sourcesIn: ["TechCrunch", "Hacker News", "The Verge", "Ars Technica"]
        },
        {
            title: "AI & Machine Learning",
            description: "Cutting-edge AI research and applications",
            memberCount: 892,
            sourcesIn: ["OpenAI Blog", "Anthropic", "DeepMind", "Papers With Code"]
        },
        {
            title: "Web Development",
            description: "Frontend, backend, and full-stack development",
            memberCount: 2156,
            sourcesIn: ["CSS-Tricks", "Smashing Magazine", "Dev.to", "MDN Docs"]
        },
        {
            title: "Design Inspiration",
            description: "UI/UX design trends and inspiration",
            memberCount: 634,
            sourcesIn: ["Dribbble", "Behance", "Awwwards", "UX Planet"]
        }
    ];

    if (authLoading || !token) {
        return (
            <div className="flex min-h-screen flex-col gap-8">
                <div className="flex justify-center text-4xl font-bold mt-16">Loading...</div>
            </div>
        );
    }

    return (
        <div className="w-full py-6 px-24 flex flex-col gap-8">
            <div className="space-y-2">
                <h1 className="text-4xl font-bold text-gray-900">Your Bookmarks</h1>
                <p className="text-gray-600">Organize your content sources into groups</p>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {mockGroups.map((group, index) => (
                    <Group 
                        key={index}
                        title={group.title}
                        description={group.description}
                        sourceCount={group.sourcesIn.length}
                        sourcesIn={group.sourcesIn}
                    />
                ))}
            </div>
        </div>
    );
}