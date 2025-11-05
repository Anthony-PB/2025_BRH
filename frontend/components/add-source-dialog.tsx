"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { createSource } from "@/api/sources";

interface AddSourceDialogProps {
  children: React.ReactNode;
  onSourceAdded: () => void;
}

export function AddSourceDialog({ children, onSourceAdded }: AddSourceDialogProps) {
  const [open, setOpen] = useState(false);
  const [name, setName] = useState("");
  const [url, setUrl] = useState("");
  const [category, setCategory] = useState("");
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);

    if (!name || !url || !category) {
      setError("All fields are required.");
      return;
    }

    const sourceData = {
      name,
      url,
      category,
      is_rss: true, // Assuming true for now
    };

    const result = await createSource(sourceData);

    if (result.id) {
      onSourceAdded();
      setOpen(false);
      // Reset form
      setName("");
      setUrl("");
      setCategory("");
    } else {
      setError("Failed to create source. Please check the details.");
      console.error("Failed to create source:", result);
    }
  };

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>{children}</DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <form onSubmit={handleSubmit}>
          <DialogHeader>
            <DialogTitle>Add a New Source</DialogTitle>
            <DialogDescription>
              Enter the details for the new RSS feed or source you want to follow.
            </DialogDescription>
          </DialogHeader>
          <div className="grid gap-4 py-4">
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="name" className="text-right">
                Name
              </Label>
              <Input
                id="name"
                value={name}
                onChange={(e: React.ChangeEvent<HTMLInputElement>) => setName(e.target.value)}
                className="col-span-3"
                placeholder="e.g., TechCrunch"
              />
            </div>
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="url" className="text-right">
                URL
              </Label>
              <Input
                id="url"
                value={url}
                onChange={(e: React.ChangeEvent<HTMLInputElement>) => setUrl(e.target.value)}
                className="col-span-3"
                placeholder="e.g., https://techcrunch.com/feed/"
              />
            </div>
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="category" className="text-right">
                Category
              </Label>
              <Input
                id="category"
                value={category}
                onChange={(e: React.ChangeEvent<HTMLInputElement>) => setCategory(e.target.value)}
                className="col-span-3"
                placeholder="e.g., Technology"
              />
            </div>
          </div>
          {error && <p className="text-red-500 text-sm text-center pb-4">{error}</p>}
          <DialogFooter>
            <Button type="submit">Add Source</Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
}
